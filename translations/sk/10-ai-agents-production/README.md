# AI agenti v produkcii: Monitorovanie a hodnotenie

[![AI Agents in Production](../../../translated_images/sk/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Keď sa AI agenti posúvajú od experimentálnych prototypov k reálnym aplikáciám, stáva sa dôležitou schopnosť porozumieť ich správaniu, monitorovať ich výkon a systematicky vyhodnocovať ich výstupy.

## Ciele učenia

Po absolvovaní tejto lekcie budete vedieť/rozumieť:
- Základné koncepty monitorovania a hodnotenia agentov
- Techniky na zlepšenie výkonu, nákladov a efektívnosti agentov
- Čo a ako systematicky hodnotiť svojich AI agentov
- Ako kontrolovať náklady pri nasadzovaní AI agentov do produkcie
- Ako inštruovať agentov vytvorených pomocou Microsoft Agent Framework

Cieľom je vybaviť vás vedomosťami na transformáciu vašich „čiernych skríň“ agentov na transparentné, spravovateľné a spoľahlivé systémy.

_**Poznámka:** Dôležité je nasadzovať AI agentov, ktorí sú bezpeční a dôveryhodní. Pozrite si tiež lekciu [Budovanie dôveryhodných AI agentov](./06-building-trustworthy-agents/README.md)._

## Trasy a úseky

Nástroje pre monitorovanie, ako sú [Langfuse](https://langfuse.com/) alebo [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), zvyčajne predstavujú behy agentov ako trasy a úseky.

- **Trasa** predstavuje kompletnú úlohu agenta od začiatku do konca (napríklad spracovanie používateľského dotazu).
- **Úseky** sú jednotlivé kroky v rámci trasy (napríklad volanie jazykového modelu alebo získavanie dát).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez monitorovania môže AI agent pôsobiť ako „čierna skrinka“ – jeho vnútorný stav a logika sú neprehľadné, čo sťažuje diagnostiku problémov alebo optimalizáciu výkonu. S monitorovaním sa agenti stávajú „sklenenými skrinkami“, ktoré ponúkajú transparentnosť nevyhnutnú na budovanie dôvery a zabezpečenie správneho fungovania.

## Prečo je monitorovanie dôležité v produkčných prostrediach

Presun AI agentov do produkčného prostredia prináša nové výzvy a požiadavky. Monitorovanie už nie je „len dobrým doplnkom“, ale kľúčovou schopnosťou:

*   **Ladenie a analýza príčiny chýb**: Keď agent zlyhá alebo vygeneruje neočakávaný výstup, nástroje monitorovania poskytnú trasy potrebné na určenie zdroja chyby. To je obzvlášť dôležité pri zložitých agentoch, ktorí môžu využívať viacnásobné volania LLM, interakcie s nástrojmi a podmienenú logiku.
*   **Správa latencie a nákladov**: AI agenti často využívajú LLM a iné externé API, ktoré sa účtujú podľa tokenu alebo volania. Monitorovanie umožňuje presné sledovanie týchto volaní, pomáha identifikovať operácie, ktoré sú príliš pomalé alebo drahé. Tím tak môže optimalizovať príklady, vybrať efektívnejšie modely alebo prerobiť workflowy na riadenie nákladov a zabezpečenie dobrej používateľskej skúsenosti.
*   **Dôvera, bezpečnosť a súlad**: V mnohých aplikáciách je dôležité zabezpečiť, aby agenti konali bezpečne a eticky. Monitorovanie poskytuje auditný záznam akcií a rozhodnutí agenta. To je možné využiť na detekciu a zmiernenie problémov ako injekcia promptov, generovanie škodlivého obsahu alebo nesprávna manipulácia s osobne identifikovateľnými informáciami (PII). Napríklad môžete priamo prehliadať trasy a rozumieť, prečo agent poskytol určitú odpoveď alebo použil konkrétny nástroj.
*   **Smyčky neustáleho zlepšovania**: Dáta z monitorovania sú základom iteratívneho vývojového procesu. Sledovaním výkonu agentov v reálnom svete môžu tímy identifikovať oblasti pre zlepšenie, získavať dáta na doladenie modelov a overovať vplyv zmien. Vzniká spätná väzba, kde produkčné poznatky z online hodnotenia vplývajú na offline experimentovanie a dolaďovanie, čo vedie k postupne lepšiemu výkonu agentov.

## Kľúčové metriky na sledovanie

Na sledovanie a pochopenie správania agenta by sa malo monitorovať viacero metrík a signálov. Konkrétne metriky sa môžu líšiť podľa účelu agenta, no niektoré sú univerzálne dôležité.

Tu sú niektoré z najbežnejších metrík, ktoré nástroje monitorovania sledujú:

**Latencia:** Ako rýchlo agent reaguje? Dlhé čakanie negatívne ovplyvňuje používateľskú skúsenosť. Mali by ste merať latenciu pre úlohy aj jednotlivé kroky pomocou trasovania behov agenta. Napríklad agent, ktorý potrebuje na všetky volania modelu 20 sekúnd, môže byť zrýchlený použitím rýchlejšieho modelu alebo súbehým spustením volaní.

**Náklady:** Koľko stojí jeden beh agenta? AI agenti závisia od volaní LLM účtovaných podľa tokenu alebo externých API. Časté používanie nástrojov alebo viacnásobné promptovanie môže náklady rýchlo zvýšiť. Ak agent volá LLM päťkrát pre marginálne zlepšenie kvality, musíte posúdiť, či sú náklady odôvodnené, alebo či môžete znížiť počet volaní či použiť lacnejší model. Sledovanie v reálnom čase tiež pomáha odhaliť neočakávané výkyvy (napríklad chyby spôsobujúce nadmerné cykly API).

**Chyby požiadaviek:** Koľko požiadaviek agent zlyhal? Môže ísť o chyby API alebo neúspešné volania nástrojov. Aby bol agent v produkcii odolnejší, môžete nastaviť záložné mechanizmy alebo opakovanie. Napríklad ak je LLM poskytovateľ A nedostupný, prepnite na poskytovateľa B ako zálohu.

**Používateľská spätná väzba:** Priama spätná väzba od používateľov poskytuje cenné poznatky. Môže ísť o explicitné hodnotenia (👍páči sa mi/👎nepáči sa, ⭐1-5 hviezdičiek) alebo textové komentáre. Konzistentná negatívna spätná väzba vás upozorní, že agent nefunguje podľa očakávania.

**Implicitná používateľská spätná väzba:** Správanie používateľov poskytuje nepriamu spätnú väzbu aj bez explicitných hodnotení. Môže to byť napríklad okamžité preformulovanie otázky, opakované dotazy alebo kliknutie na tlačidlo opakovania. Ak si všimnete, že používatelia opakovane kladú rovnaké otázky, je to znak toho, že agent nefunguje podľa očakávania.

**Presnosť:** Ako často agent produkuje správne alebo žiaduce výstupy? Definícia presnosti sa líši (napríklad správnosť riešenia problémov, presnosť získavania informácií, spokojnosť používateľa). Prvým krokom je definovať, ako vyzerá úspech pre vášho agenta. Presnosť môžete sledovať cez automatické kontroly, hodnotiace skóre alebo označenia dokončených úloh. Napríklad označenie trás ako „úspešné“ alebo „neúspešné“.

**Automatizované hodnotiace metriky:** Môžete nastaviť aj automatizované hodnotenia. Napríklad môžete použiť LLM na vyhodnotenie výstupu agenta, či je užitočný, presný alebo nie. Existuje tiež niekoľko open source knižníc, ktoré pomáhajú hodnotiť rôzne aspekty agenta, napríklad [RAGAS](https://docs.ragas.io/) pre RAG agentov alebo [LLM Guard](https://llm-guard.com/) na detekciu škodlivého jazyka či injekcie promptov.

V praxi najlepšie pokrytie zdravotného stavu AI agenta poskytuje kombinácia týchto metrík. V tomto kapitole v [príkladnom notebooku](./code_samples/10-expense_claim-demo.ipynb) vám ukážeme, ako tieto metriky vyzerajú na reálnych príkladoch, no najskôr sa naučíme, ako vyzerá typický pracovný tok hodnotenia.

## Inštrumentujte svojho agenta

Na zber dát trasovania bude potrebné inštrumentovať kód. Cieľom je inštrumentovať kód agenta tak, aby emitoval trasy a metriky, ktoré môže zachytiť, spracovať a vizualizovať monitorovací nástroj.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) sa stal priemyselným štandardom pre monitorovanie LLM. Poskytuje sadu API, SDK a nástrojov na generovanie, zber a export telemetrických dát.

Existuje množstvo inštrumentačných knižníc, ktoré obalia existujúce frameworky agentov a uľahčujú export OpenTelemetry úsekov do monitorovacieho nástroja. Microsoft Agent Framework je s OpenTelemetry natívne integrovaný. Nižšie je príklad inštrumentovania MAF agenta:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Vykonávanie agenta je automaticky sledované
    pass
```

V tejto kapitole príkladný [notebook](./code_samples/10-expense_claim-demo.ipynb) demonštruje, ako inštrumentovať váš MAF agent.

**Ručné vytváranie úsekov:** Aj keď inštrumentačné knižnice poskytujú dobrý základ, často sú prípady, keď je potrebná podrobnejšia alebo vlastná informácia. Môžete ručne vytvárať úseky na pridanie vlastnej aplikačnej logiky. Dôležité je, že môžete automaticky alebo ručne vytvorené úseky obohatiť o vlastné atribúty (tiež známe ako tagy alebo metadáta). Tieto atribúty môžu obsahovať biznisovo špecifické dáta, medziľahlé výpočty alebo akýkoľvek kontext, ktorý môže byť užitočný pre ladenie alebo analýzu, napríklad `user_id`, `session_id` alebo `model_version`.

Príklad ručného vytvárania trás a úsekov s [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Hodnotenie agenta

Monitorovanie nám poskytuje metriky, ale hodnotenie je proces analýzy týchto dát (a vykonávania testov), aby sme určili, ako dobre AI agent funguje a ako ho možné zlepšiť. Inými slovami, keď už máte trasy a metriky, ako ich používať na posúdenie agenta a prijímanie rozhodnutí?

Pravidelné hodnotenie je dôležité, pretože AI agenti sú často nedeterministickí a môžu sa vyvíjať (prostredníctvom aktualizácií alebo posunu správania modelu) – bez hodnotenia by ste nevedeli, či váš „inteligentný agent“ skutočne plní svoju úlohu dobre alebo či došlo k regresii.

Existujú dve kategórie hodnotení AI agentov: **online hodnotenie** a **offline hodnotenie**. Obe sú cenné a navzájom sa dopĺňajú. Zvyčajne začíname s offline hodnotením, pretože je to minimálny nevyhnutný krok pred nasadením akéhokoľvek agenta.

### Offline hodnotenie

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Toto zahŕňa hodnotenie agenta v kontrolovanom prostredí, zvyčajne pomocou testovacích datasetov, nie pomocou živých používateľských dotazov. Používate vybrané dataset, kde poznáte očakávaný výstup alebo správne správanie, a potom na nich spustíte svojho agenta.

Napríklad ak ste vytvorili agenta na riešenie slovných matematických úloh, môžete mať [testovací dataset](https://huggingface.co/datasets/gsm8k) so 100 úlohami a známymi odpoveďami. Offline hodnotenie sa často vykonáva počas vývoja (a môže byť súčasťou CI/CD pipeline) na kontrolu zlepšení alebo ochranu proti regresii. Výhodou je, že je **opakované a môžete získať jasné metriky presnosti, keďže máte referenciu správnosti**. Môžete tiež simulovať používateľské dotazy a merať odpovede agenta oproti ideálnym odpovediam alebo použiť automatizované metriky, ako bolo opísané vyššie.

Kľúčovou výzvou offline hodnotenia je zabezpečiť, aby bol váš testovací dataset komplexný a stále relevantný – agent môže byť úspešný na pevnom teste, ale v produkcii sa stretnúť s veľmi odlišnými dotazmi. Preto by ste mali udržiavať testovacie sady aktuálne s novými okrajovými prípadmi a príkladmi, ktoré odrážajú reálne situácie. Je užitočné mať mix malých „smoke testov“ a väčších evaluačných datasetov: malé sady pre rýchle kontroly a väčšie pre širšie metrické hodnotenie.

### Online hodnotenie

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Týka sa hodnotenia agenta v reálnom prostredí naživo, teda pri skutočnom používaní v produkcii. Online hodnotenie zahŕňa sledovanie výkonu agenta na skutočných používateľských interakciách a priebežnú analýzu výsledkov.

Napríklad môžete sledovať mieru úspešnosti, skóre spokojnosti používateľov alebo iné metriky na živej prevádzke. Výhodou online hodnotenia je, že **zachytáva veci, ktoré by ste v laboratórnom prostredí nepredpokladali** – môžete pozorovať posun modelu v čase (ak sa efektívnosť agenta zhoršuje so zmenou vstupných vzorov) a zachytiť neočakávané dotazy či situácie, ktoré neboli v testovacích dátach. Poskytuje skutočný obraz o správaní agenta v reálnom svete.

Online hodnotenie často zahŕňa zbieranie implicitnej a explicitnej spätnej väzby používateľov, ako bolo spomenuté, a prípadne spustenie shadow testov alebo A/B testov (kde nová verzia agenta beží paralelne na porovnanie s tou starou). Výzvou môže byť získať spoľahlivé označenia či skóre pre živé interakcie – môžete sa spoliehať na spätnú väzbu používateľov alebo následné metriky (napríklad či používateľ klikol na výsledok).

### Kombinovanie oboch

Online a offline hodnotenia nie sú navzájom vylučujúce, naopak sa veľmi dopĺňajú. Poznatky z online monitorovania (napríklad nové typy používateľských dotazov, pri ktorých agent obstáva zle) môžu slúžiť na doplnenie a zlepšenie offline testovacích datasetov. Naopak agenti, ktorí dobre obstáli v offline testoch, môžu byť s väčšou istotou nasadení a monitorovaní online.

Mnohé tímy skutočne prijímajú cyklus:

_offline hodnotenie -> nasadenie -> online monitoring -> zbieranie nových prípadov zlyhaní -> pridanie do offline datasetu -> vylepšenie agenta -> opakovanie_.

## Bežné problémy

Pri nasadzovaní AI agentov do produkcie môžete naraziť na rôzne výzvy. Tu sú niektoré časté problémy a ich možné riešenia:

| **Problém**    | **Možné riešenie**   |
| ------------- | ------------------ |
| AI agent nespolupracuje konzistentne | - Vylepšite prompt daný AI agentovi; buďte jasní v cieľoch.<br>- Identifikujte, kde pomôže rozdelenie úloh na podúlohy riešené viacerými agentmi. |
| AI agent sa dostáva do nekonečných slučiek  | - Zabezpečte jasné pravidlá ukončenia, aby agent vedel, kedy proces zastaviť.<br>- Pre zložité úlohy vyžadujúce plánovanie použite väčší model špecializovaný na takéto úlohy. |
| Volania nástrojov AI agenta nefungujú dobre   | - Otestujte a overte výstupy nástrojov mimo systému agenta.<br>- Upracte definované parametre, prompty a pomenovanie nástrojov.  |
| Multi-agentný systém nefunguje konzistentne | - Vylepšite prompty každého agenta, aby boli špecifické a odlíšiteľné.<br>- Postavte hierarchický systém s „routing“ alebo kontrolným agentom na určenie správneho agenta. |

Mnohé z týchto problémov možno efektívnejšie identifikovať s fungujúcim monitorovaním. Trasy a metriky, o ktorých sme hovorili, presne ukazujú, kde v pracovnom toku agenta sa problémy vyskytujú, čo uľahčuje ladenie a optimalizáciu.

## Riadenie nákladov
Tu sú niektoré stratégie na riadenie nákladov pri nasadzovaní AI agentov do produkcie:

**Používanie menších modelov:** Malé jazykové modely (SLM) môžu dobre fungovať pri určitých agentických prípadových využití a výrazne znížia náklady. Ako už bolo spomenuté, najlepším spôsobom, ako pochopiť, ako dobre sa SLM osvedčí vo vašom prípade použitia, je vybudovať systém hodnotenia na určenie a porovnanie výkonu voči väčším modelom. Zvážte použitie SLM pre jednoduchšie úlohy, ako je klasifikácia zámeru alebo extrakcia parametrov, pričom väčšie modely si nechajte na komplexné uvažovanie.

**Používanie router modelu:** Podobnou stratégiou je použitie rôznych modelov a veľkostí. Môžete použiť LLM/SLM alebo bezserverovú funkciu na nasmerovanie požiadaviek podľa zložitosti na najvhodnejšie modely. Toto tiež pomôže znížiť náklady a zároveň zabezpečiť výkon pri správnych úlohách. Napríklad nasmerujte jednoduché dotazy na menšie, rýchlejšie modely a drahé veľké modely používajte len na zložité úlohy uvažovania.

**Ukladanie odpovedí do vyrovnávacej pamäte:** Identifikácia bežných požiadaviek a úloh a poskytovanie odpovedí predtým, než prejdú cez váš agentický systém, je dobrý spôsob, ako znížiť počet podobných požiadaviek. Môžete dokonca implementovať tok na určenie, ako veľmi je požiadavka podobná vašim uloženým požiadavkám pomocou jednoduchších AI modelov. Táto stratégia môže výrazne znížiť náklady pri často kladených otázkach alebo bežných pracovných postupoch.

## Pozrime sa, ako to funguje v praxi

V [príkladovom notebooku tejto sekcie](./code_samples/10-expense_claim-demo.ipynb) uvidíme príklady, ako môžeme použiť nástroje sledovateľnosti na monitorovanie a hodnotenie nášho agenta.

### Máte viac otázok o AI agentoch v produkcii?

Pridajte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), stretnite sa s inými študentmi, zúčastnite sa konzultačných hodín a získajte odpovede na vaše otázky o AI agentech.

## Predchádzajúca lekcia

[Metakognitívny dizajnový vzor](../09-metacognition/README.md)

## Nasledujúca lekcia

[Agentické protokoly](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->