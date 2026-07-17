# AI agenti v produkcii: Observabilita a hodnotenie

[![AI agenti v produkcii](../../../translated_images/sk/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Keď sa AI agenti posúvajú od experimentálnych prototypov k reálnym aplikáciám, schopnosť pochopiť ich správanie, monitorovať ich výkon a systematicky hodnotiť ich výstupy sa stáva dôležitou.

## Ciele učenia

Po dokončení tejto lekcie budete vedieť/rozumieť:
- Kľúčové koncepty observability a vyhodnocovania agentov
- Techniky na zlepšenie výkonu, nákladov a efektívnosti agentov
- Čo a ako systematicky hodnotiť AI agentov
- Ako kontrolovať náklady pri nasadzovaní AI agentov do produkcie
- Ako inštruovať agentov postavených na Microsoft Agent Framework

Cieľom je vybaviť vás znalosťami, ako transformovať vaše „čierne skrinky“ agentov na transparentné, spravovateľné a spoľahlivé systémy.

_**Poznámka:** Je veľmi dôležité nasadzovať AI agentov, ktorí sú bezpeční a dôveryhodní. Pozrite si tiež lekciu [Budovanie dôveryhodných AI agentov](../06-building-trustworthy-agents/README.md)._

## Trasy a rozpätia (traces a spans)

Nástroje observability ako [Langfuse](https://langfuse.com/) alebo [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) zvyčajne reprezentujú behy agentov ako trasy a rozpätia.

- **Trasa (Trace)** predstavuje kompletnú úlohu agenta od začiatku do konca (napríklad spracovanie používateľského dotazu).
- **Rozpätia (Spans)** sú jednotlivé kroky v trase (napríklad volanie modelu jazyka alebo získavanie dát).

![Strom trás v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez observability môže AI agent pôsobiť ako „čierna skrinka“ – jeho vnútorný stav a zdôvodnenie sú neprehľadné, čo sťažuje diagnostiku problémov alebo optimalizáciu výkonu. S observabilitou sa agenti stávajú „sklenenými škatulkami“, ponúkajúc transparentnosť, ktorá je nevyhnutná na budovanie dôvery a zabezpečenie správnej funkčnosti.

## Prečo je observabilita dôležitá v produkčnom prostredí

Prechod AI agentov do produkčného prostredia prináša novú sadu výziev a požiadaviek. Observabilita už nie je len „príjemný doplnok“, ale kľúčová schopnosť:

*   **Ladenie a analýza príčin problémov:** Keď agent zlyhá alebo produkuje neočakávaný výstup, nástroje observability poskytujú trasy potrebné na presné identifikovanie zdroja chyby. Toto je obzvlášť dôležité pri zložitých agentoch, ktoré môžu zahŕňať viacnásobné volania LLM, interakcie s nástrojmi a podmienenú logiku.
*   **Manažment latencie a nákladov:** AI agenti často spoliehajú na LLM a ďalšie externé API, ktoré sú účtované za token alebo volanie. Observabilita umožňuje presné sledovanie týchto volaní, pomáha identifikovať operácie, ktoré sú príliš pomalé alebo drahé. To umožňuje tímom optimalizovať promptovanie, vyberať efektívnejšie modely alebo prepracovať pracovné postupy na riadenie nákladov a zabezpečenie dobrého používateľského zážitku.
*   **Dôvera, bezpečnosť a súlad:** V mnohých aplikáciách je dôležité zabezpečiť, aby sa agenti správali bezpečne a eticky. Observabilita poskytuje auditnú stopu činností a rozhodnutí agenta. To môžete využiť na detekciu a zmiernenie problémov ako prompt injection, generovanie škodlivého obsahu alebo zlé nakladanie s osobne identifikovateľnými údajmi (PII). Napríklad môžete prehliadať trasy na pochopenie, prečo agent poskytol určitú odpoveď alebo použil konkrétny nástroj.
*   **Smyčky kontinuálneho zlepšovania:** Dáta z observability sú základom iteratívneho vývojového procesu. Sledovaním výkonu agentov v reálnom svete môžu tímy identifikovať oblasti na zlepšenie, zbierať dáta pre dolaďovanie modelov a overovať vplyv zmien. To vytvára spätnú väzbu, kde produkčné poznatky z online hodnotenia ovplyvňujú offline experimentovanie a zdokonaľovanie, čo vedie k postupne lepšiemu výkonu agentov.

## Kľúčové metriky na sledovanie

Na monitorovanie a pochopenie správania agenta je potrebné sledovať rôzne metriky a signály. Konkrétne metriky sa môžu líšiť podľa účelu agenta, no niektoré sú univerzálne dôležité.

Tu sú niektoré z najbežnejších metrík, ktoré sledujú nástroje observability:

**Latencia:** Ako rýchlo agent odpovedá? Dlhé čakacie doby negatívne ovplyvňujú používateľský zážitok. Mali by ste merať latenciu pre úlohy aj jednotlivé kroky sledovaním behov agenta. Napríklad agent, ktorý vykonáva všetky volania modelu za 20 sekúnd, môže byť zrýchlený použitím rýchlejšieho modelu alebo paralelným spracovaním volaní modelov.

**Náklady:** Aké sú náklady na jeden beh agenta? AI agenti sa spoliehajú na volania LLM účtované za token alebo externé API. Časté používanie nástrojov alebo viaceré promptovania môžu rýchlo navýšiť náklady. Napríklad, ak agent volá LLM päťkrát pre minimálne zlepšenie kvality, musíte posúdiť, či je toto zvýšenie ceny opodstatnené, alebo či môžete znížiť počet volaní alebo použiť lacnejší model. Monitorovanie v reálnom čase môže tiež pomôcť identifikovať neočakávané špičky (napr. chyby spôsobujúce nekonečné cykly volaní API).

**Chyby požiadaviek:** Koľko požiadaviek agentovi zlyhalo? Môže ísť o chyby API alebo zlyhané volania nástrojov. Na zvýšenie odolnosti agenta v produkcii môžete nastaviť záložné postupy alebo opakovania. Napríklad, ak je výpadok poskytovateľa LLM A, prepnite na LLM poskytovateľa B ako zálohu.

**Používateľská spätná väzba:** Implementácia priameho hodnotenia používateľmi poskytuje cenné informácie. Môže ísť o explicitné hodnotenia (👍palec hore/👎dole, ⭐1-5 hviezdičiek) alebo textové komentáre. Konzistentne negatívna spätná väzba by vás mala varovať, pretože naznačuje, že agent nefunguje podľa očakávaní.

**Implicitná používateľská spätná väzba:** Správanie používateľov poskytuje nepriamu spätnú väzbu aj bez explicitných hodnotení. Môže to byť okamžité preformulovanie otázky, opakované dopyty alebo kliknutie na tlačidlo opakovania. Napríklad, ak vidíte, že používatelia opakovane kladú tú istú otázku, je to znak, že agent nefunguje podľa očakávaní.

**Presnosť:** Ako často agent produkuje správne alebo želané výstupy? Definície presnosti sa líšia (napr. správnosť riešenia problému, presnosť vyhľadania informácií, spokojnosť používateľa). Prvým krokom je definovať úspech pre vášho agenta. Presnosť môžete sledovať cez automatizované kontroly, hodnotiace skóre alebo označenia dokončenia úloh. Napríklad označiť trasy ako „úspešné“ alebo „neúspešné“.

**Automatizované hodnotiace metriky:** Môžete tiež nastaviť automatizované vyhodnotenia. Napríklad môžete použiť LLM na ohodnotenie výstupu agenta, či je užitočný, presný alebo nie. Existuje tiež niekoľko open source knižníc, ktoré pomáhajú skórovať rôzne aspekty agenta. Napríklad [RAGAS](https://docs.ragas.io/) pre RAG agentov alebo [LLM Guard](https://llm-guard.com/) na detekciu škodlivého jazyka alebo prompt injection.

V praxi kombinácia týchto metrík poskytuje najlepšie pokrytie zdravotného stavu AI agenta. V tomto kapitole [príkladovom notebooku](./code_samples/10-expense_claim-demo.ipynb) vám ukážeme, ako tieto metriky vyzerajú na reálnych príkladoch, ale najskôr sa naučíme, ako vyzerá typický workflow hodnotenia.

## Inštrumentujte svojho agenta

Na zbieranie dát z trasovania budete musieť inštrumentovať svoj kód. Cieľom je inštrumentovať kód agenta tak, aby emitoval trasy a metriky, ktoré môžu byť zachytené, spracované a vizualizované platformou observability.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) sa stal priemyselným štandardom pre observabilitu LLM. Poskytuje sadu API, SDK a nástrojov pre generovanie, zbieranie a export telemetrických dát.

Existuje mnoho knižníc na inštrumentovanie, ktoré obalia existujúce frameworky agentov a uľahčujú export OpenTelemetry rozpätí do nástroja observability. Microsoft Agent Framework sa nativne integruje s OpenTelemetry. Nižšie je príklad inštrumentácie agenta MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Vykonávanie agenta je automaticky sledované
    pass
```

[Príkladový notebook](./code_samples/10-expense_claim-demo.ipynb) v tejto kapitole vám ukáže, ako inštrumentovať váš MAF agenta.

**Ručné vytváranie rozpätí:** Aj keď inštrumentačné knižnice poskytujú dobrý základ, často sú prípady, keď potrebujete podrobnejšie alebo vlastné informácie. Rozpätia môžete vytvárať manuálne, aby ste pridali vlastnú aplikačnú logiku. Dôležitejšie je, že môžu obohatiť automaticky alebo ručne vytvorené rozpätia o vlastné atribúty (tiež známe ako tagy alebo metadata). Tieto atribúty môžu obsahovať obchodné špecifické dáta, medzivýpočty alebo akýkoľvek kontext užitočný pre ladenie alebo analýzu, napríklad `user_id`, `session_id` alebo `model_version`.

Príklad vytvárania trás a rozpätí manuálne pomocou [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Hodnotenie agenta

Observabilita nám poskytuje metriky, ale hodnotenie je proces analyzovania týchto dát (a vykonávania testov), aby sme určili, ako dobre AI agent funguje a ako ho možno zlepšiť. Inými slovami, keď máte tieto trasy a metriky, ako ich použijete na posúdenie agenta a prijímanie rozhodnutí?

Pravidelné hodnotenie je dôležité, pretože AI agenti sú často nedeterministickí a môžu sa vyvíjať (cez aktualizácie alebo posun správania modelu) – bez hodnotenia by ste nevedeli, či váš „inteligentný agent“ skutočne dobre plní svoju úlohu alebo či došlo k regresii.

Existujú dve kategórie hodnotení AI agentov: **online hodnotenie** a **offline hodnotenie**. Obe sú cenné a vzájomne sa dopĺňajú. Zvyčajne začíname s offline hodnotením, čo je minimálny nevyhnutný krok pred nasadením akéhokoľvek agenta.

### Offline hodnotenie

![Položky dátovej sady v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Toto zahŕňa hodnotenie agenta v kontrolovanom prostredí, typicky pomocou testovacích dátových sád, nie cez živé používateľské dotazy. Používate pripravené dátové sady, kde viete, aký je očakávaný výstup alebo správne správanie, a potom na nich spustíte svojho agenta.

Napríklad, ak ste vytvorili agenta na riešenie slovných úloh z matematiky, môžete mať [testovaciu dátovú sadu](https://huggingface.co/datasets/gsm8k) so 100 príkladmi so známymi odpoveďami. Offline hodnotenie sa často vykonáva počas vývoja (a môže byť súčasťou CI/CD pipeline) na kontrolu zlepšení alebo ochranu proti regresii. Výhodou je, že je **opakované a môžete získať jasné metriky presnosti, pretože máte pravdivé dáta**. Môžete tiež simulovať používateľské dotazy a merať odpovede agenta voči ideálnym odpovediam alebo použiť automatizované metriky, ako bolo opísané vyššie.

Kľúčovou výzvou offline hodnotenia je zabezpečiť, aby vaša testovacia dátová sada bola komplexná a zostala relevantná – agent môže na pevnej testovacej sade obstáť dobre, no v produkcii naraziť na veľmi odlišné dotazy. Preto by ste mali testovacie súbory pravidelne aktualizovať o nové okrajové prípady a príklady, ktoré odrážajú reálne scenáre​. Užitečná je kombinácia malých „smoke testov“ a väčších evaluačných súborov: malé sady na rýchle kontroly a väčšie na širšie metriky výkonu​.

### Online hodnotenie

![Prehľad metrík observability](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Toto sa týka hodnotenia agenta v živom, reálnom prostredí, teda počas skutočného používania v produkcii. Online hodnotenie zahŕňa sledovanie výkonu agenta na reálnych používateľských interakciách a nepretržitú analýzu výsledkov.

Napríklad môžete sledovať miery úspešnosti, skóre spokojnosti používateľov alebo iné metriky počas živého prevádzkovania. Výhodou online hodnotenia je, že **zachytáva veci, ktoré by ste v laboratórnych podmienkach nemuseli predvídať** – môžete pozorovať posun modelu v čase (ak efektívnosť agenta klesá, keď sa menia vzory vstupov) a odhaliť neočakávané dotazy alebo situácie, ktoré neboli v testovacích dátach​. Poskytuje pravdivý obraz o správaní agenta v reálnom svete.

Online hodnotenie často zahŕňa zbieranie implicitnej a explicitnej spätnej väzby od používateľov, ako bolo diskutované, a prípadne prebieha spúšťanie shadow testov alebo A/B testov (kde nová verzia agenta beží paralelne, aby sa porovnala s tou starou). Výzvou je, že môže byť ťažké získať spoľahlivé štítky alebo skóre pre živé interakcie – možno sa spoľahnete na spätnú väzbu používateľov alebo na následné metriky (napríklad, či používateľ klikol na výsledok).

### Kombinácia oboch

Online a offline hodnotenia nie sú navzájom vylučujúce; sú veľmi sa dopĺňajúce. Poznatky z online monitoringu (napríklad nové typy používateľských dotazov, kde agent nefunguje dobre) môžu byť použité na rozšírenie a zlepšenie offline testovacích dátových sád. Naopak, agenti, ktorí dobre obstáli v offline testoch, môžu byť s väčšou istotou nasadení a monitorovaní online.

Mnohé tímy vlastne prijímajú cyklus:

_offline hodnotenie -> nasadenie -> online monitorovanie -> zber nových chýb -> pridanie do offline datasetu -> zdokonalenie agenta -> opakovanie_.

## Bežné problémy

Pri nasadzovaní AI agentov do produkcie sa môžete stretnúť s rôznymi výzvami. Tu sú niektoré bežné problémy a ich možné riešenia:

| **Problém**    | **Možné riešenie**   |
| ------------- | ------------------ |
| AI agent nevykonáva úlohy konzistentne | - Vylepšite prompt, ktorý dávate AI agentovi; buďte jasní v cieľoch.<br>- Určite, kde by rozdelenie úloh na podúlohy riešené viacerými agentmi mohlo pomôcť. |
| AI agent uviazne v nekonečných slučkách  | - Zabezpečte jasné podmienky ukončenia, aby agent vedel, kedy zastaviť proces.<br>- Pre zložité úlohy vyžadujúce uvažovanie a plánovanie použite väčší model špecializovaný na tieto úlohy. |
| Volania nástrojov AI agenta nefungujú dobre  | - Testujte a overte výstup nástroja mimo systému agenta.<br>- Vylepšite definované parametre, promptovanie a pomenovanie nástrojov.  |
| Multi-agentný systém nefunguje konzistentne | - Vylepšite promptovanie pre každého agenta, aby boli špecifické a odlišné.<br>- Vytvorte hierarchický systém s „riadiacim“ alebo kontrolným agentom, ktorý určuje, ktorý agent je správny. |

Mnohé z týchto problémov možno efektívnejšie identifikovať vďaka observabilite. Trasy a metriky, o ktorých sme hovorili, pomáhajú presne určiť, kde v pracovnom postupe agenta sa problémy vyskytujú, čo robí ladenie a optimalizáciu omnoho efektívnejšími.

## Manažment nákladov


Tu je niekoľko stratégií, ako zvládnuť náklady na nasadenie AI agentov do produkcie:

**Použitie menších modelov:** Malé jazykové modely (SLM) môžu dobre fungovať pri niektorých agentných prípadoch použitia a výrazne znížia náklady. Ako už bolo spomenuté, vytvorenie hodnotiaceho systému na určenie a porovnanie výkonu oproti väčším modelom je najlepší spôsob, ako pochopiť, ako dobre bude SLM fungovať vo vašom prípade použitia. Zvážte použitie SLM pre jednoduchšie úlohy, ako je klasifikácia zámerov alebo extrakcia parametrov, pričom väčšie modely vyhraďte na zložité uvažovanie.

**Použitie routerového modelu:** Podobnou stratégiou je používanie rôznych modelov a veľkostí. Môžete použiť LLM/SLM alebo serverless funkciu na smerovanie požiadaviek na najvhodnejšie modely podľa ich zložitosti. Toto tiež pomôže znížiť náklady a zároveň zabezpečiť výkon na správnych úlohách. Napríklad, smerujte jednoduché dotazy na menšie, rýchlejšie modely a drahé veľké modely používajte len pre zložité rozumové úlohy.

**Ukladanie odpovedí do cache:** Identifikácia bežných požiadaviek a úloh a poskytovanie odpovedí ešte predtým, než prejdú cez váš agentný systém, je dobrý spôsob, ako znížiť množstvo podobných požiadaviek. Môžete dokonca implementovať tok na identifikovanie, ako veľmi je požiadavka podobná vašim cachovaným požiadavkám, pomocou jednoduchších AI modelov. Táto stratégia môže výrazne znížiť náklady pri často kladených otázkach alebo bežných pracovných tokoch.

## Pozrime sa, ako to funguje v praxi

V [ukážkovom notebooku tejto sekcie](./code_samples/10-expense_claim-demo.ipynb) uvidíme príklady, ako môžeme použiť nástroje na pozorovanie na monitorovanie a hodnotenie nášho agenta.


### Máte ďalšie otázky o AI agentech v produkcii?

Pripojte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), stretnite sa s ďalšími študentmi, zúčastnite sa konzultačných hodín a získajte odpovede na svoje otázky o AI agentoch.

## Predchádzajúca lekcia

[Metacognition Design Pattern](../09-metacognition/README.md)

## Nasledujúca lekcia

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->