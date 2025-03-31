<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "664afc6dd1bf275b0eafd126b71da420",
  "translation_date": "2025-03-28T11:39:53+00:00",
  "source_file": "02-explore-agentic-frameworks\\azure-ai-foundry-agent-creation.md",
  "language_code": "pt"
}
-->
# Desenvolvimento do Serviço Azure AI Agent

Neste exercício, você utilizará as ferramentas do serviço Azure AI Agent no [portal Azure AI Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) para criar um agente de Reserva de Voos. O agente será capaz de interagir com os usuários e fornecer informações sobre voos.

## Pré-requisitos

Para concluir este exercício, você precisa do seguinte:
1. Uma conta Azure com uma assinatura ativa. [Crie uma conta gratuitamente](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Permissões para criar um hub Azure AI Foundry ou que alguém crie um para você.
    - Se o seu papel for Colaborador ou Proprietário, você pode seguir os passos deste tutorial.

## Criar um hub Azure AI Foundry

> **Note:** O Azure AI Foundry era anteriormente conhecido como Azure AI Studio.

1. Siga as diretrizes do post no blog [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) para criar um hub Azure AI Foundry.
2. Quando seu projeto for criado, feche quaisquer dicas que forem exibidas e revise a página do projeto no portal Azure AI Foundry, que deve ser semelhante à imagem a seguir:

    ![Projeto Azure AI Foundry](../../../translated_images/azure-ai-foundry.8a2b56713298fd09de77022ab1ba07ebc681ea4cd4438a46c4a6fc6b6f077962.pt.png)

## Implantar um modelo

1. No painel à esquerda do seu projeto, na seção **Meus ativos**, selecione a página **Modelos + endpoints**.
2. Na página **Modelos + endpoints**, na aba **Implantações de modelo**, no menu **+ Implantar modelo**, selecione **Implantar modelo base**.
3. Procure pelo modelo `gpt-4o-mini` na lista, selecione-o e confirme.

    > **Note**: Reduzir o TPM ajuda a evitar o uso excessivo da cota disponível na assinatura que você está utilizando.

    ![Modelo Implantado](../../../translated_images/model-deployment.4adf429ebdf42103d7a759087fe0da91aeb70d2204cc8bdca70cc6c53c627938.pt.png)

## Criar um agente

Agora que você implantou um modelo, pode criar um agente. Um agente é um modelo de IA conversacional que pode ser usado para interagir com usuários.

1. No painel à esquerda do seu projeto, na seção **Construir e Personalizar**, selecione a página **Agentes**.
2. Clique em **+ Criar agente** para criar um novo agente. Na caixa de diálogo **Configuração do Agente**:
    - Insira um nome para o agente, como `FlightAgent`.
    - Certifique-se de que a implantação do modelo `gpt-4o-mini` que você criou anteriormente esteja selecionada.
    - Defina as **Instruções** conforme o prompt que você deseja que o agente siga. Aqui está um exemplo:
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
> Para um prompt mais detalhado, você pode conferir [este repositório](https://github.com/ShivamGoyal03/RoamMind) para mais informações.

> Além disso, você pode adicionar **Base de Conhecimento** e **Ações** para melhorar as capacidades do agente, permitindo que ele forneça mais informações e execute tarefas automatizadas com base nas solicitações dos usuários. Para este exercício, você pode pular essas etapas.

![Configuração do Agente](../../../translated_images/agent-setup.68a0c72f47bd1383584c52f14d694b54ea96c56c49660222409f83451b8220a8.pt.png)

3. Para criar um novo agente multi-IA, basta clicar em **Novo Agente**. O agente recém-criado será exibido na página Agentes.

## Testar o agente

Após criar o agente, você pode testá-lo para ver como ele responde às consultas dos usuários no playground do portal Azure AI Foundry.

1. No topo do painel **Configuração** do seu agente, selecione **Experimentar no playground**.
2. No painel **Playground**, você pode interagir com o agente digitando consultas na janela de chat. Por exemplo, você pode pedir ao agente para procurar voos de Seattle para Nova York no dia 28.

    > **Note**: O agente pode não fornecer respostas precisas, pois nenhum dado em tempo real está sendo usado neste exercício. O objetivo é testar a capacidade do agente de entender e responder às consultas dos usuários com base nas instruções fornecidas.

    ![Playground do Agente](../../../translated_images/agent-playground.847acb21209744353080ead65ec9326b917a6b90121d4b63f6f412a4d65af2a0.pt.png)

3. Após testar o agente, você pode personalizá-lo ainda mais, adicionando mais intenções, dados de treinamento e ações para aprimorar suas capacidades.

## Limpar recursos

Quando você terminar de testar o agente, pode excluí-lo para evitar custos adicionais.
1. Abra o [portal Azure](https://portal.azure.com) e visualize o conteúdo do grupo de recursos onde você implantou os recursos do hub utilizados neste exercício.
2. Na barra de ferramentas, selecione **Excluir grupo de recursos**.
3. Insira o nome do grupo de recursos e confirme que deseja excluí-lo.

## Recursos

- [Documentação do Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Portal Azure AI Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Introdução ao Azure AI Studio](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Fundamentos de agentes de IA no Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Discord do Azure AI](https://aka.ms/AzureAI/Discord)

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.