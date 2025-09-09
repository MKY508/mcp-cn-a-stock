# A股 ETF 数据仓库 - ChatGPT 原生 GitHub 连接器

📊 自动获取A股ETF数据，供 ChatGPT Pro 原生 GitHub 连接器直接读取分析。

## 🚀 快速开始

### 1. Fork 这个仓库
点击右上角 Fork 按钮，将仓库复制到你的账号下。

### 2. 启用 GitHub Actions
- 进入你 Fork 的仓库
- 点击 Actions 标签
- 点击 "I understand my workflows, go ahead and enable them"

### 3. 手动触发首次数据获取
- Actions → Fetch A-Share ETF Data → Run workflow
- 等待约2-3分钟完成

### 4. 在 ChatGPT Pro 中连接
- ChatGPT → Settings → Connectors
- 连接 GitHub（原生连接器）
- 授权访问你的仓库

## 📁 数据结构

```
/
├── codes.csv           # ETF代码列表
├── signals.csv         # 汇总信号数据（所有ETF）
├── orders.csv          # 订单模板（供ChatGPT写入）
├── data/
│   ├── 510300.csv     # 沪深300历史数据
│   ├── 510880.csv     # 红利ETF历史数据
│   └── ...            # 其他ETF数据文件
└── last_update.txt    # 最后更新时间
```

## 💬 在 ChatGPT 中使用

直接发送以下提示词：

```
任务：分析 GitHub 仓库 MKY508/mcp-cn-a-stock 中的 A股ETF数据

读取数据：
1. 读取 codes.csv 获取ETF列表
2. 读取 signals.csv 或 data/*.csv 获取历史价格

计算指标：
1. 计算60日和120日收益率（r60, r120）
2. 计算综合得分：Score = 0.6×r60 + 0.4×r120
3. 计算20日ATR和200日均线
4. 分析相关性矩阵（90日对数收益）

输出：
1. 动量排名 Top 10
2. 相关性 ≤ 0.8 的最优组合
3. 生成交易建议（考虑流动性 ≥ 2亿元/日）
```

## 📊 可用数据字段

每个 CSV 文件包含以下字段：
- **code**: ETF代码
- **date**: 交易日期
- **open**: 开盘价
- **high**: 最高价
- **low**: 最低价
- **close**: 收盘价
- **volume**: 成交量（手）
- **amount**: 成交额（元）

## 🔄 自动更新

- **更新时间**: 每个工作日 16:10（北京时间）
- **数据来源**: 东方财富（akshare）
- **历史深度**: 260个交易日

## 📝 自定义ETF列表

编辑 `codes.csv` 文件，添加或删除ETF代码：

```csv
code,name
510300,沪深300
510880,红利ETF
...
```

## 🎯 示例分析任务

### 动量策略分析
```
基于 MKY508/mcp-cn-a-stock 仓库数据：
1. 计算所有ETF的60日和120日动量
2. 筛选动量得分前10名
3. 分析它们的相关性
4. 推荐低相关性组合
```

### 趋势判断
```
使用 MKY508/mcp-cn-a-stock 的 510300.csv：
1. 计算沪深300的200日均线
2. 判断当前趋势（ABOVE/BELOW）
3. 计算ATR波动率
4. 给出市场状态评估
```

### 资产配置
```
读取 MKY508/mcp-cn-a-stock 所有ETF数据：
1. 按行业分类（半导体、新能源、金融等）
2. 计算各行业动量和波动率
3. 构建分散化组合
4. 考虑流动性约束（日成交额>2亿）
```

## ⚙️ 技术细节

- **Python 3.11** + akshare + pandas
- **GitHub Actions** 自动化数据更新
- **原生 GitHub 连接器** 兼容
- **无需服务器** 纯 GitHub 托管

## 🛠️ 故障排除

### 数据未更新？
1. 检查 Actions 是否启用
2. 查看 Actions 运行日志
3. 确认 akshare API 正常

### ChatGPT 读取失败？
1. 确认 GitHub 连接器已授权
2. 检查仓库名称是否正确
3. 尝试指定具体文件路径

## 📜 许可证

MIT License - 自由使用和修改

---

💡 **提示**: Star ⭐ 这个仓库以便快速找到它！