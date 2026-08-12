# Configuração do Curso

## Introdução

Esta lição irá cobrir como executar os exemplos de código deste curso.

## Junte-se a Outros Estudantes e Obtenha Ajuda

Antes de começar a clonar o seu repositório, junte-se ao [canal Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) para obter qualquer ajuda com a configuração, esclarecer dúvidas sobre o curso ou para se conectar com outros estudantes.

## Clonar ou Fazer Fork deste Repositório

Para começar, por favor clone ou faça fork do Repositório GitHub. Assim terá a sua própria versão do material do curso para poder executar, testar e ajustar o código!

Isto pode ser feito clicando no link para <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fazer fork do repositório</a>

Agora deverá ter a sua própria versão fork deste curso no seguinte link:

![Forked Repo](../../../translated_images/pt-PT/forked-repo.33f27ca1901baa6a.webp)

### Clonagem Shallow (recomendado para workshop / Codespaces)

  >O repositório completo pode ser grande (~3 GB) quando descarrega todo o histórico e todos os ficheiros. Se vai apenas participar no workshop ou precisa só de algumas pastas de lições, uma clonagem shallow (ou uma clonagem sparse) evita a maior parte desse download ao truncar o histórico e/ou pular blobs.

#### Clonagem rápida shallow — histórico mínimo, todos os ficheiros

Substitua `<your-username>` nos comandos abaixo pela URL do seu fork (ou pela URL upstream se preferir).

Para clonar apenas o histórico do último commit (download pequeno):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Para clonar uma branch específica:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clonagem Parcial (sparse) — blobs mínimos + apenas pastas selecionadas

Isto usa clonagem parcial e sparse-checkout (requer Git 2.25+ e é recomendado usar uma versão moderna do Git com suporte a clonagem parcial):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Entre na pasta do repositório:

```bash|powershell
cd ai-agents-for-beginners
```

Depois especifique quais pastas quer (exemplo abaixo mostra duas pastas):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Depois de clonar e verificar os ficheiros, se precisar apenas dos ficheiros e quiser libertar espaço (sem histórico git), por favor apague os metadados do repositório (💀irreversível — perderá toda a funcionalidade Git: sem commits, pulls, pushes, ou acesso ao histórico).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Usando GitHub Codespaces (recomendado para evitar grandes downloads locais)

- Crie um novo Codespace para este repositório via a [interface GitHub](https://github.com/codespaces).  

- No terminal do codespace recém criado, execute um dos comandos de clonagem shallow/sparse acima para trazer apenas as pastas das lições que precisa para o espaço de trabalho do Codespace.
- Opcional: depois de clonar dentro dos Codespaces, remova o .git para recuperar espaço extra (veja os comandos de remoção acima).
- Nota: Se preferir abrir o repositório diretamente nos Codespaces (sem uma clonagem extra), tenha em conta que os Codespaces irão construir o ambiente devcontainer e podem ainda assim provisionar mais do que precisa. Clonar uma cópia shallow dentro de um Codespace novo oferece mais controlo sobre o uso do disco.

#### Dicas

- Substitua sempre a URL da clonagem pelo seu fork se quiser editar/fazer commit.
- Se mais tarde precisar de mais histórico ou ficheiros, pode buscá-los ou ajustar o sparse-checkout para incluir pastas adicionais.

## Executar o Código

Este curso oferece uma série de Jupyter Notebooks que pode executar para obter experiência prática a construir Agentes de IA.

Os exemplos de código usam o **Microsoft Agent Framework (MAF)** com o `FoundryChatClient`, que liga ao **Microsoft Foundry Agent Service V2** (a API Responses) através do **Microsoft Foundry**.

Todos os notebooks Python são identificados como `*-python-agent-framework.ipynb`.

## Requisitos

- Python 3.12+
  - **NOTA**: Se não tiver o Python3.12 instalado, certifique-se que o instala. Depois crie o seu venv usando python3.12 para garantir que as versões corretas sejam instaladas a partir do ficheiro requirements.txt.
  
    >Exemplo

    Criar diretório venv Python:

    ```bash|powershell
    python -m venv venv
    ```

    Depois ative o ambiente venv para:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Para os exemplos que usam .NET, certifique-se que instalou o [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ou posterior. Depois, verifique a versão do SDK .NET instalado:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Requerido para autenticação. Instale a partir de [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Assinatura Azure** — Para acesso ao Microsoft Foundry e ao Microsoft Foundry Agent Service.
- **Projeto Microsoft Foundry** — Um projeto com um modelo implementado (exemplo, `gpt-5-mini`). Veja o [Passo 1](#passo-1-criar-um-projeto-microsoft-foundry) abaixo.

Incluímos um ficheiro `requirements.txt` na raiz deste repositório que contém todos os pacotes Python necessários para executar os exemplos de código.

Pode instalá-los executando o seguinte comando no terminal na raiz do repositório:

```bash|powershell
pip install -r requirements.txt
```

Recomendamos criar um ambiente virtual Python para evitar quaisquer conflitos e problemas.

## Configurar VSCode

Assegure-se de que está a usar a versão correta do Python no VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configurar Microsoft Foundry e Microsoft Foundry Agent Service

### Passo 1: Criar um Projeto Microsoft Foundry

Precisa de um **hub** e um **projeto** no Microsoft Foundry com um modelo implementado para executar os notebooks.

1. Vá a [ai.azure.com](https://ai.azure.com) e inicie sessão com a sua conta Azure.
2. Crie um **hub** (ou use um existente). Veja: [Visão geral de recursos de Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Dentro do hub, crie um **projeto**.
4. Implemente um modelo (exemplo, `gpt-5-mini`) em **Models + Endpoints** → **Deploy model**.

### Passo 2: Obter o Endpoint do Projeto e o Nome da Implementação do Modelo

A partir do seu projeto no portal Microsoft Foundry:

- **Endpoint do Projeto** — Vá à página **Overview** e copie a URL do endpoint.

![Project Connection String](../../../translated_images/pt-PT/project-endpoint.8cf04c9975bbfbf1.webp)

- **Nome da Implementação do Modelo** — Vá a **Models + Endpoints**, selecione o modelo implementado, e note o **Deployment name** (exemplo, `gpt-5-mini`).

### Passo 3: Iniciar sessão no Azure com `az login`

Todos os notebooks usam **`AzureCliCredential`** para autenticação — não há chaves API para gerir. Isto requer que esteja autenticado via Azure CLI.

1. **Instale a Azure CLI** se ainda não o fez: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Inicie sessão** executando:

    ```bash|powershell
    az login
    ```

    Ou se estiver num ambiente remoto/Codespace sem navegador:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Selecione a sua subscrição** se for solicitado — escolha aquela que contém o seu projeto Foundry.

4. **Verifique** que está autenticado:

    ```bash|powershell
    az account show
    ```

> **Porquê `az login`?** Os notebooks autenticam usando `AzureCliCredential` do pacote `azure-identity`. Isto significa que a sua sessão Azure CLI fornece as credenciais — sem chaves API ou segredos no seu ficheiro `.env`. Isto é uma [boa prática de segurança](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Passo 4: Criar o seu ficheiro `.env`

Copie o ficheiro de exemplo:

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

Isto é tudo para a maioria das lições! Os notebooks irão autenticar automaticamente através da sua sessão `az login`.

### Passo 5: Instalar Dependências Python

```bash|powershell
pip install -r requirements.txt
```

Recomendamos executar isto dentro do ambiente virtual que criou anteriormente.

## Configuração Adicional para a Lição 5 (Agentic RAG)

A lição 5 usa **Azure AI Search** para geração com recuperação aumentada. Se pretende executar essa lição, adicione estas variáveis ao seu ficheiro `.env`:

| Variável | Onde encontrar |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → o seu recurso **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Portal Azure → o seu recurso **Azure AI Search** → **Settings** → **Keys** → chave administrativa principal |

## Configuração Adicional para Lições que Chama Azure OpenAI Diretamente (Lições 6 e 8)

Alguns notebooks nas lições 6 e 8 chamam diretamente o **Azure OpenAI** (usando a **Responses API**) em vez de passar por um projeto Microsoft Foundry. Estes exemplos usavam anteriormente os Modelos GitHub, que está descontinuado (aposentar em julho de 2026) e não suporta a Responses API. Se pretende executar esses exemplos, adicione estas variáveis ao seu ficheiro `.env`:

| Variável | Onde encontrar |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portal Azure → o seu recurso **Azure OpenAI** → **Keys and Endpoint** → Endpoint (ex. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Nome do modelo implantado (ex. `gpt-5-mini`) que suporta a Responses API |
| `AZURE_OPENAI_API_KEY` | Opcional — apenas se usar autenticação por chave em vez de `az login` / Entra ID |

> A Responses API usa o endpoint estável `/openai/v1/`, por isso não é necessário `api-version`. Inicie sessão com `az login` para usar autenticação Entra ID sem chave.

## Provedor Alternativo: MiniMax (Compatível com OpenAI)

[MiniMax](https://platform.minimaxi.com/) fornece modelos de grande contexto (até 204K tokens) através de uma API compatível com OpenAI. Como o `OpenAIChatClient` do Microsoft Agent Framework funciona com qualquer endpoint compatível com OpenAI, pode usar MiniMax como uma alternativa direta ao Azure OpenAI ou OpenAI.

Adicione estas variáveis ao seu ficheiro `.env`:

| Variável | Onde encontrar |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Use `https://api.minimax.io/v1` (valor padrão) |
| `MINIMAX_MODEL_ID` | Nome do modelo a usar (exemplo, `MiniMax-M3`) |

**Modelos exemplares**: `MiniMax-M3` (recomendado), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (respostas mais rápidas). Os nomes e a disponibilidade dos modelos podem mudar ao longo do tempo, e o acesso a determinado modelo pode depender da sua conta ou região — verifique a [MiniMax Platform](https://platform.minimaxi.com/) para a lista atual. Se `MiniMax-M3` não estiver disponível para a sua conta, defina `MINIMAX_MODEL_ID` para um modelo a que tenha acesso (ex. `MiniMax-M2.7`).

Os exemplos que usam `OpenAIChatClient` (exemplo, fluxo de reserva de hotel na Lição 14) irão automaticamente detetar e usar a sua configuração MiniMax quando `MINIMAX_API_KEY` estiver definido.

## Provedor Alternativo: Foundry Local (Execute Modelos Localmente)

[Foundry Local](https://foundrylocal.ai) é um runtime leve que descarrega, gere e serve modelos de linguagem **completamente na sua própria máquina** através de uma API compatível com OpenAI — sem cloud, sem subscrição Azure, e sem chaves API. É uma ótima opção para desenvolvimento offline, experimentar sem custos de cloud, ou manter dados localmente.

Como o `OpenAIChatClient` do Microsoft Agent Framework funciona com qualquer endpoint compatível OpenAI, o Foundry Local é uma alternativa local direta ao Azure OpenAI.

**1. Instalar Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Descarregar e executar um modelo** (isto também inicia o serviço local):

```bash
foundry model list          # ver modelos disponíveis
foundry model run phi-4-mini
```

**3. Instalar o SDK Python** usado para descobrir o endpoint local:

```bash
pip install foundry-local-sdk
```

**4. Configure o Microsoft Agent Framework para o seu modelo local:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Transfere (se necessário) e serve o modelo localmente, depois descobre o endpoint/porto.
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

> **Nota:** O Foundry Local expõe um endpoint de **Chat Completions** compatível OpenAI. Use-o para desenvolvimento local e cenários offline. Para o conjunto completo de funcionalidades da **Responses API** (conversas com estado, orquestração profunda de ferramentas, e desenvolvimento no estilo agente), direcione para o **Azure OpenAI** ou para um projeto **Microsoft Foundry** conforme mostrado nas lições. Veja a [documentação do Foundry Local](https://foundrylocal.ai) para o catálogo atual de modelos e suporte à plataforma.

## Configuração Adicional para a Lição 8 (Fluxo de Trabalho Bing Grounding)


O notebook do fluxo de trabalho condicional na lição 8 utiliza **fundamentação Bing** através do Microsoft Foundry. Se planeia executar esse exemplo, adicione esta variável ao seu ficheiro `.env`:

| Variável | Onde encontrá-la |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal Microsoft Foundry → o seu projeto → **Gestão** → **Recursos ligados** → a sua ligação Bing → copiar o ID da ligação |

## Resolução de Problemas

### Erros de Verificação de Certificado SSL no macOS

Se estiver no macOS e encontrar um erro como:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Este é um problema conhecido com o Python no macOS onde os certificados SSL do sistema não são automaticamente confiáveis. Experimente as seguintes soluções pela ordem:

**Opção 1: Execute o script Install Certificates do Python (recomendado)**

```bash
# Substitua 3.XX pela sua versão instalada do Python (ex., 3.12 ou 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opção 2: Use `connection_verify=False` no seu notebook (apenas para notebooks GitHub Models)**

No notebook da Lição 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), já está incluída uma solução alternativa comentada. Descomente `connection_verify=False` ao criar o cliente:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Desativar a verificação SSL se encontrar erros de certificado
)
```

> **⚠️ Aviso:** Desativar a verificação SSL (`connection_verify=False`) reduz a segurança ao evitar a validação do certificado. Use isto apenas como solução temporária em ambientes de desenvolvimento, nunca em produção.

**Opção 3: Instale e use `truststore`**

```bash
pip install truststore
```

Depois adicione o seguinte no início do seu notebook ou script antes de efetuar quaisquer chamadas de rede:

```python
import truststore
truststore.inject_into_ssl()
```

## Preso em Algum Lado?

Se tiver algum problema a executar esta configuração, entre na nossa <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidade Azure AI no Discord</a> ou <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">crie um issue</a>.

## Próxima Lição

Já está pronto para executar o código deste curso. Feliz aprendizagem sobre o mundo dos Agentes de IA! 

[Introdução aos Agentes de IA e Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->