# MCP CN A-Stock Server for ChatGPT Pro

这是一个为 ChatGPT Pro 提供 A 股数据的 MCP (Model Context Protocol) 服务器。

## 功能特性

- 🔍 **search**: 搜索股票代码和名称
- 📊 **fetch**: 获取股票详细信息
- 📈 **brief**: 获取股票基本信息和行情数据
- 📉 **medium**: 获取基本数据和财务数据
- 📊 **full**: 获取所有数据和技术指标

## 快速部署

### 方案 1: 使用 GitHub Codespaces（推荐）

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/YOUR_GITHUB_USERNAME/mcp-cn-a-stock)

1. 点击上面的按钮创建 Codespace
2. 等待环境启动完成
3. 在终端运行：`python main.py --transport=sse --port=8000`
4. 将端口 8000 设为 Public
5. 复制生成的 URL

### 方案 2: 部署到 Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/YOUR_GITHUB_USERNAME/mcp-cn-a-stock)

1. 点击上面的按钮
2. 按照提示完成部署
3. 获取部署后的 URL

### 方案 3: 本地运行 + ngrok

```bash
# 克隆仓库
git clone https://github.com/YOUR_GITHUB_USERNAME/mcp-cn-a-stock.git
cd mcp-cn-a-stock

# 安装依赖
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 启动服务器
python main.py --transport=sse --port=8000

# 新开终端，使用 ngrok 暴露到公网
ngrok http 8000
```

## 在 ChatGPT Pro 中配置

1. 打开 ChatGPT Pro
2. 进入 Settings → Connectors
3. 点击 "Add custom connector"
4. 输入你的服务器 URL：
   - Codespaces: `https://[your-codespace]-8000.app.github.dev/cnstock/sse/`
   - Render: `https://[your-app].onrender.com/cnstock/sse/`
   - ngrok: `https://[your-id].ngrok-free.app/cnstock/sse/`
5. 保存并启用

## 使用方法

在 ChatGPT Pro 中启用 Deep Research 模式，然后可以：

- 搜索股票：`search for 茅台`
- 获取详情：`fetch SH600519`
- 查询信息：`分析贵州茅台的走势`

## 环境变量

- `MSD_HOST`: 数据源地址（默认：82.156.17.205）
- `STOCK_TO_SECTOR_DATA`: 股票板块数据文件路径

## 技术栈

- Python 3.12+
- MCP (Model Context Protocol)
- FastMCP
- TA-Lib
- SSE (Server-Sent Events)

## 许可证

MIT License