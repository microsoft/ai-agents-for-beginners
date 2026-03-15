# Configuração do Curso

## Introdução

Nesta lição será abordado como executar os exemplos de código deste curso.

## Junte-se a outros aprendizes e obtenha ajuda

Antes de começar a clonar seu repositório, junte-se ao [canal do Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) para obter ajuda com a configuração, tirar dúvidas sobre o curso ou conectar-se com outros aprendizes.

## Clonar ou fazer fork deste repositório

Para começar, por favor clone ou faça fork do repositório do GitHub. Isso criará sua própria versão do material do curso para que você possa executar, testar e ajustar o código!

This can be done by clicking the link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fazer fork do repositório</a>

Você agora deve ter sua própria versão forkada deste curso no link a seguir:

![Repositório Forkado](../../../translated_images/pt-BR/forked-repo.33f27ca1901baa6a.webp)

### Clone superficial (recomendado para workshop / Codespaces)

  >O repositório completo pode ser grande (~3 GB) quando você baixa todo o histórico e todos os arquivos. Se você está apenas participando do workshop ou precisa apenas de algumas pastas de lição, um clone superficial (ou um clone esparso) evita a maior parte desse download ao truncar o histórico e/ou pular blobs.

#### Clone superficial rápido — histórico mínimo, todos os arquivos

Replace `<your-username>` in the below commands with your fork URL (or the upstream URL if you prefer).

To clone only the latest commit history (small download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

To clone a specific branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clone parcial (esparso) — blobs mínimos + apenas pastas selecionadas

This uses partial clone and sparse-checkout (requires Git 2.25+ and recommended modern Git with partial clone support):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Traverse into the repo folder:

```bash|powershell
cd ai-agents-for-beginners
```

Then specify which folders you want (example below shows two folders):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

After cloning and verifying the files, if you only need files and want to free space (no git history), please delete the repository metadata (💀irreversible — you will lose all Git functionality: no commits, pulls, pushes, or history access).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Usando o GitHub Codespaces (recomendado para evitar downloads locais grandes)

- Crie um novo Codespace para este repositório via a [interface do GitHub](https://github.com/codespaces).  

- No terminal do Codespace recém-criado, execute um dos comandos de clone superficial/esparso acima para trazer apenas as pastas de lição que você precisa para o workspace do Codespace.
- Opcional: após clonar dentro do Codespaces, remova .git para recuperar espaço extra (veja os comandos de remoção acima).
- Observação: Se preferir abrir o repositório diretamente no Codespaces (sem um clone extra), esteja ciente de que o Codespaces construirá o ambiente devcontainer e pode ainda provisionar mais do que você precisa. Clonar uma cópia superficial dentro de um Codespace novo dá mais controle sobre o uso de disco.

#### Dicas

- Sempre substitua o clone URL com o seu fork se você quiser editar/commit.
- Se você mais tarde precisar de mais histórico ou arquivos, você pode buscá-los ou ajustar o sparse-checkout para incluir pastas adicionais.

## Executando o Código

Este curso oferece uma série de Jupyter Notebooks que você pode executar para obter experiência prática construindo Agentes de IA.

The code samples use **Microsoft Agent Framework (MAF)** with the `AzureAIProjectAgentProvider`, which connects to **Azure AI Agent Service V2** (the Responses API) through **Microsoft Foundry**.

All Python notebooks are labelled `*-python-agent-framework.ipynb`.

## Requisitos

- Python 3.12+
  - **NOTA**: Se você não tiver o Python 3.12 instalado, certifique-se de instalá-lo. Em seguida, crie seu venv usando python3.12 para garantir que as versões corretas sejam instaladas a partir do arquivo requirements.txt.
  
    >Exemplo

    Create Python venv directory:

    ```bash|powershell
    python -m venv venv
    ```

    Then activate venv environment for:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Para os exemplos que usam .NET, certifique-se de instalar o [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ou posterior. Em seguida, verifique a versão do SDK .NET instalada:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Necessária para autenticação. Instale a partir de [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Assinatura do Azure** — Para acesso ao Microsoft Foundry e ao Azure AI Agent Service.
- **Projeto Microsoft Foundry** — Um projeto com um modelo implantado (por exemplo, `gpt-4o`). Veja [Passo 1](../../../00-course-setup) abaixo.

We have included a `requirements.txt` file in the root of this repository that contains all the required Python packages to run the code samples.

Você pode instalá-los executando o seguinte comando no seu terminal na raiz do repositório:

```bash|powershell
pip install -r requirements.txt
```

Recomendamos criar um ambiente virtual Python para evitar quaisquer conflitos e problemas.

## Configurar o VSCode

Certifique-se de que você está usando a versão correta do Python no VSCode.

![imagem](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configurar o Microsoft Foundry e o Azure AI Agent Service

### Passo 1: Criar um projeto Microsoft Foundry

Você precisa de um **hub** e de um **projeto** no Azure AI Foundry com um modelo implantado para executar os notebooks.

1. Acesse [ai.azure.com](https://ai.azure.com) e entre com sua conta do Azure.
2. Crie um **hub** (ou use um existente). Veja: [Visão geral dos recursos do Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Dentro do hub, crie um **projeto**.
4. Faça o deploy de um modelo (por exemplo, `gpt-4o`) em **Models + Endpoints** → **Deploy model**.

### Passo 2: Recupere o Endpoint do seu Projeto e o Nome da Implantação do Modelo

No seu projeto no portal do Microsoft Foundry:

- **Project Endpoint** — Vá para a página **Overview** e copie o endpoint URL.

![String de Conexão do Projeto](../../../translated_images/pt-BR/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Vá para **Models + Endpoints**, selecione seu modelo implantado e anote o **Deployment name** (por exemplo, `gpt-4o`).

### Passo 3: Faça login no Azure com `az login`

All notebooks use **`AzureCliCredential`** for authentication — no API keys to manage. This requires you to be signed in via the Azure CLI.

1. **Instale o Azure CLI** se ainda não o fez: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Faça login** executando:

    ```bash|powershell
    az login
    ```

    Ou se você estiver em um ambiente remoto/Codespace sem um navegador:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Selecione sua assinatura** se solicitado — escolha a que contém seu projeto Foundry.

4. **Verifique** se você está logado:

    ```bash|powershell
    az account show
    ```

> **Por que `az login`?** Os notebooks autenticam usando `AzureCliCredential` do pacote `azure-identity`. Isso significa que sua sessão do Azure CLI fornece as credenciais — sem chaves de API ou segredos no seu arquivo `.env`. Esta é uma [melhor prática de segurança](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

Abra `.env` e preencha estes dois valores:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → your project → **Overview** page |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → your deployed model's name |

Isso é tudo para a maioria das lições! Os notebooks irão autenticar automaticamente por meio da sua sessão `az login`.

### Passo 5: Instale as dependências Python

```bash|powershell
pip install -r requirements.txt
```

Recomendamos executar isso dentro do ambiente virtual que você criou anteriormente.

## Configuração adicional para a Lição 5 (Agentic RAG)

A Lição 5 usa **Azure AI Search** para geração aumentada por recuperação. Se você pretende executar essa lição, adicione estas variáveis ao seu arquivo `.env`:

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → your **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → your **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## Configuração adicional para as Lições 6 e 8 (GitHub Models)

Alguns notebooks das lições 6 e 8 usam **GitHub Models** em vez do Azure AI Foundry. Se pretende executar esses exemplos, adicione estas variáveis ao seu arquivo `.env`:

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## Configuração adicional para a Lição 8 (Bing Grounding Workflow)

O notebook de fluxo de trabalho condicional na lição 8 usa **Bing grounding** via Azure AI Foundry. Se pretende executar esse exemplo, adicione esta variável ao seu arquivo `.env`:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → your project → **Management** → **Connected resources** → your Bing connection → copy the connection ID |

## Solução de Problemas

### Erros de Verificação de Certificado SSL no macOS

Se você estiver no macOS e encontrar um erro como:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Este é um problema conhecido do Python no macOS onde os certificados SSL do sistema não são automaticamente confiáveis. Tente as seguintes soluções na ordem:

**Opção 1: Execute o script Install Certificates do Python (recomendado)**

```bash
# Substitua 3.XX pela versão do Python instalada (por exemplo, 3.12 ou 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opção 2: Use `connection_verify=False` no seu notebook (somente para notebooks de GitHub Models)**

No notebook da Lição 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), um workaround comentado já está incluído. Remova o comentário de `connection_verify=False` ao criar o cliente:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Desative a verificação SSL se encontrar erros de certificado
)
```

> **⚠️ Aviso:** Desativar a verificação SSL (`connection_verify=False`) reduz a segurança ao pular a validação de certificado. Use isso apenas como um workaround temporário em ambientes de desenvolvimento, nunca em produção.

**Opção 3: Instale e use `truststore`**

```bash
pip install truststore
```

Em seguida, adicione o seguinte no topo do seu notebook ou script antes de fazer quaisquer chamadas de rede:

```python
import truststore
truststore.inject_into_ssl()
```

## Preso em algum lugar?

Se você tiver qualquer problema ao executar esta configuração, entre em nosso <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord da Comunidade Azure AI</a> ou <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">abra uma issue</a>.

## Próxima Lição

Você agora está pronto para executar o código deste curso. Bom aprendizado no mundo dos Agentes de IA! 

[Introdução a Agentes de IA e Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Isenção de Responsabilidade**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->