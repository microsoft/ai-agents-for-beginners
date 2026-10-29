# AGENTS.md

## Visão Geral do Projeto

Este repositório contém "Agentes de IA para Iniciantes" - um curso educacional abrangente que ensina tudo o que é necessário para construir Agentes de IA. O curso consiste em 18 lições (numeradas de 00 a 18) abordando fundamentos, padrões de design, frameworks, implantação em produção, agentes locais/no dispositivo e segurança de agentes de IA.

**Tecnologias Principais:**
- Python 3.12+
- Jupyter Notebooks para aprendizagem interativa
- Frameworks de IA: Microsoft Agent Framework (MAF)
- Serviços Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arquitetura:**
- Estrutura baseada em lições (pastas 00-18)
- Cada lição contém: documentação README, exemplos de código (notebooks Jupyter) e imagens
- Suporte multilíngue via sistema automático de tradução
- Um notebook Python por lição usando o Microsoft Agent Framework

## Comandos de Configuração

### Pré-requisitos
- Python 3.12 ou superior
- Assinatura Azure (para Microsoft Foundry)
- Azure CLI instalado e autenticado (`az login`)

### Configuração Inicial

1. **Clone ou faça fork do repositório:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Crie e ative um ambiente virtual Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Variáveis de Ambiente Necessárias

Para **Microsoft Foundry** (Obrigatório):
- `AZURE_AI_PROJECT_ENDPOINT` - Endpoint do projeto Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Nome da implantação do modelo (ex: gpt-5-mini)

Para **Azure AI Search** (Lição 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - Chave API Azure AI Search

Autenticação: Execute `az login` antes de rodar os notebooks (usa `AzureCliCredential`).

## Fluxo de Desenvolvimento

### Execução dos Jupyter Notebooks

Cada lição contém múltiplos notebooks Jupyter para diferentes frameworks:

1. **Inicie o Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navegue até a pasta da lição** (exemplo: `01-intro-to-ai-agents/code_samples/`)

3. **Abra e execute os notebooks:**
   - `*-python-agent-framework.ipynb` - Usando Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando Microsoft Agent Framework (.NET)

### Trabalhando com Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Requer assinatura Azure
- Usa `FoundryChatClient` para Agent Service V2 (agentes visíveis no portal Foundry)
- Pronto para produção com observabilidade embutida
- Padrão de arquivo: `*-python-agent-framework.ipynb`

## Instruções de Teste

Este é um repositório educacional com código de exemplo, não código de produção com testes automatizados. Para verificar sua configuração e alterações:

### Teste Manual

1. **Teste o ambiente Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Teste a execução dos notebooks:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifique as variáveis de ambiente:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Executando Notebooks Individualmente

Abra os notebooks no Jupyter e execute as células em sequência. Cada notebook é autocontido e inclui:
- Declarações de importação
- Carregamento de configuração
- Implementações de exemplo de agentes
- Resultados esperados nas células markdown

### Teste Básico dos Agentes Implantados

Para lições onde um agente é implantado como agente hospedado Microsoft Foundry (01, 04, 05, 16), o repositório inclui catálogos de smoke-test sob `tests/` que são executados pelo fluxo de trabalho `.github/workflows/smoke-test.yml` via a ação [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Estes são um gatilho leve pós-implantação (o agente está acessível e seguindo expectativas básicas de prompts?), complementando o pipeline de avaliação nas Lições 10 e 16. Veja [tests/README.md](./tests/README.md) para o mapeamento catálogo-para-lição-para-agente. A lição 17 roda localmente com Foundry Local e não possui endpoint hospedado, sendo validada executando seu notebook diretamente.

## Estilo de Código

### Convenções Python

- **Versão Python**: 3.12+
- **Estilo de Código**: Siga as convenções padrão Python PEP 8
- **Notebooks**: Use células markdown claras para explicar conceitos
- **Imports**: Agrupe por biblioteca padrão, terceiros e locais

### Convenções Jupyter Notebook

- Inclua células markdown descritivas antes das células de código
- Adicione exemplos de saída nos notebooks para referência
- Use nomes de variáveis claros que correspondam aos conceitos da lição
- Mantenha a ordem de execução do notebook linear (célula 1 → 2 → 3...)

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

## Build e Implantação

### Construção de Documentação

Este repositório usa Markdown para documentação:
- Arquivos README.md em cada pasta de lição
- README.md principal na raiz do repositório
- Sistema automático de tradução via GitHub Actions

### Pipeline CI/CD

Localizado em `.github/workflows/`:

1. **co-op-translator.yml** - Tradução automática para mais de 50 idiomas
2. **welcome-issue.yml** - Recebe criadores de novas issues
3. **welcome-pr.yml** - Recebe novos colaboradores de pull requests

### Implantação

Este é um repositório educacional - não há processo de implantação. Usuários:
1. Fazem fork ou clone do repositório
2. Executam os notebooks localmente ou em GitHub Codespaces
3. Aprendem modificando e experimentando os exemplos

## Diretrizes para Pull Request

### Antes de Enviar

1. **Teste suas alterações:**
   - Execute completamente os notebooks afetados
   - Verifique se todas as células executam sem erros
   - Confira se as saídas são apropriadas

2. **Atualizações na documentação:**
   - Atualize README.md se adicionar novos conceitos
   - Adicione comentários nos notebooks para códigos complexos
   - Garanta que as células markdown expliquem o propósito

3. **Alterações de arquivos:**
   - Evite commitar arquivos `.env` (use `.env.example`)
   - Não comite diretórios `venv/` ou `__pycache__/`
   - Mantenha saídas do notebook quando demonstrarem conceitos
   - Remova arquivos temporários e backups de notebooks (`*-backup.ipynb`)

### Formato do Título do PR

Use títulos descritivos:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Verificações Obrigatórias

- Notebooks devem executar sem erros
- Arquivos README devem ser claros e precisos
- Siga padrões existentes de código no repositório
- Mantenha consistência com outras lições

## Notas Adicionais

### Armadilhas Comuns

1. **Incompatibilidade de versão Python:**
   - Certifique-se de usar Python 3.12+
   - Alguns pacotes podem não funcionar com versões mais antigas
   - Use `python3 -m venv` para especificar a versão do Python explicitamente

2. **Variáveis de ambiente:**
   - Sempre crie `.env` a partir de `.env.example`
   - Não comite o arquivo `.env` (está no `.gitignore`)
   - Faça login com `az login` para autenticação Entra ID sem chave

3. **Conflitos de pacotes:**
   - Use um ambiente virtual fresco
   - Instale a partir de `requirements.txt` ao invés de pacotes individuais
   - Alguns notebooks podem requerer pacotes adicionais mencionados nas células markdown

4. **Serviços Azure:**
   - Serviços Azure AI requerem assinatura ativa
   - Algumas funcionalidades são específicas por região
   - Certifique-se que sua implantação de modelo Azure OpenAI suporta a API Responses

### Caminho de Aprendizagem

Progressão recomendada pelas lições:
1. **00-course-setup** - Inicie aqui para configurar ambiente
2. **01-intro-to-ai-agents** - Entenda fundamentos de agentes de IA
3. **02-explore-agentic-frameworks** - Aprenda sobre diferentes frameworks
4. **03-agentic-design-patterns** - Padrões de design essenciais
5. Continue sequencialmente pelas lições numeradas

### Seleção de Framework

Escolha o framework baseado nos seus objetivos:
- **Todas as lições**: Microsoft Agent Framework (MAF) com `FoundryChatClient`
- **Agentes registram do lado servidor** no Microsoft Foundry Agent Service V2 e são visíveis no portal Foundry

### Obtendo Ajuda

- Junte-se ao [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Consulte os arquivos README das lições para orientações específicas
- Verifique o [README.md principal](./README.md) para visão geral do curso
- Consulte [Course Setup](./00-course-setup/README.md) para instruções detalhadas de configuração

### Contribuindo

Este é um projeto educacional aberto. Contribuições são bem-vindas:
- Melhore exemplos de código
- Corrija erros ou typos
- Adicione comentários explicativos
- Sugira novos tópicos para lições
- Traduza para idiomas adicionais

Veja [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para necessidades atuais.

## Contexto Específico do Projeto

### Suporte Multilíngue

Este repositório usa sistema automático de tradução:
- Mais de 50 idiomas suportados
- Traduções nas pastas `/translations/<lang-code>/`
- Workflow GitHub Actions gerencia atualizações de tradução
- Arquivos fonte são em inglês na raiz do repositório

### Estrutura das Lições

Cada lição segue um padrão consistente:
1. Miniatura do vídeo com link
2. Conteúdo textual da lição (README.md)
3. Exemplos de código em múltiplos frameworks
4. Objetivos de aprendizagem e pré-requisitos
5. Recursos extras de aprendizagem linkados

### Nomeação dos Exemplos de Código

Formato: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lição 1, MAF Python
- `14-sequential.ipynb` - Lição 14, padrões avançados MAF
- `16-python-agent-framework.ipynb` - Lição 16, agente de suporte ao cliente em produção
- `17-local-agent-foundry-local.ipynb` - Lição 17, agente local com Foundry Local + Qwen

### Pastas Especiais

- `translated_images/` - Imagens localizadas para traduções
- `images/` - Imagens originais para conteúdo em inglês
- `.devcontainer/` - Configuração do container de desenvolvimento VS Code
- `.github/` - Workflows e templates GitHub Actions

### Dependências

Pacotes chave em `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Suporte ao protocolo Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Serviços Azure AI
- `azure-identity` - Autenticação Azure (AzureCliCredential)
- `azure-search-documents` - Integração Azure AI Search
- `mcp[cli]` - Suporte ao Modelo Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->