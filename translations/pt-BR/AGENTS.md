# AGENTS.md

## Visão Geral do Projeto

Este repositório contém "Agentes de IA para Iniciantes" - um curso educacional abrangente que ensina tudo o que é necessário para construir agentes de IA. O curso consiste em mais de 15 lições que abordam fundamentos, padrões de design, frameworks e implantação de agentes de IA em produção.

**Principais Tecnologias:**
- Python 3.12+
- Jupyter Notebooks para aprendizado interativo
- Frameworks de IA: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Serviços de IA do Azure: Azure AI Foundry, Azure AI Agent Service
- Marketplace de Modelos do GitHub (disponível na camada gratuita)

**Arquitetura:**
- Estrutura baseada em lições (diretórios 00-15+)
- Cada lição contém: documentação README, exemplos de código (notebooks Jupyter) e imagens
- Suporte multilíngue via sistema de tradução automatizado
- Múltiplas opções de frameworks por lição (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Comandos de Configuração

### Pré-requisitos
- Python 3.12 ou superior
- Conta no GitHub (para Modelos do GitHub - camada gratuita)
- Assinatura do Azure (opcional, para serviços de IA do Azure)

### Configuração Inicial

1. **Clone ou faça um fork do repositório:**
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

Para **Modelos do GitHub (Gratuito)**:
- `GITHUB_TOKEN` - Token de acesso pessoal do GitHub

Para **Serviços de IA do Azure** (opcional):
- `PROJECT_ENDPOINT` - Endpoint do projeto Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - Chave da API do Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL do endpoint do Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Nome da implantação para o modelo de chat
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Nome da implantação para embeddings
- Configuração adicional do Azure conforme mostrado em `.env.example`

## Fluxo de Trabalho de Desenvolvimento

### Executando Notebooks Jupyter

Cada lição contém vários notebooks Jupyter para diferentes frameworks:

1. **Inicie o Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navegue até o diretório de uma lição** (ex.: `01-intro-to-ai-agents/code_samples/`)

3. **Abra e execute os notebooks:**
   - `*-semantic-kernel.ipynb` - Usando o framework Semantic Kernel
   - `*-autogen.ipynb` - Usando o framework AutoGen
   - `*-python-agent-framework.ipynb` - Usando o Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando o Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Usando o Azure AI Agent Service

### Trabalhando com Diferentes Frameworks

**Semantic Kernel + Modelos do GitHub:**
- Camada gratuita disponível com conta no GitHub
- Bom para aprendizado e experimentação
- Padrão de arquivo: `*-semantic-kernel*.ipynb`

**AutoGen + Modelos do GitHub:**
- Camada gratuita disponível com conta no GitHub
- Capacidades de orquestração multiagente
- Padrão de arquivo: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Framework mais recente da Microsoft
- Disponível em Python e .NET
- Padrão de arquivo: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Requer assinatura do Azure
- Recursos prontos para produção
- Padrão de arquivo: `*-azureaiagent.ipynb`

## Instruções de Teste

Este é um repositório educacional com código de exemplo, em vez de código de produção com testes automatizados. Para verificar sua configuração e alterações:

### Teste Manual

1. **Teste o ambiente Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Teste a execução dos notebooks:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifique as variáveis de ambiente:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### Executando Notebooks Individualmente

Abra os notebooks no Jupyter e execute as células sequencialmente. Cada notebook é autossuficiente e inclui:
- Declarações de importação
- Carregamento de configuração
- Implementações de agentes de exemplo
- Resultados esperados em células markdown

## Estilo de Código

### Convenções de Python

- **Versão do Python**: 3.12+
- **Estilo de Código**: Siga as convenções padrão do PEP 8
- **Notebooks**: Use células markdown claras para explicar conceitos
- **Imports**: Agrupe por biblioteca padrão, terceiros e imports locais

### Convenções de Notebooks Jupyter

- Inclua células markdown descritivas antes das células de código
- Adicione exemplos de saída nos notebooks como referência
- Use nomes de variáveis claros que correspondam aos conceitos da lição
- Mantenha a ordem de execução dos notebooks linear (célula 1 → 2 → 3...)

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


## Construção e Implantação

### Construção da Documentação

Este repositório usa Markdown para documentação:
- Arquivos README.md em cada pasta de lição
- README.md principal na raiz do repositório
- Sistema de tradução automatizado via GitHub Actions

### Pipeline de CI/CD

Localizado em `.github/workflows/`:

1. **co-op-translator.yml** - Tradução automática para mais de 50 idiomas
2. **welcome-issue.yml** - Dá boas-vindas aos criadores de novas issues
3. **welcome-pr.yml** - Dá boas-vindas aos contribuidores de novos pull requests

### Implantação

Este é um repositório educacional - sem processo de implantação. Usuários:
1. Fazem fork ou clonam o repositório
2. Executam os notebooks localmente ou no GitHub Codespaces
3. Aprendem modificando e experimentando com os exemplos

## Diretrizes para Pull Requests

### Antes de Submeter

1. **Teste suas alterações:**
   - Execute completamente os notebooks afetados
   - Verifique se todas as células são executadas sem erros
   - Certifique-se de que os resultados são apropriados

2. **Atualizações na documentação:**
   - Atualize o README.md se adicionar novos conceitos
   - Adicione comentários nos notebooks para código complexo
   - Certifique-se de que as células markdown explicam o propósito

3. **Alterações nos arquivos:**
   - Evite cometer arquivos `.env` (use `.env.example`)
   - Não cometa diretórios `venv/` ou `__pycache__/`
   - Mantenha os resultados dos notebooks quando eles demonstrarem conceitos
   - Remova arquivos temporários e notebooks de backup (`*-backup.ipynb`)

### Formato do Título do PR

Use títulos descritivos:
- `[Lesson-XX] Adicionar novo exemplo para <conceito>`
- `[Fix] Corrigir erro de digitação no README da lição-XX`
- `[Update] Melhorar exemplo de código na lição-XX`
- `[Docs] Atualizar instruções de configuração`

### Verificações Necessárias

- Os notebooks devem ser executados sem erros
- Os arquivos README devem ser claros e precisos
- Siga os padrões de código existentes no repositório
- Mantenha a consistência com outras lições

## Notas Adicionais

### Armadilhas Comuns

1. **Incompatibilidade de versão do Python:**
   - Certifique-se de usar Python 3.12+
   - Alguns pacotes podem não funcionar com versões mais antigas
   - Use `python3 -m venv` para especificar explicitamente a versão do Python

2. **Variáveis de ambiente:**
   - Sempre crie `.env` a partir de `.env.example`
   - Não cometa o arquivo `.env` (está no `.gitignore`)
   - O token do GitHub precisa de permissões apropriadas

3. **Conflitos de pacotes:**
   - Use um ambiente virtual novo
   - Instale a partir de `requirements.txt` em vez de pacotes individuais
   - Alguns notebooks podem exigir pacotes adicionais mencionados em suas células markdown

4. **Serviços do Azure:**
   - Os serviços de IA do Azure exigem assinatura ativa
   - Alguns recursos são específicos de regiões
   - Limitações da camada gratuita se aplicam aos Modelos do GitHub

### Caminho de Aprendizado

Progressão recomendada pelas lições:
1. **00-course-setup** - Comece aqui para configurar o ambiente
2. **01-intro-to-ai-agents** - Entenda os fundamentos dos agentes de IA
3. **02-explore-agentic-frameworks** - Aprenda sobre diferentes frameworks
4. **03-agentic-design-patterns** - Padrões de design principais
5. Continue pelas lições numeradas sequencialmente

### Seleção de Framework

Escolha o framework com base em seus objetivos:
- **Aprendizado/Prototipagem**: Semantic Kernel + Modelos do GitHub (gratuito)
- **Sistemas multiagentes**: AutoGen
- **Recursos mais recentes**: Microsoft Agent Framework (MAF)
- **Implantação em produção**: Azure AI Agent Service

### Obtendo Ajuda

- Participe do [Discord da Comunidade Azure AI Foundry](https://aka.ms/ai-agents/discord)
- Revise os arquivos README das lições para orientações específicas
- Consulte o [README.md principal](./README.md) para visão geral do curso
- Veja [Configuração do Curso](./00-course-setup/README.md) para instruções detalhadas de configuração

### Contribuindo

Este é um projeto educacional aberto. Contribuições são bem-vindas:
- Melhore exemplos de código
- Corrija erros de digitação ou erros
- Adicione comentários esclarecedores
- Sugira novos tópicos de lições
- Traduza para idiomas adicionais

Veja [Issues do GitHub](https://github.com/microsoft/ai-agents-for-beginners/issues) para necessidades atuais.

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
4. Objetivos de aprendizado e pré-requisitos
5. Recursos de aprendizado extras vinculados

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
- `azure-ai-inference`, `azure-ai-projects` - Serviços de IA do Azure
- `azure-search-documents` - Integração de Pesquisa do Azure AI
- `chromadb` - Banco de dados vetorial para exemplos de RAG
- `chainlit` - Framework de interface de chat
- `browser_use` - Automação de navegador para agentes
- `mcp[cli]` - Suporte ao Protocolo de Contexto de Modelo
- `mem0ai` - Gerenciamento de memória para agentes

---

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.