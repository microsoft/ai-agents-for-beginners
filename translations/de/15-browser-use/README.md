# Erstellung von Computer Use Agents (CUA)

Computer Use Agents können mit Websites auf dieselbe Weise interagieren wie eine Person: indem sie einen Browser öffnen, die Seite inspizieren und die nächste beste Aktion basierend auf dem, was sie sehen, ausführen. In dieser Lektion erstellen Sie einen Browser-Automatisierungsagenten, der Airbnb durchsucht, strukturierte Angebotsdaten extrahiert und den günstigsten Aufenthalt in Stockholm ermittelt.

Die Lektion kombiniert Browser-Use für KI-gesteuerte Navigation, Playwright und Chrome DevTools Protocol (CDP) für die Browsersteuerung, Azure OpenAI für vision-aktiviertes Schließen von Zusammenhängen und Pydantic für strukturierte Extraktion.

## Einführung

Diese Lektion behandelt:

- Verständnis, wann Computer Use Agents besser geeignet sind als reine API-Automatisierung
- Kombination von Browser-Use mit Playwright und CDP für zuverlässiges Browser-Lifecycle-Management
- Verwendung von Azure OpenAI Vision und strukturierter Pydantic-Ausgabe zur Extraktion von Angebotsdaten aus dynamischen Webseiten
- Entscheidung, wann ein agentenorientierter, akteursorientierter oder hybrider Browser-Automatisierungsworkflow verwendet wird

## Lernziele

Nach Abschluss dieser Lektion wissen Sie, wie man:

- Browser-Use mit Azure OpenAI und Playwright konfiguriert
- Einen Browser-Automatisierungsworkflow erstellt, der eine reale Website navigiert und dynamische UI-Elemente handhabt
- Typisierte Ergebnisse aus sichtbarem Seiteninhalt extrahiert und sie in nachgelagerte Geschäftslogik umwandelt
- Basierend auf der Vorhersagbarkeit der Browseraufgabe zwischen Agent- und Schauspielermustern wählt

## Codebeispiel

Diese Lektion enthält ein Notebook-Tutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Startet eine Chrome-Sitzung über CDP, durchsucht Airbnb nach Einträgen in Stockholm, extrahiert Preise mit Browser-Use Vision und gibt die günstigste Option als strukturierte Daten zurück.

## Voraussetzungen

- Python 3.12+
- Azure OpenAI Deployment in Ihrer Umgebung konfiguriert
- Chrome oder Chromium lokal installiert
- Playwright-Abhängigkeiten installiert
- Grundkenntnisse in asynchronem Python

## Einrichtung

Installieren Sie die im Notebook verwendeten Pakete:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Legen Sie die von dem Notebook verwendeten Azure OpenAI-Umgebungsvariablen fest:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Optional: Standardmäßig die neueste API-Version, wenn weggelassen
AZURE_OPENAI_API_VERSION=...
```

## Architekturübersicht

Das Notebook demonstriert einen hybriden Browser-Automatisierungsworkflow:

1. Chrome startet mit aktiviertem CDP, sodass sowohl Playwright als auch Browser-Use dieselbe Browsersitzung teilen können.
2. Ein Browser-Use-Agent übernimmt offene Navigationsaufgaben wie das Öffnen von Airbnb, das Schließen von Pop-ups und die Suche nach Stockholm.
3. Die aktive Seite wird mit einem strukturierten Pydantic-Schema inspiziert, um Angebotsüberschriften, Übernachtungspreise, Bewertungen und URLs zu extrahieren.
4. Python-Logik vergleicht die extrahierten Angebote und hebt das günstigste Ergebnis hervor.

Dieser Ansatz bewahrt das flexible, auf Vision basierende Schließen von Zusammenhängen, für das Browser-Use gut ist, während Sie dennoch bei Bedarf eine deterministische Browsersteuerung erhalten.

## Wichtige Erkenntnisse und bewährte Methoden

### Wann Agent vs. Schauspieler verwenden

| Szenario | Agent verwenden | Schauspieler verwenden |
|----------|-----------------|------------------------|
| Dynamische Layouts | Ja, KI passt sich gut an Seitenänderungen an | Nein, fragile Selektoren können brechen |
| Bekannte Struktur | Nein, ein Agent ist langsamer als direkte Steuerung | Ja, schnell und präzise |
| Elemente finden | Ja, natürliche Sprache funktioniert gut | Nein, genaue Selektoren sind erforderlich |
| Timing-Steuerung | Nein, weniger vorhersehbar | Ja, volle Kontrolle über Wartezeiten und Wiederholungen |
| Komplexe Workflows | Ja, handhabt unerwartete UI-Zustände | Nein, erfordert explizite Verzweigungen |

### Beste Praktiken für Browser-Use

1. Beginnen Sie mit einem Agenten für Erkundung und dynamische Navigation.
2. Wechseln Sie zur direkten Seitensteuerung, wenn die Interaktion vorhersehbar wird.
3. Verwenden Sie strukturierte Ausgabemodelle, damit extrahierte Daten validiert und typsicher sind.
4. Fügen Sie nach Aktionen, die sichtbare UI-Änderungen auslösen, strategisch Verzögerungen hinzu.
5. Erstellen Sie während der Iteration Screenshots, damit Fehler leichter zu debuggen sind.
6. Erwarten Sie, dass sich Websites ändern, und entwerfen Sie Backup-Strategien für Pop-ups und Layoutverschiebungen.
7. Kombinieren Sie Agent- und Schauspielermuster, um sowohl Flexibilität als auch Präzision zu erhalten.

### Sicherheitsrichtlinien für Browser-Agenten

Browser-Agenten arbeiten auf Live-Websites, daher benötigen sie engere Grenzen als ein Skript, das nur eine bekannte API aufruft. Bevor Sie von einer Notebook-Demo zu einem echten Workflow wechseln, definieren Sie die Kontrollen darüber, was der Agent sehen, klicken und absenden darf.

1. **Begrenzen Sie die Browser-Umgebung.** Führen Sie den Agenten in einem dedizierten Browserprofil oder Sandbox aus und beschränken Sie ihn auf die für die Aufgabe erforderlichen Domains.
2. **Trennen Sie Beobachtung von Aktion.** Lassen Sie den Agenten erst suchen, lesen und Daten extrahieren; verlangen Sie einen ausdrücklichen Genehmigungsschritt, bevor Formulare abgesendet, Nachrichten gesendet, Reisen gebucht, Einkäufe getätigt, Datensätze gelöscht oder Kontoeinstellungen geändert werden.
3. **Halten Sie Geheimnisse aus Eingabeaufforderungen und Protokollen fern.** Platzieren Sie keine Passwörter, Zahlungsdetails, Sitzungscookies oder Roh-Personendaten im Modellkontext. Lassen Sie den Benutzer die Authentifizierung übernehmen und schwärzen Sie sensible Felder aus Protokollen.
4. **Behandeln Sie Seiteninhalt als nicht vertrauenswürdige Eingabe.** Eine Website kann Anweisungen enthalten, die an den Agenten gerichtet sind, nicht an den Benutzer. Der Agent sollte Seitentext ignorieren, der ihn auffordert, das Ziel zu ändern, Daten offenzulegen, Schutzmechanismen zu deaktivieren oder zu nicht verwandten Seiten zu navigieren.
5. **Verwenden Sie deterministische Prüfungen bei riskanten Schritten.** Überprüfen Sie aktuelle URL, Seitentitel, ausgewähltes Element, Preis, Empfänger und Aktionsübersicht programmgesteuert, bevor Sie den Benutzer um Freigabe des letzten Schrittes bitten.
6. **Setzen Sie Budgets und Stopbedingungen.** Begrenzen Sie die Anzahl der Aktionen, Wiederholungen, Tabs und Minuten, die der Agent verwenden darf. Stoppen Sie, wenn der Seitenzustand mehrdeutig ist, anstatt weiter zu klicken.
7. **Protokollieren Sie nützliche Beweise, aber nicht alles.** Bewahren Sie Aktionsübersichten, Zeitstempel, URLs, Beschreibungen ausgewählter Elemente und Screenshot-Verweise auf, damit Fehlschläge überprüft werden können, ohne unnötigen sensiblen Seiteninhalt zu speichern.

Im Airbnb-Beispiel ist die sichere Voreinstellung, Angebote zu suchen und Preise zu extrahieren. Anmeldung, Kontaktaufnahme mit einem Gastgeber oder Abschluss einer Buchung sollten separate, vom Benutzer genehmigte Aktionen sein.

### Anwendungen in der Praxis

- Reisebuchung und Preisüberwachung
- Preisvergleiche und Verfügbarkeitsprüfungen im E-Commerce
- Strukturierte Extraktion von dynamischen Websites
- Visionsbasierte UI-Tests und Verifikation
- Website-Überwachung und Alarmierung
- Intelligentes Ausfüllen von Formularen über mehrstufige Abläufe

## Praxisbeispiel: Microsoft Project Opal

Der Agent, den Sie in dieser Lektion erstellen, ist eine kleine, lokale Version eines **Computer Use Agent (CUA)** — ein Programm, das einen Browser so steuert, wie es eine Person tun würde. Microsoft bringt diese Idee mit **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)** in die Unternehmenswelt, eine Funktion in Microsoft 365 Copilot.

Mit Project Opal beschreiben Sie eine Aufgabe, und der Agent arbeitet in Ihrem Namen unter Verwendung von **Computer Use auf einem sicheren Windows 365 Cloud-PC**, der über die browserbasierten Anwendungen, Webseiten und Daten Ihrer Organisation operiert. Er arbeitet **asynchron im Hintergrund**, und Sie können die Arbeit jederzeit anleiten oder die Kontrolle übernehmen. Beispielaufgaben sind:

- Verwaltung von Sicherheitsgruppenmitgliedschaftsanfragen
- Sammlung und Validierung von Prüfungsnachweisen für Compliance-Prüfungen
- Priorisierung von IT-Vorfällen (Ticketstatus aktualisieren, Zuständige zuweisen, Duplikate schließen)
- Zusammenstellung von Excel-Daten zu einem Abschlussbericht

Opal ist eine nützliche Referenz dafür, wie ein **produktionsreifer, vertrauenswürdiger** Computer Use Agent aussieht – und bestärkt die Konzepte aus früheren Lektionen:

| Konzept in diesem Kurs | Wie Project Opal es anwendet |
|------------------------|-----------------------------|
| **Human-in-the-loop** (Lektion 06) | Opal hält für Anmeldeinformationen, sensible Daten oder mehrdeutige Anweisungen inne und gibt niemals Passwörter ein oder sendet Formulare ohne explizite Bestätigung. Sie können *Die Kontrolle übernehmen* und *Die Kontrolle zurückgeben* mitten in der Aufgabe. |
| **Vertrauenswürdige & sichere Agenten** (Lektionen 06 & 18) | Läuft in einem isolierten Windows 365 Cloud-PC, ist standardmäßig browsergebunden (andere Computerzugriffe blockiert, über Intune erzwungen), verwendet *Ihre* Identität, so dass es nur auf berechtigte Ressourcen zugreift, und protokolliert jede Aktion für die Nachvollziehbarkeit. |
| **Planung & Metakognition** (Lektionen 07 & 09) | Opal erstellt zuerst einen Plan für die Aufgabe, überwacht dann sein eigenes Schließen von Zusammenhängen bei jedem Schritt und hält an, wenn verdächtige Aktivitäten erkannt werden. |
| **Wiederverwendbare Fähigkeiten / Werkzeuge** (Lektion 04) | **Skills** ermöglichen es Ihnen, Anweisungen für wiederholbare Aufgaben zu schreiben (importiert aus einer `.md`-Datei oder in Opal erstellt) und diese in mehreren Gesprächen wiederzuverwenden. |

> **Verfügbarkeit:** Project Opal ist derzeit für Nutzer im [Frontier Early Access Program](https://adoption.microsoft.com/copilot/frontier-program/) mit einem Microsoft 365 Copilot Abonnement verfügbar, und Ihr Administrator muss die Einrichtung abschließen. Da es sich um eine experimentelle Frontier-Funktion handelt, können sich die Fähigkeiten im Laufe der Zeit ändern.

## Wissensprüfung

Testen Sie Ihr Verständnis, bevor Sie zur nächsten Lektion übergehen.

**1. Wann ist ein browserbasierter Computer Use Agent besser geeignet als ein reiner API-Workflow?**

<details>
<summary>Antwort</summary>

Verwenden Sie einen Browser-Agenten, wenn die Aufgabe davon abhängt, was in einer Web-UI sichtbar ist, die Seite die benötigte API nicht bereitstellt oder die Seite häufig genug geändert wird, dass feste API- oder Selektor-Logik unzuverlässig wäre. Wenn eine stabile API für dieselbe Aufgabe existiert, bevorzugen Sie die API, da sie in der Regel schneller, leichter zu testen und sicherer ist.
</details>

**2. Welche Teile sollte der Agent in einem hybriden Workflow übernehmen, und welche Teile sollte direkter Playwright-Code übernehmen?**

<details>
<summary>Antwort</summary>

Lassen Sie den Agenten offene Navigation und dynamische UI-Zustände übernehmen, wie das Finden der richtigen Seite oder das Schließen unerwarteter Pop-ups. Wechseln Sie zur direkten Playwright-Steuerung, wenn die Seitenstruktur bekannt ist und die Aktion Präzision, Wiederholungen, Wartezeiten oder deterministische Validierung erfordert.
</details>

**3. Das Airbnb-Beispiel findet ein Angebot, das der Nutzer möglicherweise buchen möchte. Was sollte geschehen, bevor der Workflow sich anmeldet, einen Gastgeber kontaktiert oder eine Buchung abschließt?**

<details>
<summary>Antwort</summary>

Der Workflow sollte pausieren und eine ausdrückliche Benutzerfreigabe einholen. Vor der Anfrage sollte er eine klare Zusammenfassung des ausgewählten Angebots, der aktuellen URL, des Preises, der Daten und der beabsichtigten Aktion anzeigen. Suche und Preisextraktion können autonom erfolgen; Konto-Zugriff, Nachrichten, Einkäufe und Buchungen sollten vom Benutzer genehmigt werden.
</details>

**4. Eine Webseite fordert den Agenten auf, seine ursprünglichen Anweisungen zu ignorieren, eine andere Seite zu besuchen und gespeicherte Anmeldeinformationen offenzulegen. Wie sollte der Agent diesen Text behandeln?**

<details>
<summary>Antwort</summary>

Behandeln Sie ihn als nicht vertrauenswürdigen Seiteninhalt, nicht als Entwickler- oder Benutzeranweisung. Der Agent sollte innerhalb der erlaubten Domain und des Aufgabenumfangs bleiben, die Offenlegung von Geheimnissen verweigern und Seite-Text, der das Ziel ändert, Schutzmechanismen deaktiviert oder ihn zu nicht verwandten Sites schickt, ignorieren.
</details>

**5. Welche Nachweise sind nützlich, wenn ein Browser-Agent läuft, und was sollte vermieden werden?**

<details>
<summary>Antwort</summary>

Bewahren Sie Aktionsübersichten, Zeitstempel, URLs, Beschreibungen ausgewählter Elemente, Validierungsergebnisse und Screenshot-Verweise auf, damit der Lauf überprüft werden kann. Vermeiden Sie das Speichern von Passwörtern, Zahlungsdetails, Sitzungscookies, Roh-Personendaten oder vollständigen Seiteninhalten, sofern es keinen spezifischen Aufbewahrungs- oder Datenschutzgrund gibt.
</details>

## Weitere Ressourcen

- [Erste Schritte mit Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright Integrationsvorlage](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use Schauspielerparameter und Inhaltsextraktion](https://docs.browser-use.com/customize/actor/all-parameters)
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