# Configuração do Curso

## Introdução

Esta lição irá cobrir como executar os exemplos de código deste curso.

## Junte-se a Outros Alunos e Obtenha Ajuda

Antes de começar a clonar o seu repositório, junte-se ao [canal Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) para obter ajuda com a configuração, esclarecer dúvidas sobre o curso ou conectar-se com outros alunos.

## Clonar ou Fazer Fork deste Repositório

Para começar, por favor clone ou faça fork do Repositório no GitHub. Isto criará a sua própria versão do material do curso para que possa executar, testar e ajustar o código!

Isto pode ser feito clicando no link para <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fazer fork do repositório</a>

Deve agora ter a sua própria versão forkada deste curso no seguinte link:

![Forked Repo](../../../translated_images/pt-PT/forked-repo.33f27ca1901baa6a.webp)

### Clone Raso (recomendado para workshops / Codespaces)

  >O repositório completo pode ser grande (~3 GB) quando descarrega todo o histórico e todos os ficheiros. Se estiver apenas a participar no workshop ou só precisar de algumas pastas das lições, um clone raso (ou clone esparso) descarrega muito menos.

#### Clone raso rápido — histórico mínimo, todos os ficheiros

Substitua `<your-username>` nos comandos abaixo pelo URL do seu fork (ou o URL upstream, se preferir).

Para clonar apenas o histórico do último commit (descarregamento pequeno):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Para clonar um ramo específico:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clone Parcial (esparso) — blobs mínimos + somente pastas selecionadas

Isto utiliza clone parcial e checkout esparso (requere Git 2.25+ e recomenda-se Git moderno com suporte a clone parcial):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Navegue até à pasta do repositório:

```bash
cd ai-agents-for-beginners
```

Depois, especifique as pastas que deseja (o exemplo abaixo mostra duas pastas):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Após clonar e verificar os ficheiros, se apenas precisar dos ficheiros e quiser libertar espaço (sem histórico git), por favor apague os metadados do repositório (💀irrevogável — perderá toda a funcionalidade do Git):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Utilizando GitHub Codespaces (recomendado para evitar grandes transferências locais)

- Crie um novo Codespace para este repositório via a [interface do GitHub](https://github.com/codespaces).  

- No terminal do Codespace recém criado, execute um dos comandos de clone raso/esparso acima para trazer apenas as pastas das lições de que precisa para o ambiente de trabalho do Codespace.
- Opcional: depois de clonar dentro dos Codespaces, remova a pasta .git para recuperar espaço extra (consulte os comandos de remoção acima).
- Nota: Se preferir abrir o repositório diretamente nos Codespaces (sem um clone extra), esteja ciente que os Codespaces irão construir o ambiente devcontainer e podem ainda assim provisionar mais do que precisa.

#### Dicas

- Substitua sempre o URL do clone pelo seu fork se desejar editar/fazer commits.
- Se mais tarde precisar de mais histórico ou ficheiros, pode fazer fetch desses ou ajustar o checkout esparso para incluir pastas adicionais.

## Executar o Código

Este curso oferece uma série de Jupyter Notebooks que pode executar para obter experiência prática a construir Agentes de IA.

Os exemplos de código usam o **Microsoft Agent Framework (MAF)** com o `FoundryChatClient`, que se liga ao **Microsoft Foundry Agent Service V2** (a API Responses) através do **Microsoft Foundry**.

Todos os notebooks em Python têm o rótulo `*-python-agent-framework.ipynb`.

## Requisitos

- Python 3.12+
  - **NOTA**: Se não tiver Python3.12 instalado, assegure-se de o instalar. Depois crie o seu ambiente virtual usando python3.12 para garantir que as versões corretas são instaladas a partir do ficheiro requirements.txt.
  
    >Exemplo

    Criar diretório de ambiente virtual Python:

    ```bash
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

- .NET 10+: Para os exemplos que usam .NET, assegure que instala o [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ou superior. Depois, verifique a sua versão instalada do SDK .NET:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Necessário para autenticação. Instale a partir de [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Subscrição Azure** — Para acesso ao Microsoft Foundry e Microsoft Foundry Agent Service.
- **Projeto Microsoft Foundry** — Um projeto com um modelo implementado (ex: `gpt-5-mini`). Veja [Passo 1](#passo-1-criar-um-projeto-microsoft-foundry) abaixo.

Incluímos um ficheiro `requirements.txt` na raiz deste repositório com todos os pacotes Python necessários para executar os exemplos de código.

Pode instalá-los correndo o seguinte comando no terminal na raiz do repositório:

```bash
pip install -r requirements.txt
```

Recomendamos criar um ambiente virtual Python para evitar conflitos e problemas.

## Configurar VSCode

Assegure-se de que está a usar a versão correta do Python no VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configurar Microsoft Foundry e Microsoft Foundry Agent Service

### Passo 1: Criar um Projeto Microsoft Foundry

Vai precisar de um **hub** e de um **projeto** Microsoft Foundry com um modelo implementado para executar os notebooks.

1. Vá a [ai.azure.com](https://ai.azure.com) e inicie sessão com a sua conta Azure.
2. Crie um **hub** (ou use um existente). Veja: [Visão geral dos recursos do Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Dentro do hub, crie um **projeto**.
4. Implemente um modelo (ex: `gpt-5-mini`) a partir de **Models + Endpoints** → **Deploy model**.

### Passo 2: Obter o Endpoint do Projeto e o Nome da Implementação do Modelo

A partir do seu projeto no portal Microsoft Foundry:

- **Endpoint do Projeto** — Vá à página **Overview** e copie a URL do endpoint.

![Project Connection String](../../../translated_images/pt-PT/project-endpoint.8cf04c9975bbfbf1.webp)

- **Nome da Implementação do Modelo** — Vá a **Models + Endpoints**, selecione o seu modelo implementado e anote o **Deployment name** (ex: `gpt-5-mini`).

### Passo 3: Inicie sessão no Azure com `az login`

A maioria dos notebooks autentica-se através da **sessão de inicio de sessão Azure CLI** — usando `AzureCliCredential` ou `DefaultAzureCredential` (ambos captam a sua sessão `az login`) do pacote `azure-identity` — logo não exigem chaves API. Algumas lições e integrações opcionais usam chaves API; verifique os pré-requisitos de cada lição para variáveis de ambiente adicionais. Isto requer que esteja autenticado na Azure CLI.

1. **Instale a Azure CLI** se ainda não o fez: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Inicie sessão** executando:

    ```bash
    az login
    ```

    Ou se estiver num ambiente remoto/Codespace sem navegador:

    ```bash
    az login --use-device-code
    ```

3. **Selecione a sua subscrição** se for pedido — escolha aquela que contém o seu projeto Foundry.

4. **Verifique** se está autenticado:

    ```bash
    az account show
    ```

> **Porquê usar `az login`?** Os notebooks autenticam usando `AzureCliCredential` (ou `DefaultAzureCredential`, que também usa o início de sessão Azure CLI) do pacote `azure-identity`. Isso significa que a sua sessão Azure CLI fornece as credenciais — sem chaves API ou segredos no seu ficheiro `.env`. Esta é uma [boa prática de segurança](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Passo 4: Criar o seu ficheiro `.env`

Copie o ficheiro exemplo:

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
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → o seu projeto → página **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → nome do modelo implementado |

Está tudo para a maioria das lições! Os notebooks irão autenticar automaticamente através da sua sessão `az login`.

### Passo 5: Instalar as Dependências Python

```bash
pip install -r requirements.txt
```

Recomendamos executar isto dentro do ambiente virtual que criou anteriormente.

## Configuração Opcional: Azure AI Search (Lições 5 e 16)

Os notebooks da Lição 5 (Agentic RAG) e Lição 16 funcionam imediatamente com uma **base de conhecimento em memória** — não são necessários recursos adicionais Azure. Se quiser suportá-los com um índice real do **Azure AI Search**, note que o **notebook da Lição 16 usa atualmente autenticação por chave**: muda da pesquisa em memória para Azure AI Search apenas quando **tanto** `AZURE_SEARCH_SERVICE_ENDPOINT` **quanto** `AZURE_SEARCH_API_KEY` estão definidos; caso contrário, mantém a pesquisa em memória — portanto, para o executar contra um índice real, deve definir também a chave administrativa. A autenticação sem chave com Microsoft Entra ID (RBAC) é a abordagem recomendada para o seu próprio código em produção, consistente com o fluxo `az login` usado em todo o resto do curso.

Os passos de RBAC abaixo aplicam-se aos exemplos do guia de configuração e ao seu próprio código. Eles não ativam a autenticação sem chave no notebook da Lição 16; a Lição 16 ainda requer tanto o endpoint quanto a chave administrativa para usar o Azure AI Search.

1. **Ative o controlo de acesso baseado em funções (RBAC)** no seu serviço de pesquisa:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Atribua a si mesmo as permissões necessárias** (criar/carregar índices e consultar):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Adicione o endpoint** ao seu ficheiro `.env`:

| Variável | Onde encontrar |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → seu recurso **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Necessária (juntamente com o endpoint) para ativar Azure AI Search no notebook da Lição 16, que usa autenticação por chave. Portal Azure → **Settings** → **Keys** → chave administrativa primária |

> **Porquê sem chave?** Chaves administrativas concedem acesso total de escrita ao seu serviço de pesquisa e podem vazar via ficheiros `.env`. Com RBAC, a sua identidade `az login` é usada — o mesmo padrão sem chave Entra ID que os notebooks do curso usam (via `AzureCliCredential` / `DefaultAzureCredential`). Veja [Conectar ao Azure AI Search usando funções](https://learn.microsoft.com/azure/search/search-security-rbac).

Veja o [guia de configuração do Azure AI Search](./AzureSearch.md) para exemplos completos de criação de índice em Python e .NET.

## Configuração Adicional para Lições que Chamam Azure OpenAI Diretamente (Lições 6 e 8)

Alguns notebooks nas lições 6 e 8 chamam **Azure OpenAI** diretamente (usando a **Responses API**) em vez de passar por um projeto Microsoft Foundry. Estes exemplos usavam anteriormente GitHub Models, que está obsoleto e não suporta a Responses API. Adicione estas variáveis ao seu ficheiro `.env`:

| Variável | Onde encontrar |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portal Azure → seu recurso **Azure OpenAI** → **Keys and Endpoint** → Endpoint (ex: `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Nome do seu modelo implementado (ex: `gpt-5-mini`) que suporta a Responses API |
| `AZURE_OPENAI_API_KEY` | Opcional — apenas se usar autenticação por chave em vez de `az login` / Entra ID |

> A Responses API usa o endpoint estável `/openai/v1/`, por isso não é necessário `api-version`. Inicie sessão com `az login` para usar autenticação sem chave Entra ID.

## Provedor Alternativo: MiniMax (Compatível com OpenAI)

[MiniMax](https://platform.minimaxi.com/) disponibiliza modelos de contexto extenso (até 204K tokens) através de uma API compatível com OpenAI. Como o `OpenAIChatClient` do Microsoft Agent Framework funciona com qualquer endpoint compatível com OpenAI, pode usar MiniMax como alternativa para as lições que utilizam `OpenAIChatClient`.

Adicione estas variáveis ao seu ficheiro `.env`:

| Variável | Onde encontrar |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Plataforma MiniMax](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Use `https://api.minimax.io/v1` (valor padrão) |
| `MINIMAX_MODEL_ID` | Nome do modelo a usar (ex: `MiniMax-M3`) |

**Modelos exemplo**: `MiniMax-M3` (recomendado), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (respostas mais rápidas). Os nomes e a disponibilidade dos modelos podem mudar ao longo do tempo e o acesso a um dado modelo pode depender da sua conta.

Os exemplos de código que usam `OpenAIChatClient` (ex: o fluxo de reserva de hotel da Lição 14) vão detetar e usar automaticamente a sua configuração MiniMax quando `MINIMAX_API_KEY` estiver definida.


## Fornecedor Alternativo: Novita AI (Compatível com OpenAI)

[Novita AI](https://novita.ai/llm-api) fornece uma API compatível com OpenAI para LLMs open-source e de vanguarda (DeepSeek, Llama, Qwen, e mais). Como o `OpenAIChatClient` do Microsoft Agent Framework funciona com qualquer endpoint compatível com OpenAI, pode usar o Novita AI como uma alternativa plug-and-play ao Azure OpenAI ou OpenAI.

Adicione estas variáveis ao seu ficheiro `.env`:

| Variável | Onde encontrar |
|----------|-----------------|
| `NOVITA_API_KEY` | [Painel Novita AI](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | Use `https://api.novita.ai/openai/v1` (valor predefinido) |
| `NOVITA_MODEL_ID` | Nome do modelo a usar (ex., `moonshotai/kimi-k3`) |

**Modelos de exemplo**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. O Novita AI também hospeda muitas outras famílias de modelos open-source (Llama, Qwen, GLM, e mais) — consulte a [biblioteca de modelos Novita AI](https://novita.ai/llm-api) para a lista atual de modelos disponíveis e respetivos IDs.

Os exemplos atuais não consomem automaticamente as variáveis `NOVITA_*`. Para usar o Novita AI, passe estes valores explicitamente ao construir o `OpenAIChatClient` no exemplo que estiver a executar.

## Fornecedor Alternativo: Foundry Local (Execute Modelos no Dispositivo)

[Foundry Local](https://foundrylocal.ai) é um runtime leve que descarrega, gere e serve modelos de linguagem **inteiramente na sua própria máquina** através de uma API compatível com OpenAI — sem necessidade de nuvem.

Como o `OpenAIChatClient` do Microsoft Agent Framework funciona com qualquer endpoint compatível com OpenAI, o Foundry Local é uma alternativa local plug-and-play ao Azure OpenAI.

**1. Instale o Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Descarregue e execute um modelo** (isto também inicia o serviço local):

```bash
foundry model list          # ver modelos disponíveis
foundry model run phi-4-mini
```

**3. Instale o SDK Python** usado para descobrir o endpoint local:

```bash
pip install foundry-local-sdk
```

**4. Aponte o Microsoft Agent Framework para o seu modelo local:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Descarrega (se necessário) e serve o modelo localmente, depois descobre o endpoint/porta.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # por exemplo http://localhost:<port>/v1
    api_key=manager.api_key,        # sempre "não necessário" para Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Nota:** O Foundry Local expõe um endpoint de **Chat Completions** compatível com OpenAI. Use-o para desenvolvimento local e cenários offline. Para o conjunto completo de funcionalidades da **API Responses** (conversas com estado, etc.), use Azure OpenAI ou um projeto Microsoft Foundry.

## Configuração Adicional para a Aula 8 (Fluxo de Trabalho de Fundamentação Bing)

O notebook condicional da aula 8 usa **fundamentação Bing** via Microsoft Foundry. Se pretender executar esse exemplo, adicione esta variável ao seu ficheiro `.env`:

| Variável | Onde encontrar |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal Microsoft Foundry → o seu projeto → **Gestão** → **Recursos ligados** → a sua ligação Bing → copie o ID da ligação |

## Resolução de Problemas

### Erros de Verificação de Certificado SSL no macOS

Se usar macOS e encontrar um erro como:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Este é um problema conhecido com Python no macOS onde os certificados SSL do sistema não são automaticamente confiáveis. Experimente as seguintes soluções por ordem:

**Opção 1: Execute o script Install Certificates do Python (recomendado)**

```bash
# Substitua 3.XX pela versão do Python que tem instalada (ex., 3.12 ou 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opção 2: Use `connection_verify=False` no seu notebook (apenas para notebooks GitHub Models)**

No notebook da Aula 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), já está incluída uma solução comentada. Descomente `connection_verify=False` quando encontrar erros de certificado:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Desativar a verificação SSL se encontrar erros de certificado
)
```

> **⚠️ Aviso:** Desativar a verificação SSL (`connection_verify=False`) reduz a segurança ao ignorar a validação do certificado. Use apenas como solução temporária em ambientes de desenvolvimento. Nunca utilize em produção.

**Opção 3: Instale e use `truststore`**

```bash
pip install truststore
```

Depois adicione o seguinte no topo do seu notebook ou script antes de fazer qualquer chamada de rede:

```python
import truststore
truststore.inject_into_ssl()
```

## Preso em Algum Lado?

Se encontrar algum problema a executar esta configuração, entre na nossa <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidade Azure AI no Discord</a> ou <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">crie um problema</a>.

## Próxima Aula

Já está pronto para executar o código deste curso. Boa aprendizagem sobre o mundo dos Agentes de IA!

[Introdução aos Agentes de IA e Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->