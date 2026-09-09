# Construirea agenților pentru utilizarea computerului (CUA)

Agenții de utilizare a computerului pot interacționa cu site-urile web la fel ca o persoană: deschizând un browser, inspectând pagina și luând următoarea cea mai bună acțiune bazată pe ceea ce văd. În această lecție, vei construi un agent de automatizare a browserului care caută pe Airbnb, extrage date structurate despre listări și identifică cea mai ieftină cazare în Stockholm.

Lecția combină Browser-Use pentru navigație ghidată de AI, Playwright și Protocolul Chrome DevTools (CDP) pentru controlul browserului, Azure OpenAI pentru raționament cu viziune și Pydantic pentru extracție structurată.

## Introducere

Această lecție va acoperi:

- Înțelegerea momentului când agenții pentru utilizarea computerului sunt o alegere mai bună decât automatizarea doar prin API
- Combinarea Browser-Use cu Playwright și CDP pentru management fiabil al ciclului de viață al browserului
- Folosirea viziunii Azure OpenAI și a ieșirii structurare Pydantic pentru extragerea datelor despre listări de pe pagini web dinamice
- Deciderea când să folosești un flux de lucru de automatizare a browserului bazat pe agent, actor sau hibrid

## Obiectivele de învățare

După terminarea acestei lecții, vei ști cum să:

- Configurezi Browser-Use cu Azure OpenAI și Playwright
- Construiești un flux de lucru de automatizare a browserului care navighează un site real și gestionează elemente dinamice ale interfeței
- Extragerea rezultatelor tipizate din conținutul vizibil al paginii și transformarea lor în logică de business ulterioară
- Alegi între pattern-urile agent și actor în funcție de cât de predictibilă este sarcina browserului

## Exemplu de cod

Această lecție include un singur tutorial în notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Lansează o sesiune Chrome prin CDP, caută listări Airbnb în Stockholm, extrage prețuri cu Browser-Use vision și returnează cea mai ieftină opțiune ca date structurate.

## Pregătiri

- Python 3.12+
- Implementarea Azure OpenAI configurată în mediu
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
# Opțional: implicit folosește cea mai recentă versiune a API-ului când este omis
AZURE_OPENAI_API_VERSION=...
```

## Prezentare arhitectură

Notebook-ul demonstrează un flux de lucru hibrid pentru automatizarea browserului:

1. Chrome pornește cu CDP activat astfel încât atât Playwright, cât și Browser-Use pot împărți aceeași sesiune de browser.
2. Un agent Browser-Use se ocupă de sarcini de navigare deschise, cum ar fi deschiderea Airbnb, închiderea pop-up-urilor și căutarea pentru Stockholm.
3. Pagina activă este inspectată cu un schema Pydantic structurată pentru a extrage titluri de listări, prețuri pe noapte, evaluări și URL-uri.
4. Logica Python compară listările extrase și evidențiază rezultatul cel mai ieftin.

Această abordare menține raționamentul flexibil bazat pe vizualizare pe care Browser-Use îl oferă, în timp ce oferă control determinist asupra browserului când ai nevoie.

## Concepte cheie și cele mai bune practici

### Când să folosești agent vs actor

| Scenariu | Folosește Agent | Folosește Actor |
|----------|----------------|-------------|
| Layout-uri dinamice | Da, AI se poate adapta la schimbările paginii | Nu, selectorii fragili se pot sparge |
| Structură cunoscută | Nu, un agent este mai lent decât controlul direct | Da, rapid și precis |
| Găsirea elementelor | Da, limbajul natural funcționează bine | Nu, sunt necesari selectori exacți |
| Controlul timpului | Nu, mai puțin predictibil | Da, control complet asupra timpilor de așteptare și a încercărilor |
| Fluxuri complexe | Da, gestionează stări neprevăzute ale UI | Nu, necesită ramificare explicită |

### Cele mai bune practici cu Browser-Use

1. Începe cu un agent pentru explorare și navigație dinamică.
2. Treci la controlul direct al paginii când interacțiunea devine predictibilă.
3. Folosește modele de ieșire structurate pentru ca datele extrase să fie validate și tipizate în siguranță.
4. Adaugă întârzieri strategic după acțiuni care declanșează schimbări vizibile ale UI.
5. Fă capturi de ecran în timpul iterărilor pentru a facilita depanarea erorilor.
6. Așteaptă-te ca site-urile să se schimbe și proiectează strategii de rezervă pentru pop-up-uri și schimbări de layout.
7. Combină pattern-urile agent și actor pentru a obține atât flexibilitate cât și precizie.

### Măsuri de siguranță pentru agenții browserului

Agenții browserului operează pe site-uri live, așa că au nevoie de limite mai stricte decât un script care doar apelează un API cunoscut. Înainte de a trece de la un demo în notebook la un flux de lucru real, definește controalele asupra a ceea ce agentul poate vedea, face click și trimite.

1. **Definirea mediului de navigare.** Rulează agentul într-un profil de browser dedicat sau sandbox și limitează-l la domeniile necesare sarcinii.
2. **Separă observația de acțiune.** Lasă agentul să caute, să citească și să extragă datele mai întâi; solicită un pas explicit de aprobare înainte să trimită formulare, mesaje, rezervări, achiziții, să șteargă înregistrări sau să schimbe setările contului.
3. **Păstrează secretele în afara prompturilor și logurilor.** Nu plasa parole, detalii de plată, cookie-uri de sesiune sau date personale brute în contextul modelului. Lasă utilizatorul să preia autentificarea și să mascheze câmpurile sensibile din loguri.
4. **Tratează conținutul paginii ca input neîncrezător.** Un site web poate conține instrucțiuni destinate agentului, nu utilizatorului. Agentul trebuie să ignore textul paginii care îi cere să-și schimbe scopul, să dezvăluie date, să dezactiveze măsuri de siguranță sau să viziteze site-uri nelegate.
5. **Folosește verificări deterministe în jurul pașilor riscanți.** Verifică URL-ul curent, titlul paginii, elementul selectat, prețul, destinatarul și sumarul acțiunii cu cod înainte de a cere utilizatorului să aprobe pasul final.
6. **Setează bugete și condiții de oprire.** Limitează numărul de acțiuni, încercări, tab-uri și minute pe care le poate folosi agentul. Oprește când starea paginii este ambiguă în loc să continui să faci click.
7. **Înregistrează dovezi utile, nu totul.** Păstrează sumaruri ale acțiunilor, timestamp-uri, URL-uri, descrieri ale elementelor selectate și referințe ale capturilor de ecran pentru a putea revizui erorile fără a stoca conținut sensibil inutil.

În exemplul Airbnb, implicitul sigur este să cauți listări și să extragi prețuri. Autentificarea, contactarea unui gazdă sau finalizarea unei rezervări ar trebui să fie acțiuni aprobate separat de utilizator.

### Aplicații în lumea reală

- Rezervări de călătorii și monitorizare prețuri
- Compararea prețurilor în e-commerce și verificarea disponibilității
- Extragerea structurată de pe site-uri web dinamice
- Testare și verificare UI conștientă de viziune
- Monitorizarea site-urilor web și alerte
- Completarea inteligentă a formularelor pe fluxuri multi-pas

## Exemplu real: Microsoft Project Opal

Agentul pe care îl construiești în această lecție este o versiune mică, locală a unui **agent de utilizare a computerului (CUA)** — un program care conduce un browser așa cum ar face o persoană. Microsoft aduce aceeași idee în întreprinderi cu **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, o capacitate din Microsoft 365 Copilot.

Cu Project Opal, descrii o sarcină și agentul lucrează în numele tău folosind **utilizare a computerului pe un Windows 365 Cloud PC securizat**, operând peste aplicațiile, site-urile și datele tale bazate pe browser. Lucrează **asincron în fundal**, iar tu poți ghida munca sau prelua controlul oricând. Exemple de joburi includ:

- Gestionarea cererilor de apartenență în grupuri de securitate
- Colectarea și validarea dovezilor de audit pentru revizii de conformitate
- Trierea incidentelor IT (actualizarea stării tichetului, asignarea responsabililor, închiderea duplicatelor)
- Compilarea datelor Excel într-un pachet pentru închiderea financiară

Opal este o referință utilă pentru cum arată un agent de utilizare a computerului de **calitate de producție, de încredere** — și întărește conceptele din lecțiile anterioare:

| Concept în acest curs | Cum îl aplică Project Opal |
|-------------------------|------------------------|
| **Human-in-the-loop** (Lecția 06) | Opal se oprește pentru credențiale, date sensibile sau instrucțiuni ambigue și niciodată nu introduce parole sau nu trimite formulare fără confirmare explicită. Poți *prelua controlul* și *returna controlul* în timpul sarcinii. |
| **Agenți siguri și de încredere** (Lecțiile 06 & 18) | Rulează într-un Windows 365 Cloud PC izolat, este doar pentru browser în mod implicit (accesul la alte computere este blocat, impus prin Intune), folosește *identitatea ta* deci accesează doar ce e autorizat, și loghează fiecare acțiune pentru audit. |
| **Planificare și metacogniție** (Lecțiile 07 & 09) | Opal generează un plan pentru job mai întâi, apoi supraveghează propriul raționament după fiecare pas și se oprește dacă detectează activitate suspectă. |
| **Capabilități / unelte reutilizabile** (Lecția 04) | **Skills** îți permit să scrii instrucțiuni pentru joburi repetabile (importate dintr-un fișier `.md` sau create cu Opal) și să le folosești în conversații multiple. |

> **Disponibilitate:** Project Opal este în prezent disponibil utilizatorilor din programul de acces timpuriu [Frontier](https://adoption.microsoft.com/copilot/frontier-program/) cu un abonament Microsoft 365 Copilot, iar administratorul tău trebuie să finalizeze configurarea. Fiind o caracteristică experimentală Frontier, capabilitățile pot evolua în timp.

## Verificarea cunoștințelor

Testează-ți înțelegerea înainte de a trece la următoarea lecție.

**1. Când este un agent de utilizare a browserului o alegere mai bună decât un flux de lucru doar prin API?**

<details>
<summary>Răspuns</summary>

Folosește un agent de browser când sarcina depinde de ceea ce este vizibil în interfața web, site-ul nu oferă API-ul necesar sau pagina se schimbă suficient de des încât logica fixă a API-ului sau selectorului ar fi fragilă. Dacă există un API stabil pentru aceeași sarcină, preferă API-ul deoarece este de obicei mai rapid, mai ușor de testat și mai ușor de securizat.
</details>

**2. Într-un flux hibrid, ce părți ar trebui gestionate de agent și ce părți de codul direct Playwright?**

<details>
<summary>Răspuns</summary>

Lasă agentul să gestioneze navigarea deschisă și stările dinamice ale UI, cum ar fi găsirea paginii corecte sau închiderea pop-up-urilor neașteptate. Comută la control direct Playwright când structura paginii este cunoscută și acțiunea are nevoie de precizie, încercări, așteptări sau validare deterministă.
</details>

**3. Exemplul Airbnb găsește o listare pe care utilizatorul ar putea dori să o rezerve. Ce trebuie să se întâmple înainte ca fluxul să se logheze, să contacteze un gazdă sau să finalizeze o rezervare?**

<details>
<summary>Răspuns</summary>

Fluxul ar trebui să se oprească și să ceară aprobarea explicită a utilizatorului. Înainte să o ceară, ar trebui să afișeze un sumar clar al listării selectate, URL-ul curent, prețul, datele și acțiunea intenționată. Căutarea și extragerea prețurilor poate fi autonomă; accesul la cont, mesajele, achizițiile și rezervările trebuie aprobate de utilizator.
</details>

**4. O pagină web îi spune agentului să ignore instrucțiunile originale, să viziteze un alt site și să dezvăluie credențiale salvate. Cum ar trebui agentul să trateze acest text?**

<details>
<summary>Răspuns</summary>

Tratează-l ca pe conținutul paginii neîncrezător, nu ca o instrucțiune de la dezvoltator sau utilizator. Agentul trebuie să rămână în domeniul și scopul permis, să refuze să dezvăluie secrete și să evite să urmeze textul paginii care schimbă scopul, dezactivează măsurile de siguranță sau îl trimite către site-uri nelegate.
</details>

**5. Ce dovezi sunt utile de păstrat când rulează un agent de browser și ce ar trebui evitat?**

<details>
<summary>Răspuns</summary>

Păstrează sumarurile acțiunilor, timestamp-uri, URL-uri, descrieri ale elementelor selectate, rezultate de validare și referințe la capturi de ecran pentru a putea revizui execuția. Evită stocarea parolelor, detaliilor de plată, cookie-urilor de sesiune, datelor personale brute sau conținutului complet al paginii decât dacă există un motiv specific legat de retenție și confidențialitate.
</details>

## Resurse suplimentare

- [Începe cu Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Template integrare Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parametri actor Browser-Use și extracție conținut](https://docs.browser-use.com/customize/actor/all-parameters)
- [Configurarea cursului](../00-course-setup/README.md)

## Lecția anterioară

[Explorarea Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Lecția următoare

[Dezvoltarea agenților scalabili](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->