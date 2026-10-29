# 通用方法：阅读路线图（按主题）

编号对应 [catalog_cn.csv](catalog_cn.csv)，PDF 在 [pdfs/](../../pdfs/)。【旧】为三年前的补充/基础文献（不计入近三年数量）。
简介与判断依据均为摘要，未读全文；文中“作者称”的结论未经核实。

## 0. 建议最先阅读的 10 篇

| 顺序 | 编号 | 文献 | 理由 |
|---|---|---|---|
| 1 | TS054【旧】 | Hyndman & Khandakar 2008，auto.arima / ETS | 近期基准里的统计基线（AutoARIMA/AutoETS）都按此文定义；先弄清“基线是什么”。[PDF](../../pdfs/2008_Hyndman_AutomaticTimeSeriesForecasting_en.pdf) |
| 2 | TS055【旧】 | Hyndman & Koehler 2006，MASE | GIFT-Eval、fev-bench、Chronos 的主指标之一；理解 MAPE 等指标为何会退化。[PDF](../../pdfs/2006_Hyndman_AnotherLookMeasuresForecast_en.pdf) |
| 3 | TS056【旧】 | Gneiting & Raftery 2007，严格正常评分规则 | CRPS / WQL / 区间分数的理论来源，读懂所有概率预测评测的前提。[PDF](../../pdfs/2007_Gneiting_StrictlyProperScoringRules_en.pdf) |
| 4 | TS058【旧】 | Zeng et al. 2022，DLinear | 近三年深度/基础模型论文的必比简单基线；TS027、TS029、TS031 都在回应它。[PDF](../../pdfs/2022_Zeng_TransformersEffectiveTimeSeries_en.pdf) |
| 5 | TS023 | Deep Time Series Models 综述 + TSLib | 深度学习路线的地图（模块、架构、统一基准），读完再看单篇模型更高效。[PDF](../../pdfs/2024_Wang_DeepTimeSeriesModels_en.pdf) |
| 6 | TS048 | There are no Champions（长期预测） | 说明 LTSF 排名对设定极敏感，读其他模型论文时用来校准对“SOTA”结论的信任度。[PDF](../../pdfs/2025_Brigato_ThereNoChampionsSupervised_en.pdf) |
| 7 | TS049 | TSFM 评测中的信息泄漏 | 基础模型零样本结论是否可信的关键：预训练-测试重叠与时间重叠。[PDF](../../pdfs/2025_Meyer_RethinkingEvaluationEraTime_en.pdf) |
| 8 | TS047 | fev-bench | 现行基础模型基准之一，且给出统计上更严谨的汇总（自助法置信区间、胜率与技能分）。[PDF](../../pdfs/2025_Shchur_FevBench_en.pdf) |
| 9 | TS032 | Chronos | 基础模型路线的代表与后续工作（Chronos-2、ChronosX、fev-bench）的起点。[PDF](../../pdfs/2024_Ansari_Chronos_en.pdf) |
| 10 | TS016 | 共形时间序列预测入门综述 | 预测区间与校准的现代方法总览，补足点预测之外的不确定性评估。[PDF](../../pdfs/2025_Stocker_GentleIntroductionConformalTime_en.pdf) |

紧随其后：TS043（LLM 是否真的有用）、TS040（Chronos-2）、TS045（GIFT-Eval）、TS031（线性模型分析）、TS057【旧】（交叉验证有效性）。

## A. 基础分析
1. 分解：TS001 xPatch（指数分解进入深度模型）→ TS002 BASTION（统计学的贝叶斯分解，含与 MSTL/STR/TBATS 的比较）。
2. 频谱：TS003 频域分析综述 → TS025 TSLANet（自适应频谱块）、TS006 FreDF（频域损失）。
3. 平稳性与非平稳：TS004 FAN（频率自适应归一化）→ TS005 TAFAS（部署期测试时自适应）。
4. 自相关：TS006 FreDF（标签自相关使直接多步目标有偏）；与 TS017 的“多步误差自相关”对照阅读。
5. 状态空间：TS007 ABC 状态空间预测（统计学，误设情形）→ TS008 S-Mamba（深度学习语境下的“状态空间”）。
6. 结构突变：TS009 多重变点检验实证指南 → TS010 结构突变下的区间预测（统计 vs 神经网络）。

缺口：近三年专门研究经典单位根/平稳性检验、经典谱估计、卡尔曼滤波本身的方法论文本轮未纳入合适条目（检索到的多为应用或计量理论）。

## B. 经典预测
1. 基线定义：TS054【旧】auto.arima / ETS。
2. 指数平滑理论：TS011（简单指数平滑 = 对高斯对数似然的随机梯度上升）。
3. ARIMA 多变量推广与 VAR：TS012 VARMA 综述 → TS013 从 VAR 到 AI 预测的综述。
4. 概率预测：TS014 概率预测综述 → TS015 多变量正常评分规则（聚合与变换）。
5. 预测区间：TS016 共形综述 → TS017 多步在线共形（AcMCP）。

缺口：“动态回归”（ARIMA 误差回归）近三年少有直接方法论文；本库以 TS026 TimeXer、TS041 ChronosX、TS020 签名特征回归作为“带外生变量预测”的近期代表。

## C. 机器学习
1. 树模型：TS018 零售 GBDT 概率预测实践。
2. 特征工程：TS019 时间特征（TimeSter）→ TS020 签名特征 → TS021 TabPFN-TS（特征化 + 表格基础模型）。
3. 全局模型：TS022 间歇序列上的局部 vs 全局。

缺口：近三年 GBDT 与深度模型的严谨对比研究偏少（本轮只找到应用型或 2021 年前的工作），是本库最薄的子主题。

## D. 深度学习
1. 先读 TS023 综述 + TSLib。
2. 简单基线与批评：TS058【旧】DLinear → TS031 线性模型分析 → TS029 SparseTSF → TS030 CycleNet → TS027 CATS（自注意力是否有效）。
3. 各架构代表：RNN TS024 xLSTM-Mixer；CNN TS025 TSLANet；Transformer TS026 TimeXer；MLP TS028 TimeMixer；状态空间 TS008 S-Mamba。
4. 读完后回到 TS048，检验这些模型的比较结论有多稳。

## E. 时间序列基础模型
1. 综述：TS044。
2. 预训练与零样本：TS032 Chronos → TS033 Moirai → TS034 Timer → TS035 TTM（小模型）→ TS036 Time-MoE（扩展）。
3. 2025 年代表：TS038 TiRex（xLSTM）、TS039 Sundial（流匹配）、TS037 Toto + BOOM、TS040 Chronos-2（协变量）。
4. 迁移与适配：TS041 ChronosX（适配器注入协变量）、TS042 上下文微调；对照 TS021 TabPFN-TS（非时间序列预训练的零样本）。
5. 批评：TS043（LLM 组件可去掉）、TS049（泄漏）。

## F. 评测方法
1. 指标与评分：TS055【旧】MASE → TS056【旧】正常评分规则 → TS053 多序列上的分数汇总（均值缩放分数）→ TS015 多变量评分。
2. 时间切分与交叉验证：TS057【旧】→ TS052（CV 的有限样本偏差）→ TS051（泄漏与验证设计）。
3. 基准：TS046 TFB → TS045 GIFT-Eval → TS047 fev-bench → TS050 TempusBench。
4. 对现有评测的批评：TS048（没有冠军）、TS049（TSFM 泄漏）、TS050（过时数据与重叠）。
5. 区间与校准：TS016、TS017（见 B.5）。
