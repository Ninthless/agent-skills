# Maintainability Audit

Audit observable code properties, never purported authorship. Ask whether a maintainer can locate the behavior, understand names and control flow, identify ownership and boundaries, diagnose errors, and safely change the next adjacent case.

Check cognitive load, role-oriented naming, local consistency, dependency direction, abstraction evidence, error context, lifecycle visibility, dead code, duplicated validation, and unreachable defensive branches. Every new artifact needs a current consumer or requirement. Flag pass-through layers, generic helpers, boilerplate symmetry, vague names, excessive indirection, and comments that explain complexity the structure should remove.

Do not erase reasonable asymmetry. A local exception is maintainable when its domain rule, compatibility obligation, or established subsystem pattern is visible and tested. Convert template or AI-smell concerns into concrete defects such as unnecessary layers, duplicated logic, inconsistent error semantics, unowned state, misleading names, or unverified behavior. Do not discuss how code was authored.