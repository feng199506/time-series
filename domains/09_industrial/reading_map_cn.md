# 工业与设备：阅读路线图

进度：已核验全文 50 / 目标约 50；待核验 1；下载失败 2。 近三年（已核验文献中）50 篇，占 1.0。
编号对应 [catalog_cn.csv](catalog_cn.csv)；简介与字段均依据摘要，未读全文。

## 优先阅读 10 篇

| 顺序 | 编号 | 标题 | 理由 |
|---|---|---|---|
| 1 | TS191 | [Leakage-Robust Evaluation and Data-Scale Sensitivity of Attention-Enhanced Multi-Task Learning for Joint Fault Diagnosis and Remaining Useful Life Estimation](../../pdfs/2026_Shamim_LeakageRobustEvaluationData_en.pdf) | 量化滑动窗口切分泄漏把准确率从 20-60% 抬到 99.9%，是数据集划分批评的直接证据。 |
| 2 | TS210 | [Auditing Operating-Condition Normalization in C-MAPSS Remaining Useful Life Evaluation](../../pdfs/2026_Gupta_AuditingOperatingConditionNormalization_en.pdf) | 1800 次受控运行显示归一化与重拟合策略会改变 C-MAPSS 的 RMSE 排名。 |
| 3 | TS190 | [CruiseBench: A Real-Flight-Aligned N-CMAPSS Benchmark for Engine RUL Prediction](../../pdfs/2026_Cheng_CruiseBench_en.pdf) | 给 N-CMAPSS 一个固定、可复现的巡航段协议。 |
| 4 | TS189 | [BatteryLife: A Comprehensive Dataset and Benchmark for Battery Life Prediction](../../pdfs/2025_Tan_BatteryLife_en.pdf) | 目前最广的电池寿命数据集与统一基准。 |
| 5 | TS192 | [Self-Supervised Pretraining for PHM: What Transfers, What Does Not, and What Federating It Costs](../../pdfs/2026_SanzDuran_SelfSupervisedPretrainingPHM_en.pdf) | 在泄漏受控条件下，预训练对 RUL 无稳定收益。 |
| 6 | TS202 | [Do Time-Series Foundation Models Pay Off for Industrial Monitoring? A Cost-Aware Empirical Study](../../pdfs/2026_Wen_DoTimeSeriesFoundation_en.pdf) | 计入成本后，轻量基线仍有竞争力。 |
| 7 | TS203 | [IND-Eval: Aligning Evaluation and Simulation for Industrial Time Series Foundation Models](../../pdfs/2026_Haugland_INDEval_en.pdf) | 专门面向工业时间序列的 TSFM 预测基准。 |
| 8 | TS199 | [Empirical Calibration and Conditional-Reliability Diagnostics for Bearing RUL Prediction under Operating-Regime Shift](../../pdfs/2026_Yang_EmpiricalCalibrationConditionalReliabili_en.pdf) | 按工况留出评测，并看条件覆盖率。 |
| 9 | TS196 | [RULSurv: A probabilistic survival-based method for early censoring-aware prediction of remaining useful life in ball bearings](../../pdfs/2024_Lillelund_RULSurv_en.pdf) | 在 RUL 建模中显式处理删失数据。 |
| 10 | TS197 | [Generalization bounds and sample complexity for remaining useful life prediction from complete degradation trajectories](../../pdfs/2026_Le_GeneralizationBoundsSampleComplexity_en.pdf) | 从理论上回答“需要多少条失效轨迹”。 |

## 按子方向

### 锂电池寿命预测 / 基准数据集
- TS189（高）[BatteryLife: A Comprehensive Dataset and Benchmark for Battery Life Prediction](../../pdfs/2025_Tan_BatteryLife_en.pdf) — 基准/数据集；目标：电池循环寿命（Battery Life Prediction）；方法：基准评测（含时间序列通用模型与电池专用基线）

### 涡扇发动机 RUL / N-CMAPSS 基准
- TS190（高）[CruiseBench: A Real-Flight-Aligned N-CMAPSS Benchmark for Engine RUL Prediction](../../pdfs/2026_Cheng_CruiseBench_en.pdf) — 基准/数据集；目标：航空发动机剩余使用寿命（RUL，循环）；方法：基准评测（LSTM、GRU、TCN、TSMixer 基线）

### 评测与泄漏批评
- TS191（高）[Leakage-Robust Evaluation and Data-Scale Sensitivity of Attention-Enhanced Multi-Task Learning for Joint Fault Diagnosis and Remaining Useful Life Estimation](../../pdfs/2026_Shamim_LeakageRobustEvaluationData_en.pdf) — 基准/数据集；目标：故障类别 + RUL 联合估计（重点在评测协议）；方法：深度学习（注意力多任务网络 AMTLNet）+ 统计检验（ANOVA、Tukey HSD）

### 工业基础模型 / 自监督预训练
- TS192（高）[Self-Supervised Pretraining for PHM: What Transfers, What Does Not, and What Federating It Costs](../../pdfs/2026_SanzDuran_SelfSupervisedPretrainingPHM_en.pdf) — 预测；目标：RUL（C-MAPSS）与故障分类（CWRU、HSG18）；方法：基础模型（通道独立 Transformer 编码器，掩码 patch 预训练，约 80 万参数）；集中式与联邦预训练

### 锂电池寿命预测 / 基础模型
- TS193（高）[Pretrained battery transformer (PBT): a foundation model for battery life prediction](../../pdfs/2025_Tan_PretrainedBatteryTransformerPBT_en.pdf) — 预测；目标：电池循环寿命（早期预测）；方法：基础模型（电池知识编码的混合专家 Transformer，通用 PBT + 场景专用 PBT）

### 数字孪生 / 时间序列基础模型
- TS194（高）[Grounding Time-Series Foundation Models in Digital Twin Topology for Predictive Maintenance](../../pdfs/2026_Ma_GroundingTimeSeriesFoundation_en.pdf) — 预测；目标：涡扇发动机 RUL；方法：基础模型（五个冻结骨干的 TSFM 对比）+ 数字孪生拓扑信息

### 不确定性 RUL / 涡扇发动机
- TS195（高）[Bayesian Deep Learning for Remaining Useful Life Estimation via Stein Variational Gradient Descent](../../pdfs/2024_Libera_BayesianDeepLearningRemaining_en.pdf) — 预测；目标：RUL 及其置信区间；方法：深度学习（贝叶斯神经网络，Stein 变分梯度下降训练）

### 轴承 RUL / 生存分析
- TS196（高）[RULSurv: A probabilistic survival-based method for early censoring-aware prediction of remaining useful life in ball bearings](../../pdfs/2024_Lillelund_RULSurv_en.pdf) — 预测；目标：轴承失效时间（RUL，分钟）；方法：统计 + 机器学习（KL 散度早期故障检测；CoxPH、随机生存森林）

### RUL 理论 / 样本复杂度
- TS197（高）[Generalization bounds and sample complexity for remaining useful life prediction from complete degradation trajectories](../../pdfs/2026_Le_GeneralizationBoundsSampleComplexity_en.pdf) — 预测；目标：RUL（理论分析，验证于涡扇、电池、轴承基准）；方法：统计学习理论（泛化界、极小极大下界、Bernstein 型分析）

### 随机退化模型 / Gamma 过程
- TS198（高）[Bayesian Hierarchical Modelling of Noisy Gamma Processes: Model Formulation, Identifiability, Model Fitting, and Extensions to Unit-to-Unit Variability](../../pdfs/2024_Leadbetter_BayesianHierarchicalModellingNoisy_en.pdf) — 预测；目标：单调退化量（含测量误差）与失效；方法：统计（贝叶斯分层带噪 Gamma 过程）

### 评测与泄漏批评 / 轴承 RUL 不确定性
- TS199（高）[Empirical Calibration and Conditional-Reliability Diagnostics for Bearing RUL Prediction under Operating-Regime Shift](../../pdfs/2026_Yang_EmpiricalCalibrationConditionalReliabili_en.pdf) — 预测；目标：轴承 RUL 点预测与 90% 预测区间；方法：深度学习表征 + 经验残差校准；对比 400 棵树随机森林

### 锂电池容量衰减轨迹预测
- TS200（高）[BatteryMFormer: Multi-level Learning for Battery Degradation Trajectory Forecasting](../../pdfs/2026_Tan_BatteryMFormer_en.pdf) — 预测；目标：全寿命 SOH 退化轨迹（由早期数据预测）；方法：深度学习（多层级 Transformer：老化工况感知解码器、退化模式记忆、双视角编码器）

### 工业基础模型 / RUL
- TS201（高）[Time-Series Foundation Model Embeddings for Remaining Useful Life Estimation](../../pdfs/2026_ElGhoussani_TimeSeriesFoundationModel_en.pdf) — 预测；目标：RUL；方法：基础模型（冻结 Chronos-2 提取特征 + 轻量回归头）

### 工业基础模型 / 实证评估（以异常检测与风险排序为主）
- TS202（高）[Do Time-Series Foundation Models Pay Off for Industrial Monitoring? A Cost-Aware Empirical Study](../../pdfs/2026_Wen_DoTimeSeriesFoundation_en.pdf) — 异常检测；目标：C-MAPSS 退化风险代理、MIMII 异常声音、BDG2 预测残差诊断；方法：对比：单类方法、紧凑自编码器、残差预测器、MOMENT、Chronos-T5、TimesFM 2.5

### 工业基础模型 / 预测基准
- TS203（高）[IND-Eval: Aligning Evaluation and Simulation for Industrial Time Series Foundation Models](../../pdfs/2026_Haugland_INDEval_en.pdf) — 基准/数据集；目标：多源工业传感器时间序列的点预测与概率预测；方法：基础模型评测（Chronos-2、TiRex-2、TimesFM-3）+ 基于统计结构的仿真器设计

### 工业多变量传感器预测 / 物理引导
- TS204（高）[DSPR: Dual-Stream Physics-Residual Networks for Trustworthy Industrial Time Series Forecasting](../../pdfs/2026_Zhang_DSPR_en.pdf) — 预测；目标：工业多变量过程时间序列；方法：物理-数据融合（双流：统计时间演化 + 物理引导动态图与自适应传输时滞窗口）

### 过程工业预测 / 生物制药细胞培养
- TS205（高）[Multipath Adaptive Gated Bottleneck Latent ODE with Raman Data Fusion for Cell Culture Process Forecasting](../../pdfs/2026_Peng_MultipathAdaptiveGatedBottleneck_en.pdf) — 预测；目标：细胞培养关键工艺参数的多日轨迹；方法：深度学习（门控瓶颈 Latent ODE + 多路径即时微调 MP-JIT-FT 检索相似历史轨迹）

### 锂电池容量衰减轨迹预测 / 梯次利用
- TS206（高）[iMOE: prediction of second-life battery degradation trajectory using interpretable mixture of experts](../../pdfs/2026_Huang_IMOE_en.pdf) — 预测；目标：退役动力电池全寿命容量退化轨迹；方法：深度学习（可解释混合专家 + 使用依赖循环网络）

### 涡轮发动机健康管理 / 多任务概率预测
- TS207（高）[Scientific Machine Learning for Engine Health Management and Remaining Useful Life Prediction](../../pdfs/2026_BarryStraume_ScientificMachineLearningEngine_en.pdf) — 预测；目标：涡轮燃气温度 TGTU、ΔTGT 与 RUL（含预测区间）；方法：深度学习（卷积前端 + 残差双向 LSTM + 注意力池化，多任务均值-方差头，可选生存头）

### 不确定性 RUL / 保形预测
- TS208（高）[Remaining Useful Life Estimation for Aircraft Engines with Risk-Aware Prediction Intervals via Conformalized Quantile Regression](../../pdfs/2026_Robinson_RemainingUsefulLifeEstimation_en.pdf) — 预测；目标：航空发动机 RUL 点预测与非对称预测区间；方法：机器学习（梯度提升回归 + 非对称保形分位数回归 CQR）

### 评测与泄漏批评 / RUL 标签设计
- TS209（高）[When Linear RUL Labels Disagree with Vibration Degradation: A Stage-Aware Target and Dual-Scale Predictor Evaluated on XJTU-SY and IMS](../../pdfs/2026_ShirMohammad_WhenLinearRULLabels_en.pdf) — 预测；目标：轴承退化状态目标（替代线性 RUL 标签）；方法：深度学习（CNN-LSTM 与 Transformer，OWA 融合）+ 分段线性-二次-指数目标

### 评测与泄漏批评 / C-MAPSS
- TS210（高）[Auditing Operating-Condition Normalization in C-MAPSS Remaining Useful Life Evaluation](../../pdfs/2026_Gupta_AuditingOperatingConditionNormalization_en.pdf) — 基准/数据集；目标：涡扇发动机 RUL（评测协议审计）；方法：受控探针模型（MLP、时间 CNN、LSTM）+ 析因实验

### 随机退化模型 / 多性能指标相依退化
- TS211（中）[Modeling dependent degradation data considering inherent causal relationships for reliability analysis and remaining useful life prediction](../../pdfs/2026_Chen_ModelingDependentDegradationData_en.pdf) — 预测；目标：多性能指标退化路径、可靠度与 RUL；方法：统计（Wiener 过程 + 稳定 PC 因果发现）

### 涡扇发动机 RUL / 图神经网络
- TS212（中）[Temporal and Heterogeneous Graph Neural Network for Remaining Useful Life Prediction](../../pdfs/2024_Wen_TemporalHeterogeneousGraphNeural_en.pdf) — 预测；目标：航空发动机 RUL；方法：深度学习（时间异构图神经网络 THGNN + FiLM）

### 涡扇发动机 RUL / 可解释性
- TS213（中）[Interpretable Prognostics with Concept Bottleneck Models](../../pdfs/2024_Forest_InterpretablePrognosticsConceptBottlenec_en.pdf) — 预测；目标：航空发动机 RUL；方法：深度学习（概念瓶颈模型，以退化模式为中间概念）

### 锂电池退化预测 / 生成模型
- TS215（中）[DiffBatt: A Diffusion Model for Battery Degradation Prediction and Synthesis](../../pdfs/2024_Eivazi_DiffBatt_en.pdf) — 预测；目标：电池容量衰减曲线与 RUL（循环）；方法：深度学习（条件/无条件扩散模型 + Transformer，无分类器引导）

### 锂电池 RUL / 概率预测
- TS216（中）[RUL-QMoE: Multiple Non-crossing Quantile Mixture-of-Experts for Probabilistic Remaining Useful Life Predictions of Varying Battery Materials](../../pdfs/2025_Ly_RULQMoE_en.pdf) — 预测；目标：电池 RUL 的非交叉分位数；方法：深度学习（按材料的混合专家 + 非交叉分位数回归）

### 储能系统电池退化 / 概率预测
- TS217（中）[Predicting BESS Degradation with Uncertainty Quantification: A Probabilistic Framework for Battery Energy Storage Systems](../../pdfs/2026_Graner_PredictingBESSDegradationUncertainty_en.pdf) — 预测；目标：电池储能系统 SOH 退化（含 95% 预测区间）；方法：混合（深度学习生成应力条件下容量损失分布 + 随机退化轨迹传播 + 系统拓扑聚合）

### 锂电池 RUL / 路径依赖与状态定义
- TS218（中）[The Case for DeepSOH: Addressing Path Dependency for Remaining Useful Life](../../pdfs/2024_Movahedi_CaseDeepSOHAddressingPath_en.pdf) — 预测；目标：电池 RUL（论证所需状态量）；方法：物理-数据融合（电化学退化机理仿真与状态估计分析）

### 刀具磨损预测
- TS219（中）[Data-driven tool wear prediction in milling, based on a process-integrated single-sensor approach](../../pdfs/2024_Hirsch_DataDrivenToolWear_en.pdf) — 预测；目标：铣削刀具磨损量；方法：深度学习/机器学习（Transformer 启发 CNN、LSTM 等）+ 迁移学习

### 软测量 / 多单元半监督
- TS221（中）[A deep latent variable model for semi-supervised multi-unit soft sensing in industrial processes](../../pdfs/2024_Grimstad_DeepLatentVariableModel_en.pdf) — 预测；目标：多相流流量等难测过程变量（软测量估计）；方法：深度学习（分层生成式深度潜变量模型，半监督 + 多任务）

### 软测量 / 大语言模型
- TS222（中）[A Text-Based Knowledge-Embedded Soft Sensing Modeling Approach for General Industrial Process Tasks Based on Large Language Model](../../pdfs/2025_Tong_TextKnowledgeEmbeddedSoft_en.pdf) — 预测；目标：过程工业关键性能指标（软测量）；方法：基础模型（LLM 微调 + 辅助变量序列编码器 AVS Encoder，两阶段对齐）

### 软测量 / 跨工厂迁移
- TS223（低）[Transferring Graph Neural Networks for Soft Sensor Modeling using Process Topologies](../../pdfs/2025_Theisen_TransferringGraphNeuralNetworks_en.pdf) — 预测；目标：粘度、产品浓度等难测过程量（软测量）；方法：深度学习（拓扑感知图神经网络 + 迁移学习）

### 工业基础模型 / 表格基础模型
- TS224（中）[Towards Unified and Data-Efficient Prognostics and Health Management with Tabular Foundation Models](../../pdfs/2026_Theiler_TowardsUnifiedDataEfficient_en.pdf) — 预测；目标：RUL 估计与诊断等多种 PHM 任务；方法：基础模型（表格基础模型，上下文学习）

### 工业基础模型 / 少样本 RUL
- TS225（中）[PEFT-MuTS: A Multivariate Parameter-Efficient Fine-Tuning Framework for Remaining Useful Life Prediction based on Cross-domain Time Series Representation Model](../../pdfs/2026_Fu_PEFTMuTS_en.pdf) — 预测；目标：少样本条件下的 RUL；方法：基础模型（跨领域预训练时间序列表征模型 + 多变量参数高效微调）

### 随机退化模型 / 联合模型
- TS226（中）[Bayesian Joint Model of Multi-Sensor and Failure Event Data for Multi-Mode Failure Prediction](../../pdfs/2025_Fard_BayesianJointModelMulti_en.pdf) — 预测；目标：多失效模式下的 RUL 与失效模式；方法：统计（贝叶斯联合模型：多传感器纵向数据 + 多模式失效事件）

### 生存分析 / 联邦预测
- TS227（中）[Collaborative System Failure Prognostics via Federated Longitudinal-Survival Modeling](../../pdfs/2026_Yang_CollaborativeSystemFailurePrognostics_en.pdf) — 预测；目标：时变失效风险、可靠度与 RUL；方法：统计 + 深度学习（纵向传感器表征 + Cox 比例风险，联邦学习）

### 数字孪生 / 核电设备退化预测
- TS228（中）[Digital twin-based hybrid framework for steam generator clogging prognostics](../../pdfs/2026_Jaber_DigitalTwinHybridFramework_en.pdf) — 预测；目标：蒸汽发生器管子支撑板堵塞率与 RUL；方法：物理-数据融合（物理仿真 + 多种不确定性量化技术）

### 铁路轨道几何退化预测
- TS229（中）[Sensor fusion for track geometry monitoring: integrating on-board condition monitoring and degradation models via Kalman filtering](../../pdfs/2025_TruongBa_SensorFusionTrackGeometry_en.pdf) — 预测；目标：轨道几何指标退化；方法：统计（卡尔曼滤波融合退化模型与车载振动信号）

### 风电齿轮箱 RUL / 不确定性
- TS230（中）[Accurate remaining useful life prediction and uncertainty quantification for wind turbines using temporal convolutional variational deep Gaussian processes](../../pdfs/2026_Cui_AccurateRemainingUsefulLife_en.pdf) — 预测；目标：风电机组齿轮箱 RUL 及置信区间；方法：混合（TCN + 序列注意力 + 变分深度高斯过程）

### 燃料电池电压退化 / RUL
- TS232（低）[A temporal scale transformer framework for precise remaining useful life prediction in fuel cells](../../pdfs/2025_Tang_TemporalScaleTransformerFramework_en.pdf) — 预测；目标：质子交换膜燃料电池（PEMFC）RUL / 性能退化；方法：深度学习（Temporal Scale Transformer，基于 iTransformer 的多尺度 token）

### 功率电子器件 RUL
- TS233（低）[Long Short-Term Memory Mixture Density Network for Remaining Useful Life Prediction of IGBTs](../../pdfs/2025_Cruz_LongShortTermMemory_en.pdf) — 预测；目标：IGBT 剩余使用寿命（概率分布）；方法：深度学习（LSTM + 混合密度网络）

### 半导体制造设备 RUL / 决策指标
- TS234（中）[Uncertainty and Business-Aware Remaining Useful Life Estimation for Semiconductor Manufacturing](../../pdfs/2026_Frizzo_UncertaintyBusinessAwareRemaining_en.pdf) — 预测；目标：离子铣设备 RUL 分位数与维修决策；方法：深度学习（含状态空间模型 SSM 的序列模型）+ 同时分位数回归 SQR

### 故障预警 / 预测窗口设计
- TS235（高）[Predicting Machine Failures from Multivariate Time Series: An Industrial Case Study](../../pdfs/2024_Vago_PredictingMachineFailuresMultivariate_en.pdf) — 预警；目标：未来预测窗口内是否发生故障（二分类）；方法：机器学习 + 深度学习（六种算法，含逻辑回归等）

### 故障预警 / 变点检测
- TS236（中）[Gaussian Derivative Change-point Detection for early warnings of industrial system failures](../../pdfs/2024_Zhao_GaussianDerivativeChangePoint_en.pdf) — 预警；目标：即将发生的系统失效预警；方法：统计（Gaussian 导数过程多元变点检测 + 加权马氏距离阈值）

### 综述 / 图神经网络 RUL
- TS237（中）[A survey on graph neural networks for remaining useful life prediction: Methodologies, evaluation and future trends](../../pdfs/2024_Wang_SurveyGraphNeuralNetworks_en.pdf) — 综述；目标：RUL（综述）；方法：综述（图构建、图建模、图信息处理、图读出四阶段分类）

### 饮用水厂运行数据在线预测（强化学习预测）
- TS160（低）[GVFs in the real world: making predictions online for water treatment](../../pdfs/2023_Janjua_GVFsRealWorldMaking_en.pdf) — 预测；目标：水厂传感器变量的广义价值函数（折扣累积和）预测；方法：深度学习/强化学习（TD 学习的 GVF 预测）对比 n 步预测

### 工业污水处理溶解氧预测：迁移学习 + 物理信息
- TS165（低）[A Hybrid Approach of Transfer Learning and Physics-Informed Modeling: Improving Dissolved Oxygen Concentration Prediction in an Industrial Wastewater Treatment Plant](../../pdfs/2024_Koksal_HybridApproachTransferLearning_en.pdf) — 预测；目标：工业污水处理单元溶解氧浓度；方法：物理-数据融合（迁移学习 + 物理信息目标函数）

### 污水厂传感器缺测插补（扩散模型）
- TS184（低）[STDiff: A state transition diffusion framework for time series imputation in industrial systems](../../pdfs/2025_Simethy_STDiff_en.pdf) — 插补；目标：污水厂关键传感器缺测段；方法：深度学习（扩散模型 STDiff/STDiff-W）对比 SAITS、BRITS、CSDI

### 污水厂数字孪生开环模拟（12–36 小时）
- TS188（低）[Data-Driven Open-Loop Simulation for Digital-Twin Operator Decision Support in Wastewater Treatment](../../pdfs/2026_Simethy_DataDrivenOpenLoop_en.pdf) — 预测；目标：污水厂传感器状态（规定控制方案下的响应）；方法：深度学习（受控连续时间状态空间模型 CCSS-RS）

