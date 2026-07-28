# Kurseinrichtung

## Einführung

Diese Lektion behandelt, wie Sie die Codebeispiele dieses Kurses ausführen.

## Tritt anderen Lernenden bei und erhalte Hilfe

Bevor Sie Ihr Repository klonen, treten Sie dem [AI Agents For Beginners Discord-Kanal](https://aka.ms/ai-agents/discord) bei, um Hilfe beim Setup zu erhalten, Fragen zum Kurs zu stellen oder sich mit anderen Lernenden zu vernetzen.

## Klonen oder Forken Sie dieses Repository

Beginnen Sie bitte damit, das GitHub-Repository zu klonen oder zu forken. So erhalten Sie Ihre eigene Version des Kursmaterials, mit der Sie den Code ausführen, testen und anpassen können!

Dies können Sie tun, indem Sie auf den Link <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">Fork des Repos</a> klicken.

Sie sollten nun Ihre eigene geforkte Version dieses Kurses unter folgendem Link haben:

![Geforktes Repo](../../../translated_images/de/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (empfohlen für Workshop / Codespaces)

  >Das vollständige Repository kann groß sein (~3 GB), wenn Sie die gesamte Historie und alle Dateien herunterladen. Wenn Sie nur am Workshop teilnehmen oder nur einige Lektionen benötigen, vermeidet ein Shallow Clone (oder Sparse Clone) den Großteil dieses Downloads, indem die Historie abgeschnitten und/oder Blobs übersprungen werden.

#### Schneller Shallow Clone — minimale Historie, alle Dateien

Ersetzen Sie `<your-username>` in den folgenden Befehlen mit der URL Ihres Forks (oder der Upstream-URL, falls bevorzugt).

Um nur die neueste Commit-Historie zu klonen (kleiner Download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Um einen bestimmten Branch zu klonen:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partieller (sparsamer) Clone — minimale Blobs + nur ausgewählte Ordner

Dies nutzt Partial Clone und Sparse-Checkout (erfordert Git 2.25+ und empfohlen moderne Git-Version mit Partial Clone Unterstützung):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Gehen Sie in den Repo-Ordner:

```bash|powershell
cd ai-agents-for-beginners
```

Dann geben Sie an, welche Ordner Sie möchten (das Beispiel unten zeigt zwei Ordner):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Nach dem Klonen und Verifizieren der Dateien, wenn Sie nur die Dateien brauchen und Speicherplatz freigeben möchten (keine Git-Historie), löschen Sie bitte die Repository-Metadaten (💀irreversibel — Sie verlieren alle Git-Funktionalitäten: keine Commits, Pulls, Pushes oder Zugriff auf die Historie).

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

- Führen Sie im Terminal des neu erstellten Codespace einen der oben genannten shallow/sparse clone Befehle aus, um nur die benötigten Lektionenordner in den Codespace-Arbeitsbereich zu bringen.
- Optional: Entfernen Sie nach dem Klonen in Codespaces .git, um zusätzlichen Speicherplatz zurückzugewinnen (siehe oben genannte Löschbefehle).
- Hinweis: Wenn Sie das Repo direkt in Codespaces öffnen möchten (ohne extra Klonen), beachten Sie, dass Codespaces die devcontainer-Umgebung aufbaut und dennoch mehr bereitstellen kann, als Sie brauchen. Das Klonen einer Shallow-Kopie in einem frischen Codespace gibt Ihnen mehr Kontrolle über die Speicherausnutzung.

#### Tipps

- Ersetzen Sie immer die Klon-URL durch Ihren Fork, wenn Sie bearbeiten oder committen möchten.
- Falls Sie später mehr Historie oder Dateien benötigen, können Sie diese abrufen oder das Sparse-Checkout anpassen, um zusätzliche Ordner einzubeziehen.

## Code Ausführen

Dieser Kurs bietet eine Reihe von Jupyter Notebooks, die Sie ausführen können, um praktische Erfahrung beim Erstellen von KI-Agenten zu sammeln.

Die Codebeispiele nutzen **Microsoft Agent Framework (MAF)** mit dem `FoundryChatClient`, der sich mit dem **Microsoft Foundry Agent Service V2** (der Responses API) über **Microsoft Foundry** verbindet.

Alle Python-Notebooks sind mit `*-python-agent-framework.ipynb` gekennzeichnet.

## Voraussetzungen

- Python 3.12+
  - **HINWEIS**: Wenn Sie Python3.12 nicht installiert haben, stellen Sie sicher, dass Sie es installieren. Erstellen Sie dann Ihr venv mit python3.12, um sicherzustellen, dass die richtigen Versionen aus der requirements.txt installiert werden.
  
    >Beispiel

    Erstellen des Python venv Verzeichnisses:

    ```bash|powershell
    python -m venv venv
    ```

    Dann aktivieren Sie die venv-Umgebung für:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Für die Beispielcodes mit .NET stellen Sie sicher, dass Sie das [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) oder neuer installiert haben. Prüfen Sie dann Ihre installierte .NET SDK-Version:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Erforderlich für die Authentifizierung. Installation unter [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure-Abonnement** — Für den Zugriff auf Microsoft Foundry und Microsoft Foundry Agent Service.
- **Microsoft Foundry Projekt** — Ein Projekt mit einem eingesetzten Modell (z.B. `gpt-5-mini`). Siehe [Schritt 1](#schritt-1-erstellen-sie-ein-microsoft-foundry-projekt) unten.

Wir haben eine `requirements.txt`-Datei im Root dieses Repositories beigefügt, die alle erforderlichen Python-Pakete enthält, um die Codebeispiele auszuführen.

Sie können diese installieren, indem Sie den folgenden Befehl im Terminal im Root-Verzeichnis des Repositories ausführen:

```bash|powershell
pip install -r requirements.txt
```

Wir empfehlen, eine Python-virtuelle Umgebung zu erstellen, um Konflikte und Probleme zu vermeiden.

## VSCode Einrichten

Stellen Sie sicher, dass Sie in VSCode die richtige Python-Version verwenden.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry und Microsoft Foundry Agent Service Einrichten

### Schritt 1: Erstellen Sie ein Microsoft Foundry Projekt

Sie benötigen einen Microsoft Foundry **Hub** und ein **Projekt** mit einem bereitgestellten Modell, um die Notebooks auszuführen.

1. Gehen Sie zu [ai.azure.com](https://ai.azure.com) und melden Sie sich mit Ihrem Azure-Konto an.
2. Erstellen Sie einen **Hub** (oder verwenden Sie einen vorhandenen). Siehe: [Hub-Ressourcenübersicht](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Erstellen Sie im Hub ein **Projekt**.
4. Stellen Sie ein Modell bereit (z.B. `gpt-5-mini`) über **Models + Endpoints** → **Deploy model**.

### Schritt 2: Abrufen Ihres Projekt-Endpunkts und des Modell-Bereitstellungsnamens

Im Microsoft Foundry Portal zu Ihrem Projekt:

- **Projekt-Endpunkt** — Gehen Sie zur **Übersichtsseite** und kopieren Sie die Endpunkt-URL.

![Projekt Verbindungsstring](../../../translated_images/de/project-endpoint.8cf04c9975bbfbf1.webp)

- **Modell-Bereitstellungsname** — Gehen Sie zu **Models + Endpoints**, wählen Sie Ihr bereitgestelltes Modell und notieren Sie den **Bereitstellungsnamen** (z.B. `gpt-5-mini`).

### Schritt 3: Melden Sie sich mit `az login` bei Azure an

Alle Notebooks verwenden **`AzureCliCredential`** für die Authentifizierung — es müssen keine API-Schlüssel verwaltet werden. Dies setzt voraus, dass Sie via Azure CLI angemeldet sind.

1. **Installieren Sie die Azure CLI**, falls noch nicht geschehen: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Melden Sie sich an**, indem Sie Folgendes ausführen:

    ```bash|powershell
    az login
    ```

    Oder wenn Sie in einer Remote-/Codespace-Umgebung ohne Browser sind:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Wählen Sie Ihr Abonnement aus**, falls dazu aufgefordert — wählen Sie das Abonnement, welches Ihr Foundry-Projekt enthält.

4. **Überprüfen Sie**, dass Sie angemeldet sind:

    ```bash|powershell
    az account show
    ```

> **Warum `az login`?** Die Notebooks authentifizieren sich mit `AzureCliCredential` aus dem `azure-identity` Paket. Das bedeutet, dass Ihre Azure CLI-Sitzung die Anmeldeinformationen bereitstellt — keine API-Schlüssel oder Geheimnisse in Ihrer `.env`-Datei. Dies ist eine [Sicherheits-Best-Practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Schritt 4: Erstellen Sie Ihre `.env`-Datei

Kopieren Sie die Beispiel-Datei:

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

Das war's für die meisten Lektionen! Die Notebooks authentifizieren sich automatisch über Ihre `az login`-Sitzung.

### Schritt 5: Installieren Sie Python-Abhängigkeiten

```bash|powershell
pip install -r requirements.txt
```

Wir empfehlen, dies in der zuvor erstellten virtuellen Umgebung auszuführen.

## Zusätzliche Einrichtung für Lektion 5 (Agentic RAG)

Lektion 5 verwendet **Azure AI Search** für retrieval-augmented generation. Wenn Sie diese Lektion ausführen möchten, fügen Sie diese Variablen Ihrer `.env`-Datei hinzu:

| Variable | Wo zu finden |
|----------|--------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-Portal → Ihre **Azure AI Search** Ressource → **Übersicht** → URL |
| `AZURE_SEARCH_API_KEY` | Azure-Portal → Ihre **Azure AI Search** Ressource → **Einstellungen** → **Schlüssel** → primärer Administratorschlüssel |

## Zusätzliche Einrichtung für Lektionen, die Azure OpenAI direkt aufrufen (Lektionen 6 und 8)

Einige Notebooks in Lektionen 6 und 8 rufen **Azure OpenAI** direkt auf (unter Verwendung der **Responses API**) statt über ein Microsoft Foundry Projekt. Diese Beispiele nutzten zuvor GitHub-Modelle, die veraltet sind (Einstellung Juli 2026) und die Responses API nicht unterstützen. Wenn Sie diese Beispiele ausführen möchten, fügen Sie diese Variablen Ihrer `.env`-Datei hinzu:

| Variable | Wo zu finden |
|----------|--------------|
| `AZURE_OPENAI_ENDPOINT` | Azure-Portal → Ihre **Azure OpenAI** Ressource → **Schlüssel und Endpunkt** → Endpunkt (z.B. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Name Ihres bereitgestellten Modells (z.B. `gpt-5-mini`), das die Responses API unterstützt |
| `AZURE_OPENAI_API_KEY` | Optional — nur bei Schlüssel-basierter Authentifizierung statt `az login` / Entra ID |

> Die Responses API verwendet den stabilen `/openai/v1/` Endpunkt, daher ist keine `api-version` erforderlich. Melden Sie sich mit `az login` an, um eine schlüssel-lose Entra ID Authentifizierung zu nutzen.

## Alternativer Anbieter: MiniMax (OpenAI-kompatibel)

[MiniMax](https://platform.minimaxi.com/) bietet large-context Modelle (bis zu 204K Tokens) über eine OpenAI-kompatible API an. Da der `OpenAIChatClient` des Microsoft Agent Frameworks mit jedem OpenAI-kompatiblen Endpunkt funktioniert, können Sie MiniMax als Drop-in-Alternative zu Azure OpenAI oder OpenAI verwenden.

Fügen Sie diese Variablen Ihrer `.env`-Datei hinzu:

| Variable | Wo zu finden |
|----------|--------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API-Schlüssel |
| `MINIMAX_BASE_URL` | Verwenden Sie `https://api.minimax.io/v1` (Standardwert) |
| `MINIMAX_MODEL_ID` | Modellname zur Nutzung (z.B. `MiniMax-M3`) |

**Beispielmodelle**: `MiniMax-M3` (empfohlen), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (schnellere Antworten). Modellnamen und Verfügbarkeit können sich im Laufe der Zeit ändern, und der Zugriff auf ein bestimmtes Modell kann von Ihrem Konto oder Ihrer Region abhängen — prüfen Sie die [MiniMax Platform](https://platform.minimaxi.com/) für die aktuelle Liste. Falls `MiniMax-M3` für Ihr Konto nicht verfügbar ist, setzen Sie `MINIMAX_MODEL_ID` auf ein Modell, auf das Sie Zugriff haben (z.B. `MiniMax-M2.7`).

Die Codebeispiele, die `OpenAIChatClient` nutzen (z.B. Lektion 14: Hotelbuchungs-Workflow), erkennen Ihre MiniMax-Konfiguration automatisch und verwenden sie, wenn `MINIMAX_API_KEY` gesetzt ist.

## Alternativer Anbieter: Foundry Local (Modelle lokal ausführen)

[Foundry Local](https://foundrylocal.ai) ist eine leichtgewichtige Laufzeitumgebung, die Sprachmodelle **vollständig auf Ihrem eigenen Rechner** herunterlädt, verwaltet und über eine OpenAI-kompatible API bereitstellt — keine Cloud, kein Azure-Abonnement und keine API-Schlüssel nötig. Es ist eine großartige Option für Offline-Entwicklung, Experimente ohne Cloud-Kosten oder wenn Daten lokal bleiben sollen.

Da der `OpenAIChatClient` des Microsoft Agent Frameworks mit jedem OpenAI-kompatiblen Endpunkt funktioniert, ist Foundry Local eine lokal einsetzbare Alternative zu Azure OpenAI.

**1. Foundry Local installieren**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Ein Modell herunterladen und starten** (dies startet auch den lokalen Service):

```bash
foundry model list          # verfügbare Modelle ansehen
foundry model run phi-4-mini
```

**3. Das Python SDK installieren**, mit dem der lokale Endpunkt entdeckt wird:

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework auf Ihr lokales Modell verweisen:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Lädt das Modell herunter (falls benötigt) und dient es lokal, anschließend wird der Endpunkt/Port ermittelt.
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

> **Hinweis:** Foundry Local stellt einen OpenAI-kompatiblen **Chat Completions** Endpunkt bereit. Verwenden Sie ihn für lokale Entwicklung und Offline-Szenarien. Für den vollen Funktionsumfang der **Responses API** (zustandsvolle Gespräche, tiefgreifende Tool-Orchestrierung und agentenartige Entwicklung) verwenden Sie **Azure OpenAI** oder ein **Microsoft Foundry** Projekt wie in den Lektionen gezeigt. Siehe die [Foundry Local Dokumentation](https://foundrylocal.ai) für den aktuellen Modellkatalog und Plattformunterstützung.

## Zusätzliche Einrichtung für Lektion 8 (Bing Grounding Workflow)


Das bedingte Workflow-Notizbuch in Lektion 8 verwendet **Bing Grounding** über Microsoft Foundry. Wenn Sie dieses Beispiel ausführen möchten, fügen Sie diese Variable zu Ihrer `.env`-Datei hinzu:

| Variable | Wo zu finden |
|----------|--------------|
| `BING_CONNECTION_ID` | Microsoft Foundry-Portal → Ihr Projekt → **Verwaltung** → **Verbundene Ressourcen** → Ihre Bing-Verbindung → kopieren Sie die Verbindungs-ID |

## Fehlerbehebung

### SSL-Zertifikatüberprüfungsfehler auf macOS

Wenn Sie macOS verwenden und einen Fehler wie diesen erhalten:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dies ist ein bekanntes Problem bei Python auf macOS, bei dem die System-SSL-Zertifikate nicht automatisch vertraut werden. Versuchen Sie die folgenden Lösungen der Reihe nach:

**Option 1: Führen Sie das Install Certificates-Skript von Python aus (empfohlen)**

```bash
# Ersetzen Sie 3.XX durch Ihre installierte Python-Version (z.B. 3.12 oder 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Option 2: Verwenden Sie `connection_verify=False` in Ihrem Notizbuch (nur für GitHub Models-Notizbücher)**

Im Notizbuch der Lektion 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) ist bereits eine auskommentierte Problemumgehung enthalten. Entfernen Sie das Kommentarzeichen bei `connection_verify=False`, wenn Sie den Client erstellen:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deaktivieren Sie die SSL-Überprüfung, wenn Sie Zertifikatsfehler erhalten
)
```

> **⚠️ Warnung:** Das Deaktivieren der SSL-Überprüfung (`connection_verify=False`) verringert die Sicherheit, da die Zertifikatsvalidierung übersprungen wird. Verwenden Sie dies nur als temporäre Problemumgehung in Entwicklungsumgebungen, niemals in der Produktion.

**Option 3: Installieren und verwenden Sie `truststore`**

```bash
pip install truststore
```

Fügen Sie dann Folgendes ganz oben in Ihr Notizbuch oder Skript ein, bevor Sie Netzwerkanfragen stellen:

```python
import truststore
truststore.inject_into_ssl()
```

## Sind Sie irgendwo hängen geblieben?

Wenn Sie Probleme bei der Einrichtung haben, kommen Sie in unseren <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> oder <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">erstellen Sie ein Issue</a>.

## Nächste Lektion

Sie sind nun bereit, den Code für diesen Kurs auszuführen. Viel Erfolg beim weiteren Lernen über die Welt der KI-Agenten!

[Einführung in KI-Agenten und Anwendungsfälle für Agenten](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->