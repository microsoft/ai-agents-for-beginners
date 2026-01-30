# AGENTS.md

## 项目概述

此代码库包含“AI初学者代理”课程——一门全面的教育课程，教授构建AI代理所需的一切知识。课程由15+节课组成，涵盖AI代理的基础知识、设计模式、框架以及生产部署。

**关键技术：**
- Python 3.12及以上版本
- Jupyter Notebooks用于交互式学习
- AI框架：Semantic Kernel、AutoGen、Microsoft Agent Framework (MAF)
- Azure AI服务：Azure AI Foundry、Azure AI Agent Service
- GitHub模型市场（提供免费层）

**架构：**
- 基于课程的结构（00-15+目录）
- 每节课包含：README文档、代码示例（Jupyter notebooks）和图片
- 通过自动翻译系统支持多语言
- 每节课提供多个框架选项（Semantic Kernel、AutoGen、Azure AI Agent Service）

## 设置命令

### 前置条件
- Python 3.12或更高版本
- GitHub账户（用于GitHub模型 - 免费层）
- Azure订阅（可选，用于Azure AI服务）

### 初始设置

1. **克隆或fork代码库：**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **创建并激活Python虚拟环境：**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **安装依赖项：**
   ```bash
   pip install -r requirements.txt
   ```

4. **设置环境变量：**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### 必需的环境变量

对于 **GitHub模型（免费）**：
- `GITHUB_TOKEN` - 来自GitHub的个人访问令牌

对于 **Azure AI服务**（可选）：
- `PROJECT_ENDPOINT` - Azure AI Foundry项目端点
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API密钥
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI端点URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - 聊天模型的部署名称
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - 嵌入模型的部署名称
- 其他Azure配置详见`.env.example`

## 开发工作流

### 运行Jupyter Notebooks

每节课包含多个针对不同框架的Jupyter notebooks：

1. **启动Jupyter：**
   ```bash
   jupyter notebook
   ```

2. **导航到课程目录**（例如，`01-intro-to-ai-agents/code_samples/`）

3. **打开并运行notebooks：**
   - `*-semantic-kernel.ipynb` - 使用Semantic Kernel框架
   - `*-autogen.ipynb` - 使用AutoGen框架
   - `*-python-agent-framework.ipynb` - 使用Microsoft Agent Framework（Python）
   - `*-dotnet-agent-framework.ipynb` - 使用Microsoft Agent Framework（.NET）
   - `*-azureaiagent.ipynb` - 使用Azure AI Agent Service

### 使用不同框架

**Semantic Kernel + GitHub模型：**
- GitHub账户提供免费层
- 适合学习和实验
- 文件模式：`*-semantic-kernel*.ipynb`

**AutoGen + GitHub模型：**
- GitHub账户提供免费层
- 支持多代理编排功能
- 文件模式：`*-autogen.ipynb`

**Microsoft Agent Framework (MAF)：**
- Microsoft最新框架
- 提供Python和.NET版本
- 文件模式：`*-agent-framework.ipynb`

**Azure AI Agent Service：**
- 需要Azure订阅
- 具备生产级功能
- 文件模式：`*-azureaiagent.ipynb`

## 测试说明

这是一个教育代码库，包含示例代码，而非带有自动化测试的生产代码。验证设置和更改的方法如下：

### 手动测试

1. **测试Python环境：**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **测试notebook执行：**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **验证环境变量：**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### 运行单个notebooks

在Jupyter中打开notebooks并按顺序执行单元格。每个notebook都是自包含的，包括：
- 导入语句
- 配置加载
- 示例代理实现
- Markdown单元格中的预期输出

## 代码风格

### Python约定

- **Python版本**：3.12及以上
- **代码风格**：遵循标准Python PEP 8约定
- **Notebooks**：使用清晰的Markdown单元格解释概念
- **导入**：按标准库、第三方库、本地导入分组

### Jupyter Notebook约定

- 在代码单元格之前包含描述性Markdown单元格
- 在notebooks中添加输出示例以供参考
- 使用与课程概念匹配的清晰变量名
- 保持notebook执行顺序线性（单元格1 → 2 → 3...）

### 文件组织

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```


## 构建与部署

### 构建文档

此代码库使用Markdown进行文档编写：
- 每个课程文件夹中的README.md文件
- 代码库根目录的主README.md
- 通过GitHub Actions实现自动翻译系统

### CI/CD管道

位于`.github/workflows/`：

1. **co-op-translator.yml** - 自动翻译为50+种语言
2. **welcome-issue.yml** - 欢迎新问题创建者
3. **welcome-pr.yml** - 欢迎新拉取请求贡献者

### 部署

这是一个教育代码库，没有部署流程。用户可以：
1. Fork或克隆代码库
2. 在本地或GitHub Codespaces中运行notebooks
3. 通过修改和实验示例进行学习

## 拉取请求指南

### 提交前

1. **测试您的更改：**
   - 完整运行受影响的notebooks
   - 确保所有单元格无错误执行
   - 检查输出是否合适

2. **文档更新：**
   - 如果添加新概念，请更新README.md
   - 在notebooks中为复杂代码添加注释
   - 确保Markdown单元格解释目的

3. **文件更改：**
   - 避免提交`.env`文件（使用`.env.example`）
   - 不要提交`venv/`或`__pycache__/`目录
   - 保留notebook输出以展示概念
   - 删除临时文件和备份notebooks（`*-backup.ipynb`）

### PR标题格式

使用描述性标题：
- `[Lesson-XX] 添加新示例用于<概念>`
- `[Fix] 修正lesson-XX README中的拼写错误`
- `[Update] 改进lesson-XX中的代码示例`
- `[Docs] 更新设置说明`

### 必需检查

- notebooks应无错误执行
- README文件应清晰准确
- 遵循代码库中的现有代码模式
- 与其他课程保持一致性

## 附加说明

### 常见问题

1. **Python版本不匹配：**
   - 确保使用Python 3.12及以上版本
   - 某些包可能不支持旧版本
   - 使用`python3 -m venv`明确指定Python版本

2. **环境变量：**
   - 始终从`.env.example`创建`.env`
   - 不要提交`.env`文件（已在`.gitignore`中）
   - GitHub令牌需要适当权限

3. **包冲突：**
   - 使用全新的虚拟环境
   - 从`requirements.txt`安装，而不是单独安装包
   - 某些notebooks可能需要Markdown单元格中提到的额外包

4. **Azure服务：**
   - Azure AI服务需要有效订阅
   - 某些功能仅限特定地区
   - GitHub模型的免费层有使用限制

### 学习路径

推荐的课程学习顺序：
1. **00-course-setup** - 从这里开始设置环境
2. **01-intro-to-ai-agents** - 了解AI代理基础知识
3. **02-explore-agentic-frameworks** - 学习不同的框架
4. **03-agentic-design-patterns** - 核心设计模式
5. 按编号顺序继续学习后续课程

### 框架选择

根据您的目标选择框架：
- **学习/原型开发**：Semantic Kernel + GitHub模型（免费）
- **多代理系统**：AutoGen
- **最新功能**：Microsoft Agent Framework (MAF)
- **生产部署**：Azure AI Agent Service

### 获取帮助

- 加入[Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- 查看课程README文件以获取具体指导
- 检查主[README.md](./README.md)了解课程概述
- 参考[课程设置](./00-course-setup/README.md)获取详细设置说明

### 贡献

这是一个开放的教育项目，欢迎贡献：
- 改进代码示例
- 修正拼写或错误
- 添加说明性注释
- 提议新课程主题
- 翻译为其他语言

请查看[GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues)了解当前需求。

## 项目特定背景

### 多语言支持

此代码库使用自动翻译系统：
- 支持50+种语言
- 翻译文件位于`/translations/<lang-code>/`目录
- GitHub Actions工作流处理翻译更新
- 源文件位于代码库根目录，使用英文编写

### 课程结构

每节课遵循一致的模式：
1. 视频缩略图及链接
2. 书面课程内容（README.md）
3. 多框架代码示例
4. 学习目标和前置条件
5. 额外学习资源链接

### 代码示例命名

格式：`<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - 第4课，Semantic Kernel
- `07-autogen.ipynb` - 第7课，AutoGen
- `14-python-agent-framework.ipynb` - 第14课，MAF Python
- `14-dotnet-agent-framework.ipynb` - 第14课，MAF .NET

### 特殊目录

- `translated_images/` - 翻译内容的本地化图片
- `images/` - 英文内容的原始图片
- `.devcontainer/` - VS Code开发容器配置
- `.github/` - GitHub Actions工作流和模板

### 依赖项

`requirements.txt`中的关键包：
- `autogen-agentchat`、`autogen-core`、`autogen-ext` - AutoGen框架
- `semantic-kernel` - Semantic Kernel框架
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`、`azure-ai-projects` - Azure AI服务
- `azure-search-documents` - Azure AI搜索集成
- `chromadb` - 用于RAG示例的向量数据库
- `chainlit` - 聊天UI框架
- `browser_use` - 用于代理的浏览器自动化
- `mcp[cli]` - 模型上下文协议支持
- `mem0ai` - 用于代理的内存管理

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。