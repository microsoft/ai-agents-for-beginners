<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:01:32+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "pt"
}
-->
# 🔍 RAG Empresarial com Azure AI Foundry (.NET)

## 📋 Objetivos de Aprendizagem

Este notebook demonstra como construir sistemas de Recuperação e Geração Aumentada (RAG) de nível empresarial usando o Microsoft Agent Framework em .NET com Azure AI Foundry. Aprenderá a criar agentes prontos para produção que podem pesquisar documentos e fornecer respostas precisas e contextualizadas com segurança e escalabilidade empresarial.

**Funcionalidades RAG Empresariais que Irá Desenvolver:**
- 📚 **Inteligência de Documentos**: Processamento avançado de documentos com serviços Azure AI
- 🔍 **Pesquisa Semântica**: Pesquisa vetorial de alto desempenho com recursos empresariais
- 🛡️ **Integração de Segurança**: Controle de acesso baseado em funções e padrões de proteção de dados
- 🏢 **Arquitetura Escalável**: Sistemas RAG prontos para produção com monitorização

## 🎯 Arquitetura RAG Empresarial

### Componentes Empresariais Principais
- **Azure AI Foundry**: Plataforma de IA empresarial gerida com segurança e conformidade
- **Agentes Persistentes**: Agentes com estado persistente, histórico de conversação e gestão de contexto
- **Gestão de Armazenamento Vetorial**: Indexação e recuperação de documentos de nível empresarial
- **Integração de Identidade**: Autenticação Azure AD e controle de acesso baseado em funções

### Benefícios Empresariais do .NET
- **Segurança de Tipos**: Validação em tempo de compilação para operações RAG e estruturas de dados
- **Desempenho Assíncrono**: Processamento de documentos e operações de pesquisa não bloqueantes
- **Gestão de Memória**: Utilização eficiente de recursos para coleções de documentos grandes
- **Padrões de Integração**: Integração nativa com serviços Azure usando injeção de dependência

## 🏗️ Arquitetura Técnica

### Pipeline RAG Empresarial
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Componentes Principais do .NET
- **Azure.AI.Agents.Persistent**: Gestão de agentes empresariais com persistência de estado
- **Azure.Identity**: Autenticação integrada para acesso seguro a serviços Azure
- **Microsoft.Agents.AI.AzureAI**: Implementação do framework de agentes otimizado para Azure
- **System.Linq.Async**: Operações LINQ assíncronas de alto desempenho

## 🔧 Funcionalidades e Benefícios Empresariais

### Segurança e Conformidade
- **Integração Azure AD**: Gestão de identidade empresarial e autenticação
- **Acesso Baseado em Funções**: Permissões detalhadas para acesso e operações em documentos
- **Proteção de Dados**: Criptografia em repouso e em trânsito para documentos sensíveis
- **Registo de Auditoria**: Monitorização abrangente de atividades para requisitos de conformidade

### Desempenho e Escalabilidade
- **Pooling de Conexões**: Gestão eficiente de conexões com serviços Azure
- **Processamento Assíncrono**: Operações não bloqueantes para cenários de alta capacidade
- **Estratégias de Cache**: Cache inteligente para documentos frequentemente acessados
- **Balanceamento de Carga**: Processamento distribuído para implementações em larga escala

### Gestão e Monitorização
- **Verificações de Saúde**: Monitorização integrada para componentes do sistema RAG
- **Métricas de Desempenho**: Análises detalhadas sobre qualidade de pesquisa e tempos de resposta
- **Gestão de Erros**: Gestão abrangente de exceções com políticas de repetição
- **Gestão de Configuração**: Configurações específicas do ambiente com validação

## ⚙️ Pré-requisitos e Configuração

**Ambiente de Desenvolvimento:**
- SDK .NET 9.0 ou superior
- Visual Studio 2022 ou VS Code com extensão C#
- Subscrição Azure com acesso ao AI Foundry

**Pacotes NuGet Necessários:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuração de Autenticação Azure:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Configuração do Ambiente:**
* Configuração do Azure AI Foundry (gerida automaticamente via Azure CLI)
* Certifique-se de que está autenticado na subscrição Azure correta

## 📊 Padrões RAG Empresariais

### Padrões de Gestão de Documentos
- **Carregamento em Massa**: Processamento eficiente de grandes coleções de documentos
- **Atualizações Incrementais**: Adição e modificação de documentos em tempo real
- **Controlo de Versões**: Versionamento de documentos e rastreamento de alterações
- **Gestão de Metadados**: Atributos ricos de documentos e taxonomia

### Padrões de Pesquisa e Recuperação
- **Pesquisa Híbrida**: Combinação de pesquisa semântica e por palavras-chave para resultados ótimos
- **Pesquisa Facetada**: Filtragem e categorização multidimensional
- **Ajuste de Relevância**: Algoritmos de pontuação personalizados para necessidades específicas do domínio
- **Classificação de Resultados**: Classificação avançada com integração de lógica empresarial

### Padrões de Segurança
- **Segurança ao Nível do Documento**: Controle de acesso detalhado por documento
- **Classificação de Dados**: Rotulagem automática de sensibilidade e proteção
- **Registos de Auditoria**: Registo abrangente de todas as operações RAG
- **Proteção de Privacidade**: Detecção e redação de PII

## 🔒 Funcionalidades de Segurança Empresarial

### Autenticação e Autorização
```csharp
// Azure AD integrated authentication
var credential = new AzureCliCredential();
var agentsClient = new PersistentAgentsClient(endpoint, credential);

// Role-based access validation
if (!await ValidateUserPermissions(user, documentId))
{
    throw new UnauthorizedAccessException("Insufficient permissions");
}
```

### Proteção de Dados
- **Criptografia**: Criptografia ponta a ponta para documentos e índices de pesquisa
- **Controles de Acesso**: Integração com Azure AD para permissões de utilizadores e grupos
- **Residência de Dados**: Controles de localização geográfica de dados para conformidade
- **Backup e Recuperação**: Capacidades automáticas de backup e recuperação de desastres

## 📈 Otimização de Desempenho

### Padrões de Processamento Assíncrono
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Gestão de Memória
- **Processamento em Fluxo**: Manipulação de documentos grandes sem problemas de memória
- **Pooling de Recursos**: Reutilização eficiente de recursos dispendiosos
- **Coleta de Lixo**: Padrões otimizados de alocação de memória
- **Gestão de Conexões**: Ciclo de vida adequado de conexões com serviços Azure

### Estratégias de Cache
- **Cache de Consultas**: Cache de pesquisas frequentemente executadas
- **Cache de Documentos**: Cache em memória para documentos mais acessados
- **Cache de Índices**: Cache otimizado de índices vetoriais
- **Cache de Resultados**: Cache inteligente de respostas geradas

## 📊 Casos de Uso Empresariais

### Gestão de Conhecimento
- **Wiki Corporativa**: Pesquisa inteligente em bases de conhecimento da empresa
- **Políticas e Procedimentos**: Orientação automatizada de conformidade e procedimentos
- **Materiais de Treinamento**: Assistência inteligente para aprendizagem e desenvolvimento
- **Bases de Dados de Pesquisa**: Sistemas de análise de artigos académicos e de pesquisa

### Suporte ao Cliente
- **Base de Conhecimento de Suporte**: Respostas automatizadas para atendimento ao cliente
- **Documentação de Produtos**: Recuperação inteligente de informações sobre produtos
- **Guias de Resolução de Problemas**: Assistência contextual para resolução de problemas
- **Sistemas de FAQ**: Geração dinâmica de FAQs a partir de coleções de documentos

### Conformidade Regulamentar
- **Análise de Documentos Legais**: Inteligência em contratos e documentos legais
- **Monitorização de Conformidade**: Verificação automatizada de conformidade regulatória
- **Avaliação de Riscos**: Análise e relatórios de riscos baseados em documentos
- **Suporte a Auditorias**: Descoberta inteligente de documentos para auditorias

## 🚀 Implementação em Produção

### Monitorização e Observabilidade
- **Application Insights**: Telemetria detalhada e monitorização de desempenho
- **Métricas Personalizadas**: Monitorização e alertas de KPIs específicos do negócio
- **Rastreamento Distribuído**: Rastreamento de pedidos de ponta a ponta entre serviços
- **Dashboards de Saúde**: Visualização em tempo real da saúde e desempenho do sistema

### Escalabilidade e Confiabilidade
- **Auto-Escala**: Escalabilidade automática baseada em carga e métricas de desempenho
- **Alta Disponibilidade**: Implementação multi-região com capacidades de failover
- **Teste de Carga**: Validação de desempenho sob condições de carga empresarial
- **Recuperação de Desastres**: Procedimentos automáticos de backup e recuperação

Pronto para construir sistemas RAG empresariais que podem lidar com documentos sensíveis em escala? Vamos arquitetar sistemas inteligentes de conhecimento para empresas! 🏢📖✨

## Implementação de Código

O exemplo completo de código funcional para esta lição está disponível em `05-dotnet-agent-framework.cs`. 

Para executar o exemplo:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Ou use `dotnet run` diretamente:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

O código demonstra:

1. **Instalação de Pacotes**: Instalação de pacotes NuGet necessários para Azure AI Agents
2. **Configuração do Ambiente**: Carregamento de endpoint e configurações de modelo do Azure AI Foundry
3. **Carregamento de Documentos**: Carregamento de um documento para processamento RAG
4. **Criação de Armazenamento Vetorial**: Criação de armazenamento vetorial para pesquisa semântica
5. **Configuração de Agente**: Configuração de um agente de IA com capacidades de pesquisa de arquivos
6. **Execução de Consultas**: Execução de consultas contra o documento carregado

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.