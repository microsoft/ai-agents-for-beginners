# AI Agents voor Beginners - Studiegids & Cursusoverzicht

Deze gids geeft een samenvatting van de cursus "AI Agents voor Beginners" en legt belangrijke concepten, raamwerken en ontwerppatronen uit voor het bouwen van AI Agents.

## 1. Introductie tot AI Agents

**Wat zijn AI Agents?**  
AI Agents zijn systemen die de mogelijkheden van Large Language Models (LLM's) uitbreiden door ze toegang te geven tot **tools**, **kennis** en **geheugen**. In tegenstelling tot een standaard LLM-chatbot die alleen tekst genereert op basis van trainingsgegevens, kan een AI Agent:  
- **Waarnemen** in zijn omgeving (via sensoren of invoer).  
- **Redeneren** over hoe een probleem opgelost kan worden.  
- **Handelen** om de omgeving te veranderen (via actuatoren of tool-uitvoering).

**Belangrijke componenten van een agent:**  
- **Omgeving**: De ruimte waar de agent opereert (bijv. een boekingssysteem).  
- **Sensoren**: Mechanismen om informatie te verzamelen (bijv. een API uitlezen).  
- **Actuatoren**: Mechanismen om acties uit te voeren (bijv. een e-mail verzenden).  
- **Brein (LLM)**: De redeneermotor die plant en beslist welke acties ondernomen worden.

## 2. Agentische Raamwerken

De cursus maakt gebruik van **Microsoft Agent Framework (MAF)** met de **Azure AI Foundry Agent Service V2** voor het bouwen van agents:

| Component | Focus | Het beste voor |
|-----------|-------|---------------|
| **Microsoft Agent Framework** | Unified Python/C# SDK voor agents, tools en workflows | Agents bouwen met tools, multi-agent workflows en productiemodellen. |
| **Azure AI Foundry Agent Service** | Beheerde cloud runtime | Veilige, schaalbare uitrol met ingebouwd statusbeheer, observatie en vertrouwen. |

## 3. Agentische Ontwerppatronen

Ontwerppatronen helpen structureren hoe agents opereren om problemen betrouwbaar op te lossen.

### **Tool Use Pattern** (Les 4)  
Dit patroon stelt agents in staat te interageren met de buitenwereld.  
- **Concept**: De agent krijgt een "schema" (een lijst van beschikbare functies en hun parameters). De LLM bepaalt *welke* tool aangeroepen wordt en met *welke* argumenten op basis van het verzoek van de gebruiker.  
- **Stroom**: Gebruikersverzoek -> LLM -> **Toolselectie** -> **Tooluitvoering** -> LLM (met tooloutput) -> Definitieve respons.  
- **Toepassingen**: Opvragen van realtime data (weer, aandelenkoersen), berekeningen uitvoeren, code uitvoeren.

### **Planning Pattern** (Les 7)  
Dit patroon stelt agents in staat complexe, meerstaps taken op te lossen.  
- **Concept**: De agent breekt een hoog niveau doel op in een reeks kleinere subtaken.  
- **Benaderingen**:  
  - **Taakdecompositie**: "Plan een reis" opsplitsen in "Vliegticket boeken", "Hotel boeken", "Auto huren".  
  - **Iteratieve planning**: Het plan herbeoordelen op basis van de output van eerdere stappen (bijv. als de vlucht vol is, een andere datum kiezen).  
- **Implementatie**: Vaak omvat dit een "Planner" agent die een gestructureerd plan (bijv. JSON) genereert dat vervolgens uitgevoerd wordt door andere agents.

## 4. Ontwerprichtlijnen

Bij het ontwerpen van agents, houd rekening met drie dimensies:  
- **Ruimte**: Agents moeten mensen en kennis verbinden, toegankelijk zijn maar onopvallend.  
- **Tijd**: Agents moeten leren van het *Verleden*, relevante aansturing geven in het *Nu*, en zich aanpassen voor de *Toekomst*.  
- **Kern**: Omarm onzekerheid maar bouw vertrouwen op door transparantie en gebruikerscontrole.

## 5. Samenvatting van Belangrijke Lessen

- **Les 1**: Agents zijn systemen, niet alleen modellen. Ze nemen waar, redeneren en handelen.  
- **Les 2**: Microsoft Agent Framework abstraheert de complexiteit van toolaanroepen en statusbeheer.  
- **Les 3**: Ontwerp met transparantie en gebruikerscontrole in gedachten.  
- **Les 4**: Tools zijn de "handen" van de agent. Schema-definitie is cruciaal voor de LLM om te begrijpen hoe ze te gebruiken.  
- **Les 7**: Planning is de "uitvoerende functie" van de agent, waardoor deze complexe workflows aankan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->