# Construirea agenților de utilizare a computerului (CUA)

Agenții de utilizare a computerului pot interacționa cu site-urile web în același mod în care ar face-o o persoană: deschizând un browser, inspectând pagina și făcând următoarea cea mai bună acțiune pe baza a ceea ce văd. În această lecție, vei construi un agent de automatizare a browserului care caută pe Airbnb, extrage date structurate despre listări și identifică cea mai ieftină cazare din Stockholm.

Lecția combină Browser-Use pentru navigare condusă de AI, Playwright și Chrome DevTools Protocol (CDP) pentru controlul browserului, Azure OpenAI pentru raționament cu viziune și Pydantic pentru extracție structurată.

## Introducere

Această lecție va acoperi:

- Înțelegerea cazurilor când agenții de utilizare a computerului sunt mai potriviți decât automatizarea numai prin API
- Combinarea Browser-Use cu Playwright și CDP pentru o gestionare fiabilă a ciclului de viață al browserului
- Utilizarea viziunii Azure OpenAI și a ieșirii structurate Pydantic pentru a extrage date despre listări din pagini web dinamice
- Decizia privind utilizarea unui flux de lucru de automatizare a browserului orientat pe agent, pe actor, sau un hibrid

## Obiectivele de învățare

După finalizarea acestei lecții, vei ști cum să:

- Configurezi Browser-Use cu Azure OpenAI și Playwright
- Construiești un flux de automatizare a browserului care navighează pe un site real și gestionează elemente UI dinamice
- Extragă rezultate tipizate din conținutul vizibil al paginii și să le transformi în logică de business ulterioară
- Alegi între modelele de agent și actor pe baza cât de predictibilă este sarcina browserului

## Exemplu de cod

Această lecție include un tutorial într-un notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Pornește o sesiune Chrome prin CDP, caută listări Airbnb pentru Stockholm, extrage prețuri folosind Browser-Use vision și returnează opțiunea cea mai ieftină ca date structurate.

## Cerințe preliminare

- Python 3.12+
- Configurarea implementării Azure OpenAI în mediul tău
- Chrome sau Chromium instalat local
- Dependențe Playwright instalate
- Familiaritate de bază cu Python asincron

## Instalare

Instalează pachetele folosite în notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Setează variabilele de mediu Azure OpenAI folosite de notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opțional: se utilizează versiunea API cea mai recentă dacă este omisă
AZURE_OPENAI_API_VERSION=...
```

## Prezentare generală a arhitecturii

Notebook-ul demonstrează un flux de lucru hibrid pentru automatizarea browserului:

1. Chrome pornește cu CDP activat astfel încât atât Playwright cât și Browser-Use să împartă aceeași sesiune de browser.
2. Un agent Browser-Use gestionează sarcinile de navigare deschidă, cum ar fi deschiderea Airbnb, închiderea ferestrelor pop-up și căutarea pentru Stockholm.
3. Pagina activă este inspectată folosind un schema Pydantic structurată pentru a extrage titlurile listărilor, prețurile pe noapte, ratingurile și URL-urile.
4. Logica Python compară listările extrase și evidențiază rezultatul cel mai ieftin.

Această abordare păstrează raționamentul flexibil bazat pe viziune de care Browser-Use este capabil, oferindu-ți totodată un control determinist al browserului atunci când ai nevoie.

## Concluzii cheie și bune practici

### Când să folosești Agent în loc de Actor

| Scenariu | Folosește Agent | Folosește Actor |
|----------|----------------|--------------|
| Layout-uri dinamice | Da, AI se poate adapta la schimbările paginii | Nu, selectorii rigizi pot să eșueze |
| Structură cunoscută | Nu, un agent este mai lent decât controlul direct | Da, rapid și precis |
| Găsirea elementelor | Da, limbajul natural funcționează bine | Nu, sunt necesari selectori exacți |
| Controlul timpului | Nu, mai puțin predictibil | Da, control total asupra așteptărilor și încercărilor |
| Fluxuri de lucru complexe | Da, gestionează stările neașteptate ale UI | Nu, necesită ramificări explicite |

### Bune practici Browser-Use

1. Începe cu un agent pentru explorare și navigare dinamică.
2. Comută la control direct al paginii când interacțiunea devine predictibilă.
3. Folosește modele de ieșire structurate astfel încât datele extrase să fie validate și tipizate.
4. Adaugă întârzieri strategic după acțiunile care declanșează schimbări vizibile în UI.
5. Capturează capturi de ecran în timpul iterărilor pentru a facilita depanarea erorilor.
6. Așteaptă-te ca site-urile să se schimbe și proiectează strategii de rezervă pentru ferestre pop-up și schimbări de layout.
7. Combină modelele agent și actor pentru a obține atât flexibilitate, cât și precizie.

### Aplicații în lumea reală

- Rezervări de călătorie și monitorizarea prețurilor
- Compararea prețurilor în comerțul electronic și verificarea disponibilității
- Extracție structurat din site-uri dinamice
- Testare și verificare UI conștientă de viziune
- Monitorizarea și alertarea site-urilor web
- Completarea inteligentă a formularelor în fluxuri multi-pas

## Exemplu real: Microsoft Project Opal

Agentul pe care îl construiești în această lecție este o versiune mică, locală a unui **agent de utilizare a computerului (CUA)** — un program care controlează un browser așa cum ar face-o o persoană. Microsoft aduce această idee în mediul enterprise cu **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, o facilitate în Microsoft 365 Copilot.

Cu Project Opal, descrii o sarcină iar agentul lucrează în numele tău folosind **utilizarea computerului pe un PC cloud securizat Windows 365**, operând prin aplicațiile, site-urile și datele bazate pe browser ale organizației tale. Funcționează **asincron în fundal** și poți ghida munca sau prelua controlul în orice moment. Exemple de sarcini includ:

- Gestionarea cererilor de membership în grupuri de securitate
- Colectarea și validarea dovezilor de audit pentru revizii de conformitate
- Trierea incidentelor IT (actualizarea statusului tichetelor, atribuirea responsabililor, închiderea duplicatelor)
- Compilarea datelor Excel într-o prezentare financiară de închidere

Opal este o referință utilă pentru cum arată un agent de utilizare a computerului **de clasă producție și de încredere** — și întărește conceptele din lecțiile anterioare:

| Concept în acest curs | Cum se aplică Project Opal |
|---------------------|-------------------------|
| **Omul în buclă** (Lecția 06) | Opal se oprește pentru a cere date de autentificare, date sensibile sau instrucțiuni neclare și niciodată nu introduce parole sau nu trimite formulare fără confirmare explicită. Poți *prelua controlul* și *returna controlul* în timpul sarcinii. |
| **Agenți de încredere și securizați** (Lecțiile 06 & 18) | Rulează într-un Windows 365 Cloud PC izolat, este implicit doar browser (accesul la alte resurse al computerului este blocat prin Intune), folosește *identitatea ta* astfel încât accesează doar ce ești autorizat și loghează fiecare acțiune pentru audit. |
| **Planificare și metacogniție** (Lecțiile 07 & 09) | Opal generează un plan pentru sarcină înainte, apoi supraveghează propriul raționament la fiecare pas și se oprește dacă detectează activitate suspectă. |
| **Capabilități / unelte reutilizabile** (Lecția 04) | **Skills** îți permit să scrii instrucțiuni pentru sarcini repetitive (importate dintr-un fișier `.md` sau scrise cu Opal) și să le refolosești în conversații. |

> **Disponibilitate:** Project Opal este disponibil în prezent utilizatorilor din [programul de acces timpuriu Frontier](https://adoption.microsoft.com/copilot/frontier-program/) cu un abonament Microsoft 365 Copilot, iar administratorul tău trebuie să termine configurarea. Fiind o facilitate experimentală Frontier, capabilitățile pot evolua în timp.

## Resurse suplimentare

- [Începe cu Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Template de integrare Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parametri actor Browser-Use și extracție de conținut](https://docs.browser-use.com/customize/actor/all-parameters)
- [Configurare curs](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->