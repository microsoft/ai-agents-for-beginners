# 🤝 Sistemas Empresariais de Fluxo de Trabalho Multi-Agente (.NET)

## 📋 Objetivos de Aprendizagem

Este caderno demonstra como construir sistemas multi-agente sofisticados de nível empresarial usando o Microsoft Agent Framework em .NET com Azure OpenAI (API de Respostas). Vai aprender a orquestrar múltiplos agentes especializados a trabalhar em conjunto através de fluxos de trabalho estruturados, aproveitando as funcionalidades empresariais do .NET para soluções prontas para produção.

**Capacidades Multi-Agente Empresariais que Vai Construir:**
- 👥 **Colaboração entre Agentes**: Coordenação segura por tipo dos agentes com validação em tempo de compilação
- 🔄 **Orquestração de Fluxos de Trabalho**: Definição declarativa de fluxos de trabalho com padrões async do .NET
- 🎭 **Especialização de Funções**: Personalidades e domínios de especialização dos agentes fortemente tipados
- 🏢 **Integração Empresarial**: Padrões prontos para produção com monitorização e tratamento de erros

## ⚙️ Pré-requisitos e Configuração

**Ambiente de Desenvolvimento:**
- SDK .NET 9.0 ou superior
- Visual Studio 2022 ou VS Code com extensão C#
- Subscrição Azure (para agentes persistentes)

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

O código funcional completo desta lição está disponível no ficheiro C# acompanhante: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Para executar o exemplo:

```bash
# Torne o ficheiro executável (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Execute o exemplo
./08-dotnet-agent-framework.cs
```

Ou usando a CLI do .NET:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## O que Este Exemplo Demonstra

Este sistema de fluxo de trabalho multi-agente cria um serviço de recomendação de viagens para hotéis com dois agentes especializados:

1. **Agente da Receção**: Um agente de viagens que fornece recomendações de atividades e locais
2. **Agente Concierge**: Revê as recomendações para garantir experiências autênticas, não turísticas

Os agentes trabalham juntos num fluxo de trabalho onde:
- O agente da Receção recebe o pedido inicial de viagem
- O agente Concierge revê e aprimora a recomendação
- O fluxo transmite respostas em tempo real

## Conceitos-Chave

### Coordenação de Agentes
O exemplo demonstra coordenação segura por tipo dos agentes usando o Microsoft Agent Framework com validação em tempo de compilação.

### Orquestração de Fluxos de Trabalho
Utiliza definição declarativa de fluxos de trabalho com padrões async do .NET para ligar múltiplos agentes numa pipeline.

### Transmissão em Streaming das Respostas
Implementa transmissão em tempo real das respostas dos agentes usando enumeráveis async e arquitetura orientada a eventos.

### Integração Empresarial
Mostra padrões prontos para produção incluindo:
- Configuração por variáveis de ambiente
- Gestão segura de credenciais
- Tratamento de erros
- Processamento assíncrono de eventos

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->