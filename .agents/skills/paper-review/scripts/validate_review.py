#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml",
# ]
# ///
"""Validate schema-v1 paper reviews."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml


REQUIRED_TOP_LEVEL = {
    "schema_version",
    "paper",
    "title",
    "authors",
    "publication",
    "reviewed_at",
    "canonical",
    "raw",
    "organizations",
    "artifacts",
    "facets",
    "assessment",
}

REQUIRED_PUBLICATION = {
    "first_public_date",
    "first_public_date_precision",
    "venue",
    "status",
    "reviewed_version",
    "reviewed_version_date",
}

REQUIRED_FACETS = {"domains", "paper_type", "methods", "models", "benchmarks"}
REQUIRED_ASSESSMENT = {
    "extract_quality",
    "extract_limitations",
    "critical_flags",
}

HEADINGS = [
    "What this paper is about",
    "Extended summary",
    "Learnings",
    "Verification",
    "Field context",
    "Critical discussion",
    "Relevance to us",
    "Claims",
]

ORG_ROLES = {
    "author_affiliation",
    "funder",
    "compute_provider",
    "data_provider",
    "collaborator",
}
SECTORS = {"academia", "industry", "government", "nonprofit", "other", "unknown"}
PUBLICATION_STATUSES = {
    "preprint",
    "workshop",
    "conference",
    "journal",
    "technical-report",
    "thesis",
    "other",
    "unknown",
}
PAPER_TYPES = {
    "method",
    "system",
    "benchmark",
    "analysis",
    "theory",
    "experiment",
    "survey",
    "position",
    "case-study",
    "dataset",
    "other",
}
ARTIFACT_TYPES = {"code", "data", "model", "benchmark", "project", "other"}
EXTRACT_QUALITIES = {"good", "partial", "poor"}
CRITICAL_FLAGS = {
    "weak-baseline",
    "missing-control",
    "same-family-judge",
    "circular-evaluation",
    "contamination-risk",
    "narrow-evaluation",
    "overclaim",
    "missing-uncertainty",
    "incomplete-reporting",
}
DATE_PATTERNS = {
    "day": re.compile(r"^\d{4}-\d{2}-\d{2}$"),
    "month": re.compile(r"^\d{4}-\d{2}$"),
    "year": re.compile(r"^\d{4}$"),
}


def require_mapping(value: Any, label: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{label} must be a mapping")
        return {}
    return value


def require_list(value: Any, label: str, errors: list[str]) -> list[Any]:
    if not isinstance(value, list):
        errors.append(f"{label} must be a list")
        return []
    return value


def check_allowed_strings(
    values: list[Any], allowed: set[str], label: str, errors: list[str]
) -> None:
    non_strings = [value for value in values if not isinstance(value, str)]
    if non_strings:
        errors.append(f"{label} must contain strings only")
    unknown = sorted(
        value for value in values if isinstance(value, str) and value not in allowed
    )
    if unknown:
        errors.append(f"{label} contains: {', '.join(unknown)}")


def validate_date(
    value: Any,
    precision: str,
    label: str,
    errors: list[str],
    *,
    allow_empty: bool = False,
) -> None:
    if value in (None, "") and allow_empty:
        return
    if not isinstance(value, str):
        errors.append(f"{label} must be a quoted string")
        return
    pattern = DATE_PATTERNS.get(precision)
    if pattern is None:
        errors.append(f"{label} has invalid precision {precision!r}")
    elif not pattern.fullmatch(value):
        errors.append(f"{label} must match {precision} precision, got {value!r}")


def parse_review(path: Path, errors: list[str]) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("missing opening YAML delimiter")
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        errors.append("missing closing YAML delimiter")
        return {}, text
    try:
        metadata = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError as exc:
        errors.append(f"invalid YAML: {exc}")
        return {}, text
    if not isinstance(metadata, dict):
        errors.append("frontmatter must be a mapping")
        metadata = {}
    return metadata, text[end + 5 :]


def validate_frontmatter(
    metadata: dict[str, Any], repo: Path, errors: list[str]
) -> None:
    missing = sorted(REQUIRED_TOP_LEVEL - metadata.keys())
    if missing:
        errors.append(f"missing frontmatter keys: {', '.join(missing)}")

    if metadata.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    paper = metadata.get("paper")
    if not isinstance(paper, str) or not re.fullmatch(
        r"(?:arxiv|slug|doi):\S+", paper
    ):
        errors.append("paper must be an arxiv:, slug:, or doi: identifier")

    if not isinstance(metadata.get("title"), str) or not metadata.get("title"):
        errors.append("title must be a non-empty string")

    authors = require_list(metadata.get("authors"), "authors", errors)
    if not authors or any(not isinstance(author, str) or not author for author in authors):
        errors.append("authors must contain non-empty strings")

    for path_key in ("canonical", "raw"):
        value = metadata.get(path_key)
        if not isinstance(value, str) or not value:
            errors.append(f"{path_key} must be a non-empty path")
        elif not (repo / value).exists():
            errors.append(f"{path_key} does not exist: {value}")

    validate_date(metadata.get("reviewed_at"), "day", "reviewed_at", errors)

    publication = require_mapping(metadata.get("publication"), "publication", errors)
    pub_missing = sorted(REQUIRED_PUBLICATION - publication.keys())
    if pub_missing:
        errors.append(f"missing publication keys: {', '.join(pub_missing)}")
    precision = publication.get("first_public_date_precision")
    validate_date(
        publication.get("first_public_date"),
        precision,
        "publication.first_public_date",
        errors,
    )
    status = publication.get("status")
    if status not in PUBLICATION_STATUSES:
        errors.append(f"publication.status is invalid: {status!r}")
    if not isinstance(publication.get("venue"), str) or not publication.get("venue"):
        errors.append("publication.venue must be a non-empty string")
    reviewed_version = publication.get("reviewed_version")
    if reviewed_version is not None and not isinstance(reviewed_version, str):
        errors.append("publication.reviewed_version must be a string or null")
    validate_date(
        publication.get("reviewed_version_date"),
        "day",
        "publication.reviewed_version_date",
        errors,
        allow_empty=True,
    )

    organizations = require_list(
        metadata.get("organizations"), "organizations", errors
    )
    for index, organization in enumerate(organizations):
        label = f"organizations[{index}]"
        organization = require_mapping(organization, label, errors)
        if not isinstance(organization.get("name"), str) or not organization.get(
            "name"
        ):
            errors.append(f"{label}.name must be a non-empty string")
        if organization.get("sector") not in SECTORS:
            errors.append(f"{label}.sector is invalid")
        roles = require_list(organization.get("roles"), f"{label}.roles", errors)
        if not roles:
            errors.append(f"{label}.roles must not be empty")
        check_allowed_strings(roles, ORG_ROLES, f"{label}.roles", errors)
        require_list(organization.get("authors"), f"{label}.authors", errors)
        require_list(organization.get("grants"), f"{label}.grants", errors)

    artifacts = require_list(metadata.get("artifacts"), "artifacts", errors)
    for index, artifact in enumerate(artifacts):
        label = f"artifacts[{index}]"
        artifact = require_mapping(artifact, label, errors)
        if artifact.get("type") not in ARTIFACT_TYPES:
            errors.append(f"{label}.type is invalid")
        if not isinstance(artifact.get("url"), str) or not artifact.get("url"):
            errors.append(f"{label}.url must be a non-empty string")

    facets = require_mapping(metadata.get("facets"), "facets", errors)
    facet_missing = sorted(REQUIRED_FACETS - facets.keys())
    if facet_missing:
        errors.append(f"missing facet keys: {', '.join(facet_missing)}")
    for key in REQUIRED_FACETS:
        require_list(facets.get(key), f"facets.{key}", errors)
    check_allowed_strings(
        facets.get("paper_type", []),
        PAPER_TYPES,
        "facets.paper_type",
        errors,
    )

    assessment = require_mapping(metadata.get("assessment"), "assessment", errors)
    assessment_missing = sorted(REQUIRED_ASSESSMENT - assessment.keys())
    if assessment_missing:
        errors.append(f"missing assessment keys: {', '.join(assessment_missing)}")
    if assessment.get("extract_quality") not in EXTRACT_QUALITIES:
        errors.append("assessment.extract_quality is invalid")
    require_list(
        assessment.get("extract_limitations"),
        "assessment.extract_limitations",
        errors,
    )
    flags = require_list(
        assessment.get("critical_flags"), "assessment.critical_flags", errors
    )
    check_allowed_strings(
        flags,
        CRITICAL_FLAGS,
        "assessment.critical_flags",
        errors,
    )


def validate_body(body: str, errors: list[str]) -> None:
    if not re.search(r"^Citation:\s+\S", body, re.MULTILINE):
        errors.append("missing non-empty Citation line")

    heading_matches = list(re.finditer(r"^## (.+?)\s*$", body, re.MULTILINE))
    headings = [match.group(1) for match in heading_matches]
    if headings != HEADINGS:
        errors.append(
            "level-2 headings must exactly match schema order: "
            + " | ".join(HEADINGS)
        )
        return

    positions = [match.start() for match in heading_matches]
    positions.append(len(body))
    for index, heading in enumerate(HEADINGS):
        section = body[positions[index] + len(f"## {heading}") : positions[index + 1]]
        content = section.strip()
        if not content:
            errors.append(f"{heading} section is empty; write content or None.")
        if heading == "Critical discussion" and content == "None.":
            errors.append("Critical discussion may not be None.")


def validate(path: Path, repo: Path) -> list[str]:
    errors: list[str] = []
    metadata, body = parse_review(path, errors)
    validate_frontmatter(metadata, repo, errors)
    validate_body(body, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Review files (default: reviews/*.md except README.md)",
    )
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[4]
    paths = args.paths or sorted(
        path
        for path in (repo / "reviews").glob("*.md")
        if path.name.lower() != "readme.md"
    )
    if not paths:
        print("No review files found.", file=sys.stderr)
        return 1

    failed = False
    for raw_path in paths:
        path = raw_path if raw_path.is_absolute() else repo / raw_path
        if not path.exists():
            print(f"FAIL {raw_path}: file does not exist")
            failed = True
            continue
        errors = validate(path, repo)
        if errors:
            failed = True
            print(f"FAIL {path.relative_to(repo)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {path.relative_to(repo)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
