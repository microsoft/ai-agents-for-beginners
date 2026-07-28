# AGENTS.md

## 项目概述

本仓库包含“初学者的AI代理”——一个全面的教育课程，教授构建AI代理所需的全部知识。课程包含18节课（编号00-18），涵盖基础知识、设计模式、框架、生产部署、本地/设备端代理以及AI代理的安全性。

**关键技术：**
- Python 3.12+
- 用于交互式学习的Jupyter笔记本
- AI框架：微软代理框架（Microsoft Agent Framework，MAF）
- Azure AI服务：Microsoft Foundry，Microsoft Foundry Agent Service V2

**架构：**
- 基于课程的结构（00-15+ 目录）
- 每节课包含：README文档、代码示例（Jupyter笔记本）和图片
- 通过自动翻译系统支持多语言
- 每节课一个使用微软代理框架的Python笔记本

## 环境搭建命令

### 先决条件
- Python 3.12或更高版本
- Azure订阅（用于Microsoft Foundry）
- 已安装并登录Azure CLI（`az login`）

### 初始设置

1. **克隆或分叉仓库：**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # 或者
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **创建并激活Python虚拟环境：**
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
   # 使用您的 API 密钥和端点编辑 .env
   ```

### 必需的环境变量

对于 **Microsoft Foundry**（必填）：
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry项目端点
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - 模型部署名称（例如 gpt-5-mini）

对于 **Azure AI Search**（第五课 - RAG）：
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search端点
- `AZURE_SEARCH_API_KEY` - Azure AI Search API密钥

认证：运行 `az login` 后再运行笔记本（使用 `AzureCliCredential`）。

## 开发工作流程

### 运行Jupyter笔记本

每节课程包含多个适用于不同框架的Jupyter笔记本：

1. **启动Jupyter：**
   ```bash
   jupyter notebook
   ```

2. <strong>进入某个课程目录</strong>（例如 `01-intro-to-ai-agents/code_samples/`）

3. **打开并运行笔记本：**
   - `*-python-agent-framework.ipynb` - 使用微软代理框架（Python）
   - `*-dotnet-agent-framework.ipynb` - 使用微软代理框架（.NET）

### 使用微软代理框架

**微软代理框架 + Microsoft Foundry：**
- 需要Azure订阅
- 使用 `FoundryChatClient` 访问Agent Service V2（代理可见于Foundry门户）
- 生产就绪，内置可观测性
- 文件模式：`*-python-agent-framework.ipynb`

## 测试说明

这是一个教程仓库，含示例代码，而非带自动化测试的生产代码。验证环境和更改的方法：

### 手动测试

1. **测试Python环境：**
   ```bash
   python --version  # 应该是3.12以上
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **测试笔记本执行：**
   ```bash
   # 将笔记本转换为脚本并运行（测试导入）
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **核实环境变量：**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### 运行单个笔记本

在Jupyter中打开笔记本，按顺序执行单元。每个笔记本均为自包含，包含：
- 导入语句
- 配置加载
- 示例代理实现
- 预期输出（位于markdown单元）

### 部署代理的冒烟测试

在代理作为Microsoft Foundry托管代理部署的课程（01、04、05、16）中，本仓库提供了位于 `tests/` 下的冒烟测试目录，由 `.github/workflows/smoke-test.yml` 工作流通过[AI冒烟测试](https://github.com/marketplace/actions/ai-smoke-test)动作运行。这是轻量级的部署后检查（代理是否可达且基本响应符合预期？），是课程10和16评估流程的补充。有关目录到课程再到代理的映射，详见 [tests/README.md](./tests/README.md)。第17课在本地运行Foundry Local，无托管端点，通过直接运行笔记本验证。

## 代码风格

### Python规范

- **Python版本**：3.12+
- <strong>代码风格</strong>：遵循标准Python PEP 8规范
- <strong>笔记本</strong>：使用清晰的markdown单元解释概念
- <strong>导入</strong>：按标准库、第三方、本地模块分组

### Jupyter笔记本规范

- 在代码单元前加入描述性markdown单元
- 在笔记本中添加输出示例供参考
- 使用与课程概念匹配的清晰变量名
- 保持笔记本执行顺序线性（单元1 → 2 → 3…）

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

本仓库使用Markdown编写文档：
- 各课程文件夹下的README.md文件
- 仓库根目录主README.md
- 通过GitHub Actions实现自动翻译系统

### CI/CD流程

位于 `.github/workflows/`：

1. **co-op-translator.yml** - 自动翻译成50+种语言
2. **welcome-issue.yml** - 欢迎新创建问题的用户
3. **welcome-pr.yml** - 欢迎新拉取请求贡献者

### 部署

这是一个教学仓库——无部署流程。用户：
1. 分叉或克隆仓库
2. 本地或GitHub Codespaces中运行笔记本
3. 通过修改和实验示例学习

## 拉取请求指南

### 提交前

1. **测试修改：**
   - 完整运行受影响的笔记本
   - 确认所有单元格无错误
   - 检查输出是否合理

2. **文档更新：**
   - 若新增概念，更新README.md
   - 笔记本复杂代码添加注释
   - 确保markdown单元解释目的

3. **文件变更：**
   - 避免提交 `.env` 文件（使用 `.env.example`）
   - 不提交 `venv/` 或 `__pycache__/` 目录
   - 展示概念时保留笔记本输出
   - 移除临时文件和备份笔记本（`*-backup.ipynb`）

### PR标题格式

使用描述性标题：
- `[Lesson-XX] 添加<概念>的新示例`
- `[Fix] 修正第XX课README中的拼写错误`
- `[Update] 改进第XX课代码示例`
- `[Docs] 更新安装说明`

### 必要检查

- 笔记本应无错误执行
- README文件应清晰准确
- 遵循仓库现有代码模式
- 保持与其他课程一致

## 附加说明

### 常见问题

1. **Python版本不匹配：**
   - 确保使用Python 3.12+
   - 部分包不支持旧版
   - 使用 `python3 -m venv` 明确指定Python版本

2. **环境变量：**
   - 始终从 `.env.example` 创建 `.env`
   - 不提交 `.env` 文件（已加入 `.gitignore`）
   - 使用 `az login` 进行无密Entra ID认证

3. **包冲突：**
   - 使用新虚拟环境
   - 从 `requirements.txt` 安装，不单独安装包
   - 有些笔记本markdown单元中提及额外依赖

4. **Azure服务：**
   - 需要有效的Azure订阅
   - 部分功能有区域限制
   - 确保你的Azure OpenAI模型部署支持Responses API

### 学习路线

建议按顺序学习课程：
1. **00-course-setup** - 环境搭建开始
2. **01-intro-to-ai-agents** - 理解AI代理基础
3. **02-explore-agentic-frameworks** - 学习不同框架
4. **03-agentic-design-patterns** - 核心设计模式
5. 按编号顺序继续后续课程

### 框架选择

根据目标选择框架：
- <strong>所有课程</strong>：微软代理框架（MAF）配合 `FoundryChatClient`
- <strong>代理在服务器端注册</strong>，在Microsoft Foundry Agent Service V2中，并可在Foundry门户查看

### 获取帮助

- 加入 [Microsoft Foundry社区Discord](https://aka.ms/ai-agents/discord)
- 查看课程README文件获取具体指导
- 查阅主[README.md](./README.md)了解课程概览
- 参阅[课程环境搭建](./00-course-setup/README.md)详细步骤

### 贡献

这是一个开放的教育项目，欢迎贡献：
- 改进代码示例
- 修正拼写或错误
- 添加注释说明
- 建议新增课程主题
- 翻译成更多语言

详见[GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues)了解当前需求。

## 项目特定上下文

### 多语言支持

本仓库使用自动翻译系统：
- 支持50+种语言
- 翻译存放于`/translations/<lang-code>/`目录
- GitHub Actions工作流负责翻译更新
- 源文件为仓库根目录的英文内容

### 课程结构

每节课遵循统一模式：
1. 视频缩略图与链接
2. 书面课程内容（README.md）
3. 多框架代码示例
4. 学习目标和先决条件
5. 额外学习资源链接

### 代码示例命名

格式：`<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 第1课，MAF Python
- `14-sequential.ipynb` - 第14课，MAF高级模式
- `16-python-agent-framework.ipynb` - 第16课，生产客户支持代理
- `17-local-agent-foundry-local.ipynb` - 第17课，本地代理（Foundry Local + Qwen）

### 特殊目录

- `translated_images/` - 本地化翻译对应图片
- `images/` - 英文原始图片
- `.devcontainer/` - VS Code开发容器配置
- `.github/` - GitHub Actions工作流及模板

### 依赖

`requirements.txt` 中的关键包：
- `agent-framework` - 微软代理框架
- `a2a-sdk` - 代理间协议支持
- `azure-ai-inference`, `azure-ai-projects` - Azure AI服务
- `azure-identity` - Azure认证（AzureCliCredential）
- `azure-search-documents` - Azure AI Search集成
- `mcp[cli]` - 模型上下文协议支持

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->