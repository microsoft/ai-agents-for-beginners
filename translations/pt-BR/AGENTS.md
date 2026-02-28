# AGENTS.md

## Visão Geral do Projeto

Este repositório contém "Agentes de IA para Iniciantes" - um curso educacional abrangente que ensina tudo o que é necessário para construir Agentes de IA. O curso consiste em mais de 15 aulas cobrindo fundamentos, padrões de design, frameworks e implantação em produção de agentes de IA.

**Tecnologias Principais:**
- Python 3.12+
- Jupyter Notebooks para aprendizado interativo
- Frameworks de IA: Microsoft Agent Framework (MAF)
- Serviços Azure AI: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arquitetura:**
- Estrutura baseada em lições (diretórios 00-15+)
- Cada lição contém: documentação README, exemplos de código (notebooks Jupyter) e imagens
- Suporte multilíngue via sistema automatizado de tradução
- Um notebook Python por lição usando Microsoft Agent Framework

## Comandos de Configuração

### Pré-requisitos
- Python 3.12 ou superior
- Assinatura Azure (para Azure AI Foundry)
- Azure CLI instalado e autenticado (`az login`)

### Configuração Inicial

1. **Clone ou faça fork do repositório:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Crie e ative o ambiente virtual Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   ```bash
   cp .env.example .env
   # Edite o arquivo .env com suas chaves de API e endpoints
   ```

### Variáveis de Ambiente Necessárias

Para **Azure AI Foundry** (Obrigatório):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint do projeto Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nome da implantação do modelo (ex: gpt-4o)

Para **Azure AI Search** (Lição 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint do Azure AI Search
- `AZURE_SEARCH_API_KEY` - chave API do Azure AI Search

Autenticação: Execute `az login` antes de rodar os notebooks (usa `AzureCliCredential`).

## Fluxo de Desenvolvimento

### Executando Jupyter Notebooks

Cada lição contém vários notebooks Jupyter para diferentes frameworks:

1. **Inicie o Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navegue até o diretório da lição** (ex: `01-intro-to-ai-agents/code_samples/`)

3. **Abra e execute os notebooks:**
   - `*-python-agent-framework.ipynb` - Usando Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando Microsoft Agent Framework (.NET)

### Trabalhando com Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Requer assinatura Azure
- Usa `AzureAIProjectAgentProvider` para o Agent Service V2 (agentes visíveis no portal Foundry)
- Pronto para produção com observabilidade integrada
- Padrão de arquivo: `*-python-agent-framework.ipynb`

## Instruções de Teste

Este é um repositório educacional com código exemplo, não código de produção com testes automatizados. Para verificar sua configuração e alterações:

### Teste Manual

1. **Teste o ambiente Python:**
   ```bash
   python --version  # Deve ser 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Teste a execução do notebook:**
   ```bash
   # Converter notebook para script e executar (testa importações)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifique as variáveis de ambiente:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Executando Notebooks Individualmente

Abra os notebooks no Jupyter e execute as células sequencialmente. Cada notebook é auto-contido e inclui:
- Declarações de importação
- Carregamento de configuração
- Exemplos de implementações de agentes
- Resultados esperados em células markdown

## Estilo de Código

### Convenções Python

- **Versão do Python**: 3.12+
- **Estilo de Código**: Siga as convenções padrão PEP 8 do Python
- **Notebooks**: Use células markdown claras para explicar conceitos
- **Imports**: Agrupe por biblioteca padrão, terceiros e locais

### Convenções para Jupyter Notebook

- Incluir células markdown descritivas antes das células de código
- Adicionar exemplos de saída nos notebooks para referência
- Usar nomes de variáveis claros que correspondam aos conceitos da lição
- Manter ordem linear de execução do notebook (célula 1 → 2 → 3...)

### Organização de Arquivos

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Construção e Implantação

### Construção da Documentação

Este repositório usa Markdown para documentação:
- Arquivos README.md em cada pasta de lição
- README.md principal na raiz do repositório
- Sistema automatizado de tradução via GitHub Actions

### Pipeline CI/CD

Localizado em `.github/workflows/`:

1. **co-op-translator.yml** - Tradução automática para mais de 50 idiomas
2. **welcome-issue.yml** - Dá boas-vindas a novos criadores de issues
3. **welcome-pr.yml** - Dá boas-vindas a novos contribuidores de pull request

### Implantação

Este é um repositório educacional - sem processo de implantação. Usuários:
1. Forkam ou clonam o repositório
2. Executam notebooks localmente ou no GitHub Codespaces
3. Aprendem modificando e experimentando os exemplos

## Diretrizes para Pull Requests

### Antes de Submeter

1. **Teste suas alterações:**
   - Execute completamente os notebooks afetados
   - Verifique se todas as células executam sem erros
   - Confirme que as saídas são apropriadas

2. **Atualizações de documentação:**
   - Atualize README.md se adicionar novos conceitos
   - Adicione comentários nos notebooks para código complexo
   - Assegure que as células markdown expliquem o propósito

3. **Mudanças em arquivos:**
   - Evite comitar arquivos `.env` (use `.env.example`)
   - Não comite diretórios `venv/` ou `__pycache__/`
   - Mantenha saídas do notebook quando demonstrarem conceitos
   - Remova arquivos temporários e backups de notebooks (`*-backup.ipynb`)

### Formato do Título do PR

Use títulos descritivos:
- `[Lesson-XX] Adicionar novo exemplo para <conceito>`
- `[Fix] Corrigir erro de digitação no README da lição XX`
- `[Update] Melhorar exemplo de código na lição XX`
- `[Docs] Atualizar instruções de configuração`

### Checagens Necessárias

- Notebooks devem executar sem erros
- Arquivos README devem ser claros e precisos
- Siga os padrões de código existentes no repositório
- Mantenha consistência com outras lições

## Notas Adicionais

### Problemas Comuns

1. **Incompatibilidade da versão do Python:**
   - Assegure que Python 3.12+ está em uso
   - Alguns pacotes podem não funcionar em versões mais antigas
   - Use `python3 -m venv` para especificar explicitamente a versão do Python

2. **Variáveis de ambiente:**
   - Sempre crie `.env` a partir de `.env.example`
   - Não comite o arquivo `.env` (está no `.gitignore`)
   - O token do GitHub precisa de permissões adequadas

3. **Conflitos de pacotes:**
   - Use um ambiente virtual limpo
   - Instale via `requirements.txt` ao invés de pacotes individuais
   - Alguns notebooks podem requerer pacotes adicionais mencionados nas células markdown

4. **Serviços Azure:**
   - Serviços Azure AI requerem assinatura ativa
   - Algumas funcionalidades são específicas por região
   - Limitações da camada gratuita aplicam-se aos Modelos GitHub

### Caminho de Aprendizagem

Progressão recomendada pelas lições:
1. **00-course-setup** - Comece aqui para configurar o ambiente
2. **01-intro-to-ai-agents** - Entenda os fundamentos dos agentes de IA
3. **02-explore-agentic-frameworks** - Conheça diferentes frameworks
4. **03-agentic-design-patterns** - Padrões centrais de design
5. Continue pelas lições numeradas sequencialmente

### Seleção de Framework

Escolha o framework com base em seus objetivos:
- **Todas as lições**: Microsoft Agent Framework (MAF) com `AzureAIProjectAgentProvider`
- **Agentes se registram no servidor** no Azure AI Foundry Agent Service V2 e são visíveis no portal Foundry

### Obter Ajuda

- Participe do [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Revise os arquivos README das lições para orientações específicas
- Consulte o [README.md principal](./README.md) para visão geral do curso
- Veja [Configuração do Curso](./00-course-setup/README.md) para instruções detalhadas

### Contribuindo

Este é um projeto educacional aberto. Contribuições são bem-vindas:
- Melhorar exemplos de código
- Corrigir erros de digitação ou bugs
- Adicionar comentários esclarecedores
- Sugerir novos tópicos para lições
- Traduzir para idiomas adicionais

Consulte [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para necessidades atuais.

## Contexto Específico do Projeto

### Suporte Multilíngue

Este repositório usa um sistema automático de tradução:
- Mais de 50 idiomas suportados
- Traduções em diretórios `/translations/<lang-code>/`
- Workflow GitHub Actions gerencia atualizações de tradução
- Arquivos fonte são em inglês na raiz do repositório

### Estrutura das Lições

Cada lição segue um padrão consistente:
1. Miniatura de vídeo com link
2. Conteúdo escrito da lição (README.md)
3. Exemplos de código em múltiplos frameworks
4. Objetivos de aprendizagem e pré-requisitos
5. Recursos extras de aprendizado linkados

### Nomeação dos Exemplos de Código

Formato: `<número-da-lição>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lição 1, MAF Python
- `14-sequential.ipynb` - Lição 14, padrões avançados MAF

### Diretórios Especiais

- `translated_images/` - Imagens localizadas para traduções
- `images/` - Imagens originais para conteúdo em inglês
- `.devcontainer/` - Configuração de container de desenvolvimento VS Code
- `.github/` - Workflows e templates do GitHub Actions

### Dependências

Pacotes chave do `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Suporte para protocolo Agente-para-Agente
- `azure-ai-inference`, `azure-ai-projects` - Serviços Azure AI
- `azure-identity` - Autenticação Azure (AzureCliCredential)
- `azure-search-documents` - Integração com Azure AI Search
- `mcp[cli]` - Suporte ao Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->