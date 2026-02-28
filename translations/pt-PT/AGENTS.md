# AGENTS.md

## Visão Geral do Projeto

Este repositório contém "AI Agents for Beginners" - um curso educacional completo que ensina tudo o que é necessário para construir Agentes de IA. O curso consiste em 15+ lições que cobrem fundamentos, padrões de design, frameworks e implementação em produção de agentes de IA.

**Tecnologias principais:**
- Python 3.12+
- Jupyter Notebooks para aprendizagem interativa
- Frameworks de IA: Microsoft Agent Framework (MAF)
- Serviços Azure AI: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arquitetura:**
- Estrutura baseada em lições (diretórios 00-15+)
- Cada lição contém: documentação README, exemplos de código (Jupyter notebooks) e imagens
- Suporte multilíngue via sistema de tradução automática
- Um notebook Python por lição usando o Microsoft Agent Framework

## Comandos de Configuração

### Pré-requisitos
- Python 3.12 ou superior
- Subscrição Azure (para Azure AI Foundry)
- Azure CLI instalado e autenticado (`az login`)

### Configuração Inicial

1. **Clonar ou fork do repositório:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Criar e ativar um ambiente virtual Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variáveis de ambiente:**
   ```bash
   cp .env.example .env
   # Edite o ficheiro .env com as suas chaves de API e os endpoints
   ```

### Variáveis de Ambiente Necessárias

Para **Azure AI Foundry** (Obrigatório):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint do projeto Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nome da deployment do modelo (por exemplo, gpt-4o)

Para **Azure AI Search** (Lição 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint do Azure AI Search
- `AZURE_SEARCH_API_KEY` - chave de API do Azure AI Search

Autenticação: Execute `az login` antes de executar os notebooks (usa `AzureCliCredential`).

## Fluxo de Desenvolvimento

### Executar Jupyter Notebooks

Cada lição contém múltiplos Jupyter notebooks para diferentes frameworks:

1. **Iniciar o Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navegar até um diretório de lição** (por exemplo, `01-intro-to-ai-agents/code_samples/`)

3. **Abrir e executar notebooks:**
   - `*-python-agent-framework.ipynb` - Usando Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando Microsoft Agent Framework (.NET)

### Trabalhar com o Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Requer subscrição Azure
- Usa `AzureAIProjectAgentProvider` para Agent Service V2 (agentes visíveis no portal Foundry)
- Pronto para produção com observabilidade integrada
- Padrão de ficheiro: `*-python-agent-framework.ipynb`

## Instruções de Testes

Este é um repositório educacional com código de exemplo em vez de código de produção com testes automatizados. Para verificar a sua configuração e alterações:

### Testes Manuais

1. **Testar o ambiente Python:**
   ```bash
   python --version  # Deve ser 3.12 ou superior
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testar execução do notebook:**
   ```bash
   # Converter o notebook para script e executar (testa importações)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verificar variáveis de ambiente:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Executar Notebooks Individuais

Abra os notebooks no Jupyter e execute as células sequencialmente. Cada notebook é autónomo e inclui:
- Declarações de importação
- Carregamento de configuração
- Implementações de agente de exemplo
- Saídas esperadas em células markdown

## Estilo de Código

### Convenções Python

- **Versão do Python**: 3.12+
- **Estilo de Código**: Seguir as convenções padrão Python PEP 8
- **Notebooks**: Usar células markdown claras para explicar conceitos
- **Imports**: Agrupar por biblioteca padrão, de terceiros, imports locais

### Convenções de Jupyter Notebook

- Incluir células markdown descritivas antes das células de código
- Adicionar exemplos de saída nos notebooks como referência
- Usar nomes de variáveis claros que correspondam aos conceitos da lição
- Manter a ordem de execução do notebook linear (célula 1 → 2 → 3...)

### Organização de Ficheiros

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Compilação e Deployment

### Construção da Documentação

Este repositório usa Markdown para documentação:
- Ficheiros README.md em cada pasta de lição
- README.md principal na raiz do repositório
- Sistema de tradução automática via GitHub Actions

### Pipeline CI/CD

Localizado em `.github/workflows/`:

1. **co-op-translator.yml** - Tradução automática para 50+ idiomas
2. **welcome-issue.yml** - Dá as boas-vindas a criadores de issues novos
3. **welcome-pr.yml** - Dá as boas-vindas a contribuidores de pull requests

### Deployment

Este é um repositório educacional - sem processo de deployment. Utilizadores:
1. Fork ou clonar o repositório
2. Executar os notebooks localmente ou no GitHub Codespaces
3. Aprender modificando e experimentando com os exemplos

## Diretrizes para Pull Requests

### Antes de Submeter

1. **Testar as suas alterações:**
   - Executar completamente os notebooks afetados
   - Verificar que todas as células executam sem erros
   - Confirmar que as saídas são apropriadas

2. **Atualizações de documentação:**
   - Atualizar README.md se adicionar novos conceitos
   - Adicionar comentários nos notebooks para código complexo
   - Garantir que as células markdown explicam o propósito

3. **Alterações de ficheiros:**
   - Evitar commitar ficheiros `.env` (usar `.env.example`)
   - Não commitar diretórios `venv/` ou `__pycache__/`
   - Manter saídas de notebooks quando demonstram conceitos
   - Remover ficheiros temporários e notebooks de backup (`*-backup.ipynb`)

### Formato do Título do PR

Usar títulos descritivos:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Verificações Obrigatórias

- Notebooks devem executar sem erros
- Ficheiros README devem ser claros e precisos
- Seguir os padrões de código existentes no repositório
- Manter consistência com outras lições

## Notas Adicionais

### Armadilhas Comuns

1. **Incompatibilidade da versão do Python:**
   - Garantir que é usado Python 3.12+
   - Alguns pacotes podem não funcionar com versões antigas
   - Usar `python3 -m venv` para especificar explicitamente a versão do Python

2. **Variáveis de ambiente:**
   - Criar sempre `.env` a partir de `.env.example`
   - Não commitar o ficheiro `.env` (está em `.gitignore`)
   - O token do GitHub precisa de permissões apropriadas

3. **Conflitos de pacotes:**
   - Usar um ambiente virtual limpo
   - Instalar a partir de `requirements.txt` em vez de pacotes individuais
   - Alguns notebooks podem requerer pacotes adicionais mencionados nas suas células markdown

4. **Serviços Azure:**
   - Serviços Azure AI requerem subscrição ativa
   - Algumas funcionalidades são específicas por região
   - Aplicam-se limitações da camada gratuita para GitHub Models

### Rota de Aprendizagem

Progressão recomendada através das lições:
1. **00-course-setup** - Começar aqui para configuração do ambiente
2. **01-intro-to-ai-agents** - Compreender os fundamentos dos agentes de IA
3. **02-explore-agentic-frameworks** - Aprender sobre diferentes frameworks
4. **03-agentic-design-patterns** - Padrões de design essenciais
5. Continuar pelas lições numeradas sequencialmente

### Seleção de Framework

Escolher o framework com base nos seus objetivos:
- **Todas as lições**: Microsoft Agent Framework (MAF) com `AzureAIProjectAgentProvider`
- **Agentes registam-se no servidor** em Azure AI Foundry Agent Service V2 e são visíveis no portal Foundry

### Obter Ajuda

- Junte-se ao [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Reveja os ficheiros README das lições para orientação específica
- Consulte o [README.md](./README.md) principal para visão geral do curso
- Consulte [Course Setup](./00-course-setup/README.md) para instruções detalhadas de configuração

### Contribuir

Este é um projeto educacional aberto. Contribuições são bem-vindas:
- Melhorar exemplos de código
- Corrigir erros ou typos
- Adicionar comentários esclarecedores
- Sugerir novos tópicos de lições
- Traduzir para idiomas adicionais

Veja [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para necessidades atuais.

## Contexto Específico do Projeto

### Suporte Multilíngue

Este repositório usa um sistema de tradução automática:
- 50+ idiomas suportados
- Traduções em diretórios `/translations/<lang-code>/`
- Workflow do GitHub Actions gere atualizações de tradução
- Ficheiros fonte estão em inglês na raiz do repositório

### Estrutura da Lição

Cada lição segue um padrão consistente:
1. Miniatura de vídeo com link
2. Conteúdo escrito da lição (README.md)
3. Exemplos de código em múltiplos frameworks
4. Objetivos de aprendizagem e pré-requisitos
5. Recursos adicionais de aprendizagem linkados

### Nomeação de Exemplos de Código

Formato: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lição 1, MAF Python
- `14-sequential.ipynb` - Lição 14, padrões avançados MAF

### Diretórios Especiais

- `translated_images/` - Imagens localizadas para traduções
- `images/` - Imagens originais para conteúdo em inglês
- `.devcontainer/` - Configuração do contentor de desenvolvimento do VS Code
- `.github/` - Workflows e templates do GitHub Actions

### Dependências

Pacotes-chave em `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Suporte ao protocolo Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Serviços Azure AI
- `azure-identity` - Autenticação Azure (AzureCliCredential)
- `azure-search-documents` - Integração Azure AI Search
- `mcp[cli]` - Suporte ao Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos empenhemos na precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original, na sua língua original, deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->