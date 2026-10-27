# AGENTS.md

## Visão Geral do Projeto

Este repositório contém "Agentes IA para Iniciantes" - um curso educativo abrangente que ensina tudo o que é necessário para construir Agentes IA. O curso consiste em 18 lições (numeradas de 00 a 18) que abrangem fundamentos, padrões de design, frameworks, implantação em produção, agentes locais/no dispositivo e segurança dos agentes IA.

**Tecnologias Principais:**
- Python 3.12+
- Jupyter Notebooks para aprendizagem interativa
- Frameworks IA: Microsoft Agent Framework (MAF)
- Serviços de IA Azure: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arquitetura:**
- Estrutura baseada em lições (diretórios 00-18)
- Cada lição contém: documentação README, exemplos de código (notebooks Jupyter) e imagens
- Suporte multilíngue via sistema automático de tradução
- Um notebook Python por lição usando Microsoft Agent Framework

## Comandos de Configuração

### Pré-requisitos
- Python 3.12 ou superior
- Subscrição Azure (para Microsoft Foundry)
- Azure CLI instalado e autenticado (`az login`)

### Configuração Inicial

1. **Clone ou faça fork do repositório:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Crie e ative ambiente virtual Python:**
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
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Nome da implantação do modelo (ex.: gpt-5-mini)

Para **Azure AI Search** (Lição 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - Chave API Azure AI Search

Autenticação: Execute `az login` antes de correr os notebooks (usa `AzureCliCredential`).

## Fluxo de Trabalho de Desenvolvimento

### Execução de Jupyter Notebooks

Cada lição contém múltiplos notebooks Jupyter para diferentes frameworks:

1. **Inicie o Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navegue até ao diretório da lição** (ex.: `01-intro-to-ai-agents/code_samples/`)

3. **Abra e execute os notebooks:**
   - `*-python-agent-framework.ipynb` - Usando Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando Microsoft Agent Framework (.NET)

### Trabalhar com Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Requer subscrição Azure
- Usa `FoundryChatClient` para Agent Service V2 (agentes visíveis no portal Foundry)
- Pronto para produção com observabilidade incorporada
- Padrão de ficheiro: `*-python-agent-framework.ipynb`

## Instruções de Teste

Este é um repositório educativo com código de exemplo em vez de código de produção com testes automatizados. Para verificar a sua configuração e alterações:

### Teste Manual

1. **Teste o ambiente Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Teste a execução do notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifique as variáveis de ambiente:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Execução de Notebooks Individuais

Abra os notebooks no Jupyter e execute as células sequencialmente. Cada notebook é autónomo e inclui:
- Declarações de importação
- Carregamento de configuração
- Implementações de exemplo de agentes
- Saídas esperadas em células markdown

### Teste de Fumaça aos Agentes Implantados

Para lições em que um agente está implantado como agente hospedado Microsoft Foundry (01, 04, 05, 16), o repositório inclui catálogos de smoke-test sob `tests/` que são executados pelo fluxo de trabalho `.github/workflows/smoke-test.yml` via a ação [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Estes são um controlo leve pós-implantação (o agente está acessível e responde às expectativas básicas do prompt?), complementando a pipeline de avaliação nas Lições 10 e 16. Veja [tests/README.md](./tests/README.md) para o mapeamento catálogo-para-lição-para-agente. A lição 17 corre localmente com Foundry Local e não tem endpoint hospedado, sendo validada pela execução direta do seu notebook.

## Estilo de Código

### Convenções Python

- **Versão Python**: 3.12+
- **Estilo de Código**: Siga as convenções padrão Python PEP 8
- **Notebooks**: Use células markdown claras para explicar conceitos
- **Imports**: Agrupe por biblioteca padrão, terceiros, locais

### Convenções Jupyter Notebook

- Inclua células markdown descritivas antes das células de código
- Adicione exemplos de saída nos notebooks como referência
- Use nomes de variáveis claros que correspondam aos conceitos da lição
- Mantenha a ordem de execução do notebook linear (célula 1 → 2 → 3...)

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

## Construção e Implantação

### Construção da Documentação

Este repositório usa Markdown para documentação:
- Ficheiros README.md em cada pasta de lição
- README.md principal na raiz do repositório
- Sistema automático de tradução via GitHub Actions

### CI/CD Pipeline

Localizado em `.github/workflows/`:

1. **co-op-translator.yml** - Tradução automática para 50+ idiomas
2. **welcome-issue.yml** - Dá as boas-vindas a novos criadores de issues
3. **welcome-pr.yml** - Dá as boas-vindas a novos contribuidores de pull request

### Implantação

Este é um repositório educativo - sem processo de implantação. Utilizadores:
1. Fazem fork ou clone do repositório
2. Executam notebooks localmente ou no GitHub Codespaces
3. Aprendem modificando e experimentando exemplos

## Diretrizes de Pull Request

### Antes de Submeter

1. **Teste as suas alterações:**
   - Execute completamente os notebooks afetados
   - Verifique que todas as células executam sem erros
   - Confira se as saídas são apropriadas

2. **Atualizações de documentação:**
   - Atualize README.md se adicionar novos conceitos
   - Adicione comentários nos notebooks para código complexo
   - Assegure que as células markdown expliquem o propósito

3. **Alterações em ficheiros:**
   - Evite comitar ficheiros `.env` (use `.env.example`)
   - Não comite diretórios `venv/` ou `__pycache__/`
   - Mantenha as saídas dos notebooks quando demonstrarem conceitos
   - Remova ficheiros temporários e backups de notebooks (`*-backup.ipynb`)

### Formato de Título de PR

Use títulos descritivos:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Verificações Obrigatórias

- Os notebooks devem executar sem erros
- Os ficheiros README devem ser claros e precisos
- Siga os padrões de código existentes no repositório
- Mantenha a consistência com outras lições

## Notas Adicionais

### Armadilhas Comuns

1. **Incompatibilidade de versão Python:**
   - Assegure que usa Python 3.12+
   - Alguns pacotes podem não funcionar com versões mais antigas
   - Use `python3 -m venv` para especificar explicitamente a versão Python

2. **Variáveis de ambiente:**
   - Sempre crie `.env` a partir de `.env.example`
   - Não comite ficheiro `.env` (ele está em `.gitignore`)
   - Inicie sessão com `az login` para autenticação Entra ID sem chave

3. **Conflitos de pacotes:**
   - Use um ambiente virtual fresco
   - Instale a partir de `requirements.txt` em vez de pacotes individuais
   - Alguns notebooks podem requerer pacotes adicionais mencionados nas respetivas células markdown

4. **Serviços Azure:**
   - Serviços Azure AI requerem subscrição ativa
   - Algumas funcionalidades são específicas de região
   - Assegure que a implantação do modelo Azure OpenAI suporta a API Responses

### Caminho de Aprendizagem

Progressão recomendada pelas lições:
1. **00-course-setup** - Comece aqui para configuração do ambiente
2. **01-intro-to-ai-agents** - Compreender fundamentos de agentes IA
3. **02-explore-agentic-frameworks** - Aprender sobre diferentes frameworks
4. **03-agentic-design-patterns** - Padrões principais de design
5. Continue pelas lições numeradas sequencialmente

### Seleção de Framework

Escolha framework baseado nos seus objetivos:
- **Todas as lições**: Microsoft Agent Framework (MAF) com `FoundryChatClient`
- **Registo de agentes do lado servidor** no Microsoft Foundry Agent Service V2 sendo visíveis no portal Foundry

### Obter Ajuda

- Junte-se ao [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Reveja ficheiros README das lições para orientação específica
- Consulte o [README.md principal](./README.md) para visão geral do curso
- Consulte [Course Setup](./00-course-setup/README.md) para instruções detalhadas de configuração

### Contribuindo

Este é um projeto educativo aberto. Contribuições são bem-vindas:
- Melhorar exemplos de código
- Corrigir erros tipográficos ou erros
- Adicionar comentários esclarecedores
- Sugerir novos tópicos de lição
- Traduzir para idiomas adicionais

Veja [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para necessidades atuais.

## Contexto Específico do Projeto

### Suporte Multilíngue

Este repositório usa um sistema automático de tradução:
- Suporta 50+ idiomas
- Traduções em diretórios `/translations/<lang-code>/`
- Workflow via GitHub Actions cuida das atualizações das traduções
- Ficheiros fonte estão em inglês na raiz do repositório

### Estrutura da Lição

Cada lição segue um padrão consistente:
1. Miniatura de vídeo com link
2. Conteúdo escrito da lição (README.md)
3. Exemplos de código em múltiplos frameworks
4. Objetivos de aprendizagem e pré-requisitos
5. Recursos de aprendizagem extra ligados

### Nomeação de Exemplos de Código

Formato: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lição 1, MAF Python
- `14-sequential.ipynb` - Lição 14, padrões avançados MAF
- `16-python-agent-framework.ipynb` - Lição 16, agente de suporte ao cliente em produção
- `17-local-agent-foundry-local.ipynb` - Lição 17, agente local com Foundry Local + Qwen

### Diretórios Especiais

- `translated_images/` - Imagens localizadas para traduções
- `images/` - Imagens originais para conteúdo em inglês
- `.devcontainer/` - Configuração de contentor de desenvolvimento VS Code
- `.github/` - Workflows e templates GitHub Actions

### Dependências

Pacotes chave de `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Suporte ao protocolo Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Serviços Azure AI
- `azure-identity` - Autenticação Azure (AzureCliCredential)
- `azure-search-documents` - Integração Azure AI Search
- `mcp[cli]` - Suporte ao Protocolo de Contexto de Modelo

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->