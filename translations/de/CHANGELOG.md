# Änderungsprotokoll

Alle bedeutsamen Änderungen am **AI Agents for Beginners** Kurs sind in dieser Datei dokumentiert.

## [Veröffentlicht] — 2026-07-13

Dieses Release fügt zwei neue Lektionen hinzu, die den Bereitstellungsabschnitt abschließen — Skalierung von Agenten bis hin zu Microsoft Foundry und herunter bis zu einem einzelnen Arbeitsplatz — sowie eine Smoke-Test-Pipeline, aktualisierte Kursnavigation, neue Lernfähigkeiten und aktualisiertes Branding.

### Hinzugefügt

- **Lektion 16 — Bereitstellung skalierbarer Agenten mit Microsoft Foundry.** Neue Lektion [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) und ausführbares Notebook [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), welches einen produktiven Kundenservice-Agenten (Tools, RAG, Speicher, Modellrouting, Antwort-Caching, menschliche Genehmigung, eine Evaluierungsschranke und OpenTelemetry Tracing) erstellt, mit Entwicklungs-/Bereitstellungs-/Laufzeit-Mermaid-Diagrammen, einem Wissenscheck, einer Aufgabe und einer Herausforderung.
- **Lektion 17 — Erstellung lokaler AI-Agenten mit Foundry Local und Qwen.** Neue Lektion [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) und Notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb), die einen vollständig geräteinternen Engineering-Assistenten (Qwen Funktionsaufruf via Foundry Local, sandboxed Dateitools, lokales RAG mit Chroma, optional lokaler MCP) erstellt, mit lokal-only / lokal-RAG / Tool-Aufruf-Diagrammen, einem Wissenscheck, einer Aufgabe und einer Herausforderung.
- **Smoke-Test-Pipeline.** Neuer [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) Workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) plus pro Lektion Kataloge unter [tests/](./tests/README.md) für die bereitstellbaren Agenten der Lektionen 01, 04, 05 und 16, mit einer Index-README, die jeden Katalog der jeweiligen Lektion und dem gehosteten Agent-Namen zuordnet. Lektion 16 erhält einen Abschnitt "Validierung eines bereitgestellten Agenten mit Smoke Tests"; Lektionen 01/04/05 erhalten einen optionalen Smoke-Test-Hinweis.
- **Lernfähigkeiten.** Neue Agenten-Fähigkeiten unter `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (fasst die Lektion 16 und 17 Anleitung zusammen) und [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (wie man die Notebook-Beispiele gegen eine Live Microsoft Foundry / Azure OpenAI Umgebung validiert).
- **Notebook-Validierungslauf.** Neues [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), das jedes Python-Notebook kopflos mit `nbconvert` ausführt und eine PASS/FAIL Matrix (plus `results.json`) ausgibt. Es erkennt selbständig das Repo-Root und Python, schließt standardmäßig Nicht-Kurs-Notebooks (`.venv`, `site-packages`, `translations`, Skill-Template-Assets) und `.NET` Notebooks aus und unterstützt `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` und `-Python`.
- **Kursnavigation.** Hinzugefügt wurden "Vorherige/Nächste Lektion"-Links zu den Lektionen 11–15 (zuvor fehlend), sodass der ganze Kurs in beiden Richtungen von 00 bis 18 verknüpft ist.
- **Neue Thumbnails.** Lektion-Thumbnails für Lektionen 16 und 17 sowie ein aktualisiertes Repository-Social-Bild [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (das jetzt für die zwei neuen Lektionen und die `aka.ms/ai-agents-beginners` URL wirbt).
- **Abhängigkeiten** ([requirements.txt](../../requirements.txt)): `foundry-local-sdk` und `chromadb` für Lektion 17 hinzugefügt.

### Geändert

- **Haupt-[README.md](./README.md)** Lektionstabelle: Lektionen 16 und 17 verlinken jetzt auf ihren Inhalt (vorher "Coming Soon"); Repository-Bild auf `repo-thumbnailv3.png` aktualisiert.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: Lektionen 16 und 17 zur Lektion-für-Lektion-Anleitung und Lernpfaden hinzugefügt sowie einen Abschnitt "Validierung bereitgestellter Agenten mit Smoke Tests".
- **[AGENTS.md](./AGENTS.md)**: aktualisierte Lektionenzahl/-beschreibung (00–18), Abschnitt zur Smoke-Test-Validierung hinzugefügt und Beispielenamen für Lektionen 16/17 ergänzt.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Vorherige Lektion" zeigt jetzt auf Lektion 17 (vorher Lektion 15), damit die Kette geschlossen ist.
- **Standardisierte Modellreferenzen bei nicht veralteten Modellen.** Alle `gpt-4o` / `gpt-4o-mini` Referenzen im Kurs (Dokumentation, `.env.example`, Python/.NET Notebooks und Beispiele) durch `gpt-4.1-mini` ersetzt — `gpt-4o` (alle Versionen) wird 2026 eingestellt. Lektion 16 hält im Modell-Routing Beispiel einen kleinen/großen Kontrast mit `gpt-4.1-mini` (klein) und `gpt-4.1` (groß). Python-Notebooks wählen das Modell nun über Umgebungsvariablen (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) anstelle eines fest kodierten Modellnamens.

### Hinweise und bekannte Einschränkungen

- **Nicht gegen Live Azure ausgeführt.** Die Notebooks der neuen Lektionen sind lehrreiche Beispiele; führe und validiere sie mit deinem eigenen Microsoft Foundry / Foundry Local Setup. Der Smoke-Test Workflow erfordert, dass du den Agenten der Lektion bereitstellst und Azure OIDC Geheimnisse (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) mit der **Azure AI User** Rolle auf Projekt-Ebene in Foundry konfigurierst.
- **Lektion 17 ist nur lokal.** Sie hat keinen Foundry Responses Endpunkt, daher gilt die Smoke-Test Aktion nicht; validiere sie, indem du das Notebook auf deinem Arbeitsplatz ausführst.

## [Veröffentlicht] — 2026-07-06

Dieses Release migriert den Kurs zur **Azure OpenAI Responses API**, standardisiert Produktnamen auf **Microsoft Foundry** und das **Microsoft Agent Framework (MAF)**, stellt GitHub Models ein, aktualisiert SDK-Versionen und fügt neuen Inhalt zu lokalen Modellen und dem Hosting anderer Frameworks auf Foundry hinzu.

### Hinzugefügt

- **Migrationsfähigkeit** — Installierte die [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agenten-Fähigkeit (von [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) unter `.agents/skills/`, inklusive ihrer Referenzen und Scanner-Scripts.
- **Foundry Local (Modelle lokal ausführen)** — Neuer Abschnitt "Alternativer Anbieter: Foundry Local" in [00-course-setup/README.md](./00-course-setup/README.md), der Installation (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` und die Verbindung von `FoundryLocalManager` mit dem Microsoft Agent Framework via `OpenAIChatClient` behandelt.
- **Hosting von LangChain / LangGraph Agenten auf Microsoft Foundry** — Neuer Abschnitt in [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus ausführbares Beispiel [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) mittels `langchain-azure-ai[hosting]` und `ResponsesHostServer` (das `/responses` Protokoll), basierend auf [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Neuer Abschnitt "Praxisbeispiel: Microsoft Project Opal" in [15-browser-use/README.md](./15-browser-use/README.md), der Opal als Agent für den Unternehmenseinsatz darstellt und an Kurskonzepte anbindet (Mensch in der Schleife, Vertrauen/Sicherheit, Planung, Skills).
- **Zweites Lektion 02 Python-Beispiel** — Hinzugefügt [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (siehe "Geändert" — migriert vom früheren Semantic Kernel Notebook) und dessen Verlinkung in der Lektion README.
- **Abschnitt Modelle und Anbieter** hinzugefügt zu [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Geändert

- **Chat Completions → Responses API (Python).** Beispiele, die das Modell direkt ansprachen, wurden von Chat Completions zur Responses API migriert (`client.responses.create(input=..., store=False)`, `resp.output_text`), mit dem `OpenAI` Client gegen den stabilen Azure OpenAI `/openai/v1/` Endpunkt (kein `api_version`). Betroffene Beispiele umfassen:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — der vollständige Funktionsaufruf-Durchgang (Tool-Schema an das Responses-Format angepasst, Tool-Ergebnisse als `function_call_output`, `max_output_tokens` etc. zurückgegeben).
- **GitHub Models → Azure OpenAI.** GitHub Models ist veraltet (Stelleinstellung **Juli 2026**) und unterstützt die Responses API nicht. Alle GitHub Models Code-Pfade wurden auf Azure OpenAI / Microsoft Foundry in Python und .NET-Beispielen konvertiert:
  - Python: Arbeitsablaufnotebooks Lektion 08 (`01`–`03`), Lektion 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + begleitende `.md` Dokumente, und Lektion 08 dotNET Arbeitsablaufnotebooks/`.md` (`01`–`03`) nutzen jetzt `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` mit `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Das frühere `02-semantic-kernel.ipynb` wurde neu geschrieben, um Microsoft Agent Framework mit Azure OpenAI (Responses API) zu verwenden und in `02-python-agent-framework-azure-openai.ipynb` umbenannt.
- **Standardisierung auf `FoundryChatClient` + `as_agent`.** README und Notebook-Code, der `AzureAIProjectAgentProvider` referenzierte, wurden auf das kanonische Muster von Lektion 01 und dem Framework-eigenen Beispiel standardisiert: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` mit `provider.as_agent(...)`. Aktualisiert in den READMEs und Notebooks von Lektion 02–14 (z.B. Lektion 13 Speicher, alle Lektion 14 Notebooks, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Produktnamen.** Im englischen Inhalt überall umbenannt:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Unverändert: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" und Umgebungsvariablennamen.)
- **Abhängigkeiten** ([requirements.txt](../../requirements.txt)):
  - Festgelegt `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Festgelegt `openai>=1.108.1` (Minimum für Responses API).
  - Entfernt `azure-ai-inference` (wurde nur von den migrierten GitHub Models Beispielen verwendet).
- **Umgebungskonfiguration** ([.env.example](../../.env.example)): GitHub Models Variablen entfernt (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); hinzugefügt `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` und optional `AZURE_OPENAI_API_KEY`; Benennung zu Microsoft Foundry aktualisiert.
- **Dokumentation** — Aktualisiert [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) und [STUDY_GUIDE.md](./STUDY_GUIDE.md) entsprechend (Setup Umgebungsvariablen, Verifizierungssnippet, Anbieterrichtlinien, Benennung).

### Entfernt

- GitHub Models Onboarding Schritte und Umgebungsvariablen aus den Setup-Dokumenten entfernt (ersetzt durch Azure OpenAI / Microsoft Foundry).

### Sicherheit / Datenschutz (Öffentlich Teilen Reinigung)

- Jupyter Notebook Ausführungsausgaben gelöscht, die eine echte **Azure Abonnement-ID**, Resource-Gruppen/-Namen und Bing-Verbindungs-ID preisgaben, sowie Entwickler-**lokale Dateipfade und Benutzernamen**, in:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Es wurde überprüft, dass keine API-Schlüssel, Tokens, Abonnement-IDs oder persönlichen Pfade im verfolgten englischen Inhalt verbleiben (die verbleibenden `GITHUB_TOKEN`-Verweise sind das GitHub Actions-Token in Workflows und der GitHub MCP Server PAT in der Einrichtung von Lektion 11 – beide legitim und nicht mit GitHub Models verbunden).

### Hinweise und bekannte Einschränkungen

- **Nicht ausgeführt/k compiliert.** Dies sind Bildungsbeispiele, die für API-/Namenkorrektheit aktualisiert wurden; sie wurden nicht gegen Live-Azure-Ressourcen ausgeführt und die .NET-Beispiele wurden in dieser Umgebung nicht kompiliert. Validieren Sie diese anhand Ihrer eigenen Microsoft Foundry / Azure OpenAI Bereitstellung.
- **Modellbereitstellung muss die Responses API unterstützen.** Verwenden Sie eine Bereitstellung wie `gpt-4.1-mini`, `gpt-4.1` oder ein `gpt-5.x`-Modell. Ältere Modelle unterstützen die Kernfunktionalität von Responses, aber nicht alle Features.
- **Agent-Framework Version.** Die Beispiele zielen auf die neueste MAF (`>=1.10.0`) ab. Der kanonische Agent-Erstellungsaufruf ist `client.as_agent(...)`; APIs wurden gegen die veröffentlichten Dokumentationen des Frameworks und einen installierten Build geprüft. Wenn Sie eine andere Version fixieren, bestätigen Sie die Verfügbarkeit der Methoden (`as_agent` vs. `create_agent`).
- **Lesson 08 Workflow-Notebook 04** bewahrt absichtlich `AzureAIAgentClient` (aus `agent-framework-azure-ai`), da es Microsoft Foundry Agent Service gehostete Tools (Bing-Grundlage, Code-Interpreter) verwendet; es basiert bereits auf Responses.
- **.NET Standardbereitsstellung.** Zwei Lesson 08 dotNET Workflow-Beispiele hatten zuvor ein spezifisches Modell fest kodiert; sie verwenden jetzt standardmäßig `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Wenn ein Beispiel multimodale/Vision-Eingabe erfordert, setzen Sie `AZURE_OPENAI_DEPLOYMENT` auf ein geeignetes Modell.
- **Foundry Local** bietet einen OpenAI-kompatiblen **Chat Completions** Endpunkt und ist für lokale Entwicklung gedacht; verwenden Sie Azure OpenAI / Microsoft Foundry für den vollständigen Responses API Funktionsumfang.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->