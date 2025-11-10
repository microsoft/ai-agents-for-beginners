<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:24:09+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "br"
}
-->
# 🛠️ Uso Avançado de Ferramentas com Modelos do GitHub (.NET)

## 📋 Objetivos de Aprendizado

Este notebook demonstra padrões de integração de ferramentas de nível empresarial usando o Microsoft Agent Framework em .NET com Modelos do GitHub. Você aprenderá a construir agentes sofisticados com múltiplas ferramentas especializadas, aproveitando a tipagem forte do C# e os recursos empresariais do .NET.

**Capacidades Avançadas de Ferramentas que Você Dominará:**
- 🔧 **Arquitetura Multi-Ferramentas**: Construção de agentes com múltiplas capacidades especializadas
- 🎯 **Execução de Ferramentas com Tipagem Segura**: Aproveitando a validação em tempo de compilação do C#
- 📊 **Padrões de Ferramentas Empresariais**: Design de ferramentas pronto para produção e tratamento de erros
- 🔗 **Composição de Ferramentas**: Combinação de ferramentas para fluxos de trabalho complexos de negócios

## 🎯 Benefícios da Arquitetura de Ferramentas .NET

### Recursos de Ferramentas Empresariais
- **Validação em Tempo de Compilação**: Tipagem forte garante a correção dos parâmetros das ferramentas
- **Injeção de Dependência**: Integração com contêiner IoC para gerenciamento de ferramentas
- **Padrões Async/Await**: Execução de ferramentas não bloqueante com gerenciamento adequado de recursos
- **Log Estruturado**: Integração de logs embutidos para monitoramento da execução de ferramentas

### Padrões Prontos para Produção
- **Tratamento de Exceções**: Gerenciamento abrangente de erros com exceções tipadas
- **Gerenciamento de Recursos**: Padrões adequados de descarte e gerenciamento de memória
- **Monitoramento de Desempenho**: Métricas embutidas e contadores de desempenho
- **Gerenciamento de Configuração**: Configuração com tipagem segura e validação

## 🔧 Arquitetura Técnica

### Componentes Principais de Ferramentas .NET
- **Microsoft.Extensions.AI**: Camada de abstração unificada para ferramentas
- **Microsoft.Agents.AI**: Orquestração de ferramentas de nível empresarial
- **Integração com Modelos do GitHub**: Cliente de API de alto desempenho com pool de conexões

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
- **Lógica de Negócios**: Ferramentas de cálculo e análise específicas do domínio
- **Formatação de Saída**: Geração de respostas estruturadas

### 2. **Ferramentas de Integração**
- **Conectores de API**: Integração com serviços RESTful usando HttpClient
- **Ferramentas de Banco de Dados**: Integração com Entity Framework para acesso a dados
- **Operações de Arquivo**: Operações seguras no sistema de arquivos com validação
- **Serviços Externos**: Padrões de integração com serviços de terceiros

### 3. **Ferramentas Utilitárias**
- **Processamento de Texto**: Manipulação e formatação de strings
- **Operações de Data/Hora**: Cálculos de data/hora sensíveis à cultura
- **Ferramentas Matemáticas**: Cálculos precisos e operações estatísticas
- **Ferramentas de Validação**: Validação de regras de negócios e verificação de dados

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

**Configuração de Ambiente (arquivo .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Pronto para construir agentes de nível empresarial com capacidades poderosas e ferramentas com tipagem segura em .NET? Vamos arquitetar soluções de nível profissional! 🏢⚡

## 💻 Implementação de Código

A implementação completa em C# está disponível no arquivo complementar `04-dotnet-agent-framework.cs`. Este aplicativo de arquivo único .NET demonstra:

- Carregamento de variáveis de ambiente para configuração dos Modelos do GitHub
- Definição de ferramentas personalizadas usando métodos C# com atributos
- Criação de um agente de IA com integração de ferramentas
- Gerenciamento de threads de conversação
- Execução de solicitações do agente com invocação de ferramentas

Para executar o exemplo:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Ou usando o CLI do .NET:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.