# AI Agenti vo Výrobe: Pozorovateľnosť a Hodnotenie

[![AI Agents in Production](../../../translated_images/sk/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Keď AI agenti prechádzajú od experimentálnych prototypov k reálnym aplikáciám, schopnosť porozumieť ich správaniu, sledovať ich výkon a systematicky hodnotiť ich výstupy sa stáva dôležitou.

## Ciele učenia

Po absolvovaní tejto lekcie budete vedieť/pochopíte:
- Základné pojmy pozorovateľnosti a hodnotenia agentov
- Techniky na zlepšenie výkonu, nákladov a efektívnosti agentov
- Čo a ako systematicky hodnotiť svojich AI agentov
- Ako kontrolovať náklady pri nasadení AI agentov do produkcie
- Ako instrumentovať agentov postavených na Microsoft Agent Framework

Cieľom je vybaviť vás znalosťami, ktoré premenia vaše "čierne skrinky" agentov na transparentné, spravovateľné a spoľahlivé systémy.

_**Poznámka:** Je dôležité nasadzovať AI agentov, ktorí sú bezpeční a dôveryhodní. Pozrite si tiež lekciu [Budovanie dôveryhodných AI agentov](../06-building-trustworthy-agents/README.md)._

## Trasy a Spany

Nástroje na pozorovateľnosť ako [Langfuse](https://langfuse.com/) alebo [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) zvyčajne zobrazujú beh agentov ako trasy a spany.

- **Trasa** predstavuje kompletnú úlohu agenta od začiatku do konca (napríklad spracovanie používateľského dotazu).
- **Spany** sú jednotlivé kroky v trase (napríklad volanie jazykového modelu alebo získavanie dát).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez pozorovateľnosti môže AI agent pôsobiť ako "čierna skrinka" - jeho vnútorný stav a dôvody sú neprehľadné, čo sťažuje diagnostiku problémov alebo optimalizáciu výkonu. S pozorovateľnosťou sa agenti stávajú "sklenenými skrinkami", ktoré ponúkajú transparentnosť, čo je kľúčové pre budovanie dôvery a zabezpečenie správnej funkčnosti.

## Prečo je pozorovateľnosť dôležitá v produkčných prostrediach

Prechod AI agentov do produkčných prostredí prináša novú sadu výziev a požiadaviek. Pozorovateľnosť už nie je len "príjemnou", ale kritickou schopnosťou:

*   **Ladenie a analýza príčin**: Keď agent zlyhá alebo vyprodukuje neočakávaný výstup, nástroje pozorovateľnosti poskytujú trasy potrebné na identifikáciu zdroja chyby. To je obzvlášť dôležité v zložitých agentoch, ktoré môžu zahŕňať viaceré volania LLM, interakcie s nástrojmi a podmienenú logiku.
*   **Riadenie latencie a nákladov**: AI agenti často závisia od LLM a iných externých API, ktoré sú účtované za token alebo volanie. Pozorovateľnosť umožňuje presné sledovanie týchto volaní, čo pomáha identifikovať operácie, ktoré sú nadmerne pomalé alebo drahé. To umožňuje tímom optimalizovať prompt-y, vyberať efektívnejšie modely alebo prepracovať pracovné postupy na riadenie prevádzkových nákladov a zabezpečiť dobrú používateľskú skúsenosť.
*   **Dôvera, bezpečnosť a súlad**: V mnohých aplikáciách je dôležité zabezpečiť, aby sa agenti správali bezpečne a eticky. Pozorovateľnosť poskytuje auditnú stopu aktivít a rozhodnutí agenta. Túto stopu je možné použiť na detekciu a zmiernenie problémov ako je prompt injection, generovanie škodlivého obsahu alebo nesprávne spracovanie osobných údajov (PII). Napríklad môžete prehliadať trasy, aby ste pochopili, prečo agent poskytol určitú odpoveď alebo použil konkrétny nástroj.
*   **Slučky neustáleho zlepšovania**: Dáta z pozorovateľnosti sú základom iteratívneho vývojového procesu. Sledovaním výkonu agentov v reálnom svete môžu tímy identifikovať oblasti na zlepšenie, zhromažďovať údaje na doladenie modelov a overovať vplyv zmien. To vytvára spätnú väzbu, kde produkčné poznatky z online hodnotenia informujú offline experimenty a zdokonaľovanie, čo vedie k postupnému zlepšovaniu výkonu agenta.

## Kľúčové metriky na sledovanie

Na sledovanie a pochopenie správania agenta je potrebné monitorovať množstvo metrík a signálov. Hoci konkrétne metriky sa môžu líšiť podľa účelu agenta, niektoré sú univerzálne dôležité.

Tu sú niektoré z najbežnejších metrík, ktoré nástroje pozorovateľnosti monitorujú:

**Latencia:** Ako rýchlo agent odpovedá? Dlhé čakacie doby negatívne ovplyvňujú používateľskú skúsenosť. Mali by ste merať latenciu pre úlohy a jednotlivé kroky sledovaním behov agenta. Napríklad agent, ktorý volá všetky modely 20 sekúnd, by sa mohol zrýchliť použitím rýchlejšieho modelu alebo paralelným vyvolávaním modelov.

**Náklady:** Aké sú náklady na beh agenta? AI agenti závisia na volaniach LLM účtovaných za token alebo na externých API. Časté používanie nástrojov alebo viaceré prompt-y môžu rýchlo zvýšiť náklady. Napríklad ak agent volá LLM päťkrát pre mierne zlepšenie kvality, musíte zvážiť, či sú náklady oprávnené, alebo či môžete znížiť počet volaní alebo použiť lacnejší model. Monitorovanie v reálnom čase môže tiež pomôcť odhaliť neočakávané výkyvy (napríklad chyby spôsobujúce nadmerné opakovanie API).

**Chyby požiadaviek:** Koľko požiadaviek agent zlyhal? Môže ísť o chyby API alebo zlyhané volania nástrojov. Pre zvýšenie odolnosti agenta v produkcii môžete nastaviť náhradné riešenia alebo opakovania. Napríklad ak poskytovateľ LLM A nie je dostupný, prepnite na poskytovateľa LLM B ako zálohu.

**Používateľská spätná väzba:** Implementácia priamych používateľských hodnotení poskytuje cenné poznatky. Môže ísť o explicitné hodnotenia (👍páči sa/👎nepáči, ⭐1-5 hviezdičiek) alebo textové komentáre. Konzistentná negatívna spätná väzba by vás mala varovať ako signál, že agent nefunguje podľa očakávaní.

**Implicitná používateľská spätná väzba:** Správanie používateľov poskytuje nepriamu spätnú väzbu aj bez explicitných hodnotení. Môže zahŕňať okamžité preformulovanie otázky, opakované dotazy alebo kliknutie na tlačidlo opakovania. Napríklad ak vidíte, že používatelia opakovane kladú tú istú otázku, je to znamenie, že agent nefunguje podľa očakávaní.

**Presnosť:** Ako často agent produkuje správne alebo želané výstupy? Definícia presnosti sa líši (napr. správnosť riešenia problémov, presnosť vyhľadávania informácií, spokojnosť používateľa). Prvým krokom je definovať, ako vyzerá úspech pre vášho agenta. Presnosť môžete sledovať pomocou automatizovaných kontrol, hodnotiaceho skóre alebo štítkov dokončenia úloh. Napríklad označením trás ako "úspešné" alebo "neúspešné".

**Automatizované hodnotiace metriky:** Môžete tiež nastaviť automatizované hodnotenia. Napríklad môžete použiť LLM na ohodnotenie výstupu agenta, či je užitočný, presný alebo nie. Existuje tiež niekoľko open source knižníc, ktoré pomáhajú hodnotiť rôzne aspekty agenta. Napríklad [RAGAS](https://docs.ragas.io/) pre RAG agentov alebo [LLM Guard](https://llm-guard.com/) na detekciu škodlivého jazyka alebo prompt injection.

V praxi kombinácia týchto metrík poskytuje najlepšie pokrytie "zdravia" AI agenta. V tomto kapitole v [príkladovom notebooku](./code_samples/10-expense_claim-demo.ipynb) vám ukážeme, ako tieto metriky vyzerajú na reálnych príkladoch, ale najprv sa naučíme, ako vyzerá typický pracovný postup hodnotenia.

## Instrumentujte svojho agenta

Na zhromažďovanie tracingových dát budete potrebovať instrumentovať svoj kód. Cieľom je instrumentovať kód agenta tak, aby vydával trasy a metriky, ktoré môže pozorovateľská platforma zachytiť, spracovať a vizualizovať.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) sa stala priemyselným štandardom pre pozorovateľnosť LLM. Ponúka sadu API, SDK a nástrojov na generovanie, zbieranie a export telemetry dát.

Existuje mnoho instrumentačných knižníc, ktoré obalia existujúce agentné frameworky a uľahčujú export OpenTelemetry spanov do pozorovateľského nástroja. Microsoft Agent Framework sa natívne integruje s OpenTelemetry. Nižšie je príklad instrumentácie MAF agenta:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Vykonávanie agenta je automaticky sledované
    pass
```

[Príkladový notebook](./code_samples/10-expense_claim-demo.ipynb) v tejto kapitole ukáže, ako instrumentovať svoj MAF agenta.

**Manuálne vytváranie spanov:** Aj keď instrumentačné knižnice poskytujú dobrý základ, často sú prípady, kedy je potrebné detailnejšie alebo vlastné informácie. Span môžete manuálne vytvoriť, aby ste pridali zákaznícku aplikačnú logiku. Ešte dôležitejšie je, že automaticky alebo manuálne vytvorené span-y môžu byť obohatené o vlastné atribúty (známe aj ako tagy alebo metadata). Tieto atribúty môžu obsahovať biznisovo špecifické dáta, medzivýpočty alebo akýkoľvek kontext užitočný pri ladení alebo analýze, napríklad `user_id`, `session_id` alebo `model_version`.

Príklad manuálneho vytvárania trás a spanov s [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Hodnotenie agenta

Pozorovateľnosť nám dáva metriky, no hodnotenie je proces analýzy týchto dát (a vykonávania testov), aby sme zistili, ako dobre AI agent funguje a ako ho možno zlepšiť. Inými slovami, keď máte trasy a metriky, ako ich použijete na posúdenie agenta a prijatie rozhodnutí?

Pravidelné hodnotenie je dôležité, pretože AI agenti sú často nedeterministickí a môžu sa vyvíjať (prostredníctvom aktualizácií alebo posunov správania modelu) – bez hodnotenia by ste nevedeli, či váš "chytrý agent" naozaj dobre plní úlohu alebo či je regres.

Existujú dve kategórie hodnotení AI agentov: **online hodnotenie** a **offline hodnotenie**. Obe sú cenné a dopĺňajú sa. Zvyčajne začíname offline hodnotením, pretože je to minimálny potrebný krok pred nasadením akéhokoľvek agenta.

### Offline hodnotenie

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To zahŕňa hodnotenie agenta v kontrolovanom prostredí, typicky s použitím testovacích datasetov, nie živých používateľských dotazov. Používate kurátorské datasety, kde viete, aký je očakávaný výstup alebo správne správanie, a potom spúšťate agenta na týchto dátach.

Napríklad, ak ste vytvorili agenta na slovné úlohy z matematiky, môžete mať [testovací dataset](https://huggingface.co/datasets/gsm8k) so 100 problémami so známymi odpoveďami. Offline hodnotenie sa často vykonáva počas vývoja (a môže byť súčasťou CI/CD potrubí) na kontrolu zlepšení alebo ochranu pred regresiou. Výhodou je, že je **opakoveľné a môžete získať jasné metriky presnosti, keďže máte pravdivé dáta**. Môžete tiež simulovať používateľské dotazy a merať odpovede agenta voči ideálnym odpovediam alebo použiť automatizované metriky, ako je popísané vyššie.

Kľúčovou výzvou offline hodnotenia je zabezpečiť, aby bol váš testovací dataset komplexný a zostal relevantný – agent môže na pevnej testovacej sade fungovať dobre, ale v produkcii môže čeliť veľmi odlišným dotazom. Preto by ste mali testovacie sady pravidelne aktualizovať o nové okrajové prípady a príklady, ktoré odrážajú reálne scenáre. Kombinácia malých "smoke testov" a väčších hodnotiacich sád je užitočná: malé sady na rýchle kontroly a väčšie na rozšírené metriky výkonu.

### Online hodnotenie

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ide o hodnotenie agenta v živom, reálnom prostredí, teda počas skutočného používania v produkcii. Online hodnotenie zahŕňa monitorovanie výkonu agenta pri reálnych interakciách používateľov a nepretržitú analýzu výsledkov.

Napríklad môžete sledovať miery úspešnosti, skóre spokojnosti používateľov alebo iné metriky na živom dopravnom zaťažení. Výhodou online hodnotenia je, že **zahŕňa veci, ktoré by ste možno v laboratórnych podmienkach nepredpokladali** – môžete pozorovať posuny modelu v čase (ak efektivita agenta klesá s posunom vstupných vzorov) a odhaľovať neočakávané dotazy alebo situácie, ktoré neboli zahrnuté v testovacích dátach. Poskytuje skutočný obraz o správaní agenta v reálnom svete.

Online hodnotenie často zahŕňa zhromažďovanie implicitnej a explicitnej spätnej väzby od používateľov, ako bolo rozprávané, a prípadne spúšťanie shadow testov alebo A/B testov (kde nová verzia agenta beží paralelne na porovnanie so starou). Výzvou je získať spoľahlivé štítky alebo skóre pre živé interakcie – môžete sa spoliehať na spätnú väzbu používateľov alebo následné metriky (napríklad, či používateľ klikol na výsledok).

### Kombinácia oboch

Online a offline hodnotenia nie sú navzájom vylučujúce sa; sú vysoko doplňujúce. Poznatky z online sledovania (napríklad nové typy používateľských dotazov, kde agent podáva slabý výkon) môžu byť použité na rozšírenie a zlepšenie offline testovacích datasetov. Naopak, agenti, ktorí úspešne prejdú offline testami, môžu byť s väčšou istotou nasadení a sledovaní online.

Vo väčšine tímov sa používa cyklus:

_hodnotiť offline -> nasadiť -> sledovať online -> zbierať nové prípady zlyhaní -> pridať do offline datasetu -> vylaďovať agenta -> opakovať_.

## Bežné problémy

Pri nasadzovaní AI agentov do produkcie sa môžete stretnúť s rôznymi výzvami. Tu sú niektoré bežné problémy a ich možné riešenia:

| **Problém**    | **Možné riešenie**   |
| ------------- | ------------------ |
| AI agent nevykonáva úlohy konzistentne | - Upresnite prompt daný AI agentovi; buďte jasní v cieľoch.<br>- Identifikujte miesta, kde môže pomôcť rozdelenie úloh na podúlohy a ich spracovanie viacerými agentmi. |
| AI agent sa dostane do nekonečných slučiek  | - Zabezpečte jasné podmienky ukončenia, aby agent vedel, kedy proces zastaviť.<br>- Pre zložité úlohy vyžadujúce uvažovanie a plánovanie použite väčší model špecializovaný na tieto úlohy. |
| Volania nástrojov AI agenta nefungujú dobre   | - Testujte a validujte výstupy nástroja mimo systému agenta.<br>- Upresnite definované parametre, prompt-y a názvy nástrojov.  |
| Multi-agentný systém nekonzistentný | - Upresnite prompt-y jednotlivým agentom, aby boli špecifické a odlišné.<br>- Vytvorte hierarchický systém s „routing“ alebo riadiacim agentom, ktorý určí správneho agenta. |

Mnohé z týchto problémov možno efektívnejšie identifikovať s implementovanou pozorovateľnosťou. Trasy a metriky, o ktorých sme hovorili, pomáhajú presne určiť, kde v pracovnom postupe agenta vznikajú problémy, čo znamená oveľa efektívnejšie ladenie a optimalizáciu.

## Riadenie nákladov


Tu sú niektoré stratégie na riadenie nákladov pri nasadzovaní AI agentov do produkcie:

**Používanie menších modelov:** Malé jazykové modely (SLM) môžu dobre fungovať v určitých agentných prípadoch použitia a výrazne znížia náklady. Ako bolo spomenuté vyššie, vytvorenie evaluačného systému na určenie a porovnanie výkonu oproti väčším modelom je najlepší spôsob, ako pochopiť, ako dobre bude SLM fungovať vo vašom prípade použitia. Zvážte použitie SLM pre jednoduchšie úlohy ako klasifikáciu zámerov alebo extrakciu parametrov, zatiaľ čo väčšie modely si vyhraďte na zložité uvažovanie.

**Používanie modelu smerovača:** Podobnou stratégiou je použitie rôznorodých modelov a veľkostí. Môžete použiť LLM/SLM alebo serverless funkciu na smerovanie požiadaviek podľa zložitosti na najvhodnejšie modely. Toto tiež pomôže znížiť náklady a zároveň zabezpečí výkon na správnych úlohách. Napríklad smerujte jednoduché dotazy na menšie, rýchlejšie modely a drahé veľké modely používajte iba na zložité úlohy uvažovania.

**Kešovanie odpovedí:** Identifikovanie bežných požiadaviek a úloh a poskytovanie odpovedí skôr, ako prejdú cez váš agentný systém, je dobrý spôsob, ako znížiť objem podobných požiadaviek. Môžete dokonca implementovať tok na určenie, ako veľmi je požiadavka podobná vašim kešovaným požiadavkám, pomocou jednoduchších AI modelov. Táto stratégia môže výrazne znížiť náklady na často kladené otázky alebo bežné pracovné toky.

## Pozrime sa, ako to funguje v praxi

V [príkladovom notebooku tejto sekcie](./code_samples/10-expense_claim-demo.ipynb) uvidíme príklady, ako môžeme použiť nástroje na pozorovateľnosť na monitorovanie a hodnotenie nášho agenta.


### Máte ďalšie otázky o AI agentoch v produkcii?

Pripojte sa na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde sa stretnete s ďalšími študentmi, zúčastníte sa konzultačných hodín a dostanete odpovede na svoje otázky o AI agentoch.

## Predchádzajúca lekcia

[Dizajnový vzor metakognície](../09-metacognition/README.md)

## Nasledujúca lekcia

[Agentné protokoly](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->