# AGENTS.md

## Visão Geral do Projeto

Este repositório contém "Agentes de IA para Iniciantes" - um curso educacional abrangente que ensina tudo o que é necessário para construir Agentes de IA. O curso consiste em mais de 15 aulas que cobrem fundamentos, padrões de design, frameworks e implantação em produção de agentes de IA.

**Tecnologias-chave:**
- Python 3.12+
- Jupyter Notebooks para aprendizado interativo
- Frameworks de IA: Microsoft Agent Framework (MAF)
- Serviços de IA do Azure: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arquitetura:**
- Estrutura baseada em lições (diretórios 00-15+)
- Cada lição contém: documentação README, exemplos de código (notebooks Jupyter) e imagens
- Suporte multilíngue via sistema de tradução automatizado
- Um notebook Python por lição usando o Microsoft Agent Framework

## Comandos de Configuração

### Pré-requisitos
- Python 3.12 ou superior
- Assinatura do Azure (para Azure AI Foundry)
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

### Variáveis de Ambiente Requeridas

Para **Azure AI Foundry** (Obrigatório):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint do projeto Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nome do deployment do modelo (ex: gpt-4o)

Para **Azure AI Search** (Lição 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint do Azure AI Search
- `AZURE_SEARCH_API_KEY` - chave API do Azure AI Search

Autenticação: Execute `az login` antes de rodar os notebooks (usa `AzureCliCredential`).

## Fluxo de Desenvolvimento

### Executando Jupyter Notebooks

Cada lição contém múltiplos notebooks Jupyter para diferentes frameworks:

1. **Inicie o Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navegue até um diretório de lição** (ex: `01-intro-to-ai-agents/code_samples/`)

3. **Abra e execute os notebooks:**
   - `*-python-agent-framework.ipynb` - Usando Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando Microsoft Agent Framework (.NET)

### Trabalhando com Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Requer assinatura do Azure
- Usa `AzureAIProjectAgentProvider` para Agent Service V2 (agentes visíveis no portal Foundry)
- Pronto para produção com observabilidade integrada
- Padrão de arquivo: `*-python-agent-framework.ipynb`

## Instruções de Teste

Este é um repositório educacional com código de exemplo ao invés de código de produção com testes automatizados. Para verificar sua configuração e alterações:

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

Abra os notebooks no Jupyter e execute as células sequencialmente. Cada notebook é autocontido e inclui:
- Declarações de importação
- Carregamento de configurações
- Implementações de exemplo de agentes
- Saídas esperadas em células markdown

## Estilo de Código

### Convenções Python

- **Versão Python**: 3.12+
- **Estilo de Código**: Siga as convenções padrão Python PEP 8
- **Notebooks**: Use células markdown claras para explicar conceitos
- **Imports**: Agrupe por biblioteca padrão, terceiros, locais

### Convenções Jupyter Notebook

- Incluir células markdown descritivas antes das células de código
- Adicionar exemplos de saída nos notebooks como referência
- Usar nomes de variáveis claros que correspondam aos conceitos das aulas
- Manter a ordem de execução do notebook linear (célula 1 → 2 → 3 ...)

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

## Build e Deploy

### Construindo a Documentação

Este repositório usa Markdown para documentação:
- Arquivos README.md em cada pasta de lição
- README.md principal na raiz do repositório
- Sistema automatizado de tradução via GitHub Actions

### Pipeline CI/CD

Localizado em `.github/workflows/`:

1. **co-op-translator.yml** - Tradução automática para mais de 50 idiomas
2. **welcome-issue.yml** - Dá boas-vindas a criadores de novas issues
3. **welcome-pr.yml** - Dá boas-vindas a contribuintes de pull requests

### Implantação

Este é um repositório educacional - não há processo de deploy. Usuários:
1. Forkam ou clonam o repositório
2. Executam notebooks localmente ou em GitHub Codespaces
3. Aprendem modificando e experimentando exemplos

## Diretrizes para Pull Requests

### Antes de Enviar

1. **Teste suas alterações:**
   - Execute completamente os notebooks afetados
   - Verifique que todas as células executem sem erros
   - Confirme que as saídas são apropriadas

2. **Atualizações de documentação:**
   - Atualize README.md se adicionar novos conceitos
   - Adicione comentários nos notebooks para código complexo
   - Certifique-se de que as células markdown expliquem o propósito

3. **Alterações em arquivos:**
   - Evite commitar arquivos `.env` (use `.env.example`)
   - Não inclua diretórios `venv/` ou `__pycache__/`
   - Mantenha saídas de notebooks quando demonstrarem conceitos
   - Remova arquivos temporários e backups de notebooks (`*-backup.ipynb`)

### Formato de Título do PR

Use títulos descritivos:
- `[Lesson-XX] Adicionar novo exemplo para <conceito>`
- `[Fix] Corrigir erro de digitação no README da lição-XX`
- `[Update] Melhorar exemplo de código na lição-XX`
- `[Docs] Atualizar instruções de configuração`

### Verificações Obrigatórias

- Os notebooks devem executar sem erros
- Os arquivos README devem ser claros e precisos
- Siga os padrões de código existentes no repositório
- Mantenha consistência com as outras lições

## Notas Adicionais

### Armadilhas Comuns

1. **Versão Python incompatível:**
   - Certifique-se de usar Python 3.12+
   - Alguns pacotes podem não funcionar em versões anteriores
   - Use `python3 -m venv` para especificar a versão explicitamente

2. **Variáveis de ambiente:**
   - Sempre crie `.env` a partir de `.env.example`
   - Não comite o arquivo `.env` (está no `.gitignore`)
   - Token do GitHub precisa de permissões adequadas

3. **Conflitos de pacotes:**
   - Use um ambiente virtual limpo
   - Instale via `requirements.txt` ao invés de pacotes isolados
   - Alguns notebooks podem requerer pacotes adicionais mencionados nas células markdown

4. **Serviços Azure:**
   - Serviços Azure AI exigem assinatura ativa
   - Algumas funcionalidades são regionais
   - Limitações do plano gratuito se aplicam aos Modelos GitHub

### Caminho de Aprendizado

Progressão recomendada pelas lições:
1. **00-course-setup** - Comece aqui para configuração do ambiente
2. **01-intro-to-ai-agents** - Entenda fundamentos de agentes de IA
3. **02-explore-agentic-frameworks** - Conheça diferentes frameworks
4. **03-agentic-design-patterns** - Padrões centrais de design
5. Continue pelas lições numeradas sequencialmente

### Seleção de Framework

Escolha de framework baseada nos seus objetivos:
- **Todas as lições**: Microsoft Agent Framework (MAF) com `AzureAIProjectAgentProvider`
- **Agentes registram server-side** no Azure AI Foundry Agent Service V2 e são visíveis no portal Foundry

### Obtendo Ajuda

- Junte-se ao [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Revise os arquivos README das lições para orientações específicas
- Consulte o [README.md](./README.md) principal para visão geral do curso
- Veja [Course Setup](./00-course-setup/README.md) para instruções detalhadas de configuração

### Contribuindo

Este é um projeto educacional aberto. Contribuições são bem-vindas:
- Melhorar exemplos de código
- Corrigir erros de digitação ou bugs
- Adicionar comentários explicativos
- Sugerir novos tópicos de lições
- Traduzir para idiomas adicionais

Veja [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para necessidades atuais.

## Contexto Específico do Projeto

### Suporte Multilíngue

Este repositório usa um sistema automatizado de tradução:
- Suporte a mais de 50 idiomas
- Traduções em diretórios `/translations/<lang-code>/`
- Workflow GitHub Actions gerencia atualizações de tradução
- Arquivos fonte estão em inglês na raiz do repositório

### Estrutura das Lições

Cada lição segue um padrão consistente:
1. Miniatura de vídeo com link
2. Conteúdo escrito da lição (README.md)
3. Exemplos de código em múltiplos frameworks
4. Objetivos e pré-requisitos de aprendizagem
5. Recursos extras de aprendizado vinculados

### Nomeação de Exemplos de Código

Formato: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lição 1, MAF Python
- `14-sequential.ipynb` - Lição 14, padrões avançados MAF

### Diretórios Especiais

- `translated_images/` - Imagens localizadas para traduções
- `images/` - Imagens originais para conteúdo em inglês
- `.devcontainer/` - Configuração do container de desenvolvimento VS Code
- `.github/` - Workflows e templates do GitHub Actions

### Dependências

Pacotes chave do `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Suporte a protocolo Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Serviços Azure AI
- `azure-identity` - Autenticação Azure (AzureCliCredential)
- `azure-search-documents` - Integração Azure AI Search
- `mcp[cli]` - Suporte a Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original, em seu idioma nativo, deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->