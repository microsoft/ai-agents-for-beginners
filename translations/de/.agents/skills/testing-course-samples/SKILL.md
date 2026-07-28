---
name: testing-course-samples
---
# Testen der Kursbeispiele

Überprüfen Sie, ob die Lektion-Notebooks und Codebeispiele mit einer aktiven
Microsoft Foundry / Azure OpenAI-Installation ausgeführt werden können. Das Repository
enthält einen Runner unter [`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), der
jedes Python-Notebook kopflos ausführt und eine PASS/FAIL-Matrix ausgibt.

## Wann verwenden
- "Alle Notebooks / Beispiele gegen mein Azure-Abonnement validieren."
- "Smoke-Test des Kurses nach Paket-Upgrades oder Modelländerungen."
- "Welche Lektionen bestehen / scheitern live noch?"

Verwenden Sie dies **nicht** für die AI Smoke Test GitHub Action (die *bereitgestellte*
gehostete Agenten validiert – siehe [`tests/README.md`](../../../tests/README.md)). Dieses Tool
führt die Notebooks lokal aus.

## Voraussetzungen (zuerst prüfen)
1. **Python 3.12+** mit Kursabhängigkeiten: `python -m pip install -r requirements.txt`
   plus den Executor: `python -m pip install nbconvert ipykernel`.
2. **`.env` im Repo-Stammverzeichnis** (kopieren von [`.env.example`](../../../../../.env.example)) mit mindestens:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry-Projekt-Endpunkt
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — eine nicht veraltete Bereitstellung (z.B. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) und `AZURE_OPENAI_DEPLOYMENT`
     für Lektionen, die Azure OpenAI direkt verwenden (Lektion 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** abgeschlossen — Beispiele authentifizieren sich mit `AzureCliCredential` (Entra ID, schlüssellos).
4. Verifizieren Sie, dass die Modell-Bereitstellung existiert:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Ausführen der Validierung
```powershell
# Alle Python-Notebooks (überspringt .NET, .venv, site-packages, Übersetzungen, Skill-Assets)
pwsh scripts/validate-notebooks.ps1

# Eine einzelne Lektion, mit einer längeren Zeitüberschreitung pro Zelle
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Nur auflisten, was ausgeführt würde (keine Ausführung)
pwsh scripts/validate-notebooks.ps1 -List

# Expliziter Interpreter (wenn `python` nicht im PATH ist, z.B. Windows Store Alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Das Skript schreibt ausgeführte Kopien, Pro-Notebook-Protokolle und `results.json` nach
`$env:TEMP\aiab-nbval` und beendet sich mit der Anzahl der Fehler.

Vorübergehende Fehler (geteilte Abonnement-HTTP 429 Rate Limits, ein gelegentlicher
`AzureCliCredential` Token-Fehler oder ein Timeout) werden automatisch erneut versucht
(`-Retries`, Standard 2, mit `-RetryDelaySeconds` Verzögerung, Standard 20). Wenn eine
Modell-Bereitstellung regelmäßig 429-Fehler verursacht, prüfen Sie die GlobalStandard
TPM-Quote des Abonnements (`az cognitiveservices usage list -l <region>`) — die Erhöhung der Kapazität
einer einzelnen Bereitstellung hilft nicht, wenn die *Abonnement*-Quote erschöpft ist.

## Ergebnisse interpretieren
- `PASS` — das Notebook lief durchgängig ohne Zellfehler.
- `FAIL` — die erste `*Error` / `*Exception` Zeile wird angezeigt; öffnen Sie die zugehörige
  `log_*.txt` im Ausgabeverzeichnis für den vollständigen Traceback.
- Ein einzelnes Notebook-Fehlschlagen ist durch `-Timeout` (pro Zelle) begrenzt, sodass eine
  hängende human-in-the-loop Zelle als `StdinNotImplementedError` statt hängend angezeigt wird.

## Lektionen, die zusätzliche Ressourcen benötigen (erwarten das Scheitern ohne diese)
| Lektion | Zusätzliche Anforderung |
|--------|-----------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, Schlüssel) — hat einen In-Memory-Fallback |
| 11 MCP / GitHub | GitHub MCP Server + PAT |
| 13 memory (cognee) | `cognee` konfiguriert mit einem Modellanbieter |
| 15 browser-use | Playwright-Browser installiert (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local Runtime + ein heruntergeladenes Qwen-Modell (lokal, kein Cloud) |
| `*-dotnet-*` Notebooks | .NET Interactive Kernel (standardmäßig ausgeschlossen; verwenden Sie `-IncludeDotnet`) |

## Rückmeldung
Fassen Sie die Ergebnisse als PASS/FAIL-Tabelle nach Lektionen zusammen. Trennen Sie echte Regressionen
(Code-/Konfigurationsfehler, die zu beheben sind) von Umgebungsproblemen (fehlende Search/Foundry Local/PAT),
und verweisen Sie bei jedem echten Fehler auf die fehlerhaften `log_*.txt`.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->