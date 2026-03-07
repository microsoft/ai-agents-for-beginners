# AI Agents voor Beginners - Studiegids & Cursusoverzicht

Deze gids biedt een samenvatting van de cursus "AI Agents voor Beginners" en verklaart belangrijke concepten, raamwerken en ontwerppatronen voor het bouwen van AI Agents.

## 1. Inleiding tot AI Agents

**Wat zijn AI Agents?**  
AI Agents zijn systemen die de mogelijkheden van Large Language Models (LLM's) uitbreiden door ze toegang te geven tot **tools**, **kennis**, en **geheugen**. In tegenstelling tot een standaard LLM-chatbot die alleen tekst genereert op basis van trainingsdata, kan een AI Agent:  
- **Waarnemen** van zijn omgeving (via sensoren of invoer).  
- **Redeneren** over hoe een probleem op te lossen.  
- **Handelen** om de omgeving te veranderen (via actuatoren of tooluitvoering).

**Belangrijke componenten van een agent:**  
- **Omgeving**: De ruimte waarin de agent opereert (bijv. een boekingssysteem).  
- **Sensoren**: Mechanismen om informatie te verzamelen (bijv. het uitlezen van een API).  
- **Actuatoren**: Mechanismen om acties uit te voeren (bijv. het versturen van een e-mail).  
- **Brein (LLM)**: De redeneermotor die plant en bepaalt welke acties genomen worden.

## 2. Agentic Raamwerken

De cursus gebruikt **Microsoft Agent Framework (MAF)** met **Azure AI Foundry Agent Service V2** voor het bouwen van agents:

| Component | Focus | Geschikt voor |
|-----------|-------|---------------|
| **Microsoft Agent Framework** | Geünificeerd Python/C# SDK voor agents, tools en workflows | Bouwen van agents met tools, multi-agent workflows, en productiepatronen. |
| **Azure AI Foundry Agent Service** | Beheerde cloud runtime | Veilige, schaalbare implementatie met ingebouwd statusbeheer, observeerbaarheid en vertrouwen. |

## 3. Agentic Ontwerppatronen

Ontwerppatronen helpen structureren hoe agents opereren om problemen betrouwbaar op te lossen.

### **Tool Use Pattern** (Les 4)  
Dit patroon stelt agents in staat om te communiceren met de buitenwereld.  
- **Concept**: De agent krijgt een "schema" (een lijst van beschikbare functies en hun parameters). Het LLM beslist *welke* tool wordt aangeroepen en met *welke* argumenten op basis van het verzoek van de gebruiker.  
- **Stroom**: Gebruikersverzoek -> LLM -> **Tool Selectie** -> **Tool Uitvoering** -> LLM (met tooloutput) -> Eindantwoord.  
- **Gebruik**: Ophalen van realtime data (weer, aandelenkoersen), uitvoeren van berekeningen, uitvoeren van code.

### **Planning Pattern** (Les 7)  
Dit patroon stelt agents in staat om complexe, meerstaps taken op te lossen.  
- **Concept**: De agent breekt een hoog niveau doel op in een reeks kleinere subtaken.  
- **Benaderingen**:  
  - **Taakdecompositie**: "Reis plannen" opsplitsen in "Vlucht boeken", "Hotel boeken", "Auto huren".  
  - **Iteratief plannen**: Het plan herzien op basis van output van eerdere stappen (bijv. als de vlucht vol is, een andere datum kiezen).  
- **Implementatie**: Vaak via een "Planner" agent die een gestructureerd plan genereert (bijv. JSON) dat vervolgens door andere agents wordt uitgevoerd.

## 4. Ontwerprichtlijnen

Bij het ontwerpen van agents, houd rekening met drie dimensies:  
- **Ruimte**: Agents moeten mensen en kennis verbinden, toegankelijk maar onopvallend zijn.  
- **Tijd**: Agents moeten leren van het *Verleden*, relevante aansturing bieden in het *Nu*, en zich aanpassen voor de *Toekomst*.  
- **Kern**: Omarm onzekerheid maar bouw vertrouwen op via transparantie en gebruikerscontrole.

## 5. Samenvatting van Belangrijke Lessen

- **Les 1**: Agents zijn systemen, niet alleen modellen. Ze waarnemen, redeneren en handelen.  
- **Les 2**: Microsoft Agent Framework abstraheert de complexiteit van toolaanroepen en statusbeheer.  
- **Les 3**: Ontwerp met transparantie en gebruikerscontrole in gedachten.  
- **Les 4**: Tools zijn de "handen" van de agent. Schema-definitie is cruciaal voor het LLM om te begrijpen hoe ze te gebruiken.  
- **Les 7**: Planning is de "uitvoerende functie" van de agent, waarmee complexe workflows kunnen worden aangepakt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als het gezaghebbende document worden beschouwd. Voor belangrijke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->