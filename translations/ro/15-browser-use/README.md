# Construirea agenților pentru utilizarea computerului (CUA)

Agenții pentru utilizarea computerului pot interacționa cu site-urile web în același mod în care o face o persoană: deschizând un browser, inspectând pagina și făcând cea mai bună acțiune următoare bazată pe ceea ce văd. În această lecție, vei construi un agent de automatizare a browserului care caută pe Airbnb, extrage date structurate despre listări și identifică cea mai ieftină cazare din Stockholm.

Lecția combină Browser-Use pentru navigare controlată de AI, Playwright și Chrome DevTools Protocol (CDP) pentru controlul browserului, Azure OpenAI pentru raționamente cu vedere și Pydantic pentru extragere structurată.

## Introducere

Această lecție va acoperi:

- Înțelegerea când agenții pentru utilizarea computerului sunt mai potriviți decât automatizarea bazată numai pe API
- Combinarea Browser-Use cu Playwright și CDP pentru gestionarea fiabilă a ciclului de viață al browserului
- Folosirea viziunii Azure OpenAI și a ieșirii structurate Pydantic pentru extragerea datelor despre listări de pe pagini web dinamice
- Decizia când să se folosească un flux de lucru de automatizare a browserului bazat pe agent, actor sau hibrid

## Obiective de învățare

După finalizarea acestei lecții, vei ști cum să:

- Configurezi Browser-Use cu Azure OpenAI și Playwright
- Construiești un flux de lucru de automatizare a browserului care navighează pe un site real și gestionează elementele UI dinamice
- Extragi rezultate tipizate din conținutul vizibil al paginii și să le transformi în logică de afaceri ulterioară
- Alegi între modele agent și actor în funcție de cât de predictibilă este sarcina browserului

## Exemplu de cod

Această lecție include un tutorial în notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Deschide o sesiune Chrome peste CDP, caută listările Airbnb pentru Stockholm, extrage prețurile cu viziunea Browser-Use și returnează opțiunea cea mai ieftină ca date structurate.

## Cerințe prealabile

- Python 3.12+
- Implementare Azure OpenAI configurată în mediul tău
- Chrome sau Chromium instalat local
- Dependențe Playwright instalate
- Familiaritate de bază cu Python asincron

## Configurare

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
# Opțional: implicit folosește cea mai recentă versiune API când este omis
AZURE_OPENAI_API_VERSION=...
```

## Prezentare generală a arhitecturii

Notebook-ul demonstrează un flux de lucru de automatizare hibridă a browserului:

1. Chrome pornește cu CDP activat astfel încât atât Playwright cât și Browser-Use să poată partaja aceeași sesiune de browser.
2. Un agent Browser-Use gestionează sarcini de navigare deschisă, cum ar fi deschiderea Airbnb, închiderea pop-up-urilor și căutarea pentru Stockholm.
3. Pagina activă este inspectată cu un schema Pydantic structurată pentru a extrage titlurile listărilor, prețurile pe noapte, ratingurile și URL-urile.
4. Logica Python compară listările extrase și evidențiază rezultatul cel mai ieftin.

Această abordare păstrează raționamentul flexibil bazat pe vedere care este specific Browser-Use, oferindu-ți în același timp control determinist asupra browserului când ai nevoie.

## Concluzii cheie și cele mai bune practici

### Când să folosești agent vs actor

| Scenariu | Folosește agent | Folosește actor |
|----------|-----------------|--------------|
| Layout-uri dinamice | Da, AI se poate adapta la schimbările paginii | Nu, selectorii fragili pot ceda |
| Structură cunoscută | Nu, un agent este mai lent decât controlul direct | Da, rapid și precis |
| Găsirea elementelor | Da, limbajul natural funcționează bine | Nu, sunt necesari selectorii exacți |
| Controlul timpului | Nu, mai puțin predictibil | Da, control complet asupra așteptărilor și încercărilor |
| Fluxuri de lucru complexe | Da, gestionează stări UI neașteptate | Nu, necesită ramificări explicite |

### Cele mai bune practici Browser-Use

1. Pornește cu un agent pentru explorare și navigare dinamică.
2. Treci la controlul direct al paginii când interacțiunea devine predictibilă.
3. Folosește modele de ieșire structurate astfel încât datele extrase să fie validate și tip-sigure.
4. Adaugă întârzieri strategic după acțiuni care declanșează schimbări vizibile în UI.
5. Capturează capturi de ecran în timpul iterării pentru a face eșecurile mai ușor de depanat.
6. Așteaptă-te ca site-urile să se schimbe și proiectează strategii alternative pentru pop-up-uri și schimbări de layout.
7. Combină modelele agent și actor pentru a obține atât flexibilitate, cât și precizie.

### Măsuri de siguranță pentru agenții browser

Agenții browser operează pe site-uri live, deci au nevoie de limite mai stricte decât un script care apelează doar un API cunoscut. Înainte de a trece de la un demo în notebook la un flux real, definește controlul asupra a ceea ce agentul poate vedea, apăsa și trimite.

1. **Definește mediul de navigare.** Rulează agentul într-un profil dedicat al browserului sau într-un sandbox și limitează-l la domeniile necesare sarcinii.
2. **Separă observarea de acțiune.** Permite agentului să caute, să citească și să extragă date mai întâi; necesită un pas explicit de aprobare înainte să trimită formulare, să trimită mesaje, să rezerve călătorii, să facă achiziții, să șteargă înregistrări sau să schimbe setările contului.
3. **Păstrează secretele în afara prompturilor și urmăririlor.** Nu plasa parole, detalii de plată, cookie-uri de sesiune sau date personale brute în contextul modelului. Permite utilizatorului să preia autentificarea și să redacteze câmpurile sensibile din jurnale.
4. **Tratează conținutul paginii ca intrare nesigură.** Un site web poate conține instrucțiuni destinate agentului, nu utilizatorului. Agentul ar trebui să ignore textele paginii care îi cer să-și schimbe scopul, să dezvăluie date, să dezactiveze măsuri de siguranță sau să viziteze site-uri nelegate.
5. **Folosește verificări deterministe în jurul pașilor riscanți.** Verifică URL-ul curent, titlul paginii, elementul selectat, prețul, destinatarul și sumarul acțiunii cu cod înainte de a cere utilizatorului să aprobe pasul final.
6. **Setează bugete și condiții de oprire.** Limitează numărul de acțiuni, încercări, file și minute pe care agentul le poate folosi. Opresc când starea paginii este ambiguă în loc să continue să apese.
7. **Înregistrează dovezi utile, nu totul.** Păstrează sumaruri de acțiuni, timpi, URL-uri, descrieri ale elementelor selectate și referințe la capturi de ecran astfel încât eșecurile să poată fi revizuite fără a stoca conținut sensibil inutil din pagină.

În exemplul Airbnb, implicitul sigur este să cauți listări și să extragi prețuri. Autentificarea, contactarea unui gazdă sau finalizarea unei rezervări ar trebui să fie o acțiune separată aprobată de utilizator.

### Aplicații din lumea reală

- Rezervarea de călătorii și monitorizarea prețurilor
- Compararea prețurilor în e-commerce și verificări de disponibilitate
- Extragerea structurată din site-uri dinamice
- Testarea și verificarea UI cu conștientizare vizuală
- Monitorizarea și alertarea site-urilor web
- Completarea inteligentă a formularelor în fluxuri multi-step

## Exemplu din lumea reală: Microsoft Project Opal

Agentul pe care îl construiești în această lecție este o versiune mică, locală, a unui **agent de utilizare a computerului (CUA)** — un program care controlează un browser așa cum ar face o persoană. Microsoft aduce această idee pentru companii cu **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, o capacitate în Microsoft 365 Copilot.

Cu Project Opal, descrii o sarcină și agentul lucrează în numele tău folosind **utilizarea computerului pe un Windows 365 Cloud PC securizat**, operând în aplicațiile, site-urile și datele organizației tale bazate pe browser. Lucrează **asincron în fundal**, iar tu poți ghida munca sau prelua controlul în orice moment. Exemple de sarcini includ:

- Gestionarea cererilor pentru membership-ul grupurilor de securitate
- Colectarea și validarea dovezilor de audit pentru revizuiri de conformitate
- Trierea incidentelor IT (actualizarea stării tichetelor, alocarea proprietarilor, închiderea duplicatelor)
- Compilarea datelor Excel într-o prezentare financiară de închidere

Opal este o referință utilă pentru cum arată un agent de utilizare computerizată **de producție și de încredere** — și susține conceptele din lecțiile anterioare:

| Concept în acest curs | Cum îl aplică Project Opal |
|-------------------|--------------------|
| **Human-in-the-loop** (Lecția 06) | Opal face pauză pentru acreditări de autentificare, date sensibile sau instrucțiuni ambigue și niciodată nu introduce parole sau nu trimite formulare fără confirmare explicită. Poți *Prelua Controlul* și *Returna Controlul* în timpul sarcinii. |
| **Agenți de încredere și securizați** (Lecțiile 06 & 18) | Rulează într-un Windows 365 Cloud PC izolat, e doar browser (acces la alt computer blocat, impus prin Intune), folosește *identitatea ta* pentru a accesa doar ce ai autorizare și înregistrează fiecare acțiune pentru audit. |
| **Planificare și metacogniție** (Lecțiile 07 & 09) | Opal generează planul pentru sarcină, apoi supraveghează propriul raționament la fiecare pas și face pauză dacă detectează activitate suspectă. |
| **Capabilități / unelte reutilizabile** (Lecția 04) | **Skills** îți permit să scrii instrucțiuni pentru sarcini repetabile (importate dintr-un fișier `.md` sau create în Opal) și să le refolosești în convorbiri. |

> **Disponibilitate:** Project Opal este disponibil în prezent utilizatorilor din [programul de acces timpuriu Frontier](https://adoption.microsoft.com/copilot/frontier-program/) cu un abonament Microsoft 365 Copilot, iar administratorul tău trebuie să finalizeze configurarea. Fiind o caracteristică experimentală Frontier, capabilitățile se pot schimba în timp.

## Resurse suplimentare

- [Începe cu Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Template integrare Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parametrii actorului Browser-Use și extragerea conținutului](https://docs.browser-use.com/customize/actor/all-parameters)
- [Configurarea cursului](../00-course-setup/README.md)

## Lecția precedentă

[Explorarea Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Lecția următoare

[Implementarea agenților scalabili](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->