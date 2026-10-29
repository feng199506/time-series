# 时间序列分析与预测文献库：本轮最终报告

报告日期：2026-10-29。项目路径：`/root/time_series_literature/`。

**计数口径**：只计“原文全文已下载并核验通过”的条目；候选、仅链接、下载失败、待核验、下载错文献均不计。下载核验只检查文件完整性、题名、作者和目录，**不等于精读**。所有简介与字段都依据摘要或官方页面描述。

## 1. 论文：分领域统计

| 分类 | 已核验全文 / 目标约 50 | 主分类 | 独有 | 跨类 | 近三年（占比） | 三年前 | 待核验 | 下载失败 | 状态 |
|---|---|---|---|---|---|---|---|---|---|
| 通用方法 | 73 | 58 | 57 | 16 | 68（93.2%） | 5 | 1 | 0 | 达标 |
| 金融 | 55 | 49 | 46 | 9 | 53（96.4%） | 2 | 2 | 0 | 达标 |
| 空气质量 | 51 | 50 | 42 | 9 | 50（98.0%） | 1 | 2 | 13 | 达标 |
| 水质 | 50 | 50 | 39 | 11 | 50（100%） | 0 | 0 | 22 | 达标（含补充检索） |
| 气象与气候 | 66 | 41 | 35 | 31 | 64（97.0%） | 2 | 2 | 4 | 达标 |
| 能源与电力 | 56 | 45 | 26 | 30 | 53（94.6%） | 3 | 2 | 1 | 达标 |
| 水文与水资源 | 50 | 50 | 46 | 4 | 46（92.0%） | 4 | 0 | 1 | 达标 |
| 交通与出行 | 51 | 47 | 42 | 9 | 49（96.1%） | 2 | 1 | 0 | 达标 |
| 工业与设备 | 50 | 46 | 40 | 10 | 50（100%） | 0 | 1 | 2 | 达标 |
| 医疗与公共卫生 | 50 | 48 | 45 | 5 | 48（96.0%） | 2 | 2 | 5 | 达标 |

列的含义：
- **已核验全文**：含交叉标注计入的论文；同一论文在同一分类只计一次。
- **主分类 / 独有 / 跨类**：分别为以该类为主分类的数量、只属于该类的数量、同时属于两类及以上的数量。
- **近三年占比**：以已核验全文为分母。

全库去重：
- 已核验论文 **484 篇**，PDF 文件 **484 个**（每篇一份，跨类论文用统一编号在各分类引用）。
- 近三年 **463 篇**，三年前 **21 篇**，每类三年前文献不超过 5 篇，均写明保留理由。
- 另有待核验 11 篇、下载失败 41 篇，均不计入；明细见 `download_failures_cn.csv`。

通用方法类的 73 篇中，有 15 篇是应用领域论文按摘要交叉标注计入（如基准、评测类论文）；以通用方法为主分类的是 58 篇。

## 2. 学习资料统计

| 类别 | 已核验 / 目标约 50 | 待核验 | 失败或剔除 | 年份分布（已核验，按版本年份或学期） | 格式 | 状态 |
|---|---|---|---|---|---|---|
| 大学课程教材与完整讲义 | **50** | 2 | 9 | 2023 年及以后 16；2018–2022 年 9；2010–2017 年 13；2009 年及以前 7；待核实 5 | 多文件 PDF 讲义包 35；单一 PDF 12；官方 HTML 离线包 3 | 达标 |
| 教科书、专著与参考书 | **49** | 2 | 4 | 2018–2022 年 17；2023 年及以后 13；2010–2017 年 9；2009 年及以前 5；待核实 5 | PDF 48；HTML 离线包 1 | **未完成（49/50）** |

书籍差最后 1 本：Svetunkov《ADAM》官方 HTML 版的离线包仍在后台抓取（单本请求较多，限速每 3 秒 1 次）。完成并核验后，执行一次 `build_materials_en.py` 和 `build_catalog_en.py` 即可补入统计。

去重处理：
- 学习资料独立去重后共 **99 份**（讲义 50 + 书籍 49），与论文分开统计、互不冲抵。
- 同一讲义的多个学期版本（ETH Dettling 讲义 3 个版本只保留 2016 版）、同一讲义的不同排版副本（Künsch 讲义）、书籍的前身讲义（Särkkä 2010/2012 课程讲义与其著作第 2 版）都只计一次，被剔除的文件已删除，原因写入记录。
- 我按规则剔除的非书籍或非大学课程条目：1 篇期刊长综述、4 个研讨会或短期课程、1 套仅以 HTML 注释形式存在的讲义、1 套缺讲次的讲义。

人工核验：讲义 UM020、UM022、UM054 因自动规则误判（PDF 无署名、文字编码问题、官方页面坏链）而做了人工核验，结论记录在 `scripts/seeds/materials_manual_checks_cn.json`。

## 3. 覆盖情况与缺口

### 论文
| 分类 | 主要子方向 | 明显缺口 |
|---|---|---|
| 通用方法 | 分解、频域、非平稳、状态空间、结构突变；ETS/VARMA/VAR；概率预测与共形；特征工程、GBDT、全局模型；RNN/CNN/Transformer/MLP 与简单基线；基础模型及适配；基准、泄漏、指标与交叉验证 | 经典单位根检验、经典谱估计、动态回归的近三年方法论文较少 |
| 金融 | 已实现波动率（HAR vs ML）、协方差、VaR/ES、收益与方向、外汇、利率、加密资产、限价订单簿、金融基础模型、LLM 前视偏差与记忆批评 | 商品、信用利差、系统性风险预警；无 arXiv 版的开放获取期刊论文 |
| 空气质量 | AI 全球/区域预报（Aurora、AIFS-COMPO）、概率与集合、物理引导站网模型、CTM 后处理、超标预警、野火烟雾、沙尘、次季节、基准与基础模型评测、低成本传感器 | 卫星驱动预报、SO₂、与健康入院的关联 |
| 水质 | 河流水温、溶解氧与缺氧、营养盐、叶绿素与藻华预警、湖泊生态预测与基础模型、盐度、微生物指标、给水余氯、污水出水、地下水硝酸盐 | pH 预测、溶解有机碳、水厂原水浊度、概率/共形水质预测 |
| 气象与气候 | 全球中期 ML 与集合（GenCast、AIFS、NeuralGCM）、区域公里级、降水临近预报、次季节到季节与气候模拟器、ENSO、热带气旋、极端事件、后处理与评估 | 季节预测（3–6 个月）、湿度、只有期刊版本的开放获取论文（因检索限流） |
| 能源与电力 | 系统/区域/户级负荷、日前与日内电价、风电与光伏（卫星、天空图像）、热与燃气、EV 充电、层级调和、基础模型评测、竞赛与基准 | 只有期刊版本的开放获取论文（如 WES、Solar Energy） |
| 水文与水资源 | 全球与业务径流/洪水、大样本 LSTM、可微分物理融合、概率与不确定性、小时尺度洪水、河网图模型、无资料流域、地下水、干旱、积雪、水库、CAMELS/Caravan | 水库调度、湖泊水位、冰川融水、GloFAS/NWM 后处理；中国与南亚期刊 |
| 交通与出行 | 评测审计、基准、基础模型零样本、LLM、大规模非图模型、分布漂移、概率预测、事件影响、统计与物理方法、地铁/公交/网约车/航空/铁路 | 港口物流、停车；只有期刊版本的 TR-C/T-ITS 论文 |
| 工业与设备 | 涡扇发动机 RUL、数据切分与泄漏批评、轴承、电池寿命、刀具磨损、软测量、工业基础模型、随机退化与生存模型、数字孪生 | 泵与压缩机、硬盘故障；多数软测量是当前值估计，不是提前多步预测 |
| 医疗与公共卫生 | 血糖/CGM、可穿戴、ICU 生命体征与医疗基础模型、恶化预警、疾病进展、流感/登革热预测中心评测、nowcasting、污水监测、资源需求、WIS 评测 | 慢性肾病/eGFR、心理健康可穿戴、病房恶化 |

### 学习资料
- **覆盖较好**：统计与随机过程基础、经典时间序列、谱分析、状态空间/Kalman/粒子滤波、非线性与非平稳、贝叶斯宏观、金融波动率、时空统计、深度学习、共形预测、变点与异常检测、季节调整、能源负荷与风光预测、水资源统计与洪水预报、预测性维护（课程）。
- **缺口**：
  - 时间序列基础模型没有合法公开的书本长度资料；
  - 层级预测与预测组合只有 FPP3 相关章节和少量课程；
  - 面板时间序列没有公开且完整的课程；
  - 数据泄漏与可复现性没有专书；
  - 空气质量与工业 RUL 没有公开书籍；
  - 中文课程只找到 1 套，而且因 TLS 证书问题未能下载。

## 4. 优先阅读

- 每类论文的 10 篇见附录 A，也见各 `domains/*/reading_map_cn.md`。
- 学习资料的核心书单与章节建议（依据已检查目录）见 `systematic_reading_guide_cn.md`，讲义与书籍的优先清单见 `university_materials/reading_map_cn.md` 和 `books/reading_map_cn.md`。

## 5. 未解决的来源、版本与下载问题

1. **出版社拒绝自动下载**：Wiley/AGU、ACS、PNAS、RSC、AMS、Elsevier、ResearchSquare、ESSOAr 返回 403；PMC 与 Europe PMC 返回网页或 Cloudflare 挑战页。这些论文全部记为失败、未绕过，并已用备选补位。水质类因此做了一轮补充检索。
2. **检索接口限流**：arXiv API 与 OpenAlex 在多领域并行检索期间长时间返回 429，导致只有期刊版本的开放获取论文在金融、能源、交通、水文、气象类中偏少。各类笔记中列出了未能执行的检索。
3. **渠道多为预印本**：已核验论文中有 261 篇只找到 arXiv 版本，未发现正式发表信息（标注为“未核实是否已发表”）；23 篇的会议接收信息仅来自作者在 arXiv 上的自述。
4. **以下 8 篇预印本只有 OpenAlex 或种子提供的渠道信息**（部分新 DOI 在 Crossref 未登记）：TS073、TS136、TS172、TS210、TS337、TS338、TS347、TS357。
5. **版本标注**：多数 PDF 是 arXiv 预印本或作者版，期刊正式版另见 DOI，目录中均已注明“非出版社排版版”。部分开放获取链接在元数据中没有版本标注，已注明下载域名，待人工确认。
6. **待核验（不计入）**：论文 11 篇（主要是参考文献节未识别、作者名在首页不可见），讲义 2 套（扫描件无文字；PSU 证书问题），书籍 2 本（WMO 指南仅 32 页、IMF 手册首页无作者）。文件保留在 `pending_pdfs/` 或对应目录中，等待人工复核。
7. **日期与题名**：
   - 部分 Copernicus 论文的讨论稿日期已经通过 Crossref 预印本关系纳入；
   - 少数讲义的学期或版本年份待核实（已标注）；
   - 金融 TS562 原先 arXiv 元数据中的 DOI 指向期刊更正声明，已改为原文 DOI，并按 2022 年计为三年前文献；
   - 若干论文的期刊版改了题名，目录的“其他题名”列已登记。
8. **执行中的问题**：下载脚本曾因文件未关闭就比较大小，误判约 50 篇为“截断”。已修复，并只对这些条目重新下载；全过程记录在 `search_log_cn.md` 第 11 节。

## 6. 扩展领域建议（检索中发现，未自行扩大下载）

- 宏观经济与通胀预测、现时预测（nowcasting）
- 预测市场与事件概率预测
- 大气成分数据同化
- 野火（火辐射功率、蔓延）预测
- 海洋预报（海温、海浪、海冰、风暴潮）
- 水生生态预测（NEON/EFI 挑战）
- 城市供水与用水需求预测
- 洪水淹没与水动力代理模型
- 蜂窝与网络流量预测
- 人类移动与轨迹预测
- 交通事故风险预测
- 零售与需求预测（间歇需求、层级）

## 7. 路径与续跑

- **入口文件**：`README_cn.md`（结构、核验标准、完整命令）、`catalog_cn.csv`（全库总目录）、`checksums_en.sha256`（`sha256sum -c checksums_en.sha256` 已全部通过）。
- **续跑**：所有脚本都可断点续跑，已核验、待核验、失败的条目不会重复请求。
- **补全最后一本书**：
  ```bash
  cd /root/time_series_literature
  python3 -I scripts/download_materials_en.py . <staging> <pypdf_dir> --kind book
  python3 -I scripts/build_materials_en.py . && python3 -I scripts/build_catalog_en.py .
  ```
- **项目大小**：论文 PDF 约 2.7 GB，书籍约 0.84 GB，讲义约 0.73 GB。
- **版本库**：项目目录下有一个 `.git` 版本库（非本轮创建），本轮未做任何提交或修改。

## 附录 A：各分类优先阅读 10 篇

理由均依据摘要，未读全文。完整路线与链接见各分类的 `reading_map_cn.md`。

### 通用方法（[阅读路线](domains/01_general_methods/reading_map_cn.md)）

1. TS054 *Hyndman & Khandakar 2008，auto.arima / ETS* —— 近期基准里的统计基线（AutoARIMA/AutoETS）都按此文定义；先弄清“基线是什么”。
2. TS055 *Hyndman & Koehler 2006，MASE* —— GIFT-Eval、fev-bench、Chronos 的主指标之一；理解 MAPE 等指标为何会退化。
3. TS056 *Gneiting & Raftery 2007，严格正常评分规则* —— CRPS / WQL / 区间分数的理论来源，读懂所有概率预测评测的前提。
4. TS058 *Zeng et al. 2022，DLinear* —— 近三年深度/基础模型论文的必比简单基线；TS027、TS029、TS031 都在回应它。
5. TS023 *Deep Time Series Models 综述 + TSLib* —— 深度学习路线的地图（模块、架构、统一基准），读完再看单篇模型更高效。
6. TS048 *There are no Champions（长期预测）* —— 说明 LTSF 排名对设定极敏感，读其他模型论文时用来校准对“SOTA”结论的信任度。
7. TS049 *TSFM 评测中的信息泄漏* —— 基础模型零样本结论是否可信的关键：预训练-测试重叠与时间重叠。
8. TS047 *fev-bench* —— 现行基础模型基准之一，且给出统计上更严谨的汇总（自助法置信区间、胜率与技能分）。
9. TS032 *Chronos* —— 基础模型路线的代表与后续工作（Chronos-2、ChronosX、fev-bench）的起点。
10. TS016 *共形时间序列预测入门综述* —— 预测区间与校准的现代方法总览，补足点预测之外的不确定性评估。

### 金融（[阅读路线](domains/02_finance/reading_map_cn.md)）

1. TS513 *HARd to Beat: The Overlooked Impact of Rolling Windows in the Era of Machine Learning* —— HAR 拟合方案设定合理时，ML 无法胜出，是检验基准公平性的范例。
2. TS514 *Forecasting Realized Volatility with Time Series Foundation Models: A Comparison with Econometric Be* —— 用 MCS 和 MZ 回归拆解 TSFM 的“优势”来自哪里。
3. TS515 *How do standard time series forecasting benchmarks translate to finance? A broad study of risk adjus* —— 通用 SOTA 架构不如 AR(1)，说明通用基准的排名不能迁移到金融。
4. TS517 *The Memorization Problem: Can We Trust LLMs' Economic Forecasts?* —— LLM 在训练覆盖期内的预测不可识别。
5. TS518 *Detecting Lookahead Bias in LLM Forecasts* —— 提出可操作的前视偏差检验（LAP）。
6. TS519 *FinVerse: Toward More Realistic Evaluation for Financial Time-Series Forecasting* —— 金融专用的 TSFM 基准，与 GIFT-Eval 的排名只中等相关。
7. TS524 *Evaluating financial tail risk forecasts: Testing Equal Predictive Ability* —— DM/MCS 在 VaR/ES 上检验力不足。
8. TS525 *TLOB: A Novel Transformer Model with Dual Attention for Price Trend Prediction with Limit Order Book* —— LOB 预测的最新代表，讨论可预测性衰减和价差成本。
9. TS523 *Combining a Large Pool of Forecasts of Value-at-Risk and Expected Shortfall* —— 尾部风险预测组合的系统研究。
10. TS520 *Kronos: A Foundation Model for the Language of Financial Markets* —— （补位）近期影响较大的金融专用基础模型，可与 rank4/9 的批判性结果对照阅读。

### 空气质量（[阅读路线](domains/03_air_quality/reading_map_cn.md)）

1. TS059 *A foundation model for the Earth system* —— 地球系统基础模型在空气质量预报上超过业务系统，代表范式转变。
2. TS060 *AIFS-COMPO: A Global Data-Driven Atmospheric Composition Forecasting System* —— ECMWF 业务路线的数据驱动成分预报，与 CAMS IFS-COMPO 直接对比。
3. TS062 *Diffusion-based Probabilistic Air Quality Forecasting with Mechanistic Insight* —— 扩散模型做 30 成员臭氧集合预报，并量化天气不确定性。
4. TS063 *Global probabilistic forecasting of air pollution* —— 全球公里级概率 PM2.5 预报，校准集合与提前 4 天极端探测。
5. TS067 *AirPhyNet: Harnessing Physics-Guided Neural Networks for Air Quality Prediction* —— 物理引导站点网络模型的常用基线（ICLR）。
6. TS074 *E-STGCN: extreme spatio-temporal graph convolutional networks for air quality forecasting* —— 极值理论 + 图网络 + 共形区间，统计期刊发表。
7. TS086 *AirQualityBench: A Realistic Evaluation Benchmark for Global Air Quality Forecasting* —— 保留原生缺测的全球评测，揭示“干净数据集”上的优势不可迁移。
8. TS104 *Applications of Machine Learning and Artificial Intelligence in Tropospheric Ozone Research* —— TOAR 视角下臭氧 ML 全景与挑战。
9. TS061 *Advancing global aerosol forecasting with artificial intelligence* —— （补位）全球中期气溶胶 AI 预报代表作，覆盖沙尘/野火等污染事件预警场景。
10. TS064 *Advancing operational PM2.5 forecasting with dual deep neural networks (D-DNet)* —— （补位）把“学习式同化”纳入 AI 空气质量业务预报，方法上区别于纯预测网络。

### 水质（[阅读路线](domains/04_water_quality/reading_map_cn.md)）

1. TS124 *Extended-range forecasting of stream water temperature with deep-learning models* —— 可业务化的 32 天概率水温预报（TFT，CRPS 评估，新站外推）。
2. TS128 *Explainable deep learning for multi-horizon water quality forecasting: cross-continental transferabi* —— 与持续性基线比较并做跨洲零样本迁移，结论审慎。
3. TS126 *Identifying trustworthiness challenges in deep learning models for continental-scale water quality p* —— 482 流域 20 变量的深度模型可信度系统评估。
4. TS131 *LakeFM : Toward a Foundation Model for Aquatic Ecosystems Using Irregular Multivariate Multi-depth T* —— 面向湖泊不规则多深度数据的基础模型。
5. TS136 *Time-series foundation modeling enables accurate lake ecosystem forecasting* —— Chronos/Lag-Llama 在长期月度湖泊数据上与 15 种方法对比（预印本）。
6. TS132 *Forecasting coastal hypoxia using a blend of mechanistic and artificial intelligence models* —— 机理模型后报训练 AI 的近海缺氧日预报。
7. TS164 *Machine Learning for Effluent Forecasting at a Full-Scale Municipal Wastewater Treatment Plant: Seas* —— 污水厂预测与朴素基线严格比较，揭示插值日评估造成的虚高。
8. TS125 *Deep learning for water quality* —— （补位）领域权威综述，可作为本类阅读起点与方法地图。
9. TS129 *LSTM networks provide efficient cyanobacterial blooms forecasting even with incomplete spatio-tempor* —— （补位）Water Research 发表，直面缺测高频传感器数据的水华预警，方法可复用。
10. TS135 *Evaluating Deep Learning Approaches for Predictions in Unmonitored Basins with Continental-scale Str* —— （补位）无资料流域（PUB）水温预测的系统设计实验，回答数据与模型设计问题。

### 气象与气候（[阅读路线](domains/05_weather_climate/reading_map_cn.md)）

1. TS254 *Probabilistic weather forecasting with machine learning* —— 数据驱动概率集合预报的代表，几乎所有后续集合模型都与它比较。
2. TS255 *Neural general circulation models for weather and climate* —— 混合物理-ML 路线，同时覆盖天气与气候时间尺度。
3. TS256 *End-to-end data-driven weather prediction* —— 端到端由观测到站点预报，改变 NWP 流程的范式。
4. TS059 *A foundation model for the Earth system* —— 基础模型 + 微调，覆盖天气、空气质量、海浪、TC。
5. TS276 *ChaosBench: A Multi-Channel, Physics-Based Benchmark for Subseasonal-to-Seasonal Climate Prediction* —— 说明中期模型外推到 S2S 会失效，是 S2S 评测基础。
6. TS287 *Can AI weather models predict out-of-distribution gray swan tropical cyclones?* —— 检验 AI 模型能否外推到训练集中缺失的极端事件。
7. TS292 *Do AI weather models miss extremes?* —— 用站点观测检验尾部表现，校正笼统结论。
8. TS274 *How Effective Are Time-Series Models for Precipitation Nowcasting? A Comprehensive Benchmark for GNS* —— 通用时序模型在降水/湿度站点序列上的表现，与通用方法类别交叉。
9. TS257 *AIFS -- ECMWF's data-driven forecasting system* —— （补位）首个由主要业务中心业务化运行的 ML 全球预报系统，代表数据驱动预报的业务落地。
10. TS258 *AIFS-CRPS: Ensemble forecasting using a model trained with a loss function based on the Continuous R* —— （补位）以评分规则直接训练集合模型的业务中心路线，与扩散类方法形成对照。

### 能源与电力（[阅读路线](domains/06_energy_power/reading_map_cn.md)）

1. TS578 *The hybrid renewable energy forecasting and trading competition 2024* —— The Hybrid Renewable Energy Forecasting and Trading Competition 2024。IJF 正式竞赛报告，真实前向评测，同时讨论预测技巧与交易价值。
2. TS579 *Energy Forecasting: A Review and Outlook* —— Energy Forecasting: A Review and Outlook（2020）。领域权威综述，给出可复现研究规范与开放数据源。
3. TS580 *Combining Weather Forecast Aggregation and State-Space Models for Adaptive Probabilistic Electricity* —— Combining Weather Forecast Aggregation and State-Space Models…。GAM + 状态空间在线自适应，并聚合多家气象预报，统计路线的代表。
4. TS581 *Efficient mid-term forecasting of hourly electricity load using generalized additive models* —— Efficient mid-term forecasting of hourly electricity load using GAMs。中期小时负荷，气温、节假日、经济变量处理细致，可解释。
5. TS583 *The role of probabilistic load and renewable prediction in enhancing day-ahead electricity price for* —— The role of probabilistic load and renewable prediction in enhancing day-ahead electricity price forecasts。把负荷
6. TS585 *Day-Ahead Electricity Price Forecasting Using Merit-Order Curves Time Series* —— Day-Ahead Electricity Price Forecasting Using Merit-Order Curves Time Series。从供需曲线（市场机制）出发的结构化电价预测。
7. TS586 *Seamless short- to mid-term probabilistic wind power forecasting* —— Seamless short- to mid-term probabilistic wind power forecasting。拆分天气不确定性与功率转换不确定性，6-162 小时一个模型覆盖。
8. TS588 *Intraday spatiotemporal PV power prediction at national scale using satellite-based solar forecast m* —— Intraday spatiotemporal PV power prediction at national scale…。全国 6434 个站点的卫星光伏时空预测评估。
9. TS591 *FETS Benchmark: Foundation Models Enable Scalable and Generalizable Energy Time Series Forecasting* —— FETS Benchmark。覆盖 54 个能源数据集的基础模型与专用模型对比。
10. TS595 *Foundation models for electricity price forecasting and battery arbitrage: Can they replace market-s* —— Foundation models for electricity price forecasting and battery arbitrage。同时给出统计与经济评价，结论审慎（基础模型不能普遍取代专用模型）。

### 水文与水资源（[阅读路线](domains/07_hydrology/reading_map_cn.md)）

1. TS383 *AIFL: A global daily streamflow forecasting model using deterministic an LSTM pre-trained on ERA5-La* —— 业务预报驱动下的数据驱动全球基线，按时间外推评测。
2. TS384 *HESS Opinions: Never train a Long Short-Term Memory (LSTM) network on a single basin* —— 大样本训练的方法论共识。
3. TS385 *Global prediction of extreme floods in ungauged watersheds* —— 全球无资料流域洪水预警的标杆与常用对比对象。
4. TS386 *Hourly U.S.-wide flood simulation beyond the limits of traditional and data-driven models* —— 可微分模型在小时、河网尺度上对比 NWM 与 LSTM。
5. TS388 *RiverMamba: A State Space Model for Global River Discharge and Flood Forecasting* —— 全球 0.05° 网格、利用河网空间关系的 7 天洪水预报。
6. TS389 *Probabilistic Diffusion Models Advance Extreme Flood Forecasting* —— 扩散模型做极端洪水概率预报的代表。
7. TS396 *Towards a global spatial machine learning model for seasonal groundwater level predictions in German* —— 5,288 口井、12 周的全局地下水位预测。
8. TS398 *Deep learning for flash drought forecasting and interpretation* —— 骤旱预警与可解释性。
9. TS410 *Ranked Right, Sized Wrong: Ensemble Spread Fails Silently at Streamflow Extremes* —— 深度学习集合不确定性在极端流量下的失效，直接关系预警可信度。
10. TS390 *Caravan MultiMet: Extending Caravan with Multiple Weather Nowcasts and Forecasts* —— （补位）评测“真实业务预报驱动”下水文预报的关键数据基础。

### 交通与出行（[阅读路线](domains/08_transport/reading_map_cn.md)）

1. TS448 *A Critical Audit of Spatiotemporal Forecasting Benchmark Datasets and Models* —— A Critical Audit of Spatiotemporal Forecasting Benchmark Datasets and Models。调好时间线性基线后，GNN 的增益显著缩小或被反超，解读排行榜前应
2. TS449 *Time Series Foundation Models as Strong Baselines in Transportation Forecasting: A Large-Scale Bench* —— Time Series Foundation Models as Strong Baselines in Transportation Forecasting。Chronos-2 零样本在 10 个交通数据集上有竞争力，
3. TS450 *Do We Really Need Adaptive Global Spatial Attention for Traffic Forecasting?* —— Do We Really Need Adaptive Global Spatial Attention for Traffic Forecasting?。受控消融显示空间注意力相对均匀混合没有一致优势。
4. TS451 *XXLTraffic: Expanding and Extremely Long Traffic forecasting beyond test adaptation* —— XXLTraffic。超长时间跨度且有分布漂移的交通基准，检验部署期稳健性。
5. TS452 *RideBench: A Large-Scale Exogenous-Aware Benchmark for Ride-Hailing Time Series Forecasting* —— RideBench。带天气、节假日、大型活动外生标注的滴滴网约车基准。
6. TS453 *Open Spatio-Temporal Foundation Models for Traffic Prediction* —— OpenCity。开源交通时空基础模型，可与 rank 2 的通用 TSFM 对照。
7. TS455 *Incident-Guided Spatiotemporal Traffic Forecasting* —— Incident-Guided Spatiotemporal Traffic Forecasting。把事件影响拆成空间扩散与时间衰减，并附对齐数据集。
8. TS456 *Predicting subway passenger flows under incident situation with causality* —— Predicting Subway Passenger Flows under Incident Situation with Causality。用合成控制估计事件因果效应，再嵌入预测。
9. TS457 *Hierarchical Forecast Reconciliation for Urban Rail Transit Demand Prediction under Operational Disr* —— Hierarchical Forecast Reconciliation for Urban Rail Transit Demand Prediction under Operational Disruptions。站点
10. TS458 *Conditional forecasting of bus travel time and passenger occupancy with Bayesian Markov regime-switc* —— Bayesian Markov regime-switching VAR for bus travel time and occupancy（TR-B）。高质量统计方法，给出联合不确定性。

### 工业与设备（[阅读路线](domains/09_industrial/reading_map_cn.md)）

1. TS191 *Leakage-Robust Evaluation and Data-Scale Sensitivity of Attention-Enhanced Multi-Task Learning for J* —— 量化滑动窗口切分泄漏把准确率从 20-60% 抬到 99.9%，是数据集划分批评的直接证据。
2. TS210 *Auditing Operating-Condition Normalization in C-MAPSS Remaining Useful Life Evaluation* —— 1800 次受控运行显示归一化与重拟合策略会改变 C-MAPSS 的 RMSE 排名。
3. TS190 *CruiseBench: A Real-Flight-Aligned N-CMAPSS Benchmark for Engine RUL Prediction* —— 给 N-CMAPSS 一个固定、可复现的巡航段协议。
4. TS189 *BatteryLife: A Comprehensive Dataset and Benchmark for Battery Life Prediction* —— 目前最广的电池寿命数据集与统一基准。
5. TS192 *Self-Supervised Pretraining for PHM: What Transfers, What Does Not, and What Federating It Costs* —— 在泄漏受控条件下，预训练对 RUL 无稳定收益。
6. TS202 *Do Time-Series Foundation Models Pay Off for Industrial Monitoring? A Cost-Aware Empirical Study* —— 计入成本后，轻量基线仍有竞争力。
7. TS203 *IND-Eval: Aligning Evaluation and Simulation for Industrial Time Series Foundation Models* —— 专门面向工业时间序列的 TSFM 预测基准。
8. TS199 *Empirical Calibration and Conditional-Reliability Diagnostics for Bearing RUL Prediction under Opera* —— 按工况留出评测，并看条件覆盖率。
9. TS196 *RULSurv: A probabilistic survival-based method for early censoring-aware prediction of remaining use* —— 在 RUL 建模中显式处理删失数据。
10. TS197 *Generalization bounds and sample complexity for remaining useful life prediction from complete degra* —— 从理论上回答“需要多少条失效轨迹”。

### 医疗与公共卫生（[阅读路线](domains/10_health/reading_map_cn.md)）

1. TS318 *Evaluation of FluSight influenza forecasting in the 2021–22 and 2022–23 seasons with a new target la* —— 流感住院新目标下集合预报的权威前瞻评测，WIS/覆盖率评估范式。
2. TS319 *GlucoBench: Curated List of Continuous Glucose Monitoring Datasets with Prediction Benchmarks* —— CGM 血糖预测的标准化数据集与基准。
3. TS320 *Learning the natural history of human disease with generative transformers* —— 纵向 EHR 疾病进展生成式预测，有跨国外部验证。
4. TS322 *Are Time Series Foundation Models Ready for Vital Sign Forecasting in Healthcare?* —— 对 TSFM 用于生命体征预测给出审慎证据。
5. TS323 *Deep learning models for acute kidney injury prediction: multi-center external validation and evalua* —— 揭示单点 AUROC 与连续部署表现的背离。
6. TS327 *Generative diffusion models for spatiotemporal influenza forecasting* —— 扩散模型做时空流行病预测，有实时检验。
7. TS329 *Mantis: A foundation model for mechanistic disease forecasting* —— 仅用机理模拟预训练的传染病预测基础模型，以 Forecast Hub 为对照。
8. TS331 *Stable Prediction of Adverse Events in Medical Time-Series Data* —— 把风险轨迹稳定性纳入预警评测。
9. TS334 *Evaluating infectious disease forecasts with allocation scoring rules* —— 评测与资源分配决策挂钩。
10. TS337 *Rethinking respiratory disease forecasting: temporal heterogeneity between surveillance predictors a* —— 监测预测因子与结局关系的非平稳性导致预测不稳定。
