<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c729f7442eb5afd55b5522e3ad65c822",
  "translation_date": "2025-06-05T14:52:35+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "de"
}
-->
Sie sollten nun Ihre eigene geforkte Version dieses Kurses unter folgendem Link haben:

![Forked Repo](../../../00-course-setup/images/forked-repo.png)

## Ausführen des Codes

Dieser Kurs bietet eine Reihe von Jupyter Notebooks, die Sie ausführen können, um praktische Erfahrungen im Aufbau von KI-Agenten zu sammeln.

Die Codebeispiele verwenden entweder:

**Erfordert GitHub-Konto – Kostenlos**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Bezeichnet als (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Bezeichnet als (autogen.ipynb)

**Erfordert Azure-Abonnement**:
3) Azure AI Foundry + Azure AI Agent Service. Bezeichnet als (azureaiagent.ipynb)

Wir empfehlen, alle drei Beispieltypen auszuprobieren, um herauszufinden, welcher für Sie am besten funktioniert.

Welche Option Sie auch wählen, sie bestimmt, welche Einrichtungsschritte Sie unten befolgen müssen:

## Anforderungen

- Python 3.12+
- Ein GitHub-Konto – für den Zugriff auf den GitHub Models Marketplace
- Azure-Abonnement – für den Zugriff auf Azure AI Foundry
- Azure AI Foundry-Konto – für den Zugriff auf den Azure AI Agent Service

Wir haben eine `requirements.txt` Datei im Stammverzeichnis dieses Repositories eingefügt, die alle erforderlichen Python-Pakete enthält, um die Codebeispiele auszuführen.

Sie können diese installieren, indem Sie den folgenden Befehl in Ihrem Terminal im Stammverzeichnis des Repositories ausführen:

```bash
pip install -r requirements.txt
```

Wir empfehlen, eine Python-virtuelle Umgebung zu erstellen, um Konflikte und Probleme zu vermeiden.

## Einrichtung für Beispiele mit GitHub Models

### Schritt 1: Holen Sie sich Ihren GitHub Personal Access Token (PAT)

Derzeit verwendet dieser Kurs den GitHub Models Marketplace, um kostenlosen Zugriff auf Large Language Models (LLMs) zu bieten, die zur Erstellung von KI-Agenten verwendet werden.

Um auf diesen Dienst zuzugreifen, müssen Sie einen GitHub Personal Access Token erstellen.

Dies können Sie tun, indem Sie sich in Ihrem GitHub-Konto anmelden.

Wählen Sie die Option `Fine-grained tokens` option on the left side of your screen.

Then select `Generate new token`.

![Generate Token](../../../00-course-setup/images/generate-token.png)

You will be prompted to enter a name for your token, select the expiration date (Recommended: 30 Days), and select the scopes for your token (Public Repositories).

It's also necessary to edit the permissions of this token: Permissions -> Models -> Allows access to GitHub Models

Copy your new token that you have just created. You will now add this to your `.env` file included in this course. 


### Step 2: Create Your `.env` File

To create your `.env` Datei und führen Sie den folgenden Befehl in Ihrem Terminal aus.

```bash
cp .env.example .env
```

Dies kopiert die Beispieldatei und erstellt eine `.env` in your directory and where you fill in the values for the environment variables.

With your token copied, open the `.env` file in your favorite text editor and paste your token into the `GITHUB_TOKEN` field.

You should now be able to run the code samples of this course.

## Set Up for Samples using Azure AI Foundry and Azure AI Agent Service

### Step 1: Retrieve Your Azure Project Connection String


Follow the steps to creating a hub and project in Azure AI Foundry found here: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)


Once you have created your project, you will need to retrieve the connection string for your project.

This can be done by going to the **Overview** page of your project in the Azure AI Foundry portal.

![Project Connection String](../../../00-course-setup/images/project-connection-string.png)

### Step 2: Create Your `.env` File

To create your `.env` Datei. Führen Sie den folgenden Befehl in Ihrem Terminal aus.

```bash
cp .env.example .env
```

Dies kopiert die Beispieldatei und erstellt eine `.env` in your directory and where you fill in the values for the environment variables.

With your token copied, open the `.env` file in your favorite text editor and paste your token into the `PROJECT_CONNECTION_STRING` field.

### Step 3: Sign in to Azure

As a security best practice, we'll use [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) to authenticate to Azure OpenAI with Microsoft Entra ID. Before you can do so, you'll first need to install the **Azure CLI** per the [installation instructions](https://learn.microsoft.com/cli/azure/install-azure-cli?WT.mc_id=academic-105485-koreyst) for your operating system.

Next, open a terminal and run `az login --use-device-code` to sign in to your Azure account.

Once you've logged in, select your subscription in the terminal.


## Additional Environment Variables - Azure Search and Azure OpenAI 

For the Agentic RAG Lesson - Lesson 5 - there are samples that use Azure Search and Azure OpenAI.

If you want to run these samples, you will need to add the following environment variables to your `.env` file:

### Overview Page (Project)

- `AZURE_SUBSCRIPTION_ID` - Check **Project details** on the **Overview** page of your project.

- `AZURE_AI_PROJECT_NAME` - Look at the top of the **Overview** page for your project.

- `AZURE_OPENAI_SERVICE` - Find this in the **Included capabilities** tab for **Azure OpenAI Service** on the **Overview** page.

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - Go to **Project properties** on the **Overview** page of the **Management Center**.

- `GLOBAL_LLM_SERVICE` - Under **Connected resources**, find the **Azure AI Services** connection name. If not listed, check the **Azure portal** under your resource group for the AI Services resource name.

### Models + Endpoints Page

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Select your embedding model (e.g., `text-embedding-ada-002`) and note the **Deployment name** from the model details.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Select your chat model (e.g., `gpt-4o-mini`) and note the **Deployment name** from the model details.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - Look for **Azure AI services**, click on it, then go to **Resource Management**, **Keys and Endpoint**, scroll down to the "Azure OpenAI endpoints", and copy the one that says "Language APIs".

- `AZURE_OPENAI_API_KEY` - From the same screen, copy KEY 1 or KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Find your **Azure AI Search** resource, click it, and see **Overview**.

- `AZURE_SEARCH_API_KEY` - Then go to **Settings** and then **Keys** to copy the primary or secondary admin key.

### External Webpage

- `AZURE_OPENAI_API_VERSION` - Visit the [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) page under **Latest GA API release**.

### Setup keyless authentication

Rather than hardcode your credentials, we'll use a keyless connection with Azure OpenAI. To do so, we'll import `DefaultAzureCredential` and later call the `DefaultAzureCredential` Funktion, um die Anmeldeinformationen zu erhalten.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Hängen geblieben?

Wenn Sie Probleme bei der Einrichtung haben, treten Sie gerne unserer

oder

Gruppe bei.

## Nächste Lektion

Sie sind jetzt bereit, den Code für diesen Kurs auszuführen. Viel Spaß beim weiteren Lernen über die Welt der KI-Agenten!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.