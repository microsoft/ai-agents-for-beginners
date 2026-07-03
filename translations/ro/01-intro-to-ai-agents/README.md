[![Introducere în agenții AI](../../../translated_images/ro/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul pentru această lecție)_

# Introducere în agenții AI și cazuri de utilizare a agenților

Bine ați venit la cursul **Agenți AI pentru începători**! Acest curs vă oferă cunoștințele fundamentale — și cod funcțional real — pentru a începe să construiți agenți AI de la zero.

Veniți să spuneți salut în <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunitatea Azure AI Discord</a> — este plină de cursanți și creatori AI care sunt bucuroși să răspundă la întrebări.

Înainte să începem construcția, să ne asigurăm că înțelegem cu adevărat ce este un agent AI și când are sens să folosim unul.

---

## Introducere

Această lecție acoperă:

- Ce sunt agenții AI și diferitele tipuri care există
- Pentru ce tipuri de sarcini sunt cei mai potriviți agenții AI
- Componentele de bază pe care le veți folosi când proiectați o soluție agentică

## Obiective de învățare

La sfârșitul acestei lecții, ar trebui să fiți capabil să:

- Explicați ce este un agent AI și cum diferă de o soluție AI obișnuită
- Știți când să folosiți un agent AI (și când să nu)
- Schițați un design de soluție agentică de bază pentru o problemă din lumea reală

---

## Definirea agenților AI și tipurile de agenți AI

### Ce sunt agenții AI?

Iată o modalitate simplă de a gândi:

> **Agenții AI sunt sisteme care permit modelelor mari de limbaj (LLM) să *facă efectiv lucruri* — oferindu-le instrumente și cunoștințe pentru a acționa în lume, nu doar pentru a răspunde la solicitări.**

Să descompunem acest lucru puțin:

- **Sistem** — Un agent AI nu este doar un singur lucru. Este o colecție de părți care lucrează împreună. În esență, fiecare agent are trei componente:
  - **Mediu** — Spațiul în care agentul activează. Pentru un agent de rezervări de călătorii, acesta ar fi chiar platforma de rezervări.
  - **Senzori** — Modul în care agentul citește starea actuală a mediului său. Agentul nostru de călătorii ar putea verifica disponibilitatea hotelurilor sau prețurile zborurilor.
  - **Actuatori** — Modul în care agentul ia măsuri. Agentul de călătorii ar putea rezerva o cameră, trimite o confirmare sau anula o rezervare.

![Ce sunt agenții AI?](../../../translated_images/ro/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Modele mari de limbaj** — Agenții existau înaintea LLM-urilor, dar LLM-urile sunt ceea ce îi face pe agenții moderni atât de puternici. Ei pot înțelege limbajul natural, pot raționa despre context și pot transforma o cerere vagă a utilizatorului într-un plan concret de acțiune.

- **Executarea acțiunilor** — Fără un sistem agent, un LLM generează doar text. În cadrul unui sistem agent, LLM-ul poate chiar să *execute* pași — să caute într-o bază de date, să apeleze un API, să trimită un mesaj.

- **Acces la instrumente** — Ce instrumente poate folosi agentul depinde de (1) mediul în care rulează și (2) ceea ce dezvoltatorul a ales să îi ofere. Un agent de călătorii ar putea să poată căuta zboruri, dar să nu poată edita fișele clienților — totul depinde de ce configurați.

- **Memorie + Cunoștințe** — Agenții pot avea memorie pe termen scurt (conversația curentă) și memorie pe termen lung (o bază de date clienți, interacțiuni anterioare). Agentul de călătorii ar putea „ține minte” că preferați locurile la geam.

---

### Diferitele tipuri de agenți AI

Nu toți agenții sunt construiți la fel. Iată o defalcare a principalelor tipuri, folosind ca exemplu un agent de rezervări pentru călătorii:

| **Tip agent** | **Ce face** | **Exemplu agent de călătorii** |
|---|---|---|
| **Agenți reflex simpli** | Urmează reguli codificate — fără memorie, fără planificare. | Primește un e-mail de reclamație → îl redirecționează către serviciul clienți. Atât. |
| **Agenți reflex pe bază de model** | Păstrează un model intern al lumii și îl actualizează pe măsură ce se schimbă lucrurile. | Urmărește prețurile zborurilor din trecut și avertizează rutele care devin brusc scumpe. |
| **Agenți bazati pe obiectiv** | Are un obiectiv în minte și găsește cum să-l îndeplinească pas cu pas. | Rezervă o călătorie completă (zboruri, mașină, hotel) începând de la locația curentă până la destinație. |
| **Agenți bazati pe utilitate** | Nu găsește doar o soluție — găsește *cea mai bună* evaluând compromisurile. | Echilibrează costul versus comoditatea pentru a găsi călătoria care se potrivește cel mai bine preferințelor tale. |
| **Agenți care învață** | Se îmbunătățește în timp învățând din feedback. | Ajustează recomandările viitoare de rezervări pe baza rezultatelor sondajelor post-călătorie. |
| **Agenți ierarhici** | Un agent de nivel înalt împarte munca în subtask-uri și le delegă agenților de nivel inferior. | O comandă de „anulare călătorie” se împarte în: anulare zbor, anulare hotel, anulare închiriere mașină — fiecare fiind gestionată de un subagent. |
| **Sisteme multi-agent (MAS)** | Mai mulți agenți independenți care lucrează împreună (sau concurează). | Cooperativ: agenți separați gestionează hoteluri, zboruri și divertisment. Competitiv: mai mulți agenți concurează să ocupe camere de hotel la cel mai bun preț. |

---

## Când să folosești agenți AI

Doar pentru că *poți* folosi un agent AI nu înseamnă că trebuie să o faci mereu. Iată situațiile în care agenții excelează cu adevărat:

![Când să folosești agenți AI?](../../../translated_images/ro/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Probleme deschise** — Când pașii pentru a rezolva o problemă nu pot fi preprogramați. Ai nevoie ca LLM să descopere calea dinamic.
- **Procese cu mai mulți pași** — Sarcini ce necesită utilizarea instrumentelor pe parcursul mai multor etape, nu doar o simplă interogare sau generare.
- **Îmbunătățire în timp** — Când vrei ca sistemul să devină mai inteligent bazat pe feedback-ul utilizatorului sau semnale din mediu.

Vom detalia mai mult când (și când *nu*) să folosești agenți AI în lecția **Construirea unor agenți AI de încredere**, mai târziu în curs.

---

## Noțiuni de bază despre soluțiile agentice

### Dezvoltarea agenților

Primul lucru pe care îl faci când construiești un agent este să definești *ce poate face* — instrumentele, acțiunile și comportamentele sale.

În acest curs, folosim **Azure AI Agent Service** ca platformă principală. Aceasta suportă:

- Modele de la furnizori precum OpenAI, Mistral și Meta (Llama)
- Date licențiate de la furnizori precum Tripadvisor
- Definiții standardizate de instrumente OpenAPI 3.0

### Modele agentice

Comunici cu LLM-urile prin prompturi. Cu agenții, nu poți crea întotdeauna manual fiecare prompt — agentul trebuie să acționeze pe mai mulți pași. Aici intervin **modelele agentice**. Sunt strategii reutilizabile pentru a trimite prompturi și a orchestra LLM-uri într-un mod mai scalabil și fiabil.

Acest curs este structurat în jurul celor mai comune și utile modele agentice.

### Framework-uri agentice

Framework-urile agentice oferă dezvoltatorilor șabloane, instrumente și infrastructură gata făcute pentru a construi agenți. Ele facilitează:

- Conectarea instrumentelor și capabilităților
- Observarea a ceea ce face agentul (și depanarea când lucrurile nu merg bine)
- Colaborarea între mai mulți agenți

În acest curs, ne concentrăm pe **Microsoft Agent Framework (MAF)** pentru a construi agenți pregătiți pentru producție.

---

## Exemple de cod

Gata să vezi cum funcționează? Iată exemplele de cod pentru această lecție:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Aveți întrebări?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a vă conecta cu alți cursanți, a participa la ore de consultații și a primi răspunsuri la întrebările despre agenții AI din partea comunității.

---

## Lecția anterioară

[Configurare curs](../00-course-setup/README.md)

## Lecția următoare

[Explorarea framework-urilor agentice](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->