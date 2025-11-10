<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:23:58+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "pt"
}
-->
# 🛠️ Uso Avançado de Ferramentas com Modelos do GitHub (.NET)

## 📋 Objetivos de Aprendizagem

Este notebook demonstra padrões de integração de ferramentas de nível empresarial utilizando o Microsoft Agent Framework em .NET com Modelos do GitHub. Aprenderá a construir agentes sofisticados com múltiplas ferramentas especializadas, aproveitando a tipagem forte do C# e os recursos empresariais do .NET.

**Capacidades Avançadas de Ferramentas que Irá Dominar:**
- 🔧 **Arquitetura Multi-Ferramentas**: Construção de agentes com múltiplas capacidades especializadas
- 🎯 **Execução de Ferramentas com Tipagem Segura**: Aproveitamento da validação em tempo de compilação do C#
- 📊 **Padrões de Ferramentas Empresariais**: Design de ferramentas pronto para produção e gestão de erros
- 🔗 **Composição de Ferramentas**: Combinação de ferramentas para fluxos de trabalho empresariais complexos

## 🎯 Benefícios da Arquitetura de Ferramentas em .NET

### Funcionalidades de Ferramentas Empresariais
- **Validação em Tempo de Compilação**: Tipagem forte garante a correção dos parâmetros das ferramentas
- **Injeção de Dependências**: Integração com contêiner IoC para gestão de ferramentas
- **Padrões Async/Await**: Execução de ferramentas não bloqueante com gestão adequada de recursos
- **Registo Estruturado**: Integração de registo incorporado para monitorização da execução de ferramentas

### Padrões Prontos para Produção
- **Gestão de Exceções**: Gestão abrangente de erros com exceções tipadas
- **Gestão de Recursos**: Padrões adequados de descarte e gestão de memória
- **Monitorização de Desempenho**: Métricas incorporadas e contadores de desempenho
- **Gestão de Configuração**: Configuração com tipagem segura e validação

## 🔧 Arquitetura Técnica

### Componentes Principais de Ferramentas em .NET
- **Microsoft.Extensions.AI**: Camada de abstração unificada para ferramentas
- **Microsoft.Agents.AI**: Orquestração de ferramentas de nível empresarial
- **Integração com Modelos do GitHub**: Cliente API de alto desempenho com pooling de conexões

### Pipeline de Execução de Ferramentas
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Categorias e Padrões de Ferramentas

### 1. **Ferramentas de Processamento de Dados**
- **Validação de Entrada**: Tipagem forte com anotações de dados
- **Operações de Transformação**: Conversão e formatação de dados com tipagem segura
- **Lógica Empresarial**: Ferramentas de cálculo e análise específicas do domínio
- **Formatação de Saída**: Geração de respostas estruturadas

### 2. **Ferramentas de Integração** 
- **Conectores de API**: Integração com serviços RESTful utilizando HttpClient
- **Ferramentas de Base de Dados**: Integração com Entity Framework para acesso a dados
- **Operações de Ficheiros**: Operações seguras no sistema de ficheiros com validação
- **Serviços Externos**: Padrões de integração com serviços de terceiros

### 3. **Ferramentas Utilitárias**
- **Processamento de Texto**: Manipulação e formatação de strings
- **Operações de Data/Hora**: Cálculos de data/hora sensíveis à cultura
- **Ferramentas Matemáticas**: Cálculos de precisão e operações estatísticas
- **Ferramentas de Validação**: Validação de regras empresariais e verificação de dados

## ⚙️ Pré-requisitos e Configuração

**Ambiente de Desenvolvimento:**
- SDK .NET 9.0 ou superior
- Visual Studio 2022 ou VS Code com extensão C#
- Acesso à API de Modelos do GitHub

**Pacotes NuGet Necessários:**
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

Pronto para construir agentes de nível empresarial com capacidades poderosas e ferramentas com tipagem segura em .NET? Vamos arquitetar soluções de nível profissional! 🏢⚡

## 💻 Implementação de Código

A implementação completa em C# está disponível no ficheiro complementar `04-dotnet-agent-framework.cs`. Esta aplicação única em .NET demonstra:

- Carregamento de variáveis de ambiente para configuração dos Modelos do GitHub
- Definição de ferramentas personalizadas utilizando métodos C# com atributos
- Criação de um agente de IA com integração de ferramentas
- Gestão de threads de conversação
- Execução de pedidos do agente com invocação de ferramentas

Para executar o exemplo:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Ou utilizando o CLI do .NET:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.