# A股个股三维深度分析工具包

看板 + 批量报告生成器，覆盖 11 只 A 股个股的「基本面 / 新闻面 / 资金面」三维分析。

## 在线预览

- 仓库：https://github.com/ranaeolus/stock-analysis-reports
- 看板（GitHub Pages）：https://ranaeolus.github.io/stock-analysis-reports/

> 提示：直接点开 GitHub 上的 `index.html` 看到的是源码；要看渲染后的页面请走上面的 Pages 链接，或把仓库 clone 到本地用浏览器打开。

## 目录结构

- `index.html` — 看板首页：11 只个股卡片总览，支持一键刷新实时行情、动态添加股票（存 localStorage）、拖拽排序，**卡片右上角 ✕ 可删除该股票**。
- `stock_viewer.html` — 动态报告页：通过 `?code=xxx&market=SH/SZ` 实时调用东方财富接口生成报告。
- `generate_reports.py` — 批量生成三维深度分析报告（综合评分环形图、估值区间测算、风险提示、最新一周新闻板块）。
- `news_data.json` — 新闻板块单一数据源，按股票代码索引，包含「本周综述」与若干条带情绪标签（利好/中性/利空）的关键新闻分析。
- `_add_flow_klines.py` — 资金流 kline 数据注入辅助脚本。
- `*/_三维深度分析报告/` — 11 份预生成报告，每只个股一份独立 HTML；每份报告在「风险提示」下方新增「最新一周动态与关键新闻分析」板块。

## 使用方法

1. 直接用浏览器打开 `index.html` 查看看板总览；
2. 点「🔄 刷新实时行情」可拉取东财实时行情与资金流（A 股习惯：**涨红跌绿**）；
3. 看板卡片右上角 `✕` 删除某只股票：删除记录存于 localStorage，**刷新后不再显示**；如需恢复，清除本站 localStorage 数据即可；
4. 重新生成全部报告：运行 `python generate_reports.py`（报告输出到 `个人产出` 目录）；
5. 动态查看某只股票：浏览器打开 `stock_viewer.html?code=600000&market=SH`。

## 数据说明

- 财务 / 新闻为定期快照（财务截至 2026-07-08；新闻板块汇总截至 2026-07-22 当周），行情与资金流支持实时刷新。
- 报告载入后约 0.5 秒自动拉取一次实时数据；即使接口被限流，刷新按钮也会自动恢复可点。
- 新闻板块内容由 `news_data.json` 驱动；要更新某只股票的新闻，直接编辑该 JSON 对应代码下的 `summary` 与 `items`，再重跑 `generate_reports.py` 即可。

## 已知细节

- 资金面「今日主力净流入（盘中）」KPI 与下方「每日数据」表首行同源，刷新后必然一致。
- `generate_reports.py` 内置 10 只股票，「工业富联(601138)」报告为单独生成，如需重跑脚本请自行补入。
- 删除看板股票仅影响本地 `index.html` 的展示（基于 localStorage），不会改动预生成的报告文件或仓库中的股票清单。

## 贡献

欢迎 Fork / PR，一起完善分析维度与数据源。
