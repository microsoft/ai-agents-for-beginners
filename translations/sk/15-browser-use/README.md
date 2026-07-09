# Vytváranie agentov na používanie počítača (CUA)

Agenti na používanie počítača môžu komunikovať s webovými stránkami rovnakým spôsobom ako človek: otvorením prehliadača, preskúmaním stránky a vykonaním najlepšej ďalšej akcie na základe toho, čo vidia. V tejto lekcii si vytvoríte agenta pre automatizáciu prehliadača, ktorý vyhľadáva na Airbnb, extrahuje štruktúrované údaje o ponukách a identifikuje najlacnejšie ubytovanie v Štokholme.

Lekcia kombinuje Browser-Use pre navigáciu riadenú AI, Playwright a Chrome DevTools Protocol (CDP) pre ovládanie prehliadača, Azure OpenAI pre rozumovanie podporené vizuálnym vstupom a Pydantic pre štruktúrovanú extrakciu.

## Úvod

Táto lekcia pokryje:

- Pochopenie, kedy sú agenti na používanie počítača vhodnejší ako automatizácia len cez API
- Kombinovanie Browser-Use s Playwright a CDP pre spoľahlivé riadenie životného cyklu prehliadača
- Používanie Azure OpenAI videnia a štruktúrovaného výstupu Pydantic na extrakciu údajov o ponukách z dynamických webových stránok
- Rozhodovanie, kedy použiť workflow agent-prvý, actor-prvý alebo hybridnú automatizáciu prehliadača

## Ciele učenia sa

Po dokončení tejto lekcie budete vedieť:

- Nakonfigurovať Browser-Use s Azure OpenAI a Playwright
- Vytvoriť workflow automatizácie prehliadača, ktorý naviguje na skutočnú webovú stránku a zvláda dynamické UI prvky
- Extrahovať typizované výsledky z viditeľného obsahu stránky a premeniť ich na následnú obchodnú logiku
- Vybrať medzi vzormi agent a actor na základe predvídateľnosti úlohy v prehliadači

## Príklad kódu

Táto lekcia obsahuje jeden notebookový tutoriál:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Spúšťa reláciu Chrome cez CDP, vyhľadáva ponuky Airbnb v Štokholme, extrahuje ceny pomocou Browser-Use vision a vracia najlacnejšiu možnosť ako štruktúrované údaje.

## Predpoklady

- Python 3.12+
- Nakonfigurované Azure OpenAI prostredie
- Lokálne nainštalovaný Chrome alebo Chromium
- Nainštalované závislosti Playwright
- Základná znalosť asynchrónneho Pythonu

## Nastavenie

Nainštalujte balíčky použité v notebooku:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Nastavte premenné prostredia Azure OpenAI používané v notebooku:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Voliteľné: predvolene použije najnovšiu verziu API, ak nie je zadané
AZURE_OPENAI_API_VERSION=...
```

## Prehľad architektúry

Notebook demonštruje hybridný workflow automatizácie prehliadača:

1. Chrome sa spúšťa s povoleným CDP, takže Playwright aj Browser-Use môžu zdieľať rovnakú reláciu prehliadača.
2. Agent Browser-Use zvláda otvorené navigačné úlohy, ako je otvorenie Airbnb, odmietnutie vyskakovacích okien a vyhľadávanie Štokholmu.
3. Aktívna stránka je preskúmaná pomocou štruktúrovanej schémy Pydantic na extrakciu názvov ponúk, cien za noc, hodnotení a URL.
4. Pythonovská logika porovnáva extrahované ponuky a zvýrazňuje najlacnejší výsledok.

Tento prístup zachováva flexibilné, vizuálne rozumovanie, v ktorom je Browser-Use silný, a zároveň vám poskytuje deterministické riadenie prehliadača keď je to potrebné.

## Kľúčové poznatky a osvedčené postupy

### Kedy použiť agenta vs aktéra

| Scenár | Použiť agenta | Použiť aktéra |
|----------|-----------|-----------|
| Dynamické rozloženia | Áno, AI sa môže prispôsobiť zmenám na stránke | Nie, krehké selektory môžu zlyhať |
| Známá štruktúra | Nie, agent je pomalší než priame ovládanie | Áno, rýchle a presné |
| Nájdenie prvkov | Áno, prirodzený jazyk funguje dobre | Nie, vyžadujú sa presné selektory |
| Riadenie časovania | Nie, menej predvídateľné | Áno, plná kontrola nad čakaniami a opakovaniami |
| Zložité workflow | Áno, zvláda neočakávané stavy UI | Nie, vyžaduje explicitné vetvenie |

### Osvedčené postupy Browser-Use

1. Začnite s agentom pre prieskum a dynamickú navigáciu.
2. Prepnite na priame ovládanie stránky, keď interakcia začne byť predvídateľná.
3. Používajte štruktúrované výstupné modely, aby boli extrahované údaje validované a typovo bezpečné.
4. Pridávajte oneskorenia strategicky po akciách, ktoré spúšťajú viditeľné zmeny UI.
5. Počas iterácií snímajte screenshoty, aby boli chyby ľahšie laditeľné.
6. Očakávajte zmeny webových stránok a navrhnite záložné stratégie pre vyskakovacie okná a posuny rozloženia.
7. Kombinujte vzory agent-a aktér, aby ste získali flexibilitu aj presnosť.

### Aplikácie v reálnom svete

- Rezervácie cestovania a sledovanie cien
- Porovnávanie cien v e-commerce a kontrola dostupnosti
- Štruktúrovaná extrakcia z dynamických webových stránok
- Testovanie a overovanie UI s videním
- Monitorovanie webových stránok a upozornenia
- Inteligentné vyplňovanie formulárov cez viacstupňové procesy

## Príklad z praxe: Microsoft Project Opal

Agent, ktorého vytvoríte v tejto lekcii, je malá, lokálna verzia **agenta na používanie počítača (CUA)** — programu, ktorý ovláda prehliadač rovnakým spôsobom ako človek. Microsoft prináša túto rovnakú myšlienku do podnikového prostredia s **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, schopnosťou v Microsoft 365 Copilot.

S Project Opal popíšete úlohu a agent pracuje vo vašom mene pomocou **používania počítača na zabezpečenom Windows 365 Cloud PC**, fungujúc naprieč prehliadačovými aplikáciami, stránkami a dátami vašej organizácie. Funguje **asynchrónne na pozadí** a môžete priamo riadiť jeho prácu alebo prevziať kontrolu kedykoľvek. Príkladné úlohy zahŕňajú:

- Správa žiadostí o členstvo v bezpečnostných skupinách
- Zber a validácia auditných dôkazov pre revízie zhody
- Riešenie IT incidentov (aktualizácia statusu ticketov, priraďovanie zodpovedných, zatváranie duplicit)
- Zostavovanie dát Excel do finančnej uzávierky

Opal je užitočným referenčným bodom, ako vyzerá **produkčný, dôveryhodný** agent na používanie počítača — a zároveň posilňuje koncepty z predchádzajúcich lekcií:

| Koncept v tomto kurze | Ako Project Opal aplikuje tento koncept |
|------------------------|-----------------------------|
| **Človek v slučke** (Lekcia 06) | Opal sa zastaví pre prihlasovacie údaje, citlivé dáta alebo nejednoznačné inštrukcie a nikdy nezadáva heslá ani neodosiela formuláre bez výslovného potvrdenia. Môžete *prevziať kontrolu* a *vrátiť kontrolu* počas úlohy. |
| **Dôveryhodní a bezpeční agenti** (Lekcie 06 & 18) | Beží izolovane na Windows 365 Cloud PC, je štandardne iba prehliadačový (prístup k iným počítačovým zdrojom je zablokovaný cez Intune), používa *vašu* identitu, takže pristupuje len k autorizovaným zdrojom a zaznamenáva všetky akcie pre audit. |
| **Plánovanie a metakognícia** (Lekcie 07 & 09) | Opal najprv generuje plán úlohy, potom dozerá na svoje vlastné rozumovanie pri každom kroku a zastaví sa, ak zistí podozrivú činnosť. |
| **Znovupoužiteľné schopnosti / nástroje** (Lekcia 04) | **Zručnosti** umožňujú písať inštrukcie pre opakovateľné úlohy (importované z `.md` súboru alebo vytvorené priamo v Opal) a používať ich naprieč konverzáciami. |

> **Dostupnosť:** Project Opal je momentálne dostupný používateľom v [programu skorého prístupu Frontier](https://adoption.microsoft.com/copilot/frontier-program/) s predplatným Microsoft 365 Copilot, a váš administrátor musí dokončiť nastavenie. Keďže ide o experimentálnu funkciu Frontier, schopnosti sa môžu v priebehu času meniť.

## Ďalšie zdroje

- [Začíname s Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Šablóna integrácie Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parametre aktéra Browser-Use a extrakcia obsahu](https://docs.browser-use.com/customize/actor/all-parameters)
- [Nastavenie kurzu](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->