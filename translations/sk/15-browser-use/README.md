# Vytváranie agentov na používanie počítača (CUA)

Agenti na používanie počítača môžu interagovať s webovými stránkami rovnakým spôsobom ako človek: otvorením prehliadača, preskúmaním stránky a vykonaním najvhodnejšieho ďalšieho kroku na základe toho, čo vidia. V tejto lekcii vytvoríte automatizačného agenta prehliadača, ktorý vyhľadáva na Airbnb, extrahuje štruktúrované údaje o ponukách a identifikuje najlacnejšie ubytovanie v Štokholme.

Lekcia kombinuje Browser-Use pre navigáciu riadenú AI, Playwright a Chrome DevTools Protocol (CDP) na ovládanie prehliadača, Azure OpenAI pre videním podporované uvažovanie a Pydantic pre štruktúrovanú extrakciu.

## Úvod

Táto lekcia pokrýva:

- Pochopenie, kedy sú agenti na používanie počítača vhodnejší ako automatizácia založená iba na API
- Kombinovanie Browser-Use s Playwright a CDP pre spoľahlivé riadenie životného cyklu prehliadača
- Použitie videnia Azure OpenAI a štruktúrovaného výstupu Pydantic na extrakciu údajov o ponukách z dynamických webových stránok
- Rozhodovanie, kedy použiť workflow automatizácie prehliadača založený na agentovi, aktérovi alebo hybrid

## Ciele učenia sa

Po dokončení tejto lekcie budete vedieť:

- Konfigurovať Browser-Use s Azure OpenAI a Playwright
- Vytvoriť pracovný tok automatizácie prehliadača, ktorý prechádza skutočnú webovú stránku a spracováva dynamické UI prvky
- Extrahovať typované výsledky zo zobrazeného obsahu stránky a premeniť ich na ďalšiu obchodnú logiku
- Vybrať medzi vzormi agenta a aktéra na základe toho, ako predvídateľná je úloha prehliadača

## Ukážka kódu

Táto lekcia obsahuje jeden tutoriál v notebooku:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Spúšťa reláciu Chrome cez CDP, vyhľadáva na Airbnb ponuky v Štokholme, extrahuje ceny pomocou Browser-Use vision a vracia najlacnejšiu možnosť ako štruktúrované údaje.

## Predpoklady

- Python 3.12+
- Konfigurácia nasadenia Azure OpenAI vo vašom prostredí
- Lokálne nainštalovaný Chrome alebo Chromium
- Nainštalované závislosti Playwright
- Základná znalosť asynchrónneho Pythonu

## Nastavenie

Nainštalujte balíky použité v notebooku:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Nastavte Azure OpenAI premenné prostredia používané v notebooku:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Voliteľné: predvolene používa najnovšiu verziu API, ak je vynechané
AZURE_OPENAI_API_VERSION=...
```

## Prehľad architektúry

Notebook demonštruje hybridný pracovný tok automatizácie prehliadača:

1. Chrome sa spustí s CDP povoleným, aby mohli Playwright aj Browser-Use zdieľať rovnakú reláciu prehliadača.
2. Agent Browser-Use rieši otvorené navigačné úlohy, ako je otvorenie Airbnb, zatvorenie vyskakovacích okien a vyhľadávanie Štokholmu.
3. Aktívna stránka sa kontroluje pomocou štruktúrovanej schémy Pydantic na extrakciu názvov ponúk, cien za noc, hodnotení a URL.
4. Python logika porovnáva extrahované ponuky a zvýrazňuje najlacnejší výsledok.

Tento prístup zachováva flexibilné uvažovanie založené na videní, v ktorom je Browser-Use dobrý, pričom stále poskytuje deterministickú kontrolu prehliadača, keď ju potrebujete.

## Kľúčové poznatky a osvedčené postupy

### Kedy použiť agenta vs aktéra

| Scenár | Použiť agenta | Použiť aktéra |
|----------|-----------|-----------|
| Dynamické rozloženia | Áno, AI sa dokáže prispôsobiť zmenám na stránke | Nie, krehké selektory môžu zlyhať |
| Známá štruktúra | Nie, agent je pomalší ako priama kontrola | Áno, rýchly a presný |
| Nájdenie prvkov | Áno, prirodzený jazyk funguje dobre | Nie, sú potrebné presné selektory |
| Riadenie časovania | Nie, menej predvídateľné | Áno, plná kontrola nad čakaniami a opakovaniami |
| Komplexné workflow | Áno, zvláda neočakávané stavy UI | Nie, vyžaduje explicitné vetvenie |

### Najlepšie postupy pre Browser-Use

1. Začnite s agentom pre prieskum a dynamickú navigáciu.
2. Prepnite na priamu kontrolu stránky, keď sa interakcia stane predvídateľnou.
3. Používajte štruktúrované výstupné modely, aby boli extrahované údaje validované a typovo bezpečné.
4. Pridávajte strategicky oneskorenia po akciách, ktoré spúšťajú viditeľné zmeny UI.
5. Zachytávajte screenshoty počas iterácie, aby bolo ľahšie odhaliť chyby.
6. Očakávajte zmeny na webových stránkach a navrhnite záložné stratégie pre vyskakovacie okná a posuny rozloženia.
7. Kombinujte vzory agenta a aktéra, aby ste získali flexibilitu aj presnosť.

### Bezpečnostné opatrenia pre agentov prehliadača

Agenti prehliadača pracujú na živých webových stránkach, preto potrebujú prísnejšie hranice než skript, ktorý volá len známe API. Pred prechodom z demo ukážky v notebooku na reálny pracovný tok definujte kontroly toho, čo agent môže vidieť, klikať a odosielať.

1. **Obmedzte prostredie prehliadania.** Spúšťajte agenta v samostatnom profile prehliadača alebo sandboxe a obmedzte ho na domény potrebné pre úlohu.
2. **Oddelte pozorovanie od akcie.** Nechajte agenta najprv vyhľadávať, čítať a extrahovať údaje; vyžadujte explicitné schválenie pred odoslaním formulárov, správ, rezervácií, nákupov, odstraňovania záznamov alebo zmien nastavení účtu.
3. **Nedávajte tajné údaje do promptov alebo záznamov.** Nevkladajte heslá, platobné údaje, cookies relácie alebo surové osobné údaje do kontextu modelu. Nechajte používateľa, aby prevzal autentifikáciu a cenzuroval citlivé polia z logov.
4. **Považujte obsah stránky za nedôveryhodný vstup.** Webová stránka môže obsahovať inštrukcie určené agentovi, nie používateľovi. Agent by mal ignorovať text stránky, ktorý žiada o zmenu cieľa, odhalenie údajov, deaktiváciu ochranných opatrení alebo navštívenie nesúvisiacich stránok.
5. **Používajte deterministické kontroly pri rizikových krokoch.** Overujte aktuálne URL, názov stránky, vybratý prvok, cenu, príjemcu a súhrn akcie pomocou kódu pred tým, než požiadate používateľa o schválenie finálneho kroku.
6. **Nastavte rozpočty a podmienky zastavenia.** Obmedzte počet akcií, opakovaní, kariet a minút, ktoré môže agent použiť. Zastavte, ak je stav stránky nejednoznačný, namiesto pokračovania v klikaní.
7. **Zaznamenávajte užitočné dôkazy, nie všetko.** Uchovávajte súhrny akcií, časové značky, URL, opisy vybraných prvkov a odkazy na screenshoty, aby sa chyby dali skontrolovať bez ukladania zbytočného citlivého obsahu stránky.

V ukážke Airbnb je bezpečným predvolením vyhľadávanie ponúk a extrakcia cien. Prihlasovanie, kontaktovanie hostiteľa alebo dokončenie rezervácie by mala byť samostatná akcia schválená používateľom.

### Reálne použitia

- Rezervácia ciest a monitorovanie cien
- Porovnávanie cien a kontrola dostupnosti v e-commerce
- Štruktúrovaná extrakcia z dynamických webových stránok
- Testovanie a overovanie UI s videním
- Monitorovanie webových stránok a upozorňovanie
- Inteligentné vypĺňanie formulárov v rámci viacstupňových procesov

## Príklad z reálneho sveta: Microsoft Project Opal

Agent, ktorého vytvoríte v tejto lekcii, je malou lokálnou verziou **agenta na používanie počítača (CUA)** — programu, ktorý ovláda prehliadač rovnakým spôsobom ako človek. Microsoft prináša tento rovnaký koncept do podnikov s **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, schopnosťou v Microsoft 365 Copilot.

S Project Opal popíšete úlohu a agent pracuje vo vašom mene pomocou **používania počítača na zabezpečenom Windows 365 Cloud PC**, pracujúcom naprieč aplikáciami, stránkami a údajmi vašej organizácie v prehliadači. Pracuje **asynchrónne na pozadí** a môžete kedykoľvek riadiť jeho prácu alebo prevziať kontrolu. Príklady úloh zahŕňajú:

- Spravovanie požiadaviek na členstvo v bezpečnostných skupinách
- Zhromažďovanie a overovanie audítorských dôkazov pre overovanie súladu
- Riešenie IT incidentov (aktualizácia stavu lístku, priraďovanie zodpovedných, zatváranie duplikátov)
- Skladanie údajov z Excelu do finálnej finančnej prezentácie

Opal je užitočným referenčným príkladom toho, ako vyzerá **produkčný, dôveryhodný** agent na používanie počítača — a zároveň posilňuje koncepty z predchádzajúcich lekcií:

| Koncept v tomto kurze | Ako Project Opal uplatňuje tento koncept |
|------------------------|-----------------------------|
| **Človek v slučke** (Lekcia 06) | Opal pozastaví činnosť pre prihlasovacie údaje, citlivé dáta alebo nejasné inštrukcie, a nikdy nezadá heslá ani neodosiela formuláre bez výslovného potvrdenia. Môžete *Prevziať kontrolu* a *Vrátiť kontrolu* počas úlohy. |
| **Dôveryhodní a bezpeční agenti** (Lekcie 06 & 18) | Beží v izolovanom Windows 365 Cloud PC, predvolene je iba prehliadačový (prístup k iným počítačovým zdrojom je blokovaný, vynucované cez Intune), používa *vašu* identitu, takže pristupuje len k povoleným zdrojom, a zaznamenáva každú akciu pre audit. |
| **Plánovanie a metakognícia** (Lekcie 07 & 09) | Opal najprv generuje plán úlohy, potom sleduje svoje vlastné uvažovanie v každom kroku a pozastaví sa, ak zistí podozrivú činnosť. |
| **Opakovane použiteľné schopnosti/nástroje** (Lekcia 04) | **Zručnosti** vám umožňujú písať inštrukcie pre opakovateľné úlohy (importované zo súboru `.md` alebo vytvorené pomocou Opal) a používať ich naprieč rozhovormi. |

> **Dostupnosť:** Project Opal je momentálne dostupný používateľom v [rannom prístupe programu Frontier](https://adoption.microsoft.com/copilot/frontier-program/) s predplatným Microsoft 365 Copilot, a správca musí dokončiť nastavenie. Keďže ide o experimentálnu funkciu Frontier, schopnosti sa môžu v priebehu času meniť.

## Ďalšie zdroje

- [Začíname s Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Šablóna integrácie Browser-Use s Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parametre aktérova a extrakcia obsahu v Browser-Use](https://docs.browser-use.com/customize/actor/all-parameters)
- [Nastavenie kurzu](../00-course-setup/README.md)

## Predchádzajúca lekcia

[Preskúmanie Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Nasledujúca lekcia

[Nasadenie škálovateľných agentov](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->