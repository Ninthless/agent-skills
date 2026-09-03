# Learning Protocol

## Default Path: Passive

For ordinary vibecoding, implementation, debugging, and refactoring, use this loop:

1. **Orient**: name the user-visible goal and the affected path.
2. **Select**: keep at most three concepts that are necessary or reusable.
3. **Model**: state the smallest useful model: inputs, outputs, state, boundaries, failure behavior.
4. **Build**: implement the slice while explaining only decisions that affect understanding or maintenance.
5. **Verify**: connect tests, logs, traces, or manual checks to the model.
6. **Overlay**: leave a compact learning overlay. Do not quiz.

Skip **Predict** and **Reflect** unless the user opted into `guided` or `practice`.

## Opt-In Active Loop

Use this extra loop only for `guided` or `practice`:

1. **Predict**: ask the user to predict one observable result when the task is important, unfamiliar, or conceptually rich.
2. **Build** or reveal the next step.
3. **Verify**: connect evidence to the model.
4. **Reflect**: ask the user to explain, modify, or transfer one idea.

Never use this loop to delay a requested implementation. If the user says `直接写`, `跳过`, or `不要提问`, return to the passive path immediately.

## Depth Selection

### Mechanical

Implement with almost no interruption. State the purpose and one relevant detail. Always leave one or two overlay sentences so the skill remains visible.

### Bounded Behavioral

Explain the affected path and one or two concepts after the work. In `passive` mode, stop there. In `guided` mode, one optional transfer question may follow the overlay.

### Architectural

Explain ownership, boundaries, dependency direction, and tradeoffs in a short model, then implement. Do not require a quiz before editing unless the user asked to predict first.

### Debugging

Separate symptoms, observations, hypotheses, and confirmed causes. In `passive` mode, state the working hypothesis and the evidence as you go. In `guided` or `practice`, ask for a hypothesis before the next diagnostic step only when the issue is safe to explore. Do not confuse a passing test with understanding.

## Explanation Format

Use this compact structure:

1. **Problem model**: what the system must do.
2. **Relevant concept**: what matters in this slice.
3. **Decision**: why this implementation fits the repository and behavior.
4. **Evidence**: what code, test, runtime, or documentation supports it.

Add **Practice** only for `guided` or `practice`.

Avoid:

- explaining every line
- introducing concepts unrelated to the current slice
- claiming certainty where the repository or runtime has not been inspected
- turning every interaction into an exam
- withholding code to force learning
- asking what the user wants to learn before doing the work

## Adaptive Feedback

- If the user stays in flow and does not engage the overlay, keep `passive` and keep the overlay short.
- If the user asks why, traces a path, or requests teaching, thicken the model for that slice.
- If the user answers a guided question correctly, reduce scaffolding and increase transfer.
- If the user is partly correct, keep the correct model and repair only the misconception.
- If the user is incorrect, give a smaller hint, then show the evidence.
- If the user says `直接写` or asks to skip questions, implement and keep a compact overlay.
- If the user says `只要结果` or `不要讲解`, drop the overlay.
- If the user demonstrates mastery, do not repeat introductory explanations.
