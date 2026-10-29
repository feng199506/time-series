# 气象与气候：阅读路线图

进度：已核验全文 66 / 目标约 50；待核验 2；下载失败 4。 近三年（已核验文献中）64 篇，占 0.97。
编号对应 [catalog_cn.csv](catalog_cn.csv)；简介与字段均依据摘要，未读全文。

## 优先阅读 10 篇

| 顺序 | 编号 | 标题 | 理由 |
|---|---|---|---|
| 1 | TS254 | [Probabilistic weather forecasting with machine learning](../../pdfs/2023_Price_ProbabilisticWeatherForecastingMachine_en.pdf) | 数据驱动概率集合预报的代表，几乎所有后续集合模型都与它比较。 |
| 2 | TS255 | [Neural general circulation models for weather and climate](../../pdfs/2023_Kochkov_NeuralGeneralCirculationModels_en.pdf) | 混合物理-ML 路线，同时覆盖天气与气候时间尺度。 |
| 3 | TS256 | [End-to-end data-driven weather prediction](../../pdfs/2024_Allen_EndEndDataDriven_en.pdf) | 端到端由观测到站点预报，改变 NWP 流程的范式。 |
| 4 | TS059 | [A foundation model for the Earth system](../../pdfs/2024_Bodnar_FoundationModelEarthSystem_en.pdf) | 基础模型 + 微调，覆盖天气、空气质量、海浪、TC。 |
| 5 | TS276 | [ChaosBench: A Multi-Channel, Physics-Based Benchmark for Subseasonal-to-Seasonal Climate Prediction](../../pdfs/2024_Nathaniel_ChaosBench_en.pdf) | 说明中期模型外推到 S2S 会失效，是 S2S 评测基础。 |
| 6 | TS287 | [Can AI weather models predict out-of-distribution gray swan tropical cyclones?](../../pdfs/2024_Sun_CanAIWeatherModels_en.pdf) | 检验 AI 模型能否外推到训练集中缺失的极端事件。 |
| 7 | TS292 | [Do AI weather models miss extremes?](../../pdfs/2026_Gabler_DoAIWeatherModels_en.pdf) | 用站点观测检验尾部表现，校正笼统结论。 |
| 8 | TS274 | [How Effective Are Time-Series Models for Precipitation Nowcasting? A Comprehensive Benchmark for GNSS-based Precipitation Nowcasting](../../pdfs/2025_Zhang_HowEffectiveTimeSeries_en.pdf) | 通用时序模型在降水/湿度站点序列上的表现，与通用方法类别交叉。 |
| 9 | TS257 | [AIFS -- ECMWF's data-driven forecasting system](../../pdfs/2024_Lang_AIFSECMWFSData_en.pdf) | （补位：原推荐条目未核验通过或不足 10 篇）首个由主要业务中心业务化运行的 ML 全球预报系统，代表数据驱动预报的业务落地。 |
| 10 | TS258 | [AIFS-CRPS: Ensemble forecasting using a model trained with a loss function based on the Continuous Ranked Probability Score](../../pdfs/2024_Lang_AIFSCRPS_en.pdf) | （补位：原推荐条目未核验通过或不足 10 篇）以评分规则直接训练集合模型的业务中心路线，与扩散类方法形成对照。 |

## 按子方向

### 全球中期集合预报（扩散模型）
- TS254（高）[Probabilistic weather forecasting with machine learning](../../pdfs/2023_Price_ProbabilisticWeatherForecastingMachine_en.pdf) — 预测；目标：80 余个地面与高空变量的全球 15 天集合预报（含极端天气、热带气旋路径、风电出力）；方法：深度学习（条件扩散模型 GenCast）

### 混合物理-机器学习大气环流模型
- TS255（高）[Neural general circulation models for weather and climate](../../pdfs/2023_Kochkov_NeuralGeneralCirculationModels_en.pdf) — 预测；目标：确定性与集合天气预报（1-15 天）及多年代气候指标（全球平均温度、热带气旋频率与路径）；方法：物理-数据融合（可微分动力求解器 + 机器学习物理参数化）

### 全球大气成分/空气质量预报（基础模型）
- TS059（高）[A foundation model for the Earth system](../../pdfs/2024_Bodnar_FoundationModelEarthSystem_en.pdf) — 预测；目标：空气质量（全球大气成分场，具体污染物待全文核实）；方法：基础模型（Aurora，大规模预训练+微调）

### 端到端观测到预报系统
- TS256（高）[End-to-end data-driven weather prediction](../../pdfs/2024_Allen_EndEndDataDriven_en.pdf) — 预测；目标：全球格点预报与站点局地预报（多变量）；方法：深度学习（神经过程 neural process 模型 Aardvark Weather）

### 业务化数据驱动全球预报
- TS257（高）[AIFS -- ECMWF's data-driven forecasting system](../../pdfs/2024_Lang_AIFSECMWFSData_en.pdf) — 预测；目标：高空变量、地面天气要素与热带气旋路径的中期预报；方法：深度学习（GNN 编码/解码 + 滑动窗口 Transformer 处理器，AIFS）

### 全球集合预报（CRPS 训练）
- TS258（高）[AIFS-CRPS: Ensemble forecasting using a model trained with a loss function based on the Continuous Ranked Probability Score](../../pdfs/2024_Lang_AIFSCRPS_en.pdf) — 预测；目标：中期与次季节全球集合预报；方法：深度学习（AIFS 变体，以 almost fair CRPS 为损失的随机模型）

### 全球集合预报（模型扰动）
- TS259（高）[Skillful joint probabilistic weather forecasting from marginals](../../pdfs/2025_Alet_SkillfulJointProbabilisticWeather_en.pdf) — 预测；目标：全球集合天气预报及热带气旋路径；方法：深度学习（FGN：学习的模型扰动 + 约束模型集合，按单点 CRPS 训练）

### 观测同化到预报一体化系统
- TS260（中）[A data-to-forecast machine learning system for global weather](../../pdfs/2024_Sun_DataForecastMachineLearning_en.pdf) — 预测；目标：全球 10 天天气预报（0.25°）；方法：深度学习（机器学习同化 + 预报系统 FuXi Weather）

### 全球概率预报（球面几何卷积）
- TS261（中）[FourCastNet 3: A geometric approach to probabilistic machine-learning weather forecasting at scale](../../pdfs/2025_Bonev_FourCastNet3_en.pdf) — 预测；目标：全球 0.25°、6 小时集合预报，最长 60 天；方法：深度学习（球面几何纯卷积网络 FourCastNet 3）

### 超大集合预报设计
- TS262（中）[Huge Ensembles Part I: Design of Ensemble Weather Forecasts using Spherical Fourier Neural Operators](../../pdfs/2024_Mahesh_HugeEnsemblesPartI_en.pdf) — 预测；目标：全球集合天气预报及极端天气（极端预报指数）；方法：深度学习（球面傅里叶神经算子 SFNO，参数扰动 + bred vectors 初值扰动）

### 图神经网络概率预报（全球与有限区）
- TS263（中）[Probabilistic Weather Forecasting with Hierarchical Graph Neural Networks](../../pdfs/2024_Oskarsson_ProbabilisticWeatherForecastingHierarchi_en.pdf) — 预测；目标：全球与有限区域集合天气预报；方法：深度学习（层次图神经网络 + 隐变量，Graph-EFM）

### 公里尺度对流允许模式仿真
- TS264（中）[Kilometer-Scale Convection Allowing Model Emulation using Generative Diffusion Modeling](../../pdfs/2024_Pathak_KilometerScaleConvectionAllowing_en.pdf) — 预测；目标：3 km 尺度 99 个状态变量（含组合雷达反射率）的逐小时自回归预报；方法：深度学习（生成式扩散模型 StormCast）

### 机器学习有限区域模式（公里尺度）
- TS265（中）[Building Machine Learning Limited Area Models: Kilometer-Scale Weather Forecasting in Realistic Settings](../../pdfs/2025_Adamov_BuildingMachineLearningLimited_en.pdf) — 预测；目标：丹麦与瑞士区域公里尺度多变量天气预报；方法：深度学习（图神经网络有限区域模式，多步滚动训练）

### 全球中期确定性预报（经典基线）
- TS266【三年前】（中）[GraphCast: Learning skillful medium-range global weather forecasting](../../pdfs/2022_Lam_GraphCast_en.pdf) — 预测；目标：全球数百个天气变量的 10 天预报（0.25°）；方法：深度学习（图神经网络 GraphCast）

### 评测基准（全球中期）
- TS267【三年前】（中）[WeatherBench 2: A benchmark for the next generation of data-driven global weather models](../../pdfs/2023_Rasp_WeatherBench2_en.pdf) — 基准/数据集；目标：全球 1-14 天天气预报的标准化评估；方法：其他（评测框架；比较物理模式与数据驱动模型）

### 降水临近预报（级联扩散）
- TS268（中）[CasCast: Skillful High-resolution Precipitation Nowcasting via Cascaded Modelling](../../pdfs/2024_Gong_CasCast_en.pdf) — 预测；目标：雷达降水场高分辨率临近预报（含区域极端降水）；方法：深度学习（确定性 + 隐空间帧引导扩散 Transformer 的级联框架 CasCast）

### 降水临近预报（残差扩散）
- TS269（中）[DiffCast: A Unified Framework via Residual Diffusion for Precipitation Nowcasting](../../pdfs/2023_Yu_DiffCast_en.pdf) — 预测；目标：雷达回波序列临近预报；方法：深度学习（残差扩散框架 DiffCast，可搭配任意时空模型）

### 降水临近预报（生成式语言模型）
- TS270（中）[GPTCast: a weather language model for precipitation nowcasting](../../pdfs/2024_Franch_GPTCast_en.pdf) — 预测；目标：雷达降水集合临近预报；方法：深度学习（VQ-VAE 分词 + GPT 自回归生成）

### 全球卫星降水临近预报（业务化）
- TS271（中）[An Operational Deep Learning System for Satellite-Based High-Resolution Global Nowcasting](../../pdfs/2025_Agrawal_OperationalDeepLearningSystem_en.pdf) — 预测；目标：全球降水未来 12 小时预报（约 5 km、15 分钟）；方法：深度学习（Global MetNet）

### 卫星驱动的雷达临近预报
- TS272（低）[Transformer-based nowcasting of radar composites from satellite images for severe weather](../../pdfs/2023_Kucuk_TransformerNowcastingRadarComposites_en.pdf) — 预测；目标：地基雷达组合图像序列（最长 2 小时）；方法：深度学习（Transformer）

### 2-6 小时“灰区”降水预报
- TS273（中）[StormDiT: A generative AI model bridges the 2-6 hour 'gray zone' in precipitation nowcasting](../../pdfs/2026_Sun_StormDiT_en.pdf) — 预测；目标：强对流雷达回波（≥35 dBZ）与强降水的 0-6 小时预报；方法：深度学习（统一生成式模型 StormDiT，扩散 Transformer）

### 站点降水时间序列临近预报基准
- TS274（中）[How Effective Are Time-Series Models for Precipitation Nowcasting? A Comprehensive Benchmark for GNSS-based Precipitation Nowcasting](../../pdfs/2025_Zhang_HowEffectiveTimeSeries_en.pdf) — 基准/数据集；目标：GNSS 站点未来 0-6 小时降水；方法：深度学习/基础模型（对 6 类架构 17 个时序模型基准测试；提出 BFPF 插件模块）

### 次季节到季节（S2S）评测基准
- TS276（高）[ChaosBench: A Multi-Channel, Physics-Based Benchmark for Subseasonal-to-Seasonal Climate Prediction](../../pdfs/2024_Nathaniel_ChaosBench_en.pdf) — 基准/数据集；目标：S2S 尺度多圈层气候预测；方法：其他（基准；评测 ViT/ClimaX、Pangu、GraphCast、FourCastNetV2 等）

### 次季节业务 ML 模型
- TS277（高）[AIFS-SUBS: Extending Data-Driven Forecasting to Sub-Seasonal Timescales](../../pdfs/2026_Schloer_AIFSSUBS_en.pdf) — 预测；目标：第 2-6 周全球概率预报；MJO、平流层突然增温、热带气旋活动调制；方法：深度学习（基于 AIFS-CRPS 微调的 AIFS-SUBS）

### 次季节概率偏差订正
- TS278（中）[Advancing Subseasonal Forecasting with Machine Learning](../../pdfs/2026_Guan_AdvancingSubseasonalForecastingMachine_en.pdf) — 预测；目标：第 2-6 周气压、温度、降水的全球概率预报；方法：机器学习（概率偏差订正 PBC）

### S2S 天气型与遥相关
- TS279（中）[Deep Learning Meets Teleconnections: Improving S2S Predictions for European Winter Weather](../../pdfs/2025_Bommer_DeepLearningMeetsTeleconnections_en.pdf) — 预测；目标：北大西洋-欧洲（NAE）冬季天气型未来六周；方法：深度学习（LSTM、Index-LSTM、ViT-LSTM）

### S2S 多圈层耦合概率模型
- TS280（低）[Skillful Subseasonal-to-Seasonal Forecasting of Extreme Events with a Multi-Sphere Coupled Probabilistic Model](../../pdfs/2025_Mu_SkillfulSubseasonalSeasonalForecasting_en.pdf) — 预测；目标：45 天逐日平均集合预报及极端事件（热浪、异常降水）；方法：深度学习（隐空间扩散模型 + 最优传输耦合模块，TianXing-S2S）

### 气候仿真器（次季节到年代际）
- TS281（中）[ACE2: Accurately learning subseasonal to decadal atmospheric variability and forced responses](../../pdfs/2024_WattMeyer_ACE2_en.pdf) — 预测；目标：近 80 年大气变率与强迫响应（MJO、热带气旋、平流层突然增温、ENSO 响应、温度趋势）；方法：深度学习（4.5 亿参数自回归仿真器 ACE2）

### ENSO 长时效预测
- TS282（中）[Toward long-range ENSO prediction with an explainable deep learning model](../../pdfs/2025_Chen_TowardLongRangeENSO_en.pdf) — 预测；目标：ENSO（Niño 指数）；方法：深度学习（CNN + Transformer，CTEFNet）

### ENSO 混合模型（小样本）
- TS283（中）[A Hybrid Deep-Learning Model for El Niño Southern Oscillation in the Low-Data Regime](../../pdfs/2024_Schloer_HybridDeepLearningModel_en.pdf) — 预测；目标：ENSO 演变（含热带西太平洋，超前 9 个月以上）；方法：混合（线性逆模型 LIM + 深度学习非马尔可夫订正）

### ENSO 不确定性量化
- TS284（低）[Am I confused or is this confusing?: Deep ensembles for ENSO uncertainty quantification](../../pdfs/2025_McAfee_AmIConfusedOr_en.pdf) — 预测；目标：ENSO 预测及其认知/偶然不确定性；方法：深度学习（深度集成概率神经网络）

### NAO 季节前预测
- TS285（低）[CNN-based forecasting of early winter NAO using sea surface temperature](../../pdfs/2026_Provenzano_CNNForecastingEarlyWinter_en.pdf) — 预测；目标：初冬（11-12 月）北大西洋涛动 NAO；方法：深度学习（CNN；线性模型为基准）

### 热带气旋路径与强度评测基准
- TS286（中）[TCBench: A Benchmark for Tropical Cyclone Track and Intensity Forecasting at the Global Scale](../../pdfs/2026_Gomez_TCBench_en.pdf) — 基准/数据集；目标：热带气旋 1-5 天路径与强度；方法：其他（基准；TempestExtremes 统一追踪）

### 灰天鹅热带气旋外推能力
- TS287（高）[Can AI weather models predict out-of-distribution gray swan tropical cyclones?](../../pdfs/2024_Sun_CanAIWeatherModels_en.pdf) — 预测；目标：5 级热带气旋（训练集中缺失的“灰天鹅”事件）预报；方法：深度学习（FourCastNet 多个训练版本对照实验）

### 热带气旋强度与降水（生成式降尺度）
- TS288（中）[FuXi-TC: A generative framework integrating deep learning and physics-based models for improved tropical cyclone forecasts](../../pdfs/2025_Guo_FuXiTC_en.pdf) — 预测；目标：热带气旋强度、风速与降水细尺度场；方法：混合（以 FuXi 大尺度预报为条件的扩散模型，FuXi-TC）

### AI 天气模型极端事件检验
- TS289（中）[Validating Deep Learning Weather Forecast Models on Recent High-Impact Extreme Events](../../pdfs/2024_Pasche_ValidatingDeepLearningWeather_en.pdf) — 预测；目标：极端热浪、湿热浪与冬季风暴个例的预报误差；方法：其他（比较评估）

### 热浪期间 AI 模型 2 m 温度误差
- TS290（中）[Turning Up the Heat: Assessing 2-m Temperature Forecast Errors in AI Weather Prediction Models During Heat Waves](../../pdfs/2025_Ennis_TurningUpHeatAssessing_en.pdf) — 预测；目标：60 次热浪期间 2 m 温度（CONUS 四个区域）；方法：其他（比较评估）

### 热浪预警服务的检验与订正
- TS291（中）[Evaluation and statistical correction of area-based heat index forecasts that drive a heatwave warning service](../../pdfs/2024_Loveday_EvaluationStatisticalCorrectionArea_en.pdf) — 预警；目标：澳大利亚区县热浪（热指数）多类别预警；方法：统计（FIRM 多类别评分 + 保序回归条件偏差订正）

### AI 模型尾部（极端）表现站点检验
- TS292（中）[Do AI weather models miss extremes?](../../pdfs/2026_Gabler_DoAIWeatherModels_en.pdf) — 预测；目标：10 m 风、2 m 温度、太阳辐射、降水在极端条件下的预报误差；方法：其他（比较评估）

### 集合预报后处理（Transformer）
- TS293（中）[Self-Attentive Transformer for Fast and Accurate Postprocessing of Temperature and Wind Speed Forecasts](../../pdfs/2024_Poecke_SelfAttentiveTransformerFast_en.pdf) — 预测；目标：2 m 温度、10 m 与 100 m 风速的集合成员订正（20 个预报时效）；方法：深度学习（自注意力 Transformer，逐成员后处理）

### 极端风速统计后处理（加权评分）
- TS294（中）[Improving Probabilistic Forecasts of Extreme Wind Speeds by Training Statistical Postprocessing Models with Weighted Scoring Rules](../../pdfs/2024_Wessel_ImprovingProbabilisticForecastsExtreme_en.pdf) — 预测；目标：极端风速概率预报；方法：统计（EMOS，以阈值加权 CRPS twCRPS 估计参数）

### 次季节风速预报
- TS307（低）[Improving Subseasonal Wind Speed Forecasts in Europe with a Nonlinear Model](../../pdfs/2024_Tian_ImprovingSubseasonalWindSpeed_en.pdf) — 预测；目标：欧洲次季节地面风速；方法：混合（多元线性回归 / CNN 从 Z500 回归地面风速 + 随机扰动）

### 全球大气成分/空气质量预报（业务数据驱动系统）
- TS060（高）[AIFS-COMPO: A Global Data-Driven Atmospheric Composition Forecasting System](../../pdfs/2026_Harder_AIFSCOMPO_en.pdf) — 预测；目标：气溶胶与反应性气体（多种大气成分）；方法：深度学习（Transformer 编码-处理-解码，AIFS 架构）

### 全球气溶胶/沙尘预报
- TS061（高）[Advancing global aerosol forecasting with artificial intelligence](../../pdfs/2024_Gui_AdvancingGlobalAerosolForecasting_en.pdf) — 预测；目标：气溶胶光学组分与地面浓度（AOD、沙尘组分等）；方法：深度学习（Vision Transformer + U-Net）

### 多任务气象-污染联合预报
- TS076（中）[AirCast: Improving Air Pollution Forecasting Through Multi-Variable Data Alignment](../../pdfs/2025_Nedungadi_AirCast_en.pdf) — 预测；目标：污染物浓度（并联合预测气象变量）；方法：深度学习（多任务头 + 频率加权 MAE 损失）

### 沙尘能见度等级预报（NWP 后处理）
- TS101（低）[A physics-guided machine learning framework for enhancing dust storm visibility prediction in arid and semi-arid regions](../../pdfs/2026_Xu_PhysicsGuidedMachineLearning_en.pdf) — 预测；目标：五级有序能见度等级（沙尘影响）；方法：物理-数据融合（沙尘生命周期特征库 + 有序 LightGBM）

### 季节预测（中国 PM2.5 主模态）
- TS111（低）[Lagged sea-surface-temperature precursors of the leading PM2.5 mode in China](../../pdfs/2026_Chen_LaggedSeaSurfaceTemperature_en.pdf) — 预测；目标：中国 PM2.5 主导变率模态（夏季与冬季）；方法：统计（模态分析 + 简单回归）

### 气候模式臭氧偏差订正（未来情景）
- TS114（低）[Applying deep learning to a chemistry-climate model for improved ozone prediction](../../pdfs/2025_Liu_ApplyingDeepLearningChemistry_en.pdf) — 预测；目标：地面臭氧（UKESM1 偏差订正）；方法：深度学习（六种统计/DL 模型，Transformer 最好，加权集成）

### 陆架海营养盐/浮游植物业务预报：机器学习 + 数据同化
- TS141（高）[Assimilation of machine‐learning‐predicted nitrate to improve the quality of phytoplankton forecasting in the shelf‐sea environment](../../pdfs/2025_Banerjee_AssimilationMachineLearningPredicted_en.pdf) — 预测；目标：浮游植物（叶绿素）短期预报；表层硝酸盐；方法：物理-数据融合（神经网络预测硝酸盐 + 同化进动力模型）

### 气候变化下湖泊表层水温可预测性
- TS159（中）[How climate change erodes short-term lake-temperature predictability: Informing climate resilient lake forecasting](../../pdfs/2025_Beckmann_HowClimateChangeErodes_en.pdf) — 预测；目标：日湖泊表层水温（14 天预测）；方法：机器学习/深度学习（随机森林、GRU）

### 综述：湖泊水温建模
- TS185（低）[Lake Water Temperature Modeling in an Era of Climate Change: Data Sources, Models, and Future Prospects](../../pdfs/2024_Piccolroaz_LakeWaterTemperatureModeling_en.pdf) — 综述；目标：湖泊水温；方法：综述

### 登革热概率预测挑战与集合
- TS324（高）[Leveraging probabilistic forecasts for dengue preparedness and control: The 2024 Dengue Forecasting Sprint in Brazil](../../pdfs/2026_Araujo_LeveragingProbabilisticForecastsDengue_en.pdf) — 预测；目标：巴西五个州 2024、2025 季登革热病例数（概率预测）；方法：其他（六个国际团队的机器学习与经典统计模型 + 集合）

### 急诊就诊量概率预测（预测组合）
- TS345（中）[Ascertaining cause-specific emergency department demand using forecast combinations](../../pdfs/2025_Guo_AscertainingCauseSpecificEmergency_en.pdf) — 预测；目标：新加坡按病因分类的急诊就诊数（概率预测）；方法：统计/机器学习（线性/非线性、静态/动态权重的概率预测组合）

### 疟疾病例预测（气候驱动）
- TS364（低）[Forecasting malaria cases using climate variability in Sierra Leone](../../pdfs/2025_Jalloh_ForecastingMalariaCasesClimate_en.pdf) — 预测；目标：塞拉利昂疟疾病例数；方法：统计/机器学习（SARIMA、SARIMAX、人工神经网络）

### 极端天气下城轨 OD 客流（物理类比约束）
- TS459（高）[OhmicFlow: Forecasting transit passenger flow under extreme weather disruptions via Ohm's law](../../pdfs/2026_Li_OhmicFlow_en.pdf) — 预测；目标：极端天气扰动下的 OD 客流（并推断潜在需求与出行阻抗）；方法：物理-数据融合（欧姆定律类比：需求=电压、阻抗=电阻、客流=电流）

### 极端天气下的城市流（解耦 + 因果增强）
- TS480（中）[WED-Net: A Weather-Effect Disentanglement Network with Causal Augmentation for Urban Flow Prediction](../../pdfs/2026_Hong_WEDNet_en.pdf) — 预测；目标：出租车流量（城市流）；方法：深度学习（双分支 Transformer 解耦 + 记忆库 + 天气判别器 + 因果数据增强）

### 航空：机场到达延误
- TS488（中）[Airport Delay Prediction with Temporal Fusion Transformers](../../pdfs/2024_Liu_AirportDelayPredictionTemporal_en.pdf) — 预测；目标：机场到达延误（数值，15 分钟级）；方法：深度学习（Temporal Fusion Transformer）

### 风电短期至中期无缝概率预测
- TS586（高）[Seamless short- to mid-term probabilistic wind power forecasting](../../pdfs/2025_Dantas_SeamlessShortMidTerm_en.pdf) — 预测；目标：风电场功率概率预测（6-162 小时）；方法：统计/机器学习（整合天气预报不确定性与天气-功率转换不确定性；具体模型待全文核实）

### 全国尺度光伏日内时空预测（卫星）
- TS588（高）[Intraday spatiotemporal PV power prediction at national scale using satellite-based solar forecast models](../../pdfs/2026_Lanzilao_IntradaySpatiotemporalPVPower_en.pdf) — 预测；目标：瑞士 6434 个光伏电站日内功率（经辐照度场转换）；方法：深度学习/光流/物理 NWP 七类模型比较（确定性与概率）；站点级机器学习功率转换

### 日前辐照度概率预测（卫星 + 地面站）
- TS589（高）[SolarCrossFormer: Improving Day-Ahead Solar Irradiance Forecasting by Integrating Satellite Imagery and Ground Sensors](../../pdfs/2025_Schubnel_SolarCrossFormer_en.pdf) — 预测；目标：瑞士任意位置的地表太阳辐照度概率预测；方法：深度学习（图神经网络刻画模态内/模态间相关的 Transformer 类模型）

### 大范围辐照度预测（卫星驱动 AI 替代 NWP）
- TS590（高）[SolarSeer: Ultrafast and accurate 24-hour solar irradiance forecasts outperforming numerical weather prediction across the USA](../../pdfs/2025_Bai_SolarSeer_en.pdf) — 预测；目标：美国本土 24 小时云量与太阳辐照度（5 km）；方法：深度学习（端到端大型 AI 模型，卫星观测直接映射到未来预报）

### 图像驱动的光伏临近预报全球基准
- TS594（高）[SolarBench: A global solar energy nowcasting benchmark](../../pdfs/2026_Nie_SolarBench_en.pdf) — 基准/数据集；目标：辐照度或光伏出力临近预报；方法：深度学习（代表性模型基准）+ 开源工具箱

### 天气基础模型微调用于电网资产级气象预报与覆冰预警
- TS598（高）[A Weather Foundation Model for the Power Grid](../../pdfs/2025_Bodnar_WeatherFoundationModelPower_en.pdf) — 预测；目标：电网资产级温度、降水、轮毂高度风速、风机覆冰风险、导线雾凇覆冰；方法：基础模型（微调 15 亿参数天气基础模型 GFT）

### 极端天气下负荷概率预测（小样本）
- TS605（中）[Resilient Load Forecasting under Climate Change: Adaptive Conditional Neural Processes for Few-Shot Extreme Load Forecasting](../../pdfs/2026_Hu_ResilientLoadForecastingUnder_en.pdf) — 预测；目标：极端天气期间的电力负荷概率预测；方法：深度学习（自适应条件神经过程 AdaCNP，元学习/小样本）

### 光伏爬坡事件识别与预测（预警）
- TS620（中）[Characterization and forecasting of national-scale solar power ramp events](../../pdfs/2026_Lanzilao_CharacterizationForecastingNationalScale_en.pdf) — 预警；目标：全国尺度光伏功率爬坡事件；方法：待全文核实

### 海洋生物地球化学（浮游植物/营养等）深度学习仿真器预报
- TS646（高）[Deep learning model emulators for marine biogeochemistry forecasting from days to decades](../../pdfs/2026_Skakala_DeepLearningModelEmulators_en.pdf) — 预测；目标：水柱生物地球化学变量（浮游植物、浮游动物等；春季藻华时间）；方法：深度学习（LSTM；物理信息 1D CNN 仿真器）

