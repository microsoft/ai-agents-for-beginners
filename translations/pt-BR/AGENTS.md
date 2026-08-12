# AGENTS.md

## Visão Geral do Projeto

Este repositório contém "Agentes de IA para Iniciantes" - um curso educacional abrangente que ensina tudo o que é necessário para construir Agentes de IA. O curso consiste em 18 lições (numeradas de 00 a 18) cobrindo fundamentos, padrões de design, frameworks, implantação em produção, agentes locais/no dispositivo, e segurança de agentes de IA.

**Tecnologias Principais:**
- Python 3.12+
- Jupyter Notebooks para aprendizado interativo
- Frameworks de IA: Microsoft Agent Framework (MAF)
- Serviços de IA Azure: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arquitetura:**
- Estrutura baseada em lições (diretórios 00-15+)
- Cada lição contém: documentação README, exemplos de código (notebooks Jupyter), e imagens
- Suporte multilíngue via sistema automatizado de tradução
- Um notebook Python por lição utilizando Microsoft Agent Framework

## Comandos de Configuração

### Pré-requisitos
- Python 3.12 ou superior
- Assinatura Azure (para Microsoft Foundry)
- Azure CLI instalado e autenticado (`az login`)

### Configuração Inicial

1. **Clone ou faça um fork do repositório:**
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
   # Edite o .env com suas chaves de API e endpoints
   ```

### Variáveis de Ambiente Necessárias

Para **Microsoft Foundry** (Obrigatório):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint do projeto Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nome da implantação do modelo (ex: gpt-5-mini)

Para **Azure AI Search** (Lição 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint do Azure AI Search
- `AZURE_SEARCH_API_KEY` - chave da API do Azure AI Search

Autenticação: Execute `az login` antes de rodar os notebooks (utiliza `AzureCliCredential`).

## Fluxo de Trabalho de Desenvolvimento

### Executando Jupyter Notebooks

Cada lição contém múltiplos notebooks Jupyter para diferentes frameworks:

1. **Inicie o Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navegue até o diretório da lição** (ex: `01-intro-to-ai-agents/code_samples/`)

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
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Executando Notebooks Individualmente

Abra os notebooks no Jupyter e execute as células sequencialmente. Cada notebook é autocontido e inclui:
- Declarações de importação
- Carregamento de configuração
- Implementações de exemplo de agentes
- Resultados esperados em células markdown

### Testes Rápidos dos Agentes Implantados

Para lições onde um agente está implantado como agente hospedado Microsoft Foundry (01, 04, 05, 16), o repositório inclui catálogos de teste rápido em `tests/` que são executados pelo workflow `.github/workflows/smoke-test.yml` via a ação [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Estes são um gate leve pós-implantação (o agente está acessível e seguindo as expectativas básicas do prompt?), complementando o pipeline de avaliação nas Lições 10 e 16. Veja [tests/README.md](./tests/README.md) para o mapeamento catálogo-lição-agente. A lição 17 roda localmente com Foundry Local e não possui endpoint hospedado, então é validada executando seu notebook diretamente.

## Estilo de Código

### Convenções Python

- **Versão Python**: 3.12+
- **Estilo de Código**: Siga as convenções padrão PEP 8 do Python
- **Notebooks**: Use células markdown claras para explicar conceitos
- **Imports**: Agrupe por biblioteca padrão, terceiros e locais

### Convenções para Jupyter Notebook

- Inclua células markdown descritivas antes das células de código
- Adicione exemplos de saída nos notebooks como referência
- Use nomes de variáveis claros que combinem com conceitos da lição
- Mantenha ordem linear de execução do notebook (célula 1 → 2 → 3...)

### Organização dos Arquivos

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

### Construção da Documentação

Este repositório usa Markdown para documentação:
- Arquivos README.md em cada pasta de lição
- README.md principal na raiz do repositório
- Sistema automatizado de tradução via GitHub Actions

### Pipeline CI/CD

Localizado em `.github/workflows/`:

1. **co-op-translator.yml** - Tradução automática para mais de 50 idiomas
2. **welcome-issue.yml** - Dá boas-vindas a criadores de issues
3. **welcome-pr.yml** - Dá boas-vindas a contribuidores de pull requests

### Implantação

Este é um repositório educacional - sem processo de implantação. Usuários:
1. Fazem fork ou clona o repositório
2. Executam os notebooks localmente ou no GitHub Codespaces
3. Aprendem modificando e experimentando com exemplos

## Diretrizes para Pull Requests

### Antes de Submeter

1. **Teste suas alterações:**
   - Execute completamente os notebooks afetados
   - Verifique se todas as células executam sem erros
   - Confira se as saídas são apropriadas

2. **Atualizações na documentação:**
   - Atualize README.md ao adicionar novos conceitos
   - Adicione comentários nos notebooks para códigos complexos
   - Assegure que as células markdown expliquem o propósito

3. **Alterações em arquivos:**
   - Evite commitar arquivos `.env` (use `.env.example`)
   - Não commit `venv/` ou diretórios `__pycache__/`
   - Mantenha saídas do notebook quando demonstram conceitos
   - Remova arquivos temporários e backups de notebooks (`*-backup.ipynb`)

### Formato do Título do PR

Use títulos descritivos:
- `[Lesson-XX] Adicionar novo exemplo para <conceito>`
- `[Fix] Corrigir erro de digitação no README da lição-XX`
- `[Update] Melhorar exemplo de código na lição-XX`
- `[Docs] Atualizar instruções de configuração`

### Verificações Obrigatórias

- Notebooks devem executar sem erros
- Arquivos README devem ser claros e precisos
- Siga padrões de código existentes no repositório
- Mantenha consistência com outras lições

## Notas Adicionais

### Armadilhas Comuns

1. **Incompatibilidade de versão Python:**
   - Tenha certeza de usar Python 3.12+
   - Alguns pacotes podem não funcionar em versões antigas
   - Use `python3 -m venv` para especificar a versão explicitamente

2. **Variáveis de ambiente:**
   - Sempre crie `.env` a partir do `.env.example`
   - Não comite o arquivo `.env` (está no `.gitignore`)
   - Faça login com `az login` para autenticação Entra ID sem chave

3. **Conflitos de pacotes:**
   - Use um ambiente virtual novo
   - Instale pelo `requirements.txt` em vez de pacotes individuais
   - Alguns notebooks podem exigir pacotes adicionais mencionados nas células markdown

4. **Serviços Azure:**
   - Serviços Azure AI requerem assinatura ativa
   - Algumas funcionalidades são específicas por região
   - Certifique-se que sua implantação do modelo Azure OpenAI suporta API de Respostas

### Caminho de Aprendizagem

Progressão recomendada pelas lições:
1. **00-course-setup** - Comece aqui para configuração do ambiente
2. **01-intro-to-ai-agents** - Entenda os fundamentos de agentes de IA
3. **02-explore-agentic-frameworks** - Conheça diferentes frameworks
4. **03-agentic-design-patterns** - Padrões básicos de design
5. Continue pelas lições numeradas sequencialmente

### Seleção de Framework

Escolha o framework com base em seus objetivos:
- **Todas as lições**: Microsoft Agent Framework (MAF) com `FoundryChatClient`
- **Agentes registram-se no lado servidor** no Microsoft Foundry Agent Service V2 e são visíveis no portal Foundry

### Obtendo Ajuda

- Participe do [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Consulte os arquivos README das lições para orientações específicas
- Veja o [README.md](./README.md) principal para visão geral do curso
- Consulte [Course Setup](./00-course-setup/README.md) para instruções detalhadas de configuração

### Contribuindo

Este é um projeto educacional aberto. Contribuições são bem-vindas:
- Melhore exemplos de código
- Corrija erros de digitação ou bugs
- Acrescente comentários esclarecedores
- Sugira novos tópicos para lições
- Traduza para idiomas adicionais

Veja as [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para necessidades atuais.

## Contexto Específico do Projeto

### Suporte Multilíngue

Este repositório usa sistema automatizado de tradução:
- Suporte a 50+ idiomas
- Traduções em diretórios `/translations/<lang-code>/`
- Workflow no GitHub Actions gerencia atualizações de tradução
- Arquivos fonte estão em inglês na raiz do repositório

### Estrutura da Lição

Cada lição segue um padrão consistente:
1. Miniatura de vídeo com link
2. Conteúdo escrito da lição (README.md)
3. Exemplos de código em múltiplos frameworks
4. Objetivos de aprendizado e pré-requisitos
5. Recursos extras de aprendizado vinculados

### Nomeação de Exemplos de Código

Formato: `<número-da-lição>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lição 1, MAF Python
- `14-sequential.ipynb` - Lição 14, padrões avançados MAF
- `16-python-agent-framework.ipynb` - Lição 16, agente de suporte ao cliente em produção
- `17-local-agent-foundry-local.ipynb` - Lição 17, agente local com Foundry Local + Qwen

### Diretórios Especiais

- `translated_images/` - Imagens localizadas para traduções
- `images/` - Imagens originais para conteúdo em inglês
- `.devcontainer/` - Configuração do container de desenvolvimento VS Code
- `.github/` - Workflows e templates do GitHub Actions

### Dependências

Pacotes-chave do `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Suporte ao protocolo Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Serviços Azure AI
- `azure-identity` - Autenticação Azure (AzureCliCredential)
- `azure-search-documents` - Integração Azure AI Search
- `mcp[cli]` - Suporte ao Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->