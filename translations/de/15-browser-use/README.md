# Erstellung von Computer Use Agents (CUA)

Computer Use Agents können mit Websites genauso interagieren wie eine Person: indem sie einen Browser öffnen, die Seite inspizieren und die nächstbeste Aktion basierend auf dem, was sie sehen, ausführen. In diesem Unterricht bauen Sie einen Browser-Automatisierungsagenten, der Airbnb durchsucht, strukturierte Angebotsdaten extrahiert und den günstigsten Aufenthalt in Stockholm ermittelt.

Die Lektion kombiniert Browser-Use für KI-gesteuerte Navigation, Playwright und das Chrome DevTools Protocol (CDP) für Browsersteuerung, Azure OpenAI für visionbasiertes Schlussfolgern und Pydantic für strukturierte Extraktion.

## Einführung

Diese Lektion behandelt:

- Verständnis, wann Computer Use Agents gegenüber reiner API-Automatisierung besser geeignet sind
- Kombination von Browser-Use mit Playwright und CDP für zuverlässiges Browser-Lifecycle-Management
- Nutzung von Azure OpenAI Vision und strukturierter Pydantic-Ausgabe zur Extraktion von Angebotsdaten aus dynamischen Webseiten
- Entscheidung, wann ein agentenzentrierter, akteursorientierter oder hybrider Browser-Automatisierungs-Workflow sinnvoll ist

## Lernziele

Nach Abschluss dieser Lektion wissen Sie, wie Sie:

- Browser-Use mit Azure OpenAI und Playwright konfigurieren
- Einen Browser-Automatisierungsworkflow erstellen, der eine echte Website navigiert und dynamische UI-Elemente handhabt
- Typisierte Ergebnisse aus sichtbarem Seiteninhalt extrahieren und in nachgelagerte Geschäftslogik umwandeln
- Zwischen Agent- und Actor-Pattern je nach Vorhersagbarkeit der Browseraufgabe wählen

## Code-Beispiel

Diese Lektion beinhaltet ein Notebook-Tutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Startet eine Chrome-Session über CDP, sucht auf Airbnb nach Angeboten in Stockholm, extrahiert Preise mit Browser-Use Vision und gibt die günstigste Option als strukturierte Daten zurück.

## Voraussetzungen

- Python 3.12+
- Azure OpenAI-Bereitstellung in Ihrer Umgebung konfiguriert
- Chrome oder Chromium lokal installiert
- Playwright-Abhängigkeiten installiert
- Grundkenntnisse in asynchronem Python

## Einrichtung

Installieren Sie die im Notebook verwendeten Pakete:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Stellen Sie die Azure OpenAI-Umgebungsvariablen ein, die vom Notebook verwendet werden:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Optional: Standardmäßig wird die neueste API-Version verwendet, wenn sie weggelassen wird
AZURE_OPENAI_API_VERSION=...
```

## Architekturübersicht

Das Notebook demonstriert einen hybriden Browser-Automatisierungsworkflow:

1. Chrome startet mit aktiviertem CDP, sodass sowohl Playwright als auch Browser-Use die gleiche Browsersitzung teilen können.
2. Ein Browser-Use-Agent übernimmt offene Navigationsaufgaben wie das Öffnen von Airbnb, das Schließen von Pop-ups und die Suche nach Stockholm.
3. Die aktive Seite wird mit einem strukturierten Pydantic-Schema inspiziert, um Angebotstitel, Übernachtungspreise, Bewertungen und URLs zu extrahieren.
4. Python-Logik vergleicht die extrahierten Angebote und hebt das günstigste Ergebnis hervor.

Dieser Ansatz bewahrt die flexible, visionbasierte Schlussfolgerung, für die Browser-Use bekannt ist, bietet jedoch gleichzeitig deterministische Browsersteuerung, wenn Sie sie benötigen.

## Wichtige Erkenntnisse und Best Practices

### Wann Agent vs Actor verwenden

| Szenario | Agent verwenden | Actor verwenden |
|----------|-----------------|------------------|
| Dynamische Layouts | Ja, KI passt sich an Seitenänderungen an | Nein, fragile Selektoren können brechen |
| Bekannte Struktur | Nein, ein Agent ist langsamer als direkte Steuerung | Ja, schnell und präzise |
| Elemente finden | Ja, natürliche Sprache funktioniert gut | Nein, exakte Selektoren sind erforderlich |
| Timing-Steuerung | Nein, weniger vorhersehbar | Ja, vollständige Kontrolle über Wartezeiten und Wiederholungen |
| Komplexe Workflows | Ja, handhabt unerwartete UI-Zustände | Nein, erfordert explizite Verzweigungen |

### Browser-Use Best Practices

1. Beginnen Sie mit einem Agenten zur Erkundung und dynamischen Navigation.
2. Wechseln Sie zur direkten Seitensteuerung, wenn die Interaktion vorhersehbar wird.
3. Verwenden Sie strukturierte Ausgabemodelle, damit extrahierte Daten validiert und typ-sicher sind.
4. Fügen Sie nach Aktionen, die sichtbare UI-Änderungen auslösen, gezielt Verzögerungen ein.
5. Machen Sie während der Iteration Screenshots, damit Fehler leichter debuggt werden können.
6. Erwarten Sie, dass Websites sich ändern, und entwerfen Sie Ausweichstrategien für Pop-ups und Layoutverschiebungen.
7. Kombinieren Sie Agent- und Actor-Pattern, um sowohl Flexibilität als auch Präzision zu erhalten.

### Sicherheitshinweise für Browser-Agenten

Browser-Agenten arbeiten auf Live-Websites, daher benötigen sie engere Grenzen als ein Skript, das nur eine bekannte API aufruft. Bevor Sie von einer Notebook-Demo zu einem echten Workflow wechseln, definieren Sie Kontrollen darüber, was der Agent sehen, klicken und absenden kann.

1. **Begrenzen Sie die Browsing-Umgebung.** Führen Sie den Agenten in einem dedizierten Browserprofil oder einer Sandbox aus und beschränken Sie ihn auf die für die Aufgabe erforderlichen Domains.
2. **Trennen Sie Beobachtung und Aktion.** Lassen Sie den Agenten zuerst suchen, lesen und Daten extrahieren; eine explizite Genehmigungsstufe soll erforderlich sein, bevor Formulare abgeschickt, Nachrichten gesendet, Reisen gebucht, Käufe getätigt, Datensätze gelöscht oder Kontoeinstellungen geändert werden.
3. **Halten Sie Geheimnisse aus Eingabeaufforderungen und Protokollen heraus.** Platzieren Sie keine Passwörter, Zahlungsinformationen, Sitzungscookies oder rohe persönliche Daten im Modellkontext. Übergeben Sie die Authentifizierung dem Benutzer und schwärzen Sie sensible Felder in Protokollen.
4. **Behandeln Sie Seiteninhalte als nicht vertrauenswürdige Eingaben.** Eine Website kann Anweisungen enthalten, die für den Agenten bestimmt sind, nicht für den Benutzer. Der Agent sollte Seitentexte ignorieren, die ihn auffordern, sein Ziel zu ändern, Daten preiszugeben, Schutzmechanismen zu deaktivieren oder nicht verwandte Seiten zu besuchen.
5. **Verwenden Sie deterministische Prüfungen bei riskanten Schritten.** Überprüfen Sie die aktuelle URL, den Seitentitel, das ausgewählte Element, Preise, Empfänger und Aktionszusammenfassungen programmatisch, bevor der Benutzer den letzten Schritt genehmigt.
6. **Setzen Sie Budgets und Abbruchbedingungen.** Begrenzen Sie die Anzahl der Aktionen, Wiederholungen, Tabs und Minuten, die der Agent verwenden darf. Stoppen Sie, wenn der Seitenstatus unklar ist, anstatt weiterzuklicken.
7. **Zeichnen Sie nützliche Beweise auf, nicht alles.** Bewahren Sie Aktionszusammenfassungen, Zeitstempel, URLs, Beschreibungen der ausgewählten Elemente und Screenshot-Referenzen auf, sodass Fehler überprüft werden können, ohne unnötigen sensiblen Seiteninhalt zu speichern.

Im Airbnb-Beispiel ist der sichere Standard, Angebote zu suchen und Preise zu extrahieren. Anmelden, einen Gastgeber kontaktieren oder eine Buchung abschließen sollte eine vom Benutzer genehmigte separate Aktion sein.

### Anwendungen in der Praxis

- Reisebuchungen und Preisüberwachung
- Preisvergleiche und Verfügbarkeitsprüfungen im E-Commerce
- Strukturierte Extraktion von dynamischen Webseiten
- Vision-basierte UI-Tests und Verifikation
- Webseitenüberwachung und Benachrichtigungen
- Intelligentes Ausfüllen von Formularen in mehrstufigen Abläufen

## Praxisbeispiel: Microsoft Project Opal

Der in dieser Lektion erstellte Agent ist eine kleine, lokale Version eines **Computer Use Agent (CUA)** – ein Programm, das einen Browser genauso steuert wie ein Mensch. Microsoft bringt diese Idee mit **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)** in Microsoft 365 Copilot unter die Unternehmen.

Mit Project Opal beschreiben Sie eine Aufgabe, und der Agent arbeitet in Ihrem Auftrag unter Verwendung von **Computer Use auf einem sicheren Windows 365 Cloud-PC**, der über die browserbasierten Anwendungen, Sites und Daten Ihrer Organisation hinweg operiert. Er arbeitet **asynchron im Hintergrund**, und Sie können die Arbeit jederzeit lenken oder übernehmen. Beispielaufgaben umfassen:

- Verwaltung von Anfragen zur Sicherheitsgruppenmitgliedschaft
- Sammlung und Validierung von Prüfnachweisen für Compliance-Überprüfungen
- Klassifizierung von IT-Vorfällen (Aktualisierung des Ticketstatus, Zuweisung von Verantwortlichen, Schließen von Duplikaten)
- Zusammenstellung von Excel-Daten zu einem Financial-Close-Bericht

Opal ist ein nützlicher Referenzpunkt dafür, wie ein **Produktionsreifer, vertrauenswürdiger** Computer Use Agent aussieht – und verstärkt Konzepte aus früheren Lektionen:

| Konzept in diesem Kurs | Wie Project Opal es anwendet |
|------------------------|-----------------------------|
| **Human-in-the-loop** (Lektion 06) | Opal pausiert für Login-Daten, sensible Informationen oder unklare Anweisungen und gibt niemals Passwörter ein oder sendet Formulare ohne ausdrückliche Bestätigung. Sie können während der Aufgabe *die Kontrolle übernehmen* und *zurückgeben*. |
| **Vertrauenswürdige & sichere Agenten** (Lektionen 06 & 18) | Läuft isoliert auf einem Windows 365 Cloud-PC, ist standardmäßig browserbasiert (anderer Computerzugriff wird über Intune blockiert), verwendet *Ihre* Identität, sodass nur autorisierte Zugriffe möglich sind, und protokolliert jede Aktion zur Auditierbarkeit. |
| **Planung & Metakognition** (Lektionen 07 & 09) | Opal erstellt zuerst einen Plan für die Aufgabe, überwacht dann in jedem Schritt ihre eigene Logik und pausiert, wenn es verdächtige Aktivitäten erkennt. |
| **Wiederverwendbare Fähigkeiten/Tools** (Lektion 04) | **Skills** erlauben es Ihnen, Anweisungen für wiederholbare Aufgaben zu schreiben (importiert aus einer `.md`-Datei oder mit Opal erstellt) und diese in verschiedenen Konversationen wiederzuverwenden. |

> **Verfügbarkeit:** Project Opal ist derzeit im [Frontier Early Access Program](https://adoption.microsoft.com/copilot/frontier-program/) mit einem Microsoft 365 Copilot-Abonnement für Nutzer verfügbar, und Ihr Administrator muss die Einrichtung abschließen. Da es eine experimentelle Frontier-Funktion ist, können sich Fähigkeiten im Laufe der Zeit ändern.

## Zusätzliche Ressourcen

- [Erste Schritte mit Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright-Integrationsvorlage](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use Actor-Parameter und Inhaltsextraktion](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kurs-Setup](../00-course-setup/README.md)

## Vorherige Lektion

[Erkundung des Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Nächste Lektion

[Bereitstellung skalierbarer Agenten](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->