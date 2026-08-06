# Agent Skills

[English](README.md)

一套专有的 Agent Skills 集合，包含十个职责明确的 Skill，用于构建可重复的分析、执行、操作和 companion 工作流。

## Skill 列表

- `bug-diagnosis`：调查根因未知的软件缺陷，在修复前产出有证据支撑的根因结论。
- `freelance-order-triage`：判断商业开发订单应当接受、澄清、分阶段、报价、调整范围还是拒绝。
- `git-checkpoint-push`：根据真实仓库状态，仅执行用户明确授权的 Git 检查点操作。
- `high-constraint-coding`：以语言和生态原生、资深工程师级的质量要求，实现和审查所有编程语言的实际源代码；强调经过审慎判断的项目原生设计、可维护且易读的代码、受控范围和经过验证的行为。这是工程质量要求，不是作者身份声明；网页工作在工具可用时保留浏览器验证。
- `no-code-comments`：仅在用户明确要求或仓库已有无注释策略时，作为 companion 约束代码类产物不添加注释。
- `powershell-safe-commands`：防止 PowerShell 特有的解析、引号、插值和编码问题破坏命令。
- `requirement-analysis`：将粗略、冲突或不完整的材料整理为有边界、可测试的实现合同。
- `technical-solution-research`：研究当前的库、框架、协议、标准、版本和技术方案选择。
- `vibecoding-domain-scout`：研究陌生行业的工作流、业务规则、政策、合规要求和专业术语。
- `write-api-docs`：创建、协调或审查有证据支撑的 API 合同和集成文档。

## 格式与扩展

每个 `skills/<name>/SKILL.md` 都遵循 Agent Skills 开放规范，包含可移植的名称、描述和指令。`agents/openai.yaml` 和 `agents/claude.yaml` 提供平台专用的界面提示词和调用策略。`skills-manifest.json` 是仓库本地扩展，用于记录路由模式、角色、隐式调用、副作用和 handoff 元数据；它不属于开放规范，也不会重复保存 Skill 描述。

有关最终产物归属、companion、零 Skill 场景、顺序执行和授权边界，请参阅 `docs/skill-routing.md`。

## 目录结构

```txt
skills/
  <skill-name>/
    SKILL.md
    agents/
    evals/
    references/
evals/
docs/
scripts/
```

## 验证

在仓库根目录运行完整的本地验证合同：

```powershell
python scripts/validate_all.py
```

该命令会验证 Skill 元数据和引用、两种平台的 agent 文件、manifest 一致性、行为与触发评测、跨 Skill 路由同步、机器可读合同的 obligation 极性、仓库 JSON 以及体积报告。`scripts/audit_skill_sizes.py` 会区分开放格式的硬限制和仓库建议，并将 Codex 初始目录的 8000 字符预算作为平台预算报告，而不是开放规范规则。

`.github/workflows/validate.yml` 中的 GitHub Actions 工作流会以只读仓库权限运行同一命令。路由案例定义了未来多轮模型触发率评测的预期，但仓库验证器不会执行真实模型路由试验。网页实现会路由到 `high-constraint-coding`；其验证合同要求在工具可用时检查或复用开发服务器、验证浏览器流程和响应式表现、检查控制台和相关网络请求、保留有用的视觉或 DOM 证据，并完成修复和复测闭环。

## 安装

将 Skill 目录复制到兼容的项目级或用户级目录，例如 `.agents/skills/`、`.cursor/skills/`、`.claude/skills/`、`.codex/skills/` 或对应的用户目录。

```powershell
Copy-Item -Recurse .\skills\* $env:USERPROFILE\.agents\skills
```

## 许可证

Copyright (c) 2026 Ninthless. All rights reserved.

这些 Skill 是专有的个人工作流材料。未经事先书面许可，不得复制、修改、重新分发、再发布、再许可，也不得用于创作衍生作品。
