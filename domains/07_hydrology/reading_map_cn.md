# 水文与水资源：阅读路线图

进度：已核验全文 50 / 目标约 50；待核验 0；下载失败 1。 近三年（已核验文献中）46 篇，占 0.92。
编号对应 [catalog_cn.csv](catalog_cn.csv)；简介与字段均依据摘要，未读全文。

## 优先阅读 10 篇

| 顺序 | 编号 | 标题 | 理由 |
|---|---|---|---|
| 1 | TS383 | [AIFL: A global daily streamflow forecasting model using deterministic an LSTM pre-trained on ERA5-Land and fine-tuned on IFS](../../pdfs/2026_Taccari_AIFL_en.pdf) | 业务预报驱动下的数据驱动全球基线，按时间外推评测。 |
| 2 | TS384 | [HESS Opinions: Never train a Long Short-Term Memory (LSTM) network on a single basin](../../pdfs/2024_Kratzert_HESSOpinions_en.pdf) | 大样本训练的方法论共识。 |
| 3 | TS385 | [Global prediction of extreme floods in ungauged watersheds](../../pdfs/2023_Nearing_GlobalPredictionExtremeFloods_en.pdf) | 全球无资料流域洪水预警的标杆与常用对比对象。 |
| 4 | TS386 | [Hourly U.S.-wide flood simulation beyond the limits of traditional and data-driven models](../../pdfs/2026_Yang_HourlyUSWide_en.pdf) | 可微分模型在小时、河网尺度上对比 NWM 与 LSTM。 |
| 5 | TS388 | [RiverMamba: A State Space Model for Global River Discharge and Flood Forecasting](../../pdfs/2025_Eddin_RiverMamba_en.pdf) | 全球 0.05° 网格、利用河网空间关系的 7 天洪水预报。 |
| 6 | TS389 | [Probabilistic Diffusion Models Advance Extreme Flood Forecasting](../../pdfs/2024_Ou_ProbabilisticDiffusionModelsAdvance_en.pdf) | 扩散模型做极端洪水概率预报的代表。 |
| 7 | TS396 | [Towards a global spatial machine learning model for seasonal groundwater level predictions in Germany](../../pdfs/2024_Kunz_TowardsGlobalSpatialMachine_en.pdf) | 5,288 口井、12 周的全局地下水位预测。 |
| 8 | TS398 | [Deep learning for flash drought forecasting and interpretation](../../pdfs/2025_Zhao_DeepLearningFlashDrought_en.pdf) | 骤旱预警与可解释性。 |
| 9 | TS410 | [Ranked Right, Sized Wrong: Ensemble Spread Fails Silently at Streamflow Extremes](../../pdfs/2026_Gallant_RankedRightSizedWrong_en.pdf) | 深度学习集合不确定性在极端流量下的失效，直接关系预警可信度。 |
| 10 | TS390 | [Caravan MultiMet: Extending Caravan with Multiple Weather Nowcasts and Forecasts](../../pdfs/2024_Shalev_CaravanMultiMet_en.pdf) | （补位：原推荐条目未核验通过或不足 10 篇）评测“真实业务预报驱动”下水文预报的关键数据基础。 |

## 按子方向

### 全球日径流业务预报（再分析→业务预报迁移）
- TS383（高）[AIFL: A global daily streamflow forecasting model using deterministic an LSTM pre-trained on ERA5-Land and fine-tuned on IFS](../../pdfs/2026_Taccari_AIFL_en.pdf) — 预测；目标：日河流流量；方法：深度学习（LSTM，两阶段迁移学习）

### 降雨-径流 LSTM 训练范式（大样本 vs 单流域）
- TS384（高）[HESS Opinions: Never train a Long Short-Term Memory (LSTM) network on a single basin](../../pdfs/2024_Kratzert_HESSOpinions_en.pdf) — 预测；目标：日径流（降雨-径流模拟）；方法：深度学习（LSTM）

### 全球无资料流域极端洪水预报
- TS385【三年前】（高）[Global prediction of extreme floods in ungauged watersheds](../../pdfs/2023_Nearing_GlobalPredictionExtremeFloods_en.pdf) — 预警；目标：河流流量 / 极端洪水事件（重现期事件）；方法：深度学习（LSTM 类，待全文核实）

### 可微分物理嵌入模型（小时尺度全国洪水）
- TS386（高）[Hourly U.S.-wide flood simulation beyond the limits of traditional and data-driven models](../../pdfs/2026_Yang_HourlyUSWide_en.pdf) — 预测；目标：小时河道流量（80 万余河段）/ 洪峰；方法：物理-数据融合（可微分 HBV：dHBV2.0MTS-MC，多时间尺度+Muskingum-Cunge 汇流）

### 全球网格化河流流量与洪水预报（时空）
- TS388（高）[RiverMamba: A State Space Model for Global River Discharge and Flood Forecasting](../../pdfs/2025_Eddin_RiverMamba_en.pdf) — 预测；目标：全球 0.05° 网格河流流量与洪水（不同重现期）；方法：深度学习（Mamba 状态空间模型）

### 概率洪水预报（扩散生成模型）
- TS389（高）[Probabilistic Diffusion Models Advance Extreme Flood Forecasting](../../pdfs/2024_Ou_ProbabilisticDiffusionModelsAdvance_en.pdf) — 预测；目标：流域径流 / 极端洪峰（前 0.1% 流量）；方法：深度学习（扩散模型）

### 大样本数据集（含气象预报驱动）
- TS390（高）[Caravan MultiMet: Extending Caravan with Multiple Weather Nowcasts and Forecasts](../../pdfs/2024_Shalev_CaravanMultiMet_en.pdf) — 基准/数据集；目标：多流域径流预报所需的气象现报与预报驱动；方法：其他（数据集）

### 全球水文响应特征与趋势分析（物理嵌入学习）
- TS391（中）[Distinct hydrologic response patterns and trends worldwide revealed by physics-embedded learning](../../pdfs/2025_Ji_DistinctHydrologicResponsePatterns_en.pdf) — 预测；目标：日/月径流及水文特征（基流比例、绿水-蓝水分配）的时间变化；方法：物理-数据融合（物理嵌入、大数据训练的全球水模型）

### 大陆尺度中期多变量水文预报（网格）
- TS392（中）[Hapi: A Multivariable Land-Surface Transformer for Medium-Range Hydrological Forecasting at Continental Scale](../../pdfs/2026_Zhang_Hapi_en.pdf) — 预测；目标：河流流量、地表径流、雪水当量、土壤湿度指数（多变量）；方法：深度学习（U-Net Swin Transformer）

### 小时径流概率预测与数据同化
- TS393（高）[Diffusion-Based Probabilistic Modeling for Hourly Streamflow Prediction and Assimilation](../../pdfs/2025_Yang_DiffusionProbabilisticModelingHourly_en.pdf) — 预测；目标：小时流量过程线；方法：深度学习（去噪扩散概率模型 h-Diffusion）

### 可微分模型的数据同化
- TS394（中）[Update hydrological states or meteorological forcings? Comparing data assimilation methods for differentiable hydrologic models](../../pdfs/2025_Jamaat_UpdateHydrologicalStatesOr_en.pdf) — 预测；目标：日径流（1 天预见期）；方法：物理-数据融合（可微分模型 + 变分数据同化）

### 业务洪水预报误差校正
- TS395（中）[Long short-term memory networks for enhancing real-time flood forecasts: a case study for an underperforming hydrologic model](../../pdfs/2024_Gegenleithner_LongShortTermMemory_en.pdf) — 预测；目标：实时洪水预报径流（过程模型输出校正）；方法：混合（hindcast-forecast LSTM 误差校正；对比 ARIMA）

### 地下水位预测（全局多井模型）
- TS396（高）[Towards a global spatial machine learning model for seasonal groundwater level predictions in Germany](../../pdfs/2024_Kunz_TowardsGlobalSpatialMachine_en.pdf) — 预测；目标：地下水位；方法：深度学习（Temporal Fusion Transformer、N-HiTS）

### 地下水头时间序列建模竞赛（基准）
- TS397（高）[Data-driven modelling of hydraulic-head time series: results and lessons learned from the 2022 Groundwater Time Series Modelling Challenge](../../pdfs/2024_Collenteur_DataDrivenModellingHydraulic_en.pdf) — 基准/数据集；目标：地下水头（水位）；方法：统计 | 机器学习 | 深度学习（15 个团队：集总参数模型、ML、DL）

### 骤旱与土壤湿度预报
- TS398（高）[Deep learning for flash drought forecasting and interpretation](../../pdfs/2025_Zhao_DeepLearningFlashDrought_en.pdf) — 预警；目标：土壤湿度与骤旱发生；方法：深度学习（可解释 Transformer：IT-Drought）

### 概率干旱预报（欧洲）
- TS399（中）[Probabilistic Deep Learning for Drought Forecasting: Role of Internal Climate Variability](../../pdfs/2026_Funk_ProbabilisticDeepLearningDrought_en.pdf) — 预测；目标：干旱指标（具体指数待全文核实）；方法：深度学习（概率预报框架）

### 雪水当量（SWE）概率预报
- TS400（中）[ForeSWE: Forecasting Snow-Water Equivalent with an Uncertainty-Aware Attention Model](../../pdfs/2025_Thapa_ForeSWE_en.pdf) — 预测；目标：雪水当量 SWE；方法：混合（注意力深度学习 + 高斯过程不确定性量化）

### 多水库入流预报（时空图）
- TS401（中）[Adaptive Graph Learning with Transformer for Multi-Reservoir Inflow Prediction](../../pdfs/2025_Hu_AdaptiveGraphLearningTransformer_en.pdf) — 预测；目标：水库入流；方法：深度学习（自适应时变图 + Transformer：AdaTrip）

### 大样本数据集（全球）
- TS402【三年前】（中）[Caravan - A global community dataset for large-sample hydrology](../../pdfs/2023_Kratzert_CaravanGlobalCommunityDataset_en.pdf) — 基准/数据集；目标：多流域日径流及气象驱动、流域属性；方法：其他（数据集）

### 降雨-径流新架构（状态空间模型）
- TS403（中）[A Deep State Space Model for Rainfall-Runoff Simulations](../../pdfs/2025_Wang_DeepStateSpaceModel_en.pdf) — 预测；目标：日径流（降雨-径流模拟）；方法：深度学习（S4D-FT 状态空间模型）

### 降雨-径流新架构（TFT vs LSTM）
- TS404（中）[Efficacy of Temporal Fusion Transformers for Runoff Simulation](../../pdfs/2025_Koya_EfficacyTemporalFusionTransformers_en.pdf) — 预测；目标：日径流；方法：深度学习（Temporal Fusion Transformer，对比 LSTM）

### 通用时序模型/基础模型在水文中的基准
- TS405（中）[Deep Learning Foundation and Pattern Models: Challenges in Hydrological Time Series](../../pdfs/2024_He_DeepLearningFoundationPattern_en.pdf) — 基准/数据集；目标：降雨-径流等水文时间序列任务；方法：深度学习 | 基础模型（20 余种模式模型与基础模型比较）

### 水位预报（时间序列基础模型评测）
- TS406（中）[How Effective are Large Time Series Models in Hydrology? A Study on Water Level Forecasting in Everglades](../../pdfs/2025_Rangaraj_HowEffectiveLargeTime_en.pdf) — 预测；目标：湿地水位；方法：基础模型 | 深度学习（12 个任务专用模型 + 5 个时序基础模型）

### 河网拓扑与图神经网络洪水预报
- TS407（中）[Accelerating flood warnings by 10 hours: the power of river network topology in AI-enhanced flood forecasting](../../pdfs/2024_Wang_AcceleratingFloodWarnings10_en.pdf) — 预警；目标：河流流量 / 洪水（含罕见极端事件）；方法：深度学习（GNN，基于可达性的稠密图变换；对比 EA-LSTM）

### 河网拓扑与图神经网络洪水预报（负面结果）
- TS408（中）[The Merit of River Network Topology for Neural Flood Forecasting](../../pdfs/2024_Kirschstein_MeritRiverNetworkTopology_en.pdf) — 预测；目标：站点河流流量；方法：深度学习（GNN，比较多种邻接定义）

### 分布式 ML 模型的概率预报与不确定性
- TS409（中）[Joint distribution of upstream runoff governs downstream river-discharge prediction uncertainty in distributed ML models](../../pdfs/2026_Ruparell_JointDistributionUpstreamRunoff_en.pdf) — 预测；目标：下游河流流量的预测分布；方法：深度学习（概率 LSTM）+ 物理汇流

### 集合不确定性在极端流量下的校准评估
- TS410（中）[Ranked Right, Sized Wrong: Ensemble Spread Fails Silently at Streamflow Extremes](../../pdfs/2026_Gallant_RankedRightSizedWrong_en.pdf) — 预测；目标：径流预测误差与集合离散度；方法：深度学习（LSTM 集合）+ 不确定性评估

### 概念模型-深度学习混合与分位数不确定性
- TS411（低）[QDeepGR4J: Quantile-based ensemble of deep learning and GR4J hybrid rainfall-runoff models for extreme flow prediction with uncertainty quantification](../../pdfs/2025_Kapoor_QDeepGR4J_en.pdf) — 预测；目标：径流（多步）与极端流量；方法：物理-数据融合（GR4J + 深度学习路由替代 + 分位数回归集成）

### LSTM 峰值流量模拟与洪水频率分析
- TS412（中）[Exploring the ability of LSTM-based hydrological models to simulate streamflow time series for flood frequency analysis](../../pdfs/2024_Martel_ExploringAbilityLSTMHydrological_en.pdf) — 预测；目标：年最大流量 / 峰值流量序列；方法：深度学习 | 混合（LSTM、注意力、过采样、LSTM-水文模型混合）

### 质量守恒感知机（可解释物理-概念网络）
- TS413（低）[Towards Interpretable Physical-Conceptual Catchment-Scale Hydrological Modeling using the Mass-Conserving-Perceptron](../../pdfs/2024_Wang_TowardsInterpretablePhysicalConceptual_en.pdf) — 预测；目标：流域径流（高/中/低流量全过程）；方法：物理-数据融合（Mass-Conserving Perceptron 有向图结构）

### 概念水文模型的解析可微分标定
- TS414（低）[Reclaiming First Principles: A Differentiable Framework for Conceptual Hydrologic Models](../../pdfs/2026_Vrugt_ReclaimingFirstPrinciples_en.pdf) — 预测；目标：降雨-径流模型参数与径流模拟；方法：物理-数据融合（ODE 灵敏度方程得到解析梯度）

### 无资料流域预测（地球基础模型嵌入）
- TS415（中）[Utilizing Earth Foundation Models to Enhance the Simulation Performance of Hydrological Models with AlphaEarth Embeddings](../../pdfs/2026_Qu_UtilizingEarthFoundationModels_en.pdf) — 预测；目标：无资料流域径流；方法：深度学习 + 基础模型嵌入（AlphaEarth 卫星表征替代流域属性）

### 无资料流域径流预测（多模型集成 + 储备池计算）
- TS416（中）[Multi‐Model Ensemble and Reservoir Computing for River Discharge Prediction in Ungauged Basins](../../pdfs/2025_Funato_MultiModelEnsembleReservoir_en.pdf) — 预测；目标：日河流流量；方法：混合（贝叶斯模型平均 + 储备池计算误差校正）

### 全球模型本地微调（洪水预报）
- TS417（中）[Fine Flood Forecasts: Incorporating local data into global models through fine-tuning](../../pdfs/2025_Ryd_FineFloodForecasts_en.pdf) — 预测；目标：流域径流 / 洪水预报；方法：深度学习（预训练-微调）

### 非洲缺资料跨境流域径流预报
- TS418（低）[Towards Operational Streamflow Forecasting in the Limpopo River Basin using Long Short-Term Memory Networks](../../pdfs/2026_Tlhomole_TowardsOperationalStreamflowForecasting_en.pdf) — 预测；目标：河流流量；方法：深度学习（LSTM）

### 因果时空表示学习（多站径流）
- TS419（低）[CauSTream: Causal Spatio-Temporal Representation Learning for Streamflow Forecasting](../../pdfs/2025_Wan_CauSTream_en.pdf) — 预测；目标：多站点径流；方法：深度学习（因果图学习 + 时空网络）

### 雷达降水驱动的短时河流水位预报
- TS420（中）[R2RNet: A deep spatiotemporal RaintoRiverNetwork for water level prediction and flood forecasting](../../pdfs/2025_Dhankhar_R2RNet_en.pdf) — 预测；目标：河流水位；方法：深度学习（(2+1)D CNN + LSTM，残差校正：R2RNet）

### 预报驱动的防洪调度（闸泵水库预泄）
- TS421（中）[FIDLAR: Forecast-Informed Deep Learning Architecture for Flood Mitigation](../../pdfs/2024_Shi_FIDLAR_en.pdf) — 预测；目标：沿海河流系统水位与预泄调度；方法：深度学习（Flood Manager + 预报模块联合）

### 时空地下水位预测（纯 DL 与物理引导）
- TS422（中）[Pure and physics-guided deep learning approaches for spatio-temporal groundwater level prediction](../../pdfs/2026_Salis_PurePhysicsGuidedDeep_en.pdf) — 预测；目标：周地下水位；方法：深度学习 | 物理-数据融合（注意力模型 STAINet 及物理引导变体）

### 融雪主导流域季节径流概率预报
- TS423（低）[Probabilistic Seasonal Streamflow Forecasting Across California's Sierra Nevada Watersheds with Agentic AI](../../pdfs/2026_LopezGomez_ProbabilisticSeasonalStreamflowForecasti_en.pdf) — 预测；目标：春夏季融雪径流量（季节尺度）；方法：其他（LLM 代理 + 自动代码变异搜索模型架构）

### 大样本数据集（CAMELS 系列）
- TS424（中）[CAMELS-DE: hydro-meteorological time series and attributes for 1582 catchments in Germany](../../pdfs/2024_Loritz_CAMELSDE_en.pdf) — 基准/数据集；目标：多流域径流与水文气象时间序列；方法：其他（数据集）

### 积雪（雪深/SWE）物理约束神经微分方程
- TS425（中）[A Physics-Constrained Neural Differential Equation Framework for Data-Driven Snowpack Simulation](../../pdfs/2024_Charbonneau_PhysicsConstrainedNeuralDifferential_en.pdf) — 预测；目标：日雪深与雪水当量；方法：物理-数据融合（物理约束神经微分方程参数化）

### 径流观测质量控制（异常检测与重建）
- TS426（低）[HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control](../../pdfs/2025_Haq_HydroGEM_en.pdf) — 异常检测；目标：流量观测异常（检测与重建）；方法：基础模型（自监督 TCN-Transformer，14.2M 参数）

### 陆地水储量预测（统计基准）
- TS427（中）[Rethinking deep learning: linear regression remains a key benchmark in predicting terrestrial water storage](../../pdfs/2025_Nie_RethinkingDeepLearning_en.pdf) — 预测；目标：陆地水储量 TWS；方法：统计 | 深度学习（线性回归 vs LSTM vs TFT）

### 地下水位统计时间序列建模
- TS428（低）[The Whittle likelihood for mixed models with application to groundwater level time series](../../pdfs/2025_Pypkowski_WhittleLikelihoodMixedModels_en.pdf) — 预测；目标：地下水位；方法：统计（混合模型 + 频域 Whittle 似然）

### 地球科学基础模型（径流、土壤湿度）
- TS429（中）[StefaLand: An Efficient Geoscience Foundation Model That Improves Dynamic Land-Surface Predictions](../../pdfs/2025_Kraabel_StefaLand_en.pdf) — 预测；目标：径流、土壤湿度等陆面动态变量；方法：基础模型（位置感知掩码自编码器 + 残差微调适配器）

### 非洲次季节-季节干旱/骤旱预测
- TS430（低）[Prediction of Drought and Flash Drought in Africa at the Seasonal-to-Subseasonal Scale using the Community Research Earth Digital Intelligence Twin Framework](../../pdfs/2026_Edris_PredictionDroughtFlashDrought_en.pdf) — 预警；目标：干旱与骤旱；方法：深度学习（CrossFormer，基于 NCAR CREDIT 框架：DroughtFormer）

### 可微分参数学习（方法基础）
- TS431【三年前】（低）[From calibration to parameter learning: Harnessing the scaling effects of big data in geoscientific modeling](../../pdfs/2020_Tsai_CalibrationParameterLearningHarnessing_en.pdf) — 预测；目标：水文/陆面模型参数及其模拟变量；方法：物理-数据融合（可微分参数学习 dPL）

### 区域 LSTM 降雨-径流（经典基线）
- TS432【三年前】（低）[Towards learning universal, regional, and local hydrological behaviors via machine learning applied to large-sample datasets](../../pdfs/2019_Kratzert_TowardsLearningUniversalRegional_en.pdf) — 预测；目标：日径流；方法：深度学习（EA-LSTM）

### 概率径流预报（扩散 + 状态空间骨干）
- TS433（低）[HydroDiffusion: Diffusion-Based Probabilistic Streamflow Forecasting with a State Space Backbone](../../pdfs/2025_Wang_HydroDiffusion_en.pdf) — 预测；目标：多日径流轨迹；方法：深度学习（扩散模型 + 仅解码器状态空间模型）

