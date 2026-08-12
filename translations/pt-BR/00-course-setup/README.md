# Configuração do Curso

## Introdução

Esta lição abordará como executar os exemplos de código deste curso.

## Participe de Outros Alunos e Obtenha Ajuda

Antes de começar a clonar seu repositório, entre no [canal AI Agents For Beginners Discord](https://aka.ms/ai-agents/discord) para obter ajuda com a configuração, tirar dúvidas sobre o curso ou conectar-se com outros alunos.

## Clone ou Faça Fork deste Repositório

Para começar, por favor clone ou faça fork do Repositório GitHub. Isso criará sua própria versão do material do curso para que você possa executar, testar e ajustar o código!

Isso pode ser feito clicando no link para <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fazer fork do repositório</a>

Agora você deve ter sua própria versão fork deste curso no link abaixo:

![Repositório Forkado](../../../translated_images/pt-BR/forked-repo.33f27ca1901baa6a.webp)

### Clone Raso (recomendado para workshop / Codespaces)

  > O repositório completo pode ser grande (~3 GB) ao fazer download do histórico completo e de todos os arquivos. Se você está participando apenas do workshop ou precisa de algumas pastas das lições, um clone raso (ou clone esparso) evita a maior parte do download truncando o histórico e/ou pulando blobs.

#### Clone raso rápido — histórico mínimo, todos os arquivos

Substitua `<your-username>` nos comandos abaixo pelo URL do seu fork (ou o URL upstream se preferir).

Para clonar apenas o histórico do commit mais recente (download pequeno):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Para clonar um branch específico:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clone parcial (esparso) — blobs mínimos + somente pastas selecionadas

Isso usa clone parcial e sparse-checkout (requer Git 2.25+ e é recomendado usar Git moderno com suporte a clone parcial):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Entre na pasta do repositório:

```bash|powershell
cd ai-agents-for-beginners
```

Depois especifique quais pastas você quer (exemplo abaixo mostra duas pastas):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Após clonar e verificar os arquivos, se você precisa apenas deles e deseja liberar espaço (sem histórico git), por favor apague os metadados do repositório (💀 irreversível — você perderá toda funcionalidade Git: sem commits, pulls, pushes, ou acesso a histórico).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Usando GitHub Codespaces (recomendado para evitar downloads grandes locais)

- Crie um novo Codespace para este repositório via [GitHub UI](https://github.com/codespaces).  

- No terminal do codespace recém-criado, execute um dos comandos de clone raso/esparso acima para trazer somente as pastas das lições que você precisa para o workspace do Codespace.
- Opcional: após clonar dentro do Codespaces, remova o .git para liberar espaço extra (veja comandos de remoção acima).
- Nota: Se preferir abrir o repositório diretamente no Codespaces (sem clone extra), fique ciente que o Codespaces irá construir o ambiente devcontainer e pode provisionar mais do que você precisa. Clonar uma cópia rasa dentro de um Codespace novo oferece mais controle sobre o uso de disco.

#### Dicas

- Sempre substitua o URL do clone pelo seu fork se quiser editar/commitar.
- Se depois precisar de mais histórico ou arquivos, você pode buscá-los ou ajustar o sparse-checkout para incluir pastas adicionais.

## Executando o Código

Este curso oferece uma série de Jupyter Notebooks que você pode executar para obter experiência prática construindo Agentes de IA.

Os exemplos de código usam o **Microsoft Agent Framework (MAF)** com o `FoundryChatClient`, que conecta ao **Microsoft Foundry Agent Service V2** (a API de Respostas) através do **Microsoft Foundry**.

Todos os notebooks Python são rotulados como `*-python-agent-framework.ipynb`.

## Requisitos

- Python 3.12+
  - **NOTA**: Se você não tiver Python3.12 instalado, certifique-se de instalá-lo. Crie seu ambiente virtual com python3.12 para garantir que as versões corretas sejam instaladas do arquivo requirements.txt.
  
    >Exemplo

    Crie o diretório do ambiente Python virtual:

    ```bash|powershell
    python -m venv venv
    ```

    Depois ative o ambiente virtual para:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Para os exemplos que usam .NET, certifique-se de instalar o [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ou superior. Depois, verifique sua versão .NET instalada:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Necessário para autenticação. Instale em [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Assinatura Azure** — Para acesso ao Microsoft Foundry e ao Microsoft Foundry Agent Service.
- **Projeto Microsoft Foundry** — Um projeto com modelo implantado (ex: `gpt-5-mini`). Veja o [Passo 1](#passo-1-crie-um-projeto-microsoft-foundry) abaixo.

Incluímos um arquivo `requirements.txt` na raiz deste repositório que contém todos os pacotes Python necessários para executar os exemplos de código.

Você pode instalá-los executando o seguinte comando no terminal na raiz do repositório:

```bash|powershell
pip install -r requirements.txt
```

Recomendamos criar um ambiente virtual Python para evitar conflitos e problemas.

## Configuração do VSCode

Certifique-se de estar usando a versão correta do Python no VSCode.

![imagem](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configure o Microsoft Foundry e o Microsoft Foundry Agent Service

### Passo 1: Crie um Projeto Microsoft Foundry

Você precisa de um **hub** e **projeto** no Microsoft Foundry com um modelo implantado para executar os notebooks.

1. Vá para [ai.azure.com](https://ai.azure.com) e faça login com sua conta Azure.
2. Crie um **hub** (ou use um existente). Veja: [Visão geral dos recursos do Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Dentro do hub, crie um **projeto**.
4. Implemente um modelo (ex: `gpt-5-mini`) em **Modelos + Endpoints** → **Desplegar modelo**.

### Passo 2: Recupere o Endpoint do Projeto e o Nome da Implantação do Modelo

No seu projeto no portal Microsoft Foundry:

- **Endpoint do Projeto** — Vá para a página **Visão Geral** e copie o URL do endpoint.

![String de conexão do projeto](../../../translated_images/pt-BR/project-endpoint.8cf04c9975bbfbf1.webp)

- **Nome da Implantação do Modelo** — Vá para **Modelos + Endpoints**, selecione seu modelo implantado e anote o **Nome da implantação** (ex: `gpt-5-mini`).

### Passo 3: Faça login no Azure com `az login`

Todos os notebooks usam **`AzureCliCredential`** para autenticação — sem necessidade de gerenciar chaves API. Isso requer que você esteja logado via Azure CLI.

1. **Instale a Azure CLI** se ainda não tiver: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Faça login** executando:

    ```bash|powershell
    az login
    ```

    Ou, se estiver em um ambiente remoto/Codespace sem navegador:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Selecione sua assinatura** se solicitado — escolha aquela que contém seu projeto Foundry.

4. **Verifique** se você está logado:

    ```bash|powershell
    az account show
    ```

> **Por que `az login`?** Os notebooks autenticam usando `AzureCliCredential` do pacote `azure-identity`. Isso significa que sua sessão Azure CLI fornece as credenciais — sem chaves API ou segredos no arquivo `.env`. Esta é uma [melhor prática de segurança](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Passo 4: Crie seu arquivo `.env`

Copie o arquivo de exemplo:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Abra o `.env` e preencha estes dois valores:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variável | Onde encontrar |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → seu projeto → página **Visão Geral** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Modelos + Endpoints** → nome do seu modelo implantado |

Isso é tudo para a maioria das lições! Os notebooks irão autenticar automaticamente pela sua sessão `az login`.

### Passo 5: Instale as Dependências Python

```bash|powershell
pip install -r requirements.txt
```

Recomendamos executar isso dentro do ambiente virtual que você criou antes.

## Configuração Adicional para a Lição 5 (Agentic RAG)

A lição 5 usa **Azure AI Search** para geração aumentada por recuperação. Se planeja executar essa lição, adicione estas variáveis ao seu arquivo `.env`:

| Variável | Onde encontrar |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → seu recurso **Azure AI Search** → **Visão Geral** → URL |
| `AZURE_SEARCH_API_KEY` | Portal Azure → seu recurso **Azure AI Search** → **Configurações** → **Chaves** → chave administrativa primária |

## Configuração Adicional para Lições que Chamam Azure OpenAI Diretamente (Lições 6 e 8)

Alguns notebooks das lições 6 e 8 chamam o **Azure OpenAI** diretamente (usando a **API de Respostas**) em vez de passar por um projeto Microsoft Foundry. Esses exemplos usavam anteriormente Modelos do GitHub, que estão depreciados (aposentadoria em julho de 2026) e não suportam a API de Respostas. Se planeja executar esses exemplos, adicione estas variáveis ao seu arquivo `.env`:

| Variável | Onde encontrar |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portal Azure → seu recurso **Azure OpenAI** → **Chaves e Endpoint** → Endpoint (ex: `https://<seu-recurso>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | O nome do seu modelo implantado (ex: `gpt-5-mini`) que suporta a API de Respostas |
| `AZURE_OPENAI_API_KEY` | Opcional — somente se usar autenticação por chave em vez de `az login` / Entra ID |

> A API de Respostas usa o endpoint estável `/openai/v1/`, então nenhum `api-version` é necessário. Faça login com `az login` para usar autenticação Entra ID sem chave.

## Provedor Alternativo: MiniMax (Compatível com OpenAI)

[MiniMax](https://platform.minimaxi.com/) fornece modelos de contexto grande (até 204K tokens) através de uma API compatível OpenAI. Como o `OpenAIChatClient` do Microsoft Agent Framework funciona com qualquer endpoint compatível OpenAI, você pode usar MiniMax como alternativa direta ao Azure OpenAI ou OpenAI.

Adicione estas variáveis ao seu arquivo `.env`:

| Variável | Onde encontrar |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Plataforma MiniMax](https://platform.minimaxi.com/) → Chaves API |
| `MINIMAX_BASE_URL` | Use `https://api.minimax.io/v1` (valor padrão) |
| `MINIMAX_MODEL_ID` | Nome do modelo para usar (ex: `MiniMax-M3`) |

**Modelos exemplo**: `MiniMax-M3` (recomendado), `MiniMax-M2.7`, `MiniMax-M2.7-veloz` (respostas mais rápidas). Nomes e disponibilidade dos modelos podem mudar com o tempo, e o acesso a um modelo depende da sua conta ou região — consulte a [Plataforma MiniMax](https://platform.minimaxi.com/) para a lista atual. Se o `MiniMax-M3` não estiver disponível para sua conta, configure `MINIMAX_MODEL_ID` para um modelo que tenha acesso (ex: `MiniMax-M2.7`).

Os exemplos de código que usam `OpenAIChatClient` (ex: fluxo de reserva de hotel da Lição 14) detectarão e usarão automaticamente sua configuração MiniMax quando `MINIMAX_API_KEY` estiver definido.

## Provedor Alternativo: Foundry Local (Execute Modelos Localmente)

[Foundry Local](https://foundrylocal.ai) é um runtime leve que baixa, gerencia e serve modelos de linguagem **totalmente na sua própria máquina** via API compatível OpenAI — sem nuvem, assinatura Azure, ou chaves API. É uma ótima opção para desenvolvimento offline, experimentar sem custos na nuvem, ou manter dados localmente.

Como o `OpenAIChatClient` do Microsoft Agent Framework funciona com qualquer endpoint compatível OpenAI, o Foundry Local é uma alternativa local direta ao Azure OpenAI.

**1. Instale o Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Baixe e execute um modelo** (isso também inicia o serviço local):

```bash
foundry model list          # veja os modelos disponíveis
foundry model run phi-4-mini
```

**3. Instale o SDK Python** usado para descobrir o endpoint local:

```bash
pip install foundry-local-sdk
```

**4. Aponte o Microsoft Agent Framework para seu modelo local:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Baixa (se necessário) e serve o modelo localmente, então descobre o endpoint/porta.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ex. http://localhost:<porta>/v1
    api_key=manager.api_key,        # sempre "não-requerido" para Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Nota:** Foundry Local expõe um endpoint compatível OpenAI para **Chat Completions**. Use-o para desenvolvimento local e cenários offline. Para o conjunto completo de recursos da **API de Respostas** (conversas com estado, orquestração profunda de ferramentas e desenvolvimento estilo agente), utilize o **Azure OpenAI** ou um projeto **Microsoft Foundry** conforme mostrado nas lições. Veja a [documentação Foundry Local](https://foundrylocal.ai) para catálogo atual de modelos e suporte da plataforma.

## Configuração Adicional para a Lição 8 (Fluxo de Terreno Bing)


O notebook do fluxo condicional na lição 8 usa **integração Bing** via Microsoft Foundry. Se você planeja executar esse exemplo, adicione esta variável ao seu arquivo `.env`:

| Variável | Onde encontrá-la |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal Microsoft Foundry → seu projeto → **Gerenciamento** → **Recursos conectados** → sua conexão Bing → copie o ID da conexão |

## Solução de Problemas

### Erros de Verificação de Certificado SSL no macOS

Se você estiver no macOS e encontrar um erro como:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Este é um problema conhecido com Python no macOS onde os certificados SSL do sistema não são automaticamente confiáveis. Tente as soluções a seguir na ordem:

**Opção 1: Execute o script Install Certificates do Python (recomendado)**

```bash
# Substitua 3.XX pela versão do Python instalada (exemplo: 3.12 ou 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opção 2: Use `connection_verify=False` no seu notebook (apenas para notebooks GitHub Models)**

No notebook da Lição 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), uma solução alternativa comentada já está incluída. Remova o comentário de `connection_verify=False` ao criar o cliente:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Desative a verificação SSL se você encontrar erros de certificado
)
```

> **⚠️ Aviso:** Desabilitar a verificação SSL (`connection_verify=False`) reduz a segurança ao pular a validação do certificado. Use isso apenas como uma solução temporária em ambientes de desenvolvimento, nunca em produção.

**Opção 3: Instale e use `truststore`**

```bash
pip install truststore
```

Em seguida, adicione o seguinte no topo do seu notebook ou script antes de fazer quaisquer chamadas de rede:

```python
import truststore
truststore.inject_into_ssl()
```

## Preso em Algum Lugar?

Se você tiver qualquer problema ao executar essa configuração, entre no nosso <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord da Comunidade Azure AI</a> ou <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">crie uma issue</a>.

## Próxima Lição

Agora você está pronto para executar o código deste curso. Aproveite para aprender mais sobre o mundo dos Agentes de IA! 

[Introdução a Agentes de IA e Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->