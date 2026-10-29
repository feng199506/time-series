# 金融：阅读路线图

进度：已核验全文 55 / 目标约 50；待核验 2；下载失败 0。 近三年（已核验文献中）53 篇，占 0.964。
编号对应 [catalog_cn.csv](catalog_cn.csv)；简介与字段均依据摘要，未读全文。

## 优先阅读 10 篇

| 顺序 | 编号 | 标题 | 理由 |
|---|---|---|---|
| 1 | TS513 | [HARd to Beat: The Overlooked Impact of Rolling Windows in the Era of Machine Learning](../../pdfs/2024_Audrino_HARdToBeat_en.pdf) | HAR 拟合方案设定合理时，ML 无法胜出，是检验基准公平性的范例。 |
| 2 | TS514 | [Forecasting Realized Volatility with Time Series Foundation Models: A Comparison with Econometric Benchmarks](../../pdfs/2026_Brini_ForecastingRealizedVolatilityTime_en.pdf) | 用 MCS 和 MZ 回归拆解 TSFM 的“优势”来自哪里。 |
| 3 | TS515 | [How do standard time series forecasting benchmarks translate to finance? A broad study of risk adjusted performance](../../pdfs/2026_SalyKaufmann_HowDoStandardTime_en.pdf) | 通用 SOTA 架构不如 AR(1)，说明通用基准的排名不能迁移到金融。 |
| 4 | TS517 | [The Memorization Problem: Can We Trust LLMs' Economic Forecasts?](../../pdfs/2025_LopezLira_TheMemorizationProblem_en.pdf) | LLM 在训练覆盖期内的预测不可识别。 |
| 5 | TS518 | [Detecting Lookahead Bias in LLM Forecasts](../../pdfs/2025_Gao_DetectingLookaheadBiasLLM_en.pdf) | 提出可操作的前视偏差检验（LAP）。 |
| 6 | TS519 | [FinVerse: Toward More Realistic Evaluation for Financial Time-Series Forecasting](../../pdfs/2026_Lee_FinVerse_en.pdf) | 金融专用的 TSFM 基准，与 GIFT-Eval 的排名只中等相关。 |
| 7 | TS524 | [Evaluating financial tail risk forecasts: Testing Equal Predictive Ability](../../pdfs/2025_Bauer_EvaluatingFinancialTailRisk_en.pdf) | DM/MCS 在 VaR/ES 上检验力不足。 |
| 8 | TS525 | [TLOB: A Novel Transformer Model with Dual Attention for Price Trend Prediction with Limit Order Book Data](../../pdfs/2025_Berti_TLOB_en.pdf) | LOB 预测的最新代表，讨论可预测性衰减和价差成本。 |
| 9 | TS523 | [Combining a Large Pool of Forecasts of Value-at-Risk and Expected Shortfall](../../pdfs/2025_Taylor_CombiningLargePoolForecasts_en.pdf) | 尾部风险预测组合的系统研究。 |
| 10 | TS520 | [Kronos: A Foundation Model for the Language of Financial Markets](../../pdfs/2025_Shi_Kronos_en.pdf) | （补位：原推荐条目未核验通过或不足 10 篇）近期影响较大的金融专用基础模型，可与 rank4/9 的批判性结果对照阅读。 |

## 按子方向

### 已实现波动率（HAR vs 机器学习）
- TS513（高）[HARd to Beat: The Overlooked Impact of Rolling Windows in the Era of Machine Learning](../../pdfs/2024_Audrino_HARdToBeat_en.pdf) — 预测；目标：个股日度已实现波动率（RV）；方法：统计 vs 机器学习（HAR 对比多种 ML）
- TS562【三年前】（中）[A Machine Learning Approach to Volatility Forecasting](../../pdfs/2022_Christensen_MachineLearningApproachVolatility_en.pdf) — 预测；目标：道琼斯成分股已实现方差；方法：机器学习 vs 统计（正则化、回归树、神经网络 vs HAR）

### 已实现波动率 / 时间序列基础模型
- TS514（高）[Forecasting Realized Volatility with Time Series Foundation Models: A Comparison with Econometric Benchmarks](../../pdfs/2026_Brini_ForecastingRealizedVolatilityTime_en.pdf) — 预测；目标：已实现波动率（多资产，三个预测跨度）；方法：基础模型 vs 统计（9 个零样本 TSFM 对比 8 个 HAR 类计量模型）

### 收益率预测 / 深度架构基准
- TS515（高）[How do standard time series forecasting benchmarks translate to finance? A broad study of risk adjusted performance](../../pdfs/2026_SalyKaufmann_HowDoStandardTime_en.pdf) — 基准/数据集；目标：期货日收益（以波动率目标化 Sharpe 比为端到端优化目标）；方法：深度学习（16 种架构：Transformer、SSM、xLSTM、循环混合模型）

### LLM 预测批判 / 记忆与前视偏差
- TS517（高）[The Memorization Problem: Can We Trust LLMs' Economic Forecasts?](../../pdfs/2025_LopezLira_TheMemorizationProblem_en.pdf) — 预测；目标：LLM 对经济与金融变量（数值）的回忆/预测能力；方法：基础模型（大语言模型）

### LLM 预测批判 / 前视偏差检验
- TS518（高）[Detecting Lookahead Bias in LLM Forecasts](../../pdfs/2025_Gao_DetectingLookaheadBiasLLM_en.pdf) — 预测；目标：LLM 生成的股票收益预测（新闻标题）与资本支出预测（电话会文本）；方法：统计检验 + 大语言模型

### 金融基础模型评测基准
- TS519（高）[FinVerse: Toward More Realistic Evaluation for Financial Time-Series Forecasting](../../pdfs/2026_Lee_FinVerse_en.pdf) — 基准/数据集；目标：多类金融序列的点预测、横截面排序与组合结果；方法：基础模型（43 个公开 TSFM 评测）

### 金融基础模型（K 线）
- TS520（高）[Kronos: A Foundation Model for the Language of Financial Markets](../../pdfs/2025_Shi_Kronos_en.pdf) — 预测；目标：K 线价格序列（RankIC 评价）与波动率；以及合成 K 线生成；方法：基础模型（专用 tokenizer + 自回归预训练 Transformer）

### 收益率预测 / 时间序列基础模型
- TS521（高）[Pretrained Time-Series Foundation Models for Financial Return Forecasting](../../pdfs/2026_Alonso_PretrainedTimeSeriesFoundation_en.pdf) — 预测；目标：5 只美股（AAPL、AMZN、GOOG、JPM、META）的线性与对数收益；方法：基础模型（TimeGPT、TimesFM-2.5、Moirai-2.0、Chronos/Chronos-2）vs 深度学习（NBEATS、NHITS、PatchTST、iTransformer、KAN）

### 波动率（GARCH 与神经网络融合）
- TS522（高）[From GARCH to Neural Network for Volatility Forecast](../../pdfs/2024_Zhao_GARCHNeuralNetworkVolatility_en.pdf) — 预测；目标：金融资产波动率；方法：混合（GARCH-NN，GARCH-LSTM）

### 尾部风险（VaR/ES 预测组合）
- TS523（高）[Combining a Large Pool of Forecasts of Value-at-Risk and Expected Shortfall](../../pdfs/2025_Taylor_CombiningLargePoolForecasts_en.pdf) — 预测；目标：VaR 与 ES；方法：统计（预测组合：中位数、众数、截尾均值、正则化加权、混合分布）

### 尾部风险预测评价方法
- TS524（高）[Evaluating financial tail risk forecasts: Testing Equal Predictive Ability](../../pdfs/2025_Bauer_EvaluatingFinancialTailRisk_en.pdf) — 预测；目标：VaR/ES 预测的等预测能力检验（DM、MCS）；方法：统计（检验有限样本性质）

### 限价订单簿（LOB）价格趋势预测
- TS525（高）[TLOB: A Novel Transformer Model with Dual Attention for Price Trend Prediction with Limit Order Book Data](../../pdfs/2025_Berti_TLOB_en.pdf) — 预测；目标：基于 LOB 的价格趋势（上涨/持平/下跌）分类；方法：深度学习（双注意力 Transformer TLOB；对比 MLP 等）

### 已实现波动率（粗糙波动 / 分数布朗运动）
- TS526（中）[Modeling and Forecasting Realized Volatility with Multivariate Fractional Brownian Motion](../../pdfs/2025_Bibinger_ModelingForecastingRealizedVolatility_en.pdf) — 预测；目标：已实现波动率（多变量）；方法：统计（多变量分数布朗运动 mfBm，最优预测公式）

### 尾部风险（VaR/ES，已实现高阶矩）
- TS527（中）[Dynamic tail risk forecasting: what do realized skewness and kurtosis add?](../../pdfs/2024_Gallo_DynamicTailRiskForecasting_en.pdf) — 预测；目标：个股 VaR 与 ES；方法：统计（加性与乘性模型纳入已实现偏度/峰度）

### 尾部风险（ES 动态模型）
- TS528（中）[CAESar: Conditional Autoregressive Expected Shortfall](../../pdfs/2024_Gatta_CAESar_en.pdf) — 预测；目标：VaR 与 ES（联合）；方法：统计（CAESar：CAViaR + ES 自回归，联合可引出损失）

### 尾部风险（多步 VaR/ES）
- TS529（中）[Using quantile time series and historical simulation to forecast financial risk multiple steps ahead](../../pdfs/2025_Gerlach_QuantileTimeSeriesHistorical_en.pdf) — 预测；目标：1% 与 2.5% 的 VaR 和 ES；方法：统计（分位数时间序列 + 半参数历史模拟）

### 尾部风险（分位数尺度动态）
- TS530（中）[Quantile-based modeling of scale dynamics in financial returns for Value-at-Risk and Expected Shortfall forecasting](../../pdfs/2025_Liu_QuantileModelingScaleDynamics_en.pdf) — 预测；目标：VaR 与 ES；方法：统计（受限分位回归建模条件尺度）

### 尾部风险（窗口选择 / 结构变化）
- TS531（中）[Adaptive Window Selection for Financial Risk Forecasting](../../pdfs/2026_Li_AdaptiveWindowSelectionFinancial_en.pdf) — 预测；目标：VaR 及 VaR-ES 对；方法：统计（自助法自适应窗口选择 BAWS，在线学习）

### 已实现协方差矩阵预测（几何深度学习）
- TS533（中）[Geometric Deep Learning for Realized Covariance Matrix Forecasting](../../pdfs/2024_Bucci_GeometricDeepLearningRealized_en.pdf) — 预测；目标：日度已实现协方差矩阵；方法：深度学习（黎曼几何感知网络；矩阵变量 HAR 扩展）

### 已实现波动率（全球市场溢出 / 图信号处理）
- TS534（中）[Graph Signal Processing for Global Stock Market Realized Volatility Forecasting](../../pdfs/2024_Chi_GraphSignalProcessingGlobal_en.pdf) — 预测；目标：24 个全球股指的已实现波动率；方法：混合（HAR + 图信号处理 / 图傅里叶变换）

### 横截面波动率预测（体制信息）
- TS535（中）[Regime-Gated Residual Mixture-of-Experts for Cross-Sectional Volatility Forecasting](../../pdfs/2026_Ye_RegimeGatedResidualMixture_en.pdf) — 预测；目标：个股未来 5 日已实现波动率；方法：深度学习（体制门控残差专家混合 RG-ResMoE）

### 已实现波动率（期权信息 / 粗糙波动）
- TS536（中）[On options-driven realized volatility forecasting: Information gains via rough volatility model](../../pdfs/2026_Fan_OptionsDrivenRealizedVolatility_en.pdf) — 预测；目标：日度已实现波动率；方法：混合（HAR + 粗糙 Heston 现货波动估计，深度学习代理加速）

### 波动率（新闻多模态 + 时点一致 LLM）
- TS537（中）[Fusing Narrative Semantics for Financial Volatility Forecasting](../../pdfs/2025_Kong_FusingNarrativeSemanticsFinancial_en.pdf) — 预测；目标：金融波动率；方法：深度学习（多模态网络 M2VN，对齐损失）

### 隐含波动率曲面预测
- TS538（中）[Forecasting implied volatility surface with generative diffusion models](../../pdfs/2025_Jin_ForecastingImpliedVolatilitySurface_en.pdf) — 预测；目标：一天后的（近似无套利）隐含波动率曲面；方法：深度学习（条件 DDPM 扩散模型，SNR 加权套利惩罚）

### 外汇日内波动率曲线
- TS539（中）[Intraday FX Volatility-Curve Forecasting with Functional GARCH Approaches](../../pdfs/2023_Kearney_IntradayFXVolatilityCurve_en.pdf) — 预测；目标：USD/EUR、USD/GBP、USD/JPY 日内波动率曲线（及日内 VaR）；方法：统计（函数型 GARCH + 多层函数主成分）

### 外汇汇率预测（长记忆）
- TS540（中）[Neural ARFIMA model for forecasting BRIC exchange rates with long memory](../../pdfs/2025_Besher_NeuralARFIMAModelForecasting_en.pdf) — 预测；目标：BRIC 汇率；方法：混合（NARFIMA：ARFIMA 长记忆 + 神经网络；共形预测区间）

### 外汇收益可预测性（LLM 基本面）
- TS541（中）[AI and Exchange Rate Predictability](../../pdfs/2026_Izadyar_AIExchangeRatePredictability_en.pdf) — 预测；目标：主要货币对的收益（横截面）；方法：基础模型（大语言模型提取基本面强度）

### 利率 / 收益率曲线
- TS542（中）[Yield Curve Prediction with Machine Learning: Forecasting Approaches and the Role of Macroeconomic Predictors](../../pdfs/2026_Kang_YieldCurvePredictionMachine_en.pdf) — 预测；目标：美国国债月度零息收益率（水平与斜率）；方法：机器学习（直接收益率法 vs 因子法）

### 利率期限结构
- TS543（中）[Forecasting the Term Structure of Interest Rates with SPDE-Based Models](../../pdfs/2025_Duan_ForecastingTermStructureInterest_en.pdf) — 预测；目标：利率期限结构（收益率曲线）点预测与概率预测；方法：统计（动态 Nelson-Siegel + SPDE 高斯随机场残差，INLA 贝叶斯推断）

### 利率 / 多条收益率曲线
- TS544（中）[Multiple yield curve modeling and forecasting using deep learning](../../pdfs/2024_Richman_MultipleYieldCurveModeling_en.pdf) — 预测；目标：多条收益率曲线的点预测与区间预测；方法：深度学习（自注意力 + 非参数分位回归，避免分位交叉）

### 跨资产（股票 + 利率）基础模型
- TS545（中）[Multivariate Financial Forecasting using the Chronos Time Series Foundation Models](../../pdfs/2026_Das_MultivariateFinancialForecastingChronos_en.pdf) — 预测；目标：Magnificent-7 股票与美国国债利率（RMSE/MAPE）；方法：基础模型（Chronos-2，多变量 vs 单变量输入）

### 加密资产波动率（概率预测）
- TS546（中）[Probabilistic Forecasting Cryptocurrencies Volatility: From Point to Quantile Forecasts](../../pdfs/2025_Dudek_ProbabilisticForecastingCryptocurrencies_en.pdf) — 预测；目标：比特币已实现方差的条件分位数；方法：混合（HAR、GARCH、ARFIMA、LASSO、SVR、MLP、RF、LSTM 等基模型 + 残差模拟分位估计/概率堆叠）

### 加密资产收益与波动（链上数据）
- TS547（中）[Return and Volatility Forecasting Using On-Chain Flows in Cryptocurrency Markets](../../pdfs/2024_Chi_ReturnVolatilityForecastingChain_en.pdf) — 预测；目标：BTC、ETH 日内收益与波动率；方法：统计（预测回归）

### 加密资产价格预测（文献评估）
- TS548（中）[Bitcoin Price Prediction: Peer-Reviewed Evidence and Social Media Discourse](../../pdfs/2026_Baquero_BitcoinPricePrediction_en.pdf) — 综述；目标：比特币价格（1-6 个月跨度能否胜过朴素基准）；方法：其他（综述）

### 限价订单簿（L3 事件）短期趋势预测
- TS549（低）[Event History Over Scale: Compact Transformers for Low-Latency Limit Order Book Forecasting](../../pdfs/2026_Schaurecker_EventHistoryOverScale_en.pdf) — 预测；目标：短期价格趋势（宏 F1）；方法：深度学习（约 7 千参数的紧凑因果 Transformer MBOFormer / MBOFusion）

### 日内成交量预测
- TS550（中）[Forecasting Intraday Volume in Equity Markets with Machine Learning](../../pdfs/2025_Cucuringu_ForecastingIntradayVolumeEquity_en.pdf) — 预测；目标：个股日内成交量；方法：机器学习（多种 ML + 高频预测因子，考虑共性）

### 日内股票收益预测
- TS551（中）[Multi-Horizon Echo State Network Prediction of Intraday Stock Returns](../../pdfs/2025_Ballarin_MultiHorizonEchoState_en.pdf) — 预测；目标：多跨度日内股票收益；方法：机器学习（回声状态网络 ESN，随机储备池 + 岭回归）

### 横截面股票收益预测
- TS552（中）[Dependence-Informed Sparse Neural Architecture for Stock Return Prediction](../../pdfs/2026_Lin_DependenceInformedSparseNeural_en.pdf) — 预测；目标：美股年度超额收益（横截面）；方法：深度学习（由 MFCF 图结构确定的稀疏同调神经网络 HNN）

### 期权隐含信号与崩盘风险
- TS553（中）[Option-Implied Signals and Crash Risk: Predictability and Machine-Learning Evidence from U.S. Equity Options](../../pdfs/2026_Li_OptionImpliedSignalsCrash_en.pdf) — 预测；目标：下月个股收益与 5 日个股崩盘（分类）；方法：统计 + 机器学习（重估经典期权信号；提升树）

### 金融市场预警（新兴市场）
- TS554（中）[An early warning system for emerging markets](../../pdfs/2024_Kraevskiy_EarlyWarningSystemEmerging_en.pdf) — 预警；目标：新兴市场信息传导的体制转换/变点（概念漂移）；方法：统计 + 机器学习（条件熵、随机森林、copula 的在线预警系统）

### LLM 智能体股票收益现时预测
- TS555（中）[Autonomous Market Intelligence: Agentic AI Nowcasting Predicts Stock Returns](../../pdfs/2026_Chen_AutonomousMarketIntelligence_en.pdf) — 预测；目标：Russell 1000 成分股日度吸引力排名（对应后续收益）；方法：基础模型（自主联网的 LLM 智能体）

### 时点一致的语言模型（前视偏差控制）
- TS556（中）[Chronologically Consistent Large Language Models](../../pdfs/2025_He_ChronologicallyConsistentLargeLanguage_en.pdf) — 预测；目标：基于新闻的次日股票收益；方法：基础模型（ChronoBERT、ChronoGPT）

### 回测过拟合与数据挖掘偏差
- TS557（中）[What survives honest evaluation? Leakage-safe, search-aware assessment of LLM-driven trading strategy discovery](../../pdfs/2026_Gencay_WhatSurvivesHonestEvaluation_en.pdf) — 预测；目标：LLM 发现的交易策略的样本外表现（Deflated Sharpe 等）；方法：其他（评估框架：防泄漏工具注册 + 按试验次数折减）

### 多资产 / 跨资产体制预测
- TS558（低）[Dynamic Asset Allocation with Asset-Specific Regime Forecasts](../../pdfs/2024_Shu_DynamicAssetAllocationAsset_en.pdf) — 预测；目标：各资产牛熊体制（分类）及据此的收益与风险预测；方法：混合（统计跳跃模型无监督标注 + 梯度提升树监督预测）

### 高频波动率与收益（中国股市，体制）
- TS559（低）[Volatility Forecasting and Return Prediction under Market Regimes: Evidence from High-Frequency Chinese Equity Data](../../pdfs/2026_Fang_VolatilityForecastingReturnPrediction_en.pdf) — 预测；目标：CSI 300 已实现波动率与收益；方法：混合（体制增强 HARQ + 马尔可夫转换 GJR-GARCH；XGBoost 收益预测）

### LOB 市场操纵检测
- TS560（低）[Detecting Multilevel Manipulation from Limit Order Book via Cascaded Contrastive Representation Learning](../../pdfs/2025_Lin_DetectingMultilevelManipulationLimit_en.pdf) — 异常检测；目标：订单簿中的多层级幌骗（spoofing）操纵；方法：深度学习（级联 LOB 表示 + 监督对比学习；Transformer 最佳）

### LOB 价格趋势预测基准
- TS561【三年前】（中）[LOB-Based Deep Learning Models for Stock Price Trend Prediction: A Benchmark Study](../../pdfs/2023_Prata_LOBDeepLearningModels_en.pdf) — 基准/数据集；目标：基于 LOB 的股票价格趋势；方法：深度学习（15 个 SOTA 模型）

### 金融 LLM 评测偏差（立场论文）
- TS563（中）[Evaluating LLMs in Finance Requires Explicit Bias Consideration](../../pdfs/2026_Kong_EvaluatingLLMsFinanceRequires_en.pdf) — 综述；目标：金融 LLM 应用的评测有效性；方法：其他（立场/综述）

### 结构突变
- TS010（低）[Interval Forecasts for Gas Prices in the Face of Structural Breaks -- Statistical Models vs. Neural Networks](../../pdfs/2024_Schluter_IntervalForecastsGasPrices_en.pdf) — 预测；不确定性量化；评测比较；目标：欧洲天然气价格的区间预测，比较统计模型与神经网络在结构突变（俄乌战争、北溪 1 号爆炸冲击）下的稳健性；方法：统计 + 深度学习对比（条件异方差 ARMA、copula 时间序列模型 vs MLP、LSTM）

### 风光混合发电预测与交易竞赛
- TS578（高）[The hybrid renewable energy forecasting and trading competition 2024](../../pdfs/2025_Browell_HybridRenewableEnergyForecasting_en.pdf) — 基准/数据集；目标：英国 3.6 GW 风电与光伏组合日前发电（分位数）及交易；方法：多方法竞赛分析（梯度提升树等）

### 基础模型电价预测评测 + 经济价值
- TS595（高）[Foundation models for electricity price forecasting and battery arbitrage: Can they replace market-specific forecasting models?](../../pdfs/2026_Lipiecki_FoundationModelsElectricityPrice_en.pdf) — 预测；目标：德国、波兰、西班牙日前电价的点与概率预测；方法：基础模型（5 个家族 9 个变体，零样本，含 TabPFN）对比 DDNN 等专用基准

### 电价概率后处理（QRA/保形/IDR 比较与组合）
- TS610（中）[Postprocessing of point predictions for probabilistic forecasting of day-ahead electricity prices: The benefits of using isotonic distributional regression](../../pdfs/2024_Lipiecki_PostprocessingPointPredictionsProbabilis_en.pdf) — 预测；目标：德国与西班牙日前电价的预测分布；方法：统计（分位数回归平均、保形预测、等渗分布回归 IDR 及其组合）

### 日内连续市场电价路径概率预测
- TS612（中）[Probabilistic intraday electricity price forecasting using generative machine learning](../../pdfs/2025_Chen_ProbabilisticIntradayElectricityPrice_en.pdf) — 预测；目标：德国连续日内市场电价的概率路径；方法：深度学习（生成式神经网络）

### 中长期电价（计量经济模型）
- TS613（中）[From day-ahead to mid and long-term horizons with econometric electricity price forecasting models](../../pdfs/2024_Ghelasi_DayAheadMidLong_en.pdf) — 预测；目标：电价（一天至一年前瞻）；方法：统计（计量经济模型：基本面约束系数、季节期望回归项、同日关系外推处理单位根）

