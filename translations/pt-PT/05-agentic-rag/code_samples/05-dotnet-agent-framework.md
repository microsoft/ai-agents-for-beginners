# 🔍 RAG Empresarial com Microsoft Foundry (.NET)

## 📋 Objetivos de Aprendizagem

Este notebook demonstra como construir sistemas de Geração Aumentada por Recuperação (RAG) a nível empresarial, utilizando o Microsoft Agent Framework em .NET com Microsoft Foundry. Aprenderá a criar agentes prontos para produção que podem pesquisar documentos e fornecer respostas precisas, contextualmente relevantes, com segurança e escalabilidade empresariais.

**Capacidades Empresariais de RAG que irá Construir:**
- 📚 **Inteligência de Documentos**: Processamento avançado de documentos com serviços Azure AI
- 🔍 **Pesquisa Semântica**: Pesquisa vetorial de alto desempenho com funcionalidades empresariais
- 🛡️ **Integração de Segurança**: Acesso baseado em papéis e padrões de proteção de dados
- 🏢 **Arquitetura Escalável**: Sistemas RAG prontos para produção com monitorização

## 🎯 Arquitetura Empresarial RAG

### Componentes Empresariais Principais
- **Microsoft Foundry**: Plataforma empresarial de IA gerida com segurança e conformidade
- **Agentes Persistentes**: Agentes com estado, histórico de conversação e gestão de contexto
- **Gestão de Armazenamento Vetorial**: Indexação e recuperação de documentos de nível empresarial
- **Integração de Identidade**: Autenticação Azure AD e controlo de acesso baseado em papéis

### Benefícios do .NET Empresarial
- **Segurança de Tipos**: Validação em tempo de compilação para operações e estruturas de dados RAG
- **Desempenho Async**: Processamento e pesquisa de documentos não bloqueantes
- **Gestão de Memória**: Utilização eficiente de recursos para grandes coleções de documentos
- **Padrões de Integração**: Integração nativa de serviços Azure com injeção de dependências

## 🏗️ Arquitetura Técnica

### Pipeline RAG Empresarial
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Componentes Core .NET
- **Azure.AI.Agents.Persistent**: Gestão de agentes empresariais com persistência de estado
- **Azure.Identity**: Autenticação integrada para acesso seguro a serviços Azure
- **Microsoft.Agents.AI.AzureAI**: Implementação do framework de agentes otimizado para Azure
- **System.Linq.Async**: Operações LINQ assíncronas de alto desempenho

## 🔧 Funcionalidades e Benefícios Empresariais

### Segurança e Conformidade
- **Integração Azure AD**: Gestão de identidade empresarial e autenticação
- **Acesso Baseado em Papéis**: Permissões granulares para acesso e operações em documentos
- **Proteção de Dados**: Encriptação em repouso e em trânsito para documentos sensíveis
- **Registo de Auditoria**: Monitorização abrangente para requisitos de conformidade

### Desempenho e Escalabilidade
- **Pooling de Conexões**: Gestão eficiente de conexões a serviços Azure
- **Processamento Assíncrono**: Operações não bloqueantes para cenários de alto débito
- **Estratégias de Cache**: Cache inteligente para documentos acedidos frequentemente
- **Balanceamento de Carga**: Processamento distribuído para implantações em grande escala

### Gestão e Monitorização
- **Verificações de Saúde**: Monitorização integrada dos componentes do sistema RAG
- **Métricas de Desempenho**: Análises detalhadas sobre qualidade de pesquisa e tempos de resposta
- **Gestão de Erros**: Gestão abrangente de exceções com políticas de repetição
- **Gestão de Configuração**: Definições específicas por ambiente com validação

## ⚙️ Pré-requisitos e Configuração

**Ambiente de Desenvolvimento:**
- SDK .NET 9.0 ou superior
- Visual Studio 2022 ou VS Code com extensão C#
- Subscrição Azure com acesso ao Microsoft Foundry

**Pacotes NuGet Requeridos:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuração de Autenticação Azure:**
```bash
# Instale o Azure CLI e autentique-se
az login
az account set --subscription "your-subscription-id"
```

**Configuração do Ambiente:**
* Configuração Microsoft Foundry (gerida automaticamente via Azure CLI)
* Certifique-se de que está autenticado na subscrição correta do Azure

## 📊 Padrões RAG Empresariais

### Padrões de Gestão de Documentos
- **Upload em Massa**: Processamento eficiente de grandes coleções de documentos
- **Atualizações Incrementais**: Adição e modificação de documentos em tempo real
- **Gestão de Versões**: Versionamento de documentos e rastreio de alterações
- **Gestão de Metadados**: Atributos ricos de documentos e taxonomia

### Padrões de Pesquisa e Recuperação
- **Pesquisa Híbrida**: Combinação de pesquisa semântica e por palavras-chave para resultados ótimos
- **Pesquisa Facetada**: Filtragem multidimensional e categorização
- **Ajuste de Relevância**: Algoritmos de pontuação customizados para necessidades específicas de domínio
- **Ranking de Resultados**: Ordenação avançada com integração de lógica de negócio

### Padrões de Segurança
- **Segurança ao Nível de Documento**: Controlo de acesso granulado por documento
- **Classificação de Dados**: Rotulagem automática de sensibilidade e proteção
- **Traços de Auditoria**: Registo completo de todas as operações RAG
- **Proteção de Privacidade**: Capacidades de deteção e anonimização de dados pessoais

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
- **Encriptação**: Encriptação fim-a-fim para documentos e índices de pesquisa
- **Controlo de Acessos**: Integração com Azure AD para permissões de utilizadores e grupos
- **Residência de Dados**: Controlo geográfico da localização dos dados para conformidade
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
- **Processamento em Streaming**: Gerir documentos grandes sem problemas de memória
- **Pooling de Recursos**: Reutilização eficiente de recursos dispendiosos
- **Gestão de Lixo**: Padrões otimizados de alocação de memória
- **Gestão de Conexões**: Ciclo de vida adequado das conexões aos serviços Azure

### Estratégias de Cache
- **Cache de Consultas**: Cache de pesquisas realizadas frequentemente
- **Cache de Documentos**: Cache na memória para documentos "quentes"
- **Cache de Índice**: Cache otimizado de índices vetoriais
- **Cache de Resultados**: Cache inteligente das respostas geradas

## 📊 Casos de Uso Empresariais

### Gestão do Conhecimento
- **Wiki Corporativa**: Pesquisa inteligente através das bases de conhecimento da empresa
- **Políticas e Procedimentos**: Cumprimento automático e orientação de procedimentos
- **Materiais de Formação**: Assistência inteligente ao aprendizado e desenvolvimento
- **Bases de Dados de Investigação**: Sistemas de análise de artigos académicos e de investigação

### Suporte ao Cliente
- **Base de Conhecimento de Suporte**: Respostas automatizadas ao cliente
- **Documentação de Produto**: Recuperação inteligente de informações de produto
- **Guias de Resolução de Problemas**: Assistência contextual para resolução de problemas
- **Sistemas FAQ**: Geração dinâmica de FAQ a partir de coleções de documentos

### Conformidade Regulamentar
- **Análise de Documentos Legais**: Inteligência para contratos e documentos legais
- **Monitorização de Conformidade**: Verificação automática da conformidade regulatória
- **Avaliação de Risco**: Análise e reporte de risco baseado em documentos
- **Suporte a Auditorias**: Descoberta inteligente de documentos para auditorias

## 🚀 Implantação em Produção

### Monitorização e Observabilidade
- **Application Insights**: Telemetria detalhada e monitorização de desempenho
- **Métricas Customizadas**: Monitorização e alertas para KPIs de negócio específicos
- **Rastreamento Distribuído**: Monitorização fim-a-fim de pedidos entre serviços
- **Dashboards de Saúde**: Visualização em tempo real da saúde e desempenho do sistema

### Escalabilidade e Fiabilidade
- **Auto-Escala**: Escalão automático baseado na carga e métricas de desempenho
- **Alta Disponibilidade**: Implantação multi-região com capacidades de failover
- **Teste de Carga**: Validação de desempenho sob condições de carga empresarial
- **Recuperação de Desastres**: Procedimentos automáticos de backup e recuperação

Pronto para construir sistemas RAG a nível empresarial capazes de lidar com documentos sensíveis em escala? Vamos arquitetar sistemas inteligentes de conhecimento para a empresa! 🏢📖✨

## Implementação de Código

O exemplo completo e funcional de código para esta lição está disponível em `05-dotnet-agent-framework.cs`. 

Para executar o exemplo:

```bash
# Torne o script executável (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Execute a aplicação .NET de ficheiro único
./05-dotnet-agent-framework.cs
```

Ou use `dotnet run` diretamente:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

O código demonstra:

1. **Instalação de Pacotes**: Instalar os pacotes NuGet necessários para Azure AI Agents
2. **Configuração do Ambiente**: Carregar o endpoint Microsoft Foundry e definições do modelo
3. **Upload de Documento**: Enviar um documento para processamento RAG
4. **Criação do Armazenamento Vetorial**: Criar um armazenamento vetorial para pesquisa semântica
5. **Configuração do Agente**: Configurar um agente AI com capacidades de pesquisa de ficheiros
6. **Execução de Consultas**: Executar consultas contra o documento carregado

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->