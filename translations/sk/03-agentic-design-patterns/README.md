[![Ako navrhnúť dobrých AI agentov](../../../translated_images/sk/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_
# Zásady navrhovania AI agentov

## Úvod

Existuje mnoho spôsobov, ako premýšľať o budovaní agentných AI systémov. Pretože nejasnosť je vlastnosťou, nie chybou v návrhu generatívnej AI, pre inžinierov je niekedy ťažké zistiť, kde vlastne začať. Vytvorili sme súbor užívateľsky orientovaných UX zásad navrhovania, ktoré umožňujú vývojárom budovať zákaznícky orientované agentné systémy na riešenie ich obchodných potrieb. Tieto zásady navrhovania nie sú predpisovou architektúrou, ale skôr východiskovým bodom pre tímy, ktoré definujú a budujú agentné skúsenosti.

Všeobecne by agenti mali:

- Rozširovať a škálovať ľudské schopnosti (brainstorming, riešenie problémov, automatizácia atď.)
- Vyplniť medzery v poznatkoch (dostať ma do obrazu v oblastiach poznatkov, preklady atď.)
- Uľahčovať a podporovať spoluprácu spôsobmi, aké ako jednotlivci preferujeme pri práci s ostatnými
- Robiť nás lepšími verziami samých seba (napr. životný kouč/manažér úloh, pomáhanie učiť sa emočnú reguláciu a zručnosti všímavosti, budovanie odolnosti atď.)

## Čo táto lekcia pokrýva

- Čo sú zásady agentného dizajnu
- Aké sú niektoré pokyny, ktoré treba dodržiavať pri implementácii týchto zásad dizajnu
- Niektoré príklady použitia zásad dizajnu

## Naučné ciele

Po dokončení tejto lekcie budete schopní:

1. Vysvetliť, čo sú zásady agentného dizajnu
2. Vysvetliť pokyny pre používanie zásad agentného dizajnu
3. Pochopiť, ako vytvoriť agenta pomocou zásad agentného dizajnu

## Zásady agentného dizajnu

![Zásady agentného dizajnu](../../../translated_images/sk/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (Prostredie)

Toto je prostredie, v ktorom agent operuje. Tieto zásady informujú, ako navrhujeme agentov pre pôsobenie vo fyzických a digitálnych svetoch.

- **Spájanie, nie zrážanie** – pomáha spájať ľudí s inými ľuďmi, udalosťami a použiteľnými znalosťami na umožnenie spolupráce a spojenia.
- Agent pomáha spájať udalosti, vedomosti a ľudí.
- Agent prináša ľudí bližšie k sebe. Nie je navrhnutý na nahradenie alebo znehodnotenie ľudí.
- **Ľahko dostupný, no občas neviditeľný** – agent väčšinou funguje na pozadí a upozorní nás len keď je to relevantné a vhodné.
  - Agent je pre autorizovaných používateľov ľahko vyhľadateľný a dostupný na akomkoľvek zariadení alebo platforme.
  - Agent podporuje multimodálne vstupy a výstupy (zvuk, hlas, text atď.).
  - Agent môže plynulo prechádzať medzi popredím a pozadím; medzi proaktívnym a reaktívnym, podľa toho, ako vníma potreby používateľa.
  - Agent môže fungovať v neviditeľnej forme, no jeho procesy na pozadí a spolupráca s inými agentmi sú používateľovi transparentné a ovládateľné.

### Agent (Čas)

Toto je spôsob, akým agent pôsobí v čase. Tieto zásady informujú o tom, ako navrhujeme agentov interagujúcich cez minulosť, prítomnosť a budúcnosť.

- **Minulosť**: Reflektovanie histórie, ktorá zahŕňa stav aj kontext.
  - Agent poskytuje relevantnejšie výsledky na základe analýzy bohatších historických dát, nielen udalostí, ľudí alebo stavov.
  - Agent vytvára spojenia z minulých udalostí a aktívne odráža spomienky, aby sa zapojil do aktuálnych situácií.
- **Teraz**: Podnecovať skôr ako len informovať.
  - Agent zosobňuje komplexný prístup k interakcii s ľuďmi. Keď sa udalosť stane, Agent prekračuje statické oznámenie alebo inú statickú formalitu. Agent môže zjednodušiť postupy alebo dynamicky generovať signály na nasmerovanie používateľovej pozornosti v správnom momente.
  - Agent poskytuje informácie na základe kontextuálneho prostredia, sociálnych a kultúrnych zmien a prispôsobené používateľskému zámeru.
  - Interakcia s agentom môže byť postupná, rozvíjajúca sa a rastúca v zložitosti, aby posilnila používateľov dlhodobo.
- **Budúcnosť**: Prispôsobovanie a vývoj.
  - Agent sa prispôsobuje rôznym zariadeniam, platformám a modalitám.
  - Agent sa prispôsobuje správaniu používateľa, potrebám prístupnosti a je slobodne prispôsobiteľný.
  - Agent je formovaný a vyvíja sa prostredníctvom neustálej interakcie s používateľom.

### Agent (Jadro)

Toto sú kľúčové prvky v jadre návrhu agenta.

- **Prijímanie neistoty, ale budovanie dôvery**.
  - Očakáva sa určitá miera neistoty u Agenta. Neistota je kľúčovým prvkom návrhu agenta.
  - Dôvera a transparentnosť sú základnými vrstvami návrhu Agenta.
  - Ľudia majú kontrolu nad zapnutím/vypnutím Agenta a stav Agenta je vždy jasne viditeľný.

## Pokyny na implementáciu týchto zásad

Keď používate vyššie uvedené zásady navrhovania, dodržujte nasledujúce pokyny:

1. **Transparentnosť**: Informujte používateľa, že sa používa AI, ako funguje (vrátane minulých akcií) a ako poskytovať spätnú väzbu a meniť systém.
2. **Kontrola**: Umožnite používateľovi prispôsobiť systém, špecifikovať preferencie, personalizovať a mať kontrolu nad systémom a jeho atribútmi (vrátane možnosti zabudnúť).
3. **Konzistentnosť**: Usilujte o konzistentné, multimodálne zážitky naprieč zariadeniami a koncovými bodmi. Používajte známe UI/UX prvky, kde je to možné (napr. ikona mikrofónu pre hlasovú interakciu) a znižujte kognitívnu záťaž používateľa čo najviac (napr. snažte sa o stručné odpovede, vizuálne pomôcky a obsah „Dozvedieť sa viac“).

## Ako navrhnúť cestovného agenta pomocou týchto zásad a pokynov

Predstavte si, že navrhujete cestovného agenta, takto by ste mohli premýšľať o použítí zásad a pokynov:

1. **Transparentnosť** – Dajte používateľovi vedieť, že cestovný agent je AI agent. Poskytnite základné inštrukcie, ako začať (napr. správa „Ahoj“, ukážkové výzvy). Jasne to zdokumentujte na produktovej stránke. Ukážte zoznam výziev, ktoré používateľ zadal v minulosti. Jasne vysvetlite, ako poskytnúť spätnú väzbu (palce hore/dolu, tlačidlo Poslať spätnú väzbu atď.). Jasne uveďte, či má agent obmedzenia používania alebo tém.
2. **Kontrola** – Uistite sa, že je jasné, ako môže používateľ agenta po jeho vytvorení upravovať, napríklad pomocou systémovej výzvy. Umožnite používateľovi zvoliť si, ako verbózny agent je, jeho štýl písania a akékoľvek obmedzenia, o čom by agent nemal hovoriť. Umožnite používateľovi prezerať a mazať súvisiace súbory, dáta, výzvy a minulé konverzácie.
3. **Konzistentnosť** – Uistite sa, že ikony pre zdieľanie výzvy, pridanie súboru alebo fotografie a označenie niekoho alebo niečo sú štandardné a rozpoznateľné. Použite ikonu spinky na označenie nahrania/zdieľania súboru s agentom a ikonu obrázka na označenie nahrávania grafiky.

## Vzorky kódov

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Máte viac otázok o vzorcoch AI agentného dizajnu?

Pridajte sa na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby ste sa stretli s ostatnými študentmi, zúčastnili sa konzultačných hodín a získali odpovede na svoje otázky o AI agentoch.

## Dodatočné zdroje

- <a href="https://openai.com" target="_blank">Praktiky správy agentných AI systémov | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Projekt HAX Toolkit - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Zodpovedná AI Toolbox</a>

## Predchádzajúca lekcia

[Preskúmanie agentných rámcov](../02-explore-agentic-frameworks/README.md)

## Nasledujúca lekcia

[Vzor návrhu používateľských nástrojov](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->