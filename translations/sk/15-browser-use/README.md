# Budovanie agentov počítačového používania (CUA)

Agenti počítačového používania môžu interagovať so stránkami rovnakým spôsobom ako človek: otvorením prehliadača, kontrolou stránky a vykonaním najlepšieho možného kroku na základe toho, čo vidia. V tejto lekcii si vytvoríte agenta automatizácie prehliadača, ktorý vyhľadá na Airbnb, extrahuje štruktúrované údaje o ponukách a nájde najlacnejšie ubytovanie v Štokholme.

Lekcia kombinuje Browser-Use pre AI-riadenú navigáciu, Playwright a Chrome DevTools Protocol (CDP) pre ovládanie prehliadača, Azure OpenAI pre rozumovanie s podporou videnia a Pydantic pre štruktúrovanú extrakciu.

## Úvod

Táto lekcia bude pokrývať:

- Pochopenie, kedy sú agenti počítačového používania vhodnejší než automatizácia založená len na API
- Kombinovanie Browser-Use s Playwright a CDP pre spoľahlivú správu životného cyklu prehliadača
- Využitie Azure OpenAI vízie a štruktúrovaného výstupu Pydantic na extrahovanie údajov o ponukách z dynamických webových stránok
- Rozhodovanie, kedy použiť agent-first, actor-first alebo hybridný pracovný tok pre automatizáciu prehliadača

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

- Nakonfigurovať Browser-Use s Azure OpenAI a Playwright
- Vytvoriť pracovný tok automatizácie prehliadača, ktorý naviguje na reálnu webovú stránku a zvláda dynamické UI prvky
- Extrahovať typované výsledky z viditeľného obsahu stránky a premeniť ich na obchodnú logiku
- Vybrať medzi vzormi agent a actor na základe predvídateľnosti úlohy prehliadača

## Ukážkový kód

Táto lekcia obsahuje jeden notebookový návod:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Spúšťa reláciu Chrome cez CDP, vyhľadáva na Airbnb ponuky v Štokholme, extrahuje ceny pomocou Browser-Use vision a vracia najlacnejšiu možnosť ako štruktúrované údaje.

## Požiadavky

- Python 3.12+
- Azure OpenAI deployment nakonfigurovaný vo vašom prostredí
- Lokálne nainštalovaný Chrome alebo Chromium
- Nainštalované závislosti Playwright
- Základná znalosť asynchrónneho Pythonu

## Nastavenie

Nainštalujte balíčky použité v notebooku:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Nastavte environmentálne premenné Azure OpenAI, ktoré používa notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Voliteľné: predvolene sa použije najnovšia verzia API, ak nie je zadaná
AZURE_OPENAI_API_VERSION=...
```

## Prehľad architektúry

Notebook demonštruje hybridný pracovný tok automatizácie prehliadača:

1. Chrome sa spúšťa s povoleným CDP, takže Playwright aj Browser-Use môžu zdieľať tú istú reláciu prehliadača.
2. Agent Browser-Use rieši otvorené úlohy navigácie, ako je otvorenie Airbnb, zatváranie vyskakovacích okien a vyhľadávanie Štokholmu.
3. Aktívna stránka je kontrolovaná pomocou štruktúrovaného Pydantic schémy na extrakciu názvov ponúk, cien za noc, hodnotení a URL.
4. Pythonovská logika porovná extrahované ponuky a zvýrazní najlacnejší výsledok.

Tento prístup si zachováva flexibilné, na videnie založené rozumovanie, v ktorom je Browser-Use dobrý, pričom stále poskytuje deterministickú kontrolu prehliadača, keď je to potrebné.

## Kľúčové poznatky a najlepšie praktiky

### Kedy použiť agenta vs aktéra

| Scenár | Použiť agenta | Použiť aktéra |
|----------|-----------|-----------|
| Dynamické rozloženia | Áno, AI sa dokáže prispôsobiť zmenám stránky | Nie, krehké selektory môžu zlyhať |
| Známá štruktúra | Nie, agent je pomalší než priamy kontrolný kód | Áno, rýchly a presný |
| Nájdenie prvkov | Áno, prirodzený jazyk funguje dobre | Nie, potrebné sú presné selektory |
| Riadenie časovania | Nie, menej predvídateľné | Áno, plná kontrola nad čakaniami a opakovaniami |
| Zložité pracovné toky | Áno, zvláda neočakávané stavy UI | Nie, vyžaduje explicitné vetvenie |

### Najlepšie praktiky Browser-Use

1. Začnite s agentom na prieskum a dynamickú navigáciu.
2. Prejdite na priamu kontrolu stránky, keď je interakcia predvídateľná.
3. Používajte štruktúrované modely výstupu, aby extrahované údaje boli overené a typovo bezpečné.
4. Pridávajte oneskorenia strategicky po akciách, ktoré vyvolávajú viditeľné zmeny UI.
5. Zachytávajte snímky obrazovky počas iterácií, aby bolo jednoduchšie dekódovať chyby.
6. Očakávajte zmeny webových stránok a navrhnite náhradné stratégie pre vyskakovacie okná a zmeny rozloženia.
7. Kombinujte vzory agenta a aktéra, aby ste získali flexibilitu aj presnosť.

### Bezpečnostné opatrenia pre browser agentov

Agenti prehliadača pracujú na živých webových stránkach, preto potrebujú prísnejšie hranice než skript, ktorý volá len známe API. Pred prechodom z ukážky v notebooku na reálny pracovný tok definujte obmedzenia toho, čo agent môže vidieť, na čo kliknúť a čo odosielať.

1. **Obmedzte prostredie prehliadania.** Spúšťajte agenta v samostatnom profile prehliadača alebo sandboxe a obmedzte ho len na domény potrebné pre úlohu.
2. **Oddelte pozorovanie od akcie.** Nechajte agenta najprv vyhľadávať, čítať a extrahovať údaje; vyžadujte explicitné schválenie pred odoslaním formulárov, správ, rezervácií, nákupov, mazania záznamov alebo zmien v nastaveniach účtu.
3. **Nepoužívajte tajné údaje v promptoch a záznamoch.** Nevkladajte heslá, platobné údaje, session cookies ani surové osobné údaje do kontextu modelu. Nech užívateľ prevezme overovanie a zmaže citlivé polia z logov.
4. **Zaobchádzajte s obsahom stránky ako s nedôveryhodnými údajmi.** Web môže obsahovať pokyny určené agentovi, nie užívateľovi. Agent by mal ignorovať texty, ktoré ho žiadajú zmeniť cieľ, odhaliť údaje, vypnúť ochrany alebo navštíviť nesúvisiace stránky.
5. **Používajte deterministické kontroly rizikových krokov.** Overujte aktuálnu URL, titulok stránky, vybraný prvok, cenu, príjemcu a zhrnutie akcie kódom predtým, než požiadate užívateľa o schválenie konečného kroku.
6. **Nastavte rozpočty a podmienky zastavenia.** Obmedzte počet krokov, opakovaní, otvorených kariet a minút, ktoré môže agent využiť. Zastavte, keď je stav stránky nejasný, namiesto pokračovania v kliknutí.
7. **Zaznamenávajte užitočné dôkazy, nie všetko.** Uchovávajte zhrnutia akcií, časové pečiatky, URL, popisy vybraných prvkov a referencie snímok obrazovky, aby bolo možné spustenie skontrolovať bez uchovávania zbytočného citlivého obsahu stránky.

V ukážke Airbnb je bezpečný predvolený režim vyhľadávať ponuky a extrahovať ceny. Prihlasovanie, kontaktovanie hostiteľa alebo dokončenie rezervácie by mala byť samostatná akcia schválená užívateľom.

### Reálne použitia

- Rezervácie cestovania a monitorovanie cien
- Porovnávanie cien a kontrola dostupnosti v e-commerce
- Štruktúrovaná extrakcia z dynamických webových stránok
- Testovanie a overovanie UI s podporou videnia
- Monitorovanie webu a upozornenia
- Inteligentné vypĺňanie formulárov v multi-krokových procesoch

## Reálny príklad: Microsoft Project Opal

Agent, ktorého si vytvoríte v tejto lekcii, je malá, lokálna verzia **agenta počítačového používania (CUA)** — programu, ktorý ovláda prehliadač tak, ako by to robil človek. Microsoft prináša tento istý koncept do podnikov s **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, funkciou v Microsoft 365 Copilot.

S Project Opal popíšete úlohu a agent na váš účet pracuje pomocou **počítačového používania na zabezpečenom Windows 365 Cloud PC**, fungujúceho v rámci prehliadačových aplikácií, stránok a dát vašej organizácie. Pracuje **asynchrónne na pozadí** a kedykoľvek môžete smerovať jeho prácu alebo prevziať kontrolu. Príklady úloh sú:

- Správa žiadostí o členstvo v bezpečnostných skupinách
- Zhromažďovanie a overovanie auditných dôkazov pre kontrolu súladu
- Riešenie IT incidentov (aktualizácia stavu ticketu, priraďovanie majiteľov, uzatváranie duplikátov)
- Kompilovanie dát z Excelu do finančnej záverečnej správy

Opal je užitočný vzor toho, ako vyzerá **produkčne použiteľný, dôveryhodný** agent počítačového používania — a potvrdzuje koncepty z predchádzajúcich lekcií:

| Koncept v tomto kurze | Ako ho Project Opal aplikuje |
|------------------------|-----------------------------|
| **Človek v slučke** (lekcia 06) | Opal sa zastaví pri prihlasovaní, citlivých údajoch alebo nejednoznačných inštrukciách a nikdy nezadáva heslá ani neodosiela formuláre bez explicitného potvrdenia. Môžete *prevziať kontrolu* a *vrátiť kontrolu* počas úlohy. |
| **Dôveryhodní a bezpeční agenti** (lekcie 06 a 18) | Beží v izolovanom Windows 365 Cloud PC, je predvolene iba prehliadačový (iný prístup k počítaču je blokovaný, vynucované cez Intune), používa *vašu* identitu, takže pristupuje len k autorizovaným zdrojom a zaznamenáva každý krok na audit. |
| **Plánovanie a metakognícia** (lekcie 07 a 09) | Opal najskôr vytvorí plán úlohy, potom dohliada na vlastné rozumovanie v každom kroku a zastaví sa, ak zistí podozrivú aktivitu. |
| **Znovupoužiteľné schopnosti / nástroje** (lekcia 04) | **Zručnosti** umožňujú písať inštrukcie pre opakovateľné úlohy (importované zo súboru `.md` alebo vytvorené v Opal) a opakovane ich používať v konverzáciách. |

> **Dostupnosť:** Project Opal je momentálne k dispozícii používateľom v [skorom prístupe Frontier](https://adoption.microsoft.com/copilot/frontier-program/) s predplatným Microsoft 365 Copilot a nastavenie musí vykonať správca. Pretože ide o experimentálnu funkciu Frontier, schopnosti sa môžu časom meniť.

## Kontrola vedomostí

Otestujte svoje porozumenie pred prechodom na ďalšiu lekciu.

**1. Kedy je agent počítačového používania založený na prehliadači vhodnejší než workflow založený len na API?**

<details>
<summary>Odpoveď</summary>

Použite agenta prehliadača, keď úloha závisí od toho, čo je viditeľné v webovom UI, stránka neponúka potrebné API alebo sa stránka dostatočne často mení, že fixné API alebo selektorová logika by boli krehké. Ak existuje stabilné API pre tú istú úlohu, uprednostnite API, pretože je zvyčajne rýchlejšie, jednoduchšie testovateľné a bezpečnejšie.
</details>

**2. V hybridnom pracovnom toku, ktoré časti by mal riešiť agent a ktoré priamy Playwright kód?**

<details>
<summary>Odpoveď</summary>

Nechajte agenta riešiť otvorené navigačné úlohy a dynamické UI stavy, napríklad nájdenie správnej stránky alebo zatváranie neočakávaných vyskakovacích okien. Prejdite na priamu kontrolu Playwright, keď je štruktúra stránky známa a akcia potrebuje presnosť, opakovania, čakania alebo deterministickú validáciu.
</details>

**3. Ukážka Airbnb nájde ponuku, ktorú by používateľ mohol chcieť rezervovať. Čo by sa malo stať pred tým, než workflow vykoná prihlásenie, kontaktuje hostiteľa alebo dokončí rezerváciu?**

<details>
<summary>Odpoveď</summary>

Workflow by sa mal zastaviť a požiadať o explicitné schválenie používateľa. Pred žiadosťou by mal zobraziť jasné zhrnutie vybranej ponuky, aktuálnu URL, cenu, dátumy a zamýšľanú akciu. Vyhľadávanie a extrahovanie cien môže byť autonómne; prístup k účtu, správy, nákupy a rezervácie by mali byť schválené používateľom.
</details>

**4. Webová stránka povie agentovi, aby ignoroval svoje pôvodné inštrukcie, navštívil inú stránku a odhalil uložené prihlasovacie údaje. Ako by mal agent k tomuto textu pristupovať?**

<details>
<summary>Odpoveď</summary>

Zaobchádzajte s tým ako s nedôveryhodným obsahom stránky, nie ako s inštrukciou od vývojára alebo používateľa. Agent by mal ostať v rámci povoleného doménového okruhu a rozsahu úlohy, odmietnuť odhaliť tajomstvá a vyhýbať sa sledovaniu textu stránky, ktorý mení cieľ, vypína ochrany alebo nasmerúva na nesúvisiace stránky.
</details>

**5. Aké dôkazy je užitočné uchovávať, keď agent prehliadača beží, a čomu sa treba vyhnúť?**

<details>
<summary>Odpoveď</summary>

Uchovávajte zhrnutia akcií, časové pečiatky, URL, popisy vybraných prvkov, výsledky validácie a referencie na snímky obrazovky, aby bežec bolo možné skontrolovať. Vyhnite sa ukladaniu hesiel, platobných údajov, session cookies, surových osobných údajov alebo kompletného obsahu stránok, pokiaľ neexistuje konkrétny dôvod pre ich zadržanie a ochranu súkromia.
</details>

## Ďalšie zdroje

- [Začíname s Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integračný šablón](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use parametre aktéra a extrakcia obsahu](https://docs.browser-use.com/customize/actor/all-parameters)
- [Nastavenie kurzu](../00-course-setup/README.md)

## Predchádzajúca lekcia

[Preskúmanie Frameworku Microsoft Agent](../14-microsoft-agent-framework/README.md)

## Nasledujúca lekcia

[Nasadzovanie škálovateľných agentov](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->