[![Ako navrhnúť dobrých AI agentov](../../../translated_images/sk/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_
# Zásady agentického dizajnu AI

## Úvod

Existuje mnoho spôsobov, ako premýšľať o budovaní agentických AI systémov. Vzhľadom na to, že neurčitosť je v generatívnom AI dizajne vlastnosťou, nie chybou, niekedy je pre inžinierov ťažké zistiť, kde začať. Vytvorili sme súbor používateľsky orientovaných zásad UX dizajnu, ktoré umožnia vývojárom vytvárať zákaznícky orientované agentické systémy na riešenie ich obchodných potrieb. Tieto dizajnové zásady nie sú predpisovou architektúrou, ale skôr východiskovým bodom pre tímy, ktoré definujú a budujú agentické skúsenosti.

Všeobecne by agenti mali:

- Rozširovať a škálovať ľudské schopnosti (brainstorming, riešenie problémov, automatizácia atď.)
- Vyplniť medzery vo vedomostiach (pripraviť ma na znalostné oblasti, preklad atď.)
- Uľahčovať a podporovať spoluprácu spôsobmi, aké my ako jednotlivci preferujeme pri práci s ostatnými
- Robiť nás lepšou verziou samých seba (napr. životný kouč / manažér úloh, pomoc pri učení sa emocionálnej regulácie a mindfulness zručností, budovanie odolnosti atď.)

## Táto lekcia pokryje

- Čo sú agentické dizajnové zásady
- Aké sú usmernenia pri implementácii týchto dizajnových zásad
- Príklady použitia dizajnových zásad

## Ciele učenia

Po dokončení tejto lekcie budete schopní:

1. Vysvetliť, čo sú agentické dizajnové zásady
2. Vysvetliť usmernenia na používanie agentických dizajnových zásad
3. Pochopiť, ako postaviť agenta pomocou agentických dizajnových zásad

## Agentické dizajnové zásady

![Agentické dizajnové zásady](../../../translated_images/sk/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (Priestor)

Toto je prostredie, v ktorom agent pôsobí. Tieto zásady ovplyvňujú, ako navrhujeme agentov pre interakciu v fyzických a digitálnych svetoch.

- **Spájanie, nie zhlukovanie** – pomáha spájať ľudí s inými ľuďmi, udalosťami a akcieschopnými znalosťami, aby umožnil spoluprácu a spojenie.
- Agentom pomáhajú spájať udalosti, vedomosti a ľudí.
- Agent približuje ľudí k sebe. Nie je navrhnutý na náhradu alebo podceňovanie ľudí.
- **Ľahko dostupný, ale občas neviditeľný** – agent vo veľkej miere funguje na pozadí a upozorňuje nás len vtedy, keď je to relevantné a vhodné.
  - Agent je ľahko objaviteľný a dostupný pre oprávnených používateľov na akomkoľvek zariadení alebo platforme.
  - Agent podporuje multimodálne vstupy a výstupy (zvuk, hlas, text atď.).
  - Agent sa plynule presúva medzi popredím a pozadím; medzi proaktívnym a reaktívnym, podľa svojho vnímania potrieb používateľa.
  - Agent môže fungovať v neviditeľnej forme, no jeho proces na pozadí a spolupráca s inými agentmi sú transparentné a používateľom ovládateľné.

### Agent (Čas)

Takto agent funguje v čase. Tieto zásady ovplyvňujú, ako navrhujeme agentov, ktorí interagujú naprieč minulosťou, prítomnosťou a budúcnosťou.

- **Minulosť**: reflexia histórie vrátane stavu a kontextu.
  - Agent poskytuje relevantnejšie výsledky založené na analýze bohatších historických údajov než len udalosti, ľudí alebo stavov.
  - Agent vytvára spojenia z minulých udalostí a aktívne reflektuje pamäť na zapojenie sa do súčasných situácií.
- **Teraz**: Podnety viac ako upozornenia.
  - Agent stelesňuje komplexný prístup k interakcii s ľuďmi. Keď sa stane udalosť, agent presahuje statické oznámenie alebo inú formálnosť. Agent môže zjednodušiť procesy alebo dynamicky generovať podnety na správne nasmerovanie pozornosti používateľa.
  - Agent poskytuje informácie podľa kontextu prostredia, sociálnych a kultúrnych zmien prispôsobené zámeru používateľa.
  - Interakcia agenta môže byť postupná, vyvíjajúca sa a rastúca v komplexnosti, aby dlhodobo posilnila používateľov.
- **Budúcnosť**: adaptácia a vývoj.
  - Agent sa prispôsobuje rôznym zariadeniam, platformám a modalitám.
  - Agent sa prispôsobuje správaniu používateľa, potrebám prístupnosti a je voľne prispôsobiteľný.
  - Agent je formovaný a vyvíja sa prostredníctvom kontinuálnej interakcie s používateľom.

### Agent (Jadro)

Toto sú kľúčové prvky v jadre dizajnu agenta.

- **Prijmite neistotu, ale vytvorte dôveru**.
  - Očakáva sa určitá úroveň neistoty agenta. Neistota je kľúčovým prvkom dizajnu agenta.
  - Dôvera a transparentnosť sú základnými vrstvami dizajnu agenta.
  - Ľudia majú kontrolu nad zapnutím/vypnutím agenta a stav agenta je vždy jasne viditeľný.

## Usmernenia na implementáciu týchto zásad

Pri používaní predchádzajúcich dizajnových zásad používajte nasledujúce usmernenia:

1. **Transparentnosť**: Informujte používateľa, že AI je zapojená, ako funguje (vrátane minulých akcií) a ako poskytnúť spätnú väzbu a upraviť systém.
2. **Kontrola**: Umožnite používateľovi prispôsobiť si systém, špecifikovať preferencie a personalizovať ho a mať kontrolu nad systémom a jeho vlastnosťami (vrátane možnosti zabudnúť).
3. **Konzistencia**: Smerujte k konzistentným multimodálnym zážitkom na zariadeniach a koncových bodoch. Používajte známe UI/UX prvky, kde je to možné (napr. ikona mikrofónu pre hlasovú interakciu) a čo najviac znižujte kognitívne zaťaženie zákazníka (napr. stručné odpovede, vizuálne pomôcky a obsah „Dozvedieť sa viac“).

## Ako navrhnúť cestovného agenta podľa týchto zásad a usmernení

Predstavte si, že navrhujete cestovného agenta, tu je návod, ako môžete použiť dizajnové zásady a usmernenia:

1. **Transparentnosť** – Dajte používateľovi vedieť, že cestovný agent je agent s podporou AI. Poskytnite základné inštrukcie, ako začať (napr. uvítaciu správu „Hello“, vzorové podnety). Jasne to zdokumentujte na stránke produktu. Ukážte zoznam podnetov, ktoré používateľ položil v minulosti. Uveďte jasne, ako poskytnúť spätnú väzbu (palce hore alebo dole, tlačidlo „Odoslať spätnú väzbu“ atď.). Jasne uveďte, či agent má obmedzenia používania alebo tém.
2. **Kontrola** – Zabezpečte, aby bolo jasné, ako môže používateľ upraviť agenta po jeho vytvorení, napríklad pomocou systémového podnetu. Umožnite používateľovi vybrať, aký rozsiahly má agent byť, jeho štýl písania a akékoľvek výhrady o témach, o ktorých by agent nemal hovoriť. Umožnite používateľovi zobrazovať a mazať akékoľvek súvisiace súbory alebo údaje, podnety a minulé konverzácie.
3. **Konzistencia** – Zabezpečte, aby ikony na zdieľanie podnetov, pridanie súboru alebo fotky a označenie niekoho alebo niečoho boli štandardné a ľahko rozpoznateľné. Použite ikonu spinky na označenie nahrávania/zdieľania súborov s agentom a ikonu obrázku na nahrávanie grafiky.

## Ukážkové kódy

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Máte ďalšie otázky o agentických dizajnových vzorcoch AI?

Pridajte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), stretávajte sa s inými študentmi, zúčastňujte sa konzultačných hodín a získajte odpovede na vaše otázky o AI agentoch.

## Ďalšie zdroje

- <a href="https://openai.com" target="_blank">Praktiky pre riadenie agentických AI systémov | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Projekt HAX Toolkit - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Responsible AI Toolbox</a>

## Predchádzajúca lekcia

[Preskúmanie agentických rámcov](../02-explore-agentic-frameworks/README.md)

## Nasledujúca lekcia

[Vzory dizajnu používania nástrojov](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->