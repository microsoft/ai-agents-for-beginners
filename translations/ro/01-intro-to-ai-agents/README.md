[![Intro to AI Agents](../../../translated_images/ro/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul pentru această lecție)_

# Introducere în Agenții AI și Cazuri de Utilizare ale Agenților

Bine ați venit la cursul **Agenți AI pentru Începători**! Acest curs vă oferă cunoștințele fundamentale — și codul funcțional real — pentru a începe să construți Agenți AI de la zero.

Veniți să spuneți „salut” în <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunitatea Azure AI Discord</a> — este plină de cursanți și creatori AI care sunt bucuroși să răspundă la întrebări.

Înainte să trecem la construcție, să ne asigurăm că înțelegem cu adevărat ce este un Agent AI și când are sens să folosești unul.

---

## Introducere

Această lecție acoperă:

- Ce sunt Agenții AI și diferitele tipuri care există
- Pentru ce fel de sarcini sunt cei mai potriviți Agenții AI
- Blocurile de construcție esențiale pe care le veți folosi când proiectați o soluție agentică

## Obiective de Învățare

Până la finalul acestei lecții, ar trebui să puteți:

- Explica ce este un Agent AI și cum se diferențiază de o soluție AI obișnuită
- Ști când să folosiți un Agent AI (și când să nu îl folosiți)
- Desena un schițat de design de soluție agentică pentru o problemă din viața reală

---

## Definirea Agenților AI și Tipurile de Agenți AI

### Ce sunt Agenții AI?

Iată o modalitate simplă de a gândi acest lucru:

> **Agenții AI sunt sisteme care permit Modelelor Mari de Limbaj (LLM) să *facă efectiv lucruri* — oferindu-le unelte și cunoștințe pentru a acționa asupra lumii, nu doar să răspundă la solicitări.**

Hai să descompunem puțin asta:

- **Sistem** — Un Agent AI nu este doar un singur lucru. Este un ansamblu de părți care lucrează împreună. La bază, fiecare agent are trei componente:
  - **Mediu** — Spațiul în care agentul lucrează. Pentru un agent de rezervări de călătorie, acesta ar fi platforma de rezervare în sine.
  - **Senzori** — Modul în care agentul citește starea actuală a mediului său. Agentul nostru de călătorie ar putea verifica disponibilitatea hotelurilor sau prețurile zborurilor.
  - **Actuatori** — Modul în care agentul acționează. Agentul de călătorie ar putea rezerva o cameră, trimite o confirmare sau anula o rezervare.

![What Are AI Agents?](../../../translated_images/ro/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Modele Mari de Limbaj** — Agenții existau înainte de LLM-uri, dar LLM-urile sunt ceea ce face agenții moderni atât de puternici. Ei pot înțelege limbajul natural, pot raționa despre context și pot transforma o cerere vagă a utilizatorului într-un plan concret de acțiune.

- **Realizează Acțiuni** — Fără un sistem agent, un LLM doar generează text. În cadrul unui sistem agent, LLM-ul poate efectiv să *execută* pași — să caute într-o bază de date, să apeleze un API, să trimită un mesaj.

- **Acces la Unelte** — Ce unelte poate folosi agentul depinde de (1) mediul în care rulează și (2) ce a ales dezvoltatorul să îi ofere. Un agent de călătorii ar putea putea căuta zboruri, dar nu edita înregistrări de clienți — totul depinde de ce i se conectează.

- **Memorie + Cunoștințe** — Agenții pot avea memorie pe termen scurt (conversația curentă) și memorie pe termen lung (baza de date a clienților, interacțiuni anterioare). Agentul de călătorie ar putea „ține minte” că preferați locurile lângă geam.

---

### Diferitele Tipuri de Agenți AI

Nu toți agenții sunt construiți la fel. Iată o prezentare generală a principalelor tipuri, folosind un agent de rezervări de călătorie ca exemplu:

| **Tip Agent** | **Ce Face** | **Exemplu Agent de Călătorie** |
|---|---|---|
| **Agenți Reflex Simpli** | Urmează reguli prestabilite — fără memorie, fără planificare. | Vede un email de reclamație → îl transmite serviciului clienți. Atât. |
| **Agenți Reflex Bazati pe Modele** | Păstrează un model intern al lumii și îl actualizează pe măsură ce lucrurile se schimbă. | Monitorizează prețurile zborurilor din trecut și marchează rutele care devin brusc scumpe. |
| **Agenți Bazati pe Obiective** | Are un obiectiv clar și găsește pas cu pas cum să-l atingă. | Rezervă un întreg traseu (zboruri, mașină, hotel) pornind de la locația ta actuală pentru a ajunge la destinație. |
| **Agenți Bazati pe Utilitate** | Nu găsește doar *o* soluție — găsește *cea mai bună* cântărind compromisurile. | Echilibrează costul versus confortul pentru a găsi călătoria care se potrivește cel mai bine preferințelor tale. |
| **Agenți care Învăț** | Devine mai bun în timp, învățând din feedback. | Ajustează recomandările viitoare de rezervare pe baza rezultatelor sondajelor după călătorie. |
| **Agenți Ierarhici** | Un agent de nivel înalt împarte munca în subtask-uri și le delegă către agenți de nivel inferior. | O solicitare de „anularea călătoriei” este împărțită în: anulare zbor, anulare hotel, anulare închirieri auto — fiecare gestionată de un sub-agent. |
| **Sisteme Multi-Agent (MAS)** | Mai mulți agenți independenți care lucrează împreună (sau concurând). | Cooperare: agenți separați se ocupă de hoteluri, zboruri și divertisment. Competitiv: mai mulți agenți concurează pentru a umple camerele de hotel la cel mai bun preț. |

---

## Când să Folosești Agenți AI

Doar pentru că poți folosi un Agent AI nu înseamnă că întotdeauna trebuie să o faci. Iată situațiile în care agenții strălucesc cu adevărat:

![When to use AI Agents?](../../../translated_images/ro/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Probleme Deschise** — Când pașii de rezolvare a unei probleme nu pot fi pre-programați. Ai nevoie ca LLM-ul să găsească dinamic calea.
- **Procese cu Mai Mulți Pași** — Sarcini care necesită folosirea uneltelor pe parcursul mai multor etape, nu doar o simplă căutare sau generare.
- **Îmbunătățire în Timp** — Când vrei ca sistemul să devină mai inteligent pe baza feedback-ului utilizatorului sau semnalelor din mediu.

Vom aprofunda când (și când *nu*) să folosiți Agenți AI în lecția **Construirea Agenților AI de Încredere** mai târziu în curs.

---

## Noțiuni de Bază ale Soluțiilor Agentice

### Dezvoltarea Agenților

Primul lucru pe care îl faci când construiești un agent este să definești *ce poate face* — uneltele, acțiunile și comportamentele sale.

În acest curs folosim **Azure AI Agent Service** ca platforma principală. Acesta suportă:

- Modele de la furnizori precum OpenAI, Mistral și Meta (Llama)
- Date licențiate de la furnizori precum Tripadvisor
- Definiții standardizate de unelte OpenAPI 3.0

### Modele Agentice

Comunici cu LLM-uri prin prompturi. Cu agenții, nu poți întotdeauna să creezi manual fiecare prompt — agentul trebuie să acționeze pe mai mulți pași. Aici intervin **Modelele Agentice**. Sunt strategii reutilizabile pentru prompting și orchestracea LLM-urilor într-un mod mai scalabil și fiabil.

Acest curs este structurat în jurul celor mai comune și utile modele agentice.

### Cadre Agentice

Cadrele agentice oferă dezvoltatorilor șabloane gata făcute, unelte și infrastructură pentru construirea agenților. Fac mai ușor să:

- Conectezi unelte și capabilități
- Observezi ce face agentul (și să depanezi când ceva nu merge bine)
- Colaborezi între mai mulți agenți

În acest curs, ne concentrăm pe **Microsoft Agent Framework (MAF)** pentru construirea agenților pregătiți pentru producție.

---

## Exemple de Cod

Gata să vezi în acțiune? Iată exemplele de cod pentru această lecție:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Ai Întrebări?

Alătură-te pe [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pentru a conecta cu alți cursanți, a participa la ore de birou și a-ți primi răspunsuri la întrebările despre Agenții AI de la comunitate.

---

## Lecția Anterioară

[Configurarea Cursului](../00-course-setup/README.md)

## Lecția Următoare

[Explorarea Cadrelor Agentice](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->