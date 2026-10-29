# 能源与电力：阅读路线图

进度：已核验全文 56 / 目标约 50；待核验 2；下载失败 1。 近三年（已核验文献中）53 篇，占 0.946。
编号对应 [catalog_cn.csv](catalog_cn.csv)；简介与字段均依据摘要，未读全文。

## 优先阅读 10 篇

| 顺序 | 编号 | 标题 | 理由 |
|---|---|---|---|
| 1 | TS578 | [The hybrid renewable energy forecasting and trading competition 2024](../../pdfs/2025_Browell_HybridRenewableEnergyForecasting_en.pdf) | The Hybrid Renewable Energy Forecasting and Trading Competition 2024。IJF 正式竞赛报告，真实前向评测，同时讨论预测技巧与交易价值。 |
| 2 | TS579 | [Energy Forecasting: A Review and Outlook](../../pdfs/2020_Hong_EnergyForecasting_en.pdf) | Energy Forecasting: A Review and Outlook（2020）。领域权威综述，给出可复现研究规范与开放数据源。 |
| 3 | TS580 | [Combining Weather Forecast Aggregation and State-Space Models for Adaptive Probabilistic Electricity Load Forecasting](../../pdfs/2026_Vilmarest_CombiningWeatherForecastAggregation_en.pdf) | Combining Weather Forecast Aggregation and State-Space Models…。GAM + 状态空间在线自适应，并聚合多家气象预报，统计路线的代表。 |
| 4 | TS581 | [Efficient mid-term forecasting of hourly electricity load using generalized additive models](../../pdfs/2024_Zimmermann_EfficientMidTermForecasting_en.pdf) | Efficient mid-term forecasting of hourly electricity load using GAMs。中期小时负荷，气温、节假日、经济变量处理细致，可解释。 |
| 5 | TS583 | [The role of probabilistic load and renewable prediction in enhancing day-ahead electricity price forecasts](../../pdfs/2025_Uniejewski_RoleProbabilisticLoadRenewable_en.pdf) | The role of probabilistic load and renewable prediction in enhancing day-ahead electricity price forecasts。把负荷与风光预测的不确定性传递到电价预测。 |
| 6 | TS585 | [Day-Ahead Electricity Price Forecasting Using Merit-Order Curves Time Series](../../pdfs/2025_Koechlin_DayAheadElectricityPrice_en.pdf) | Day-Ahead Electricity Price Forecasting Using Merit-Order Curves Time Series。从供需曲线（市场机制）出发的结构化电价预测。 |
| 7 | TS586 | [Seamless short- to mid-term probabilistic wind power forecasting](../../pdfs/2025_Dantas_SeamlessShortMidTerm_en.pdf) | Seamless short- to mid-term probabilistic wind power forecasting。拆分天气不确定性与功率转换不确定性，6-162 小时一个模型覆盖。 |
| 8 | TS588 | [Intraday spatiotemporal PV power prediction at national scale using satellite-based solar forecast models](../../pdfs/2026_Lanzilao_IntradaySpatiotemporalPVPower_en.pdf) | Intraday spatiotemporal PV power prediction at national scale…。全国 6434 个站点的卫星光伏时空预测评估。 |
| 9 | TS591 | [FETS Benchmark: Foundation Models Enable Scalable and Generalizable Energy Time Series Forecasting](../../pdfs/2026_Obermeier_FETSBenchmark_en.pdf) | FETS Benchmark。覆盖 54 个能源数据集的基础模型与专用模型对比。 |
| 10 | TS595 | [Foundation models for electricity price forecasting and battery arbitrage: Can they replace market-specific forecasting models?](../../pdfs/2026_Lipiecki_FoundationModelsElectricityPrice_en.pdf) | Foundation models for electricity price forecasting and battery arbitrage。同时给出统计与经济评价，结论审慎（基础模型不能普遍取代专用模型）。 |

## 按子方向

### 风光混合发电预测与交易竞赛
- TS578（高）[The hybrid renewable energy forecasting and trading competition 2024](../../pdfs/2025_Browell_HybridRenewableEnergyForecasting_en.pdf) — 基准/数据集；目标：英国 3.6 GW 风电与光伏组合日前发电（分位数）及交易；方法：多方法竞赛分析（梯度提升树等）

### 综述：能源预测全景（经典基础）
- TS579【三年前】（高）[Energy Forecasting: A Review and Outlook](../../pdfs/2020_Hong_EnergyForecasting_en.pdf) — 综述；目标：电力需求、电价、风光发电；方法：（综述）

### 系统级短期负荷概率预测
- TS580（高）[Combining Weather Forecast Aggregation and State-Space Models for Adaptive Probabilistic Electricity Load Forecasting](../../pdfs/2026_Vilmarest_CombiningWeatherForecastAggregation_en.pdf) — 预测；目标：法国全国电力消费（负荷）的点预测与概率（分位数）预测；方法：统计（自适应 GAM + 状态空间/Viking 算法 + GAMLSS 概率层）

### 中期小时负荷预测（国家级）
- TS581（高）[Efficient mid-term forecasting of hourly electricity load using generalized additive models](../../pdfs/2024_Zimmermann_EfficientMidTermForecasting_en.pdf) — 预测；目标：国家级小时电力负荷（中期：数周至一年）；方法：统计（P 样条 GAM + 自回归后处理；社会经济状态用 ETS 建模）

### 美国电网小时需求多架构基准（含天气协变量）
- TS582（高）[Benchmarking State Space Models, Transformers, and Recurrent Networks for US Grid Forecasting](../../pdfs/2026_Hong_BenchmarkingStateSpaceModels_en.pdf) — 预测；目标：美国六个电网的小时电力需求（24-168 小时）；方法：深度学习（PowerMamba、S-Mamba、iTransformer、PatchTST、LSTM）

### 日前电价（概率基本面输入）
- TS583（高）[The role of probabilistic load and renewable prediction in enhancing day-ahead electricity price forecasts](../../pdfs/2025_Uniejewski_RoleProbabilisticLoadRenewable_en.pdf) — 预测；目标：德国 EPEX 日前电价；方法：统计（专家模型、LASSO 高维模型；输入用历史模拟、保形预测、分位数回归生成）

### 日前电价（供需曲线函数型预测）
- TS585（高）[Day-Ahead Electricity Price Forecasting Using Merit-Order Curves Time Series](../../pdfs/2025_Koechlin_DayAheadElectricityPrice_en.pdf) — 预测；目标：日前市场供给与需求 merit-order 曲线及由此得出的电价；方法：统计（函数型数据分析）

### 风电短期至中期无缝概率预测
- TS586（高）[Seamless short- to mid-term probabilistic wind power forecasting](../../pdfs/2025_Dantas_SeamlessShortMidTerm_en.pdf) — 预测；目标：风电场功率概率预测（6-162 小时）；方法：统计/机器学习（整合天气预报不确定性与天气-功率转换不确定性；具体模型待全文核实）

### 风电领域基础模型（零样本概率预测）
- TS587（高）[WindFM: An Open-Source Foundation Model for Zero-Shot Wind Power Forecasting](../../pdfs/2025_Fan_WindFM_en.pdf) — 预测；目标：风电功率概率预测（零样本）；方法：基础模型（离散化分词器 + 仅解码器 Transformer 自回归预训练，生成式）

### 全国尺度光伏日内时空预测（卫星）
- TS588（高）[Intraday spatiotemporal PV power prediction at national scale using satellite-based solar forecast models](../../pdfs/2026_Lanzilao_IntradaySpatiotemporalPVPower_en.pdf) — 预测；目标：瑞士 6434 个光伏电站日内功率（经辐照度场转换）；方法：深度学习/光流/物理 NWP 七类模型比较（确定性与概率）；站点级机器学习功率转换

### 日前辐照度概率预测（卫星 + 地面站）
- TS589（高）[SolarCrossFormer: Improving Day-Ahead Solar Irradiance Forecasting by Integrating Satellite Imagery and Ground Sensors](../../pdfs/2025_Schubnel_SolarCrossFormer_en.pdf) — 预测；目标：瑞士任意位置的地表太阳辐照度概率预测；方法：深度学习（图神经网络刻画模态内/模态间相关的 Transformer 类模型）

### 大范围辐照度预测（卫星驱动 AI 替代 NWP）
- TS590（高）[SolarSeer: Ultrafast and accurate 24-hour solar irradiance forecasts outperforming numerical weather prediction across the USA](../../pdfs/2025_Bai_SolarSeer_en.pdf) — 预测；目标：美国本土 24 小时云量与太阳辐照度（5 km）；方法：深度学习（端到端大型 AI 模型，卫星观测直接映射到未来预报）

### 能源时间序列基础模型基准
- TS591（高）[FETS Benchmark: Foundation Models Enable Scalable and Generalizable Energy Time Series Forecasting](../../pdfs/2026_Obermeier_FETSBenchmark_en.pdf) — 基准/数据集；目标：9 类能源数据（负荷、发电、价格等，具体待全文核实）；方法：基础模型对比任务专用机器学习

### 跨电网层级负荷预测基准
- TS592（高）[A Benchmark for Electrical Load Forecasting Across Grid Levels: Time-Series Transformers Outperform Established Methods](../../pdfs/2026_Hertel_BenchmarkElectricalLoadForecasting_en.pdf) — 基准/数据集；目标：输电控制区、低压馈线、个体终端用户三层级的短期负荷；方法：深度学习（Transformer、YAformer）等 10 种方法 + 时间序列基础模型

### 风电预测基准
- TS593（高）[WPBench: A Comprehensive Benchmark for Wind Power Forecasting](../../pdfs/2026_Zhu_WPBench_en.pdf) — 基准/数据集；目标：风电功率（单机/多机，单变量/多变量）；方法：19 个代表模型（统计、机器学习、深度学习等）

### 图像驱动的光伏临近预报全球基准
- TS594（高）[SolarBench: A global solar energy nowcasting benchmark](../../pdfs/2026_Nie_SolarBench_en.pdf) — 基准/数据集；目标：辐照度或光伏出力临近预报；方法：深度学习（代表性模型基准）+ 开源工具箱

### 基础模型电价预测评测 + 经济价值
- TS595（高）[Foundation models for electricity price forecasting and battery arbitrage: Can they replace market-specific forecasting models?](../../pdfs/2026_Lipiecki_FoundationModelsElectricityPrice_en.pdf) — 预测；目标：德国、波兰、西班牙日前电价的点与概率预测；方法：基础模型（5 个家族 9 个变体，零样本，含 TabPFN）对比 DDNN 等专用基准

### 基础模型 + 外生变量的电力需求预测评测
- TS596（高）[Assessing Electricity Demand Forecasting with Exogenous Data in Time Series Foundation Models](../../pdfs/2026_Cheong_AssessingElectricityDemandForecasting_en.pdf) — 预测；目标：新加坡与澳大利亚电力市场的电力需求；方法：基础模型（MOIRAI、MOMENT、TinyTimeMixers、ChronosX、Chronos-2）对比 LSTM+RevIN 基线

### EV 充电需求时空贝叶斯模型 + 新数据集
- TS597（高）[Spatio-temporal modelling of electric vehicle charging demand](../../pdfs/2026_Bouaachra_SpatioTemporalModellingElectric_en.pdf) — 预测；目标：苏格兰充电站级 EV 充电需求；方法：统计（时空潜高斯场 + INLA 近似贝叶斯推断）对比机器学习基线

### 天气基础模型微调用于电网资产级气象预报与覆冰预警
- TS598（高）[A Weather Foundation Model for the Power Grid](../../pdfs/2025_Bodnar_WeatherFoundationModelPower_en.pdf) — 预测；目标：电网资产级温度、降水、轮毂高度风速、风机覆冰风险、导线雾凇覆冰；方法：基础模型（微调 15 亿参数天气基础模型 GFT）

### 日前电价基准与最佳实践（经典基础）
- TS599【三年前】（高）[Forecasting day-ahead electricity prices: A review of state-of-the-art algorithms, best practices and an open-access benchmark](../../pdfs/2020_Lago_ForecastingDayAheadElectricity_en.pdf) — 基准/数据集；目标：多个市场的日前电价；方法：统计与深度学习（LEAR、DNN 等）对比

### 建筑负荷大规模数据集与基准（经典基础）
- TS600【三年前】（高）[BuildingsBench: A Large-Scale Dataset of 900K Buildings and Benchmark for Short-Term Load Forecasting](../../pdfs/2023_Emami_BuildingsBench_en.pdf) — 基准/数据集；目标：住宅与商业建筑短期负荷（零样本与迁移学习）；方法：深度学习（预训练 Transformer 等）

### 中期负荷预测 + 经济指标
- TS601（中）[Medium-Term Multi-Resolution Electric Load Forecasting using Economic Data and Foundation Model](../../pdfs/2026_Eloi_MediumTermMultiResolution_en.pdf) — 预测；目标：法国电力负荷（提前 1-48 个月）；方法：基础模型（表格基础模型）

### 长期（多年）小时负荷预测
- TS602（中）[A Stability-Driven Framework for Long-Term Hourly Electricity Demand Forecasting](../../pdfs/2025_Dhar_StabilityDrivenFrameworkLong_en.pdf) — 预测；目标：国家级年用电总量与小时负荷（5-6 年前瞻）；方法：统计（t 检验验证负荷形状稳定性 + GDP 回归 + 季节指数；短期用指数平滑）

### 区域负荷时空预测（图神经网络）
- TS603（中）[Graph Neural Networks for Electricity Load Forecasting](../../pdfs/2025_Campagne_GraphNeuralNetworksElectricity_en.pdf) — 预测；目标：区域/细粒度电力负荷；方法：深度学习（GCN、GraphSAGE、APPNP、GAT + 注意力 + 集成聚合）

### 极端天气下负荷概率预测（小样本）
- TS605（中）[Resilient Load Forecasting under Climate Change: Adaptive Conditional Neural Processes for Few-Shot Extreme Load Forecasting](../../pdfs/2026_Hu_ResilientLoadForecastingUnder_en.pdf) — 预测；目标：极端天气期间的电力负荷概率预测；方法：深度学习（自适应条件神经过程 AdaCNP，元学习/小样本）

### 低压馈线净负荷概率预测（基础模型）
- TS606（中）[Probabilistic Low-Voltage Peak Load Forecasting with Time Series Foundation Models Evaluated on Application-Oriented Metrics](../../pdfs/2026_Kaas_ProbabilisticLowVoltagePeak_en.pdf) — 预测；目标：200 条真实低压馈线的短期净负荷及峰值（概率）；方法：基础模型（Chronos-Bolt、Chronos-2、TabPFN-TS）对比 6 个基线

### 配电网多聚合层级短期负荷与峰值评估
- TS607（中）[Peak-Aware Short-Term Load Forecasting Across Distribution Grid Aggregation Levels](../../pdfs/2026_Chattopadhyay_PeakAwareShortTerm_en.pdf) — 预测；目标：配电网区号/二次变电站/低压馈线三层级负荷，重点为高需求时段；方法：统计基线、机器学习（LightGBM、XGBoost）、基础模型（Chronos-Bolt、Chronos-2）对比

### 户级小时采暖与用电需求概率预测
- TS608（中）[Forecasting residential heating and electricity demand with scalable, high-resolution, open-source models](../../pdfs/2025_Lee_ForecastingResidentialHeatingElectricity_en.pdf) — 预测；目标：住宅建筑级小时采暖需求与非采暖用电需求；方法：深度学习（概率深度学习，多模态建筑信息）

### 高比例可再生电网净负荷日前概率预测
- TS609（中）[Probabilistic Net Load Forecasting for High-Penetration RES Grids Utilizing Enhanced Conditional Diffusion Model](../../pdfs/2025_Huang_ProbabilisticNetLoadForecasting_en.pdf) — 预测；目标：日前净负荷概率分布；方法：深度学习（增强条件扩散模型 ECDM，插补式条件扩散 + 交叉注意力融合）

### 电价概率后处理（QRA/保形/IDR 比较与组合）
- TS610（中）[Postprocessing of point predictions for probabilistic forecasting of day-ahead electricity prices: The benefits of using isotonic distributional regression](../../pdfs/2024_Lipiecki_PostprocessingPointPredictionsProbabilis_en.pdf) — 预测；目标：德国与西班牙日前电价的预测分布；方法：统计（分位数回归平均、保形预测、等渗分布回归 IDR 及其组合）

### 日内电价贝叶斯概率预测
- TS611（中）[Bayesian hierarchical probabilistic forecasting of intraday electricity prices](../../pdfs/2024_Nickelsen_BayesianHierarchicalProbabilisticForecas_en.pdf) — 预测；目标：德国日内市场 IDFull 价格指数（后验预测分布）；方法：统计（贝叶斯分层模型；正交匹配追踪 OMP 选择协变量 + 正则化先验）

### 日内连续市场电价路径概率预测
- TS612（中）[Probabilistic intraday electricity price forecasting using generative machine learning](../../pdfs/2025_Chen_ProbabilisticIntradayElectricityPrice_en.pdf) — 预测；目标：德国连续日内市场电价的概率路径；方法：深度学习（生成式神经网络）

### 中长期电价（计量经济模型）
- TS613（中）[From day-ahead to mid and long-term horizons with econometric electricity price forecasting models](../../pdfs/2024_Ghelasi_DayAheadMidLong_en.pdf) — 预测；目标：电价（一天至一年前瞻）；方法：统计（计量经济模型：基本面约束系数、季节期望回归项、同日关系外推处理单位根）

### 日前电价时空预测（跨竞价区）
- TS614（中）[Networked Spatial Effects in European Electricity Price Forecasting](../../pdfs/2026_Chomon_NetworkedSpatialEffectsEuropean_en.pdf) — 预测；目标：欧洲 39 个竞价区的日前电价；方法：统计（网络化时空模型 NSTM，度量图邻域）

### 综述：深度学习电价预测
- TS615（中）[Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets](../../pdfs/2026_Yu_DeepLearningElectricityPrice_en.pdf) — 综述；目标：日前、日内、平衡市场电价；方法：深度学习（综述；骨干-输出头-损失三分解分类法）

### 多风电场超短期时空概率预测
- TS616（中）[STDHL: Spatio-Temporal Dynamic Hypergraph Learning for Wind Power Forecasting](../../pdfs/2024_Dong_STDHL_en.pdf) — 预测；目标：多风电场超短期风电功率（分位数）；方法：深度学习（动态超图卷积 + 分组时间卷积 + 分位数解码器）

### 风电集合预报误差校正（概率后处理）
- TS617（中）[Sequential Methods for Error Correction of Probabilistic Wind Power Forecasts](../../pdfs/2025_Jrgensen_SequentialMethodsErrorCorrection_en.pdf) — 预测；目标：陆上与海上风电日前功率的中位数与分位数；方法：混合（神经网络/LSTM 校正集合 + 时间自适应分位数回归 NABQR）

### 风电概率预测（缺失数据）
- TS618（中）[Marginalize, Rather than Impute: Probabilistic Wind Power Forecasting with Incomplete Data](../../pdfs/2024_Wen_MarginalizeRatherThanImpute_en.pdf) — 预测；目标：风电功率概率预测；方法：机器学习/深度学习（特征与目标的联合生成模型，部署时对缺失特征边缘化）

### 次季节风速预报
- TS307（低）[Improving Subseasonal Wind Speed Forecasts in Europe with a Nonlinear Model](../../pdfs/2024_Tian_ImprovingSubseasonalWindSpeed_en.pdf) — 预测；目标：欧洲次季节地面风速；方法：混合（多元线性回归 / CNN 从 Z500 回归地面风速 + 随机扰动）

### 多区域光伏任意分位数概率预测
- TS619（中）[Probabilistic Multi-Regional Solar Power Forecasting with Any-Quantile Recurrent Neural Networks](../../pdfs/2026_Smyl_ProbabilisticMultiRegionalSolar_en.pdf) — 预测；目标：欧洲 259 个区域光伏发电的任意分位数预测；方法：深度学习（任意分位数 RNN：双轨循环结构、空洞循环单元、分块时间建模、动态集成）

### 光伏爬坡事件识别与预测（预警）
- TS620（中）[Characterization and forecasting of national-scale solar power ramp events](../../pdfs/2026_Lanzilao_CharacterizationForecastingNationalScale_en.pdf) — 预警；目标：全国尺度光伏功率爬坡事件；方法：待全文核实

### 区域供热热负荷（零样本基础模型）
- TS621（中）[Systematic Evaluation of TabPFN-TS and Chronos-2 for Zero-Shot Heat Load Forecasting in District Heating Networks](../../pdfs/2026_Spoek_SystematicEvaluationTabPFNTS_en.pdf) — 预测；目标：德国两个区域供热网络的热负荷概率预测；方法：基础模型（TabPFN-TS、Chronos-2，上下文学习）对比训练基线

### 城市居民天然气月度需求预测
- TS622（中）[Forecasting monthly residential natural gas demand in two cities of Turkey using just-in-time-learning modeling](../../pdfs/2025_Alakent_ForecastingMonthlyResidentialNatural_en.pdf) — 预测；目标：土耳其布尔萨与开塞利居民天然气月需求；方法：统计 + 机器学习（SARIMA、ETS 对比 JITL-GPR 即时学习高斯过程回归）

### 建筑能源系统概率预测（基础模型微调）
- TS623（中）[Probabilistic Forecasting for Building Energy Systems using Time-Series Foundation Models](../../pdfs/2025_Park_ProbabilisticForecastingBuildingEnergy_en.pdf) — 预测；目标：商业净零能耗建筑的房间占用、碳排放、插座负荷、HVAC 能耗等；方法：基础模型（全量微调与 LoRA 参数高效微调）

### 电动汽车充电负荷概率预测（扩散模型）
- TS624（中）[DiffPLF: A Conditional Diffusion Model for Probabilistic Forecasting of EV Charging Load](../../pdfs/2024_Li_DiffPLF_en.pdf) — 预测；目标：电动汽车充电站充电负荷的概率分布；方法：深度学习（条件去噪扩散模型 + 交叉注意力条件机制 + 任务感知微调）

### 结构突变
- TS010（低）[Interval Forecasts for Gas Prices in the Face of Structural Breaks -- Statistical Models vs. Neural Networks](../../pdfs/2024_Schluter_IntervalForecastsGasPrices_en.pdf) — 预测；不确定性量化；评测比较；目标：欧洲天然气价格的区间预测，比较统计模型与神经网络在结构突变（俄乌战争、北溪 1 号爆炸冲击）下的稳健性；方法：统计 + 深度学习对比（条件异方差 ARMA、copula 时间序列模型 vs MLP、LSTM）

### 锂电池容量衰减轨迹预测 / 梯次利用
- TS206（高）[iMOE: prediction of second-life battery degradation trajectory using interpretable mixture of experts](../../pdfs/2026_Huang_IMOE_en.pdf) — 预测；目标：退役动力电池全寿命容量退化轨迹；方法：深度学习（可解释混合专家 + 使用依赖循环网络）

### 储能系统电池退化 / 概率预测
- TS217（中）[Predicting BESS Degradation with Uncertainty Quantification: A Probabilistic Framework for Battery Energy Storage Systems](../../pdfs/2026_Graner_PredictingBESSDegradationUncertainty_en.pdf) — 预测；目标：电池储能系统 SOH 退化（含 95% 预测区间）；方法：混合（深度学习生成应力条件下容量损失分布 + 随机退化轨迹传播 + 系统拓扑聚合）

### 数字孪生 / 核电设备退化预测
- TS228（中）[Digital twin-based hybrid framework for steam generator clogging prognostics](../../pdfs/2026_Jaber_DigitalTwinHybridFramework_en.pdf) — 预测；目标：蒸汽发生器管子支撑板堵塞率与 RUL；方法：物理-数据融合（物理仿真 + 多种不确定性量化技术）

### 风电齿轮箱 RUL / 不确定性
- TS230（中）[Accurate remaining useful life prediction and uncertainty quantification for wind turbines using temporal convolutional variational deep Gaussian processes](../../pdfs/2026_Cui_AccurateRemainingUsefulLife_en.pdf) — 预测；目标：风电机组齿轮箱 RUL 及置信区间；方法：混合（TCN + 序列注意力 + 变分深度高斯过程）

### 全球中期集合预报（扩散模型）
- TS254（高）[Probabilistic weather forecasting with machine learning](../../pdfs/2023_Price_ProbabilisticWeatherForecastingMachine_en.pdf) — 预测；目标：80 余个地面与高空变量的全球 15 天集合预报（含极端天气、热带气旋路径、风电出力）；方法：深度学习（条件扩散模型 GenCast）

### 集合预报后处理（Transformer）
- TS293（中）[Self-Attentive Transformer for Fast and Accurate Postprocessing of Temperature and Wind Speed Forecasts](../../pdfs/2024_Poecke_SelfAttentiveTransformerFast_en.pdf) — 预测；目标：2 m 温度、10 m 与 100 m 风速的集合成员订正（20 个预报时效）；方法：深度学习（自注意力 Transformer，逐成员后处理）

### 交通基础模型零样本评测
- TS449（高）[Time Series Foundation Models as Strong Baselines in Transportation Forecasting: A Large-Scale Benchmark Analysis](../../pdfs/2026_YanesPulido_TimeSeriesFoundationModels_en.pdf) — 基准/数据集；目标：高速公路交通量/流量、城市路段速度、共享单车需求、EV 充电站数据；方法：基础模型（Chronos-2 零样本）vs 统计与专用深度学习

### 持续学习：传感器网络扩张
- TS464（中）[Expand and Compress: Exploring Tuning Principles for Continual Spatio-Temporal Graph Forecasting](../../pdfs/2024_Chen_ExpandAndCompress_en.pdf) — 预测；目标：交通流量（并含空气质量、风能等）；方法：深度学习（STGNN + 连续提示池，提示微调）

### 限价订单簿（L3 事件）短期趋势预测
- TS549（低）[Event History Over Scale: Compact Transformers for Low-Latency Limit Order Book Forecasting](../../pdfs/2026_Schaurecker_EventHistoryOverScale_en.pdf) — 预测；目标：短期价格趋势（宏 F1）；方法：深度学习（约 7 千参数的紧凑因果 Transformer MBOFormer / MBOFusion）

