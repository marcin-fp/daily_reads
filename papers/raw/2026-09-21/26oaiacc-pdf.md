
### For AGI to benefit all of humanity, we believe it must be democratically governed. This can only happen through an informed public debate about the capabilities, risks and safeguards of highly capable AI systems. People everywhere need to understand the likely future trajectory of frontier AI, so they can have a meaningful voice in how it develops.
### Transparency about specific risks, incidents and safeguards is necessary, but not sufficient. We believe the public also needs to understand how the most capable systems are developing, and how they are driving research progress, inside of frontier labs.
### We aim to safely build an automated AI researcher that can work under human supervision to further progress on deep learning and alignment, enabling iterative improvements. According to our measurements, we have now reached the goal,  last fall, of having an automated research intern by September of this year. By “research intern,” we mean a system that can carry out well-defined research tasks under human direction, including tasks that would take a skilled researcher a few days. We are making strong progress toward creating an automated AI researcher by March of 2028.
### Over the course of this year, OpenAI researchers’ daily work has changed substantially. Researchers are using coding agents throughout the day (often in concurrent sessions) and
September 6, 2026 Research Publication Safety
# Research acceleration: The view inside OpenAI
Listen to article 13:39 Share
### announced
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_gBsAPLkwkgwBzx4nJdY_A6Tsl38yBgiqlX7kph2e1uxfYHbKg3rOKLI-ExPOG1ZmKbwp6OA712n269-2-Z8fvmJn8gnzELGEHmaRHGYSVBVK4bCt1xbs61ClZIJ_-OzQDgRMBsw=w784-h1038-v0?authuser=0)

### total usage is rapidly increasing, outpacing growth among other OpenAI teams. Researchers are contributing code faster and running more experiments. The ways researchers use agents are changing, too: agents are handling increasingly complex tasks, and succeeding at them more often. AI research is a complex process with many potential bottlenecks, so the overall pace of progress likely won’t keep pace with these specific metrics. But on the whole, these findings are consistent with the broader impression many of us have internally that agentic tools are meaningfully accelerating research progress. People still set our research priorities, judge which ideas and results to pursue, and decide whether to scale, pause, or deploy systems.
### If it is done responsibly, we believe automated AI research will yield models that directly enhance human welfare and advance OpenAI’s mission. It can bring down the cost of advanced intelligence so that people worldwide can benefit. We are pursuing this work in part because automated research could help us solve alignment and build defenses against increasingly capable AI. An automated AI researcher can also be an automated safety or alignment researcher. More capable, aligned systems could help secure critical infrastructure, defend against dangerous AI agents, and develop new protective measures.
### These are reasons to develop useful automated research capabilities, but they do not mean that rapid RSI is necessarily an outcome we should pursue. Whether and how to proceed must depend on our ability to preserve human control and on informed democratic choices about the benefits and risks.
### We do not yet know how to safely get all the way to aligned, full RSI. We are working to scale alignment and safety measures alongside capabilities. But we cannot assume that progress in alignment and safety will keep pace, and more capable systems can become harder to monitor. Careful alignment and safety work is at the center of this effort, and it starts with measuring and mitigating the safety problems we see today in agentic coding systems. Whenever we find that proceeding would pose an unacceptable safety risk, we will respond appropriately including by slowing or stopping our development or deployment of systems we find ourselves unable to sufficiently safeguard.
### After the recent Hugging Face incident, we , pausing reinforcement learning (RL) training on our latest models intended for deployment while we further hardened and red-teamed our research environments and expanded coverage of
### put this commitment into action
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9WRvzKqFriHoGq2BC8zjBhgAg-EHgmQ8-h3PU08EA_RmRB4NIiHYrsiqVKqZChFtbQgwe-TJkvT3nnwDKSACvNaYXVnFYgdH5NNnMlzBrGPY1eENpxi6rTJgCHazbTjYco8f-47w=w784-h1038-v0?authuser=0)

### our monitoring systems. This did not halt all research: some workloads resumed under stronger controls, while others remained paused. We have raised our safety and alignment standards and moved safety work deeper into the model lifecycle, requiring stronger evidence of aligned behavior throughout all of training.
### Today we are providing a detailed snapshot of how agentic systems have contributed to our progress toward RSI in recent months. Agentic systems are new and rapidly changing, and our measurement efforts are still preliminary. By sharing these early results and the methods behind them, we aim to inform the public, encourage a norm of public disclosure, and help the field move toward shared standards of measurement.
### Ultimately, as we wrote in our , we believe that we and other companies should be required to publicly track our progress toward RSI. Even without such a requirement, we plan to continue being transparent about our RSI progress. We will evolve our transparency approach as our measurement techniques and understanding improve, while balancing the need to protect security and proprietary information.
1. Coding agents are reshaping daily work for OpenAI researchers
### At the start of this year, the median researcher ranked by agent usage at OpenAI was using coding agents only in modest amounts. By mid-August, the median researcher was integrating agents daily into their work, using more than $600 per day of inference at API prices. The 90th percentile user in our research organization now uses more than $7,000 of tokens per day.
### frontier policy blueprint
### **Usage of internal coding agents is increasing significantly— Median researcher**
### **Usage of internal coding agents is increasing significantly—90th percentile researcher**
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8l58TkfXSME4RI24ILJyF5ZAuE8nCcpYmtr5eS0X5gDWj3vTolGSiRJ5Gu4RgFmkFJvIRSEpZEJa_rFYoUAVSnny1jHqOPZ0S04LUXBkHjeq3I0EuyYUFU6zDjubCP6An31e1CqA=w784-h1038-v0?authuser=0)

View methods
View methods
### Before June 2026, total agent runtime across the research organization was still below that of total human labor. That has since changed. In terms of a standard 8 hour workday, as of
F b A J
F b A J
D ai
ly  $
/ re
se ar
ch er
### **Usage growth is faster among researchers than in other parts of the company**
Dec 2025
Feb 2026
Apr 2026
Jun 2026
Aug 2026
fo r t
he  m
ed ia
n em
pl oy
ee
Research (124x)
### mid-August, in total, the research organization uses 3.1 agent-workdays of effort for every workday of human labor.
View methods
### Another way of looking at this is to understand how many researchers use highly concurrent workflows (e.g., running 4 or more agents simultaneously). As shown below, this number is increasing. These figures include the daily peaks of both agents started directly by the user and subagents created downstream from those the user launched directly.
### **Agentic workdays now far exceed those of human researchers**
May 2026
Jun 2026
Jul 2026
Aug 2026
re
se ar
ch er
w or
kd ay
s
3.14x
### **Researchers are leveraging concurrent workflows more over time**
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8sra92BHqNB2jc5WwWZYxiB_AfU8Pqo_AjdZc1FbToGkPt4yd5buOl1-T4tthJKOoijmHdlnIdewuCW08tUXY_eiTkGL6OxTszUoM2DooulsUMNiNHCqEhBpP-pwUA3dWIN_eE=w784-h1038-v0?authuser=0)

View methods
2. Researchers are writing more code and running more experiments
### Much of AI research can be seen as a labor-intensive process with the goal of integrating a new improvement to model intelligence or performance into one of our core models. The process depends on many steps, and capabilities advance when all the steps go right together: Researchers have to design new improvements, write evaluations to judge model performance, write infrastructure to test these improvements at scale, catch bugs as well as unsafe or misaligned behavior during training, and integrate winning ideas into a core training run. A failure at any part of the research process can constrain the entire loop.
### Writing code and running experiments are two major activities that researchers do as part of their work, and we see evidence that these processes are accelerating.
Apr 12
Apr 29
May 17
Jun 4
Jun 22
Jul 10
Jul 28
Aug 15
co nc
ur re
nt  w
or kfl
ow s
### **Across the company, engineers are shipping code faster**
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9tIgqkD-tJnjZebJZE5izMfNbOQRyPKyXo7ITSAih-mK-A-4IFHW1ZztrdKXLJV-C3umtYrm2LPaVC7wQDU0MQEvLjqFErAyh12k0lsSOIm_WEaAjDjFuG5wItp9gI3pg6-9XhUw=w784-h1038-v0?authuser=0)

View methods
### These data points are relatively easy to measure, but can be hard to interpret. As*automation progresses, the tasks which are least automatable will take on a larger share of*researcher effort and will become the important bottlenecks to future progress. Compute is another gating factor for progress, and may become more important over time as other bottlenecks diminish.
### Through 2026, the number of experiments per active experimenter has increased, with August 2026 being an all-time high since tracking began in Jan 2025. This is correlated with increased Codex adoption, though we note that our available compute has also grown significantly since 2025.
Jan 2022
Jan 2023
Jan 2024
Jan 2025
Jan 2026
ac
tiv e
co nt
rib ut
or (p
re -2
02 5
= 1x
)
Average before 2025
### **Experiment velocity has increased**
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9CZ8CgkRqLqNSYXZ8nwtIA0gEfRooeQhbuZTxkmzOMhRjYCyS3sZsIahaVd3axG89H0tXMtXwjErDrBKhYlJx4vZOj1QbfoyWrHczdG-73hDFsW7ouHqtz3JmOnKDfP7jrN1WqlA=w785-h1038-v0?authuser=0)

View methods
3. The work researchers use agents for is changing
### Both qualitative impressions and internal data indicate that the mix of tasks researchers delegate to coding agents is changing, with delegation of higher level and longer-horizon tasks becoming more common over time.
### To get a clearer picture of this trend, we analyzed recent usage in the research organization using a  of the different kinds of work that are part of the AI R&D lifecycle, developed by Epoch AI. This taxonomy, inspired by the longstanding O*NET system for classifying all kinds of work, is specifically tailored to frontier AI R&D, and breaks the process down into six main phases:
1. Decide: what to work on, what to continue, where to allocate
2. Design: research ideas and engineering specs
3. Build: code and datasets
4. Run: training/eval runs, hardware, serving
5. Analyze: experiments, models, deployment, external work
6. Communicate: findings, feedback, status, decisions
### Below, we classify coding agent tokens under this taxonomy.
Jan 2026
Feb 2026
Mar 2026
Apr 2026
May 2026
Jun 2026
Jul 2026
Aug 2026
Week
ex
pe rim
en te
r (2
02 5
= 1×
)
### recently published taxonomy
### **Researchers are using coding agents in new ways**
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9DNcDOQTm8Tv1c2tI22IYFzuYkOX9tQdt8Huk03NRYDaZXsC5Rnm8MLVpSXZf93GPgWw-EjlRKheC5IpxAD2x6CfkveYr3HqX4bPPjpFjBjTxp3Gh1gwcLZ5p-FsrjElzdJQFkcQ=w784-h1038-v0?authuser=0)

View methods
Feb 2026
Mar 2026
Apr 2026
May 2026
Jun 2026 2
1.1 What to work on
1.2 What to continue or stop
1.3 Compute & staffing decisions
2.1 Research & experiment planning
2.2 Technical specifications
3.1 Research & infrastructure code
3.2 Training & eval datasets
4.1 Launch, monitor & debug runs
4.2 Compute-cluster operations
4.3 Production serving reliability
5.1 Analyze experiment results
5.2 Analyze model behavi & capabilities
5.3 Analyze production usage
5.4 Review external research
### **All categories of research activity have increased since the start of the year**
View methods
### We see that all categories of research activities have increased between January and August 2026. In January, the dominant category was research and infrastructure code. This category has expanded, but we also see notable increases in additional categories, especially technical help and monitoring runs. High-level planning still remains a minimal fraction of agent output tokens.
### Anecdotally, colleagues report that coding agents excel at troubleshooting internal research infrastructure, which addresses one meaningful bottleneck to research progress. Multiple teams which previously held office hours to help researchers troubleshoot their experiments have noted declining attendance in 2026, and one has stopped holding sessions entirely, to focus on making other system improvements instead.
### Here, we plot the number of top-level posts per day to one of the main internal channels where researchers seek technical support from other teams. To our knowledge, the channel’s decrease in activity has not been offset by queries shifting to another technical support channel run by humans. The decline in traffic aligns with this broader shift.
`0k 50k 100k 150k`
Output token increase / researcher / day
3.1 Research & infrastructure code 6.2 Technical help & review
4.1 Launch, monitor & debug runs 5.1 Analyze experiment results
4.2 Compute-cluster operations 6.1 Research write-ups & documentation
3.2 Training & eval datasets 4.3 Production serving reliability
5.2 Analyze model behavior & capabilities 2.2 Technical specifications
6.3 Status updates & work logs 2.1 Research & experiment planning
5.3 Analyze production usage 1.1 What to work on
1.3 Compute & staffing decisions 5.4 Review external research 1.2 What to continue or stop
6.4 Decision announcements
1.1 What to work on
1.2 What to continue or stop
1.3 Compute & staffing decisions
2.1 Research & experiment planning
2.2 Technical specifications
3.1 Research & infrastructure code
3.2 Training & eval datasets
4.1 Launch, monitor & debug runs
4.2 Compute-cluster operations
4.3 Production serving reliability
5.1 Analyze experiment results
5.2 Analyze model behavior & capabilities
5.3 Analyze production usage
5.4 Review external research
6.1 wr do
6.2 he
6.3 up log
6.4 an
+15 +133.1k
+40.2k +37.4k
+18.0k +13.7k +12.9k
+11.2k +9.5k
+8.1k +5.1k
+3.1k +2.3k +1.5k +0.7k +0.2k +0.03k
View methods
### We can also study whether coding agents are succeeding at the tasks researchers request. Using an agentic classifier, we find that from January to July, success rates generally increased across several difficulty buckets (proxied as the estimated time a human would take to complete the task) on tasks we can find a ground truth outcome for. However, agents still require significant human steering to be successful, especially as task complexity rises. In the last 6 months, over half of successful 4-8 hour tasks involved 1 or more interventions.
### **Certain forms of troubleshooting are increasingly handled by agents**
Jan 2025
Jul 2025
Jan 2026
Jul 2026
tr
ou bl
es ho
ot in
g ch
an ne
l
### **Agents are increasingly solving more complex tasks for researchers**
2026-01 2026-02 2026-03 2026-04 2026-05 2026-06 2026-07
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-ACk21j938U3Ywyy0boNchDF1KXYmOInkZa3pXC9XtnPtckkDvUg-NWLTRqUuvjm-Gbhzbbmw9igVkUpFNYM9N5Krg4paK9J9ljsF7MQvjHWAFyYp9vhe1uFSVRJm0f4mGPgmhog=w784-h1038-v0?authuser=0)

View methods
<15m
15-30m
30m-1h 1-2 h
2-4 h
4-8 h
8-16 h
16-32h
32-6 4h
64-12 8h
>=128h
Estimated time for a human
Success rates on researcher tasks have increased over time. Graph excludes classifications where the outcome was uncertain and points with <50 sessions or <50 unique users.
### **Longer tasks need more interventions**
Success + 0 interventions Success + ≥1 intervention Failure Tool errors
No clear goal
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9s4KoD_aNIblNIPUrx1Gkgk6_QVYiz3KTu-3lrAYsE4h5ySN-tJEScsDVr-QIbqiZUYOPS93x0n-3Jf0xvLoGdXaUpzKAJC8wiRT6hzNlvEahJJoQg3DLqE8K93VzlYkMTd8yevA=w784-h1038-v0?authuser=0)

View methods
4. Pacing model development
### Progress toward more capable systems for safe and beneficial AGI will also depend on the safeguards needed for such work. Our assessment of the needed safeguards may change as we learn more about the risks.
### we have recently updated our standards for monitoring, alignment, and security. Here, we show how recent restrictions have affected one aspect of research activity.
<15m
15–30m
30m–1h 1–2h
2–4h 4–8h
8–16h
16–32h
32–64h
64–128h
Estima ed time for a human
86%
8%
76%
19%
69%
23%
61%
29%
57%
33%
8%
43%
45%
10%
40%
48%
11%
23%
59%
15%
13%
63%
13%
10%
16%
51%
26%
Task success and intervention rate from Jan to July, broken out by time horizon. Excludes classifications where the outcome was uncertain.
### As we have described,
### **Changes in RL compute in response to safety-related restrictions**
Non-Astra Astra-class (before Aug 6–7 restrictions)
Astra-class (with Aug 6–7 security restrictions)
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9mn4bXQ42VP4Dh_UGlXX62YRvfPRfoRWzzWWhY89xexMY4vwdtadr2ZQfSZNqeSLsS4_gq8Blhy81tUgri3XzT25kyaNBqGkz_GaItkAEVaanN1Qh9rr1t-oovwJheHXPUMYa4qA=w785-h1038-v0?authuser=0)

View methods
### On July 20, following the discovery that agents had compromised our research infrastructure, we temporarily shut down the container service used for training, and then restored it with significant additional restrictions.
### This led to a sharp decline in RL training compute while teams reconfigured their workflows to operate within the hardened research environment. The plot above includes the two week pause in reinforcement learning on our latest models intended for deployment. Astra-class RL experiments between July 20 and August 6 include a majority of runs (by GPU allocation) intended to test the implementation of safety and security improvements.
### On August 7, preliminary evidence that Astra  under our  led to additional model-specific security restrictions which
### required the Astra model to be run in higher security research environments. In the
Jul 15 2026
July 20 2026*
Jul 27 2026
Aug 03 2026
Aug 10 2026
Aug 15 EOD 2026
Date (PDT)
(J
ul  1-
A ug
15  d
ai ly
p ea
k =
10 0%
)
Safety infrastructure pause and
institution of additional security requirements
Additional Astra-class
security restrictions
*The majority of Astra compute shown here between July 20 and August 6 was intended to test the implementation of safety and security improvements.
### may have critical cyber capabilities Preparedness Framework
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-_RTZ6lwG2AZwTw0eblbZTEqudJUk-6Vv4Vi3hutTCslvNoD2X6Wvg0OOFxXNBAmNmwZiUiVkCvTmLIAlTwPnhTRSUMRxB_-MeGzwWpQt1ZwooyXWT7Mz3y9p1tUL7dhjjTDpAnQ=w784-h1038-v0?authuser=0)

### model classes rose 17.2 percent. That increase offset about 85 percent of the Astra-class decline, leaving total allocation in the analyzed RL workloads largely unchanged. This pattern is consistent with substitution of some training and experimentation to non-Astra models while work involving Astra was restricted, and comports with anecdotal reports of researchers finding other uses for compute that could no longer be leveraged for workloads covered by the new constraints.
### This data provides a useful signal for ongoing conversations about training and safety: When new controls are introduced, compute remains valuable and flexible, and will naturally be channeled into alternative uses within the research enterprise. Longer term, discussions about the pace of AI progress should also extend to the question of how compute that is subject to new or proposed controls can best be used.
5. The path ahead
### Making and understanding progress toward aligned RSI is important for our mission. We will continue to refine our methods, report on our evolving understanding, and work toward an informed public debate and meaningful democratic governance of frontier systems.Appendix: Our methods for this post
### Agent-powered AI research is still new, and we are still learning how to measure it. Some indicators, such as the amount of code our research teams generate, are relatively easy to gather, but hard to interpret because their relationship to research progress is uncertain. Metrics that focus more directly on research progress—such as how often agents succeed at the tasks researchers give them—could be more useful, but are complex to develop and validate. Furthering the difficulty, the tools and systems researchers rely on are evolving rapidly. Deepening our understanding of research acceleration is a significant focus area across OpenAI.
### Across these analyses, unless otherwise noted:
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_nEP9rVwJzsET1zhpXrh3QkUuWbylVu4ZELhLnMVoXxJCVYrHfqWLZ5Qy3X3GZLmJ_ePfQgTO9ZKVOUavOg8E3UevWrZYV5WRAAm-USMYG3p9cKUbPhdjpxe_Tzd3dlhx68rsEdQ=w784-h1038-v0?authuser=0)

### “Researcher” is a broad term for any member of our research organization, including some who build research infrastructure, manage research projects, or otherwise support the enterprise.
### Metrics of coding agent use cover most, but not all, usage given rapid evolution in the tools and systems researchers rely on.
2026 Economic Research
Author
OpenAI
Research
Research Index
Research Overview
Economic Research
Latest Advancements
GPT-6
GPT-5.6
GPT-5.5
GPT-5.4
Products
ChatGPT
ChatGPT Business
ChatGPT Enterprise
ChatGPT for Education
Codex
Release Notes
API Platform
Business
Overview
Solutions
Resources
Plugins
Customer Stories
Partner Network
Contact Sales
Developers
Company
About Us
Our Charter
Careers
News
Support
Help Center
More
Stories
Academy
Supply Co.
Livestreams
Podcast
RSS
Terms & Policies
Terms of Use
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9qjnwPRDM0_TIM3eU2t4JgDlUbhAKPyhQ9fYczvoZi49SLBu3sU3rfX9aYiq_bPBH2VMS-BIpwlfX6eobtky50KQBori1qry2pvVIR174N-a6Sm7eJSIui7M1XwIqcir0P0Svqnw=w784-h1038-v0?authuser=0)

Safety Approach
Deployment Safety
Security & Privacy
Trust & Transparency
API Log In
Docs
Docs
Resources
Developer Forum
OpenAI © 2015–2026
Your privacy choices
### English United States
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8U-EfgbNigqJD0tV4ZvYBCBcJamiJlB8l__RbyCHuNc-V-9ASTsVR4JMOxTOW77-TfvlIYXOf5AhjM6gbQPHTnRst7SWlXP73FnCBa12SqGXQCxGaoTqORwySqnjNlWVeuSlwnpg=w784-h1038-v0?authuser=0)
