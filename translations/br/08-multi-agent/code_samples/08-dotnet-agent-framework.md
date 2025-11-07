<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:15:48+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "br"
}
-->
# 🤝 Sistemas de Fluxo de Trabalho Multi-Agente Empresarial (.NET)

## 📋 Objetivos de Aprendizagem

Este notebook demonstra como construir sistemas multi-agente sofisticados de nível empresarial usando o Microsoft Agent Framework em .NET com Modelos do GitHub. Você aprenderá a orquestrar múltiplos agentes especializados trabalhando juntos por meio de fluxos de trabalho estruturados, aproveitando os recursos empresariais do .NET para soluções prontas para produção.

**Capacidades Multi-Agente Empresariais que Você Irá Desenvolver:**
- 👥 **Colaboração entre Agentes**: Coordenação de agentes com validação em tempo de compilação
- 🔄 **Orquestração de Fluxo de Trabalho**: Definição declarativa de fluxo de trabalho com padrões assíncronos do .NET
- 🎭 **Especialização de Funções**: Personalidades de agentes fortemente tipadas e domínios de especialização
- 🏢 **Integração Empresarial**: Padrões prontos para produção com monitoramento e tratamento de erros

## ⚙️ Pré-requisitos e Configuração

**Ambiente de Desenvolvimento:**
- SDK .NET 9.0 ou superior
- Visual Studio 2022 ou VS Code com extensão C#
- Assinatura do Azure (para agentes persistentes)

**Pacotes NuGet Necessários:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Exemplo de Código

O código completo funcional para esta lição está disponível no arquivo C# correspondente: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Para executar o exemplo:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Ou usando o CLI do .NET:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## O Que Este Exemplo Demonstra

Este sistema de fluxo de trabalho multi-agente cria um serviço de recomendação de viagens para hotéis com dois agentes especializados:

1. **Agente FrontDesk**: Um agente de viagens que fornece recomendações de atividades e locais
2. **Agente Concierge**: Revisa as recomendações para garantir experiências autênticas e não turísticas

Os agentes trabalham juntos em um fluxo de trabalho onde:
- O agente FrontDesk recebe a solicitação inicial de viagem
- O agente Concierge revisa e refina a recomendação
- O fluxo de trabalho transmite respostas em tempo real

## Conceitos Principais

### Coordenação de Agentes
O exemplo demonstra a coordenação de agentes com validação em tempo de compilação usando o Microsoft Agent Framework.

### Orquestração de Fluxo de Trabalho
Utiliza definição declarativa de fluxo de trabalho com padrões assíncronos do .NET para conectar múltiplos agentes em um pipeline.

### Respostas em Streaming
Implementa transmissão em tempo real de respostas dos agentes usando enumeráveis assíncronos e arquitetura orientada a eventos.

### Integração Empresarial
Mostra padrões prontos para produção, incluindo:
- Configuração de variáveis de ambiente
- Gerenciamento seguro de credenciais
- Tratamento de erros
- Processamento de eventos assíncronos

---

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.