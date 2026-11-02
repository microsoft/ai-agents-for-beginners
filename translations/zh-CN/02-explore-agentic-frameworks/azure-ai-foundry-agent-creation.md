# Microsoft Foundry 代理服务开发

在本练习中，您将使用 [Microsoft Foundry 门户](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)中的 Microsoft Foundry 代理服务工具创建一个航班预订代理。该代理能够与用户交互并提供有关航班的信息。

## 先决条件

要完成此练习，您需要以下内容：
1. 具有有效订阅的 Azure 账户。[免费创建账户](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
2. 您需要拥有创建 Microsoft Foundry 中枢的权限，或者由他人为您创建。
    - 如果您的角色是贡献者或所有者，可以按照本教程中的步骤操作。

## 创建 Microsoft Foundry 中枢

> **注意：** Microsoft Foundry 之前称为 Azure AI Studio。

1. 按照 [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) 博客文章中的指南创建 Microsoft Foundry 中枢。
2. 创建项目后，关闭显示的任何提示，查看 Microsoft Foundry 门户中的项目页面，页面应类似下图：

    ![Microsoft Foundry Project](../../../translated_images/zh-CN/azure-ai-foundry.88d0c35298348c2f.webp)

## 部署模型

1. 在项目左侧窗格的 <strong>我的资产</strong> 部分中，选择 **模型 + 端点** 页面。
2. 在 **模型 + 端点** 页面中，选择 <strong>模型部署</strong> 选项卡，在 **+ 部署模型** 菜单中选择 <strong>部署基础模型</strong>。
3. 在列表中搜索 `gpt-5-mini` 模型，然后选择并确认部署。

    > <strong>注意</strong>：降低 TPM 有助于避免过度使用您所使用订阅中的配额。

    ![Model Deployed](../../../translated_images/zh-CN/model-deployment.3749c53fb81e18fd.webp)

## 创建代理

现在您已经部署了模型，可以创建代理。代理是可用于与用户交互的对话式 AI 模型。

1. 在项目左侧窗格的 <strong>构建与自定义</strong> 部分，选择 <strong>代理</strong> 页面。
2. 点击 **+ 创建代理** 创建一个新代理。在 <strong>代理设置</strong> 对话框中：
    - 输入代理名称，例如 `FlightAgent`。
    - 确保选中了之前创建的 `gpt-5-mini` 模型部署。
    - 根据您希望代理遵循的提示，设置 <strong>说明</strong>。示例如下：
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> 详情提示请查看[此仓库](https://github.com/ShivamGoyal03/RoamMind)了解更多信息。
    
> 此外，您可以添加 <strong>知识库</strong> 和 <strong>操作</strong>，以增强代理根据用户请求提供更多信息和执行自动任务的能力。对于此练习，可以跳过这些步骤。
    
![Agent Setup](../../../translated_images/zh-CN/agent-setup.9bbb8755bf5df672.webp)

3. 若要创建新的多 AI 代理，只需点击 <strong>新建代理</strong>。新创建的代理将显示在代理页面上。


## 测试代理

创建代理后，您可以在 Microsoft Foundry 门户游乐场测试代理的响应。

1. 在代理的 <strong>设置</strong> 面板顶部，选择 <strong>在游乐场中试用</strong>。
2. 在 <strong>游乐场</strong> 面板中，您可以通过聊天窗口输入查询与代理交互。例如，您可以让代理搜索 28 日从西雅图到纽约的航班。

    > <strong>注意</strong>：由于本练习中未使用实时数据，代理可能无法给出准确答案。目的是测试代理基于所提供的说明理解和响应用户查询的能力。

    ![Agent Playground](../../../translated_images/zh-CN/agent-playground.dc146586de715010.webp)

3. 测试完后，您可以通过添加更多意图、训练数据和操作进一步自定义代理以增强其功能。

## 清理资源

测试完代理后，您可以将其删除，以避免产生额外费用。
1. 打开 [Azure 门户](https://portal.azure.com)，查看您用于本练习中部署中枢资源的资源组内容。
2. 在工具栏选择 <strong>删除资源组</strong>。
3. 输入资源组名称并确认删除。

## 资源

- [Microsoft Foundry 文档](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry 门户](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry 入门](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure 上的 AI 代理基础](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->