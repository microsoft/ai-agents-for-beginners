# AGENTS.md

## Visão Geral do Projeto

Este repositório contém "Agentes de IA para Iniciantes" - um curso educacional abrangente que ensina tudo o que é necessário para criar Agentes de IA. O curso consiste em mais de 15 lições que abordam fundamentos, padrões de design, frameworks e implementação em produção de agentes de IA.

**Principais Tecnologias:**
- Python 3.12+
- Jupyter Notebooks para aprendizagem interativa
- Frameworks de IA: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Serviços de IA da Azure: Azure AI Foundry, Azure AI Agent Service
- Marketplace de Modelos do GitHub (disponível na versão gratuita)

**Arquitetura:**
- Estrutura baseada em lições (diretórios 00-15+)
- Cada lição contém: documentação README, exemplos de código (notebooks Jupyter) e imagens
- Suporte multilíngue através de sistema de tradução automatizado
- Múltiplas opções de frameworks por lição (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Comandos de Configuração

### Pré-requisitos
- Python 3.12 ou superior
- Conta no GitHub (para Modelos do GitHub - versão gratuita)
- Subscrição Azure (opcional, para serviços de IA da Azure)

### Configuração Inicial

1. **Clonar ou fazer fork do repositório:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Criar e ativar um ambiente virtual Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variáveis de ambiente:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### Variáveis de Ambiente Necessárias

Para **Modelos do GitHub (Gratuito)**:
- `GITHUB_TOKEN` - Token de acesso pessoal do GitHub

Para **Serviços de IA da Azure** (opcional):
- `PROJECT_ENDPOINT` - Endpoint do projeto Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - Chave API do Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL do endpoint do Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Nome da implementação para o modelo de chat
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Nome da implementação para embeddings
- Configuração adicional da Azure conforme mostrado em `.env.example`

## Fluxo de Trabalho de Desenvolvimento

### Executar Jupyter Notebooks

Cada lição contém múltiplos notebooks Jupyter para diferentes frameworks:

1. **Iniciar Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navegar até o diretório de uma lição** (ex.: `01-intro-to-ai-agents/code_samples/`)

3. **Abrir e executar os notebooks:**
   - `*-semantic-kernel.ipynb` - Usando o framework Semantic Kernel
   - `*-autogen.ipynb` - Usando o framework AutoGen
   - `*-python-agent-framework.ipynb` - Usando o Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando o Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Usando o Azure AI Agent Service

### Trabalhar com Diferentes Frameworks

**Semantic Kernel + Modelos do GitHub:**
- Versão gratuita disponível com conta GitHub
- Bom para aprendizagem e experimentação
- Padrão de arquivo: `*-semantic-kernel*.ipynb`

**AutoGen + Modelos do GitHub:**
- Versão gratuita disponível com conta GitHub
- Capacidades de orquestração multiagente
- Padrão de arquivo: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Framework mais recente da Microsoft
- Disponível em Python e .NET
- Padrão de arquivo: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Requer subscrição Azure
- Recursos prontos para produção
- Padrão de arquivo: `*-azureaiagent.ipynb`

## Instruções de Teste

Este é um repositório educacional com código de exemplo, em vez de código de produção com testes automatizados. Para verificar sua configuração e alterações:

### Teste Manual

1. **Testar o ambiente Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Testar a execução dos notebooks:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verificar variáveis de ambiente:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### Executar Notebooks Individualmente

Abra os notebooks no Jupyter e execute as células sequencialmente. Cada notebook é autossuficiente e inclui:
- Declarações de importação
- Carregamento de configuração
- Implementações de agentes de exemplo
- Resultados esperados em células markdown

## Estilo de Código

### Convenções de Python

- **Versão Python**: 3.12+
- **Estilo de Código**: Seguir as convenções padrão do PEP 8
- **Notebooks**: Usar células markdown claras para explicar conceitos
- **Importações**: Agrupar por biblioteca padrão, terceiros e importações locais

### Convenções de Notebooks Jupyter

- Incluir células markdown descritivas antes das células de código
- Adicionar exemplos de saída nos notebooks como referência
- Usar nomes de variáveis claros que correspondam aos conceitos da lição
- Manter a ordem de execução dos notebooks linear (célula 1 → 2 → 3...)

### Organização de Arquivos

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```


## Construção e Implementação

### Construção da Documentação

Este repositório usa Markdown para documentação:
- Arquivos README.md em cada pasta de lição
- README.md principal na raiz do repositório
- Sistema de tradução automatizado via GitHub Actions

### Pipeline CI/CD

Localizado em `.github/workflows/`:

1. **co-op-translator.yml** - Tradução automática para mais de 50 idiomas
2. **welcome-issue.yml** - Dá boas-vindas aos criadores de novos issues
3. **welcome-pr.yml** - Dá boas-vindas aos novos contribuidores de pull requests

### Implementação

Este é um repositório educacional - sem processo de implementação. Usuários:
1. Fazem fork ou clonam o repositório
2. Executam os notebooks localmente ou no GitHub Codespaces
3. Aprendem modificando e experimentando com os exemplos

## Diretrizes para Pull Requests

### Antes de Submeter

1. **Testar suas alterações:**
   - Executar completamente os notebooks afetados
   - Verificar se todas as células são executadas sem erros
   - Checar se os resultados são apropriados

2. **Atualizações na documentação:**
   - Atualizar README.md ao adicionar novos conceitos
   - Adicionar comentários nos notebooks para código complexo
   - Garantir que as células markdown expliquem o propósito

3. **Alterações nos arquivos:**
   - Evitar o commit de arquivos `.env` (usar `.env.example`)
   - Não fazer commit de diretórios `venv/` ou `__pycache__/`
   - Manter as saídas dos notebooks quando demonstrarem conceitos
   - Remover arquivos temporários e notebooks de backup (`*-backup.ipynb`)

### Formato do Título do PR

Usar títulos descritivos:
- `[Lesson-XX] Adicionar novo exemplo para <conceito>`
- `[Fix] Corrigir erro de digitação no README da lição-XX`
- `[Update] Melhorar exemplo de código na lição-XX`
- `[Docs] Atualizar instruções de configuração`

### Verificações Necessárias

- Os notebooks devem ser executados sem erros
- Os arquivos README devem ser claros e precisos
- Seguir os padrões de código existentes no repositório
- Manter consistência com outras lições

## Notas Adicionais

### Erros Comuns

1. **Incompatibilidade de versão do Python:**
   - Garantir que Python 3.12+ seja usado
   - Alguns pacotes podem não funcionar com versões mais antigas
   - Usar `python3 -m venv` para especificar explicitamente a versão do Python

2. **Variáveis de ambiente:**
   - Sempre criar `.env` a partir de `.env.example`
   - Não fazer commit do arquivo `.env` (está no `.gitignore`)
   - O token do GitHub precisa de permissões apropriadas

3. **Conflitos de pacotes:**
   - Usar um ambiente virtual novo
   - Instalar a partir de `requirements.txt` em vez de pacotes individuais
   - Alguns notebooks podem exigir pacotes adicionais mencionados em suas células markdown

4. **Serviços da Azure:**
   - Os serviços de IA da Azure requerem subscrição ativa
   - Alguns recursos são específicos de regiões
   - Limitações da versão gratuita aplicam-se aos Modelos do GitHub

### Caminho de Aprendizagem

Progressão recomendada pelas lições:
1. **00-course-setup** - Comece aqui para configurar o ambiente
2. **01-intro-to-ai-agents** - Compreender os fundamentos dos agentes de IA
3. **02-explore-agentic-frameworks** - Aprender sobre diferentes frameworks
4. **03-agentic-design-patterns** - Padrões de design principais
5. Continue pelas lições numeradas sequencialmente

### Seleção de Framework

Escolha o framework com base nos seus objetivos:
- **Aprendizagem/Prototipagem**: Semantic Kernel + Modelos do GitHub (gratuito)
- **Sistemas multiagente**: AutoGen
- **Recursos mais recentes**: Microsoft Agent Framework (MAF)
- **Implementação em produção**: Azure AI Agent Service

### Obter Ajuda

- Junte-se ao [Discord da Comunidade Azure AI Foundry](https://aka.ms/ai-agents/discord)
- Revise os arquivos README das lições para orientações específicas
- Consulte o [README.md principal](./README.md) para visão geral do curso
- Veja [Configuração do Curso](./00-course-setup/README.md) para instruções detalhadas de configuração

### Contribuir

Este é um projeto educacional aberto. Contribuições são bem-vindas:
- Melhorar exemplos de código
- Corrigir erros de digitação ou erros
- Adicionar comentários esclarecedores
- Sugerir novos tópicos de lições
- Traduzir para idiomas adicionais

Veja [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para necessidades atuais.

## Contexto Específico do Projeto

### Suporte Multilíngue

Este repositório usa um sistema de tradução automatizado:
- Suporte para mais de 50 idiomas
- Traduções em diretórios `/translations/<lang-code>/`
- Workflow do GitHub Actions gerencia atualizações de tradução
- Arquivos de origem estão em inglês na raiz do repositório

### Estrutura das Lições

Cada lição segue um padrão consistente:
1. Miniatura de vídeo com link
2. Conteúdo escrito da lição (README.md)
3. Exemplos de código em múltiplos frameworks
4. Objetivos de aprendizagem e pré-requisitos
5. Recursos de aprendizagem adicionais vinculados

### Nomeação de Exemplos de Código

Formato: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Lição 4, Semantic Kernel
- `07-autogen.ipynb` - Lição 7, AutoGen
- `14-python-agent-framework.ipynb` - Lição 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Lição 14, MAF .NET

### Diretórios Especiais

- `translated_images/` - Imagens localizadas para traduções
- `images/` - Imagens originais para conteúdo em inglês
- `.devcontainer/` - Configuração de contêiner de desenvolvimento do VS Code
- `.github/` - Workflows e templates do GitHub Actions

### Dependências

Pacotes principais de `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - Framework AutoGen
- `semantic-kernel` - Framework Semantic Kernel
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Serviços de IA da Azure
- `azure-search-documents` - Integração de Pesquisa da Azure AI
- `chromadb` - Base de dados vetorial para exemplos RAG
- `chainlit` - Framework de interface de chat
- `browser_use` - Automação de navegador para agentes
- `mcp[cli]` - Suporte ao Protocolo de Contexto de Modelo
- `mem0ai` - Gestão de memória para agentes

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.