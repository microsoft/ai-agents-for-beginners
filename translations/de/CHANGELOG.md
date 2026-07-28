# Änderungsprotokoll

Alle bemerkenswerten Änderungen am **AI Agents for Beginners** Kurs sind in dieser Datei dokumentiert.

## [Veröffentlicht] — 2026-07-14

Diese Version entfernt den Kurs von zwei neu eingestellten Modellen, migriert die verbleibenden Lesson-Notebooks zur stabilen Microsoft Agent Framework API und validiert die Python-Notebooks gegen eine aktive Microsoft Foundry Bereitstellung.

### Geändert

- **Umstieg von eingestellten Modellen (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Sowohl `gpt-4.1` als auch `gpt-4.1-mini` sind jetzt eingestellt (veröffentlichter Abschaltdatum **14. Oktober 2026**). Alle Kursverweise (Dokumentation, `.env.example`, Python/.NET-Notebooks und Beispiele) wurden durch das nicht eingestellte `gpt-5-mini` ersetzt. Das Modell-Routing-Beispiel in Lektion 16 behält einen Klein/Groß-Kontrast mit `gpt-5-nano` (klein) und `gpt-5-mini` (groß). Drittanbieter-Dateien ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), historischer GitHub Models-Text und die Fähigkeitsnotizen der `azure-openai-to-responses` Skill blieben absichtlich unverändert.
- **Lesson 14 Übergabe-Notebook zur stabilen API migriert.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) verwendet jetzt `agent_framework.orchestrations.HandoffBuilder` mit `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, auf `event.type` basierendes Streaming und `FoundryChatClient` (ersetzt die entfernten Symbole vor Version 1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Lesson 14 Human-in-the-Loop-Notebook zur stabilen API migriert.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) pausiert jetzt über `ctx.request_info(...)` + `@response_handler` (ersetzt die entfernten `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), baut mit `WorkflowBuilder(start_executor=..., output_executors=[...])`, steuert strukturierte Ausgaben über `default_options={"response_format": ...}` und verwendet eine skriptbasierte Antwort, sodass das Notebook unbeaufsichtigt läuft (kein blockierendes `input()`).
- **Umgebungskonfiguration** ([.env.example](../../.env.example)): Modell-Bereitstellungsnamen auf `gpt-5-mini` geändert; hinzugefügt `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (Routing in Lektion 16) und das zuvor fehlende `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (Lektion 15 Browser-Nutzung).
- **Abhängigkeiten** ([requirements.txt](../../requirements.txt)): `agent-framework`, `agent-framework-foundry` und `agent-framework-openai` auf `~=1.10.0` festgelegt für eine selbstkonsistente, validierte Menge (1.11.0 bringt experimentelle Breaking Changes an den Oberflächen, die von diesen Lektionen verwendet werden).

### Anmerkungen und bekannte Einschränkungen

- **Validiert gegen live Microsoft Foundry.** Die Python-Notebooks wurden kopflos mit `nbconvert` gegen ein Microsoft Foundry Projekt ausgeführt unter Verwendung von `gpt-5-mini` (und `gpt-5-nano` für das Routing in Lektion 16). Bereitstellen Sie äquivalente nicht eingestellte Modelle in Ihrem eigenen Projekt; die Notebooks lesen den Bereitstellungsnamen aus `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Für einige Lektionen werden weiterhin zusätzliche Ressourcen benötigt.** Lektion 05 benötigt Azure AI Search; der Workflow für Bing-Grundierung in Lektion 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) benötigt eine Bing-Verbindung und Microsoft Foundry Agent Service hostete Werkzeuge; Lektion 13 (Cognee) und Lektion 17 (Foundry Local) benötigen eigene Laufzeitumgebungen.

## [Veröffentlicht] — 2026-07-13

Diese Version fügt zwei neue Lektionen hinzu, die den Bereitstellungsbogen vollständig machen — Skalierung von Agenten hoch auf Microsoft Foundry und runter auf einen einzelnen Arbeitsplatz — plus eine Smoke-Test-Pipeline, aktualisierte Kursnavigation, neue Lernendenfähigkeiten und ein aktualisiertes Branding.

### Hinzugefügt

- **Lesson 16 — Skalierbare Agenten mit Microsoft Foundry bereitstellen.** Neue Lektion [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) und ausführbares Notebook [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) zum Aufbau eines produktiven Kunden-Support-Agenten (Tools, RAG, Memory, Modell-Routing, Antwort-Caching, menschliche Freigabe, Bewertungsgate und OpenTelemetry-Tracing), mit Entwickungs-/Bereitstellungs-/Runtime-Mermaid-Diagrammen, einer Wissensabfrage, einer Aufgabe und einer Herausforderung.
- **Lesson 17 — Erstellung lokaler AI-Agenten mit Foundry Local und Qwen.** Neue Lektion [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) und Notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) zum Aufbau eines vollständig geräteinternen Ingenieurassistenten (Qwen Funktionsaufruf über Foundry Local, sandboxed Dateitools, lokaler RAG mit Chroma, optional lokales MCP), mit lokal-only / lokal-RAG / Toolaufruf-Diagrammen, einer Wissensabfrage, einer Aufgabe und einer Herausforderung.
- **Smoke-Test-Pipeline.** Neuer [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) Workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) plus pro Lektion Kataloge unter [tests/](./tests/README.md) für die in Lektionen 01, 04, 05 und 16 bereitstellbaren Agenten, mit einem Index-README zum Abbilden jedes Katalogs auf seine Lektion und den Namen des gehosteten Agenten. Lektion 16 erhält eine Sektion "Validierung eines bereitgestellten Agenten mit Smoke Tests"; die Lektionen 01/04/05 erhalten einen optionalen Verweis auf Smoke Tests.
- **Lernenden-Fähigkeiten.** Neue Agenten-Fähigkeiten unter `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (bündelt die Anleitung der Lektionen 16 und 17) und [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (wie man die Notebook-Beispiele gegen eine aktive Microsoft Foundry / Azure OpenAI Umgebung validiert).
- **Notebook-Validierungs-Runner.** Neues [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), das jedes Python-Notebook kopflos mit `nbconvert` ausführt und eine PASS/FAIL-Matrix (plus `results.json`) ausgibt. Es erkennt automatisch das Repo-Root und Python, schließt standardmäßig Nicht-Kurs-Notebooks (`.venv`, `site-packages`, `translations`, Skill-Template-Assets) und `.NET`-Notebooks aus und unterstützt `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` und `-Python`.
- **Kursnavigation.** Hinzufügen von Vorherige/Nächste-Lektion Links zu den Lektionen 11–15 (vorher fehlend), sodass der gesamte Kurs 00 → 18 in beide Richtungen verkettet ist.
- **Neue Thumbnails.** Lektionsthumbnails für die Lektionen 16 und 17, plus ein aktualisiertes soziales Repository-Bild [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (bewirbt jetzt die beiden neuen Lektionen und die URL `aka.ms/ai-agents-beginners`).
- **Abhängigkeiten** ([requirements.txt](../../requirements.txt)): hinzugefügt `foundry-local-sdk` und `chromadb` für Lektion 17.

### Geändert

- **Haupt [README.md](./README.md)** Lektionstabelle: Lektionen 16 und 17 verlinken jetzt zu ihrem Inhalt (vorher "Demnächst"); Repository-Bild auf `repo-thumbnailv3.png` aktualisiert.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: Lektionen 16 und 17 zur Lektion-für-Lektion-Anleitung und Lernpfaden hinzugefügt sowie eine Sektion "Validierung bereitgestellter Agenten mit Smoke Tests".
- **[AGENTS.md](./AGENTS.md)**: Lektionenzahl/Beschreibung aktualisiert (00–18), Smoke-Test Validierung Abschnitt hinzugefügt und Lektionen 16/17 Beispielbenennungen ergänzt.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Vorherige Lektion" verweist jetzt auf Lektion 17 (statt Lektion 15), Schließen der Kette.
- **Standardisierte Modellverweise auf nicht eingestellte Modelle.** Alle `gpt-4o` / `gpt-4o-mini` Verweise im Kurs (Dokumente, `.env.example`, Python/.NET-Notebooks und Beispiele) mit `gpt-4.1-mini` ersetzt — `gpt-4o` (alle Versionen) wird 2026 eingestellt. Lektion 16 Modell-Routing-Beispiel behält Klein/Groß-Kontrast mit `gpt-4.1-mini` (klein) und `gpt-4.1` (groß). Python-Notebooks wählen das Modell jetzt aus Umgebungsvariablen (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) statt einen Modellnamen hart zu kodieren.

### Anmerkungen und bekannte Einschränkungen

- **Nicht gegen live Azure ausgeführt.** Die neuen Lektionen-Notebooks sind edukative Beispieldateien; führen Sie sie gegen Ihre eigene Microsoft Foundry / Foundry Local Umgebung aus und validieren Sie sie. Der Smoke-Test Workflow erfordert, dass Sie den Agenten der Lektion bereitstellen und Azure OIDC-Geheimnisse (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) mit der **Azure AI User** Rolle im Foundry Projektkontext konfigurieren.
- **Lektion 17 ist lokal-only.** Sie hat keinen Foundry Responses Endpunkt, daher gilt die Smoke-Test Aktion nicht; validieren Sie sie, indem Sie das Notebook auf Ihrem Arbeitsplatzrechner ausführen.

## [Veröffentlicht] — 2026-07-06

Dieses Release migriert den Kurs zur **Azure OpenAI Responses API**, standardisiert Produktbezeichnungen auf **Microsoft Foundry** und das **Microsoft Agent Framework (MAF)**, stellt GitHub Models ein, aktualisiert SDK-Versionen und fügt neue Inhalte zu lokalen Modellen und zum Hosting anderer Frameworks auf Foundry hinzu.

### Hinzugefügt

- **Migrations-Skill** — Installierte die [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agenten-Fähigkeit (aus [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) unter `.agents/skills/`, inklusive Referenzen und Scanner-Skript.
- **Foundry Local (Modelle lokal ausführen)** — Neue Sektion "Alternative Provider: Foundry Local" in [00-course-setup/README.md](./00-course-setup/README.md) mit Installation (`winget` / `brew`), `foundry model run`, dem `foundry-local-sdk` und Anbindung von `FoundryLocalManager` ans Microsoft Agent Framework via `OpenAIChatClient`.
- **LangChain / LangGraph Agenten auf Microsoft Foundry hosten** — Neue Sektion in [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus ausführbares Beispiel [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) mit `langchain-azure-ai[hosting]` und `ResponsesHostServer` (das `/responses` Protokoll), basierend auf [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Neue Sektion "Real-World Example: Microsoft Project Opal" in [15-browser-use/README.md](./15-browser-use/README.md), die Opal als Agenten für Unternehmens computer-Nutzung darstellt und auf Kurskonzepte (Human-in-the-Loop, Vertrauen/Sicherheit, Planung, Skills) abbildet.
- **Zweites Python-Beispiel für Lektion 02** — Hinzugefügt [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (siehe "Geändert" — migriert vom früheren Semantic Kernel Notebook) und im Lektion-README verlinkt.
- Abschnitt Modelle und Anbieter zu [STUDY_GUIDE.md](./STUDY_GUIDE.md) hinzugefügt.

### Geändert

- **Chat Completions → Responses API (Python).** Beispiele, die das Modell direkt aufgerufen haben, wurden von Chat Completions auf die Responses API migriert (`client.responses.create(input=..., store=False)`, `resp.output_text`), unter Verwendung des `OpenAI` Clients gegen den stabilen Azure OpenAI `/openai/v1/` Endpunkt (ohne `api_version`). Betroffene Beispiele umfassen:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — der komplette Function-Calling Walkthrough (Tool-Schema wurde auf das Responses-Format abgeflacht, Tool-Ergebnisse als `function_call_output`, `max_output_tokens` etc. zurückgegeben).

- **GitHub-Modelle → Azure OpenAI.** GitHub-Modelle sind veraltet (Abschaltung **Juli 2026**) und unterstützen die Responses API nicht. Alle GitHub-Model-Codepfade wurden über Python- und .NET-Beispiele auf Azure OpenAI / Microsoft Foundry umgestellt:
  - Python: Lesson 08 Workflow-Notebooks (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + begleitende `.md`-Dokumente sowie die Lesson 08 dotNET Workflow-Notebooks/`.md` (`01`–`03`) verwenden jetzt `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` mit `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Das frühere `02-semantic-kernel.ipynb` wurde umgeschrieben, um das Microsoft Agent Framework mit Azure OpenAI (Responses API) zu verwenden, und in `02-python-agent-framework-azure-openai.ipynb` umbenannt.
- **Standardisierung auf `FoundryChatClient` + `as_agent`.** README- und Notebook-Code, der `AzureAIProjectAgentProvider` referenzierte, wurde auf das kanonische Muster aus Lesson 01 und den Framework-eigenen Beispielen vereinheitlicht: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` mit `provider.as_agent(...)`. Aktualisiert in den README-Dateien und Notebooks von Lesson 02–14 (z. B. Lesson 13 Speicher, alle Lesson 14 Notebooks, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Produktbenennung.** Überall im englischen Inhalt umbenannt:
  - „Azure AI Foundry“ / „Azure AI Studio“ → **Microsoft Foundry**
  - „Azure AI Agent Service“ → **Microsoft Foundry Agent Service**
  - (Unverändert: „Azure OpenAI“, „Azure AI Search“, „Azure AI Inference“ und Umgebungsvariablen-Namen.)
- **Abhängigkeiten** ([requirements.txt](../../requirements.txt)):
  - Festgelegt `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Festgelegt `openai>=1.108.1` (Mindestversion für die Responses API).
  - Entfernt `azure-ai-inference` (wurde nur von den migrierten GitHub-Modelle-Beispielen verwendet).
- **Umgebungskonfiguration** ([.env.example](../../.env.example)): GitHub-Modelle-Variablen (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) entfernt; hinzugefügt `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` und optional `AZURE_OPENAI_API_KEY`; Benennung auf Microsoft Foundry aktualisiert.
- **Dokumentation** — Aktualisiert [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) und [STUDY_GUIDE.md](./STUDY_GUIDE.md) entsprechend oben (Setup-Umgebungsvariablen, Verifikations-Snippet, Provider-Hinweise, Benennung).

### Entfernt

- GitHub-Modelle Onboarding-Schritte und Umgebungsvariablen aus den Setup-Dokumenten (durch Azure OpenAI / Microsoft Foundry ersetzt).

### Sicherheit / Datenschutz (öffentliche Freigabe bereinigt)

- Jupyter-Notebook-Ausgabe gelöscht, die eine echte **Azure-Abonnement-ID**, Ressourcengruppen- / Ressourcen-Namen und Bing-Verbindungs-ID sowie Entwickler-**lokale Dateipfade und Benutzernamen** enthielt, in:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Verifiziert, dass keine API-Schlüssel, Tokens, Abonnement-IDs oder persönliche Pfade mehr im getrackten englischen Inhalt vorhanden sind (die verbleibenden `GITHUB_TOKEN`-Referenzen sind der GitHub Actions Token in Workflows und der GitHub MCP Server PAT im Lesson 11 Setup – beide legitim und unabhängig von GitHub-Modelle).

### Hinweise und bekannte Einschränkungen

- **Nicht ausgeführt/kompiliert.** Dies sind edukative Beispiele, die auf API-/Namenskonsistenz aktualisiert wurden; sie wurden nicht gegen live Azure-Ressourcen ausgeführt und die .NET-Beispiele wurden in dieser Umgebung nicht kompiliert. Bitte gegen Ihre eigene Microsoft Foundry / Azure OpenAI Bereitstellung validieren.
- **Modell-Deployment muss die Responses API unterstützen.** Verwenden Sie ein Deployment wie `gpt-4.1-mini`, `gpt-4.1` oder ein `gpt-5.x` Modell. Ältere Modelle unterstützen die Kernfunktionen der Responses API, aber nicht alle Features.
- **Agent-Framework-Version.** Die Beispiele zielen auf die neueste MAF Version (`>=1.10.0`) ab. Der kanonische Agent-Erzeugungsaufruf ist `client.as_agent(...)`; APIs wurden gegen die veröffentlichte Dokumentation des Frameworks und eines installierten Builds validiert. Wenn Sie eine andere Version verwenden, prüfen Sie die Methodenverfügbarkeit (`as_agent` vs. `create_agent`).
- **Lesson 08 Workflow-Notebook 04** behält absichtlich `AzureAIAgentClient` (aus `agent-framework-azure-ai`), da es Microsoft Foundry Agent Service gehostete Tools nutzt (Bing Grounding, Code-Interpreter); es basiert bereits auf Responses.
- **.NET Standard-Deployment.** Zwei Lesson 08 dotNET Workflow-Beispiele hatten zuvor ein festcodiertes spezifisches Modell; sie verwenden jetzt standardmäßig `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Wenn ein Beispiel multimodale/visuelle Eingaben benötigt, setzen Sie `AZURE_OPENAI_DEPLOYMENT` auf ein geeignetes Modell.
- **Foundry Local** stellt einen OpenAI-kompatiblen **Chat Completions** Endpunkt bereit und ist für lokale Entwicklung gedacht; verwenden Sie Azure OpenAI / Microsoft Foundry für den vollständigen Responses API Funktionsumfang.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->