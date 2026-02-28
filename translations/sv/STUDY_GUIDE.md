# AI-agenter för nybörjare - Studieguid och kursöversikt

Denna guide ger en översikt av kursen "AI Agents for Beginners" och förklarar nyckelkoncept, ramverk och designmönster för att bygga AI-agenter.

## 1. Introduktion till AI-agenter

**Vad är AI-agenter?**  
AI-agenter är system som utökar kapaciteterna hos stora språkmodeller (LLMs) genom att ge dem tillgång till **verktyg**, **kunskap** och **minne**. Till skillnad från en standard LLM-chattbot som bara genererar text baserat på träningsdata kan en AI-agent:  
- **Uppfatta** sin omgivning (via sensorer eller indata).  
- **Resonera** om hur ett problem ska lösas.  
- **Agera** för att förändra omgivningen (via aktuatörer eller verktygsexekvering).  

**Nyckelkomponenter i en agent:**  
- **Miljö**: Utrymmet där agenten verkar (t.ex. ett bokningssystem).  
- **Sensorer**: Mekanismer för att samla information (t.ex. läsa ett API).  
- **Aktuatorer**: Mekanismer för att utföra handlingar (t.ex. skicka ett e-postmeddelande).  
- **Hjärna (LLM)**: Resoneringsmotorn som planerar och bestämmer vilka handlingar som ska tas.

## 2. Agentiska ramverk

Kursen använder **Microsoft Agent Framework (MAF)** med **Azure AI Foundry Agent Service V2** för att bygga agenter:

| Komponent | Fokus | Bäst för |
|-----------|-------|----------|
| **Microsoft Agent Framework** | Enhetligt Python/C# SDK för agenter, verktyg och arbetsflöden | Bygga agenter med verktyg, multi-agentarbetsflöden och produktionsmönster. |
| **Azure AI Foundry Agent Service** | Hanterad moln-körning | Säker, skalbar distribution med inbyggd tillståndshantering, observerbarhet och förtroende. |

## 3. Agentiska designmönster

Designmönster hjälper till att strukturera hur agenter arbetar för att pålitligt lösa problem.

### **Verktygsanvändningsmönster** (Lektion 4)  
Det här mönstret gör det möjligt för agenter att interagera med omvärlden.  
- **Koncept**: Agenten får en "schema" (en lista över tillgängliga funktioner och deras parametrar). LLM bestämmer *vilket* verktyg som ska anropas och med *vilka* argument baserat på användarens förfrågan.  
- **Flöde**: Användarförfrågan -> LLM -> **Verktygsval** -> **Verktygsexekvering** -> LLM (med verktygsutdata) -> Slutligt svar.  
- **Användningsfall**: Hämta realtidsdata (väder, aktiekurser), utföra beräkningar, exekvera kod.

### **Planeringsmönster** (Lektion 7)  
Detta mönster möjliggör för agenter att lösa komplexa, flerstegsuppgifter.  
- **Koncept**: Agenten delar upp ett övergripande mål i en sekvens av mindre deluppgifter.  
- **Tillvägagångssätt**:  
  - **Uppgiftsnedbrytning**: Delar "Planera en resa" i "Boka flyg", "Boka hotell", "Hyra bil".  
  - **Iterativ planering**: Omtvärderar planen baserat på resultatet från föregående steg (t.ex. om flyget är fullbokat, välj ett annat datum).  
- **Implementering**: Involverar ofta en "Planner"-agent som genererar en strukturerad plan (t.ex. JSON) som sedan exekveras av andra agenter.

## 4. Designprinciper

När du designar agenter, beakta tre dimensioner:  
- **Rum**: Agenter ska koppla samman människor och kunskap, vara tillgängliga men diskreta.  
- **Tid**: Agenter ska lära av *Det förflutna*, ge relevanta påminnelser i *Nuet* och anpassa sig för *Framtiden*.  
- **Kärna**: Omfamna osäkerhet men skapa förtroende genom transparens och användarkontroll.

## 5. Sammanfattning av viktiga lektioner

- **Lektion 1**: Agenter är system, inte bara modeller. De uppfattar, resonerar och agerar.  
- **Lektion 2**: Microsoft Agent Framework döljer komplexiteten i verktygsanrop och tillståndshantering.  
- **Lektion 3**: Designa med transparens och användarkontroll i åtanke.  
- **Lektion 4**: Verktyg är agentens "händer". Schemadefinition är avgörande för att LLM ska förstå hur de används.  
- **Lektion 7**: Planering är agentens "exekutiva funktion" som gör det möjligt att hantera komplexa arbetsflöden.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Originaldokumentet på dess ursprungliga språk ska betraktas som den auktoritativa källan. För viktig information rekommenderas professionell översättning av människor. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->