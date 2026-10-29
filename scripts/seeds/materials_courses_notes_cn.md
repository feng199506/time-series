# 课程讲义类学习材料（materials_courses）检索与筛选说明

生成日期：2026-10-29　｜　对应种子文件：`scripts/seeds/materials_courses_seed_cn.json`（60 条：第 1-50 为主选，第 51-60 为备选）

## 1. 检索方法与来源

**核验方式**：每一条都回到官方课程页（或作者主页、OCW 页面）读取页面，并从 HTML 中逐个提取讲义链接。文件 URL 全部取自页面实际链接，没有按命名规律推测。MIT OCW 的 resource 页面逐个解析，得到真实 PDF 地址（带哈希前缀）。部分站点无法用 WebFetch 打开：PKU 与 PSU 的证书链不完整，TAMU 的 TLS 握手失败。这几处改用 WebSearch 摘要辅助判断，并在条目中标为“待核实”。

**下载可用性**：最后对全部单 PDF 条目做了 HEAD 检查，对每个多文件条目抽查首尾两个文件（只请求前 100 字节）。由此剔除了两项：ETH 2018 讲义返回 403，NBER 2008 幻灯片返回 404。除 PKU 外，其余抽查均为 200 或 206。

**WebSearch 检索词（节选）**：
- Dettling "Applied Time Series Analysis" script ETH；Gregory Plett ECE5550 Kalman notes；Eric Zivot Econ 584 notes；Kevin Sheppard Financial Econometrics Notes
- Joshua Chan Bayesian macroeconometrics notes；Dembo Stochastic Processes notes；"lecture notes" "time series" Oxford/Cambridge/Imperial/LSE/Warwick/Edinburgh
- conformal prediction lecture notes course；"deep learning for time series" course slides；renewable energy forecasting course DTU Pinson
- NPTEL Stochastic Hydrology / Applied Time-Series Analysis；Särkkä Aalto Bayesian filtering course；spatio-temporal statistics course notes
- change point detection lecture notes；probabilistic forecasting scoring rules course；Bayesian forecasting DLM course West Harrison
- 时间序列分析 讲义 课程 pdf；financial econometrics GARCH lecture notes；nonlinear / high-dimensional time series lecture notes
- prognostics RUL course；hydrology time series course；anomaly detection time series course；Hyndman ETC3550 slides
- 李东风 应用时间序列分析 备课笔记；PSU STAT 510；Takahama EPFL air pollution；Martin Haugh QRM time series
- stat.ethz.ch time series script；STAT 443 / STA457 notes；Stanford EE363 archive；van der Vaart Time Series notes
- Prado/West Bayesian time series course；hierarchical forecasting course；Pinson DTU 31761；Percival STAT 520；Gustafsson TSRT14
- particle filter / SMC course；TU Delft time series OCW；NBER "What's New in Econometrics" 2008；MATH4341 Durham

**直接浏览的官方页面（节选）**：
- MIT OCW：14.384、18.S096、6.262、16.322、12.864、6.011、2.160、6.435、6.436J、15.070J、18.650、6.041
- Berkeley：ryantibs/timeseries-f23、statlearn-s24、statlearn-s23；aditya Stat 153 S13；bartlett 153-fall2010
- ionides.github.io/531w25、531w24；af.numbat.space（Monash）；darrenjw.github.io/spatio-temporal；stat.ethz.ch 多个学期页与教学目录
- cs.runi.ac.il/~kipnis；bashtage.github.io（Sheppard）；rtavenar.github.io/x-dl4ts；laurentoudre.fr/ast.html；lancaster.ac.uk/~romano
- 02427/02417.compute.dtu.dk；mocha-java.uccs.edu/ECE5550；ida.liu.se SMC 2025；isy.gitlab-pages.liu.se TSRT14；users.aalto.fi/~ssarkka
- atmos.uw.edu/~dennis；faculty.washington.edu/ezivot；stat.cmu.edu/~cshalizi/dst；staff.fnwi.uva.nl/p.j.c.spreij；statslab.cam.ac.uk/~rrw1
- web.math.princeton.edu/~rvan；galton.uchicago.edu/~lalley；fleuret.org/dlc；sas.upenn.edu/~jesusfv；numeric.cs.unibuc.ro；bookdown.org/hefleyt2
- maths.dur.ac.uk/~jcr/DLM；ee363.stanford.edu/archive；martin-haugh.github.io；nworbmot.org/courses/es-22；sites.ualberta.ca/~kashlak；uio.no STK4060；people.duke.edu/~rnau

## 2. 纳入与排除决策

### 与书单（materials_books_seed_cn.json）去重

以下内容已在书单中，这里不重复计入：
- Cochrane《Time Series for Macroeconomics and Finance》（书单第 6 项）：已从本清单删除。
- Sheppard《Financial Econometrics Notes》（书单第 23 项）：本清单第 9 项只收同课程的两套幻灯片，cross_kind 中已注明。
- Särkkä《Bayesian Filtering and Smoothing》（书单第 2 项）：本清单第 17 项收的是 2012 年课程合订讲义，cross_kind 已注明二者内容有重叠。
- 《Elements of Sequential Monte Carlo》（书单第 31 项）：本清单第 16 项只收课程讲义与幻灯片。
- fpp3：Monash 课程（第 3 项）只收周幻灯片，cross_kind 已注明。

### 主要排除项

| 候选 | 排除原因 |
|---|---|
| ETH Meinshausen “Time Series Analysis” AS2018 整本讲义 TimeSeries2018.pdf | 课程页虽列出，但文件对外返回 403（疑似仅限校内），改用同系 HS2012 讲义（第 5 项） |
| NBER SI 2008 “What's New in Econometrics: Time Series”（Stock & Watson） | 程序页的 13 个 Slides 链接全部 404；NBER 新页面只有视频 |
| Suhasini Subba Rao（TAMU）“A course in Time Series Analysis” | 作者官方页 TLS 握手失败、无法核验；能找到的只有 Scribd、SlideShare 等第三方副本 |
| Dembo Stanford Stat 219 随机过程讲义 | 只有 Scribd 副本，没有官方托管 |
| Tsay（Chicago Booth Bus 41202 / 41910） | 旧课程页 404，新页面无讲义 |
| Hurvich（NYU Stern Forecasting）、Sigman（Columbia 随机过程）、Pollock（Leicester）、Bastani（UPenn CIS 7000 共形/不确定性） | 页面返回 403，无法核验 |
| NPTEL Stochastic Hydrology（IISc）/ Applied Time-Series Analysis（IIT Madras） | 只核验到课程大纲；讲义下载入口未能核实，第三方副本不收 |
| Pinson DTU 31761 Renewables in Electricity Markets | 以视频模块为主，没有完整讲义或幻灯片 |
| Liège ELEN0445 microgrids forecasting lessons 1-2 | 只是课程中的两讲，不是完整课程包 |
| DTU 02417 Time Series Analysis | 页面只列出部分讲次（缺第 4、7-9 讲），学期进行中 |
| DTU 02427 本学期幻灯片（含层级预测协调、多元概率预测评估讲次） | 学期进行中，逐周上传、尚未完整；只收课程完整讲义（第 14 项） |
| Stanford EE363 2026（Lall） | 学期进行中，页面注明幻灯片会陆续增加；改收 Boyd 2008-09 存档版（第 42 项） |
| CMU 36-467 Fall 2020 | 只有 HTML 幻灯片；2018 版是文字讲义，改收 2018 版（第 19 项） |
| ETH Dettling ATSA SS2020 及以后 | 讲义转入 Moodle，需登录 |
| KTH SF2943、Uppsala 深度时间序列、Ulm 非线性时间序列 | 讲义在 Canvas、Moodle 等需登录平台 |
| UBC/Waterloo STAT 443、USC STAT 720 等 | 能找到的多为学生自制笔记（非官方）；或官方列表页已迁移、无法核验 |
| Gneiting KIT “Forecasting: Theory and Praxis”、Chicago STAT 30810 高维时间序列、ENSAI 高维时间序列、UCSC AMS223（Prado） | 只有课程介绍，没有公开讲义 |
| Boniol 时间序列异常检测暑期课、Polimi 故障预测（Baraldi）、Linköping 预测性维护博士课 | 幻灯片未在页面列出、只有单讲，或页面无讲义 |
| Kunst（Vienna）各课程 | 现存课程页没有讲义 PDF |
| Bartlett Berkeley Stat 153 F2010 | 与第 2、44 项同属一门课，降为备选（第 51 项） |

## 3. 覆盖表（主题 → 排名）

| 覆盖主题 | 排名（主选；括号内为备选） |
|---|---|
| 概率、统计与随机过程基础 | 25, 32, 33, 34, 43, 48, 49（54） |
| 平稳性、自相关、谱分析、趋势/季节分解 | 1, 2, 3, 4, 5, 7, 8, 18, 19, 20, 21, 27, 28, 31, 37, 44（51, 57, 59, 60） |
| ARIMA、指数平滑、动态回归 | 1, 2, 3, 7, 8, 23, 26, 29, 44, 47 |
| 预测组合 | 无专讲（缺口） |
| 状态空间、Kalman 滤波、贝叶斯方法（含 DLM、粒子滤波、HMM） | 1, 4, 5, 6, 15, 16, 17, 24, 30, 32, 33, 36, 41, 42, 46（53） |
| 多变量、高维（因子/VAR）、非线性、波动率 | 6, 9, 12, 14, 22, 23, 26（52） |
| 机器学习、深度学习、时间序列基础模型 | 11, 12, 35 |
| 概率预测、预测区间、校准、不确定性 | 3, 10, 11, 22（55） |
| 非平稳、结构突变/变点、异常检测、缺失数据 | 6, 12, 13, 14, 23, 40 |
| 时空分析、面板、层级预测 | 4, 19, 39（58）；面板与层级预测为缺口 |
| 滚动评估、时间划分、泄露、可复现 | 3（精度评估与时间序列交叉验证）、29（估计期/验证期划分）；泄露与可复现无专讲 |
| 应用：金融 | 6, 9, 22, 23, 26, 36 |
| 应用：气候/大气/环境（空气、水质背景） | 4, 18, 31, 39 |
| 应用：能源 | 50（能源系统时间序列与可再生能源变率）、14（DTU 课程面向能源与环境） |
| 应用：工业、预测性维护、传感器 | 15, 30, 40, 41, 45 |

**缺口与建议**：以下主题没有找到合格的完整公开课程讲义，需靠书单或论文补齐：
- 预测组合
- 层级预测/预测协调：DTU 02427 本学期有专讲，但还在建设中
- 面板时间序列
- 数据泄露与可复现
- 专门的水文/水质、空气质量时间序列预测
- 能源负荷/新能源功率预测方法
- 剩余寿命（RUL）预测
- 中文课程：只有北大李东风的两份讲义，其中一份为备选

## 4. 建议的前 15 项

1. **#1 Michigan STATS 531（W25）**：从经典 ARMA 平滑过渡到 POMP/粒子滤波的主干课程。
2. **#2 Berkeley Stat 153（F23）**：面向预测的入门主线（ARIMA、ETS、谱分析）。
3. **#3 Monash ETC3550/5550**：预测实务、精度评估与时间序列交叉验证，配合 fpp3。
4. **#4 Durham MATH4341（Wilkinson 2026）**：时间序列、状态空间与时空统计合一的单 PDF 讲义。
5. **#6 MIT 14.384**：计量取向高级课，覆盖 VAR、因子模型、单位根、结构突变、Kalman 与贝叶斯。
6. **#10 Berkeley Stat 241B（S24）**：共形预测与校准/评分规则。
7. **#11 IP Paris Deep Learning for Time Series**：时间序列深度学习与基础模型。
8. **#12 ENS Paris-Saclay MVA ML for TS**：去噪、缺失插补、变点与异常检测等预处理“隐藏任务”。
9. **#13 Lancaster MATH337**：变点检测入门（CUSUM、PELT、WBS）。
10. **#15 UCCS ECE5550（Plett）**：工程版 Kalman/EKF/SPKF/粒子滤波全流程。
11. **#16 Linköping SMC 2025**：粒子滤波与粒子 MCMC 的完整课程。
12. **#17 Aalto Särkkä 2012 合订讲义**：贝叶斯滤波与平滑的统一推导。
13. **#14 DTU 02427 Madsen & Holst 讲义**：非线性与非平稳时间序列、递推估计。
14. **#18 UW ATM S 552（Hartmann）**：地学取向的谱分析、EOF、滤波与小波。
15. **#5 ETH HS2012 Skript**：理论型平稳过程、谱、Kalman 与 ARCH。

## 5. 年份分布（主选 50 项，按版本或学期年份）

| 年份区间 | 项数 | 排名 |
|---|---|---|
| 2023 年及以后 | 11 | 1, 2, 3, 4, 10, 12, 13, 16, 28, 30, 40 |
| 2018-2022 | 9 | 7, 9, 19, 27, 35, 37, 39, 43, 50 |
| 2010-2017 | 13 | 5, 6, 8, 17, 18, 20, 22, 25, 26, 34, 44, 48, 49 |
| 2010 年以前 | 11 | 14, 21, 23, 24, 31, 32, 33, 41, 42, 45, 46 |
| 年份待核实 | 6 | 11, 15, 29, 36, 38, 47 |

说明：第 14 项按讲义版本年份（2006）计入“2010 年以前”，但它是 DTU 2026 秋季课程正在使用的教材。第 35 项版本年份待核实，按“EPFL 讲授至 2022”计入 2018-2022。

2023 年后的主选仍偏少：很多顶校课程把新讲义放进 Canvas、Moodle 等需登录平台。较早的经典材料都在 classic_reason 中写明了保留理由。

**语言**：英文 57 项、中文 2 项（第 38、52 项）、德文 1 项（第 57 项，备选）。

**格式**：
- 主选：multi_pdf 33 项、pdf 13 项、html 4 项（第 19、29、39、47 项）。
- 备选：pdf 6 项、multi_pdf 3 项、html 1 项（第 52 项）。
- 全清单 html 共 5 项。

## 6. 存疑条目

| 排名 | 存疑点 |
|---|---|
| 3 | Monash 页面未写年份；按周次日期和抓取时间判断为 2026 年第 2 学期，待核实 |
| 5 | 讲义作者（Künsch）、版本日期（2011 年 8 月）与语言都来自检索摘要，待下载核对；课程目录归属 Bühlmann HS2012 |
| 7 | Kipnis STATS 207 的具体学期只来自 ExploreCourses 链接参数（2020-21 学年） |
| 11 | Tavenard 课程的学期/年份不明 |
| 15 | Plett 课程的学期不明 |
| 35 | Fleuret 讲义版本年份不明 |
| 36 | 讲授学期不明 |
| 14 | 讲义版本年份取自文件名（2006），页面写作 2001 |
| 17 | 2012 年课程编号与课程全名待核实（2011 年同名课程为 MAT-55216） |
| 18 | ATM S 552 课程全名待核实 |
| 24 | ORF 557 讲义在作者主页上的条目目前被 HTML 注释隐藏；目录页与文件仍公开可访问 |
| 28 | Oslo STK4060 页面只列 6 份讲义，是否覆盖全部课次需下载核对 |
| 30 | TSRT14 的学期取自课程信息页（VT2 2024），不确定是否为最新学期 |
| 38、52 | 北大站点 TLS 证书链不完整：WebFetch 与直连都无法打开，只靠检索结果确认 URL 在官方域名下。下载时可能需要处理证书问题（勿关闭校验，建议人工确认） |
| 47 | PSU STAT 510 同样有证书问题，html_chapters 未能清点（填 0） |
| 46 | Durham DLM 讲义页面缺 dlm10，疑似不完整 |
| 22 | 页面注明 2016 年未讲到时间序列与 EVT 两章，但讲义已全部给出 |
| 1 | 第 12-16、18 章的 notes.pdf 由课程页链接至合作课程站 kingaa.github.io/sbied |
| 57、58 | 作者与语言据目录归属判断，待核实（第 58 项语言待核实） |
