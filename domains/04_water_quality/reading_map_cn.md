# 水质：阅读路线图

进度：已核验全文 50 / 目标约 50；待核验 0；下载失败 22。 近三年（已核验文献中）50 篇，占 1.0。
编号对应 [catalog_cn.csv](catalog_cn.csv)；简介与字段均依据摘要，未读全文。

## 优先阅读 10 篇

| 顺序 | 编号 | 标题 | 理由 |
|---|---|---|---|
| 1 | TS124 | [Extended-range forecasting of stream water temperature with deep-learning models](../../pdfs/2024_Padron_ExtendedRangeForecastingStream_en.pdf) | 可业务化的 32 天概率水温预报（TFT，CRPS 评估，新站外推）。 |
| 2 | TS128 | [Explainable deep learning for multi-horizon water quality forecasting: cross-continental transferability for environmental decision support](../../pdfs/2026_Tavares_ExplainableDeepLearningMulti_en.pdf) | 与持续性基线比较并做跨洲零样本迁移，结论审慎。 |
| 3 | TS126 | [Identifying trustworthiness challenges in deep learning models for continental-scale water quality prediction](../../pdfs/2025_Xia_IdentifyingTrustworthinessChallengesDeep_en.pdf) | 482 流域 20 变量的深度模型可信度系统评估。 |
| 4 | TS131 | [LakeFM : Toward a Foundation Model for Aquatic Ecosystems Using Irregular Multivariate Multi-depth Time Series Data](../../pdfs/2026_Neog_LakeFM_en.pdf) | 面向湖泊不规则多深度数据的基础模型。 |
| 5 | TS136 | [Time-series foundation modeling enables accurate lake ecosystem forecasting](../../pdfs/2026_Matsushita_TimeSeriesFoundationModeling_en.pdf) | Chronos/Lag-Llama 在长期月度湖泊数据上与 15 种方法对比（预印本）。 |
| 6 | TS132 | [Forecasting coastal hypoxia using a blend of mechanistic and artificial intelligence models](../../pdfs/2025_Ou_ForecastingCoastalHypoxiaBlend_en.pdf) | 机理模型后报训练 AI 的近海缺氧日预报。 |
| 7 | TS164 | [Machine Learning for Effluent Forecasting at a Full-Scale Municipal Wastewater Treatment Plant: Seasonal Performance Deterioration and the Decisive Role of Prediction Horizon](../../pdfs/2026_Vukmirovic_MachineLearningEffluentForecasting_en.pdf) | 污水厂预测与朴素基线严格比较，揭示插值日评估造成的虚高。 |
| 8 | TS125 | [Deep learning for water quality](../../pdfs/2024_Zhi_DeepLearningWaterQuality_en.pdf) | （补位：原推荐条目未核验通过或不足 10 篇）领域权威综述，可作为本类阅读起点与方法地图。 |
| 9 | TS129 | [LSTM networks provide efficient cyanobacterial blooms forecasting even with incomplete spatio-temporal data](../../pdfs/2024_Fournier_LSTMNetworksProvideEfficient_en.pdf) | （补位：原推荐条目未核验通过或不足 10 篇）Water Research 发表，直面缺测高频传感器数据的水华预警，方法可复用。 |
| 10 | TS135 | [Evaluating Deep Learning Approaches for Predictions in Unmonitored Basins with Continental-scale Stream Temperature Models](../../pdfs/2024_Willard_EvaluatingDeepLearningApproaches_en.pdf) | （补位：原推荐条目未核验通过或不足 10 篇）无资料流域（PUB）水温预测的系统设计实验，回答数据与模型设计问题。 |

## 按子方向

### 河流水温（延伸期概率预测）
- TS124（高）[Extended-range forecasting of stream water temperature with deep-learning models](../../pdfs/2024_Padron_ExtendedRangeForecastingStream_en.pdf) — 预测；目标：日最高河流水温（未来 32 天，概率预测）；方法：深度学习（TFT、RNN 编解码、N-HiTS）对比 RF/MLP/AR

### 综述：深度学习水质建模
- TS125（高）[Deep learning for water quality](../../pdfs/2024_Zhi_DeepLearningWaterQuality_en.pdf) — 综述；目标：水质变量（综述范围待全文核实）；方法：综述（深度学习）

### 大尺度多变量河流水质预测与可信度评估
- TS126（高）[Identifying trustworthiness challenges in deep learning models for continental-scale water quality prediction](../../pdfs/2025_Xia_IdentifyingTrustworthinessChallengesDeep_en.pdf) — 预测；目标：20 种河流水质变量；方法：深度学习（LSTM、DeepONet、Informer）

### 河流多参数多步预测与跨洲迁移
- TS128（高）[Explainable deep learning for multi-horizon water quality forecasting: cross-continental transferability for environmental decision support](../../pdfs/2026_Tavares_ExplainableDeepLearningMulti_en.pdf) — 预测；目标：溶解氧、营养盐、硝酸盐、痕量金属超标等；方法：深度学习（注意力 LSTM）对比随机森林与持续性基线

### 蓝藻水华预测与预警
- TS129（高）[LSTM networks provide efficient cyanobacterial blooms forecasting even with incomplete spatio-temporal data](../../pdfs/2024_Fournier_LSTMNetworksProvideEfficient_en.pdf) — 预警；目标：蓝藻（藻蓝蛋白 PC 荧光）；方法：统计+机器学习+深度学习（线性回归、随机森林、LSTM 的自回归与多变量版本）

### 湖泊水质基础模型（不规则多深度时间序列）
- TS131（高）[LakeFM : Toward a Foundation Model for Aquatic Ecosystems Using Irregular Multivariate Multi-depth Time Series Data](../../pdfs/2026_Neog_LakeFM_en.pdf) — 预测；目标：湖泊多变量、多深度水质/生态变量；方法：基础模型（预训练）

### 近海低氧（缺氧）日预报：机理模型 + AI
- TS132（高）[Forecasting coastal hypoxia using a blend of mechanistic and artificial intelligence models](../../pdfs/2025_Ou_ForecastingCoastalHypoxiaBlend_en.pdf) — 预测；目标：路易斯安那-得克萨斯陆架日缺氧事件；方法：物理-数据融合（用机理模型后报训练轻量 AI）

### 无资料流域河流水温预测
- TS135（高）[Evaluating Deep Learning Approaches for Predictions in Unmonitored Basins with Continental-scale Stream Temperature Models](../../pdfs/2024_Willard_EvaluatingDeepLearningApproaches_en.pdf) — 预测；目标：河流水温；方法：深度学习（自上而下大样本模型 vs 自下而上迁移 vs 分组模型）

### 时序基础模型用于湖泊叶绿素 a 预测
- TS136（高）[Time-series foundation modeling enables accurate lake ecosystem forecasting](../../pdfs/2026_Matsushita_TimeSeriesFoundationModeling_en.pdf) — 预测；目标：叶绿素 a 及其他水质变量；方法：基础模型（Chronos-T5、Lag-Llama）对比统计（AR/ARIMA/SARIMA/Prophet）、机器学习与深度学习

### 跨流域迁移/表征学习水质预测
- TS137（高）[Deep representation learning enables cross-basin water quality prediction under data-scarce conditions](../../pdfs/2025_Zheng_DeepRepresentationLearningEnables_en.pdf) — 预测；目标：地表水多指标水质；方法：深度学习（预训练表征学习 + 迁移）

### 水库水温剖面近期预测：多模型集合
- TS139（高）[A Multi‐Model Ensemble of Baseline and Process‐Based Models Improves the Predictive Skill of Near‐Term Lake Forecasts](../../pdfs/2024_Olsson_MultiModelEnsembleBaseline_en.pdf) — 预测；目标：水库水温剖面；方法：混合：过程模型 + 经验模型的多模型集合

### 湖泊溶解氧：过程引导学习
- TS140（中）[Adaptive Process-Guided Learning: An Application in Predicting Lake DO Concentrations](../../pdfs/2024_Yu_AdaptiveProcessGuidedLearning_en.pdf) — 预测；目标：湖泊分层溶解氧浓度；方法：物理-数据融合（RNN + 分层溶解氧微分方程，生成器-判别器自适应步长）

### 陆架海营养盐/浮游植物业务预报：机器学习 + 数据同化
- TS141（高）[Assimilation of machine‐learning‐predicted nitrate to improve the quality of phytoplankton forecasting in the shelf‐sea environment](../../pdfs/2025_Banerjee_AssimilationMachineLearningPredicted_en.pdf) — 预测；目标：浮游植物（叶绿素）短期预报；表层硝酸盐；方法：物理-数据融合（神经网络预测硝酸盐 + 同化进动力模型）

### 供水管网水质（余氯等）时空预测：图 + PINN
- TS145（中）[ST-GPINN: a spatio-temporal graph physics-informed neural network for enhanced water quality prediction in water distribution systems](../../pdfs/2025_Mu_STGPINN_en.pdf) — 预测；目标：管网节点水质浓度（mg/L，具体物质待全文核实）；方法：物理-数据融合（水力模拟 + PINN + GNN）

### 水库叶绿素 a 多步预测（N-BEATS）
- TS148（中）[Deep learning methods for multi-horizon long-term forecasting of Harmful Algal Blooms](../../pdfs/2024_MartinSuazo_DeepLearningMethodsMulti_en.pdf) — 预测；目标：叶绿素 a；方法：深度学习（N-BEATS 对比 LSTM、CNN）

### 大型湖泊叶绿素 a 短期预测
- TS150（中）[Forecasting short-term chlorophyll a concentration in Lake Erie using the machine learning XGBoost algorithm](../../pdfs/2025_Song_ForecastingShortTermChlorophyll_en.pdf) — 预测；目标：叶绿素 a；方法：机器学习（XGBoost）+ SHAP

### 蓝藻警戒等级预测（不平衡分类）
- TS152（低）[Machine Learning-Based Early Warning Level Prediction for Cyanobacterial Blooms Using Environmental Variable Selection and Data Resampling](../../pdfs/2023_Kim_MachineLearningEarlyWarning_en.pdf) — 预警；目标：藻类警戒等级（L0/L1/L2）；方法：机器学习（ANN、随机森林）+ 特征选择 + 重采样

### 湖泊水温预测：高斯过程代理 + 偏差校正
- TS158（中）[Synthesizing data products, mathematical models, and observational measurements for lake temperature forecasting](../../pdfs/2024_Holthuijzen_SynthesizingDataProductsMathematical_en.pdf) — 预测；目标：湖泊水温；方法：统计 / 物理-数据融合（GLM 过程模型的高斯过程代理与偏差校正）

### 气候变化下湖泊表层水温可预测性
- TS159（中）[How climate change erodes short-term lake-temperature predictability: Informing climate resilient lake forecasting](../../pdfs/2025_Beckmann_HowClimateChangeErodes_en.pdf) — 预测；目标：日湖泊表层水温（14 天预测）；方法：机器学习/深度学习（随机森林、GRU）

### 饮用水厂运行数据在线预测（强化学习预测）
- TS160（低）[GVFs in the real world: making predictions online for water treatment](../../pdfs/2023_Janjua_GVFsRealWorldMaking_en.pdf) — 预测；目标：水厂传感器变量的广义价值函数（折扣累积和）预测；方法：深度学习/强化学习（TD 学习的 GVF 预测）对比 n 步预测

### 供水系统水质时间序列分析（ARIMA/传递函数）
- TS161（低）[ARIMA and TFARIMA Analysis of the Main Water Quality Parameters in the Initial Components of a Megacity’s Drinking Water Supply System](../../pdfs/2024_ZafraMejia_ARIMATFARIMAAnalysisMain_en.pdf) — 预测；目标：浊度、色度、总铁等水质参数；方法：统计（ARIMA、传递函数 TFARIMA）

### 配水清水池余氯不足风险提前一个月预警
- TS162（中）[A data‐driven predictive model for disinfectant residual in drinking water storage tanks](../../pdfs/2024_Kyritsakas_DataDrivenPredictiveModel_en.pdf) — 预警；目标：清水池低消毒剂余量风险等级；方法：机器学习（具体算法待全文核实）

### 应急供水家庭端余氯概率预测
- TS163（低）[Training for the test: Using multi-objective training to improve ANN ensemble forecasts of household residual chlorine in emergencies](../../pdfs/2025_Santi_TrainingTestMultiObjective_en.pdf) — 预测；目标：配送后（家庭储存）游离余氯；方法：机器学习（ANN 集合预测系统 + 多目标训练）

### 污水厂出水预测：与朴素基线对比
- TS164（高）[Machine Learning for Effluent Forecasting at a Full-Scale Municipal Wastewater Treatment Plant: Seasonal Performance Deterioration and the Decisive Role of Prediction Horizon](../../pdfs/2026_Vukmirovic_MachineLearningEffluentForecasting_en.pdf) — 预测；目标：出水总氮、COD 及总氮超标（15 mg/L）；方法：机器学习（四类模型）对比持续性与滚动均值基线

### 工业污水处理溶解氧预测：迁移学习 + 物理信息
- TS165（低）[A Hybrid Approach of Transfer Learning and Physics-Informed Modeling: Improving Dissolved Oxygen Concentration Prediction in an Industrial Wastewater Treatment Plant](../../pdfs/2024_Koksal_HybridApproachTransferLearning_en.pdf) — 预测；目标：工业污水处理单元溶解氧浓度；方法：物理-数据融合（迁移学习 + 物理信息目标函数）

### 河流大肠杆菌达标状态多年预警
- TS167（低）[From Compliant to Critical: Forecasting Emerging E. coli Risk in New Zealand’s South Island Rivers](../../pdfs/2026_Tiwari_CompliantCriticalForecastingEmerging_en.pdf) — 预警；目标：大肠杆菌最差等级（Band E）不达标；方法：机器学习（LightGBM 汇总分类器）对比持续性、趋势外推、多数类基线

### 河网水质传感器异常检测
- TS168（中）[Unsupervised Anomaly Detection in Spatio‐Temporal Stream Network Sensor Data](../../pdfs/2024_SantosFernandez_UnsupervisedAnomalyDetectionSpatio_en.pdf) — 异常检测；目标：水质传感器技术性异常；方法：统计（后验预测分布、有限混合、隐马尔可夫模型，贝叶斯递推）

### 地下水硝酸盐长期时间序列与政策效果分析
- TS169（低）[Multivariate and long-term time series analysis to assess the effect of nitrogen management policy on groundwater quality in Wallonia, BE](../../pdfs/2024_Verstraeten_MultivariateLongTermTime_en.pdf) — 因果分析；目标：地下水硝酸盐浓度状态与趋势指标；方法：统计（六类污染指标 + 解释变量分析）

### 河流氨氮多尺度长期预测
- TS170（低）[Long-term AI prediction of ammonium levels in rivers using transformer and ensemble models](../../pdfs/2024_Ali_LongTermAIPrediction_en.pdf) — 预测；目标：河流铵（NH4+）浓度；方法：深度学习 + 集成学习（TFT、随机森林、XGBoost）

### 湖泊透明度（Secchi 深度）预测与缺测
- TS171（低）[Data-Driven Lake Water Quality Forecasting for Time Series with Missing Data Using Machine Learning](../../pdfs/2026_Chatterjee_DataDrivenLakeWater_en.pdf) — 预测；目标：Secchi 盘深度（水体透明度）；方法：统计/机器学习（岭回归等 6 种模型 + MICE 多重插补）

### 综述：河流（流动水体）有害藻华预测模型
- TS172（中）[A systematic literature review of forecasting and predictive models of harmful algal blooms in flowing waters](../../pdfs/2025_Murphy_SystematicLiteratureReviewForecasting_en.pdf) — 综述；目标：河流有害藻华（生物量、叶绿素、毒素等）；方法：综述

### 综述：机器学习河流水温建模与评价指标
- TS173（中）[Machine learning in stream and river water temperature modeling: a review and metrics for evaluation](../../pdfs/2024_Corona_MachineLearningStreamRiver_en.pdf) — 综述；目标：河流水温；方法：综述

### 湖泊浮游植物实时预报系统框架
- TS174（低）[A framework for developing a real-time lake phytoplankton forecasting system to support water quality management in the face of global change](../../pdfs/2024_Carey_FrameworkDevelopingRealTime_en.pdf) — 综述；目标：浮游植物（水华）；方法：其他（框架与研究议程）

### 过程模型（FLARE）湖泊水温与溶解氧概率预报
- TS175（中）[Process-based forecasts of lake water temperature and dissolved oxygen outperform null models, with variability over time and depth](../../pdfs/2024_Woelmer_ProcessForecastsLakeWater_en.pdf) — 预测；目标：多深度湖泊水温与溶解氧；方法：物理-数据融合（FLARE：一维水动力-生物地球化学模型 + 数据同化）

### 河网水温图神经网络（公平性）
- TS177（低）[Physics-Guided Fair Graph Sampling for Water Temperature Prediction in River Networks](../../pdfs/2024_He_PhysicsGuidedFairGraph_en.pdf) — 预测；目标：河流水温；方法：物理-数据融合（物理引导的图采样 GNN）

### 运河总磷时空预测
- TS178（低）[Prediction of Total Phosphorus Concentration in Canals by GAT-Informer Model Based on Spatiotemporal Correlations](../../pdfs/2024_Huan_PredictionTotalPhosphorusConcentration_en.pdf) — 预测；目标：总磷；方法：深度学习（GAT + Informer）

### 遥感时间序列蓝藻强度多步预测
- TS179（低）[From Remote Sensing to Multiple Time Horizons Forecasts: Transformers Model for CyanoHAB Intensity in Lake Champlain](../../pdfs/2025_Adil_RemoteSensingMultipleTime_en.pdf) — 预测；目标：蓝藻指数（CyanoHAB 强度）；方法：深度学习（Transformer + BiLSTM）

### 近海有害藻华（拟菱形藻）发生预测
- TS180（低）[Predicting Pseudo-nitzschia harmful algal blooms along the Portuguese Coast using satellite-derived predictors](../../pdfs/2026_Bnoussaad_PredictingPseudoNitzschiaHarmful_en.pdf) — 预警；目标：拟菱形藻有害藻华发生；方法：机器学习（具体待全文核实）

### 管网余氯状态估计基准
- TS183（低）[A Benchmark for Physics-informed Machine Learning of Chlorine Concentration States in Water Distribution Networks](../../pdfs/2025_Hermes_BenchmarkPhysicsInformedMachine_en.pdf) — 基准/数据集；目标：管网余氯浓度状态；方法：物理-数据融合（基准）

### 污水厂传感器缺测插补（扩散模型）
- TS184（低）[STDiff: A state transition diffusion framework for time series imputation in industrial systems](../../pdfs/2025_Simethy_STDiff_en.pdf) — 插补；目标：污水厂关键传感器缺测段；方法：深度学习（扩散模型 STDiff/STDiff-W）对比 SAITS、BRITS、CSDI

### 综述：湖泊水温建模
- TS185（低）[Lake Water Temperature Modeling in an Era of Climate Change: Data Sources, Models, and Future Prospects](../../pdfs/2024_Piccolroaz_LakeWaterTemperatureModeling_en.pdf) — 综述；目标：湖泊水温；方法：综述

### 近海遥感水质时间序列（叶绿素 a、悬浮物、浊度）
- TS186（低）[Improving Water Quality Time-Series Prediction in Hong Kong using Sentinel-2 MSI Data and Google Earth Engine Cloud Computing](../../pdfs/2024_Sood_ImprovingWaterQualityTime_en.pdf) — 预测；目标：叶绿素 a、悬浮固体、浊度；方法：深度学习（LSTM）

### 污水厂数字孪生开环模拟（12–36 小时）
- TS188（低）[Data-Driven Open-Loop Simulation for Digital-Twin Operator Decision Support in Wastewater Treatment](../../pdfs/2026_Simethy_DataDrivenOpenLoop_en.pdf) — 预测；目标：污水厂传感器状态（规定控制方案下的响应）；方法：深度学习（受控连续时间状态空间模型 CCSS-RS）

### 有害藻华发生前的微生物（宏蛋白质组）早期预警指标
- TS642（高）[Harmful algal blooms are preceded by a predictable and quantifiable shift in the oceanic microbiome](../../pdfs/2025_Mudge_HarmfulAlgalBloomsPreceded_en.pdf) — 预警；目标：有害藻华暴发起始（以细菌肽段生物标志物提前识别）；方法：其他（宏蛋白质组学时间序列 + 生物标志物筛选与相关分析）

### 湖泊水质时间序列与垂向剖面基准数据集
- TS643（高）[LakeBeD-US: a benchmark dataset for lake water quality time series and vertical profiles](../../pdfs/2025_McAfee_LakeBeDUS_en.pdf) — 基准/数据集；目标：17 个湖泊水质变量的时间序列与垂向剖面（供机器学习水质预测基准使用）；方法：其他（数据集构建与整理）

### 降雨驱动的河流水质多尺度预测（多模态：站点序列 + 降水栅格）
- TS644（高）[Learning Intrinsic Water-Quality Dynamics with Rainfall for Data-Driven Forecasting](../../pdfs/2025_Wang_LearningIntrinsicWaterQuality_en.pdf) — 预测；目标：监测站水质指标序列（具体指标待全文核实）；方法：深度学习（RaiNet：LocTrend 不规则动态建模 + 站点降雨事件构建 + XGateFusion 滞后感知融合）

### 湖泊水温与溶解氧：物理感知检索增强的跨湖迁移
- TS645（高）[PIER: Physics-Informed Environmental Retrieval for Time-Series Modeling](../../pdfs/2026_Luo_PIER_en.pdf) — 预测；目标：湖泊水温与溶解氧；方法：物理-数据融合（检索增强 + 基于通量特征的物理一致性验证器，模型无关）

### 海洋生物地球化学（浮游植物/营养等）深度学习仿真器预报
- TS646（高）[Deep learning model emulators for marine biogeochemistry forecasting from days to decades](../../pdfs/2026_Skakala_DeepLearningModelEmulators_en.pdf) — 预测；目标：水柱生物地球化学变量（浮游植物、浮游动物等；春季藻华时间）；方法：深度学习（LSTM；物理信息 1D CNN 仿真器）

### 河流溶解氧：超统计涨落分析 + Transformer 长期预测
- TS647（高）[Analyzing spatio-temporal dynamics of dissolved oxygen for the River Thames using superstatistical methods and machine learning](../../pdfs/2024_He_AnalyzingSpatioTemporalDynamics_en.pdf) — 预测；目标：溶解氧浓度（同时刻回归与长期预测）；方法：统计 + 机器学习 + 深度学习（q-Gaussian 超统计、EMD 去趋势、LightGBM + SHAP、Informer/Transformer）

### 河口咸潮上溯（氯度超标时长）归因与预报
- TS648（高）[Attribution analysis and forecast of salinity intrusion in the Modaomen estuary of the Pearl River Delta](../../pdfs/2024_Tian_AttributionAnalysisForecastSalinity_en.pdf) — 预测；目标：日氯度超标时长（咸潮上溯严重程度）；方法：统计 + 深度学习（EOF、决策树归因；LSTM、CNN 预测）

