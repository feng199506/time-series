# 空气质量：阅读路线图

进度：已核验全文 51 / 目标约 50；待核验 2；下载失败 13。 近三年（已核验文献中）50 篇，占 0.98。
编号对应 [catalog_cn.csv](catalog_cn.csv)；简介与字段均依据摘要，未读全文。

## 优先阅读 10 篇

| 顺序 | 编号 | 标题 | 理由 |
|---|---|---|---|
| 1 | TS059 | [A foundation model for the Earth system](../../pdfs/2024_Bodnar_FoundationModelEarthSystem_en.pdf) | 地球系统基础模型在空气质量预报上超过业务系统，代表范式转变。 |
| 2 | TS060 | [AIFS-COMPO: A Global Data-Driven Atmospheric Composition Forecasting System](../../pdfs/2026_Harder_AIFSCOMPO_en.pdf) | ECMWF 业务路线的数据驱动成分预报，与 CAMS IFS-COMPO 直接对比。 |
| 3 | TS062 | [Diffusion-based Probabilistic Air Quality Forecasting with Mechanistic Insight](../../pdfs/2026_Ding_DiffusionProbabilisticAirQuality_en.pdf) | 扩散模型做 30 成员臭氧集合预报，并量化天气不确定性。 |
| 4 | TS063 | [Global probabilistic forecasting of air pollution](../../pdfs/2026_Kheder_GlobalProbabilisticForecastingAir_en.pdf) | 全球公里级概率 PM2.5 预报，校准集合与提前 4 天极端探测。 |
| 5 | TS067 | [AirPhyNet: Harnessing Physics-Guided Neural Networks for Air Quality Prediction](../../pdfs/2024_Hettige_AirPhyNet_en.pdf) | 物理引导站点网络模型的常用基线（ICLR）。 |
| 6 | TS074 | [E-STGCN: extreme spatio-temporal graph convolutional networks for air quality forecasting](../../pdfs/2024_Panja_ESTGCN_en.pdf) | 极值理论 + 图网络 + 共形区间，统计期刊发表。 |
| 7 | TS086 | [AirQualityBench: A Realistic Evaluation Benchmark for Global Air Quality Forecasting](../../pdfs/2026_Xu_AirQualityBench_en.pdf) | 保留原生缺测的全球评测，揭示“干净数据集”上的优势不可迁移。 |
| 8 | TS104 | [Applications of Machine Learning and Artificial Intelligence in Tropospheric Ozone Research](../../pdfs/2025_Hickman_ApplicationsMachineLearningArtificial_en.pdf) | TOAR 视角下臭氧 ML 全景与挑战。 |
| 9 | TS061 | [Advancing global aerosol forecasting with artificial intelligence](../../pdfs/2024_Gui_AdvancingGlobalAerosolForecasting_en.pdf) | （补位：原推荐条目未核验通过或不足 10 篇）全球中期气溶胶 AI 预报代表作，覆盖沙尘/野火等污染事件预警场景。 |
| 10 | TS064 | [Advancing operational PM2.5 forecasting with dual deep neural networks (D-DNet)](../../pdfs/2024_Cai_AdvancingOperationalPM25_en.pdf) | （补位：原推荐条目未核验通过或不足 10 篇）把“学习式同化”纳入 AI 空气质量业务预报，方法上区别于纯预测网络。 |

## 按子方向

### 全球大气成分/空气质量预报（基础模型）
- TS059（高）[A foundation model for the Earth system](../../pdfs/2024_Bodnar_FoundationModelEarthSystem_en.pdf) — 预测；目标：空气质量（全球大气成分场，具体污染物待全文核实）；方法：基础模型（Aurora，大规模预训练+微调）

### 全球大气成分/空气质量预报（业务数据驱动系统）
- TS060（高）[AIFS-COMPO: A Global Data-Driven Atmospheric Composition Forecasting System](../../pdfs/2026_Harder_AIFSCOMPO_en.pdf) — 预测；目标：气溶胶与反应性气体（多种大气成分）；方法：深度学习（Transformer 编码-处理-解码，AIFS 架构）

### 全球气溶胶/沙尘预报
- TS061（高）[Advancing global aerosol forecasting with artificial intelligence](../../pdfs/2024_Gui_AdvancingGlobalAerosolForecasting_en.pdf) — 预测；目标：气溶胶光学组分与地面浓度（AOD、沙尘组分等）；方法：深度学习（Vision Transformer + U-Net）

### 概率/集合预报（臭氧）
- TS062（高）[Diffusion-based Probabilistic Air Quality Forecasting with Mechanistic Insight](../../pdfs/2026_Ding_DiffusionProbabilisticAirQuality_en.pdf) — 预测；目标：地面臭氧（O3）浓度；方法：物理-数据融合（扩散生成模型 AirFusion）

### 概率/集合预报（全球公里级 PM2.5）
- TS063（高）[Global probabilistic forecasting of air pollution](../../pdfs/2026_Kheder_GlobalProbabilisticForecastingAir_en.pdf) — 预测；目标：PM2.5 浓度及局地极端值；方法：深度学习（生成式模型 Foehn）

### 全球业务预报+数据同化
- TS064（高）[Advancing operational PM2.5 forecasting with dual deep neural networks (D-DNet)](../../pdfs/2024_Cai_AdvancingOperationalPM25_en.pdf) — 预测；目标：PM2.5 与 AOD550；方法：深度学习（预测网络+同化网络双网络）

### 城市多站点业务预报（多模态）
- TS065（高）[FuXi-Air: air quality forecasting based on emission-meteorology-pollutant multimodal machine learning](../../pdfs/2025_Geng_FuXiAir_en.pdf) — 预测；目标：六种主要污染物逐小时浓度；方法：深度学习（多模态融合+自回归+帧插值）

### 高分辨率格点预报（物理引导）
- TS066（高）[TopoFlow: Topography-aware Pollutant Flow Learning for High-Resolution Air Quality Prediction](../../pdfs/2026_Kheder_TopoFlow_en.pdf) — 预测；目标：PM2.5 及四种主要污染物；方法：物理-数据融合（ViT + 地形感知注意力 + 风向引导 patch 重排）

### 站点网络时空预测（物理引导 GNN）
- TS067（高）[AirPhyNet: Harnessing Physics-Guided Neural Networks for Air Quality Prediction](../../pdfs/2024_Hettige_AirPhyNet_en.pdf) — 预测；目标：空气质量（站点污染物浓度）；方法：物理-数据融合（扩散+对流微分方程网络+图结构）

### 站点网络时空预测（物理引导 Neural ODE）
- TS068（中）[Air Quality Prediction with Physics-Guided Dual Neural ODEs in Open Systems](../../pdfs/2024_Tian_AirQualityPredictionPhysics_en.pdf) — 预测；目标：污染物浓度；方法：物理-数据融合（双分支 Neural ODE）

### CTM 替代模型（站点级）
- TS069（中）[PCDCNet: A Surrogate Model for Air Quality Forecasting with Physical-Chemical Dynamics and Constraints](../../pdfs/2025_Wang_PCDCNet_en.pdf) — 预测；目标：站点 PM2.5 与 O3；方法：物理-数据融合（图输送+循环累积+约束）

### 站点网络时空预测（输送算子 GNN）
- TS070（中）[TransNet: a transport-informed graph neural network for forecasting PM2.5 concentrations across South Korea](../../pdfs/2026_Dimri_TransNet_en.pdf) — 预测；目标：PM2.5 浓度；方法：物理-数据融合（学习耦合平流-扩散-反应算子的 GNN）

### 业务 CTM 后处理（日本）
- TS072（中）[Machine learning post-processing for air quality prediction in Japan](../../pdfs/2026_Yumimoto_MachineLearningPostProcessing_en.pdf) — 预测；目标：臭氧与 PM2.5 预报订正；方法：深度学习（DNN 后处理）

### 臭氧站点预报与跨区域迁移
- TS073（中）[Transferable Hourly Ozone Forecasting with Transformers](../../pdfs/2026_Vasireddy_TransferableHourlyOzoneForecasting_en.pdf) — 预测；目标：地面臭氧逐小时浓度；方法：深度学习（Temporal Fusion Transformer）

### 极端污染/区间预测（EVT+GNN）
- TS074（高）[E-STGCN: extreme spatio-temporal graph convolutional networks for air quality forecasting](../../pdfs/2024_Panja_ESTGCN_en.pdf) — 预测；目标：多种污染物浓度（含极端值）；方法：混合（极值理论 GPD + 图卷积 + LSTM + 共形预测）

### 极端颗粒物事件预报
- TS075（中）[Synergistic neural forecasting of air pollution with stochastic sampling](../../pdfs/2025_Abeysinghe_SynergisticNeuralForecastingAir_en.pdf) — 预测；目标：PM1、PM2.5、PM10；方法：深度学习（区域化 Transformer + 扩散随机细化 + 极值导向损失）

### 多任务气象-污染联合预报
- TS076（中）[AirCast: Improving Air Pollution Forecasting Through Multi-Variable Data Alignment](../../pdfs/2025_Nedungadi_AirCast_en.pdf) — 预测；目标：污染物浓度（并联合预测气象变量）；方法：深度学习（多任务头 + 频率加权 MAE 损失）

### 超标事件统计建模（数据融合）
- TS077（中）[Spatiotemporal fusion of reanalysis and in situ data for censored threshold exceedances of PM2.5](../../pdfs/2025_Cuba_SpatiotemporalFusionReanalysisSitu_en.pdf) — 预测；目标：PM2.5 删失阈值超标（超标与否及超标量）；方法：统计（贝叶斯层次模型，Dirac-delta 广义帕累托分布）

### 预报评估（决策导向，野火）
- TS079（中）[Are Hourly PM2.5 Forecasts Sufficiently Accurate to Plan Your Day? Individual Decision-Making in the Face of Increasing Wildfire Smoke](../../pdfs/2024_Berlinghieri_HourlyPM25Forecasts_en.pdf) — 预测；目标：逐小时地面 PM2.5 预报的决策价值；方法：其他（预报检验，涵盖物理、集合与 AI 预报）

### 野火/计划烧除影响情景预报
- TS080（低）[Simulating the air quality impact of prescribed fires using graph neural network-based PM 2.5 forecasts](../../pdfs/2023_Liao_SimulatingAirQualityImpact_en.pdf) — 预测；目标：加州逐小时 PM2.5（净值与背景值，推算火源贡献）；方法：深度学习（时空 GNN）

### 沙尘暴预报
- TS081（中）[An artificial intelligence model for sand and dust storm forecast driven by AI weather forecasts](../../pdfs/2026_Wang_ArtificialIntelligenceModelSand_en.pdf) — 预测；目标：沙尘浓度/沙尘暴事件；方法：物理-数据融合（多重堆叠图注意力网络 + 物理约束 + 物理排放方案）

### 站点-格点融合预报（沙尘期 PM10）
- TS082（中）[OmniPMNet: Bridging discrete and gridded PM10 forecasts via omni-query neural processes](../../pdfs/2026_He_OmniPMNet_en.pdf) — 预测；目标：PM10（站点与格点）；方法：深度学习（卷积条件神经过程 ConvCNP + 空间源注意力）

### 次季节（10-30 天）预测
- TS083（中）[A skillful hybrid framework for seamless subseasonal PM2.5 prediction over North China](../../pdfs/2026_Li_SkillfulHybridFrameworkSeamless_en.pdf) — 预测；目标：华北 PM2.5 的 30 天演变；方法：混合（动力-统计，ICEOTW）

### 基准/数据集（时序基础模型）
- TS085（高）[Air Quality Arena: A Large-Scale Multi-Region Ground Monitoring Dataset and Benchmark for Air Quality Forecasting with Time-Series Foundation Models](../../pdfs/2026_Bharadwaj_AirQualityArena_en.pdf) — 基准/数据集；目标：6 种主要污染物短期浓度；方法：基础模型（评测 11 个时序基础模型与经典基线）

### 基准/数据集（真实缺测条件）
- TS086（高）[AirQualityBench: A Realistic Evaluation Benchmark for Global Air Quality Forecasting](../../pdfs/2026_Xu_AirQualityBench_en.pdf) — 基准/数据集；目标：6 种主要污染物逐小时浓度；方法：其他（评测代表性时空模型）

### 大语言模型骨干的少样本/零样本预测
- TS088（中）[Meteorology-Driven GPT4AP: A Multi-Task Forecasting LLM for Atmospheric Air Pollution in Data-Scarce Settings](../../pdfs/2026_Dey_MeteorologyDrivenGPT4AP_en.pdf) — 预测；目标：空气污染物浓度；方法：基础模型（GPT-2 骨干 + rsLoRA 参数高效微调）

### NO2 站点网络预测（未来协变量）
- TS089（中）[Back to the Future: GNN-based NO$_2$ Forecasting via Future Covariates](../../pdfs/2024_Giganti_BackFutureGNNNO_en.pdf) — 预测；目标：NO2 浓度；方法：深度学习（时空 GNN + 协变量条件化模块）

### 站点网络时空预测（多层气象）
- TS090（中）[Air Quality Prediction With a Meteorology-Guided Modality-Decoupled Spatiotemporal Network](../../pdfs/2025_Yin_AirQualityPredictionMeteorology_en.pdf) — 预测；目标：空气质量（站点污染物浓度）；方法：深度学习（编码-解码，模态解耦，天气预报作动态提示）

### 可解释时空预测（欧洲城市）
- TS091（中）[Interpretable Air Pollution Forecasting by Physics-Guided Spatiotemporal Decoupling](../../pdfs/2025_Zhang_InterpretableAirPollutionForecasting_en.pdf) — 预测；目标：空气污染物浓度；方法：物理-数据融合（物理引导输送核 + 可解释注意力，加性分解）

### CTM 输送过程仿真器（NOAA）
- TS092（低）[Difference Learning for Air Quality Forecasting Transport Emulation](../../pdfs/2024_Chen_DifferenceLearningAirQuality_en.pdf) — 预测；目标：化学物种输送（服务于美国本土空气质量预报）；方法：深度学习（差分学习输送仿真器）

### 非洲传感器网络临近/短期预报
- TS095（低）[Gaussian Processes for Monitoring Air-Quality in Kampala](../../pdfs/2023_Stoddart_GaussianProcessesMonitoringAir_en.pdf) — 预测；目标：空气污染（PM 浓度，待全文核实）；方法：统计（高斯过程 + 稀疏近似）

### 移动低成本传感器细粒度预报
- TS096（中）[STeP-Diff: Spatio-Temporal Physics-Informed Diffusion Models for Mobile Fine-Grained Pollution Forecasting](../../pdfs/2025_Zhou_STePDiff_en.pdf) — 预测；目标：细粒度空气污染时空场；方法：物理-数据融合（DeepONet + PDE 约束扩散模型）

### 低成本传感器序列预测（小波+树模型）
- TS097（低）[A Novel Hybrid Approach For Efficiently Forecasting Air Quality Data](../../pdfs/2024_Borah_NovelHybridApproachEfficiently_en.pdf) — 预测；目标：空气污染物实时浓度；方法：混合（MODWT 小波分解 + CatBoost）

### 室内 PM2.5 预测（传感器）
- TS098（低）[Indoor PM2.5 forecasting and the association with outdoor air pollution: a modelling study based on sensor data in Australia](../../pdfs/2024_Yu_IndoorPM25Forecasting_en.pdf) — 预测；目标：室内逐小时 PM2.5；方法：机器学习（三阶段深度集成 DEML：SVM/RF/XGBoost + 元模型）

### CO 场预测（神经算子）
- TS100（低）[CoNOAir: A Neural Operator for Forecasting Carbon Monoxide Evolution in Cities](../../pdfs/2025_Bedi_CoNOAir_en.pdf) — 预测；目标：一氧化碳（CO）浓度；方法：深度学习（复数神经算子 CoNOAir）

### 沙尘能见度等级预报（NWP 后处理）
- TS101（低）[A physics-guided machine learning framework for enhancing dust storm visibility prediction in arid and semi-arid regions](../../pdfs/2026_Xu_PhysicsGuidedMachineLearning_en.pdf) — 预测；目标：五级有序能见度等级（沙尘影响）；方法：物理-数据融合（沙尘生命周期特征库 + 有序 LightGBM）

### 非洲多城市多污染物与跨城迁移
- TS102（低）[Explainable PSO-optimised machine learning models for multi-pollutant air quality forecasting in major African cities with transfer learning](../../pdfs/2026_Mazuruse_ExplainablePSOOptimisedMachine_en.pdf) — 预测；目标：PM2.5、PM10、NO2、SO2、CO、O3；方法：机器学习（PSO 优化 XGBoost/RF + 迁移学习/域适应）

### 交通数据驱动的超局地预报
- TS103（低）[Tackling air quality with SAPIENS](../../pdfs/2026_Bona_TacklingAirQualitySAPIENS_en.pdf) — 预测；目标：墨西哥城站点污染物水平；方法：统计（偏最小二乘回归，交通环形描述特征）

### 综述（对流层臭氧 ML）
- TS104（高）[Applications of Machine Learning and Artificial Intelligence in Tropospheric Ozone Research](../../pdfs/2025_Hickman_ApplicationsMachineLearningArtificial_en.pdf) — 综述；目标：对流层臭氧（短期预报、化学仿真、遥感估计）；方法：其他（综述）

### 综述/展望（深度学习污染预报）
- TS106（中）[Deep learning for air pollutant forecasting: opportunities, challenges, and future directions](../../pdfs/2025_Tao_DeepLearningAirPollutant_en.pdf) — 综述；目标：空气污染物预报；方法：其他（观点/综述）

### 综述（室内空气质量预测）
- TS107（低）[Indoor Air Quality Forecasting With Machine Learning: A Systematic Review](../../pdfs/2026_Rudford_IndoorAirQualityForecasting_en.pdf) — 综述；目标：室内空气质量；方法：其他（系统综述）

### 站点网络时空预测（经典基线）
- TS108【三年前】（低）[PM2.5-GNN](../../pdfs/2020_Wang_PM25GNN_en.pdf) — 预测；目标：PM2.5 浓度；方法：深度学习（融合领域知识的图神经网络）

### 多污染物自回归长时效预报
- TS109（低）[MVAR: MultiVariate AutoRegressive Air Pollutants Forecasting Model](../../pdfs/2025_Fan_MVAR_en.pdf) — 预测；目标：6 种主要污染物；方法：深度学习（多变量自回归 + 气象耦合空间 Transformer）

### 多区域多污染物时空预测（因果感知）
- TS110（低）[A Causality-Aware Spatiotemporal Model for Multi-Region and Multi-Pollutant Air Quality Forecasting](../../pdfs/2025_Lu_CausalityAwareSpatiotemporalModel_en.pdf) — 预测；目标：多污染物浓度（含突发污染过程与长期趋势）；方法：深度学习（AirPCM，气象-污染动态因果建模）

### 季节预测（中国 PM2.5 主模态）
- TS111（低）[Lagged sea-surface-temperature precursors of the leading PM2.5 mode in China](../../pdfs/2026_Chen_LaggedSeaSurfaceTemperature_en.pdf) — 预测；目标：中国 PM2.5 主导变率模态（夏季与冬季）；方法：统计（模态分析 + 简单回归）

### 深度学习区域 CTM
- TS112（低）[Zeeman: A Deep Learning Regional Atmospheric Chemistry Transport Model](../../pdfs/2025_Pang_Zeeman_en.pdf) — 预测；目标：多组分大气化学（含 PM2.5、臭氧等）；方法：深度学习（注意力机制的 DL 化学传输模型）

### 减排情景 CTM 仿真
- TS113（低）[A deep-learning model for predicting daily PM2.5 concentration in response to emission reduction](../../pdfs/2025_Liu_DeepLearningModelPredicting_en.pdf) — 预测；目标：逐日 PM2.5 及其化学组分对前体物减排的响应；方法：深度学习（残差对称 3D U-Net，CleanAir）

### 气候模式臭氧偏差订正（未来情景）
- TS114（低）[Applying deep learning to a chemistry-climate model for improved ozone prediction](../../pdfs/2025_Liu_ApplyingDeepLearningChemistry_en.pdf) — 预测；目标：地面臭氧（UKESM1 偏差订正）；方法：深度学习（六种统计/DL 模型，Transformer 最好，加权集成）

### 臭氧站点网络预测（含区间）
- TS115（低）[A Novel Wind-Aware Dynamic Graph Neural Network for Urban Ground-Level Ozone Concentration Prediction](../../pdfs/2026_Wu_NovelWindAwareDynamic_en.pdf) — 预测；目标：逐小时地面臭氧多步预测及连续空间场；方法：深度学习（风感知动态图注意力 + Transformer 时间编码 + 协同克里金）

### 沙尘预报数据同化
- TS123（低）[Valid time shifting ensemble Kalman filter (VTS-EnKF) for dust storm forecasting](../../pdfs/2024_Pang_ValidTimeShiftingEnsemble_en.pdf) — 预测；目标：沙尘浓度/沙尘载量；方法：统计（集合卡尔曼滤波变体：邻近时刻集合扩充）

### 持续学习：传感器网络扩张
- TS464（中）[Expand and Compress: Exploring Tuning Principles for Continual Spatio-Temporal Graph Forecasting](../../pdfs/2024_Chen_ExpandAndCompress_en.pdf) — 预测；目标：交通流量（并含空气质量、风能等）；方法：深度学习（STGNN + 连续提示池，提示微调）

