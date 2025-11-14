<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:56:43+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "br"
}
-->
# 🎯 Planejamento e Padrões de Design com Modelos do GitHub (.NET)

## 📋 Objetivos de Aprendizagem

Este notebook demonstra padrões de planejamento e design de nível empresarial para construir agentes inteligentes usando o Microsoft Agent Framework em .NET com Modelos do GitHub. Você aprenderá a criar agentes que podem decompor problemas complexos, planejar soluções em várias etapas e executar fluxos de trabalho sofisticados com os recursos empresariais do .NET.

## ⚙️ Pré-requisitos e Configuração

**Ambiente de Desenvolvimento:**
- SDK .NET 9.0 ou superior
- Visual Studio 2022 ou VS Code com extensão C#
- Acesso à API de Modelos do GitHub

**Dependências Necessárias:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuração de Ambiente (arquivo .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Executando o Código

Esta lição inclui uma implementação de Aplicativo de Arquivo Único .NET. Para executá-lo:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Ou use o comando dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementação do Código

A implementação completa está disponível em `07-dotnet-agent-framework.cs`, que demonstra:

- Carregamento da configuração de ambiente com DotNetEnv
- Configuração do cliente OpenAI para Modelos do GitHub
- Definição de modelos de dados estruturados (Plan e TravelPlan) com serialização JSON
- Criação de um agente de IA com saída estruturada usando esquema JSON
- Execução de solicitações de planejamento com respostas tipadas

## Conceitos Principais

### Planejamento Estruturado com Modelos Tipados

O agente utiliza classes C# para definir a estrutura das saídas de planejamento:

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

O agente é configurado para retornar respostas que correspondem ao esquema TravelPlan:

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

### Instruções do Agente de Planejamento

O agente atua como um coordenador, delegando tarefas para subagentes especializados:

- FlightBooking: Para reservar voos e fornecer informações sobre voos
- HotelBooking: Para reservar hotéis e fornecer informações sobre hotéis
- CarRental: Para reservar carros e fornecer informações sobre aluguel de carros
- ActivitiesBooking: Para reservar atividades e fornecer informações sobre atividades
- DestinationInfo: Para fornecer informações sobre destinos
- DefaultAgent: Para lidar com solicitações gerais

## Saída Esperada

Quando você executa o agente com uma solicitação de planejamento de viagem, ele analisará a solicitação e gerará um plano estruturado com atribuições de tarefas apropriadas para agentes especializados, formatado como JSON conforme o esquema TravelPlan.

---

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.