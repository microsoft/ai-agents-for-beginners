# AGENTES.md

## Visão Geral do Projeto

Este repositório contém "Agentes de IA para Principiantes" - um curso educativo abrangente que ensina tudo o que é necessário para construir Agentes de IA. O curso consiste em 18 lições (numeradas 00-18) cobrindo fundamentos, padrões de design, frameworks, implementação em produção, agentes locais/no dispositivo e segurança dos agentes de IA.

**Tecnologias-Chave:**
- Python 3.12+
- Jupyter Notebooks para aprendizagem interativa
- Frameworks de IA: Microsoft Agent Framework (MAF)
- Serviços Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arquitetura:**
- Estrutura baseada em lições (diretórios 00-15+)
- Cada lição contém: documentação README, exemplos de código (Jupyter notebooks) e imagens
- Suporte multilíngue através de sistema automático de tradução
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
   # OU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Crie e ative um ambiente virtual Python:**
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
   # Edite o .env com as suas chaves API e pontos finais
   ```

### Variáveis de Ambiente Necessárias

Para **Microsoft Foundry** (Obrigatório):
- `AZURE_AI_PROJECT_ENDPOINT` - Endpoint do projeto Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Nome do deployment do modelo (ex.: gpt-5-mini)

Para **Azure AI Search** (Lição 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - Chave API do Azure AI Search

Autenticação: Execute `az login` antes de correr os notebooks (usa `AzureCliCredential`).

## Fluxo de Desenvolvimento

### Executar Jupyter Notebooks

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

Este é um repositório educativo com código de exemplo, não código de produção com testes automatizados. Para verificar a sua configuração e alterações:

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
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Executar Notebooks Individualmente

Abra os notebooks no Jupyter e execute as células sequencialmente. Cada notebook é autónomo e inclui:
- Instruções de importação
- Carregamento de configurações
- Implementações de exemplo do agente
- Saídas esperadas em células markdown

### Teste Básico dos Agentes Implementados

Para as lições onde um agente é implementado como agente hospedado Microsoft Foundry (01, 04, 05, 16), o repositório inclui catálogos de smoke-test em `tests/` que são executados pelo workflow `.github/workflows/smoke-test.yml` via a ação [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Estes são uma verificação leve pós-implementação (o agente está acessível e responde conforme esperado?), complementando o pipeline de avaliação nas Lições 10 e 16. Veja [tests/README.md](./tests/README.md) para o mapeamento catálogo-para-lição-para-agente. A Lição 17 executa localmente com Foundry Local e não tem endpoint hospedado, sendo validada pela execução direta do seu notebook.

## Estilo de Código

### Convenções Python

- **Versão Python**: 3.12+
- **Estilo de Código**: Siga as convenções padrão PEP 8 para Python
- **Notebooks**: Use células markdown claras para explicar conceitos
- **Importações**: Agrupe por biblioteca padrão, terceiros, importações locais

### Convenções Jupyter Notebook

- Inclua células markdown descritivas antes das células de código
- Adicione exemplos de saída nos notebooks para referência
- Use nomes de variáveis claros que correspondam aos conceitos da lição
- Mantenha a ordem de execução do notebook linear (célula 1 → 2 → 3...)

### Organização dos Ficheiros

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Construção e Implementação

### Construir Documentação

Este repositório usa Markdown para documentação:
- Ficheiros README.md em cada pasta de lição
- README.md principal na raiz do repositório
- Sistema automático de tradução via GitHub Actions

### Pipeline CI/CD

Localizado em `.github/workflows/`:

1. **co-op-translator.yml** - Tradução automática para mais de 50 idiomas
2. **welcome-issue.yml** - Dá as boas-vindas aos criadores de issues
3. **welcome-pr.yml** - Dá as boas-vindas aos contribuidores de pull requests

### Implementação

Este é um repositório educativo - sem processo de deployment. Utilizadores:
1. Fazem fork ou clone do repositório
2. Executam notebooks localmente ou no GitHub Codespaces
3. Aprendem modificando e experimentando com exemplos

## Diretrizes para Pull Request

### Antes de Submeter

1. **Teste as suas alterações:**
   - Execute completamente os notebooks afetados
   - Verifique que todas as células executam sem erros
   - Confira que as saídas são apropriadas

2. **Atualizações à documentação:**
   - Atualize README.md caso adicione novos conceitos
   - Adicione comentários nos notebooks para código complexo
   - Assegure que as células markdown explicam o propósito

3. **Alterações em ficheiros:**
   - Evite commitar ficheiros `.env` (use `.env.example`)
   - Não commite diretórios `venv/` ou `__pycache__/`
   - Mantenha as saídas dos notebooks quando estas demonstrem conceitos
   - Remova ficheiros temporários e backups de notebooks (`*-backup.ipynb`)

### Formato do Título do PR

Use títulos descritivos:
- `[Lesson-XX] Adicionar novo exemplo para <concepto>`
- `[Fix] Corrigir erro tipográfico no README da lição-XX`
- `[Update] Melhorar exemplo de código na lição-XX`
- `[Docs] Atualizar instruções de configuração`

### Verificações Obrigatórias

- Notebooks devem executar sem erros
- Ficheiros README devem ser claros e precisos
- Seguir padrões de código existentes no repositório
- Manter consistência com outras lições

## Notas Adicionais

### Armadilhas Comuns

1. **Incompatibilidade de versão Python:**
   - Assegure que usa Python 3.12+
   - Alguns pacotes podem não funcionar em versões mais antigas
   - Use `python3 -m venv` para especificar explicitamente a versão do Python

2. **Variáveis de ambiente:**
   - Crie sempre `.env` a partir de `.env.example`
   - Não faça commit do ficheiro `.env` (está no `.gitignore`)
   - Faça login com `az login` para autenticação Entra ID sem chave

3. **Conflitos de pacotes:**
   - Utilize um ambiente virtual limpo
   - Instale a partir do `requirements.txt` em vez de pacotes individuais
   - Alguns notebooks podem requerer pacotes adicionais indicados nas células markdown

4. **Serviços Azure:**
   - Serviços Azure AI requerem subscrição ativa
   - Algumas funcionalidades são específicas por região
   - Assegure que o deployment do seu modelo Azure OpenAI suporta a Responses API

### Caminho de Aprendizagem

Progressão recomendada pelas lições:
1. **00-course-setup** - Comece aqui para configurar o ambiente
2. **01-intro-to-ai-agents** - Compreenda os fundamentos de agentes IA
3. **02-explore-agentic-frameworks** - Conheça diferentes frameworks
4. **03-agentic-design-patterns** - Padrões de design principais
5. Continue sequencialmente pelas lições numeradas

### Seleção de Framework

Escolha o framework com base nos seus objetivos:
- **Todas as lições**: Microsoft Agent Framework (MAF) com `FoundryChatClient`
- **Agentes registam-se no servidor** no Microsoft Foundry Agent Service V2 e são visíveis no portal Foundry

### Obter Ajuda

- Junte-se ao [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Reveja os ficheiros README das lições para orientações específicas
- Consulte o README principal [README.md](./README.md) para visão geral do curso
- Consulte [Course Setup](./00-course-setup/README.md) para instruções detalhadas de configuração

### Contribuir

Este é um projeto educativo aberto. Contribuições são bem-vindas:
- Melhorar exemplos de código
- Corrigir erros tipográficos ou erros
- Adicionar comentários esclarecedores
- Sugerir novos tópicos para lições
- Traduzir para outros idiomas

Veja [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para necessidades atuais.

## Contexto Específico do Projeto

### Suporte Multilíngue

Este repositório usa um sistema automático de tradução:
- Suporte para mais de 50 idiomas
- Traduções nas pastas `/translations/<lang-code>/`
- Workflow GitHub Actions gere atualizações de tradução
- Arquivos fonte estão em Inglês na raiz do repositório

### Estrutura da Lição

Cada lição segue um padrão consistente:
1. Miniatura de vídeo com link
2. Conteúdo escrito da lição (README.md)
3. Exemplos de código em múltiplos frameworks
4. Objetivos e pré-requisitos de aprendizagem
5. Recursos extra de aprendizagem ligados

### Nomeação de Exemplos de Código

Formato: `<número-da-lição>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lição 1, MAF Python
- `14-sequential.ipynb` - Lição 14, padrões avançados MAF
- `16-python-agent-framework.ipynb` - Lição 16, agente de suporte ao cliente em produção
- `17-local-agent-foundry-local.ipynb` - Lição 17, agente local com Foundry Local + Qwen

### Diretórios Especiais

- `translated_images/` - Imagens localizadas para traduções
- `images/` - Imagens originais para conteúdo em Inglês
- `.devcontainer/` - Configuração do contentor de desenvolvimento VS Code
- `.github/` - Workflows e templates GitHub Actions

### Dependências

Pacotes chave do `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Suporte ao protocolo Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Serviços Azure AI
- `azure-identity` - Autenticação Azure (AzureCliCredential)
- `azure-search-documents` - Integração Azure AI Search
- `mcp[cli]` - Suporte ao Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->