# 🤝 Sistemas Empresariais de Fluxo de Trabalho Multiagente (.NET)

## 📋 Objetivos de Aprendizagem

Este notebook demonstra como construir sistemas sofisticados multiagentes de nível empresarial usando o Microsoft Agent Framework em .NET com Azure OpenAI (API de Respostas). Você aprenderá a orquestrar vários agentes especializados trabalhando juntos por meio de fluxos de trabalho estruturados, aproveitando os recursos empresariais do .NET para soluções prontas para produção.

**Capacidades Multiagentes Empresariais que Você Construirá:**
- 👥 **Colaboração de Agentes**: Coordenação segura por tipo com validação em tempo de compilação
- 🔄 **Orquestração de Fluxo de Trabalho**: Definição declarativa de fluxo de trabalho com padrões async do .NET
- 🎭 **Especialização de Função**: Personalidades de agentes fortemente tipadas e domínios de especialização
- 🏢 **Integração Empresarial**: Padrões prontos para produção com monitoramento e tratamento de erros

## ⚙️ Pré-requisitos e Configuração

**Ambiente de Desenvolvimento:**
- SDK .NET 9.0 ou superior
- Visual Studio 2022 ou VS Code com extensão C#
- Assinatura Azure (para agentes persistentes)

**Pacotes NuGet Necessários:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## Exemplo de Código

O código completo funcional para esta lição está disponível no arquivo C# acompanhante: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Para executar o exemplo:

```bash
# Torne o arquivo executável (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Execute o exemplo
./08-dotnet-agent-framework.cs
```

Ou usando o CLI do .NET:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## O Que Este Exemplo Demonstra

Este sistema de fluxo de trabalho multiagente cria um serviço de recomendação de viagens para hotéis com dois agentes especializados:

1. **Agente FrontDesk**: Um agente de viagens que fornece recomendações de atividades e locais
2. **Agente Concierge**: Revisa as recomendações para garantir experiências autênticas, não turísticas

Os agentes trabalham juntos em um fluxo de trabalho onde:
- O agente FrontDesk recebe a solicitação inicial de viagem
- O agente Concierge revisa e aprimora a recomendação
- O fluxo de trabalho transmite respostas em tempo real

## Conceitos-Chave

### Coordenação de Agentes
O exemplo demonstra coordenação segura por tipo de agentes usando o Microsoft Agent Framework com validação em tempo de compilação.

### Orquestração de Fluxo de Trabalho
Usa definição declarativa de fluxo de trabalho com padrões async do .NET para conectar múltiplos agentes em uma pipeline.

### Transmissão de Respostas
Implementa transmissão em tempo real das respostas dos agentes usando enumeráveis async e arquitetura orientada a eventos.

### Integração Empresarial
Mostra padrões prontos para produção incluindo:
- Configuração de variáveis de ambiente
- Gerenciamento seguro de credenciais
- Tratamento de erros
- Processamento assíncrono de eventos

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->