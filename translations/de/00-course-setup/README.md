# Kurs-Einrichtung

## Einführung

Diese Lektion behandelt, wie man die Codebeispiele dieses Kurses ausführt.

## Tritt anderen Lernenden bei und erhalte Hilfe

Bevor du dein Repository klonst, tritt dem [AI Agents For Beginners Discord-Kanal](https://aka.ms/ai-agents/discord) bei, um Hilfe bei der Einrichtung zu erhalten, Fragen zum Kurs zu stellen oder um dich mit anderen Lernenden zu vernetzen.

## Klone oder Forke dieses Repository

Um zu beginnen, klone oder forke bitte das GitHub-Repository. So erhältst du deine eigene Version des Kursmaterials, um den Code auszuführen, zu testen und anzupassen!

Dies kannst du tun, indem du auf den Link <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a> klickst.

Du solltest nun deine eigene geforkte Version dieses Kurses unter folgendem Link haben:

![Geforktes Repo](../../../translated_images/de/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (empfohlen für Workshop / Codespaces)

  >Das vollständige Repository kann groß sein (~3 GB), wenn du die komplette Historie und alle Dateien herunterlädst. Wenn du nur am Workshop teilnimmst oder nur wenige Lektion-Ordner benötigst, vermeidet ein Shallow Clone (oder ein Sparse Clone) die meisten Downloads, indem die Historie gekürzt und/oder Blobs übersprungen werden.

#### Schneller Shallow Clone — minimale Historie, alle Dateien

Ersetze `<your-username>` in den folgenden Befehlen durch deine Fork-URL (oder die Upstream-URL, wenn du bevorzugst).

Um nur die neuesten Commit-Historie zu klonen (kleiner Download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Um einen bestimmten Branch zu klonen:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partieller (sparse) Clone — minimale Blobs + nur ausgewählte Ordner

Dies verwendet partial clone und sparse-checkout (erfordert Git 2.25+ und empfohlen wird modernes Git mit partial clone-Unterstützung):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Wechsle in den Repo-Ordner:

```bash|powershell
cd ai-agents-for-beginners
```

Dann gib an, welche Ordner du möchtest (Beispiel zeigt zwei Ordner):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Nach dem Klonen und Überprüfen der Dateien, wenn du nur Dateien brauchst und Speicherplatz freigeben möchtest (keine Git-Historie), lösche bitte die Repository-Metadaten (💀irreversibel – du verlierst alle Git-Funktionalitäten: keine Commits, Pulls, Pushes oder Historienzugriff).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Verwendung von GitHub Codespaces (empfohlen, um große lokale Downloads zu vermeiden)

- Erstelle einen neuen Codespace für dieses Repository über die [GitHub UI](https://github.com/codespaces).  

- Führe im Terminal des neu erstellten Codespace einen der oben genannten shallow/sparse clone Befehle aus, um nur die benötigten Lektion-Ordner in den Codespace-Arbeitsbereich zu holen.
- Optional: Nach dem Klonen in Codespaces entferne .git, um zusätzlichen Speicherplatz zurückzugewinnen (siehe oben angegebene Entfernen-Befehle).
- Hinweis: Wenn du das Repository direkt in Codespaces öffnen möchtest (ohne zusätzlichen Clone), bedenke, dass Codespaces die Devcontainer-Umgebung erstellt und möglicherweise mehr bereitstellt, als du brauchst. Ein Shallow Clone in einem frischen Codespace gibt dir mehr Kontrolle über die Festplattennutzung.

#### Tipps

- Ersetze immer die Clone-URL mit deinem Fork, wenn du bearbeiten/committen möchtest.
- Wenn du später mehr Historie oder Dateien brauchst, kannst du sie abrufen oder sparse-checkout anpassen, um weitere Ordner einzuschließen.

## Code ausführen

Dieser Kurs bietet eine Reihe von Jupyter Notebooks, die du ausführen kannst, um praktische Erfahrungen beim Erstellen von KI-Agenten zu sammeln.

Die Codebeispiele nutzen **Microsoft Agent Framework (MAF)** mit dem `FoundryChatClient`, welcher eine Verbindung zum **Microsoft Foundry Agent Service V2** (der Responses API) über **Microsoft Foundry** herstellt.

Alle Python-Notebooks sind mit `*-python-agent-framework.ipynb` gekennzeichnet.

## Voraussetzungen

- Python 3.12+
  - **HINWEIS**: Wenn du Python3.12 nicht installiert hast, solltest du es installieren. Erstelle dann deine virtuelle Umgebung mit python3.12, um sicherzustellen, dass die korrekten Versionen aus der requirements.txt installiert werden.
  
    >Beispiel

    Erstelle das Python venv-Verzeichnis:

    ```bash|powershell
    python -m venv venv
    ```

    Aktiviere dann die venv-Umgebung für:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Für den Beispielcode mit .NET stelle sicher, dass du das [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) oder neuer installierst. Prüfe dann deine installierte .NET SDK Version:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Wird für die Authentifizierung benötigt. Installiere es unter [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure-Abonnement** — Für den Zugriff auf Microsoft Foundry und Microsoft Foundry Agent Service.
- **Microsoft Foundry Projekt** — Ein Projekt mit bereitgestelltem Modell (z.B. `gpt-4.1-mini`). Siehe unten unter [Schritt 1](#schritt-1-erstelle-ein-microsoft-foundry-projekt).

Im Root dieses Repositories haben wir eine `requirements.txt` Datei beigefügt, welche alle benötigten Python-Pakete enthält, um die Codebeispiele auszuführen.

Du kannst sie installieren, indem du folgenden Befehl im Terminal im Root des Repositories ausführst:

```bash|powershell
pip install -r requirements.txt
```

Wir empfehlen, eine Python-virtuelle Umgebung zu verwenden, um Konflikte und Probleme zu vermeiden.

## VSCode einrichten

Stelle sicher, dass du die richtige Python-Version in VSCode verwendest.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry und Microsoft Foundry Agent Service einrichten

### Schritt 1: Erstelle ein Microsoft Foundry Projekt

Du benötigst einen Microsoft Foundry **Hub** und ein **Projekt** mit einem bereitgestellten Modell, um die Notebooks auszuführen.

1. Gehe zu [ai.azure.com](https://ai.azure.com) und melde dich mit deinem Azure-Konto an.
2. Erstelle einen **Hub** (oder nutze einen bestehenden). Siehe: [Hub-Ressourcen Übersicht](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Erstelle im Hub ein **Projekt**.
4. Stelle ein Modell bereit (z.B. `gpt-4.1-mini`) unter **Models + Endpoints** → **Deploy model**.

### Schritt 2: Hole deinen Projekt-Endpunkt und Modellbereitstellungsnamen

Vom Projekt im Microsoft Foundry Portal:

- **Projekt-Endpunkt** — Gehe auf die **Übersichtsseite** und kopiere die Endpunkt-URL.

![Projekt-Verbindungsstring](../../../translated_images/de/project-endpoint.8cf04c9975bbfbf1.webp)

- **Modell-Bereitstellungsname** — Gehe zu **Models + Endpoints**, wähle dein bereitgestelltes Modell aus, und notiere den **Deployment name** (z.B. `gpt-4.1-mini`).

### Schritt 3: Melde dich mit `az login` bei Azure an

Alle Notebooks verwenden **`AzureCliCredential`** zur Authentifizierung — es sind keine API-Schlüssel zu verwalten. Du musst über die Azure CLI angemeldet sein.

1. **Installiere die Azure CLI**, falls noch nicht geschehen: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Melde dich an** mit:

    ```bash|powershell
    az login
    ```

    Oder wenn du in einer Remote-/Codespace-Umgebung ohne Browser arbeitest:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Wähle dein Abonnement** falls gefragt — wähle das mit deinem Foundry-Projekt.

4. **Überprüfe**, dass du angemeldet bist:

    ```bash|powershell
    az account show
    ```

> **Warum `az login`?** Die Notebooks authentifizieren mit `AzureCliCredential` aus dem Paket `azure-identity`. Dadurch liefert deine Azure CLI Session die Anmeldedaten — keine API-Schlüssel oder Geheimnisse in deiner `.env` Datei. Das ist eine [Sicherheits-Best Practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Schritt 4: Erstelle deine `.env` Datei

Kopiere die Beispieldatei:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Öffne `.env` und fülle die zwei Werte aus:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| Variable | Wo zu finden |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-Portal → dein Projekt → **Übersichtsseite** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-Portal → **Models + Endpoints** → Name deines bereitgestellten Modells |

Das war es schon für die meisten Lektionen! Die Notebooks authentifizieren sich automatisch über deine `az login` Session.

### Schritt 5: Installiere Python-Abhängigkeiten

```bash|powershell
pip install -r requirements.txt
```

Wir empfehlen, dies innerhalb der zuvor erstellten virtuellen Umgebung auszuführen.

## Zusätzliche Einrichtung für Lektion 5 (Agentic RAG)

Lektion 5 nutzt **Azure AI Search** für retrieval-augmented generation. Wenn du diese Lektion ausführen möchtest, füge diese Variablen zu deiner `.env` Datei hinzu:

| Variable | Wo zu finden |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-Portal → deine **Azure AI Search** Ressource → **Übersicht** → URL |
| `AZURE_SEARCH_API_KEY` | Azure-Portal → deine **Azure AI Search** Ressource → **Einstellungen** → **Schlüssel** → primärer Admin-Schlüssel |

## Zusätzliche Einrichtung für Lektionen, die Azure OpenAI direkt aufrufen (Lektion 6 und 8)

Einige Notebooks in Lektion 6 und 8 rufen **Azure OpenAI** direkt auf (über die **Responses API**) anstatt über ein Microsoft Foundry Projekt zu gehen. Diese Beispiele verwendeten zuvor GitHub Models, die veraltet sind (Auslauf Juli 2026) und die Responses API nicht unterstützen. Wenn du diese Samples ausführen möchtest, füge diese Variablen zu deiner `.env` Datei hinzu:

| Variable | Wo zu finden |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure-Portal → deine **Azure OpenAI** Ressource → **Schlüssel und Endpunkt** → Endpunkt (z.B. `https://<deine-ressource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Name deines bereitgestellten Modells (z.B. `gpt-4.1-mini`), welches die Responses API unterstützt |
| `AZURE_OPENAI_API_KEY` | Optional — nur wenn du schlüsselbasierte Authentifizierung statt `az login` / Entra ID nutzt |

> Die Responses API benutzt den stabilen `/openai/v1/` Endpunkt, deshalb ist keine `api-version` nötig. Melde dich mit `az login` an, um schlüssellose Entra ID Authentifizierung zu nutzen.

## Alternativer Anbieter: MiniMax (OpenAI-kompatibel)

[MiniMax](https://platform.minimaxi.com/) bietet Modelle mit großem Kontext (bis zu 204K Token) über eine OpenAI-kompatible API. Da der Microsoft Agent Framework `OpenAIChatClient` mit jedem OpenAI-kompatiblen Endpunkt funktioniert, kannst du MiniMax als Drop-in-Alternative zu Azure OpenAI oder OpenAI verwenden.

Füge diese Variablen zu deiner `.env` Datei hinzu:

| Variable | Wo zu finden |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Plattform](https://platform.minimaxi.com/) → API Schlüssel |
| `MINIMAX_BASE_URL` | Verwende `https://api.minimax.io/v1` (Standardwert) |
| `MINIMAX_MODEL_ID` | Modellname zur Nutzung (z.B. `MiniMax-M3`) |

**Beispielmodelle**: `MiniMax-M3` (empfohlen), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (schnellere Antworten). Modellnamen und Verfügbarkeit können sich im Laufe der Zeit ändern, und der Zugriff auf ein bestimmtes Modell kann von deinem Konto oder deiner Region abhängen — siehe die aktuelle Liste auf der [MiniMax Plattform](https://platform.minimaxi.com/). Wenn `MiniMax-M3` für dein Konto nicht verfügbar ist, stelle `MINIMAX_MODEL_ID` auf ein Modell um, zu dem du Zugang hast (z.B. `MiniMax-M2.7`).

Die Codebeispiele, die `OpenAIChatClient` verwenden (z.B. Lektion 14 Hotelbuchungs-Workflow), erkennen deine MiniMax-Konfiguration automatisch, wenn `MINIMAX_API_KEY` gesetzt ist.

## Alternativer Anbieter: Foundry Local (Modelle lokal ausführen)

[Foundry Local](https://foundrylocal.ai) ist eine leichte Laufzeitumgebung, die Sprachmodelle **vollständig auf deinem eigenen Rechner** herunterlädt, verwaltet und bereitstellt über eine OpenAI-kompatible API — keine Cloud, kein Azure-Abonnement und keine API-Schlüssel. Es ist eine großartige Option für Offline-Entwicklung, Experimente ohne Cloud-Kosten oder um Daten lokal zu behalten.

Da der Microsoft Agent Framework `OpenAIChatClient` mit jedem OpenAI-kompatiblen Endpunkt funktioniert, ist Foundry Local eine lokale Drop-in-Alternative zu Azure OpenAI.

**1. Installiere Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Lade ein Modell herunter und starte es** (dies startet auch den lokalen Dienst):

```bash
foundry model list          # verfügbare Modelle ansehen
foundry model run phi-4-mini
```

**3. Installiere das Python SDK**, das verwendet wird, um den lokalen Endpunkt zu erkennen:

```bash
pip install foundry-local-sdk
```

**4. Richte das Microsoft Agent Framework auf dein lokales Modell aus:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Lädt das Modell (falls benötigt) herunter und stellt es lokal bereit, danach wird der Endpunkt/Port ermittelt.
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

> **Hinweis:** Foundry Local stellt einen OpenAI-kompatiblen **Chat Completions** Endpunkt bereit. Nutze ihn für lokale Entwicklung und Offline-Szenarien. Für den vollen Funktionsumfang der **Responses API** (zustandsbehaftete Gespräche, tiefgehende Werkzeug-Orchestrierung und Agenten-Entwicklung) wähle **Azure OpenAI** oder ein **Microsoft Foundry** Projekt wie in den Lektionen gezeigt. Siehe die [Foundry Local Dokumentation](https://foundrylocal.ai) für den aktuellen Modellkatalog und Plattform-Unterstützung.


## Zusätzliche Einrichtung für Lektion 8 (Bing Grounding Workflow)

Das bedingte Workflow-Notebook in Lektion 8 verwendet **Bing Grounding** über Microsoft Foundry. Wenn Sie dieses Beispiel ausführen möchten, fügen Sie diese Variable zu Ihrer `.env`-Datei hinzu:

| Variable | Wo zu finden |
|----------|--------------|
| `BING_CONNECTION_ID` | Microsoft Foundry-Portal → Ihr Projekt → **Verwaltung** → **Verbundene Ressourcen** → Ihre Bing-Verbindung → Kopieren der Verbindungs-ID |

## Fehlerbehebung

### SSL-Zertifikat-Überprüfungsfehler auf macOS

Wenn Sie macOS verwenden und einen Fehler wie diesen erhalten:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dies ist ein bekanntes Problem bei Python auf macOS, bei dem die System-SSL-Zertifikate nicht automatisch als vertrauenswürdig eingestuft werden. Versuchen Sie die folgenden Lösungen in der angegebenen Reihenfolge:

**Option 1: Führen Sie das Install Certificates-Skript von Python aus (empfohlen)**

```bash
# Ersetzen Sie 3.XX durch Ihre installierte Python-Version (z. B. 3.12 oder 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Option 2: Verwenden Sie `connection_verify=False` in Ihrem Notebook (nur für GitHub Models Notebooks)**

Im Notebook zu Lektion 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) ist bereits eine auskommentierte Umgehung enthalten. Kommentieren Sie `connection_verify=False` aus, wenn Sie den Client erstellen:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deaktivieren Sie die SSL-Überprüfung, wenn Sie Zertifikatsfehler erhalten
)
```

> **⚠️ Warnung:** Das Deaktivieren der SSL-Überprüfung (`connection_verify=False`) reduziert die Sicherheit, da die Zertifikatvalidierung übersprungen wird. Verwenden Sie dies nur als vorübergehende Umgehung in Entwicklungsumgebungen, niemals in Produktionsumgebungen.

**Option 3: Installieren und verwenden Sie `truststore`**

```bash
pip install truststore
```

Fügen Sie dann das Folgende am Anfang Ihres Notebooks oder Skripts hinzu, bevor Sie Netzwerkaufrufe tätigen:

```python
import truststore
truststore.inject_into_ssl()
```

## Stecken geblieben?

Wenn Sie Probleme bei der Ausführung dieser Einrichtung haben, treten Sie unserem <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> bei oder <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">erstellen Sie ein Issue</a>.

## Nächste Lektion

Sie sind jetzt bereit, den Code für diesen Kurs auszuführen. Viel Erfolg beim weiteren Lernen über die Welt der KI-Agenten!

[Einführung in KI-Agenten und Anwendungsfälle für Agenten](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->