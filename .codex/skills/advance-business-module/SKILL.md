---
name: advance-business-module
description: Safely start, continue, review, design, implement, or accept a business module in the 杏林骨科 project by loading its current module pool and confirmed cross-module interfaces first. Use for business-rule interviews, module handoffs, information architecture, page lists, page flows, low-fidelity or visual design, implementation, acceptance, or when opening a new task for 手术通知、手术植入、库存 or another explicitly registered module. Prevents reliance on long chat memory and prevents invention of undiscussed APP or Web functions.
---

# 推进业务模块

将项目文件视为跨任务记忆，将 Skill 视为推进工作流。不要把聊天长度或当前模型记忆当成事实来源。

## 1. 识别范围

1. 找到项目根目录。
2. 读取 `docs/00-当前范围与模块登记.md`。
3. 确认用户指定的模块、所属端和本次阶段。
4. 若模块未登记、仍是概念阶段或所属端未启动，只进行范围澄清和规则访谈；不得自动建立页面、状态、代码、接口或后台能力。

## 2. 接管已有模块

读取目标模块的 `00-START-HERE.md`，先输出一段简短接管摘要：

- 当前模块和所属端；
- 当前推进阶段；
- 本次实际读取的有效文件；
- 已知未决问题；
- 本次明确不进入的范围。

若找不到总池，先盘点已有资料并请用户确认其成熟度，再决定是否实例化；不要从文件编号、行业惯例或其他模块反推。

## 3. 按需加载资料

只读取完成当前任务所需的最小集合：

- 规则讨论：总池首页、当前规则、直接相关接口；
- 页面设计：再读取设计进度、页面清单、页面流程和目标页面资料；
- 代码实现：再读取当前设计与真实代码入口；
- 验收：再读取验收对象、规则依据和已确认接口。

历史池默认不读。只有追溯冲突或版本来源时才读取，并且不得让历史覆盖当前有效文件。

## 4. 继承跨模块内容

只通过已确认接口继承前一模块的结果：

- 读取来源模块在接口池中明确输出的对象、状态或结果；
- 读取目标模块明确接收的内容；
- 不把来源模块的内部流程、页面和操作复制到目标模块；
- 关联模块尚无总池或接口未确认时，将其标记为待讨论，不自行补全。

例如，手术植入可以接收手术通知已确认的来源订单和候选实物，但不能因此继承手术通知的完整要货、履约和结余流程。

## 5. 按阶段推进

通常按以下顺序推进：

1. 业务规则与边界；
2. 规则封板与验收；
3. 信息架构；
4. 页面清单；
5. 页面流程；
6. 低保真结构；
7. 视觉稿；
8. 代码实现；
9. 模块验收与跨模块联调。

从资料池标注的当前阶段继续，不重做已完成阶段。每次只推进用户明确指定的一项；发现冲突时暂停下游制作，先回到规则层确认。

## 6. 沉淀结果

任务形成有效结论后：

1. 更新对应规则、接口、设计、代码或验收子池；
2. 更新模块总池首页的当前版本、未决问题和下一步；
3. 被替代文件移入决策与历史池并注明替代关系；
4. 跨模块影响只更新已确认接口，不擅自改写另一模块；
5. 新模块或成熟度变化先更新范围登记。

总池保存“现在相信什么”，历史池保存“为什么走到这里”，Skill 保证“下一次怎样继续”。
