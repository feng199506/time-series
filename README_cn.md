# 时间序列分析与预测文献库

本目录收集时间序列分析与预测的论文和系统学习资料，只做文献收集与核验，不训练模型、不复现实验。属于初步范围检索，不宣称穷尽，也不是系统综述。

- 检索执行日：2026-10-29（UTC/CET 同日）
- 论文时间窗口：首次公开日期在 2023-10-29 至 2026-10-29 之间。arXiv 论文取 v1 提交日；期刊论文取 Crossref 在线、印刷、posted、created 日期中最早的一个；若 Crossref 登记了预印本或讨论稿（如 Copernicus），取其日期。
- 计数规则：只计“原文全文 PDF 已下载并核验通过”的条目。候选、仅链接、下载失败、待核验、下载错文献一律不计。

## 总进度（脚本自动生成）

<!-- PROGRESS:START -->
| 分类 | 进度 | 主分类 | 独有 | 跨类 | 近三年占比 | 三年前 | 状态 |
|---|---|---|---|---|---|---|---|
| [通用方法](domains/01_general_methods/) | 已核验全文 73 / 目标约 50；待核验 1；下载失败 0。 | 58 | 57 | 16 | 68/73（93.2%） | 5 | 达标 |
| [金融](domains/02_finance/) | 已核验全文 55 / 目标约 50；待核验 2；下载失败 0。 | 49 | 46 | 9 | 53/55（96.4%） | 2 | 达标 |
| [空气质量](domains/03_air_quality/) | 已核验全文 51 / 目标约 50；待核验 2；下载失败 13。 | 50 | 42 | 9 | 50/51（98.0%） | 1 | 达标 |
| [水质](domains/04_water_quality/) | 已核验全文 50 / 目标约 50；待核验 0；下载失败 22。 | 50 | 39 | 11 | 50/50（100.0%） | 0 | 达标 |
| [气象与气候](domains/05_weather_climate/) | 已核验全文 66 / 目标约 50；待核验 2；下载失败 4。 | 41 | 35 | 31 | 64/66（97.0%） | 2 | 达标 |
| [能源与电力](domains/06_energy_power/) | 已核验全文 56 / 目标约 50；待核验 2；下载失败 1。 | 45 | 26 | 30 | 53/56（94.6%） | 3 | 达标 |
| [水文与水资源](domains/07_hydrology/) | 已核验全文 50 / 目标约 50；待核验 0；下载失败 1。 | 50 | 46 | 4 | 46/50（92.0%） | 4 | 达标 |
| [交通与出行](domains/08_transport/) | 已核验全文 51 / 目标约 50；待核验 1；下载失败 0。 | 47 | 42 | 9 | 49/51（96.1%） | 2 | 达标 |
| [工业与设备](domains/09_industrial/) | 已核验全文 50 / 目标约 50；待核验 1；下载失败 2。 | 46 | 40 | 10 | 50/50（100.0%） | 0 | 达标 |
| [医疗与公共卫生](domains/10_health/) | 已核验全文 50 / 目标约 50；待核验 2；下载失败 5。 | 48 | 45 | 5 | 48/50（96.0%） | 2 | 达标 |

全库去重：已核验论文 484 篇，已核验 PDF 文件 484 个；待核验 11；下载失败 41（均不计入）。

| 学习资料 | 进度 | 年份分布（已核验） | 格式 |
|---|---|---|---|
| [大学课程教材与完整讲义](university_materials/) | 已核验 50 / 目标约 50；待核验 2；下载失败 9。 | 2023 及以后: 16；2010–2017: 13；2018–2022: 9；年份待核实: 5；2009 及以前: 7 | 多文件 PDF 讲义包: 35；PDF: 12；官方 HTML 离线包（zip）: 3 |
| [教科书、专著与参考书](books/) | 已核验 49 / 目标约 50；待核验 2；下载失败 4。 | 2018–2022: 17；2023 及以后: 13；2009 及以前: 5；2010–2017: 9；年份待核实: 5 | 官方 HTML 离线包（zip）: 1；PDF: 48 |
<!-- PROGRESS:END -->

各列含义：
- **进度**：该类已核验全文数，包含交叉标注计入的论文。
- **主分类**：以该类为主分类的已核验数。
- **独有**：只属于该类的已核验数。
- **跨类**：同时属于两个或以上分类的已核验数。

近三年占比和三年前数量都以已核验全文为分母。

## 目录结构

| 路径 | 内容 |
|---|---|
| [catalog_cn.csv](catalog_cn.csv) | 全库总目录：论文和学习资料，用“资料类型”列区分 |
| [download_failures_cn.csv](download_failures_cn.csv) | 论文的下载失败、仅链接与待核验条目（均不计入） |
| [checksums_en.sha256](checksums_en.sha256) | 所有已核验文件的 SHA256，可在本目录执行 `sha256sum -c checksums_en.sha256` |
| [search_log_cn.md](search_log_cn.md) | 检索平台、检索词、筛选原则、排除记录与执行日志 |
| [final_report_cn.md](final_report_cn.md) | 本轮最终报告：分领域统计、覆盖与缺口、优先阅读、未解决问题 |
| [systematic_reading_guide_cn.md](systematic_reading_guide_cn.md) | 系统阅读指南：入门、理论、现代方法、应用四条路线与核心书单 |
| [domains/](domains/) | 10 个分类各一个子目录，内含 `catalog_cn.csv` 与 `reading_map_cn.md` |
| [university_materials/](university_materials/) | 大学课程教材与完整讲义：`catalog_cn.csv`、`reading_map_cn.md`、`files/` |
| [books/](books/) | 教科书、专著与参考书：`catalog_cn.csv`、`reading_map_cn.md`、`files/` |
| [pdfs/](pdfs/) | 已核验论文 PDF，去重后每篇一份，命名为 `首次公开年份_第一作者_短标题_语言.pdf` |
| `pending_pdfs/` | 已下载但未通过全部核验的论文 PDF（不计入，需人工复核） |
| [scripts/](scripts/) | 本轮实际使用的脚本、种子名单、元数据缓存和结果记录 |

10 个分类：

| 编号 | 子目录 | 分类 |
|---|---|---|
| 01 | `01_general_methods` | 通用方法 |
| 02 | `02_finance` | 金融 |
| 03 | `03_air_quality` | 空气质量 |
| 04 | `04_water_quality` | 水质 |
| 05 | `05_weather_climate` | 气象与气候 |
| 06 | `06_energy_power` | 能源与电力 |
| 07 | `07_hydrology` | 水文与水资源 |
| 08 | `08_transport` | 交通与出行 |
| 09 | `09_industrial` | 工业与设备 |
| 10 | `10_health` | 医疗与公共卫生 |

每篇论文有一个主分类，可带多个交叉分类，交叉分类须有摘要层面的依据。跨类论文只保存一份 PDF，通过统一编号（TSxxx）在各分类目录中引用。学习资料的编号为 UMxxx（大学讲义）和 BKxxx（书籍）。

文件命名规则：所有自建、下载和交付的文件都在扩展名前标注语言，英文 `_en`、中文 `_cn`、中英双语 `_cn_en`。HTML 教材的离线 zip 包内部保留原站点路径，以保证页面链接可用。

## 核验标准

### 论文（`scripts/download_papers_en.py`）
一篇论文要计入，必须同时满足：
- HTTP 200，文件完整保存（与 Content-Length 一致），以 `%PDF-` 开头，pypdf 可解析；
- 是全文：至少 4 页、至少 12,000 字符，含参考文献节，且不是补充材料；
- 前几页能找到题名（arXiv 版与期刊版题名任一匹配均可，词匹配率 ≥ 0.8）和第一作者姓氏（含 ü→ue 等转写）；
- 登记了原始来源、下载版本、本地路径和 SHA256。

下载前，先把种子题名与 arXiv/Crossref/OpenAlex 返回的题名比对，防止标识符错误。

### 学习资料（`scripts/download_materials_en.py`）
- 一本书或一套完整课程讲义计一次。多文件讲义包须全部文件下载成功并可解析。
- 单一 PDF 须达到页数下限，并在前 6 页中找到题名与作者或教师；同时提取 PDF 书签作为“已检查目录”。
- 官方 HTML 教材整站保存为 zip 离线包，须检查页面数、缺失页和资源缺失率。
- “已核验”只表示检查了完整性、目录和身份，不表示已精读。

## 执行与续跑

宿主机没有 pip/venv。先把 pypdf 纯 Python wheel 解压到本目录之外：

```bash
cd /root/time_series_literature
LIB=/tmp/tsl_pylib; STAGE=/tmp/tsl_staging
mkdir -p "$LIB" && curl -sSL -o /tmp/pypdf-5.1.0.whl \
  https://files.pythonhosted.org/packages/04/fc/6f52588ac1cb4400a7804ef88d0d4e00cfe57a7ac6793ec3b00de5a8758b/pypdf-5.1.0-py3-none-any.whl
echo "3bd4f503f4ebc58bae40d81e81a9176c400cbbac2ba2d877367595fb524dfdfc  /tmp/pypdf-5.1.0.whl" | sha256sum -c \
  && python3 -I -c "import zipfile; zipfile.ZipFile('/tmp/pypdf-5.1.0.whl').extractall('$LIB')"
```

论文部分：

```bash
python3 -I scripts/merge_seeds_en.py .            # 合并各分类种子，分配/保持统一编号并去重
python3 -I scripts/fetch_metadata_en.py .         # arXiv / Crossref / OpenAlex / 出版方页面元数据（有缓存，可续跑）
python3 -I scripts/verify_venues_en.py .          # 用官方论文集索引页核验会议渠道
python3 -I scripts/download_papers_en.py . "$STAGE" "$LIB"           # 逐类下载核验到目标数，失败自动用备选补位
#   可选参数：--only 04_water_quality  --target 50  --retry-reasons 'truncated'
python3 -I scripts/make_top10_en.py .             # 由检索笔记生成各类优先阅读清单
```

学习资料与汇总：

```bash
python3 -I scripts/download_materials_en.py . "$STAGE" "$LIB" --kind book     # 或 --kind course
python3 -I scripts/build_materials_en.py .        # 讲义/书籍目录与阅读路线
python3 -I scripts/build_catalog_en.py .          # 全库目录、分类目录、失败清单、校验清单、本 README 进度表
sha256sum -c checksums_en.sha256
```

续跑说明：
- 所有步骤都可断点续跑：已核验、待核验、已失败的条目不会重复请求；只有用 `--retry-failed` 或 `--retry-reasons` 显式指定时才重试。
- 请求限速由 `scripts/ratelimit_en.py` 跨进程统一控制：arXiv 至少间隔 4 秒，其他主机至少 3 秒，每个 URL 最多尝试 3 次。
- 遇到 401/402/403/404/451 立即放弃，不重试。
- 不绕过付费墙、登录、验证码或机器人检测（包括 Cloudflare 挑战页）。

新增文献或资料的方法：在 `scripts/seeds/` 对应的种子文件里追加条目，排名续排，然后按上述顺序重跑。
