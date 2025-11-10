<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:01:50+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "br"
}
-->
# 🔍 RAG Empresarial com Azure AI Foundry (.NET)

## 📋 Objetivos de Aprendizagem

Este notebook demonstra como construir sistemas de Recuperação e Geração Aumentada (RAG) de nível empresarial usando o Microsoft Agent Framework em .NET com Azure AI Foundry. Você aprenderá a criar agentes prontos para produção que podem buscar documentos e fornecer respostas precisas e contextualizadas com segurança e escalabilidade empresarial.

**Recursos de RAG Empresarial que Você Vai Construir:**
- 📚 **Inteligência de Documentos**: Processamento avançado de documentos com serviços Azure AI
- 🔍 **Busca Semântica**: Busca vetorial de alto desempenho com recursos empresariais
- 🛡️ **Integração de Segurança**: Controle de acesso baseado em funções e padrões de proteção de dados
- 🏢 **Arquitetura Escalável**: Sistemas RAG prontos para produção com monitoramento

## 🎯 Arquitetura de RAG Empresarial

### Componentes Principais Empresariais
- **Azure AI Foundry**: Plataforma de IA empresarial gerenciada com segurança e conformidade
- **Agentes Persistentes**: Agentes com estado persistente, histórico de conversas e gerenciamento de contexto
- **Gerenciamento de Armazenamento Vetorial**: Indexação e recuperação de documentos de nível empresarial
- **Integração de Identidade**: Autenticação Azure AD e controle de acesso baseado em funções

### Benefícios Empresariais do .NET
- **Segurança de Tipos**: Validação em tempo de compilação para operações RAG e estruturas de dados
- **Desempenho Assíncrono**: Processamento de documentos e operações de busca não bloqueantes
- **Gerenciamento de Memória**: Utilização eficiente de recursos para grandes coleções de documentos
- **Padrões de Integração**: Integração nativa com serviços Azure usando injeção de dependência

## 🏗️ Arquitetura Técnica

### Pipeline de RAG Empresarial
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Componentes Principais do .NET
- **Azure.AI.Agents.Persistent**: Gerenciamento de agentes empresariais com persistência de estado
- **Azure.Identity**: Autenticação integrada para acesso seguro aos serviços Azure
- **Microsoft.Agents.AI.AzureAI**: Implementação do framework de agentes otimizado para Azure
- **System.Linq.Async**: Operações LINQ assíncronas de alto desempenho

## 🔧 Recursos e Benefícios Empresariais

### Segurança e Conformidade
- **Integração com Azure AD**: Gerenciamento de identidade empresarial e autenticação
- **Acesso Baseado em Funções**: Permissões detalhadas para acesso e operações em documentos
- **Proteção de Dados**: Criptografia em repouso e em trânsito para documentos sensíveis
- **Registro de Auditoria**: Rastreamento abrangente de atividades para requisitos de conformidade

### Desempenho e Escalabilidade
- **Pooling de Conexões**: Gerenciamento eficiente de conexões com serviços Azure
- **Processamento Assíncrono**: Operações não bloqueantes para cenários de alta demanda
- **Estratégias de Cache**: Cache inteligente para documentos acessados frequentemente
- **Balanceamento de Carga**: Processamento distribuído para implantações em larga escala

### Gerenciamento e Monitoramento
- **Verificações de Saúde**: Monitoramento integrado para componentes do sistema RAG
- **Métricas de Desempenho**: Análises detalhadas sobre qualidade de busca e tempos de resposta
- **Tratamento de Erros**: Gerenciamento abrangente de exceções com políticas de repetição
- **Gerenciamento de Configuração**: Configurações específicas de ambiente com validação

## ⚙️ Pré-requisitos e Configuração

**Ambiente de Desenvolvimento:**
- SDK .NET 9.0 ou superior
- Visual Studio 2022 ou VS Code com extensão C#
- Assinatura Azure com acesso ao AI Foundry

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

**Configuração de Ambiente:**
* Configuração do Azure AI Foundry (gerenciada automaticamente via Azure CLI)
* Certifique-se de estar autenticado na assinatura Azure correta

## 📊 Padrões de RAG Empresarial

### Padrões de Gerenciamento de Documentos
- **Upload em Massa**: Processamento eficiente de grandes coleções de documentos
- **Atualizações Incrementais**: Adição e modificação de documentos em tempo real
- **Controle de Versão**: Versionamento de documentos e rastreamento de alterações
- **Gerenciamento de Metadados**: Atributos ricos de documentos e taxonomia

### Padrões de Busca e Recuperação
- **Busca Híbrida**: Combinação de busca semântica e por palavras-chave para resultados ideais
- **Busca Facetada**: Filtragem e categorização multidimensional
- **Ajuste de Relevância**: Algoritmos de pontuação personalizados para necessidades específicas do domínio
- **Classificação de Resultados**: Classificação avançada com integração de lógica de negócios

### Padrões de Segurança
- **Segurança em Nível de Documento**: Controle de acesso detalhado por documento
- **Classificação de Dados**: Rotulagem automática de sensibilidade e proteção
- **Trilhas de Auditoria**: Registro abrangente de todas as operações RAG
- **Proteção de Privacidade**: Detecção e redação de PII (Informações Pessoais Identificáveis)

## 🔒 Recursos de Segurança Empresarial

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
- **Criptografia**: Criptografia ponta a ponta para documentos e índices de busca
- **Controles de Acesso**: Integração com Azure AD para permissões de usuários e grupos
- **Residência de Dados**: Controle de localização geográfica de dados para conformidade
- **Backup e Recuperação**: Recursos automatizados de backup e recuperação de desastres

## 📈 Otimização de Desempenho

### Padrões de Processamento Assíncrono
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Gerenciamento de Memória
- **Processamento em Streaming**: Manipulação de grandes documentos sem problemas de memória
- **Pooling de Recursos**: Reutilização eficiente de recursos caros
- **Coleta de Lixo**: Padrões otimizados de alocação de memória
- **Gerenciamento de Conexões**: Ciclo de vida adequado de conexões com serviços Azure

### Estratégias de Cache
- **Cache de Consultas**: Cache de buscas executadas frequentemente
- **Cache de Documentos**: Cache em memória para documentos mais acessados
- **Cache de Índices**: Cache otimizado de índices vetoriais
- **Cache de Resultados**: Cache inteligente de respostas geradas

## 📊 Casos de Uso Empresariais

### Gerenciamento de Conhecimento
- **Wiki Corporativo**: Busca inteligente em bases de conhecimento da empresa
- **Políticas e Procedimentos**: Orientação automatizada de conformidade e procedimentos
- **Materiais de Treinamento**: Assistência inteligente para aprendizado e desenvolvimento
- **Bases de Dados de Pesquisa**: Sistemas de análise de artigos acadêmicos e de pesquisa

### Suporte ao Cliente
- **Base de Conhecimento de Suporte**: Respostas automatizadas para atendimento ao cliente
- **Documentação de Produtos**: Recuperação inteligente de informações sobre produtos
- **Guias de Solução de Problemas**: Assistência contextual para resolução de problemas
- **Sistemas de FAQ**: Geração dinâmica de FAQs a partir de coleções de documentos

### Conformidade Regulamentar
- **Análise de Documentos Legais**: Inteligência em contratos e documentos legais
- **Monitoramento de Conformidade**: Verificação automatizada de conformidade regulatória
- **Avaliação de Riscos**: Análise e relatórios de riscos baseados em documentos
- **Suporte a Auditorias**: Descoberta inteligente de documentos para auditorias

## 🚀 Implantação em Produção

### Monitoramento e Observabilidade
- **Application Insights**: Telemetria detalhada e monitoramento de desempenho
- **Métricas Personalizadas**: Rastreamento e alertas de KPIs específicos de negócios
- **Rastreamento Distribuído**: Rastreamento de solicitações de ponta a ponta entre serviços
- **Painéis de Saúde**: Visualização em tempo real da saúde e desempenho do sistema

### Escalabilidade e Confiabilidade
- **Autoescalonamento**: Escalonamento automático com base em carga e métricas de desempenho
- **Alta Disponibilidade**: Implantação em várias regiões com capacidades de failover
- **Teste de Carga**: Validação de desempenho sob condições de carga empresarial
- **Recuperação de Desastres**: Procedimentos automatizados de backup e recuperação

Pronto para construir sistemas RAG de nível empresarial que podem lidar com documentos sensíveis em escala? Vamos arquitetar sistemas inteligentes de conhecimento para empresas! 🏢📖✨

## Implementação de Código

O código completo funcional para esta lição está disponível em `05-dotnet-agent-framework.cs`. 

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
2. **Configuração de Ambiente**: Carregamento de endpoint e configurações de modelo do Azure AI Foundry
3. **Upload de Documentos**: Upload de um documento para processamento RAG
4. **Criação de Armazenamento Vetorial**: Criação de armazenamento vetorial para busca semântica
5. **Configuração de Agente**: Configuração de um agente de IA com capacidades de busca em arquivos
6. **Execução de Consultas**: Execução de consultas contra o documento carregado

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.