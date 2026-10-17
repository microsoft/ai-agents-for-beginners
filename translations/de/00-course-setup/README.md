# Kurseinrichtung

## Einführung

Diese Lektion behandelt, wie Sie die Codebeispiele dieses Kurses ausführen.

## Treten Sie anderen Lernenden bei und erhalten Sie Hilfe

Bevor Sie Ihr Repository klonen, treten Sie dem [AI Agents For Beginners Discord-Kanal](https://aka.ms/ai-agents/discord) bei, um Hilfe bei der Einrichtung zu erhalten, Fragen zum Kurs zu stellen oder sich mit anderen Lernenden zu vernetzen.

## Klonen oder Forken Sie dieses Repo

Um zu beginnen, klonen oder forken Sie bitte das GitHub-Repository. Dadurch erhalten Sie Ihre eigene Version des Kursmaterials, damit Sie den Code ausführen, testen und anpassen können!

Dies können Sie tun, indem Sie auf den Link klicken, um <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">das Repo zu forken</a>.

Sie sollten nun Ihre eigene geforkte Version dieses Kurses unter folgendem Link haben:

![Geforktes Repo](../../../translated_images/de/forked-repo.33f27ca1901baa6a.webp)

### Flaches Klonen (empfohlen für Workshop / Codespaces)

  > Das vollständige Repository kann groß sein (~3 GB), wenn Sie die gesamte Historie und alle Dateien herunterladen. Wenn Sie nur am Workshop teilnehmen oder nur einige Lektion-Ordner benötigen, lädt ein flaches Klonen (oder ein sparse clone) wesentlich weniger herunter.

#### Schnelles flaches Klonen — minimale Historie, alle Dateien

Ersetzen Sie `<your-username>` in den folgenden Befehlen durch Ihre Fork-URL (oder die Upstream-URL, falls bevorzugt).

Um nur die letzte Commit-Historie zu klonen (kleiner Download):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Um einen bestimmten Branch zu klonen:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Teilweises (sparse) Klonen — minimale Blobs + nur ausgewählte Ordner

Dies verwendet Partial Clone und Sparse-Checkout (erfordert Git 2.25+ und empfohlen eine moderne Git-Version mit Partial Clone Unterstützung):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Wechseln Sie in den Repo-Ordner:

```bash
cd ai-agents-for-beginners
```

Geben Sie dann an, welche Ordner Sie möchten (Beispiel unten zeigt zwei Ordner):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Nach dem Klonen und der Überprüfung der Dateien: Wenn Sie nur die Dateien benötigen und Speicherplatz freigeben wollen (keine Git-Historie), löschen Sie bitte die Repository-Metadaten (💀 irreversibel — Sie verlieren alle Git-Funktionalität):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Verwendung von GitHub Codespaces (empfohlen, um lokale große Downloads zu vermeiden)

- Erstellen Sie einen neuen Codespace für dieses Repo über die [GitHub UI](https://github.com/codespaces).  

- Führen Sie im Terminal des neu erstellten Codespaces einen der oben genannten flachen/sparsamen Klon-Befehle aus, um nur die benötigten Lektion-Ordner in den Codespace-Arbeitsbereich zu laden.
- Optional: Entfernen Sie nach dem Klonen in Codespaces die .git, um zusätzlichen Speicher freizugeben (siehe oben die Löschbefehle).
- Hinweis: Wenn Sie das Repo direkt in Codespaces öffnen (ohne zusätzlichen Klon), beachten Sie, dass Codespaces die devcontainer-Umgebung erstellt und möglicherweise dennoch mehr bereitstellt, als Sie benötigen.

#### Tipps

- Ersetzen Sie immer die Klon-URL durch Ihre Fork, wenn Sie bearbeiten/committen möchten.
- Wenn Sie später mehr Historie oder Dateien benötigen, können Sie diese abrufen oder sparse-checkout anpassen, um zusätzliche Ordner einzuschließen.

## Ausführen des Codes

In diesem Kurs gibt es eine Reihe von Jupyter Notebooks, die Sie ausführen können, um praktische Erfahrungen beim Erstellen von KI-Agenten zu sammeln.

Die Codebeispiele verwenden das **Microsoft Agent Framework (MAF)** mit dem `FoundryChatClient`, der sich über **Microsoft Foundry** mit dem **Microsoft Foundry Agent Service V2** (der Responses API) verbindet.

Alle Python-Notebooks sind mit `*-python-agent-framework.ipynb` gekennzeichnet.

## Voraussetzungen

- Python 3.12+
  - **HINWEIS**: Falls Sie Python 3.12 nicht installiert haben, stellen Sie sicher, dass Sie es installieren. Erstellen Sie anschließend Ihr venv mit python3.12, um sicherzustellen, dass die korrekten Versionen aus der requirements.txt installiert werden.
  
    >Beispiel

    Erstellen des Python venv-Verzeichnisses:

    ```bash
    python -m venv venv
    ```

    Aktivieren Sie dann die venv-Umgebung für:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Für die Beispielcodes mit .NET stellen Sie sicher, dass Sie das [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) oder höher installiert haben. Prüfen Sie dann Ihre installierte .NET SDK-Version:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Erforderlich für die Authentifizierung. Installation unter [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure-Abonnement** — Für den Zugriff auf Microsoft Foundry und Microsoft Foundry Agent Service.
- **Microsoft Foundry Projekt** — Ein Projekt mit einem bereitgestellten Modell (z.B. `gpt-5-mini`). Siehe [Schritt 1](#schritt-1-erstellen-sie-ein-microsoft-foundry-projekt) unten.

Im Root dieses Repositories liegt eine `requirements.txt` Datei bei, die alle erforderlichen Python-Pakete zum Ausführen der Codebeispiele enthält.

Sie können diese installieren, indem Sie folgenden Befehl im Terminal im Root-Verzeichnis des Repositories ausführen:

```bash
pip install -r requirements.txt
```

Wir empfehlen, eine Python-virtuelle Umgebung zu erstellen, um Konflikte und Probleme zu vermeiden.

## VSCode einrichten

Stellen Sie sicher, dass Sie die richtige Python-Version in VSCode verwenden.

![Bild](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry und Microsoft Foundry Agent Service einrichten

### Schritt 1: Erstellen Sie ein Microsoft Foundry-Projekt

Sie benötigen einen Microsoft Foundry **Hub** und ein **Projekt** mit einem bereitgestellten Modell, um die Notebooks auszuführen.

1. Gehen Sie zu [ai.azure.com](https://ai.azure.com) und melden Sie sich mit Ihrem Azure-Konto an.
2. Erstellen Sie einen **Hub** (oder verwenden Sie einen bestehenden). Siehe: [Hub Ressourcenübersicht](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Erstellen Sie innerhalb des Hubs ein **Projekt**.
4. Stellen Sie ein Modell bereit (z.B. `gpt-5-mini`) unter **Models + Endpoints** → **Deploy model**.

### Schritt 2: Abrufen Ihres Projekt-Endpunkts und des Modell-Bereitstellungsnamens

Aus Ihrem Projekt im Microsoft Foundry-Portal:

- **Projekt-Endpunkt** — Gehen Sie zur **Übersichtsseite** und kopieren Sie die Endpunkt-URL.

![Projekt-Verbindungszeichenfolge](../../../translated_images/de/project-endpoint.8cf04c9975bbfbf1.webp)

- **Modell-Bereitstellungsname** — Gehen Sie zu **Models + Endpoints**, wählen Sie Ihr bereitgestelltes Modell aus, und notieren Sie den **Bereitstellungsnamen** (z.B. `gpt-5-mini`).

### Schritt 3: Anmeldung bei Azure mit `az login`

Die meisten Notebooks authentifizieren sich über Ihre **Azure CLI-Anmeldung** — mit `AzureCliCredential` oder `DefaultAzureCredential` (beide übernehmen Ihre `az login`-Sitzung) aus dem `azure-identity`-Paket — sodass keine API-Schlüssel erforderlich sind. Einige Lektionen und optionale Integrationen verwenden API-Schlüssel; prüfen Sie die Voraussetzungen jeder Lektion für zusätzliche Umgebungsvariablen. Dies erfordert, dass Sie mit der Azure CLI angemeldet sind.

1. **Installieren Sie die Azure CLI**, falls nicht bereits vorhanden: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Melden Sie sich an** mit:

    ```bash
    az login
    ```

    Oder falls Sie sich in einer Remote-/Codespace-Umgebung ohne Browser befinden:

    ```bash
    az login --use-device-code
    ```

3. **Wählen Sie Ihr Abonnement** aus, wenn Sie dazu aufgefordert werden — wählen Sie dasjenige, das Ihr Foundry-Projekt enthält.

4. **Überprüfen Sie** die Anmeldung:

    ```bash
    az account show
    ```

> **Warum `az login`?** Die Notebooks authentifizieren sich mit `AzureCliCredential` (oder `DefaultAzureCredential`, das ebenfalls Ihre Azure CLI-Anmeldung übernimmt) aus dem `azure-identity`-Paket. Das bedeutet, Ihre Azure CLI-Sitzung stellt die Anmeldedaten bereit — keine API-Schlüssel oder Geheimnisse in Ihrer `.env`-Datei. Dies ist eine [Sicherheitsbest Practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Schritt 4: Erstellen Sie Ihre `.env`-Datei

Kopieren Sie die Beispieldatei:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Öffnen Sie `.env` und füllen Sie diese beiden Werte aus:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variable | Wo zu finden |
|----------|--------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-Portal → Ihr Projekt → **Übersichtsseite** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-Portal → **Models + Endpoints** → Name Ihres bereitgestellten Modells |

Das war's für die meisten Lektionen! Die Notebooks authentifizieren automatisch über Ihre `az login`-Sitzung.

### Schritt 5: Installieren Sie Python-Abhängigkeiten

```bash
pip install -r requirements.txt
```

Wir empfehlen, dies innerhalb der zuvor erstellten virtuellen Umgebung auszuführen.

## Optionale Einrichtung: Azure AI Search (Lektionen 5 und 16)

Die Notebooks der Lektion 5 (Agentic RAG) und Lektion 16 laufen sofort mit einer **In-Memory-Wissensbasis** — es sind keine zusätzlichen Azure-Ressourcen erforderlich. Wenn Sie sie mit einem echten **Azure AI Search** Index absichern möchten, beachten Sie, dass das **Lektion 16 Notebook derzeit schlüsselbasierte Authentifizierung verwendet**: Es wechselt von In-Memory-Suche zu Azure AI Search nur, wenn **sowohl** `AZURE_SEARCH_SERVICE_ENDPOINT` **als auch** `AZURE_SEARCH_API_KEY` gesetzt sind, andernfalls bleibt es bei In-Memory-Suche — um es mit einem echten Index auszuführen, müssen Sie daher auch den Administratorschlüssel setzen. Schlüsselose Authentifizierung mit Microsoft Entra ID (RBAC) ist der empfohlene Ansatz für Ihren eigenen Produktionscode und entspricht dem `az login`-Flow, der überall sonst im Kurs verwendet wird.

Die RBAC-Schritte unten gelten für die Setup-Guide-Beispiele und Ihren eigenen Code. Sie aktivieren keine schlüssellose Authentifizierung im Lektion 16 Notebook; Lektion 16 benötigt weiterhin sowohl den Endpunkt als auch den Administratorschlüssel, um Azure AI Search zu verwenden.

1. **Aktivieren Sie rollenbasierte Zugriffe** auf Ihrem Suchdienst:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Weisen Sie sich die erforderlichen Rollen zu** (Indizes erstellen/laden und abfragen):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Fügen Sie den Endpunkt** Ihrer `.env`-Datei hinzu:

| Variable | Wo zu finden |
|----------|--------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-Portal → Ihre **Azure AI Search** Ressource → **Übersicht** → URL |
| `AZURE_SEARCH_API_KEY` | Erforderlich (zusammen mit dem Endpunkt) zur Aktivierung von Azure AI Search im Lektion 16 Notebook, welches schlüsselbasierte Authentifizierung verwendet. Azure-Portal → **Einstellungen** → **Schlüssel** → primärer Administratorschlüssel |

> **Warum schlüssellos?** Administratorschlüssel gewähren vollen Schreibzugriff auf Ihren Suchdienst und können über `.env`-Dateien auslaufen. Mit RBAC wird stattdessen Ihre `az login`-Identität genutzt — das gleiche schlüssellose Entra ID-Muster, das von den Kursnotebooks verwendet wird (über `AzureCliCredential` / `DefaultAzureCredential`). Siehe [Verbindung zu Azure AI Search mit Rollen](https://learn.microsoft.com/azure/search/search-security-rbac).

Siehe die [Azure AI Search-Einrichtungsanleitung](./AzureSearch.md) für vollständige Indexerstellungsbeispiele in Python und .NET.

## Zusätzliche Einrichtung für Lektionen, die Azure OpenAI direkt aufrufen (Lektionen 6 und 8)

Einige Notebooks in Lektionen 6 und 8 rufen **Azure OpenAI** direkt auf (mithilfe der **Responses API**), anstatt über ein Microsoft Foundry-Projekt zu gehen. Diese Beispiele nutzten zuvor GitHub Models, die veraltet sind und die Responses API nicht unterstützen. Fügen Sie diese Variablen Ihrer `.env`-Datei hinzu:

| Variable | Wo zu finden |
|----------|--------------|
| `AZURE_OPENAI_ENDPOINT` | Azure-Portal → Ihre **Azure OpenAI** Ressource → **Schlüssel und Endpunkt** → Endpunkt (z.B. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Name Ihres bereitgestellten Modells (z.B. `gpt-5-mini`), das die Responses API unterstützt |
| `AZURE_OPENAI_API_KEY` | Optional — nur wenn Sie schlüsselbasierte Authentifizierung statt `az login` / Entra ID verwenden |

> Die Responses API verwendet den stabilen `/openai/v1/` Endpunkt, daher ist keine `api-version` nötig. Melden Sie sich mit `az login` an, um schlüssellose Entra ID-Authentifizierung zu nutzen.

## Alternative Anbieter: MiniMax (OpenAI-kompatibel)

[MiniMax](https://platform.minimaxi.com/) bietet Modelle mit großem Kontext (bis zu 204K Tokens) über eine OpenAI-kompatible API an. Da der `OpenAIChatClient` des Microsoft Agent Framework mit jedem OpenAI-kompatiblen Endpunkt funktioniert, können Sie MiniMax als Drop-in-Alternative für Lektionen nutzen, die `OpenAIChatClient` verwenden.

Fügen Sie folgende Variablen Ihrer `.env`-Datei hinzu:

| Variable | Wo zu finden |
|----------|--------------|
| `MINIMAX_API_KEY` | [MiniMax Plattform](https://platform.minimaxi.com/) → API-Schlüssel |
| `MINIMAX_BASE_URL` | Verwenden Sie `https://api.minimax.io/v1` (Standardwert) |
| `MINIMAX_MODEL_ID` | Modellname zur Verwendung (z.B. `MiniMax-M3`) |

**Beispielmodelle**: `MiniMax-M3` (empfohlen), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (schnellere Antworten). Modellnamen und Verfügbarkeit können sich im Laufe der Zeit ändern, und der Zugang zu einem bestimmten Modell hängt von Ihrem Konto ab.

Die Codebeispiele, die `OpenAIChatClient` verwenden (z.B. Lektion 14 Hotelbuchungs-Workflow), erkennen Ihre MiniMax-Konfiguration automatisch und verwenden sie, wenn `MINIMAX_API_KEY` gesetzt ist.


## Alternativer Anbieter: Novita AI (OpenAI-kompatibel)

[Novita AI](https://novita.ai/llm-api) bietet eine OpenAI-kompatible API für Open-Source- und modernste LLMs (DeepSeek, Llama, Qwen und mehr). Da das Microsoft Agent Framework `OpenAIChatClient` mit jedem OpenAI-kompatiblen Endpunkt funktioniert, können Sie Novita AI als Drop-in-Alternative zu Azure OpenAI oder OpenAI verwenden.

Fügen Sie diese Variablen zu Ihrer `.env`-Datei hinzu:

| Variable | Wo zu finden |
|----------|--------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API-Schlüssel |
| `NOVITA_BASE_URL` | Verwenden Sie `https://api.novita.ai/openai/v1` (Standardwert) |
| `NOVITA_MODEL_ID` | Modellname zur Verwendung (z.B. `moonshotai/kimi-k3`) |

**Beispielmodelle**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI hostet auch viele andere Open-Source-Modellfamilien (Llama, Qwen, GLM und mehr) — prüfen Sie die [Novita AI Modellbibliothek](https://novita.ai/llm-api) für die aktuelle Liste verfügbarer Modelle und deren Modell-IDs.

Die aktuellen Beispiele verwenden `NOVITA_*` Variablen nicht automatisch. Um Novita AI zu nutzen, übergeben Sie diese Werte explizit beim Erstellen von `OpenAIChatClient` im Beispiel, das Sie ausführen.

## Alternativer Anbieter: Foundry Local (Modelle lokal ausführen)

[Foundry Local](https://foundrylocal.ai) ist eine leichtgewichtige Laufzeitumgebung, die Sprachmodelle **vollständig auf Ihrem eigenen Gerät** herunterlädt, verwaltet und über eine OpenAI-kompatible API bereitstellt — keine Cloud erforderlich.

Da das Microsoft Agent Framework `OpenAIChatClient` mit jedem OpenAI-kompatiblen Endpunkt funktioniert, ist Foundry Local eine lokale Drop-in-Alternative zu Azure OpenAI.

**1. Foundry Local installieren**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Laden Sie ein Modell herunter und starten Sie es** (dies startet auch den lokalen Dienst):

```bash
foundry model list          # verfügbare Modelle ansehen
foundry model run phi-4-mini
```

**3. Installieren Sie das Python SDK**, um den lokalen Endpunkt zu entdecken:

```bash
pip install foundry-local-sdk
```

**4. Weisen Sie das Microsoft Agent Framework auf Ihr lokales Modell:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Lädt das Modell (falls erforderlich) herunter und stellt es lokal bereit, dann wird der Endpunkt/Port ermittelt.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # z.B. http://localhost:<port>/v1
    api_key=manager.api_key,        # immer "nicht erforderlich" für Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Hinweis:** Foundry Local stellt einen OpenAI-kompatiblen **Chat Completions** Endpunkt bereit. Verwenden Sie diesen für lokale Entwicklung und Offline-Szenarien. Für den vollständigen Funktionsumfang der **Responses API** (statusbehaftete Unterhaltungen usw.) nutzen Sie Azure OpenAI oder ein Microsoft Foundry-Projekt.

## Zusätzliche Einrichtung für Lektion 8 (Bing Grounding Workflow)

Das bedingte Workflow-Notebook in Lektion 8 verwendet **Bing Grounding** über Microsoft Foundry. Wenn Sie dieses Beispiel ausführen möchten, fügen Sie diese Variable zu Ihrer `.env`-Datei hinzu:

| Variable | Wo zu finden |
|----------|--------------|
| `BING_CONNECTION_ID` | Microsoft Foundry Portal → Ihr Projekt → **Management** → **Verbundene Ressourcen** → Ihre Bing-Verbindung → kopieren Sie die Verbindungs-ID |

## Fehlerbehebung

### SSL-Zertifikatüberprüfungsfehler auf macOS

Wenn Sie macOS verwenden und auf einen Fehler wie diesen stoßen:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dies ist ein bekanntes Problem bei Python auf macOS, bei dem die System-SSL-Zertifikate nicht automatisch als vertrauenswürdig eingestuft werden. Versuchen Sie die folgenden Lösungen der Reihe nach:

**Option 1: Führen Sie das Install-Certificates-Skript von Python aus (empfohlen)**

```bash
# Ersetzen Sie 3.XX durch Ihre installierte Python-Version (z. B. 3.12 oder 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Option 2: Verwenden Sie `connection_verify=False` in Ihrem Notebook (nur für GitHub Models Notebooks)**

Im Notebook der Lektion 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) ist bereits eine auskommentierte Workaround-Lösung enthalten. Kommentieren Sie `connection_verify=False` ein, wenn Sie Zertifikatsfehler erhalten:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deaktivieren Sie die SSL-Überprüfung, wenn Sie Zertifikatsfehler erhalten
)
```

> **⚠️ Warnung:** Das Deaktivieren der SSL-Verifikation (`connection_verify=False`) verringert die Sicherheit, da die Zertifikatsprüfung übersprungen wird. Nutzen Sie dies nur als temporären Workaround in Entwicklungsumgebungen. Verwenden Sie es niemals in der Produktion.

**Option 3: Installieren und verwenden Sie `truststore`**

```bash
pip install truststore
```

Fügen Sie dann Folgendes am Anfang Ihres Notebooks oder Skripts hinzu, bevor Sie Netzwerkanfragen stellen:

```python
import truststore
truststore.inject_into_ssl()
```

## Stecken geblieben?

Wenn Sie Probleme bei der Einrichtung haben, treten Sie unserem <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> bei oder <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">eröffnen Sie ein Issue</a>.

## Nächste Lektion

Sie sind jetzt bereit, den Code für diesen Kurs auszuführen. Viel Freude beim weiteren Lernen der Welt der KI-Agenten!

[Einführung in KI-Agenten und Anwendungsfälle von Agenten](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->