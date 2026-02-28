# AGENTS.md

## 项目概述

该仓库包含“初学者AI代理”——一门全面的教育课程，教授构建AI代理所需的所有内容。课程包含15+节课，涵盖基础知识、设计模式、框架以及AI代理的生产部署。

**关键技术：**  
- Python 3.12+  
- 交互式学习的Jupyter笔记本  
- AI框架：Microsoft Agent Framework (MAF)  
- Azure AI服务：Microsoft Foundry，Azure AI Foundry Agent Service V2  

**架构：**  
- 基于课程的结构（00-15+目录）  
- 每节课包含：README文档、代码示例（Jupyter笔记本）和图片  
- 通过自动翻译系统支持多语言  
- 每节课一个Python笔记本，使用Microsoft Agent Framework  

## 设置命令

### 前提条件  
- Python 3.12或更高版本  
- Azure订阅（用于Azure AI Foundry）  
- 已安装并认证的Azure CLI（`az login`）  

### 初始设置

1. **克隆或派生仓库：**  
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # 或
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```
  
2. **创建并激活Python虚拟环境：**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # 在 Windows 上：venv\Scripts\activate
   ```
  
3. **安装依赖：**  
   ```bash
   pip install -r requirements.txt
   ```
  
4. **设置环境变量：**  
   ```bash
   cp .env.example .env
   # 使用您的 API 密钥和端点编辑 .env
   ```
  
### 必需的环境变量

针对**Azure AI Foundry**（必需）：  
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry项目端点  
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - 模型部署名称（例如 gpt-4o）  

针对**Azure AI Search**（第五课 - RAG）：  
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search端点  
- `AZURE_SEARCH_API_KEY` - Azure AI Search API密钥  

认证：运行`az login`后再运行笔记本（使用`AzureCliCredential`）。  

## 开发工作流程

### 运行Jupyter笔记本

每节课包含用于不同框架的多个Jupyter笔记本:

1. **启动Jupyter：**  
   ```bash
   jupyter notebook
   ```
  
2. **导航到课程目录**（例如 `01-intro-to-ai-agents/code_samples/`）  

3. **打开并运行笔记本：**  
   - `*-python-agent-framework.ipynb` - 使用Microsoft Agent Framework（Python）  
   - `*-dotnet-agent-framework.ipynb` - 使用Microsoft Agent Framework（.NET）  

### 使用Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry：**  
- 需要Azure订阅  
- 使用`AzureAIProjectAgentProvider`针对Agent Service V2（代理在Foundry门户中可见）  
- 内置可观察性，适合生产环境  
- 文件模式：`*-python-agent-framework.ipynb`  

## 测试说明

这是一个包含示例代码的教学仓库，而非带有自动化测试的生产代码。验证您的设置和更改：

### 手动测试

1. **测试Python环境：**  
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

在Jupyter中打开笔记本并按顺序执行单元格。每个笔记本是独立的，包括：  
- 导入语句  
- 配置加载  
- 示例代理实现  
- 用Markdown单元展示的预期输出  

## 代码风格

### Python规范

- **Python版本**：3.12+  
- **代码风格**：遵循标准Python PEP 8规范  
- **笔记本**：使用清晰的Markdown单元解释概念  
- **导入顺序**：标准库、第三方、本地导入分组  

### Jupyter笔记本规范

- 在代码单元前包含描述性的Markdown单元  
- 笔记本中包含输出示例供参考  
- 使用清晰与课程概念匹配的变量名  
- 保持笔记本执行顺序线性（单元格1 → 2 → 3…）  

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
  
## 构建和部署

### 构建文档

本仓库使用Markdown进行文档编写：  
- 每节课文件夹内的README.md  
- 仓库根目录的README.md  
- 通过GitHub Actions实现自动翻译系统  

### CI/CD流程

位于`.github/workflows/`：  

1. **co-op-translator.yml** - 自动翻译成50+种语言  
2. **welcome-issue.yml** - 欢迎新的问题提交者  
3. **welcome-pr.yml** - 欢迎新的拉取请求贡献者  

### 部署

这是一个教学仓库，无部署流程。用户操作：  
1. 派生或克隆仓库  
2. 本地或GitHub Codespaces中运行笔记本  
3. 通过修改和实验示例学习  

## 拉取请求指南

### 提交前

1. **测试更改：**  
   - 完整运行受影响的笔记本  
   - 确认所有单元格无错误执行  
   - 检查输出是否正确  

2. **文档更新：**  
   - 添加新概念时更新README.md  
   - 笔记本复杂代码处添加注释  
   - 确保Markdown单元解释目的  

3. **文件更改：**  
   - 避免提交`.env`文件（使用`.env.example`）  
   - 不提交`venv/`或`__pycache__/`目录  
   - 需要展示概念时保留笔记本输出  
   - 删除临时文件和备份笔记本（`*-backup.ipynb`）  

### PR标题格式

使用描述性标题：  
- `[Lesson-XX] 添加<概念>新示例`  
- `[Fix] 更正lesson-XX README中的错字`  
- `[Update] 优化lesson-XX代码示例`  
- `[Docs] 更新设置说明`  

### 必需检查

- 笔记本应无错误执行  
- README文件应清晰准确  
- 遵循仓库中现有代码模式  
- 保持与其他课程一致性  

## 其他说明

### 常见问题

1. **Python版本不匹配：**  
   - 确保使用Python 3.12+  
   - 一些包可能不支持旧版本  
   - 使用`python3 -m venv`明确指定Python版本  

2. **环境变量：**  
   - 始终从`.env.example`复制生成`.env`  
   - 不提交`.env`文件（已在`.gitignore`中）  
   - GitHub令牌需具备适当权限  

3. **包冲突：**  
   - 使用干净的虚拟环境  
   - 从`requirements.txt`安装依赖，避免单独安装  
   - 某些笔记本可能需要额外包，已在Markdown单元注明  

4. **Azure服务：**  
   - 需要有效的Azure订阅  
   - 部分功能受区域限制  
   - GitHub模型免费层有使用限制  

### 学习路径

推荐按顺序阅读课程：  
1. **00-course-setup** - 环境设置入门  
2. **01-intro-to-ai-agents** - 了解AI代理基础  
3. **02-explore-agentic-frameworks** - 学习不同框架  
4. **03-agentic-design-patterns** - 核心设计模式  
5. 按编号顺序继续学习  

### 框架选择

按目标选择框架：  
- **所有课程**：使用Microsoft Agent Framework (MAF) 和 `AzureAIProjectAgentProvider`  
- **代理服务器端注册**于Azure AI Foundry Agent Service V2，且在Foundry门户显示  

### 获取帮助

- 加入[Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)  
- 查看课程README获取具体指导  
- 参阅主README.md了解课程概览  
- 查阅[Course Setup](./00-course-setup/README.md)获取详细设置指导  

### 贡献

这是一个开放的教育项目。欢迎贡献：  
- 改进代码示例  
- 修正错字或错误  
- 添加澄清性注释  
- 建议新课程主题  
- 翻译到更多语言  

查看[GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues)了解当前需求。  

## 项目特定上下文

### 多语言支持

该仓库使用自动翻译系统：  
- 支持50+语言  
- 翻译文件位于`/translations/<lang-code>/`目录  
- GitHub Actions工作流自动处理翻译更新  
- 源文件以英语保存在仓库根目录  

### 课程结构

每节课遵循统一模式：  
1. 带链接的视频缩略图  
2. 书面课程内容（README.md）  
3. 多框架代码示例  
4. 学习目标与前置条件  
5. 额外学习资源链接  

### 代码示例命名

格式：`<lesson-number>-python-agent-framework.ipynb`  
- `01-python-agent-framework.ipynb` - 第1课，MAF Python  
- `14-sequential.ipynb` - 第14课，MAF高级模式  

### 特殊目录

- `translated_images/` - 本地化图片  
- `images/` - 英文原始图片  
- `.devcontainer/` - VS Code开发容器配置  
- `.github/` - GitHub Actions工作流和模板  

### 依赖项

`requirements.txt`中的关键包：  
- `agent-framework` - Microsoft Agent Framework  
- `a2a-sdk` - 代理间协议支持  
- `azure-ai-inference`、`azure-ai-projects` - Azure AI服务  
- `azure-identity` - Azure认证（AzureCliCredential）  
- `azure-search-documents` - Azure AI Search集成  
- `mcp[cli]` - 模型上下文协议支持

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)翻译完成。尽管我们力求准确，但请注意，自动翻译可能存在错误或不准确之处。原始语言版本的文件应视为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们不承担任何责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->