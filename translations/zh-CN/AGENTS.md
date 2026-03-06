# AGENTS.md

## 项目概述

本仓库包含“初学者 AI 代理” —— 一个全面的教育课程，教授构建 AI 代理所需的所有知识。课程包含超过15节课，涵盖基础知识、设计模式、框架以及 AI 代理的生产部署。

**关键技术：**
- Python 3.12+
- 用于交互式学习的 Jupyter 笔记本
- AI 框架：微软代理框架 (MAF)
- Azure AI 服务：Microsoft Foundry，Azure AI Foundry Agent Service V2

**架构：**
- 基于章节的结构（00-15+ 文件夹）
- 每节课包含：README 文档、代码示例（Jupyter 笔记本）和图片
- 通过自动翻译系统支持多语言
- 每节课一个使用微软代理框架的 Python 笔记本

## 安装命令

### 先决条件
- Python 3.12 或更高版本
- Azure 订阅（用于 Azure AI Foundry）
- 安装并登录 Azure CLI（`az login`）

### 初始化设置

1. **克隆或分叉仓库：**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # 或
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **创建并激活 Python 虚拟环境：**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # 在 Windows 上：venv\Scripts\activate
   ```

3. **安装依赖项：**
   ```bash
   pip install -r requirements.txt
   ```

4. **设置环境变量：**
   ```bash
   cp .env.example .env
   # 使用您的API密钥和端点编辑.env
   ```

### 必需的环境变量

对于 **Azure AI Foundry**（必需）：
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry 项目端点
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - 模型部署名称（例如 gpt-4o）

对于 **Azure AI Search**（第 05 课 - RAG）：
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search 端点
- `AZURE_SEARCH_API_KEY` - Azure AI Search API 密钥

认证：运行笔记本前请先运行 `az login`（使用 `AzureCliCredential`）。

## 开发工作流

### 运行 Jupyter 笔记本

每节课包含多个不同框架的 Jupyter 笔记本：

1. **启动 Jupyter：**
   ```bash
   jupyter notebook
   ```

2. **导航到某节课程目录**（例如 `01-intro-to-ai-agents/code_samples/`）

3. **打开并运行笔记本：**
   - `*-python-agent-framework.ipynb` - 使用微软代理框架（Python）
   - `*-dotnet-agent-framework.ipynb` - 使用微软代理框架（.NET）

### 使用微软代理框架

**微软代理框架 + Azure AI Foundry：**
- 需要 Azure 订阅
- 使用 `AzureAIProjectAgentProvider` 连接 Agent Service V2（代理可在 Foundry 门户中查看）
- 生产级，内置可观察性
- 文件模式：`*-python-agent-framework.ipynb`

## 测试说明

这是一个教学仓库，包含示例代码而非带自动化测试的生产代码。验证你的设置和更改：

### 手动测试

1. **测试 Python 环境：**
   ```bash
   python --version  # 应该是3.12及以上
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **测试笔记本执行：**
   ```bash
   # 将笔记本转换为脚本并运行（测试导入）
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **验证环境变量：**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### 运行单个笔记本

在 Jupyter 中打开笔记本，按顺序执行代码单元。每个笔记本自包含，包括：
- 导入语句
- 配置加载
- 示例代理实现
- 预期输出的 markdown 单元

## 代码风格

### Python 规范

- **Python 版本**：3.12+
- **代码风格**：遵循 Python 标准 PEP 8 规范
- **笔记本**：使用清晰的 markdown 单元解释概念
- **导入顺序**：标准库、第三方库、本地导入分组

### Jupyter 笔记本规范

- 在代码单元前添加描述性 markdown 单元
- 在笔记本中添加输出示例作为参考
- 使用与课程概念匹配的清晰变量名
- 保持笔记本执行顺序线性（单元1→2→3...）

### 文件组织

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## 构建与部署

### 文档构建

本仓库使用 Markdown 进行文档编写：
- 每节课文件夹内的 README.md 文件
- 仓库根目录的主 README.md
- 通过 GitHub Actions 实现自动翻译系统

### CI/CD 流水线

位于 `.github/workflows/`：

1. **co-op-translator.yml** - 自动翻译成 50+ 种语言
2. **welcome-issue.yml** - 欢迎新的 issue 创建者
3. **welcome-pr.yml** - 欢迎新的 pull request 贡献者

### 部署

这是教学仓库——无部署流程。用户可：
1. 分叉或克隆仓库
2. 本地或 GitHub Codespaces 运行笔记本
3. 通过修改和实验示例学习

## Pull Request 指南

### 提交前

1. **测试你的更改：**
   - 彻底运行受影响的笔记本
   - 确认所有单元执行无误
   - 检查输出是否正确

2. **文档更新：**
   - 添加新概念时更新 README.md
   - 在笔记本中为复杂代码添加注释
   - 确保 markdown 单元解释功能目的

3. **文件变更：**
   - 避免提交 `.env` 文件（使用 `.env.example`）
   - 不提交 `venv/` 或 `__pycache__/` 目录
   - 保留演示概念的笔记本输出
   - 删除临时文件和备份笔记本（`*-backup.ipynb`）

### PR 标题格式

使用描述性标题：
- `[Lesson-XX] 添加 <概念> 的新示例`
- `[Fix] 修正第 XX 课 README 中的拼写错误`
- `[Update] 改进第 XX 课代码示例`
- `[Docs] 更新安装说明`

### 必需检查

- 笔记本应无错误执行
- README 应清晰准确
- 遵循仓库现有代码模式
- 与其他课程保持一致性

## 其他注意事项

### 常见问题

1. **Python 版本不匹配：**
   - 确保使用 Python 3.12+
   - 某些包在老版本无法正常工作
   - 使用 `python3 -m venv` 显式指定 Python 版本

2. **环境变量：**
   - 始终用 `.env.example` 创建 `.env`
   - 不要提交 `.env` 文件（已加入 `.gitignore`）
   - GitHub 令牌需要适当权限

3. **包冲突：**
   - 使用全新虚拟环境
   - 从 `requirements.txt` 安装，而非单独安装包
   - 某些笔记本需额外依赖，详见 markdown 单元

4. **Azure 服务：**
   - 需要有效的 Azure 订阅
   - 部分功能受区域限制
   - GitHub Models 免费层有使用限制

### 学习路径

推荐顺序学习课程：
1. **00-course-setup** - 环境搭建起步
2. **01-intro-to-ai-agents** - 了解 AI 代理基础
3. **02-explore-agentic-frameworks** - 学习不同框架
4. **03-agentic-design-patterns** - 核心设计模式
5. 按序完成后续编号课程

### 框架选择

根据目标选择框架：
- **所有课程**：微软代理框架 (MAF)，使用 `AzureAIProjectAgentProvider`
- **代理在服务器端注册**，Azure AI Foundry Agent Service V2 中显示，Foundry 门户可见代理

### 寻求帮助

- 加入 [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- 查看各课 README 文件获取具体指导
- 参阅主 README.md 了解课程总体介绍
- 参考 [Course Setup](./00-course-setup/README.md) 了解详细搭建步骤

### 贡献指南

这是开放的教育项目。欢迎贡献：
- 改进代码示例
- 修复拼写或错误
- 添加解释性注释
- 建议新的课程主题
- 翻译成更多语言

详见 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) 了解当前需求。

## 项目特定上下文

### 多语言支持

本仓库使用自动翻译系统：
- 支持 50+ 种语言
- 翻译文件位于 `/translations/<lang-code>/` 目录
- 通过 GitHub Actions workflow 自动更新翻译
- 源文件均为英文，位于仓库根目录

### 课程结构

每节课遵循一致模式：
1. 带有链接的视频缩略图
2. 书面课程内容（README.md）
3. 多框架代码示例
4. 学习目标和先决条件
5. 额外学习资源链接

### 代码示例命名

格式：`<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 第1课，MAF Python
- `14-sequential.ipynb` - 第14课，MAF 高级模式

### 特殊目录

- `translated_images/` - 本地化图片
- `images/` - 英文原始图片
- `.devcontainer/` - VS Code 开发容器配置
- `.github/` - GitHub Actions workflow 和模板

### 依赖项

`requirements.txt` 关键包：
- `agent-framework` - 微软代理框架
- `a2a-sdk` - 代理对代理协议支持
- `azure-ai-inference`、`azure-ai-projects` - Azure AI 服务
- `azure-identity` - Azure 认证（AzureCliCredential）
- `azure-search-documents` - Azure AI Search 集成
- `mcp[cli]` - 模型上下文协议支持

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求翻译准确，但请注意自动翻译可能存在错误或不准确之处。原始语言版本的文件应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或错误解释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->