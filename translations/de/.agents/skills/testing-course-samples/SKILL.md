---
name: testing-course-samples
---
# Testen der Kursbeispiele

Überprüfen Sie, dass die Lernnotebooks und Codebeispiele mit einer aktiven
Microsoft Foundry / Azure OpenAI-Umgebung ausgeführt werden können. Das Repository enthält einen Runner unter
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), der
jedes Python-Notebook kopflos ausführt und eine PASS/FAIL-Matrix ausgibt.

## Wann verwenden
- "Alle Notebooks / Beispiele gegen mein Azure-Abonnement validieren."
- "Rauchtest des Kurses nach Paket-Upgrades oder Modelländerungen."
- "Welche Lektionen bestehen / scheitern noch live?"

Verwenden Sie diesen Test **nicht** für den KI-Rauchtest GitHub Action (der *bereitgestellte*
gehostete Agenten validiert — siehe [`tests/README.md`](../../../tests/README.md)). Dieses Tool
führt die Notebooks lokal aus.

## Voraussetzungen (zuerst prüfen)
1. **Python 3.12+** mit Kursabhängigkeiten: `python -m pip install -r requirements.txt`
   plus den Executor: `python -m pip install nbconvert ipykernel`.
2. **`.env` im Repo-Stammverzeichnis** (kopieren Sie von [`.env.example`](../../../../../.env.example)) mit mindestens:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry-Projekt-Endpunkt
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — eine nicht veraltete Bereitstellung (z.B. `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) und `AZURE_OPENAI_DEPLOYMENT`
     für Lektionen, die Azure OpenAI direkt aufrufen (Lektion 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** abgeschlossen — Beispiele authentifizieren sich mit `AzureCliCredential` (Entra ID, schlüsselextern).
4. Verifizieren Sie, dass die Modellbereitstellung existiert:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Validierung ausführen
```powershell
# Alle Python-Notebooks (überspringt .NET, .venv, site-packages, Übersetzungen, Skill-Assets)
pwsh scripts/validate-notebooks.ps1

# Eine einzelne Lektion, mit einem längeren Timeout pro Zelle
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Nur auflisten, was ausgeführt würde (keine Ausführung)
pwsh scripts/validate-notebooks.ps1 -List

# Expliziter Interpreter (wenn `python` nicht im PATH ist, z.B. Windows Store-Alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Das Skript schreibt ausgeführte Kopien, Pro-Notebook-Protokolle und `results.json` nach
`$env:TEMP\aiab-nbval` und beendet sich mit der Anzahl der Fehler.

## Ergebnisse interpretieren
- `PASS` — das Notebook wurde durchgehend ohne Fehler in Zellen ausgeführt.
- `FAIL` — die erste `*Error` / `*Exception`-Zeile wird angezeigt; öffnen Sie die passende
  `log_*.txt` im Ausgabeverzeichnis für den vollständigen Traceback.
- Der Fehler eines einzelnen Notebooks ist durch `-Timeout` (pro Zelle) begrenzt, sodass eine blockierte
  Human-in-the-Loop-Zelle als `StdinNotImplementedError` erscheint, anstatt zu hängen.

## Lektionen, die zusätzliche Ressourcen benötigen (werden ohne diese voraussichtlich fehlschlagen)
| Lektion | Zusätzliche Voraussetzung |
|--------|-------------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, Schlüssel) — hat eine In-Memory-Fallback-Option |
| 11 MCP / GitHub | GitHub MCP-Server + PAT |
| 13 Memory (cognee) | `cognee` konfiguriert mit einem Modellanbieter |
| 15 Browser-Nutzung | Playwright-Browser installiert (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 Lokaler Agent | Foundry Local Runtime + heruntergeladenes Qwen-Modell (auf Gerät, keine Cloud) |
| `*-dotnet-*` Notebooks | .NET Interactive Kernel (standardmäßig ausgeschlossen; verwenden Sie `-IncludeDotnet`) |

## Rückmeldung geben
Fassen Sie als PASS/FAIL-Tabelle zusammen, gruppiert nach Lektion. Trennen Sie echte Regressionen
(Code-/Konfigurationsfehler, die behoben werden müssen) von Umgebungsproblemen (fehlender Search/Foundry Local/PAT),
und geben Sie die fehlerhaften `log_*.txt` für jede echte Fehlfunktion an.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->