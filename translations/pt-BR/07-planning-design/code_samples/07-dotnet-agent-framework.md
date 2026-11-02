# 🎯 Padrões de Planejamento & Design com Azure OpenAI (Responses API) (.NET)

## 📋 Objetivos de Aprendizagem

Este notebook demonstra padrões de design e planejamento em nível empresarial para criar agentes inteligentes usando o Microsoft Agent Framework em .NET com Azure OpenAI (Responses API). Você aprenderá a criar agentes que podem decompor problemas complexos, planejar soluções em múltiplas etapas e executar fluxos de trabalho sofisticados com os recursos empresariais do .NET.

## ⚙️ Pré-requisitos & Configuração

**Ambiente de Desenvolvimento:**
- .NET 9.0 SDK ou superior
- Visual Studio 2022 ou VS Code com extensão C#
- Uma assinatura do Azure com um recurso Azure OpenAI e um deployment de modelo
- O Azure CLI — faça login com `az login`

**Dependências Necessárias:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuração do Ambiente (arquivo .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Executando o Código

Esta lição inclui uma implementação de Aplicativo de Arquivo Único .NET. Para executá-lo:

```bash
# Torne o arquivo executável (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Execute o aplicativo
./07-dotnet-agent-framework.cs
```

Ou use o comando dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementação do Código

A implementação completa está disponível em `07-dotnet-agent-framework.cs`, que demonstra:

- Carregamento da configuração do ambiente com DotNetEnv
- Configuração do cliente Azure OpenAI e criação de um agente de IA usando `GetChatClient().AsAIAgent()`
- Definição de modelos de dados estruturados (Plan e TravelPlan) com serialização JSON
- Criação de um agente de IA com saída estruturada usando esquema JSON
- Execução de solicitações de planejamento com respostas tipadas e seguras

## Conceitos-Chave

### Planejamento Estruturado com Modelos Tipados

O agente usa classes C# para definir a estrutura das saídas de planejamento:

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### Esquema JSON para Saídas Estruturadas

O agente está configurado para retornar respostas que correspondem ao esquema TravelPlan:

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Instruções do Agente de Planejamento

O agente atua como coordenador, delegando tarefas a sub-agentes especializados:

- FlightBooking: Para reservar voos e fornecer informações sobre voos
- HotelBooking: Para reservar hotéis e fornecer informações sobre hotéis
- CarRental: Para aluguel de carros e fornecimento de informações sobre aluguel de carros
- ActivitiesBooking: Para reservar atividades e fornecer informações sobre atividades
- DestinationInfo: Para fornecer informações sobre destinos
- DefaultAgent: Para lidar com solicitações gerais

## Resultado Esperado

Quando você executar o agente com uma solicitação de planejamento de viagem, ele analisará a solicitação e gerará um plano estruturado com atribuição apropriada de tarefas para agentes especializados, formatado como JSON em conformidade com o esquema TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->