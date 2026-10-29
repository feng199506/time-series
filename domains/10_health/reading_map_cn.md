# 医疗与公共卫生：阅读路线图

进度：已核验全文 50 / 目标约 50；待核验 2；下载失败 5。 近三年（已核验文献中）48 篇，占 0.96。
编号对应 [catalog_cn.csv](catalog_cn.csv)；简介与字段均依据摘要，未读全文。

## 优先阅读 10 篇

| 顺序 | 编号 | 标题 | 理由 |
|---|---|---|---|
| 1 | TS318 | [Evaluation of FluSight influenza forecasting in the 2021–22 and 2022–23 seasons with a new target laboratory-confirmed influenza hospitalizations](../../pdfs/2024_Mathis_EvaluationFluSightInfluenzaForecasting_en.pdf) | 流感住院新目标下集合预报的权威前瞻评测，WIS/覆盖率评估范式。 |
| 2 | TS319 | [GlucoBench: Curated List of Continuous Glucose Monitoring Datasets with Prediction Benchmarks](../../pdfs/2024_Sergazinov_GlucoBench_en.pdf) | CGM 血糖预测的标准化数据集与基准。 |
| 3 | TS320 | [Learning the natural history of human disease with generative transformers](../../pdfs/2025_Shmatko_LearningNaturalHistoryHuman_en.pdf) | 纵向 EHR 疾病进展生成式预测，有跨国外部验证。 |
| 4 | TS322 | [Are Time Series Foundation Models Ready for Vital Sign Forecasting in Healthcare?](../../pdfs/2025_Gu_TimeSeriesFoundationModels_en.pdf) | 对 TSFM 用于生命体征预测给出审慎证据。 |
| 5 | TS323 | [Deep learning models for acute kidney injury prediction: multi-center external validation and evaluation under simulated continuous monitoring conditions](../../pdfs/2026_Lee_DeepLearningModelsAcute_en.pdf) | 揭示单点 AUROC 与连续部署表现的背离。 |
| 6 | TS327 | [Generative diffusion models for spatiotemporal influenza forecasting](../../pdfs/2026_Lemaitre_GenerativeDiffusionModelsSpatiotemporal_en.pdf) | 扩散模型做时空流行病预测，有实时检验。 |
| 7 | TS329 | [Mantis: A foundation model for mechanistic disease forecasting](../../pdfs/2025_Dudley_Mantis_en.pdf) | 仅用机理模拟预训练的传染病预测基础模型，以 Forecast Hub 为对照。 |
| 8 | TS331 | [Stable Prediction of Adverse Events in Medical Time-Series Data](../../pdfs/2025_Keoliya_StablePredictionAdverseEvents_en.pdf) | 把风险轨迹稳定性纳入预警评测。 |
| 9 | TS334 | [Evaluating infectious disease forecasts with allocation scoring rules](../../pdfs/2023_Gerding_EvaluatingInfectiousDiseaseForecasts_en.pdf) | 评测与资源分配决策挂钩。 |
| 10 | TS337 | [Rethinking respiratory disease forecasting: temporal heterogeneity between surveillance predictors and outcomes drives forecast instability](../../pdfs/2026_Topazian_RethinkingRespiratoryDiseaseForecasting_en.pdf) | 监测预测因子与结局关系的非平稳性导致预测不稳定。 |

## 按子方向

### 传染病预测中心评测（流感住院）
- TS318（高）[Evaluation of FluSight influenza forecasting in the 2021–22 and 2022–23 seasons with a new target laboratory-confirmed influenza hospitalizations](../../pdfs/2024_Mathis_EvaluationFluSightInfluenzaForecasting_en.pdf) — 预测；目标：美国国家及各辖区每周实验室确诊流感住院人数（1–4 周前瞻概率预测）；方法：其他（多团队模型 + 集合预报评测：统计/机理/机器学习）

### 血糖/CGM 预测基准
- TS319（高）[GlucoBench: Curated List of Continuous Glucose Monitoring Datasets with Prediction Benchmarks](../../pdfs/2024_Sergazinov_GlucoBench_en.pdf) — 基准/数据集；目标：CGM 血糖轨迹（未来血糖值）；方法：其他（基准：多种统计/机器学习/深度学习基线）

### 疾病进展建模（纵向 EHR 生成式轨迹）
- TS320（高）[Learning the natural history of human disease with generative transformers](../../pdfs/2025_Shmatko_LearningNaturalHistoryHuman_en.pdf) — 预测；目标：个体未来 1000 多种 ICD-10 疾病及死亡的发生率与未来健康轨迹（最长 20 年）；方法：深度学习（改造 GPT 的生成式 Transformer，Delphi-2M）

### 流感住院预测（多数据源 + 机器学习集合）
- TS321（高）[Flusion: Integrating multiple data sources for accurate influenza predictions](../../pdfs/2024_Ray_Flusion_en.pdf) — 预测；目标：美国 NHSN 流感住院人数（FluSight 目标）；方法：混合（梯度提升等两种机器学习模型 + 统计模型的集合）

### 时间序列基础模型用于生命体征预测（评测）
- TS322（高）[Are Time Series Foundation Models Ready for Vital Sign Forecasting in Healthcare?](../../pdfs/2025_Gu_TimeSeriesFoundationModels_en.pdf) — 预测；目标：患者连续记录的生命体征（面向恶化预测）；方法：基础模型（多种 TSFM 设置与配置；对照传统预测模型）

### 急性肾损伤（AKI）早期预警与部署式评测
- TS323（高）[Deep learning models for acute kidney injury prediction: multi-center external validation and evaluation under simulated continuous monitoring conditions](../../pdfs/2026_Lee_DeepLearningModelsAcute_en.pdf) — 预警；目标：住院患者 AKI 发生风险（0、48、72 小时前瞻）；方法：深度学习（LSTM-Attention、Masked CNN、ITE-Transformer；对照 XGBoost、逻辑回归）

### 登革热概率预测挑战与集合
- TS324（高）[Leveraging probabilistic forecasts for dengue preparedness and control: The 2024 Dengue Forecasting Sprint in Brazil](../../pdfs/2026_Araujo_LeveragingProbabilisticForecastsDengue_en.pdf) — 预测；目标：巴西五个州 2024、2025 季登革热病例数（概率预测）；方法：其他（六个国际团队的机器学习与经典统计模型 + 集合）

### 可穿戴生理信号基础模型（插补/外推）
- TS325（高）[Scaling Wearable Foundation Models](../../pdfs/2024_Narayanswamy_ScalingWearableFoundationModels_en.pdf) — 预测；目标：每分钟心率、HRV、皮电、加速度、皮温、高度计等信号的插补、内插与外推（时间与模态）；方法：基础模型（多模态生成式预训练 LSM，研究扩展律）

### 血糖/CGM 基础模型
- TS326（高）[A Large Sensor Foundation Model Pretrained on Continuous Glucose Monitor Data for Diabetes Management](../../pdfs/2024_Luo_LargeSensorFoundationModel_en.pdf) — 预测；目标：未来 2 小时内 CGM 血糖读数；方法：基础模型（Transformer 解码器自回归 Large Sensor Model，CGM-LSM）

### 流感时空预测（扩散生成模型）
- TS327（高）[Generative diffusion models for spatiotemporal influenza forecasting](../../pdfs/2026_Lemaitre_GenerativeDiffusionModelsSpatiotemporal_en.pdf) — 预测；目标：美国流感发病（FluSight 目标）的时空概率预测；方法：深度学习（去噪扩散概率模型，条件生成/图像修补）

### ICU 生命体征多变量轨迹预测
- TS328（高）[TFT-multi: simultaneous forecasting of vital sign trajectories in the ICU](../../pdfs/2024_He_TFTMulti_en.pdf) — 预测；目标：ICU 中血压、脉搏、SpO2、体温、呼吸频率五项生命体征轨迹；方法：深度学习（扩展 Temporal Fusion Transformer，联合多目标）

### 传染病预测基础模型（机理模拟预训练）
- TS329（高）[Mantis: A foundation model for mechanistic disease forecasting](../../pdfs/2025_Dudley_Mantis_en.pdf) — 预测；目标：多种疾病、地区与结局指标的发病/住院/死亡等；方法：基础模型（基于机理模拟数据预训练）

### 报告延迟下的即时预测（nowcasting）与集合
- TS330（高）[Post-processing and weighted combination of infectious disease nowcasts](../../pdfs/2024_Amaral_PostProcessingWeightedCombination_en.pdf) — 预测；目标：德国 COVID-19 住院发生数的概率即时预测（校正报告延迟）；方法：统计（概率 nowcast 后处理 + 加权集合）

### 早期事件预测评测（风险轨迹稳定性）
- TS331（高）[Stable Prediction of Adverse Events in Medical Time-Series Data](../../pdfs/2025_Keoliya_StablePredictionAdverseEvents_en.pdf) — 基准/数据集；目标：脓毒症发生等六类不良事件的连续风险轨迹；方法：其他（基准：经典学习器、深度序列模型、零样本 LLM）

### 预测评测（决策导向评分规则）
- TS334（高）[Evaluating infectious disease forecasts with allocation scoring rules](../../pdfs/2023_Gerding_EvaluatingInfectiousDiseaseForecasts_en.pdf) — 预测；目标：美国各地区 COVID-19 住院概率预测的评分；方法：统计（分配评分规则：按预测分配医疗资源以最小化未满足需求）

### 医疗时间序列基础模型（不规则采样）
- TS335（高）[MIRA: Medical Time Series Foundation Model for Real-World Health Data](../../pdfs/2025_Li_MIRA_en.pdf) — 预测；目标：医疗时间序列在任意时间点的未来值；方法：基础模型（连续时间旋转位置编码 + 频率专家混合 + Neural ODE 外推）

### 医院床位占用预测（病房/ICU）
- TS336（中）[A modular approach to forecasting COVID-19 hospital bed occupancy](../../pdfs/2025_Tobin_ModularApproachForecastingCOVID_en.pdf) — 预测；目标：澳大利亚各州/领地 COVID-19 病房与 ICU 床位占用数（21 天）；方法：混合（随机病人流转模拟 + 近似贝叶斯拟合，输入外部病例预测）

### 评测与非平稳性（呼吸道疾病预测不稳定）
- TS337（高）[Rethinking respiratory disease forecasting: temporal heterogeneity between surveillance predictors and outcomes drives forecast instability](../../pdfs/2026_Topazian_RethinkingRespiratoryDiseaseForecasting_en.pdf) — 预测；目标：犹他州 SARS-CoV-2 与流感住院人数；方法：统计/机器学习（具体模型待全文核实）

### 传染病预测中心评测（流感 ILI/住院十年回顾）
- TS338（高）[A Decade of CDC FluSight Influenza Forecasting](../../pdfs/2026_Hines_DecadeCDCFluSightInfluenza_en.pdf) — 预测；目标：流感样病例（ILI）比例（2014/15–2019/20）与流感住院人数（2021/22–2024/25）；方法：其他（跨模型类型比较：统计、机理、机器学习、混合）

### 脓毒症早期预警（外部验证/可迁移性）
- TS339（中）[Evaluating sepsis watch generalizability through multisite external validation of a sepsis machine learning model](../../pdfs/2025_Valan_EvaluatingSepsisWatchGeneralizability_en.pdf) — 预警；目标：急诊就诊中的脓毒症早期识别（风险评分）；方法：机器学习（Duke Sepsis Watch 模型，静态+动态患者数据）

### EHR 健康轨迹生成式预测（零样本）
- TS340（中）[Zero shot health trajectory prediction using transformer](../../pdfs/2024_Renc_ZeroShotHealthTrajectory_en.pdf) — 预测；目标：患者未来健康事件轨迹（tokenized Patient Health Timelines）；方法：基础模型（Transformer，ETHOS，零样本）

### 流行病时间序列预训练（仓室原型）
- TS341（中）[Pre-training Epidemic Time Series Forecasters with Compartmental Prototypes](../../pdfs/2025_Liu_PreTrainingEpidemicTime_en.pdf) — 预测；目标：多种疾病感染时间序列；方法：基础模型（仓室原型字典 + 下一 token 预测预训练 + 流行病学正则）

### 流行病多变量预测基准
- TS342（中）[EpiCastBench: Datasets and Benchmarks for Multivariate Epidemic Forecasting](../../pdfs/2026_Panja_EpiCastBench_en.pdf) — 基准/数据集；目标：多种传染病多变量（相关）时间序列；方法：其他（基准：多种单变量/多变量预测模型）

### 传染病预测中心（意大利 ILI）
- TS343（中）[Collaborative forecasting of influenza-like illness in Italy: The Influcast experience](../../pdfs/2024_Fiandrino_CollaborativeForecastingInfluenzaLike_en.pdf) — 预测；目标：意大利国家与大区流感样病例（ILI）发病率（最多 4 周前瞻）；方法：其他（多模型集合 vs 基线）

### 血糖预测（生理模型约束神经网络）
- TS344（中）[PMB-NN: Physiological-Model-Based Neural Network for Glucose Forecasting in Type 1 Diabetes](../../pdfs/2026_Zhang_PMBNN_en.pdf) — 预测；目标：1 型糖尿病患者 CGM 血糖；方法：物理-数据融合（TCN + 个体化四参数生理模型约束）

### 急诊就诊量概率预测（预测组合）
- TS345（中）[Ascertaining cause-specific emergency department demand using forecast combinations](../../pdfs/2025_Guo_AscertainingCauseSpecificEmergency_en.pdf) — 预测；目标：新加坡按病因分类的急诊就诊数（概率预测）；方法：统计/机器学习（线性/非线性、静态/动态权重的概率预测组合）

### 术中低血压实时预警（生命体征序列）
- TS346（中）[Transformer-based deep learning model for real-time prediction of intraoperative hypotension using dynamic time-series vital signs: A retrospective study](../../pdfs/2026_Zhu_TransformerDeepLearningModel_en.pdf) — 预警；目标：术中低血压（IOH）发生风险（5/10/15 分钟前瞻）；方法：深度学习（Transformer；对照 XGBoost）

### 报告延迟即时预测基线方法
- TS347（中）[Baseline nowcasting methods for handling delays in epidemiological data](../../pdfs/2025_Johnson_BaselineNowcastingMethodsHandling_en.pdf) — 预测；目标：受报告延迟影响的近期病例数（德国 COVID-19 住院、英国诺如病毒监测）；方法：统计（基线 nowcasting 方法族 + R 包 baselinenowcast）

### 污水监测信号用于住院负担预测
- TS348（中）[EpiFlow: A framework for improving the utility of wastewater signals for disease forecasting](../../pdfs/2026_Adiga_EpiFlow_en.pdf) — 预测；目标：医院负担指标（住院等）的实时预测；方法：统计/机器学习（熵可预测性分析 + 因果检验 + 时变关系预测模型）

### 不规则采样临床时间序列（神经 SDE）
- TS349（中）[Trajectory Flow Matching with Applications to Clinical Time Series Modeling](../../pdfs/2024_Zhang_TrajectoryFlowMatchingApplications_en.pdf) — 预测；目标：临床时间序列未来轨迹及不确定性；方法：深度学习（Trajectory Flow Matching 训练 Neural SDE，免模拟）

### 医疗时间序列预训练与长期预测
- TS350（中）[TimelyGPT: Extrapolatable Transformer Pre-training for Long-term Time-Series Forecasting in Healthcare](../../pdfs/2023_Song_TimelyGPT_en.pdf) — 预测；目标：连续生物信号与不规则采样序列的长期外推；方法：基础模型（xPos 可外推位置编码 + 循环注意力 + 时间卷积）

### 心率变异性（HRV）预测（基础模型零样本）
- TS351（中）[Zero-Shot Heart Rate Variability Forecasting from Consumer Wearables Using Time Series Foundation Models](../../pdfs/2026_Perakyla_ZeroShotHeartRate_en.pdf) — 预测；目标：短期 HRV；方法：基础模型（TimesFM、Chronos、MOIRAI 零样本；对照均值、指数平滑、EWMA）

### 房颤发作短期预警（可穿戴 ECG）
- TS352（中）[Personalized deep learning for short-term forecasting of impending atrial fibrillation from continuous wearable ECG signals](../../pdfs/2026_Suh_PersonalizedDeepLearningShort_en.pdf) — 预警；目标：5 分钟内即将发生的房颤；方法：深度学习（全局模型 + 个体微调）

### 血压时间序列预测（个性化）
- TS353（中）[A Multi-scenario Attention-based Generative Model for Personalized Blood Pressure Time Series Forecasting](../../pdfs/2024_Wan_MultiScenarioAttentionGenerative_en.pdf) — 预测；目标：个体连续血压；方法：深度学习（注意力生成模型 + 2D 表示学习）

### 脓毒症早期预测（临床计算器 + 时间图）
- TS354（中）[SepsisCalc: Integrating Clinical Calculators into Early Sepsis Prediction via Dynamic Temporal Graph Construction](../../pdfs/2024_Yin_SepsisCalc_en.pdf) — 预警；目标：脓毒症风险与器官功能障碍评分；方法：深度学习（动态时间图 + 估计 SOFA 等临床计算器）

### 脓毒症轨迹基准（ICU）
- TS355（中）[MIMIC-Sepsis: A Curated Benchmark for Modeling and Learning from Sepsis Trajectories in the ICU](../../pdfs/2025_Huang_MIMICSepsis_en.pdf) — 基准/数据集；目标：早期死亡、住院时长、休克发生（基准任务）；方法：其他（基准：含 Transformer 等序列模型）

### 住院患者恶化早期预警（部署）
- TS356（中）[Early Warning Index for Patient Deteriorations in Hospitals](../../pdfs/2025_Bertsimas_EarlyWarningIndexPatient_en.pdf) — 预警；目标：ICU 转入、急救小组出动与死亡的综合风险；方法：机器学习（多模态 + SHAP 解释 + 临床人员参与设定阈值）

### 纵向 EHR 化验指标预测
- TS357（中）[Forecasting laboratory measurements from longitudinal electronic health records](../../pdfs/2026_Firoozbakht_ForecastingLaboratoryMeasurementsLongitu_en.pdf) — 预测；目标：患者下一次就诊时的实验室检测值（如 INR、aPTT 等）；方法：深度学习（Transformer，LaBERT）

### 阿尔茨海默病进展预测（纵向多模态）
- TS358（中）[Physics-Informed Neural Koopman Machine for Interpretable Longitudinal Personalized Alzheimer's Disease Forecasting](../../pdfs/2025_Hrusanov_PhysicsInformedNeuralKoopman_en.pdf) — 预测；目标：多项认知评分的个体纵向轨迹；方法：物理-数据融合（Neural Koopman Machine + 分组层级注意力）

### 流感预测（物理信息神经网络）
- TS359（中）[Forecasting seasonal influenza epidemics with physics-informed neural networks](../../pdfs/2025_Rama_ForecastingSeasonalInfluenzaEpidemics_en.pdf) — 预测；目标：意大利全国流感发病（短期与长期概率预测）；方法：物理-数据融合（SIR 结构嵌入神经网络 SIR-INN + MCMC 推断参数）

### 多病原体合并住院负担预测
- TS362（中）[Beyond Single-Pathogen Forecasts: Predicting Shared Respiratory Hospital Burden from Influenza, COVID-19, and RSV](../../pdfs/2026_Saha_BeyondSinglePathogenForecasts_en.pdf) — 预测；目标：流感、COVID-19、RSV 合计每周住院人数（1–4 周）；方法：机器学习（监督学习框架，比较“分病原体求和”与“直接预测合计”两种策略）

### 血糖/CGM 预测（时间序列基础模型评测）
- TS363（中）[Evaluating Time-Series Foundation Models and Multimodal Dietary Context for CGM Forecasting](../../pdfs/2026_Zhang_EvaluatingTimeSeriesFoundation_en.pdf) — 预测；目标：短期 CGM 血糖；方法：基础模型（Chronos-Bolt 等零样本/微调；对照 Elastic Net、PatchTST）

### 疟疾病例预测（气候驱动）
- TS364（低）[Forecasting malaria cases using climate variability in Sierra Leone](../../pdfs/2025_Jalloh_ForecastingMalariaCasesClimate_en.pdf) — 预测；目标：塞拉利昂疟疾病例数；方法：统计/机器学习（SARIMA、SARIMAX、人工神经网络）

### 手足口病概率预测
- TS365（低）[Probabilistic forecasting of hand, foot and mouth disease in Mainland China using Bayesian additive regression tree model](../../pdfs/2025_Geng_ProbabilisticForecastingHandFoot_en.pdf) — 预测；目标：中国大陆七个地区每月手足口病病例数（点预测与预测区间）；方法：机器学习（贝叶斯加性回归树 BART；对照 ARIMA）

### 预测评测方法（区间/分位数预测评分）
- TS366【三年前】（高）[Evaluating epidemic forecasts in an interval format](../../pdfs/2020_Bracher_EvaluatingEpidemicForecastsInterval_en.pdf) — 预测；目标：以区间/分位数形式发布的病例、住院、死亡预测的评分；方法：统计（适当评分规则：WIS 近似 CRPS）

### ICU 临床预测基准（可复现性）
- TS367【三年前】（中）[Yet Another ICU Benchmark: A Flexible Multi-Center Framework for Clinical ML](../../pdfs/2023_Water_YetAnotherICUBenchmark_en.pdf) — 基准/数据集；目标：ICU 预测任务（如并发症早期检测等，具体任务待全文核实）；方法：其他（基准框架：多种 ML 与深度模型）

### 登革热发病率预测（时空集合）
- TS369（低）[A reproducible ensemble machine learning approach to forecast dengue outbreaks](../../pdfs/2024_Sebastianelli_ReproducibleEnsembleMachineLearning_en.pdf) — 预测；目标：巴西 19 岁以下人群州级登革热发病率（提前 1 个月）；方法：机器学习（集合模型）

### 污水监测驱动的住院预测
- TS370（低）[Wastewater as an early indicator for short-term forecasting COVID-19 hospitalization in Germany](../../pdfs/2024_Radermacher_WastewaterEarlyIndicatorShort_en.pdf) — 预测；目标：德国全国及各联邦州 COVID-19 住院率（短期）；方法：机器学习/统计（随机森林、XGBoost、ARIMA、线性与岭回归）

### 应急供水家庭端余氯概率预测
- TS163（低）[Training for the test: Using multi-objective training to improve ANN ensemble forecasts of household residual chlorine in emergencies](../../pdfs/2025_Santi_TrainingTestMultiObjective_en.pdf) — 预测；目标：配送后（家庭储存）游离余氯；方法：机器学习（ANN 集合预测系统 + 多目标训练）

### AI 天气模型极端事件检验
- TS289（中）[Validating Deep Learning Weather Forecast Models on Recent High-Impact Extreme Events](../../pdfs/2024_Pasche_ValidatingDeepLearningWeather_en.pdf) — 预测；目标：极端热浪、湿热浪与冬季风暴个例的预报误差；方法：其他（比较评估）

