# Kurs-Setup

## Einführung

Diese Lektion behandelt, wie Sie die Codebeispiele dieses Kurses ausführen.

## Treten Sie anderen Lernenden bei und erhalten Sie Hilfe

Bevor Sie Ihr Repo klonen, treten Sie dem [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) bei, um Hilfe beim Setup zu erhalten, Fragen zum Kurs zu stellen oder sich mit anderen Lernenden zu vernetzen.

## Dieses Repo klonen oder forken

Um zu beginnen, klonen oder forken Sie bitte das GitHub-Repository. Dadurch erhalten Sie Ihre eigene Version des Kursmaterials, sodass Sie den Code ausführen, testen und anpassen können!

Dies kann durch Klicken des Links zum <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">das Repo forken</a> erfolgen

Sie sollten nun Ihre eigene geforkte Version dieses Kurses unter folgendem Link haben:

![Geforktes Repository](../../../translated_images/de/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (empfohlen für Workshops / Codespaces)

  >Das gesamte Repository kann groß sein (~3 GB), wenn Sie die vollständige Historie und alle Dateien herunterladen. Wenn Sie nur am Workshop teilnehmen oder nur wenige Lektionen benötigen, vermeidet ein flacher Klon (oder ein sparsamer Klon) den größten Teil dieses Downloads, indem die Historie abgeschnitten und/oder Blobs übersprungen werden.

#### Schneller Shallow-Clone — minimale Historie, alle Dateien

Ersetzen Sie `<your-username>` in den folgenden Befehlen durch Ihre Fork-URL (oder die Upstream-URL, wenn Sie dies bevorzugen).

Um nur die neueste Commit-Historie zu klonen (kleiner Download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Um einen bestimmten Branch zu klonen:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partieller (sparsamer) Klon — minimale Blobs + nur ausgewählte Ordner

Dies verwendet Partial Clone und sparse-checkout (erfordert Git 2.25+ und empfohlen moderne Git-Version mit Partial-Clone-Unterstützung):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Wechseln Sie in den Repo-Ordner:

```bash|powershell
cd ai-agents-for-beginners
```

Geben Sie dann an, welche Ordner Sie möchten (das Beispiel unten zeigt zwei Ordner):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Nachdem Sie geklont und die Dateien überprüft haben: Wenn Sie nur die Dateien benötigen und Speicherplatz freigeben möchten (keine Git-Historie), löschen Sie bitte die Repository-Metadaten (💀irreversibel — Sie verlieren alle Git-Funktionen: keine Commits, Pulls, Pushes oder Zugriff auf die Historie).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Verwendung von GitHub Codespaces (empfohlen, um lokale große Downloads zu vermeiden)

- Erstellen Sie für dieses Repo einen neuen Codespace über die [GitHub UI](https://github.com/codespaces).  

- Führen Sie im Terminal des neu erstellten Codespace einen der oben genannten shallow-/sparse-clone-Befehle aus, um nur die Lektion-Ordner in den Codespace-Arbeitsbereich zu holen, die Sie benötigen.
- Optional: Entfernen Sie nach dem Klonen in Codespaces .git, um zusätzlichen Speicher freizugeben (siehe oben stehende Löschbefehle).
- Hinweis: Wenn Sie das Repo direkt in Codespaces öffnen (ohne zusätzlichen Klon), erstellt Codespaces die Devcontainer-Umgebung und kann dennoch mehr bereitstellen, als Sie benötigen. Das Klonen einer flachen Kopie in einem frischen Codespace gibt Ihnen mehr Kontrolle über den Festplattenspeicher.

#### Tipps

- Ersetzen Sie immer die Klon-URL durch Ihre Fork, wenn Sie bearbeiten/committen möchten.
- Wenn Sie später mehr Historie oder Dateien benötigen, können Sie diese abrufen oder sparse-checkout anpassen, um zusätzliche Ordner einzuschließen.

## Ausführen des Codes

Dieser Kurs bietet eine Reihe von Jupyter-Notebooks, die Sie ausführen können, um praktische Erfahrungen beim Erstellen von AI-Agenten zu sammeln.

Die Codebeispiele verwenden das Microsoft Agent Framework (MAF) mit dem `AzureAIProjectAgentProvider`, das sich über Microsoft Foundry mit dem Azure AI Agent Service V2 (der Responses API) verbindet.

Alle Python-Notebooks sind mit `*-python-agent-framework.ipynb` gekennzeichnet.

## Voraussetzungen

- Python 3.12+
  - **HINWEIS**: Wenn Sie Python 3.12 nicht installiert haben, stellen Sie sicher, dass Sie es installieren. Erstellen Sie dann Ihr venv mit python3.12, um sicherzustellen, dass die richtigen Versionen aus der requirements.txt installiert werden.
  
    >Beispiel

    Erstellen Sie ein Python-venv-Verzeichnis:

    ```bash|powershell
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

- .NET 10+: Für Beispielcodes, die .NET verwenden, stellen Sie sicher, dass Sie das [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) oder neuer installieren. Prüfen Sie anschließend Ihre installierte .NET SDK-Version:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Erforderlich für die Authentifizierung. Installieren Sie es von [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure-Abonnement** — Für den Zugriff auf Microsoft Foundry und Azure AI Agent Service.
- **Microsoft Foundry-Projekt** — Ein Projekt mit einem bereitgestellten Modell (z. B. `gpt-4o`). Siehe [Schritt 1](../../../00-course-setup) unten.

Wir haben eine `requirements.txt`-Datei im Stamm dieses Repositories aufgenommen, die alle benötigten Python-Pakete zur Ausführung der Codebeispiele enthält.

Sie können diese installieren, indem Sie den folgenden Befehl in Ihrem Terminal im Stammverzeichnis des Repositories ausführen:

```bash|powershell
pip install -r requirements.txt
```

Wir empfehlen, eine Python-Virtual-Environment zu erstellen, um Konflikte und Probleme zu vermeiden.

## VSCode einrichten

Stellen Sie sicher, dass Sie in VSCode die richtige Python-Version verwenden.

![Bild](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry und Azure AI Agent Service einrichten

### Schritt 1: Erstellen Sie ein Microsoft Foundry-Projekt

Sie benötigen ein Azure AI Foundry **hub** und **project** mit einem bereitgestellten Modell, um die Notebooks auszuführen.

1. Gehen Sie zu [ai.azure.com](https://ai.azure.com) und melden Sie sich mit Ihrem Azure-Konto an.
2. Erstellen Sie ein **hub** (oder verwenden Sie ein vorhandenes). Siehe: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Erstellen Sie innerhalb des Hubs ein **project**.
4. Stellen Sie ein Modell bereit (z. B. `gpt-4o`) über **Models + Endpoints** → **Deploy model**.

### Schritt 2: Abrufen Ihres Projektendpunkts und des Modellbereitstellungsnamens

Aus Ihrem Projekt im Microsoft Foundry-Portal:

- **Project Endpoint** — Gehen Sie zur **Übersicht**-Seite und kopieren Sie die Endpunkt-URL.

![Projekt-Endpunkt](../../../translated_images/de/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Gehen Sie zu **Models + Endpoints**, wählen Sie Ihr bereitgestelltes Modell aus und notieren Sie den **Deployment name** (z. B. `gpt-4o`).

### Schritt 3: Anmelden bei Azure mit `az login`

Alle Notebooks verwenden **`AzureCliCredential`** für die Authentifizierung — es sind keine API-Schlüssel zu verwalten. Dafür müssen Sie über die Azure CLI angemeldet sein.

1. **Installieren Sie die Azure CLI** falls noch nicht geschehen: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Melden Sie sich an** durch Ausführen von:

    ```bash|powershell
    az login
    ```

    Oder wenn Sie sich in einer Remote-/Codespace-Umgebung ohne Browser befinden:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Wählen Sie Ihr Abonnement aus**, falls Sie dazu aufgefordert werden — wählen Sie dasjenige aus, das Ihr Foundry-Projekt enthält.

4. **Überprüfen** Sie, ob Sie angemeldet sind:

    ```bash|powershell
    az account show
    ```

> **Warum `az login`?** Die Notebooks authentifizieren sich mit `AzureCliCredential` aus dem Paket `azure-identity`. Das bedeutet, dass Ihre Azure CLI-Session die Anmeldeinformationen bereitstellt — keine API-Schlüssel oder Geheimnisse in Ihrer `.env`-Datei. Dies ist eine [Sicherheitsbest Practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Wo zu finden |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-Portal → Ihr Projekt → **Übersicht**-Seite |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-Portal → **Models + Endpoints** → Name Ihrer Modellbereitstellung |

Das war's für die meisten Lektionen! Die Notebooks authentifizieren sich automatisch über Ihre `az login`-Session.

### Schritt 5: Installieren Sie die Python-Abhängigkeiten

```bash|powershell
pip install -r requirements.txt
```

Wir empfehlen, dies innerhalb der zuvor erstellten Virtual Environment auszuführen.

## Zusätzliche Einrichtung für Lektion 5 (Agentic RAG)

Lektion 5 verwendet **Azure AI Search** für retrieval-augmented generation. Wenn Sie diese Lektion ausführen möchten, fügen Sie diese Variablen zu Ihrer `.env`-Datei hinzu:

| Variable | Wo zu finden |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-Portal → Ihre **Azure AI Search**-Ressource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure-Portal → Ihre **Azure AI Search**-Ressource → **Settings** → **Keys** → primärer Admin-Schlüssel |

## Zusätzliche Einrichtung für Lektion 6 und Lektion 8 (GitHub Models)

Einige Notebooks in Lektion 6 und 8 verwenden **GitHub Models** statt Azure AI Foundry. Wenn Sie diese Beispiele ausführen möchten, fügen Sie diese Variablen zu Ihrer `.env`-Datei hinzu:

| Variable | Wo zu finden |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Verwenden Sie `https://models.inference.ai.azure.com` (Standardwert) |
| `GITHUB_MODEL_ID` | Modellname zur Verwendung (z. B. `gpt-4o-mini`) |

## Zusätzliche Einrichtung für Lektion 8 (Bing Grounding Workflow)

Das bedingte Workflow-Notebook in Lektion 8 verwendet **Bing grounding** über Azure AI Foundry. Wenn Sie dieses Beispiel ausführen möchten, fügen Sie diese Variable zu Ihrer `.env`-Datei hinzu:

| Variable | Wo zu finden |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry-Portal → Ihr Projekt → **Management** → **Connected resources** → Ihre Bing-Verbindung → kopieren Sie die Connection ID |

## Fehlerbehebung

### SSL-Zertifikat-Überprüfungsfehler auf macOS

Wenn Sie macOS verwenden und auf einen Fehler wie diesen stoßen:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dies ist ein bekanntes Problem mit Python auf macOS, bei dem die System-SSL-Zertifikate nicht automatisch vertraut werden. Versuchen Sie die folgenden Lösungen in der Reihenfolge:

**Option 1: Führen Sie das Install Certificates-Skript von Python aus (empfohlen)**

```bash
# Ersetzen Sie 3.XX durch Ihre installierte Python-Version (z. B. 3.12 oder 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Option 2: Verwenden Sie `connection_verify=False` in Ihrem Notebook (nur für GitHub Models-Notebooks)**

Im Lesson 6-Notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) ist bereits ein auskommentierter Workaround enthalten. Kommentieren Sie `connection_verify=False` aus, wenn Sie den Client erstellen:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deaktivieren Sie die SSL-Überprüfung, wenn Sie auf Zertifikatsfehler stoßen.
)
```

> **⚠️ Warnung:** Das Deaktivieren der SSL-Überprüfung (`connection_verify=False`) reduziert die Sicherheit, indem die Zertifikatsvalidierung übersprungen wird. Verwenden Sie dies nur als vorübergehende Problemumgehung in Entwicklungsumgebungen, niemals in der Produktion.

**Option 3: Installieren und verwenden Sie `truststore`**

```bash
pip install truststore
```

Fügen Sie dann Folgendes oben in Ihr Notebook oder Skript ein, bevor Sie Netzwerkaufrufe tätigen:

```python
import truststore
truststore.inject_into_ssl()
```

## Festgefahren?

Wenn Sie Probleme beim Ausführen dieses Setups haben, springen Sie in unseren <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> oder <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">erstellen Sie ein Issue</a>.

## Nächste Lektion

Sie sind nun bereit, den Code für diesen Kurs auszuführen. Viel Spaß beim weiteren Lernen über die Welt der AI-Agenten!

[Einführung in AI-Agenten und Anwendungsfälle](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Haftungsausschluss:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir um Genauigkeit bemüht sind, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->