# AI agenti za početnike - Vodič za učenje & Sažetak tečaja

Ovaj vodič daje sažetak tečaja "AI Agents for Beginners" i objašnjava ključne pojmove, okvire i obrasce dizajna za izgradnju AI agenata.

## 1. Uvod u AI agente

**Što su AI agenti?**
AI agenti su sustavi koji proširuju mogućnosti Large Language Models (LLMs) dajući im pristup **alatima**, **znanju** i **memoriji**. Za razliku od standardnog LLM chatbota koji samo generira tekst na temelju podataka za treniranje, AI agent može:
- **Percipirati** svoje okruženje (putem senzora ili ulaza).
- **Rasuđivati** o tome kako riješiti problem.
- **Djelovati** kako bi promijenio okruženje (putem aktuatora ili izvršavanja alata).

**Ključne komponente agenta:**
- **Okruženje**: Prostor u kojem agent djeluje (npr. sustav za rezervacije).
- **Senzori**: Mehanizmi za prikupljanje informacija (npr. čitanje API-ja).
- **Aktuatori**: Mehanizmi za izvršavanje radnji (npr. slanje e-pošte).
- **Mozak (LLM)**: Jedinica za rasuđivanje koja planira i odlučuje koje akcije poduzeti.

## 2. Okviri za agente

Tečaj koristi **Microsoft Agent Framework (MAF)** s **Azure AI Foundry Agent Service V2** za izgradnju agenata:

| Komponenta | Fokus | Najprikladnije za |
|-----------|-------|----------|
| **Microsoft Agent Framework** | Ujedinjeni Python/C# SDK za agente, alate, i tokove rada | Izgradnju agenata s alatima, tijekovima rada više agenata i produkcijskim obrascima. |
| **Azure AI Foundry Agent Service** | Upravljano runtime okruženje u oblaku | Sigurna, skalabilna implementacija s ugrađenim upravljanjem stanja, nadzorom i povjerenjem. |

## 3. Obrasci dizajna agenata

Obrasci dizajna pomažu strukturirati način na koji agenti djeluju kako bi pouzdano rješavali probleme.

### **Obrazac korištenja alata** (Lekcija 4)
Ovaj obrazac omogućuje agentima interakciju s vanjskim svijetom.
- **Koncept**: Agentu se daje "shema" (popis dostupnih funkcija i njihovih parametara). LLM odlučuje *koji* alat pozvati i s *kojim* argumentima na temelju korisničkog zahtjeva.
- **Tijek**: Zahtjev korisnika -> LLM -> **Odabir alata** -> **Izvršavanje alata** -> LLM (s izlazom alata) -> Konačni odgovor.
- **Primjeri upotrebe**: Dohvaćanje podataka u stvarnom vremenu (vrijeme, cijene dionica), izvođenje proračuna, izvršavanje koda.

### **Obrazac planiranja** (Lekcija 7)
Ovaj obrazac omogućuje agentima rješavanje složenih zadataka s više koraka.
- **Koncept**: Agent razlaže cilj visoke razine u niz manjih podzadataka.
- **Pristupi**:
  - **Razlaganje zadatka**: Raščlanjivanje "Isplaniraj putovanje" u "Rezerviraj let", "Rezerviraj hotel", "Iznajmi auto".
  - **Iterativno planiranje**: Ponovna procjena plana na temelju izlaza prethodnih koraka (npr. ako je let pun, odaberite drugi datum).
- **Implementacija**: Često uključuje "Planner" agenta koji generira strukturirani plan (npr. JSON) koji zatim izvršavaju drugi agenti.

## 4. Načela dizajna

Prilikom dizajniranja agenata, razmotrite tri dimenzije:
- **Prostor**: Agenti bi trebali povezati ljude i znanje, biti dostupni ali nenametljivi.
- **Vrijeme**: Agenti bi trebali učiti iz *prošlosti*, pružati relevantne poticaje u *sadašnjosti*, i prilagođavati se za *budućnost*.
- **Srž**: Prihvatite nesigurnost, ali uspostavite povjerenje kroz transparentnost i kontrolu korisnika.

## 5. Sažetak ključnih lekcija

- **Lekcija 1**: Agenti su sustavi, a ne samo modeli. Oni percipiraju, rasuđuju i djeluju.
- **Lekcija 2**: Microsoft Agent Framework apstrahira složenost pozivanja alata i upravljanja stanjem.
- **Lekcija 3**: Dizajnirajte imajući na umu transparentnost i kontrolu korisnika.
- **Lekcija 4**: Alati su "ruke" agenta. Definicija sheme je ključna za to da LLM razumije kako ih koristiti.
- **Lekcija 7**: Planiranje je "izvršna funkcija" agenta, omogućavajući mu da se nosi sa složenim tokovima rada.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje odgovornosti**:
Ovaj dokument je preveden pomoću AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo biti točni, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalan ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->