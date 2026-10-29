# 交通与出行：阅读路线图

进度：已核验全文 51 / 目标约 50；待核验 1；下载失败 0。 近三年（已核验文献中）49 篇，占 0.961。
编号对应 [catalog_cn.csv](catalog_cn.csv)；简介与字段均依据摘要，未读全文。

## 优先阅读 10 篇

| 顺序 | 编号 | 标题 | 理由 |
|---|---|---|---|
| 1 | TS448 | [A Critical Audit of Spatiotemporal Forecasting Benchmark Datasets and Models](../../pdfs/2026_Martin_CriticalAuditSpatiotemporalForecasting_en.pdf) | A Critical Audit of Spatiotemporal Forecasting Benchmark Datasets and Models。调好时间线性基线后，GNN 的增益显著缩小或被反超，解读排行榜前应先读。 |
| 2 | TS449 | [Time Series Foundation Models as Strong Baselines in Transportation Forecasting: A Large-Scale Benchmark Analysis](../../pdfs/2026_YanesPulido_TimeSeriesFoundationModels_en.pdf) | Time Series Foundation Models as Strong Baselines in Transportation Forecasting。Chronos-2 零样本在 10 个交通数据集上有竞争力，应作为必备基线。 |
| 3 | TS450 | [Do We Really Need Adaptive Global Spatial Attention for Traffic Forecasting?](../../pdfs/2026_Zhang_DoWeReallyNeed_en.pdf) | Do We Really Need Adaptive Global Spatial Attention for Traffic Forecasting?。受控消融显示空间注意力相对均匀混合没有一致优势。 |
| 4 | TS451 | [XXLTraffic: Expanding and Extremely Long Traffic forecasting beyond test adaptation](../../pdfs/2024_Yin_XXLTraffic_en.pdf) | XXLTraffic。超长时间跨度且有分布漂移的交通基准，检验部署期稳健性。 |
| 5 | TS452 | [RideBench: A Large-Scale Exogenous-Aware Benchmark for Ride-Hailing Time Series Forecasting](../../pdfs/2026_Lin_RideBench_en.pdf) | RideBench。带天气、节假日、大型活动外生标注的滴滴网约车基准。 |
| 6 | TS453 | [Open Spatio-Temporal Foundation Models for Traffic Prediction](../../pdfs/2024_Li_OpenSpatioTemporalFoundation_en.pdf) | OpenCity。开源交通时空基础模型，可与 rank 2 的通用 TSFM 对照。 |
| 7 | TS455 | [Incident-Guided Spatiotemporal Traffic Forecasting](../../pdfs/2026_Fan_IncidentGuidedSpatiotemporalTraffic_en.pdf) | Incident-Guided Spatiotemporal Traffic Forecasting。把事件影响拆成空间扩散与时间衰减，并附对齐数据集。 |
| 8 | TS456 | [Predicting subway passenger flows under incident situation with causality](../../pdfs/2024_Huang_PredictingSubwayPassengerFlows_en.pdf) | Predicting Subway Passenger Flows under Incident Situation with Causality。用合成控制估计事件因果效应，再嵌入预测。 |
| 9 | TS457 | [Hierarchical Forecast Reconciliation for Urban Rail Transit Demand Prediction under Operational Disruptions](../../pdfs/2026_Nguyen_HierarchicalForecastReconciliationUrban_en.pdf) | Hierarchical Forecast Reconciliation for Urban Rail Transit Demand Prediction under Operational Disruptions。站点与 OD 层次一致性，扰动期效果有提升，并如实报告与统计方法相当。 |
| 10 | TS458 | [Conditional forecasting of bus travel time and passenger occupancy with Bayesian Markov regime-switching vector autoregression](../../pdfs/2024_Chen_ConditionalForecastingBusTravel_en.pdf) | Bayesian Markov regime-switching VAR for bus travel time and occupancy（TR-B）。高质量统计方法，给出联合不确定性。 |

## 按子方向

### 评测批评：时空基准与 GNN 基线审计
- TS448（高）[A Critical Audit of Spatiotemporal Forecasting Benchmark Datasets and Models](../../pdfs/2026_Martin_CriticalAuditSpatiotemporalForecasting_en.pdf) — 基准/数据集；目标：交通等时空基准上的多步预测（速度/流量，具体变量随数据集）；方法：统计 | 深度学习（时间线性基线 vs GNN 审计）

### 交通基础模型零样本评测
- TS449（高）[Time Series Foundation Models as Strong Baselines in Transportation Forecasting: A Large-Scale Benchmark Analysis](../../pdfs/2026_YanesPulido_TimeSeriesFoundationModels_en.pdf) — 基准/数据集；目标：高速公路交通量/流量、城市路段速度、共享单车需求、EV 充电站数据；方法：基础模型（Chronos-2 零样本）vs 统计与专用深度学习

### 评测批评：空间注意力消融
- TS450（高）[Do We Really Need Adaptive Global Spatial Attention for Traffic Forecasting?](../../pdfs/2026_Zhang_DoWeReallyNeed_en.pdf) — 预测；目标：交通流量/速度（六个交通基准）；方法：深度学习（受控消融：空间注意力 vs 均匀全范围混合）

### 基准数据集：超长时间跨度与分布漂移
- TS451（高）[XXLTraffic: Expanding and Extremely Long Traffic forecasting beyond test adaptation](../../pdfs/2024_Yin_XXLTraffic_en.pdf) — 基准/数据集；目标：道路交通流量；方法：其他（数据集与基准）

### 网约车需求：外生变量基准
- TS452（高）[RideBench: A Large-Scale Exogenous-Aware Benchmark for Ride-Hailing Time Series Forecasting](../../pdfs/2026_Lin_RideBench_en.pdf) — 基准/数据集；目标：网约车市场时间序列（需求等，具体变量待全文核实）；方法：基准（30+ 方法：内生模型、外生感知模型、时间序列基础模型）

### 交通时空基础模型（零样本）
- TS453（高）[Open Spatio-Temporal Foundation Models for Traffic Prediction](../../pdfs/2024_Li_OpenSpatioTemporalFoundation_en.pdf) — 预测；目标：交通流量/速度等；方法：基础模型（Transformer + GNN 预训练）

### 时空 LLM（指令微调）
- TS454（高）[UrbanGPT: Spatio-Temporal Large Language Models](../../pdfs/2024_Li_UrbanGPT_en.pdf) — 预测；目标：城市时空变量（交通、人流等）；方法：基础模型（时空依赖编码器 + 指令微调 LLM）

### 事件影响：事故/恶劣天气引导
- TS455（高）[Incident-Guided Spatiotemporal Traffic Forecasting](../../pdfs/2026_Fan_IncidentGuidedSpatiotemporalTraffic_en.pdf) — 预测；目标：交通流量；方法：深度学习（IGSTGNN：事件上下文空间融合 + 时间衰减模块）

### 地铁客流：事故情形下的因果分解
- TS456（高）[Predicting subway passenger flows under incident situation with causality](../../pdfs/2024_Huang_PredictingSubwayPassengerFlows_en.pdf) — 预测；目标：地铁客流；方法：混合（正常情形预测模型 + 合成控制法估计事件因果效应 + 效应预测模型）

### 城轨需求：站点-OD 层次协调
- TS457（高）[Hierarchical Forecast Reconciliation for Urban Rail Transit Demand Prediction under Operational Disruptions](../../pdfs/2026_Nguyen_HierarchicalForecastReconciliationUrban_en.pdf) — 预测；目标：站点进/出站量与 OD 客流（层次一致）；方法：混合（神经全连接协调器 FCR vs MinT 等统计/机器学习协调）

### 公交旅行时间与满载率（统计）
- TS458（高）[Conditional forecasting of bus travel time and passenger occupancy with Bayesian Markov regime-switching vector autoregression](../../pdfs/2024_Chen_ConditionalForecastingBusTravel_en.pdf) — 预测；目标：公交旅行时间与车内载客量（联合，含不确定性）；方法：统计（贝叶斯马尔可夫状态切换 VAR + MCMC）

### 极端天气下城轨 OD 客流（物理类比约束）
- TS459（高）[OhmicFlow: Forecasting transit passenger flow under extreme weather disruptions via Ohm's law](../../pdfs/2026_Li_OhmicFlow_en.pdf) — 预测；目标：极端天气扰动下的 OD 客流（并推断潜在需求与出行阻抗）；方法：物理-数据融合（欧姆定律类比：需求=电压、阻抗=电阻、客流=电流）

### 评测批评：自适应节点嵌入的泛化缺陷
- TS460（中）[Unveiling the Inflexibility of Adaptive Embedding in Traffic Forecasting](../../pdfs/2024_Wang_UnveilingInflexibilityAdaptiveEmbedding_en.pdf) — 预测；目标：道路交通流量/速度（具体待全文核实）；方法：深度学习（PCA 嵌入替代可学习节点嵌入）

### 大规模路网：无空间关系的全 MLP
- TS461（中）[RPMixer: Shaking Up Time Series Forecasting with Random Projections for Large Spatial-Temporal Data](../../pdfs/2024_Yeh_RPMixer_en.pdf) — 预测；目标：交通流量（大规模时空基准）；方法：深度学习（全 MLP + 随机投影）

### 大规模路网：超轻量通道独立模型
- TS462（中）[UltraSTF: Ultra-Compact Model for Large-Scale Spatio-Temporal Forecasting](../../pdfs/2025_Yeh_UltraSTF_en.pdf) — 预测；目标：交通流量（LargeST）；方法：深度学习（跨周期分量 + 形状库注意力）

### 大规模路网：空间分块 Transformer
- TS463（中）[Efficient Large-Scale Traffic Forecasting with Transformers: A Spatial Data Management Perspective](../../pdfs/2024_Fang_EfficientLargeScaleTraffic_en.pdf) — 预测；目标：道路交通流量；方法：深度学习（PatchSTG：KD 树不规则空间分块 + 深度/广度注意力）

### 持续学习：传感器网络扩张
- TS464（中）[Expand and Compress: Exploring Tuning Principles for Continual Spatio-Temporal Graph Forecasting](../../pdfs/2024_Chen_ExpandAndCompress_en.pdf) — 预测；目标：交通流量（并含空气质量、风能等）；方法：深度学习（STGNN + 连续提示池，提示微调）

### 分布漂移：在线测试时适应
- TS465（中）[Online Test-Time Adaptation of Spatial–Temporal Traffic Flow Forecasting](../../pdfs/2024_Guo_OnlineTestTimeAdaptation_en.pdf) — 预测；目标：交通流量；方法：深度学习（ADCSD：季节/趋势双修正的轻量网络，在线更新）

### 概率预测：GMM 输出层通用改造
- TS466（中）[Unveiling Stochasticity: Universal Multi-modal Probabilistic Modeling for Traffic Forecasting](../../pdfs/2026_Xiong_UnveilingStochasticity_en.pdf) — 预测；目标：交通状态（多交通数据集 + 一个密集城市路网）；方法：深度学习（任意模型 + 高斯混合输出层，NLL 训练）

### 概率预测：谱域扩散
- TS467（中）[SpecSTG: A Fast Spectral Diffusion Framework for Probabilistic Spatio-Temporal Traffic Forecasting](../../pdfs/2024_Lin_SpecSTG_en.pdf) — 预测；目标：交通流量/速度；方法：深度学习（谱域扩散 + 快速谱图卷积）

### 不确定性：测试时残差协方差更新
- TS468（中）[Teger: Spatiotemporal Covariance for Probabilistic Traffic Forecasting](../../pdfs/2026_Moghadas_Teger_en.pdf) — 预测；目标：交通状态（四个交通数据集，60 分钟跨度）；方法：统计（闭式高斯条件化 + EMA 波动率）+ 任意骨干（含冻结的 Chronos）

### 不确定性：多变量城市现象联合预测
- TS469（中）[UQGNN: Uncertainty Quantification of Graph Neural Networks for Multivariate Spatiotemporal Prediction](../../pdfs/2025_Yu_UQGNN_en.pdf) — 预测；目标：出租车、共享单车、犯罪、交通事故等多变量城市时空量；方法：深度学习（多变量扩散 GCN + 交互感知 TCN + 概率输出）

### 通用城市时空模型（网格）
- TS470（中）[UniST: A Prompt-Empowered Universal Model for Urban Spatio-Temporal Prediction](../../pdfs/2024_Yuan_UniST_en.pdf) — 预测；目标：城市时空变量（交通、人流等多场景）；方法：基础模型（多场景预训练 + 知识引导提示）

### 城市时空基础模型的规模化
- TS471（中）[UrbanFM: Scaling Urban Spatio-Temporal Foundation Models](../../pdfs/2026_Chen_UrbanFM_en.pdf) — 预测；目标：交通流量与速度等城市物理信号；方法：基础模型（MiniST 单元 + 极简自注意力架构）

### LLM 主干的交通预测（部分冻结注意力）
- TS472（中）[Spatial-Temporal Large Language Model for Traffic Prediction](../../pdfs/2024_Liu_SpatialTemporalLargeLanguage_en.pdf) — 预测；目标：交通流量/需求（具体数据集待全文核实）；方法：基础模型（ST-LLM：部分冻结注意力的 LLM）

### LLM 辅助测试时适应
- TS473（中）[Embracing Large Language Models in Traffic Flow Forecasting](../../pdfs/2024_Zhao_EmbracingLargeLanguageModels_en.pdf) — 预测；目标：交通流量；方法：混合（图/超图双分支 + LLM 选择 + 排序损失）

### LLM 可解释交通预测
- TS474（中）[Towards explainable traffic flow prediction with large language models](../../pdfs/2024_Guo_TowardsExplainableTrafficFlow_en.pdf) — 预测；目标：交通流量；方法：基础模型（指令微调 LLM：xTP-LLM）

### 零样本：图感知先验拟合网络
- TS475（中）[GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting](../../pdfs/2026_Natter_GASPFN_en.pdf) — 预测；目标：交通状态（六个基准，90 分钟跨度）；方法：基础模型（PFN，合成先验预训练，图感知）

### 无传感器区域的预测（物理约束 + 外部信号）
- TS476（中）[Generalising Traffic Forecasting to Regions without Traffic Observations](../../pdfs/2025_Su_GeneralisingTrafficForecastingRegions_en.pdf) — 预测；目标：交通状态（流量/速度，待全文核实）；方法：物理-数据融合（PINN 正则 + 外部信号学习 + 空间分组）

### 张量分解在线预测（缺失与异常）
- TS478（中）[A Multi-View Coupled Tensor Decomposition for Lightweight Online Adaptive Traffic Prediction](../../pdfs/2026_Yu_MultiViewCoupledTensor_en.pdf) — 预测；目标：交通速度、流量、占有率（多视图）；方法：统计（耦合张量分解 + 组稀疏正则，闭式更新）

### 物理引导的城市流预测
- TS479（中）[Physics-guided Active Sample Reweighting for Urban Flow Prediction](../../pdfs/2024_Jiang_PhysicsGuidedActiveSample_en.pdf) — 预测；目标：公交、出租车、网约车等交通服务的城市流量；方法：物理-数据融合（离散化物理引导网络 + 主动样本重加权）

### 极端天气下的城市流（解耦 + 因果增强）
- TS480（中）[WED-Net: A Weather-Effect Disentanglement Network with Causal Augmentation for Urban Flow Prediction](../../pdfs/2026_Hong_WEDNet_en.pdf) — 预测；目标：出租车流量（城市流）；方法：深度学习（双分支 Transformer 解耦 + 记忆库 + 天气判别器 + 因果数据增强）

### 事件影响：事故与交通管制
- TS481（中）[Towards Resilient Transportation: A Conditional Transformer for Accident-Informed Traffic Forecasting](../../pdfs/2025_Wang_TowardsResilientTransportation_en.pdf) — 预测；目标：交通流量/速度（待全文核实）；方法：深度学习（ConFormer：图传播 + 引导归一化层）

### 事件感知 + 共形区间（长跨度）
- TS482（中）[Long-Horizon Traffic Forecasting via Incident-Aware Conformal Spatio-Temporal Transformers](../../pdfs/2026_Patil_LongHorizonTrafficForecasting_en.pdf) — 预测；目标：多跨度交通计数（并验证旅行时间）；方法：混合（时空 Transformer + 自适应共形预测 + 分段变异系数动态图）

### 行人流量：基础模型与基线对比
- TS483（中）[How Good Are Time-Series Foundation Models for Pedestrian Crowd Count Forecasting? A Cross-Dataset Comparative Study](../../pdfs/2026_Hari_HowGoodTimeSeries_en.pdf) — 预测；目标：行人计数；方法：基准（季节朴素、LightGBM/CatBoost、N-HiTS/PatchTST、TimesFM/Chronos-2）

### 公交/BRT 站点客流
- TS484（中）[DST-TransitNet: A Dynamic Spatio-Temporal Deep Learning Model for Scalable and Efficient Network-Wide Prediction of Station-Level Transit Ridership](../../pdfs/2024_Wang_DSTTransitNet_en.pdf) — 预测；目标：站点级公交客流；方法：混合（GNN + RNN + 时间序列分解）

### 地铁 OD 预测
- TS485（中）[ODMixer: Fine-grained Spatial-temporal MLP for Metro Origin-Destination Prediction](../../pdfs/2024_Liu_ODMixer_en.pdf) — 预测；目标：地铁跨站 OD 客流；方法：深度学习（双分支 MLP：通道混合 + 多视角混合 + 双向趋势学习）

### 网约车需求：地理表示 + LLM
- TS486（中）[Enhancing Ride-Hailing Forecasting at DiDi with Multi-View Geospatial Representation Learning from the Web](../../pdfs/2026_Hao_EnhancingRideHailingForecasting_en.pdf) — 预测；目标：网约车需求（具体变量待全文核实）；方法：混合（POI 与移动模式多视图预训练 + 提示微调 LLM）

### 共享单车：扩张冷启动与公平性
- TS487（中）[Toward Equitable Low-Carbon Mobility: Fairness-Aware Demand Prediction for Expanding Bike-Sharing Systems](../../pdfs/2026_Luo_TowardEquitableLowCarbon_en.pdf) — 预测；目标：共享单车站点需求（含新建站点）；方法：深度学习（FairGIN：扩张模拟训练 + 注意力知识迁移 + 公平正则）

### 航空：机场到达延误
- TS488（中）[Airport Delay Prediction with Temporal Fusion Transformers](../../pdfs/2024_Liu_AirportDelayPredictionTemporal_en.pdf) — 预测；目标：机场到达延误（数值，15 分钟级）；方法：深度学习（Temporal Fusion Transformer）

### 铁路：车站级平均延误
- TS489（中）[RSTGCN: Railway-Centric Spatio-Temporal Graph Convolutional Network for Train Delay Prediction](../../pdfs/2025_Chowdhury_RSTGCN_en.pdf) — 预测；目标：车站某时段所有到达列车的平均到达延误；方法：深度学习（铁路中心 STGCN + 列车频次感知空间注意力）

### 旅行时间估计（工业部署）
- TS490（中）[MixTTE: Multi-Level Mixture-of-Experts for Scalable and Adaptive Travel Time Estimation](../../pdfs/2026_Jiang_MixTTE_en.pdf) — 预测；目标：网约车行程旅行时间；方法：深度学习（时空外部注意力 + 图 MoE + 异步增量学习）

### 拥堵预测（工业部署）
- TS491（中）[Interpretable Cascading Mixture-of-Experts for Urban Traffic Congestion Prediction](../../pdfs/2024_Jiang_InterpretableCascadingMixtureExperts_en.pdf) — 预测；目标：城市路段拥堵等级（序数回归）；方法：深度学习（CP-MoE：稀疏门控自适应图学习器混合 + 趋势/周期专家）

### 港口：集装箱吞吐量
- TS492（低）[Application of Large Language Models for Container Throughput Forecasting: Incorporating Contextual Information in Port Logistics](../../pdfs/2026_Kim_ApplicationLargeLanguageModels_en.pdf) — 预测；目标：港口集装箱吞吐量；方法：基础模型（LLM + 港口上下文提示结构）

### 基准数据集：传感器网络演化与持续学习
- TS493（中）[From XXLTraffic to EvoXXLTraffic: Scaling Traffic Forecasting to Sensor-Evolving Networks](../../pdfs/2026_Yin_XXLTrafficEvoXXLTrafficScalingTraffic_en.pdf) — 基准/数据集；目标：道路交通流量；方法：基准（静态 STGNN、在线方案、演化图持续学习、检索/测试时方法）

### 经典 STGNN 基线与基准来源
- TS494【三年前】（中）[Diffusion Convolutional Recurrent Neural Network: Data-Driven Traffic Forecasting](../../pdfs/2017_Li_DiffusionConvolutionalRecurrentNeural_en.pdf) — 预测；目标：道路交通速度；方法：深度学习（扩散卷积 + 编码器-解码器 RNN）

### 基准数据集：大规模路网
- TS495【三年前】（中）[LargeST: A Benchmark Dataset for Large-Scale Traffic Forecasting](../../pdfs/2023_Liu_LargeST_en.pdf) — 基准/数据集；目标：道路交通流量；方法：其他（数据集与基线评测）

### 交通数据驱动的超局地预报
- TS103（低）[Tackling air quality with SAPIENS](../../pdfs/2026_Bona_TacklingAirQualitySAPIENS_en.pdf) — 预测；目标：墨西哥城站点污染物水平；方法：统计（偏最小二乘回归，交通环形描述特征）

### 铁路轨道几何退化预测
- TS229（中）[Sensor fusion for track geometry monitoring: integrating on-board condition monitoring and degradation models via Kalman filtering](../../pdfs/2025_TruongBa_SensorFusionTrackGeometry_en.pdf) — 预测；目标：轨道几何指标退化；方法：统计（卡尔曼滤波融合退化模型与车载振动信号）

### EV 充电需求时空贝叶斯模型 + 新数据集
- TS597（高）[Spatio-temporal modelling of electric vehicle charging demand](../../pdfs/2026_Bouaachra_SpatioTemporalModellingElectric_en.pdf) — 预测；目标：苏格兰充电站级 EV 充电需求；方法：统计（时空潜高斯场 + INLA 近似贝叶斯推断）对比机器学习基线

### 电动汽车充电负荷概率预测（扩散模型）
- TS624（中）[DiffPLF: A Conditional Diffusion Model for Probabilistic Forecasting of EV Charging Load](../../pdfs/2024_Li_DiffPLF_en.pdf) — 预测；目标：电动汽车充电站充电负荷的概率分布；方法：深度学习（条件去噪扩散模型 + 交叉注意力条件机制 + 任务感知微调）

