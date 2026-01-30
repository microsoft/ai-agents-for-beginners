# AI Agents voor Beginners - Studiegids & Cursusoverzicht

Deze gids biedt een overzicht van de cursus "AI Agents voor Beginners" en legt belangrijke concepten, frameworks en ontwerppatronen uit voor het bouwen van AI Agents.

## 1. Introductie tot AI Agents

**Wat zijn AI Agents?**  
AI Agents zijn systemen die de mogelijkheden van Large Language Models (LLM's) uitbreiden door hen toegang te geven tot **tools**, **kennis** en **geheugen**. In tegenstelling tot een standaard LLM-chatbot die alleen tekst genereert op basis van trainingsdata, kan een AI Agent:  
- **Waarnemen** van zijn omgeving (via sensoren of invoer).  
- **Redeneren** over hoe een probleem op te lossen.  
- **Handelen** om de omgeving te veranderen (via actuatoren of tooluitvoering).

**Belangrijke componenten van een Agent:**  
- **Omgeving**: De ruimte waarin de agent opereert (bijv. een boekingssysteem).  
- **Sensoren**: Mechanismen om informatie te verzamelen (bijv. het lezen van een API).  
- **Actuatoren**: Mechanismen om acties uit te voeren (bijv. het versturen van een e-mail).  
- **Brein (LLM)**: De redeneerengine die plant en beslist welke acties worden ondernomen.

## 2. Agentische Frameworks

De cursus behandelt drie primaire frameworks voor het bouwen van agents:

| Framework | Focus | Het beste voor |
|-----------|-------|---------------|
| **Semantic Kernel** | Productieklaar SDK voor .NET/Python | Enterprise-applicaties, integratie van AI met bestaande code. |
| **AutoGen** | Samenwerking tussen meerdere agents | Complexe scenario's die meerdere gespecialiseerde agents vereisen die met elkaar communiceren. |
| **Azure AI Agent Service** | Beheerde cloudservice | Veilige, schaalbare implementatie met ingebouwd statusbeheer. |

## 3. Agentische Ontwerppatronen

Ontwerppatronen helpen structureren hoe agents opereren om problemen betrouwbaar op te lossen.

### **Tool Use Pattern** (Les 4)  
Dit patroon stelt agents in staat om met de buitenwereld te interageren.  
- **Concept**: De agent krijgt een "schema" (een lijst van beschikbare functies en hun parameters). De LLM bepaalt *welke* tool moet worden aangeroepen en met *welke* argumenten op basis van het verzoek van de gebruiker.  
- **Stroom**: Gebruikersverzoek -> LLM -> **Tool Selectie** -> **Tool Uitvoering** -> LLM (met tool output) -> Eindantwoord.  
- **Gebruiksscenario’s**: Ophalen van realtime data (weer, aandelenkoersen), uitvoeren van berekeningen, uitvoeren van code.

### **Planning Pattern** (Les 7)  
Dit patroon stelt agents in staat om complexe, meerstaps-taken op te lossen.  
- **Concept**: De agent splitst een hoog niveau doel op in een reeks kleinere subtaken.  
- **Benaderingen**:  
  - **Taakdecompositie**: "Plan een reis" opsplitsen in "Vlucht boeken", "Hotel boeken", "Auto huren".  
  - **Iteratief plannen**: Het plan herzien op basis van de output van eerdere stappen (bijv. als de vlucht vol is, kies een andere datum).  
- **Implementatie**: Vaak met een "Planner" agent die een gestructureerd plan (bijv. JSON) genereert dat vervolgens door andere agents wordt uitgevoerd.

## 4. Ontwerprichtlijnen

Bij het ontwerpen van agents, houd rekening met drie dimensies:  
- **Ruimte**: Agents moeten mensen en kennis verbinden, toegankelijk maar onopvallend zijn.  
- **Tijd**: Agents moeten leren van het *Verleden*, relevante aanmoedigingen bieden in het *Nu*, en zich aanpassen voor de *Toekomst*.  
- **Kern**: Omarm onzekerheid maar bouw vertrouwen op door transparantie en gebruikerscontrole.

## 5. Samenvatting van Belangrijke Lessen

- **Les 1**: Agents zijn systemen, niet alleen modellen. Ze waarnemen, redeneren en handelen.  
- **Les 2**: Frameworks zoals Semantic Kernel en AutoGen abstraheren de complexiteit van tool-aanroepen en statusbeheer.  
- **Les 3**: Ontwerp met transparantie en gebruikerscontrole in gedachten.  
- **Les 4**: Tools zijn de "handen" van de agent. Schema-definitie is cruciaal voor de LLM om te begrijpen hoe ze te gebruiken.  
- **Les 7**: Plannen is de "uitvoerende functie" van de agent, die het in staat stelt complexe workflows aan te pakken.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, kan het zijn dat automatische vertalingen fouten of onnauwkeurigheden bevatten. Het originele document in de oorspronkelijke taal dient als de gezaghebbende bron te worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->