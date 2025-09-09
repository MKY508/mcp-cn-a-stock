# 部署指南 - ChatGPT Pro MCP 连接器

## 方案对比

| 方案 | 优点 | 缺点 | 费用 |
|------|------|------|------|
| GitHub Codespaces | 简单快速，GitHub 集成 | 有免费额度限制 | 免费额度后收费 |
| ngrok | 本地运行，即时生效 | 需要保持电脑开启 | 免费/付费 |
| Railway | 一键部署，永久运行 | 需要配置环境 | $5/月起 |
| Render | 免费套餐可用 | 免费版有限制 | 免费/$7/月 |

## 方案 1: GitHub Codespaces（推荐）

### 步骤：
1. Fork 或上传代码到 GitHub
2. 在仓库页面点击 "Code" → "Codespaces" → "Create codespace"
3. 等待环境启动
4. 在终端运行：
   ```bash
   python main.py --transport=sse --port 8000
   ```
5. 点击 "Ports" 标签，将 8000 端口设为 Public
6. 复制生成的 URL（格式：`https://xxx-8000.app.github.dev`）

### ChatGPT Pro 配置：
- URL: `https://你的codespace名-8000.app.github.dev/cnstock/sse/`

## 方案 2: 使用 ngrok（快速测试）

### 步骤：
1. 安装 ngrok：
   ```bash
   brew install ngrok
   ```

2. 启动本地服务器：
   ```bash
   cd mcp-cn-a-stock-main
   source .venv/bin/activate
   python main.py --transport=sse --port 8000
   ```

3. 新开终端，启动 ngrok：
   ```bash
   ngrok http 8000
   ```

4. 复制 ngrok 提供的 HTTPS URL

### ChatGPT Pro 配置：
- URL: `https://xxx.ngrok-free.app/cnstock/sse/`

## 方案 3: 部署到 Railway

### 步骤：
1. 创建 `railway.toml`：
   ```toml
   [build]
   builder = "nixpacks"
   buildCommand = "pip install -r requirements.txt"

   [deploy]
   startCommand = "python main.py --transport=sse --port $PORT"
   ```

2. 在 Railway.app 创建新项目
3. 连接 GitHub 仓库
4. 自动部署完成后获取 URL

### ChatGPT Pro 配置：
- URL: `https://你的app.railway.app/cnstock/sse/`

## 方案 4: 部署到 Render

### 步骤：
1. 创建 `render.yaml`：
   ```yaml
   services:
     - type: web
       name: mcp-cn-stock
       runtime: python
       buildCommand: pip install -r requirements.txt
       startCommand: python main.py --transport=sse --port $PORT
       envVars:
         - key: MSD_HOST
           value: 82.156.17.205
   ```

2. 在 Render.com 创建新服务
3. 连接 GitHub 仓库
4. 部署完成后获取 URL

### ChatGPT Pro 配置：
- URL: `https://你的app.onrender.com/cnstock/sse/`

## 在 ChatGPT Pro 中添加连接器

1. 打开 ChatGPT Pro
2. 点击头像 → Settings → Connectors
3. 滚动到底部，点击 "Add custom connector"
4. 输入你的 MCP 服务器 URL
5. 启用 Deep Research 模式
6. 测试搜索功能：输入 "search for 茅台"

## 注意事项

1. **必须使用 HTTPS**：ChatGPT Pro 只接受 HTTPS 连接
2. **端口必须公开**：确保防火墙允许访问
3. **工具要求**：必须包含 `search` 和 `fetch` 工具
4. **Deep Research 模式**：只在此模式下可用

## 故障排除

### 连接失败
- 检查 URL 是否正确（包含 `/cnstock/sse/`）
- 确认服务器正在运行
- 验证端口是否公开访问

### 工具不可用
- 确认已添加 `search` 和 `fetch` 工具
- 检查服务器日志是否有错误

### 数据为空
- 检查 `.env` 文件配置
- 确认 `MSD_HOST` 设置正确
- 验证 markets.json 文件存在