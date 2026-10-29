# 下载与解压恢复说明（时间序列文献库，2026-10-29）

本资料库按“轻量 Git 分支 + Release 全文附件”的方式发布：

- **Git 分支 `release-lite-20261029`**：只包含总目录、各领域目录与阅读路线（`domains/`）、脚本与检索记录（`scripts/`）、报告和本说明，不含 PDF 全文、书籍和课程讲义。仓库原有的 `main` 分支没有改动。
- **Release `ts-full-20261029`**：3 个独立的不压缩 `.tar` 包，合起来就是完整的资料库，包括全部论文、书籍、课程讲义、目录、报告和脚本。

Release 页面：https://github.com/feng199506/time-series/releases/tag/ts-full-20261029

## 1. 包列表

| 包文件名 | 内容范围（按路径顺序） |
|---|---|
| `time_series_20261029_batch001_cn_en.tar` | 顶层目录与报告、`domains/`、`scripts/`、`books/`（全部书籍）、`pdfs/`（至 2024_Olsson_MultiModelEnsembleBaseline） |
| `time_series_20261029_batch002_cn_en.tar` | `pdfs/`（2024_Oskarsson … 2026_Gupta） |
| `time_series_20261029_batch003_cn_en.tar` | `pdfs/` 剩余部分、`pending_pdfs/`、`university_materials/`（全部课程讲义） |

每个文件属于哪个包，见 `archive_index_cn.csv`（UTF-8 带 BOM，可直接用 Excel 打开；1,254 行）。表中列出包文件名、批次、相对路径、类型和字节数。

- 每个包都可以**单独解压**，不需要拼接。只要某几类资料时，可以只下载对应的包。
- 各包之间**没有重复文件**，解压到同一目录时不会互相覆盖。
- 包未压缩，解压很快，所需磁盘空间约等于包的大小。全部解压约需 **4.3 GiB**，建议预留 6 GiB。

## 2. Windows：浏览器下载

1. 打开上面的 Release 页面，展开 **Assets**。
2. 依次点击 3 个 `.tar` 文件，以及 `archive_index_cn.csv`、`download_restore_cn.md`、`upload_report_cn.md`，全部保存到**同一个下载文件夹**，例如 `D:\下载\ts\`。
3. 单个包最大约 1.5 GB。浏览器提示“是否保留”时选择保留。下载中断可在浏览器下载列表里点“恢复”或重新下载。
4. 对照 `upload_report_cn.md` 中的字节数，在文件属性里核对每个包的大小（属性窗口里看“大小”的字节数，不要看“占用空间”）。

## 3. Windows：WinRAR 解压（全部解压到同一个目标目录）

请使用 **WinRAR 6 或更新版本**，目标目录用短路径，例如 `D:\ts\`。

**方法 A：一次批量解压（推荐）**

1. 在下载文件夹中，按住 Ctrl 选中全部 3 个 `.tar` 文件。
2. 右键 → **WinRAR → 解压文件…**（Extract files…）。
3. “目标路径”填 `D:\ts\`。
4. **不要**勾选“解压到单独的文件夹 / 在子文件夹中解压”（Extract archives to subfolders）。
5. 确定。所有包会解压到同一个 `D:\ts\` 下，恢复出完整的目录结构：

```
D:\ts\
├─ README_cn.md、catalog_cn.csv、final_report_cn.md、systematic_reading_guide_cn.md、checksums_en.sha256 …
├─ books\
├─ domains\
├─ pdfs\
├─ pending_pdfs\
├─ scripts\
└─ university_materials\
```

**方法 B：逐个解压**

对每个 `.tar` 文件：右键 → WinRAR → **解压文件…** → 目标路径都填同一个 `D:\ts\` → 确定。

注意：不要用“解压到 time_series_20261029_batch00X_cn_en\”这个菜单项，它会给每个包各建一个子文件夹，目录结构就被拆散了。

### Windows 文件名兼容

已逐个检查：全部文件名都不含 Windows 不允许的字符，同一目录下没有仅大小写不同的文件，最长相对路径 134 个字符。发布包中的文件与原件逐字节相同，没有改名。书籍和课程讲义里的 5 个 `.zip` 离线网页包，内部文件名也检查过，同样没有问题。

### 离线网页包（.zip）

少数官方 HTML 教材和讲义是整站保存的 `.zip` 离线包：`books/files/` 下 1 个，`university_materials/files/` 下 4 个。解压 tar 后，右键 zip → WinRAR → **解压到 “文件名\”**，再用浏览器打开其中的页面。

## 4. Linux / macOS

```bash
mkdir -p ~/ts
for f in time_series_20261029_batch*_cn_en.tar; do tar -xf "$f" -C ~/ts || echo "FAILED: $f"; done
```

（macOS 自带 bsdtar，同样支持此格式。）

## 5. 资料状态说明（来自资料库自身的目录，与打包无关）

- **只按已核验全文计数**：各领域与总目录中的数量，都只计已下载并核验通过的全文。`pending_pdfs/` 中的 11 个 PDF 是已下载、但还没有通过全部核验的论文。它们一并打包，但不计入数量，需要人工复核。
- **课程讲义**：`PennStateUniversityD_STAT510_NA_html_en.zip` 离线包不完整（没有保存到页面），目录中已标为“待核验（不计入）”。
- **书籍 49/50**：Svetunkov《ADAM》的官方 HTML 离线包在打包时仍在抓取，没有收进这次的发布包。
- 本次按 2026-10-29 18:58（中欧时间）的资料库内容打包。打包前先把整个资料库复制成一份快照，打包用的就是这份快照。之后资料库再有改动，不会进入这次发布。

## 6. 完整性说明

- 本次发布只登记了上传状态（以 GitHub API 显示附件为 `uploaded`、远端大小等于本地大小为准），**没有**做下载回验和哈希校验。
- 解压后的根目录有 `checksums_en.sha256`，这是资料库生成的 SHA-256 清单，与原件完全相同，列出了 1,135 个论文、书籍和讲义文件。需要时可以自行核对，例如在 Linux 上运行 `sha256sum -c checksums_en.sha256`。
- 资料库中的全部文件都已打包，没有排除任何资料文件（资料库目录里的本地 `.git/` 不属于资料内容，未打包）。
