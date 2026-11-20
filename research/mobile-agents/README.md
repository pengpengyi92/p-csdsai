# 手机 Agent 与研究工作流

Author: Pengyi Peng / P-CSDSAI. Source cutoff:2026-11-19T23:26:41+08:00 (Asia/Shanghai).

[专题报告](../../report/2026-11-19-phonego-mobile-agents.md)说明PhoneGo如何作为可选执行层，
向PDD证据研究、PFF轻量研究、PPRT开源工程交接。三个prop repo仅作职责介绍，无私库链接或资料。
[源码卡](../../repo/ai/mobile-agents/phonego.md) · [固定12任务协议](PROTOCOL.json)。

本次仅新增公开目录、原创报告和拟定协议。未实现私库连接器、未赋予Agent写入/发送权，
未安装APK、接入真实设备、调用模型或运行新手机任务；**PROPOSED_NOT_IMPLEMENTED / NOT RUN / UNMEASURED**。

## 接入前要求

先批准具体设备、App与资料权利、模型端点、数据范围和总预算；保留官方网页/API与人工基线。
再冻结任务、金标准、版本和内容指纹，核实只读边界、取消和预算停止机制。
最后才实现候选包交接：原始来源、时间、状态、脱敏和人工核对分开记录，不允许手机直接入正式库或外发。

## 离线检查

```sh
python -X utf8 -m unittest discover -s tests -p 'test_phonego_mobile_agents.py' -v
python -X utf8 scripts/publish_phonego_report.py --check
```

这些只验证公开元数据、目录、链接、报告与拟定协议的契约，不证明真实设备可用。
实际完整回归及应用边界见本期CHECKS.json；Report发布后的作者、类别和正文精确匹配见
repo/ai/mobile-agents/PUBLICATION.json，不以“已写文件”代替“已发布”。
