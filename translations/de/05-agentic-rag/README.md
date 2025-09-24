<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2f04b783b9e1253100329afd698f8ff",
  "translation_date": "2025-08-30T13:27:19+00:00",
  "source_file": "05-agentic-rag/README.md",
  "language_code": "de"
}
-->
[![Agentic RAG](../../../translated_images/lesson-5-thumbnail.20ba9d0c0ae64fae06637eb2023395d437b0152c0463c2227ff456afe5f14644.de.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Klicken Sie auf das Bild oben, um das Video zu dieser Lektion anzusehen)_

# Agentic RAG

Diese Lektion bietet einen umfassenden Überblick über Agentic Retrieval-Augmented Generation (Agentic RAG), ein aufkommendes KI-Paradigma, bei dem große Sprachmodelle (LLMs) eigenständig ihre nächsten Schritte planen, während sie Informationen aus externen Quellen abrufen. Im Gegensatz zu statischen Mustern des Abrufens und Lesens umfasst Agentic RAG iterative Aufrufe des LLM, unterbrochen von Werkzeug- oder Funktionsaufrufen und strukturierten Ausgaben. Das System bewertet Ergebnisse, verfeinert Abfragen, ruft bei Bedarf zusätzliche Werkzeuge auf und setzt diesen Zyklus fort, bis eine zufriedenstellende Lösung erreicht ist.

## Einführung

Diese Lektion behandelt:

- **Agentic RAG verstehen:** Lernen Sie das aufkommende Paradigma in der KI kennen, bei dem große Sprachmodelle (LLMs) eigenständig ihre nächsten Schritte planen, während sie Informationen aus externen Datenquellen abrufen.
- **Iterativer Maker-Checker-Stil:** Verstehen Sie den iterativen Zyklus von LLM-Aufrufen, unterbrochen von Werkzeug- oder Funktionsaufrufen und strukturierten Ausgaben, der darauf abzielt, die Korrektheit zu verbessern und fehlerhafte Abfragen zu behandeln.
- **Praktische Anwendungen erkunden:** Identifizieren Sie Szenarien, in denen Agentic RAG besonders nützlich ist, wie z. B. in korrektheitsorientierten Umgebungen, bei komplexen Datenbankinteraktionen und in erweiterten Workflows.

## Lernziele

Nach Abschluss dieser Lektion werden Sie wissen, wie man:

- **Agentic RAG versteht:** Lernen Sie das aufkommende Paradigma in der KI kennen, bei dem große Sprachmodelle (LLMs) eigenständig ihre nächsten Schritte planen, während sie Informationen aus externen Datenquellen abrufen.
- **Iterativer Maker-Checker-Stil:** Verstehen Sie das Konzept eines iterativen Zyklus von LLM-Aufrufen, unterbrochen von Werkzeug- oder Funktionsaufrufen und strukturierten Ausgaben, der darauf abzielt, die Korrektheit zu verbessern und fehlerhafte Abfragen zu behandeln.
- **Den Denkprozess übernehmen:** Verstehen Sie die Fähigkeit des Systems, seinen Denkprozess zu steuern, Entscheidungen darüber zu treffen, wie Probleme angegangen werden, ohne auf vordefinierte Pfade angewiesen zu sein.
- **Workflow:** Verstehen Sie, wie ein agentisches Modell eigenständig Markttrendberichte abruft, Wettbewerbsdaten identifiziert, interne Verkaufsmetriken korreliert, Erkenntnisse synthetisiert und die Strategie bewertet.
- **Iterative Schleifen, Werkzeugintegration und Gedächtnis:** Lernen Sie die Abhängigkeit des Systems von einem iterativen Interaktionsmuster kennen, das den Zustand und das Gedächtnis über die Schritte hinweg beibehält, um wiederholte Schleifen zu vermeiden und fundierte Entscheidungen zu treffen.
- **Fehlermodi und Selbstkorrektur behandeln:** Erkunden Sie die robusten Selbstkorrekturmechanismen des Systems, einschließlich Iteration und erneuter Abfrage, Nutzung diagnostischer Werkzeuge und Rückgriff auf menschliche Aufsicht.
- **Grenzen der Eigenständigkeit:** Verstehen Sie die Einschränkungen von Agentic RAG, mit Fokus auf domänenspezifische Autonomie, Infrastrukturabhängigkeit und die Einhaltung von Leitplanken.
- **Praktische Anwendungsfälle und Nutzen:** Identifizieren Sie Szenarien, in denen Agentic RAG besonders nützlich ist, wie z. B. in korrektheitsorientierten Umgebungen, bei komplexen Datenbankinteraktionen und in erweiterten Workflows.
- **Governance, Transparenz und Vertrauen:** Lernen Sie die Bedeutung von Governance und Transparenz kennen, einschließlich erklärbarer Entscheidungsfindung, Bias-Kontrolle und menschlicher Aufsicht.

## Was ist Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) ist ein aufkommendes KI-Paradigma, bei dem große Sprachmodelle (LLMs) eigenständig ihre nächsten Schritte planen, während sie Informationen aus externen Quellen abrufen. Im Gegensatz zu statischen Mustern des Abrufens und Lesens umfasst Agentic RAG iterative Aufrufe des LLM, unterbrochen von Werkzeug- oder Funktionsaufrufen und strukturierten Ausgaben. Das System bewertet Ergebnisse, verfeinert Abfragen, ruft bei Bedarf zusätzliche Werkzeuge auf und setzt diesen Zyklus fort, bis eine zufriedenstellende Lösung erreicht ist. Dieser iterative „Maker-Checker“-Stil verbessert die Korrektheit, behandelt fehlerhafte Abfragen und sorgt für qualitativ hochwertige Ergebnisse.

Das System übernimmt aktiv seinen Denkprozess, indem es fehlgeschlagene Abfragen umschreibt, verschiedene Abrufmethoden wählt und mehrere Werkzeuge integriert – wie z. B. Vektorsuche in Azure AI Search, SQL-Datenbanken oder benutzerdefinierte APIs – bevor es seine Antwort finalisiert. Die herausragende Eigenschaft eines agentischen Systems ist seine Fähigkeit, seinen Denkprozess zu steuern. Traditionelle RAG-Implementierungen verlassen sich auf vordefinierte Pfade, während ein agentisches System die Abfolge der Schritte basierend auf der Qualität der gefundenen Informationen autonom bestimmt.

## Definition von Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) ist ein aufkommendes Paradigma in der KI-Entwicklung, bei dem LLMs nicht nur Informationen aus externen Datenquellen abrufen, sondern auch eigenständig ihre nächsten Schritte planen. Im Gegensatz zu statischen Mustern des Abrufens und Lesens oder sorgfältig geskripteten Prompt-Sequenzen umfasst Agentic RAG einen Zyklus iterativer LLM-Aufrufe, unterbrochen von Werkzeug- oder Funktionsaufrufen und strukturierten Ausgaben. In jedem Schritt bewertet das System die erhaltenen Ergebnisse, entscheidet, ob es Abfragen verfeinern muss, ruft bei Bedarf zusätzliche Werkzeuge auf und setzt diesen Zyklus fort, bis eine zufriedenstellende Lösung erreicht ist.

Dieser iterative „Maker-Checker“-Stil ist darauf ausgelegt, die Korrektheit zu verbessern, fehlerhafte Abfragen an strukturierte Datenbanken (z. B. NL2SQL) zu behandeln und ausgewogene, qualitativ hochwertige Ergebnisse sicherzustellen. Anstatt sich ausschließlich auf sorgfältig entwickelte Prompt-Ketten zu verlassen, übernimmt das System aktiv seinen Denkprozess. Es kann fehlgeschlagene Abfragen umschreiben, verschiedene Abrufmethoden wählen und mehrere Werkzeuge integrieren – wie z. B. Vektorsuche in Azure AI Search, SQL-Datenbanken oder benutzerdefinierte APIs – bevor es seine Antwort finalisiert. Dies macht komplexe Orchestrierungs-Frameworks überflüssig. Stattdessen kann eine relativ einfache Schleife aus „LLM-Aufruf → Werkzeugnutzung → LLM-Aufruf → …“ zu anspruchsvollen und fundierten Ergebnissen führen.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.c8f4b85c26920f71ed181ebb14001ac7aae47c0b0af237edcf71898645a62db3.de.png)

## Den Denkprozess übernehmen

Die herausragende Eigenschaft, die ein System „agentisch“ macht, ist seine Fähigkeit, seinen Denkprozess zu steuern. Traditionelle RAG-Implementierungen hängen oft davon ab, dass Menschen einen Pfad für das Modell vordefinieren: eine Gedankenkette, die festlegt, was wann abgerufen werden soll.  
Ein wirklich agentisches System entscheidet jedoch intern, wie es das Problem angeht. Es führt nicht einfach ein Skript aus, sondern bestimmt autonom die Abfolge der Schritte basierend auf der Qualität der gefundenen Informationen.  
Beispielsweise, wenn es darum geht, eine Produktstartstrategie zu entwickeln, verlässt sich das agentische Modell nicht ausschließlich auf einen Prompt, der den gesamten Forschungs- und Entscheidungsworkflow vorgibt. Stattdessen entscheidet das Modell eigenständig:

1. Aktuelle Markttrendberichte mit Bing Web Grounding abzurufen.
2. Relevante Wettbewerbsdaten mit Azure AI Search zu identifizieren.
3. Historische interne Verkaufsmetriken mit Azure SQL Database zu korrelieren.
4. Die Erkenntnisse in eine kohärente Strategie zu synthetisieren, orchestriert über Azure OpenAI Service.
5. Die Strategie auf Lücken oder Inkonsistenzen zu bewerten und bei Bedarf eine weitere Runde des Abrufs einzuleiten.  

All diese Schritte – Abfragen verfeinern, Quellen auswählen, iterieren, bis die Antwort „zufriedenstellend“ ist – werden vom Modell entschieden, nicht von einem Menschen vordefiniert.

## Iterative Schleifen, Werkzeugintegration und Gedächtnis

![Tool Integration Architecture](../../../translated_images/tool-integration.0f569710b5c17c106757adba082f6c4be025ca0721bff7d1ee4b929a3617a600.de.png)

Ein agentisches System basiert auf einem iterativen Interaktionsmuster:

- **Erster Aufruf:** Das Ziel des Nutzers (d. h. der Nutzer-Prompt) wird dem LLM präsentiert.
- **Werkzeugaufruf:** Wenn das Modell fehlende Informationen oder unklare Anweisungen erkennt, wählt es ein Werkzeug oder eine Abrufmethode – wie eine Abfrage in einer Vektordatenbank (z. B. Azure AI Search Hybrid-Suche über private Daten) oder einen strukturierten SQL-Aufruf – um mehr Kontext zu sammeln.
- **Bewertung & Verfeinerung:** Nach der Überprüfung der zurückgegebenen Daten entscheidet das Modell, ob die Informationen ausreichen. Falls nicht, verfeinert es die Abfrage, probiert ein anderes Werkzeug oder passt seinen Ansatz an.
- **Wiederholen, bis zufriedenstellend:** Dieser Zyklus wird fortgesetzt, bis das Modell feststellt, dass es genügend Klarheit und Beweise hat, um eine fundierte, abschließende Antwort zu liefern.
- **Gedächtnis & Zustand:** Da das System den Zustand und das Gedächtnis über die Schritte hinweg beibehält, kann es sich an vorherige Versuche und deren Ergebnisse erinnern, wiederholte Schleifen vermeiden und fundiertere Entscheidungen treffen, während es voranschreitet.

Mit der Zeit entsteht so ein Gefühl des fortschreitenden Verständnisses, das es dem Modell ermöglicht, komplexe, mehrstufige Aufgaben zu bewältigen, ohne dass ein Mensch ständig eingreifen oder den Prompt umgestalten muss.

## Fehlermodi und Selbstkorrektur behandeln

Die Autonomie von Agentic RAG umfasst auch robuste Selbstkorrekturmechanismen. Wenn das System auf Sackgassen stößt – wie das Abrufen irrelevanter Dokumente oder das Auftreten fehlerhafter Abfragen – kann es:

- **Iterieren und erneut abfragen:** Anstatt minderwertige Antworten zurückzugeben, versucht das Modell neue Suchstrategien, schreibt Datenbankabfragen um oder betrachtet alternative Datensätze.
- **Diagnosewerkzeuge nutzen:** Das System kann zusätzliche Funktionen aufrufen, die ihm helfen, seine Denkschritte zu debuggen oder die Korrektheit der abgerufenen Daten zu bestätigen. Werkzeuge wie Azure AI Tracing sind wichtig, um eine robuste Beobachtbarkeit und Überwachung zu ermöglichen.
- **Auf menschliche Aufsicht zurückgreifen:** In kritischen oder wiederholt scheiternden Szenarien könnte das Modell Unsicherheiten kennzeichnen und menschliche Anleitung anfordern. Sobald der Mensch korrigierendes Feedback gibt, kann das Modell diese Lektion für die Zukunft übernehmen.

Dieser iterative und dynamische Ansatz ermöglicht es dem Modell, sich kontinuierlich zu verbessern, sodass es nicht nur ein Einweg-System ist, sondern eines, das aus seinen Fehlern während einer Sitzung lernt.

![Self Correction Mechanism](../../../translated_images/self-correction.da87f3783b7f174bdc592c754b352884dd283814758bfeb7a68f5fd910272f3b.de.png)

## Grenzen der Eigenständigkeit

Trotz seiner Autonomie innerhalb einer Aufgabe ist Agentic RAG nicht mit einer Allgemeinen Künstlichen Intelligenz vergleichbar. Seine „agentischen“ Fähigkeiten sind auf die von menschlichen Entwicklern bereitgestellten Werkzeuge, Datenquellen und Richtlinien beschränkt. Es kann keine eigenen Werkzeuge erfinden oder die festgelegten Domänengrenzen überschreiten. Vielmehr glänzt es darin, die vorhandenen Ressourcen dynamisch zu orchestrieren.  
Wesentliche Unterschiede zu fortgeschritteneren KI-Formen umfassen:

1. **Domänenspezifische Autonomie:** Agentic RAG-Systeme konzentrieren sich darauf, benutzerdefinierte Ziele innerhalb einer bekannten Domäne zu erreichen, indem sie Strategien wie Abfrageumschreibung oder Werkzeugauswahl anwenden, um Ergebnisse zu verbessern.
2. **Infrastrukturabhängigkeit:** Die Fähigkeiten des Systems hängen von den von Entwicklern integrierten Werkzeugen und Daten ab. Es kann diese Grenzen ohne menschliches Eingreifen nicht überschreiten.
3. **Einhaltung von Leitplanken:** Ethische Richtlinien, Compliance-Regeln und Geschäftspolitiken bleiben von großer Bedeutung. Die Freiheit des Agenten ist immer durch Sicherheitsmaßnahmen und Aufsichtsmechanismen eingeschränkt (hoffentlich?).

## Praktische Anwendungsfälle und Nutzen

Agentic RAG glänzt in Szenarien, die iterative Verfeinerung und Präzision erfordern:

1. **Korrektheitsorientierte Umgebungen:** Bei Compliance-Prüfungen, regulatorischen Analysen oder juristischen Recherchen kann das agentische Modell wiederholt Fakten überprüfen, mehrere Quellen konsultieren und Abfragen umschreiben, bis es eine gründlich geprüfte Antwort liefert.
2. **Komplexe Datenbankinteraktionen:** Beim Umgang mit strukturierten Daten, bei denen Abfragen häufig fehlschlagen oder angepasst werden müssen, kann das System seine Abfragen autonom mit Azure SQL oder Microsoft Fabric OneLake verfeinern, um sicherzustellen, dass der endgültige Abruf den Absichten des Nutzers entspricht.
3. **Erweiterte Workflows:** Länger laufende Sitzungen können sich entwickeln, wenn neue Informationen auftauchen. Agentic RAG kann kontinuierlich neue Daten einbeziehen und Strategien anpassen, während es mehr über den Problemraum lernt.

## Governance, Transparenz und Vertrauen

Da diese Systeme in ihrer Entscheidungsfindung immer autonomer werden, sind Governance und Transparenz entscheidend:

- **Erklärbare Entscheidungsfindung:** Das Modell kann eine Prüfspur der von ihm durchgeführten Abfragen, der konsultierten Quellen und der unternommenen Denkschritte bereitstellen. Werkzeuge wie Azure AI Content Safety und Azure AI Tracing / GenAIOps können helfen, Transparenz zu gewährleisten und Risiken zu minimieren.
- **Bias-Kontrolle und ausgewogene Abrufe:** Entwickler können Abrufstrategien anpassen, um sicherzustellen, dass ausgewogene, repräsentative Datenquellen berücksichtigt werden, und regelmäßig Ausgaben überprüfen, um Bias oder verzerrte Muster zu erkennen, z. B. mit benutzerdefinierten Modellen für fortgeschrittene Datenwissenschaftsorganisationen, die Azure Machine Learning verwenden.
- **Menschliche Aufsicht und Compliance:** Für sensible Aufgaben bleibt die menschliche Überprüfung unerlässlich. Agentic RAG ersetzt nicht das menschliche Urteilsvermögen bei Entscheidungen mit hohen Einsätzen – es ergänzt es, indem es gründlich geprüfte Optionen liefert.

Werkzeuge, die eine klare Aufzeichnung der Aktionen bereitstellen, sind essenziell. Ohne sie kann das Debuggen eines mehrstufigen Prozesses sehr schwierig sein. Sehen Sie sich das folgende Beispiel von Literal AI (dem Unternehmen hinter Chainlit) für einen Agentenlauf an:

![AgentRunExample](../../../translated_images/AgentRunExample.471a94bc40cbdc0cd04c1f43c8d8c9b751f10d97918c900e29cb3ba0d6aa4c00.de.png)

## Fazit

Agentic RAG stellt eine natürliche Weiterentwicklung dar, wie KI-Systeme komplexe, datenintensive Aufgaben bewältigen. Durch die Einführung eines iterativen Interaktionsmusters, die autonome Auswahl von Werkzeugen und die Verfeinerung von Abfragen bis zur Erzielung eines qualitativ hochwertigen Ergebnisses geht das System über statisches Prompt-Following hinaus und wird zu einem adaptiveren, kontextbewussten Entscheidungsträger. Obwohl es weiterhin durch menschlich definierte Infrastrukturen und ethische Richtlinien begrenzt ist, ermöglichen diese agentischen Fähigkeiten reichhaltigere, dynamischere und letztlich nützlichere KI-Interaktionen für Unternehmen und Endnutzer.

### Haben Sie weitere Fragen zu Agentic RAG?

Treten Sie dem [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) bei, um sich mit anderen Lernenden auszutauschen, Sprechstunden zu besuchen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.

## Zusätzliche Ressourcen

-
<a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">
Implementieren Sie Retrieval Augmented Generation (RAG) mit Azure OpenAI Service: Erfahren Sie, wie Sie Ihre eigenen Daten mit dem Azure OpenAI Service nutzen können. Dieses Microsoft Learn-Modul bietet eine umfassende Anleitung zur Implementierung von RAG.
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Bewertung von generativen KI-Anwendungen mit Azure AI Foundry: Dieser Artikel behandelt die Bewertung und den Vergleich von Modellen auf öffentlich verfügbaren Datensätzen, einschließlich Agentic-KI-Anwendungen und RAG-Architekturen</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Was ist Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Ein vollständiger Leitfaden zu agentenbasierter Retrieval Augmented Generation – Neuigkeiten aus der RAG-Generation</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: Beschleunigen Sie Ihr RAG mit Abfrageumformung und Selbstabfrage! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Agentic Layer zu RAG hinzufügen</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Die Zukunft von Wissensassistenten: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Wie man Agentic RAG-Systeme baut</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Verwendung des Azure AI Foundry Agent Service zur Skalierung Ihrer KI-Agenten</a>

### Akademische Arbeiten

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterative Verfeinerung mit Selbst-Feedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Sprachagenten mit verbalem Verstärkungslernen</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Große Sprachmodelle können sich mit tool-interaktiver Kritik selbst korrigieren</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Eine Übersicht über Agentic RAG</a>

## Vorherige Lektion

[Tool Use Design Pattern](../04-tool-use/README.md)

## Nächste Lektion

[Vertrauenswürdige KI-Agenten entwickeln](../06-building-trustworthy-agents/README.md)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.