[![Agentic RAG](../../../translated_images/de/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

# Agentic RAG

Diese Lektion bietet einen umfassenden Überblick über Agentic Retrieval-Augmented Generation (Agentic RAG), ein aufkommendes KI-Paradigma, bei dem große Sprachmodelle (LLMs) autonom ihre nächsten Schritte planen, während sie Informationen aus externen Quellen abrufen. Im Gegensatz zu statischen Abruf-danach-Lesen-Mustern beinhaltet Agentic RAG iterative Aufrufe an das LLM, durchsetzt mit Werkzeug- oder Funktionsaufrufen und strukturierten Ausgaben. Das System bewertet Ergebnisse, verfeinert Abfragen, ruft bei Bedarf zusätzliche Werkzeuge auf und setzt diesen Zyklus fort, bis eine zufriedenstellende Lösung erreicht ist.

## Einführung

Diese Lektion behandelt

- **Agentic RAG verstehen:** Erfahren Sie mehr über das aufkommende Paradigma in der KI, bei dem große Sprachmodelle (LLMs) autonom ihre nächsten Schritte planen, während sie Informationen aus externen Datenquellen abrufen.
- **Iterativen Maker-Checker-Stil erfassen:** Verstehen Sie die Schleife iterativer Aufrufe an das LLM, durchsetzt mit Werkzeug- oder Funktionsaufrufen und strukturierten Ausgaben, die darauf ausgelegt sind, die Korrektheit zu verbessern und fehlerhafte Abfragen zu handhaben.
- **Praktische Anwendungen erkunden:** Identifizieren Sie Szenarien, in denen Agentic RAG glänzt, wie z. B. korrektenzentrierte Umgebungen, komplexe Datenbankinteraktionen und erweiterte Workflows.

## Lernziele

Nach Abschluss dieser Lektion werden Sie wissen wie/verstanden:

- **Agentic RAG verstehen:** Lernen Sie das aufkommende Paradigma in der KI kennen, bei dem große Sprachmodelle (LLMs) autonom ihre nächsten Schritte planen, während sie Informationen aus externen Datenquellen abrufen.
- **Iterativer Maker-Checker-Stil:** Verstehen Sie das Konzept einer Schleife iterativer Aufrufe an das LLM, durchsetzt mit Werkzeug- oder Funktionsaufrufen und strukturierten Ausgaben, die darauf ausgelegt sind, die Korrektheit zu verbessern und fehlerhafte Abfragen zu handhaben.
- **Den Denkprozess übernehmen:** Verstehen Sie die Fähigkeit des Systems, seinen Denkprozess zu besitzen, Entscheidungen darüber zu treffen, wie Probleme angegangen werden, ohne sich auf vorgegebene Pfade zu verlassen.
- **Workflow:** Verstehen Sie, wie ein agentisches Modell eigenständig entscheidet, Marktentwicklungsberichte abzurufen, Wettbewerbsdaten zu identifizieren, interne Verkaufsmetriken zu korrelieren, Ergebnisse zu synthetisieren und die Strategie zu evaluieren.
- **Iterative Schleifen, Werkzeugintegration und Gedächtnis:** Lernen Sie das Loop-Interaktionsmuster des Systems kennen, das Status und Gedächtnis über Schritte hinweg erhält, um wiederholte Schleifen zu vermeiden und fundierte Entscheidungen zu treffen.
- **Umgang mit Fehlerfällen und Selbstkorrektur:** Erkunden Sie die robusten Selbstkorrekturmechanismen des Systems, einschließlich Iteration und erneuter Abfrage, Nutzung diagnostischer Werkzeuge und Zurückgreifen auf menschliche Aufsicht.
- **Grenzen der Agency:** Verstehen Sie die Einschränkungen von Agentic RAG, wobei der Fokus auf domänenspezifischer Autonomie, Infrastrukturabhängigkeit und Einhaltung von Leitplanken liegt.
- **Praktische Anwendungsfälle und Nutzen:** Identifizieren Sie Szenarien, in denen Agentic RAG glänzt, wie korrektezentrierte Umgebungen, komplexe Datenbankinteraktionen und erweiterte Workflows.
- **Governance, Transparenz und Vertrauen:** Erfahren Sie die Bedeutung von Governance und Transparenz, einschließlich erklärbarem Denken, Bias-Kontrolle und menschlicher Aufsicht.

## Was ist Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) ist ein aufkommendes KI-Paradigma, bei dem große Sprachmodelle (LLMs) autonom ihre nächsten Schritte planen, während sie Informationen aus externen Quellen abrufen. Im Gegensatz zu statischen Abruf-danach-Lesen-Mustern beinhaltet Agentic RAG iterative Aufrufe an das LLM, durchsetzt mit Werkzeug- oder Funktionsaufrufen und strukturierten Ausgaben. Das System bewertet Ergebnisse, verfeinert Abfragen, ruft bei Bedarf zusätzliche Werkzeuge auf und setzt diesen Zyklus fort, bis eine zufriedenstellende Lösung erreicht ist. Dieser iterative „Maker-Checker“-Stil verbessert die Korrektheit, behandelt fehlerhafte Abfragen und sorgt für hochwertige Ergebnisse.

Das System übernimmt aktiv seinen Denkprozess, schreibt fehlgeschlagene Abfragen um, wählt andere Abrufmethoden und integriert mehrere Werkzeuge – wie Vektorsuche in Azure AI Search, SQL-Datenbanken oder benutzerdefinierte APIs – bevor es seine Antwort finalisiert. Die Unterscheidung eines agentischen Systems liegt in seiner Fähigkeit, seinen Denkprozess zu besitzen. Traditionelle RAG-Implementierungen beruhen auf vorgegebenen Pfaden, während ein agentisches System die Abfolge der Schritte autonom basierend auf der Qualität der gefundenen Informationen bestimmt.

## Definition von Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) ist ein aufkommendes Paradigma in der KI-Entwicklung, bei dem LLMs nicht nur Informationen aus externen Datenquellen abrufen, sondern auch autonom ihre nächsten Schritte planen. Im Gegensatz zu statischen Abruf-danach-Lesen-Mustern oder sorgfältig skriptierten Prompt-Sequenzen beinhaltet Agentic RAG eine Schleife iterativer Aufrufe an das LLM, durchsetzt mit Werkzeug- oder Funktionsaufrufen und strukturierten Ausgaben. Das System bewertet bei jedem Schritt die erzielten Ergebnisse, entscheidet, ob es seine Abfragen verfeinern soll, ruft bei Bedarf zusätzliche Werkzeuge auf und setzt diesen Zyklus fort, bis es eine zufriedenstellende Lösung erreicht.

Dieser iterative „Maker-Checker“-Betriebsstil ist darauf ausgelegt, die Korrektheit zu erhöhen, fehlerhafte Abfragen an strukturierte Datenbanken (z. B. NL2SQL) zu behandeln und ausgewogene, hochwertige Ergebnisse zu gewährleisten. Anstatt sich ausschließlich auf sorgfältig entworfene Prompt-Ketten zu verlassen, übernimmt das System aktiv seinen Denkprozess. Es kann fehlgeschlagene Abfragen umschreiben, verschiedene Abrufmethoden wählen und mehrere Werkzeuge integrieren – wie Vektorsuche in Azure AI Search, SQL-Datenbanken oder benutzerdefinierte APIs – bevor es seine Antwort abschließt. Dadurch entfällt die Notwendigkeit für übermäßig komplexe Orchestrierungsframeworks. Stattdessen kann eine relativ einfache Schleife von „LLM-Aufruf → Werkzeugnutzung → LLM-Aufruf → …“ anspruchsvolle und gut fundierte Ausgaben liefern.

![Agentic RAG Core Loop](../../../translated_images/de/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Besitz des Denkprozesses

Das hervorstechende Merkmal, das ein System „agentisch“ macht, ist seine Fähigkeit, seinen Denkprozess zu besitzen. Traditionelle RAG-Implementierungen verlassen sich oft darauf, dass Menschen einen Pfad für das Modell vorgeben: eine Gedankenfokuskette, die umreißt, was wann abgerufen werden soll.
Doch wenn ein System wirklich agentisch ist, entscheidet es intern, wie es das Problem angeht. Es führt nicht nur ein Skript aus, sondern bestimmt autonom die Abfolge der Schritte basierend auf der Qualität der gefundenen Informationen.
Zum Beispiel, wenn es gebeten wird, eine Produkteinführungsstrategie zu erstellen, verlässt es sich nicht nur auf einen Prompt, der den gesamten Forschungs- und Entscheidungsprozess beschreibt. Stattdessen entscheidet das agentische Modell eigenständig:

1. Aktuelle Markttrends über Bing Web Grounding abzurufen
2. Relevante Wettbewerbsdaten mithilfe von Azure AI Search zu identifizieren
3. Historische interne Verkaufsmetriken mit Azure SQL-Datenbank zu korrelieren
4. Die Erkenntnisse zu einer kohärenten Strategie zusammenzuführen, orchestriert über Azure OpenAI Service
5. Die Strategie auf Lücken oder Inkonsistenzen zu bewerten und bei Bedarf eine weitere Abrufrunde einzuleiten
Alle diese Schritte – Abfragen verfeinern, Quellen auswählen, solange iterieren, bis das Ergebnis „zufriedenstellend“ ist – werden vom Modell entschieden, nicht von Menschen vorprogrammiert.

## Iterative Schleifen, Werkzeugintegration und Gedächtnis

![Tool Integration Architecture](../../../translated_images/de/tool-integration.0f569710b5c17c10.webp)

Ein agentisches System basiert auf einem loopbasierten Interaktionsmuster:

- **Erster Aufruf:** Das Ziel des Benutzers (auch Benutzerprompt genannt) wird dem LLM präsentiert.
- **Werkzeugaufruf:** Wenn das Modell fehlende Informationen oder mehrdeutige Anweisungen erkennt, wählt es ein Werkzeug oder eine Abrufmethode – wie eine Vektordatenbankabfrage (z. B. Azure AI Search Hybrid-Suche über private Daten) oder einen strukturierten SQL-Aufruf – um mehr Kontext zu sammeln.
- **Bewertung & Verfeinerung:** Nach Durchsicht der zurückgegebenen Daten entscheidet das Modell, ob die Informationen ausreichen. Falls nicht, verfeinert es die Abfrage, probiert ein anderes Werkzeug oder passt seine Herangehensweise an.
- **Wiederholen bis zufrieden:** Dieser Zyklus setzt sich fort, bis das Modell feststellt, dass es genügend Klarheit und Belege hat, um eine finale, gut begründete Antwort zu liefern.
- **Gedächtnis & Zustand:** Da das System über die Schritte hinweg Zustand und Gedächtnis aufrechterhält, kann es frühere Versuche und deren Ergebnisse abrufen, wiederholte Schleifen vermeiden und im weiteren Verlauf fundiertere Entscheidungen treffen.

Mit der Zeit entsteht so ein Gefühl für sich entwickelndes Verständnis, das es dem Modell ermöglicht, komplexe, mehrstufige Aufgaben zu bewältigen, ohne dass ein Mensch ständig eingreifen oder den Prompt umgestalten muss.

## Umgang mit Fehlermodi und Selbstkorrektur

Die Autonomie von Agentic RAG beinhaltet auch robuste Selbstkorrekturmechanismen. Wenn das System auf Sackgassen stößt – z. B. irrelevante Dokumente abruft oder fehlerhafte Abfragen erhält – kann es:

- **Iterieren und neu abfragen:** Anstatt minderwertige Antworten zurückzugeben, versucht das Modell neue Suchstrategien, schreibt Datenbankabfragen um oder betrachtet alternative Datensätze.
- **Diagnosewerkzeuge verwenden:** Das System kann zusätzliche Funktionen aufrufen, die ihm helfen, seine Denkprozesse zu debuggen oder die Korrektheit der abgerufenen Daten zu bestätigen. Werkzeuge wie Azure AI Tracing sind wichtig, um robuste Beobachtbarkeit und Überwachung zu ermöglichen.
- **Auf menschliche Aufsicht zurückgreifen:** Für kritische oder wiederholt fehlschlagende Szenarien könnte das Modell Unsicherheit signalisieren und menschliche Anleitung anfordern. Sobald der Mensch korrigierendes Feedback gibt, kann das Modell diese Lektion für die Zukunft einbauen.

Dieser iterative und dynamische Ansatz ermöglicht es dem Modell, sich kontinuierlich zu verbessern und sicherzustellen, dass es nicht nur ein einmaliges System ist, sondern eins, das aus seinen Fehlern während einer Sitzung lernt.

![Self Correction Mechanism](../../../translated_images/de/self-correction.da87f3783b7f174b.webp)

## Grenzen der Agency

Trotz seiner Autonomie innerhalb einer Aufgabe ist Agentic RAG nicht mit künstlicher allgemeiner Intelligenz gleichzusetzen. Seine „agentischen“ Fähigkeiten sind auf die von menschlichen Entwicklern bereitgestellten Werkzeuge, Datenquellen und Richtlinien beschränkt. Es kann keine eigenen Werkzeuge erfinden oder die festgelegten Domänengrenzen überschreiten. Stattdessen glänzt es darin, die verfügbaren Ressourcen dynamisch zu orchestrieren.
Wichtige Unterschiede zu fortgeschritteneren KI-Formen umfassen:

1. **Domänenspezifische Autonomie:** Agentic RAG-Systeme konzentrieren sich darauf, benutzerdefinierte Ziele innerhalb einer bekannten Domäne zu erreichen und wenden Strategien wie Abfrageumschreibungen oder Werkzeugauswahl an, um Ergebnisse zu verbessern.
2. **Infrastrukturabhängig:** Die Fähigkeiten des Systems hängen von den von Entwicklern integrierten Werkzeugen und Daten ab. Ohne menschliches Eingreifen kann es diese Grenzen nicht überschreiten.
3. **Einhaltung von Leitplanken:** Ethische Richtlinien, Compliance-Vorschriften und Unternehmensrichtlinien bleiben sehr wichtig. Die Freiheit des Agenten ist stets durch Sicherheitsmaßnahmen und Aufsicht beschränkt (hoffentlich).

## Praktische Anwendungsfälle und Nutzen

Agentic RAG zeigt seine Stärken in Szenarien, die iterative Verfeinerung und Präzision erfordern:

1. **Korrektheitszentrierte Umgebungen:** Bei Compliance-Prüfungen, regulatorischer Analyse oder juristischer Recherche kann das agentische Modell Fakten wiederholt überprüfen, mehrere Quellen konsultieren und Abfragen so lange umschreiben, bis eine gründlich geprüfte Antwort vorliegt.
2. **Komplexe Datenbankinteraktionen:** Beim Umgang mit strukturierten Daten, bei denen Abfragen oft fehlschlagen oder angepasst werden müssen, kann das System seine Abfragen autonom verfeinern – mit Azure SQL oder Microsoft Fabric OneLake –, sodass der endgültige Abruf der Benutzerintention entspricht.
3. **Erweiterte Workflows:** Längere Sitzungen könnten sich weiterentwickeln, wenn neue Informationen auftauchen. Agentic RAG kann kontinuierlich neue Daten einbeziehen und Strategien anpassen, während es mehr über das Problemfeld lernt.

## Governance, Transparenz und Vertrauen

Da diese Systeme beim Denken autonomer werden, sind Governance und Transparenz entscheidend:

- **Erklärbares Denken:** Das Modell kann eine Prüfspur der getätigten Abfragen, konsultierten Quellen und durchgeführten Denkschritte bereitstellen, um zu seiner Schlussfolgerung zu gelangen. Werkzeuge wie Azure AI Content Safety und Azure AI Tracing / GenAIOps helfen, Transparenz aufrechtzuerhalten und Risiken zu mindern.
- **Bias-Kontrolle und ausgewogener Abruf:** Entwickler können Abrufstrategien so anpassen, dass ausgewogene, repräsentative Datenquellen berücksichtigt werden, und die Ausgaben regelmäßig prüfen, um Verzerrungen oder fehlerhafte Muster mithilfe benutzerdefinierter Modelle für fortgeschrittene Data-Science-Organisationen mit Azure Machine Learning zu erkennen.
- **Menschliche Aufsicht und Compliance:** Für sensible Aufgaben bleibt die menschliche Überprüfung unerlässlich. Agentic RAG ersetzt menschliches Urteilsvermögen bei Entscheidungen mit hoher Bedeutung nicht – es ergänzt es durch die Bereitstellung gründlich geprüfter Optionen.

Es ist essentiell, Werkzeuge zu haben, die eine klare Aufzeichnung der Aktionen liefern. Ohne diese ist die Fehlerbehebung bei mehrstufigen Prozessen sehr schwierig. Nachfolgend ein Beispiel von Literal AI (Firma hinter Chainlit) für einen Agentenlauf:

![AgentRunExample](../../../translated_images/de/AgentRunExample.471a94bc40cbdc0c.webp)

## Fazit

Agentic RAG stellt eine natürliche Weiterentwicklung dar, wie KI-Systeme komplexe, datenintensive Aufgaben handhaben. Durch die Annahme eines loopbasierten Interaktionsmusters, die autonome Werkzeugwahl und Abfrageverfeinerung bis zum Erreichen eines hochwertigen Ergebnisses bewegt sich das System über reines promptbasiertes Folgen hinaus hin zu einem adaptiven, kontextbewussten Entscheidungsträger. Obwohl es weiterhin durch von Menschen definierte Infrastrukturen und ethische Vorgaben begrenzt ist, ermöglichen diese agentischen Fähigkeiten reichhaltigere, dynamischere und letztlich nützlichere KI-Interaktionen sowohl für Unternehmen als auch für Endanwender.

### Haben Sie weitere Fragen zu Agentic RAG?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Antworten auf Ihre Fragen zu KI-Agenten zu erhalten.

## Zusätzliche Ressourcen

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementierung von Retrieval Augmented Generation (RAG) mit Azure OpenAI Service: Lernen Sie, wie Sie Ihre eigenen Daten mit dem Azure OpenAI Service verwenden. Dieses Microsoft Learn-Modul bietet eine umfassende Anleitung zur Implementierung von RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Bewertung generativer KI-Anwendungen mit Microsoft Foundry: Dieser Artikel behandelt die Bewertung und den Vergleich von Modellen anhand öffentlich verfügbarer Datensätze, einschließlich agentischer KI-Anwendungen und RAG-Architekturen</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Was ist Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Ein vollständiger Leitfaden zur agentenbasierten Retrieval Augmented Generation – Nachrichten von generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: Beschleunigen Sie Ihr RAG mit Abfrage-Umformulierung und Selbstabfrage! Hugging Face Open-Source KI-Kochbuch</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Agentische Schichten zu RAG hinzufügen</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Die Zukunft der Wissensassistenten: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Wie man agentische RAG-Systeme baut</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Verwendung des Microsoft Foundry Agent Service zur Skalierung Ihrer KI-Agenten</a>

### Wissenschaftliche Veröffentlichungen

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterative Verfeinerung mit Selbst-Feedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Sprachagenten mit verbalem Verstärkungslernen</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Große Sprachmodelle können sich mit werkzeug-interaktivem Kritisieren selbst korrigieren</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Eine Übersicht über Agentic RAG</a>

## Smoke-Test dieses Agenten (Optional)

Nachdem Sie gelernt haben, Agenten in [Lesson 16](../16-deploying-scalable-agents/README.md) bereitzustellen, können Sie den `TravelRAGAgent` dieser Lektion mit [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) einem Schnelltest unterziehen — um zu prüfen, ob seine Antworten auf der Wissensbasis basieren. Siehe [`tests/README.md`](../tests/README.md) für Anweisungen zur Ausführung.

## Vorherige Lektion

[Tool Use Design Pattern](../04-tool-use/README.md)

## Nächste Lektion

[Vertrauenswürdige KI-Agenten entwickeln](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->