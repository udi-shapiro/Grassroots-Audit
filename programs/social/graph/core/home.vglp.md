# Audit report: programs/social/graph/core/home.vglp

Project: GSA
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: c40e6d3ad68b198066ab723d17c05171c0a7de76

Scope: Home's local-artifact installation request and creator-certificate production, including the committed compilation in `home.glp`.
Coverage: Traced `serve(install(...))` through `load_file`, `install_act` and `creator_certification` to the host. Compared the vGLP producer with the same code in `home.glp`; executed the latter's helper through an audit-only export, followed by the host's unchanged verifier.

For every loaded module, the helper signs its source identity under `self_key` with fixed acts `[friendship, ending_a_friendship]` and a fixed `syntactically_grassroots` verdict. That certificate was accepted by the host. This behavior and the missing provenance/schema checks are consolidated in [agent.glp Finding 1](agent.glp.md); they are not counted again here.

Home's request type has local `install(AppName, Artefact)`, but no `trust_store`, listing retrieval or `install_from_store` path. The [GAS report](../GAS.glp.md) records the incomplete store integration. No live store delivery, UI click path, physical phone or general Home feature audit was performed.
