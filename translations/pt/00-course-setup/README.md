<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T08:36:59+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "pt"
}
-->
# Configuração do Curso

## Introdução

Esta lição abordará como executar os exemplos de código deste curso.

## Junte-se a Outros Alunos e Obtenha Ajuda

Antes de começar a clonar o seu repositório, junte-se ao [canal Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) para obter ajuda com a configuração, esclarecer dúvidas sobre o curso ou conectar-se com outros alunos.

## Clonar ou Fazer Fork deste Repositório

Para começar, por favor, clone ou faça um fork do repositório GitHub. Isso criará a sua própria versão do material do curso para que possa executar, testar e ajustar o código!

Isso pode ser feito clicando no link para <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fazer fork do repositório</a>.

Agora deverá ter a sua própria versão do curso no seguinte link:

![Repositório Forkado](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.pt.png)

### Clone Superficial (recomendado para workshop / Codespaces)

  >O repositório completo pode ser grande (~3 GB) ao fazer o download do histórico completo e de todos os ficheiros. Se estiver apenas a participar do workshop ou precisar apenas de algumas pastas de lições, um clone superficial (ou um clone esparso) evita a maior parte desse download, truncando o histórico e/ou ignorando blobs.

#### Clone superficial rápido — histórico mínimo, todos os ficheiros

Substitua `<your-username>` nos comandos abaixo pelo URL do seu fork (ou o URL original, se preferir).

Para clonar apenas o histórico do último commit (download pequeno):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Para clonar um ramo específico:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clone parcial (esparso) — blobs mínimos + apenas pastas selecionadas

Isto utiliza clone parcial e checkout esparso (requer Git 2.25+ e Git moderno recomendado com suporte a clone parcial):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Aceda à pasta do repositório:

Para bash:

```bash
cd ai-agents-for-beginners
```

Para Powershell:

```powershell
Set-Location ai-agents-for-beginners
```

Depois, especifique quais pastas deseja (o exemplo abaixo mostra duas pastas):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Após clonar e verificar os ficheiros, se precisar apenas dos ficheiros e quiser liberar espaço (sem histórico do git), por favor, apague os metadados do repositório (💀irreversível — perderá toda a funcionalidade do Git: sem commits, pulls, pushes ou acesso ao histórico).

Para Linux/macOS:

```bash
rm -rf .git
```

Para Windows:

```powershell
Remove-Item -Recurse -Force .git
```

#### Usar GitHub Codespaces (recomendado para evitar grandes downloads locais)

- Crie um novo Codespace para este repositório através da [interface do GitHub](https://github.com/codespaces).  

- No terminal do Codespace recém-criado, execute um dos comandos de clone superficial/esparso acima para trazer apenas as pastas de lições necessárias para o espaço de trabalho do Codespace.
- Opcional: após clonar dentro do Codespaces, remova o .git para recuperar espaço extra (veja os comandos de remoção acima).
- Nota: Se preferir abrir o repositório diretamente no Codespaces (sem um clone extra), esteja ciente de que o Codespaces construirá o ambiente devcontainer e ainda poderá provisionar mais do que o necessário. Clonar uma cópia superficial dentro de um Codespace novo dá-lhe mais controlo sobre o uso do disco.

#### Dicas

- Substitua sempre o URL do clone pelo seu fork se quiser editar/commitar.
- Se mais tarde precisar de mais histórico ou ficheiros, pode buscá-los ou ajustar o checkout esparso para incluir pastas adicionais.

## Executar o Código

Este curso oferece uma série de Jupyter Notebooks que pode executar para obter experiência prática na construção de Agentes de IA.

Os exemplos de código utilizam:

**Requer Conta GitHub - Gratuita**:

1) Framework Semantic Kernel Agent + GitHub Models Marketplace. Identificado como (semantic-kernel.ipynb)
2) Framework AutoGen + GitHub Models Marketplace. Identificado como (autogen.ipynb)

**Requer Subscrição Azure**:
3) Azure AI Foundry + Azure AI Agent Service. Identificado como (azureaiagent.ipynb)

Incentivamos a experimentar os três tipos de exemplos para ver qual funciona melhor para si.

Qualquer que seja a opção escolhida, isso determinará quais etapas de configuração precisa seguir abaixo:

## Requisitos

- Python 3.12+
  - **NOTA**: Se não tiver Python3.12 instalado, certifique-se de instalá-lo. Depois, crie o seu venv usando python3.12 para garantir que as versões corretas sejam instaladas a partir do ficheiro requirements.txt.
  
    >Exemplo

    Criar diretório Python venv:

    ``` bash
    python3 -m venv venv
    ```

    Depois, ative o ambiente venv para:

    macOS e Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- Uma Conta GitHub - Para acesso ao GitHub Models Marketplace
- Subscrição Azure - Para acesso ao Azure AI Foundry
- Conta Azure AI Foundry - Para acesso ao Azure AI Agent Service

Incluímos um ficheiro `requirements.txt` na raiz deste repositório que contém todos os pacotes Python necessários para executar os exemplos de código.

Pode instalá-los executando o seguinte comando no terminal na raiz do repositório:

```bash
pip install -r requirements.txt
```
Recomendamos criar um ambiente virtual Python para evitar conflitos e problemas.

## Configurar VSCode
Certifique-se de que está a usar a versão correta do Python no VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configuração para Exemplos usando GitHub Models 

### Passo 1: Obter o Seu Token de Acesso Pessoal (PAT) do GitHub

Este curso utiliza o GitHub Models Marketplace, que oferece acesso gratuito a Modelos de Linguagem Grande (LLMs) que usará para construir Agentes de IA.

Para usar os GitHub Models, precisará criar um [Token de Acesso Pessoal do GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Isso pode ser feito indo às <a href="https://github.com/settings/personal-access-tokens" target="_blank">configurações de Tokens de Acesso Pessoal</a> na sua conta GitHub.

Por favor, siga o [Princípio do Menor Privilégio](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) ao criar o seu token. Isso significa que deve dar ao token apenas as permissões necessárias para executar os exemplos de código deste curso.

1. Selecione a opção `Fine-grained tokens` no lado esquerdo do ecrã, navegando até **Developer settings**.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.pt.png)

    Depois, selecione `Generate new token`.

    ![Gerar Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.pt.png)

2. Insira um nome descritivo para o seu token que reflita o seu propósito, facilitando a identificação posteriormente.


    🔐 Recomendação de Duração do Token

    Duração recomendada: 30 dias  
    Para uma postura mais segura, pode optar por um período mais curto—como 7 dias 🛡️  
    É uma ótima forma de definir um objetivo pessoal e concluir o curso enquanto mantém o ritmo de aprendizagem 🚀.

    ![Nome e Expiração do Token](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.pt.png)

3. Limite o escopo do token ao seu fork deste repositório.

    ![Limitar escopo ao repositório forkado](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.pt.png)

4. Restrinja as permissões do token: Em **Permissions**, clique na aba **Account** e no botão "+ Add permissions". Aparecerá um menu suspenso. Procure por **Models** e marque a caixa correspondente.
    ![Adicionar Permissão de Models](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.pt.png)

5. Verifique as permissões necessárias antes de gerar o token. ![Verificar Permissões](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.pt.png)

6. Antes de gerar o token, certifique-se de que está pronto para armazená-lo num local seguro, como um cofre de gestor de senhas, pois ele não será exibido novamente após a sua criação. ![Armazenar Token com Segurança](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.pt.png)

Copie o novo token que acabou de criar. Agora, adicione-o ao ficheiro `.env` incluído neste curso.


### Passo 2: Criar o Seu Ficheiro `.env`

Para criar o seu ficheiro `.env`, execute o seguinte comando no terminal.

```bash
cp .env.example .env
```

Isso copiará o ficheiro de exemplo e criará um `.env` no seu diretório, onde preencherá os valores das variáveis de ambiente.

Com o seu token copiado, abra o ficheiro `.env` no seu editor de texto favorito e cole o seu token no campo `GITHUB_TOKEN`.
![Campo do Token do GitHub](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.pt.png)


Agora deverá conseguir executar os exemplos de código deste curso.

## Configuração para Exemplos usando Azure AI Foundry e Azure AI Agent Service

### Passo 1: Obter o Endpoint do Seu Projeto Azure


Siga os passos para criar um hub e projeto no Azure AI Foundry aqui: [Visão geral dos recursos do Hub](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)


Depois de criar o seu projeto, precisará obter a string de conexão para o seu projeto.

Isso pode ser feito indo à página **Overview** do seu projeto no portal Azure AI Foundry.

![String de Conexão do Projeto](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.pt.png)

### Passo 2: Criar o Seu Ficheiro `.env`

Para criar o seu ficheiro `.env`, execute o seguinte comando no terminal.

```bash
cp .env.example .env
```

Isso copiará o ficheiro de exemplo e criará um `.env` no seu diretório, onde preencherá os valores das variáveis de ambiente.

Com o seu token copiado, abra o ficheiro `.env` no seu editor de texto favorito e cole o seu token no campo `PROJECT_ENDPOINT`.

### Passo 3: Iniciar Sessão no Azure

Como uma prática de segurança, usaremos [autenticação sem chave](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) para autenticar no Azure OpenAI com Microsoft Entra ID. 

Em seguida, abra um terminal e execute `az login --use-device-code` para iniciar sessão na sua conta Azure.

Depois de iniciar sessão, selecione a sua subscrição no terminal.


## Variáveis de Ambiente Adicionais - Azure Search e Azure OpenAI 

Para a lição Agentic RAG - Lição 5 - há exemplos que utilizam Azure Search e Azure OpenAI.

Se quiser executar esses exemplos, precisará adicionar as seguintes variáveis de ambiente ao seu ficheiro `.env`:

### Página de Visão Geral (Projeto)

- `AZURE_SUBSCRIPTION_ID` - Verifique **Project details** na página **Overview** do seu projeto.

- `AZURE_AI_PROJECT_NAME` - Veja no topo da página **Overview** do seu projeto.

- `AZURE_OPENAI_SERVICE` - Encontre isto na aba **Included capabilities** para **Azure OpenAI Service** na página **Overview**.

### Centro de Gestão

- `AZURE_OPENAI_RESOURCE_GROUP` - Vá para **Project properties** na página **Overview** do **Management Center**.

- `GLOBAL_LLM_SERVICE` - Em **Connected resources**, encontre o nome da conexão **Azure AI Services**. Se não estiver listado, verifique o **portal Azure** no seu grupo de recursos para o nome do recurso AI Services.

### Página de Modelos + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Selecione o seu modelo de embedding (por exemplo, `text-embedding-ada-002`) e anote o **Deployment name** nos detalhes do modelo.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Selecione o seu modelo de chat (por exemplo, `gpt-4o-mini`) e anote o **Deployment name** nos detalhes do modelo.

### Portal Azure

- `AZURE_OPENAI_ENDPOINT` - Procure por **Azure AI services**, clique nele, depois vá para **Resource Management**, **Keys and Endpoint**, desça até "Azure OpenAI endpoints" e copie o que diz "Language APIs".

- `AZURE_OPENAI_API_KEY` - Na mesma página, copie a CHAVE 1 ou CHAVE 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Encontre o recurso **Azure AI Search**, clique nele e veja **Overview**.

- `AZURE_SEARCH_API_KEY` - Depois vá para **Settings** e depois **Keys** para copiar a chave de administrador primária ou secundária.

### Página Externa

- `AZURE_OPENAI_API_VERSION` - Visite a página [ciclo de vida da versão da API](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) em **Latest GA API release**.

### Configurar autenticação sem chave

Em vez de codificar as suas credenciais, usaremos uma conexão sem chave com o Azure OpenAI. Para isso, importaremos `DefaultAzureCredential` e, posteriormente, chamaremos a função `DefaultAzureCredential` para obter a credencial.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Está com dificuldades?
Se tiver algum problema ao executar esta configuração, entre no nosso <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord da Comunidade Azure AI</a> ou <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">crie um problema</a>.

## Próxima Aula

Agora está pronto para executar o código deste curso. Boa aprendizagem sobre o mundo dos Agentes de IA!

[Introdução aos Agentes de IA e Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.