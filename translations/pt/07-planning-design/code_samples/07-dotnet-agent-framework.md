<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:56:36+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "pt"
}
-->
# 🎯 Planeamento e Padrões de Design com Modelos GitHub (.NET)

## 📋 Objetivos de Aprendizagem

Este notebook demonstra padrões de planeamento e design de nível empresarial para construir agentes inteligentes utilizando o Microsoft Agent Framework em .NET com Modelos GitHub. Vais aprender a criar agentes que conseguem decompor problemas complexos, planear soluções em várias etapas e executar fluxos de trabalho sofisticados com as funcionalidades empresariais do .NET.

## ⚙️ Pré-requisitos e Configuração

**Ambiente de Desenvolvimento:**
- SDK .NET 9.0 ou superior
- Visual Studio 2022 ou VS Code com extensão C#
- Acesso à API de Modelos GitHub

**Dependências Necessárias:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuração de Ambiente (ficheiro .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Executar o Código

Esta lição inclui uma implementação de Aplicação de Ficheiro Único em .NET. Para executá-la:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Ou utiliza o comando dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementação do Código

A implementação completa está disponível em `07-dotnet-agent-framework.cs`, que demonstra:

- Carregar a configuração de ambiente com DotNetEnv
- Configurar o cliente OpenAI para Modelos GitHub
- Definir modelos de dados estruturados (Plan e TravelPlan) com serialização JSON
- Criar um agente de IA com saída estruturada utilizando o esquema JSON
- Executar pedidos de planeamento com respostas tipificadas

## Conceitos-Chave

### Planeamento Estruturado com Modelos Tipificados

O agente utiliza classes C# para definir a estrutura das saídas de planeamento:

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

O agente está configurado para retornar respostas que correspondam ao esquema TravelPlan:

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Instruções do Agente de Planeamento

O agente atua como um coordenador, delegando tarefas a subagentes especializados:

- FlightBooking: Para reservar voos e fornecer informações sobre voos
- HotelBooking: Para reservar hotéis e fornecer informações sobre hotéis
- CarRental: Para reservar carros e fornecer informações sobre aluguer de carros
- ActivitiesBooking: Para reservar atividades e fornecer informações sobre atividades
- DestinationInfo: Para fornecer informações sobre destinos
- DefaultAgent: Para lidar com pedidos gerais

## Saída Esperada

Quando executares o agente com um pedido de planeamento de viagem, ele irá analisar o pedido e gerar um plano estruturado com atribuições de tarefas apropriadas aos agentes especializados, formatado como JSON conforme o esquema TravelPlan.

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.