[![Intro to AI Agents](../../../translated_images/ro/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Click pe imaginea de mai sus pentru a vedea videoclipul acestei lecții)_

# Introducere în Agenții AI și Cazuri de Utilizare ale Agenților

Bine ați venit la cursul **Agenți AI pentru Începători**! Acest curs îți oferă cunoștințele fundamentale — și cod funcțional real — pentru a începe să construiești Agenți AI de la zero.

Vino să spui salut în <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunitatea Azure AI pe Discord</a> — este plină de cursanți și constructori de AI care sunt bucuroși să răspundă la întrebări.

Înainte să ne apucăm de construit, să ne asigurăm că înțelegem cu adevărat ce este un Agent AI *și* când are sens să folosești unul.

---

## Introducere

Această lecție acoperă:

- Ce sunt Agenții AI și tipurile diferite care există
- Pentru ce fel de sarcini sunt Agenții AI cei mai potriviți
- Blocurile esențiale de construcție pe care le vei folosi atunci când proiectezi o soluție Agentică

## Obiective de Învățare

Până la sfârșitul acestei lecții, ar trebui să poți:

- Explica ce este un Agent AI și cum diferă de o soluție AI obișnuită
- Știi când să alegi un Agent AI (și când nu)
- Schița un design de bază pentru o soluție Agentică pentru o problemă din viața reală

---

## Definirea Agenților AI și Tipurile de Agenți AI

### Ce sunt Agenții AI?

Iată o modalitate simplă de a gândi:

> **Agenții AI sunt sisteme care permit Modelelor Mari de Limbaj (LLM-uri) să *facă lucruri* — oferindu-le unelte și cunoștințe pentru a acționa asupra lumii, nu doar să răspundă la solicitări.**

Să descompunem puțin:

- **Sistem** — Un Agent AI nu este doar un singur lucru. Este o colecție de părți care lucrează împreună. La bază, fiecare agent are trei componente:
  - **Mediu** — Spațiul în care agentul activează. Pentru un agent de rezervări de călătorii, ar fi platforma de rezervări însăși.
  - **Senzori** — Cum agentul citește starea curentă a mediului său. Agentul nostru de călătorii ar putea verifica disponibilitatea hotelurilor sau prețurile zborurilor.
  - **Actuatori** — Cum agentul ia acțiune. Agentul de călătorii ar putea rezerva o cameră, trimite o confirmare sau anula o rezervare.

![What Are AI Agents?](../../../translated_images/ro/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Modele Mari de Limbaj** — Agenții existau înaintea LLM-urilor, dar LLM-urile sunt cele care fac agenții moderni atât de puternici. Ei pot înțelege limbajul natural, raționa despre context și transforma o solicitare vagă a utilizatorului într-un plan concret de acțiune.

- **Execută acțiuni** — Fără un sistem de agent, un LLM doar generează text. În cadrul unui sistem de agent, LLM-ul poate efectiv *executa* pași — căutarea într-o bază de date, apelarea unei API, trimiterea unui mesaj.

- **Acces la unelte** — Ce unelte poate folosi agentul depinde de (1) mediul în care rulează și (2) ce i-a ales dezvoltatorul să folosească. Un agent de călătorii poate căuta zboruri, dar nu poate edita înregistrările clienților — depinde totul de legăturile pe care le faci.

- **Memorie + Cunoștințe** — Agenții pot avea memorie pe termen scurt (conversația curentă) și memorie pe termen lung (o bază de date a clienților, interacțiuni anterioare). Agentul de călătorii ar putea "ține minte" că preferi locurile lângă geam.

---

### Tipurile Diferite de Agenți AI

Nu toți agenții sunt construiți la fel. Iată o defalcare a tipurilor principale, folosind ca exemplu un agent de rezervări de călătorii:

| **Tip Agent** | **Ce face** | **Exemplu Agent de Călătorii** |
|---|---|---|
| **Agenți Reflex Simpli** | Urmează reguli codificate — fără memorie, fără planificare. | Vezi un email de reclamație → îl transmite către serviciul clienți. Atât. |
| **Agenți Reflex pe Bază de Model** | Păstrează un model intern al lumii și îl actualizează pe măsură ce lucrurile se schimbă. | Urmărește prețurile zborurilor din trecut și semnalează rutele care devin brusc scumpe. |
| **Agenți cu Obiective** | Are un obiectiv în minte și găsește pas cu pas cum să îl atingă. | Rezervă o excursie completă (zboruri, mașină, hotel) începând de la locația ta curentă pentru a te duce la destinație. |
| **Agenți pe Bază de Utilitate** | Nu găsește doar *o* soluție — găsește *cea mai bună* cântărind compromisurile. | Echilibrează costul versus confortul pentru a găsi călătoria care se potrivește cel mai bine preferințelor tale. |
| **Agenți care Învățăt** | Se îmbunătățește în timp învățând din feedback. | Ajustează recomandările viitoare de rezervare în funcție de rezultatele unor sondaje post-excursie. |
| **Agenți ierarhici** | Un agent la nivel înalt împarte munca în sub-sarcini și delegă agenților de nivel inferior. | O cerere de „anulare excursie” este împărțită în: anulare zbor, anulare hotel, anulare mașină — fiecare gestionată de un sub-agent. |
| **Sisteme Multi-Agent (MAS)** | Mai mulți agenți independenți care lucrează împreună (sau concurează). | Cooperativ: agenți separați se ocupă de hoteluri, zboruri și divertisment. Competitiv: mulți agenți concurează pentru a umple camere la hotel la cel mai bun preț. |

---

## Când să folosești Agenți AI

Doar pentru că *poți* folosi un Agent AI nu înseamnă că *trebuie* întotdeauna să o faci. Iată situațiile în care agenții chiar excelează:

![When to use AI Agents?](../../../translated_images/ro/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Probleme deschise** — Când pașii pentru rezolvarea unei probleme nu pot fi preprogramați. Ai nevoie ca LLM-ul să găsească dinamica calea.
- **Procese cu mai mulți pași** — Sarcini care necesită utilizarea uneltelor pe parcursul mai multor runde, nu doar o căutare sau generare unică.
- **Îmbunătățire în timp** — Când dorești ca sistemul să devină mai inteligent pe baza feedback-ului utilizatorului sau a semnalelor din mediu.

Vom aprofunda când (și când *nu*) să folosești Agenți AI în lecția **Construirea Agenților AI de Încredere** mai târziu în curs.

---

## Bazele Soluțiilor Agentice

### Dezvoltarea Agentului

Primul lucru pe care îl faci când construiești un agent este să definești *ce poate face* — uneltele, acțiunile și comportamentele sale.

În acest curs, folosim **Azure AI Agent Service** ca platforma noastră principală. Ea suportă:

- Modele deschise precum OpenAI, Mistral și Llama
- Date licențiate de la furnizori precum Tripadvisor
- Definiții standardizate ale uneltelor OpenAPI 3.0

### Tipare Agentice

Comunici cu LLM-urile prin prompturi. Cu agenții, nu poți întotdeauna să creezi manual fiecare prompt — agentul trebuie să acționeze în mai mulți pași. Aici intră în scenă **Tiparele Agentice**. Sunt strategii reutilizabile pentru prompting și coordonarea LLM-urilor într-un mod mai scalabil și fiabil.

Acest curs este structurat în jurul celor mai comune și utile tipare agentice.

### Framework-uri Agentice

Framework-urile Agentice oferă dezvoltatorilor șabloane gata făcute, unelte și infrastructură pentru a construi agenți. Ele fac mai ușor să:

- Leagă unelte și capacități
- Observe ce face agentul (și să diagnoseze erorile când apar)
- Colaboreze între mai mulți agenți

În acest curs, ne concentrăm pe **Microsoft Agent Framework (MAF)** pentru a construi agenți pregătiți pentru producție.

---

## Exemple de Cod

Gata să vezi totul în acțiune? Iată exemplele de cod pentru această lecție:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Ai întrebări?

Alătură-te la [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pentru a te conecta cu alți cursanți, pentru ore de consultanță și pentru a primi răspunsuri la întrebările tale legate de Agenții AI din partea comunității.

---

## Lecția Anterioară

[Configurarea Cursului](../00-course-setup/README.md)

## Următoarea Lecție

[Explorarea Framework-urilor Agentice](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventuale neînțelegeri sau interpretări greșite care rezultă din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->