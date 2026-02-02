# AI Agenti za Početnike - Vodič za Učenje i Sažetak Tečaja

Ovaj vodič pruža sažetak tečaja "AI Agenti za Početnike" i objašnjava ključne pojmove, okvire i dizajnerske obrasce za izgradnju AI Agenta.

## 1. Uvod u AI Agente

**Što su AI Agenti?**
AI Agenti su sustavi koji proširuju mogućnosti Velikih Jezičnih Modela (LLM) dajući im pristup **alatima**, **znanju** i **memoriji**. Za razliku od standardnog LLM chatbota koji samo generira tekst na temelju podataka za treniranje, AI Agent može:
- **Perceptirati** svoje okruženje (putem senzora ili ulaza).
- **Razmišljati** o tome kako riješiti problem.
- **Djelovati** da promijeni okruženje (putem aktuatora ili izvršavanja alata).

**Ključne Komponente Agenta:**
- **Okruženje**: Prostor u kojem agent djeluje (npr. sustav za rezervacije).
- **Senzori**: Mehanizmi za prikupljanje informacija (npr. čitanje API-ja).
- **Aktuatori**: Mehanizmi za izvođenje radnji (npr. slanje emaila).
- **Mozak (LLM)**: Motor razmišljanja koji planira i odlučuje koje radnje poduzeti.

## 2. Agentni Okviri

Tečaj pokriva tri glavna okvira za izgradnju agenata:

| Okvir | Fokus | Najbolje za |
|-----------|-------|----------|
| **Semantic Kernel** | SDK spreman za proizvodnju za .NET/Python | Poslovne aplikacije, integracija AI-ja s postojećim kodom. |
| **AutoGen** | Suradnja više agenata | Kompleksni scenariji koji zahtijevaju komunikaciju višestrukih specijaliziranih agenata. |
| **Azure AI Agent Service** | Upravljana cloud usluga | Sigurno, skalabilno postavljanje s ugrađenim upravljanjem stanja. |

## 3. Agentni Dizajnerski Obrasci

Dizajnerski obrasci pomažu strukturirati način rada agenata kako bi pouzdano rješavali probleme.

### **Obrazac Korištenja Alata** (Lekcija 4)
Ovaj obrazac omogućuje agentima interakciju s vanjskim svijetom.
- **Koncept**: Agentu se pruža "shema" (lista dostupnih funkcija i njihovih parametara). LLM odlučuje *koji* alat pozvati i s *kojim* argumentima na temelju zahtjeva korisnika.
- **Tijek**: Korisnički Zahtjev -> LLM -> **Odabir Alata** -> **Izvršenje Alata** -> LLM (s izlazom alata) -> Konačni Odgovor.
- **Primjene**: Dohvaćanje podataka u stvarnom vremenu (vrijeme, cijene dionica), izvođenje proračuna, izvršavanje koda.

### **Obrazac Planiranja** (Lekcija 7)
Ovaj obrazac omogućuje agentima da riješe složene zadatke s više koraka.
- **Koncept**: Agent razlaže visoku razinu cilja u niz manjih podzadatka.
- **Pristupi**:
  - **Raspad Zadataka**: Razbijanje "Isplaniraj putovanje" u "Rezerviraj let", "Rezerviraj hotel", "Iznajmi auto".
  - **Iterativno Planiranje**: Ponovno ocjenjivanje plana na temelju izlaza prethodnih koraka (npr. ako je let pun, odabrati drugi datum).
- **Implementacija**: Često uključuje "Planner" agenta koji generira strukturirani plan (npr. JSON) koji zatim drugi agenti izvršavaju.

## 4. Dizajnerska Načela

Pri dizajniranju agenata razmotrite tri dimenzije:
- **Prostor**: Agenti trebaju povezivati ljude i znanje, biti dostupni, ali nenametljivi.
- **Vrijeme**: Agenti trebaju učiti iz *Prošlosti*, pružati relevantne poticaje *Sada*, i prilagođavati se za *Budućnost*.
- **Srž**: Prihvatiti nesigurnost, ali uspostaviti povjerenje kroz transparentnost i kontrolu korisnika.

## 5. Sažetak Ključnih Lekcija

- **Lekcija 1**: Agenti su sustavi, ne samo modeli. Oni percipiraju, razmišljaju i djeluju.
- **Lekcija 2**: Okviri poput Semantic Kernel i AutoGen apstrahiraju složenost pozivanja alata i upravljanja stanjem.
- **Lekcija 3**: Dizajnirajte s transparentnošću i kontrolom korisnika na umu.
- **Lekcija 4**: Alati su "ruke" agenta. Definicija sheme je ključna da LLM razumije kako ih koristiti.
- **Lekcija 7**: Planiranje je "izvršna funkcija" agenta koja mu omogućuje rješavanje složenih radnih tokova.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je korištenjem AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba se smatrati službenim i autoritativnim izvorom. Za važne informacije preporučujemo profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz upotrebe ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->