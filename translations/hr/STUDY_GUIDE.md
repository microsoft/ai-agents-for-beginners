# AI Agenti za Početnike - Vodič za Učenje i Sažetak Tečaja

Ovaj vodič daje sažetak tečaja "AI Agents for Beginners" i objašnjava ključne pojmove, okvire i obrasce dizajna za izradu AI agenata.

## 1. Uvod u AI Agente

**Što su AI Agenti?**
AI agenti su sustavi koji proširuju mogućnosti velikih jezičnih modela (LLM-ova) dajući im pristup **alatima**, **znanju** i **memoriji**. Za razliku od standardnog LLM chatbota koji samo generira tekst na temelju podataka za obuku, AI agent može:
- **Percepcija** svog okruženja (putem senzora ili ulaza).
- **Rasuditi** o tome kako riješiti problem.
- **Djelovati** kako bi promijenio okruženje (putem aktuatora ili izvršavanja alata).

**Ključne komponente agenta:**
- **Okruženje**: Prostor u kojem agent djeluje (npr., sustav za rezervacije).
- **Senzori**: Mehanizmi za prikupljanje informacija (npr., čitanje API-ja).
- **Aktuatori**: Mehanizmi za izvođenje radnji (npr., slanje e-pošte).
- **Mozak (LLM)**: Pokretač razmišljanja koji planira i odlučuje koje radnje poduzeti.

## 2. Agentni okviri

Tečaj koristi **Microsoft Agent Framework (MAF)** s **Azure AI Foundry Agent Service V2** za izgradnju agenata:

| Component | Focus | Best For |
|-----------|-------|----------|
| **Microsoft Agent Framework** | Ujedinjeni Python/C# SDK za agente, alate i tijekove rada | Izgradnja agenata s alatima, višestrukim tijekovima rada agenata i proizvodnim obrascima. |
| **Azure AI Foundry Agent Service** | Upravljano cloud runtime | Sigurno, skalabilno postavljanje s ugrađenim upravljanjem stanja, promatranjem i povjerenjem. |

## 3. Obrasci dizajna za agente

Obrasci dizajna pomažu strukturirati način na koji agenti djeluju kako bi pouzdano rješavali probleme.

### **Obrazac upotrebe alata** (Lekcija 4)
Ovaj obrazac omogućuje agentima interakciju s vanjskim svijetom.
- **Koncept**: Agentu se daje "schema" (popis dostupnih funkcija i njihovih parametara). LLM odlučuje *koji* alat pozvati i s *kojim* argumentima na temelju korisničkog zahtjeva.
- **Tijek**: Zahtjev korisnika -> LLM -> **Odabir alata** -> **Izvršavanje alata** -> LLM (s izlazom alata) -> Konačni odgovor.
- **Slučajevi upotrebe**: Dohvaćanje podataka u stvarnom vremenu (vrijeme, cijene dionica), izvođenje izračuna, izvršavanje koda.

### **Obrazac planiranja** (Lekcija 7)
Ovaj obrazac omogućuje agentima rješavanje složenih zadataka u više koraka.
- **Koncept**: Agent razlaže cilj visoke razine u niz manjih podzadatka.
- **Pristupi**:
  - **Razlaganje zadatka**: Razdvajanje "Isplaniraj putovanje" u "Rezerviraj let", "Rezerviraj hotel", "Iznajmi auto".
  - **Iterativno planiranje**: Ponovno vrednovanje plana na temelju rezultata prethodnih koraka (npr., ako je let pun, odaberite drugi datum).
- **Implementacija**: Često uključuje "Planner" agenta koji generira strukturirani plan (npr., JSON) koji zatim izvršavaju drugi agenti.

## 4. Načela dizajna

Pri dizajniranju agenata, razmotrite tri dimenzije:
- **Prostor**: Agenti bi trebali povezivati ljude i znanje, biti pristupačni, ali neupadljivi.
- **Vrijeme**: Agenti bi se trebali učiti iz *Prošlosti*, pružati relevantne poticaje u *Sadašnjosti*, i prilagođavati se za *Budućnost*.
- **Jezgra**: Prihvatite neizvjesnost, ali uspostavite povjerenje kroz transparentnost i kontrolu korisnika.

## 5. Sažetak ključnih lekcija

- **Lekcija 1**: Agenti su sustavi, ne samo modeli. Oni percipiraju, rasuđuju i djeluju.
- **Lekcija 2**: Microsoft Agent Framework apstrahira složenost pozivanja alata i upravljanja stanjem.
- **Lekcija 3**: Dizajnirajte imajući na umu transparentnost i kontrolu korisnika.
- **Lekcija 4**: Alati su "ruke" agenta. Definicija sheme ključna je da bi LLM razumio kako ih koristiti.
- **Lekcija 7**: Planiranje je "izvršna funkcija" agenta, omogućujući mu rješavanje složenih tijekova rada.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Odricanje odgovornosti:
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za eventualne nesporazume ili pogrešna tumačenja koja proizlaze iz upotrebe ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->