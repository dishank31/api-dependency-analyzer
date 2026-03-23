Problem Research - API Dependency Graph Analyzer
I research on Day 1 to understand the problem space, validate the tools needed for this and identified the gaps in existing solutions.

The Core Problem
Microservices teams changes APIs without knowing which other service are dependent on them.
Breaking changes are discovered in production, not before deployment.
There is currently no tool that auto-discovers dependencies from logs and predicts which services will break before the change is deployed.

What are Microservices?
Microservices is a software architecture style where an application is built as a collection of small, independent services, and each service performs one specific business function and communicates with other services through APIs.




Pain Points Found (Most Important)

Pain point 1- No visibility into API dependents

When a team changes an API, they have no automated way to know
which other services consume it. Coordination happens manually via Slack,
emails, or tribal knowledge — all of which are unreliable at scale.

Source: Martin Fowler, "Microservices" (martinfowler.com)

"Any interface changes need to be coordinated between participants,
layers of backwards compatibility need to be added."
But no tool tells you WHO to coordinate with automatically.

Pain Point 2 — Breaking changes discovered at runtime, not compile time

When services share data models and a field name changes,
the break doesn't happen until runtime in production — not at compile time.
This means outages are the first signal that something went wrong.

Source: InfoQ, "7 Ways to Fail at Microservices"

A consultant found a team where "every time we change one microservice,
another one breaks" — because field name changes silently broke
all consumers at runtime, not caught until production.

Pain Point 3 — Failures cascade across services

In microservice architectures, the downtime of your system becomes
the product of the downtimes of individual components.
One broken API doesn't just break one service — it breaks everything downstream.

Source: Martin Fowler, "Microservices" (martinfowler.com)

"The downtime of your system becomes the product of the downtimes
of the individual components."



Real-World Incidents

# Incident 1 --- Netflix (2008)
What happened: A single database corruption caused a 3-day service outage
Impact: Complete service unavailability for millions of users
Root cause: No visibility into how deeply one change could cascade
Source: yochana.com — Netflix microservices case study

# Incident 2 — Uber (1300+ microservices)
What happened: After any maintenance, service outages became common because microservices had differing standards and no coordination tooling
Impact: Outages became routine — "impossible to coordinate standards for all microservices after maintenance"
Root cause: No tool to track which services depended on which
Source: sayonetech.com — Uber microservices case study

# Incident 3 — Anonymous Fintech (InfoQ case study)
What happened: Renaming a field in a shared object model broke all consumer services silently
Impact: Runtime failures in production with no compile-time warning
Root cause: No dependency contract tracking between services
Source: InfoQ — "7 Ways to Fail at Microservices"


Existing Tools and Their Gaps

# Tool 1 — Backstage (by Spotify)
What it does: A software catalog where teams manually register their services, owners, and dependencies.

Gap: Everything is manual. Teams must update the catalog themselves.
No auto-discovery from logs. If a team forgets to update it, the catalog becomes outdated and useless.
No break prediction before deployment.

Verdict: A documentation tool, not a dependency analyzer.

# Tool 2 - LogClaw (Open Source)
What it does: Detects anomalies in logs AFTER something goes wrong.
Maps blast radius across affected services in ~90 seconds.

Gap: Reactive not predictive. It tells you what broke, not what WILL break before you deploy.
No pre-deployment analysis at all.

Verdict: Solves the monitoring problem, not the prevention problem.
Source: Hacker News launch post (found during Day 1 research).

# Tool 3 - Swagger / OpenAPI
What it does: Documents individual API contracts — endpoints,
parameters, and responses for a single service.

Gap: Documents APIs in isolation, not relationships between services.
Does not track who calls whom.
Does not warn about breaking changes.

Verdict: API documentation tool, not a dependency graph tool.

# Note on Unverified Tools
During research, Google's AI search suggested a tool called "R.A.D.A.R" for API dependency visualization. After verification via
GitHub and direct search, no such tool exists. This was an AI hallucination in search results. Always verify tool existence before citing.

Lesson: Never trust AI-generated search summaries without verification.

# Our Solution's Unique Value
Every existing tool is either:
- Reactive  → tells you what broke after it broke (LogClaw)
- Manual    → requires teams to document dependencies (Backstage, Swagger)

Our tool is proactive and automatic:
1. Auto-discovers dependencies by analyzing API call logs
2. Predicts which services break BEFORE deployment
3. Visualizes full dependency graph with blast radius
4. Works passively — zero extra work for developers

No existing tool does all four together.