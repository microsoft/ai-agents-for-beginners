[![Introducere în Agenții AI](../../../translated_images/ro/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Click pe imaginea de mai sus pentru a viziona videoclipul pentru această lecție)_

# Introducere în Agenții AI și Cazuri de Utilizare a Agenților

Bine ați venit la cursul **Agenții AI pentru Începători**! Acest curs vă oferă cunoștințele de bază — și codul real funcțional — pentru a începe să construiți Agenți AI de la zero.

Veniți să spuneți bună în <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunitatea Discord Azure AI</a> — este plină de cursanți și dezvoltatori AI fericiți să răspundă la întrebări.

Înainte să începem construcția, să ne asigurăm că înțelegem cu adevărat ce este un Agent AI și când are sens să folosim unul.

---

## Introducere

Această lecție acoperă:

- Ce sunt Agenții AI și tipurile diferite care există
- Pentru ce fel de sarcini sunt cei mai potriviți Agenții AI
- Componentele de bază pe care le veți folosi la proiectarea unei soluții agentice

## Obiective de Învățare

Până la sfârșitul acestei lecții, ar trebui să puteți:

- Explica ce este un Agent AI și cum diferă de o soluție AI obișnuită
- Ști când să apelați la un Agent AI (și când nu)
- Schițați un design simplu de soluție agentică pentru o problemă din lumea reală

---

## Definirea Agenților AI și Tipuri de Agenți AI

### Ce sunt Agenții AI?

Iată o modalitate simplă de a vă gândi:

> **Agenții AI sunt sisteme care permit Modelelor Lingvistice Mari (LLM-uri) să *facă lucruri* — oferindu-le unelte și cunoștințe pentru a acționa în lume, nu doar să răspundă la solicitări.**

Să desfacem acest lucru puțin:

- **Sistem** — Un Agent AI nu este doar un lucru singular. Este o colecție de părți care lucrează împreună. La bază, fiecare agent are trei componente:
  - **Mediu** — Spațiul în care agentul operează. Pentru un agent de rezervări de călătorie, acesta ar fi chiar platforma de rezervări.
  - **Senzori** — Cum citește agentul starea curentă a mediului său. Agentul nostru de călătorii ar putea verifica disponibilitatea hotelurilor sau prețurile zborurilor.
  - **Actuatori** — Cum ia agentul măsuri. Agentul de călătorii ar putea rezerva o cameră, trimite o confirmare sau anula o rezervare.

![Ce sunt Agenții AI?](../../../translated_images/ro/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Modele Lingvistice Mari** — Agenții existau înaintea LLM-urilor, dar LLM-urile sunt ceea ce face agenții moderni atât de puternici. Ei pot înțelege limbajul natural, pot raționa despre context și pot transforma o cerere vagă a utilizatorului într-un plan concret de acțiune.

- **Execută Acțiuni** — Fără un sistem agent, un LLM doar generează text. Într-un sistem agent, LLM-ul poate cu adevărat *executa* pași — căutând într-o bază de date, apelând o API, trimițând un mesaj.

- **Acces la Unelte** — Ce unelte poate folosi agentul depinde de (1) mediul în care rulează și (2) ce i-a oferit dezvoltatorul. Un agent de călătorii ar putea să caute zboruri, dar să nu poată edita datele clienților — totul depinde de ce legi între unelte.

- **Memorie + Cunoștințe** — Agenții pot avea memorie pe termen scurt (conversația curentă) și memorie pe termen lung (o bază de date a clienților, interacțiuni anterioare). Agentul de călătorii ar putea "ține minte" că preferați locurile lângă geam.

---

### Tipurile Diferite de Agenți AI

Nu toți agenții sunt construiți la fel. Iată o prezentare a principalelor tipuri, folosind un agent de rezervări de călătorii ca exemplu:

| **Tip Agent** | **Ce Face** | **Exemplu Agent de Călătorii** |
|---|---|---|
| **Agenți Reflex Simpli** | Urmează reguli codificate — fără memorie, fără planificare. | Primește un email de reclamație → îl redirecționează către serviciul clienți. Atât. |
| **Agenți Reflex Bazat pe Model** | Păstrează un model intern al lumii și îl actualizează pe măsură ce lucrurile se schimbă. | Monitorizează prețurile istorice ale zborurilor și semnalează rute care devin brusc costisitoare. |
| **Agenți Bazat pe Obiective** | Are un scop în minte și înțelege cum să-l atingă pas cu pas. | Rezervă o excursie completă (zboruri, mașină, hotel) pornind de la locația ta curentă până la destinația dorită. |
| **Agenți Bazat pe Utilitate** | Nu găsește doar *o* soluție — găsește *cea mai bună* analizând compromisurile. | Echilibrează costul vs. comoditatea pentru a găsi călătoria cu cel mai mare scor pentru preferințele tale. |
| **Agenți Învățători** | Devine mai bun în timp pe baza feedback-ului. | Ajustează recomandările viitoare de rezervări bazate pe rezultatele sondajelor după călătorie. |
| **Agenți Ierarhici** | Un agent de nivel înalt împarte munca în sub-sarcini și le delegă agenților de nivel inferior. | O cerere de "anulare a călătoriei" este divizată în: anulare zbor, anulare hotel, anulare închiriere mașină — fiecare gestionată de un sub-agent. |
| **Sisteme Multi-Agent (MAS)** | Mai mulți agenți independenți care lucrează împreună (sau concurează). | Cooperativ: agenți separați se ocupă de hoteluri, zboruri și divertisment. Competitiv: mai mulți agenți concurează să ocupe camere de hotel la cel mai bun preț. |

---

## Când să Folosești Agenți AI

Doar pentru că *poți* folosi un Agent AI nu înseamnă că mereu *trebuie*. Iată situațiile în care agenții chiar excelează:

![Când să folosești Agenți AI?](../../../translated_images/ro/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Probleme Deschise** — Când pașii pentru rezolvarea unei probleme nu pot fi pre-programați. Ai nevoie ca LLM-ul să găsească calea dinamic.
- **Procese cu Mai Mulți Pași** — Sarcini care necesită folosirea uneltelor pe mai multe runde, nu doar o simplă căutare sau generare.
- **Îmbunătățiri În Timp** — Când vrei ca sistemul să devină mai inteligent pe baza feedback-ului utilizatorului sau a semnalelor din mediu.

Vom explora mai în detaliu când (și când *nu*) să folosim Agenți AI în lecția **Construirea Agenților AI de Încredere** mai târziu în curs.

---

## Bazele Soluțiilor Agentice

### Dezvoltarea Agenților

Primul lucru pe care îl faci când construiești un agent este să definești *ce poate face* — uneltele, acțiunile și comportamentele sale.

În acest curs folosim **Microsoft Foundry Agent Service** ca platformă principală. Ea suportă:

- Modele de la furnizori ca OpenAI, Mistral și Meta (Llama)
- Date licențiate de la furnizori ca Tripadvisor
- Definiții standardizate OpenAPI 3.0 pentru unelte

### Modele Agentice

Comunici cu LLM-uri prin prompts. Cu agenții, nu poți crea manual fiecare prompt — agentul trebuie să ia acțiuni în mai mulți pași. Aici intervin **Modelele Agentice**. Sunt strategii reutilizabile pentru prompting și coordonarea LLM-urilor într-un mod mai scalabil și de încredere.

Acest curs este structurat în jurul celor mai comune și utile modele agentice.

### Framework-uri Agentice

Framework-urile Agentice oferă dezvoltatorilor șabloane, unelte și infrastructură pregătite pentru a construi agenți. Fac mai ușor să:

- Leagă unelte și capabilități
- Observe ce face agentul (și să faci depanare când ceva nu merge)
- Colaborezi între mai mulți agenți

În acest curs, ne concentrăm pe **Microsoft Agent Framework (MAF)** pentru a construi agenți gata pentru producție.

---

## Exemple de Cod

Gata să vezi cum funcționează? Iată exemplele de cod pentru această lecție:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Aveți Întrebări?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a vă conecta cu alți cursanți, a participa la orele de birou și a primi răspunsuri la întrebările despre Agenți AI din partea comunității.


---

## Testare Rapidă a Acestui Agent (Opțional)

Odată ce înveți să deployezi agenți în [Lecția 16](../16-deploying-scalable-agents/README.md), poți adăuga un control rapid de sănătate după deploy pentru `TravelAgent` din această lecție folosind catalogul gata făcut [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Vezi [`tests/README.md`](../tests/README.md) pentru detalii despre cum să îl rulezi.

---

## Lecția Anterioară

[Configurarea Cursului](../00-course-setup/README.md)

## Lecția Următoare

[Explorarea Framework-urilor Agentice](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->