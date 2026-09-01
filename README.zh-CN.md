# Agent Skills

简体中文 | [English](./README.md)

一套面向实际软件工程工作的 Agent Skills 集合，用于稳定执行需求整理、领域调研、代码实现、AI 辅助开发中的学习、界面设计、接口文档、平台专项开发和交付流程。

这个仓库解决的不是“如何写一个更长的提示词”，而是如何把反复出现的 Agent 工作沉淀为有触发条件、有执行流程、有质量边界、能按需加载并且可以验证的独立能力。项目也把 AI 交付和人类学习视为可以同时实现的目标：Agent 可以承担项目实现，同时暴露用户理解并逐步接管项目所需的概念、决策和验证证据。

## 项目提供什么

每个 Skill 都是一套自包含工作流，告诉兼容的编码 Agent：

- 什么情况下应该启用
- 开始前必须读取哪些证据
- 如何划定任务边界和作出决策
- 哪些常见失败模式必须避免
- 完成前应该进行什么验证

整个项目重点关注：

- 有边界的任务范围和明确假设
- 符合现有项目习惯的实现，而不是生成器式通用架构
- 跨编程语言的人类手写维护能力
- 在 AI 主导的实现、调试和重构中进行主动学习
- 契约、生命周期、顺序协议和依赖能力验证
- 完整的用户界面状态和真实渲染证据
- 根据源码、类型、测试和运行证据编写文档
- 安全的平台专项执行与 Git 交付
- 可重复使用的触发评测和行为评测

## Skill 列表

| Skill | 用途 |
| --- | --- |
| [`build-user-facing-ui`](./skills/build-user-facing-ui/) | 构建、重做、审查和验证 Web、移动端、桌面端、游戏、信息亭等用户界面，覆盖完整状态、响应式、无障碍和渲染验证。 |
| [`english-spec-first`](./skills/english-spec-first/) | 把粗糙、中英混合或存在实质歧义的需求整理成简洁的英文工作规格，再据此执行任务。 |
| [`freelance-order-triage`](./skills/freelance-order-triage/) | 在接单或报价前评估客户需求、隐藏范围、交付风险、里程碑、修改次数和验收条件。 |
| [`git-checkpoint-push`](./skills/git-checkpoint-push/) | 通过定向暂存、Conventional Commit、远程分支检查和明确结果报告创建并推送可靠的 Git 检查点。 |
| [`high-constraint-coding`](./skills/high-constraint-coding/) | 使用最小、严谨、证据驱动的流程编写正确且符合项目习惯的代码，让人类能够直接定位、追踪、修改和验证。 |
| [`learn-while-building`](./skills/learn-while-building/) | 把正在进行的 AI 辅助项目工作转化为聚焦学习，通过自适应教学、代码追踪、主动回忆、反思、迁移练习和可选项目知识记录帮助用户理解项目。 |
| [`no-code-comments`](./skills/no-code-comments/) | 默认让生成或修改的代码类文件不包含解释性注释，同时保留工具指令和必要文档契约。 |
| [`powershell-safe-commands`](./skills/powershell-safe-commands/) | 避免 Windows PowerShell 中的插值、引号、嵌套 Shell、路径和包装层解析错误。 |
| [`vibecoding-domain-scout`](./skills/vibecoding-domain-scout/) | 调研陌生、受监管或依赖平台规则的领域，并整理真实流程、约束、风险、MVP 边界和可开发需求。 |
| [`websearch-first`](./skills/websearch-first/) | 在回答或修改文件前搜索权威且时效匹配的来源，把外部依据与本地事实对照，并只引用实际影响结果的资料。 |
| [`write-api-docs`](./skills/write-api-docs/) | 根据路由、Schema、客户端、测试、运行证据、OpenAPI、GraphQL、gRPC、Webhook 或消息协议编写和审查接口契约，不虚构行为。 |
| [`xposed-module-dev`](./skills/xposed-module-dev/) | 开发、审查、迁移和调试 Android Xposed 或 LSPosed 模块，覆盖现代 libxposed 和传统 XposedBridge 项目。 |

## 设计方式

每个 Skill 遵循 [Agent Skills 开放标准](https://agentskills.io)，并使用渐进式加载：

1. 通过 frontmatter 元数据判断是否应该触发。
2. 触发后读取 `SKILL.md` 中的核心工作流。
3. 只有任务确实需要时，才读取参考资料或执行脚本。

一个 Skill 目录可以包含：

```text
skills/
  <skill-name>/
    SKILL.md
    agents/
      claude.yaml
      openai.yaml
    references/
    scripts/
    evals/
      evals.json
      trigger_eval.json
```

标准只要求存在 `SKILL.md`。这个仓库还会按实际需要使用：

- `agents/`：面向不同 Agent 平台的名称、简介、默认提示词和调用策略
- `references/`：不应长期占用基础上下文的详细规则和领域资料
- `scripts/`：需要确定性执行的验证或证据处理工具
- `evals/`：正负触发样例和贴近真实任务的行为评测

`agents/` 中的文件是仓库为具体平台增加的扩展，不属于 Agent Skills 基础标准。

## Skill 如何组合

Skill 可以独立使用，也可以围绕同一个任务组合：

- `english-spec-first` -> `vibecoding-domain-scout` -> 对应实现 Skill
- `freelance-order-triage` -> 付费调研、分阶段交付或受控报价
- `websearch-first` + 任意任务 Skill -> 用当前外部依据校准本地事实
- `high-constraint-coding` + `no-code-comments` -> 严谨实现和干净源码风格
- `learn-while-building` + 实现或调试 Skill -> 在完成项目工作的同时形成聚焦理解、主动回忆和迁移能力
- `build-user-facing-ui` + `high-constraint-coding` -> 完整界面体验和受控工程实现
- `write-api-docs` -> 有证据支持的接口对接契约
- 工作完成后 -> `git-checkpoint-push`

组合使用不代表自动扩大任务范围。辅助 Skill 应该加强当前工作流，而不是增加用户没有要求的交付物。

## 安装

兼容 Agent 通常会从以下项目级或用户级目录发现 Skill：

| 路径 | 作用范围 |
| --- | --- |
| `.agents/skills/` | 项目级，通用 |
| `.cursor/skills/` | 项目级，Cursor |
| `.claude/skills/` | 项目级，Claude Code |
| `~/.agents/skills/` | 用户级，通用 |
| `~/.cursor/skills/` | 用户级，Cursor |
| `~/.claude/skills/` | 用户级，Claude Code |

Codex 当前从 `.agents/skills/` 发现仓库 Skill，从 `~/.agents/skills/` 发现个人 Skill。平台专属路径应以对应 Agent 自身的发现规则为准。

在 Windows 中安装单个 Skill：

```powershell
New-Item -ItemType Directory -Force $env:USERPROFILE\.agents\skills | Out-Null
Copy-Item -Recurse .\skills\high-constraint-coding $env:USERPROFILE\.agents\skills\
```

安装整个集合：

```powershell
New-Item -ItemType Directory -Force $env:USERPROFILE\.agents\skills | Out-Null
Copy-Item -Recurse .\skills\* $env:USERPROFILE\.agents\skills\
```

对应平台明确要求专属目录时，可把目标位置替换为 `.cursor\skills` 或 `.claude\skills`。

在 macOS 或 Linux 中：

```bash
mkdir -p ~/.agents/skills
cp -r ./skills/high-constraint-coding ~/.agents/skills/
cp -r ./skills/* ~/.agents/skills/
```

部分 Agent 在安装后需要重新启动或重新加载，具体取决于它的 Skill 发现机制。

## 使用

兼容 Agent 可以根据 Skill 的元数据自动触发，也可以在支持具名调用的平台中显式指定。

示例：

```text
使用 high-constraint-coding，以最小完整改动修复这个回归问题。

使用 build-user-facing-ui 重做这个流程，并验证所有响应式状态。

使用 write-api-docs，把前端客户端和后端路由整理成一份一致的接口契约。

使用 learn-while-building 实现这个功能。代码由你完成，但要教我理解请求链路、关键决策，以及测试如何证明行为。
```

使用前应以目标 Skill 的 `description` 和正文工作流为准。负面触发样例会避免专业 Skill 接管简单概念问答或与其无关的任务。

## 评测与验证

复杂 Skill 通常包含多类互补评测：

- `trigger_eval.json`：验证代表性请求是否应该触发该 Skill。
- `evals.json`：验证 Agent 在真实任务中的工作方式和质量要求，但不强制唯一实现。
- 代码评测夹具：针对真实仓库改动运行公开测试、仅评分阶段可见的验收测试、依赖限制和 Diff 范围规则。

部分 Skill 还包含确定性脚本，例如 UI 证据校验、视觉指纹比较和 OpenAPI 证据校验。

`high-constraint-coding` 包含四个跨平台代码夹具，分别覆盖运行时版本兼容、持久化往返、事务重试边界和 Provider 集成可维护性。Runner 只把公开夹具复制到隔离工作区，可选执行外部 Agent 命令，等实现结束后再注入评分测试，并把测试失败、受保护文件改动、依赖变更和越界修改视为硬失败。

运行确定性检查：

```powershell
python -m unittest skills/high-constraint-coding/scripts/test_run_code_eval.py -v
python skills/high-constraint-coding/scripts/self_check_code_evals.py
```

让候选实现通过隔离评测：

```powershell
python skills/high-constraint-coding/scripts/run_code_eval.py skills/high-constraint-coding/evals/fixtures/go-metadata-roundtrip/fixture.json --agent-command <可执行程序> <参数>
```

Runner 通过 `CODE_EVAL_PROMPT` 环境变量传递任务。任何适用门槛失败都禁止完成声明；必需门槛未验证时只能标记为 `Implemented but unverified`。

修改 Skill 时，应当：

1. 保持 `SKILL.md` 简洁，把详细内容拆到可直接发现的参考文件
2. 当 Skill 定位或默认行为改变时，同步平台元数据
3. 为可泛化规则补充触发评测和行为评测
4. 运行相关脚本和结构校验
5. 使用不泄露预期答案的新任务前向测试复杂改动

## 项目原则

- 用实际证据代替看似合理的 API 名称和记忆中的行为。
- 正确性、契约一致、生命周期闭环和人类维护优先于代码短小。
- 实现和指导必须符合目标项目及目标语言的习惯。
- 只有在隔离真实策略、副作用、依赖、所有权边界或变化原因时才新增抽象。
- 不根据代码风格推断作者身份，也不以规避 AI 检测为目标。
- 完成声明不能超过实际执行过的验证范围。

## 许可证

Copyright (c) 2026 Ninthless. All rights reserved.

本仓库包含专有的个人工作流材料。查看本仓库不代表获得复制、修改、重新分发、发布、再许可、托管、转载、销售或创作衍生作品的权限。

完整条款请查看 [LICENSE](./LICENSE)。
