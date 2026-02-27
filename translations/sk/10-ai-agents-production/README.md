# AI Agenti v produkcii: Pozorovateľnosť a hodnotenie

[![AI Agenti v produkcii](../../../translated_images/sk/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Keď sa AI agenti presúvajú z experimentálnych prototypov do reálnych aplikácií, schopnosť porozumieť ich správaniu, monitorovať ich výkon a systematicky hodnotiť ich výstupy sa stáva dôležitou.

## Ciele učenia

Po dokončení tejto lekcie budete vedieť/rozumieť:
- Základné koncepty pozorovateľnosti a hodnotenia agentov
- Techniky na zlepšenie výkonu, nákladov a efektívnosti agentov
- Čo a ako systematicky hodnotiť vašich AI agentov
- Ako kontrolovať náklady pri nasadení AI agentov do produkcie
- Ako instrumentovať agentov postavených pomocou Microsoft Agent Framework

Cieľom je vybaviť vás vedomosťami potrebnými na premenu vašich "čiernych skríň" agentov na transparentné, spravovateľné a spoľahlivé systémy.

_**Poznámka:** Je dôležité nasadzovať AI agentov, ktorí sú bezpeční a dôveryhodní. Pozrite si tiež lekciu [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md)._

## Trasy a úseky

Nástroje na pozorovateľnosť, ako napríklad [Langfuse](https://langfuse.com/) alebo [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), zvyčajne reprezentujú behy agenta ako trasy a úseky.

- **Trasa** predstavuje kompletnú úlohu agenta od začiatku do konca (napr. spracovanie používateľského dotazu).
- **Úseky** sú jednotlivé kroky v rámci trasy (napr. volanie jazykového modelu alebo získavanie údajov).

![Strom trasovania v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez pozorovateľnosti môže AI agent pôsobiť ako "čierna skrinka" — jeho vnútorný stav a uvažovanie sú nepriehľadné, čo sťažuje diagnostiku problémov alebo optimalizáciu výkonu. S pozorovateľnosťou sa agenti stávajú "sklenenými skrinkami", poskytujúcimi transparentnosť, ktorá je nevyhnutná na budovanie dôvery a zabezpečenie toho, aby fungovali podľa očakávaní.

## Prečo je pozorovateľnosť dôležitá v produkčných prostrediach

Prechod AI agentov do produkcie prináša nové výzvy a požiadavky. Pozorovateľnosť už nie je „príjemným doplnkom“, ale kľúčovou schopnosťou:

*   **Ladenie a analýza koreňovej príčiny**: Keď agent zlyhá alebo vygeneruje neočakávaný výstup, nástroje pozorovateľnosti poskytujú trasy potrebné na určenie zdroja chyby. To je obzvlášť dôležité pri zložitých agentoch, ktoré môžu zahŕňať viacero volaní LLM, interakcie s nástrojmi a podmienenú logiku.
*   **Riadenie latencie a nákladov**: AI agenti často závisia od LLM a iných externých API, ktoré sú účtované za token alebo za volanie. Pozorovateľnosť umožňuje presné sledovanie týchto volaní a pomáha identifikovať operácie, ktoré sú nadmerne pomalé alebo nákladné. To tímom umožňuje optimalizovať promptovanie, vybrať efektívnejšie modely alebo prepracovať pracovné postupy na riadenie prevádzkových nákladov a zabezpečenie dobrej používateľskej skúsenosti.
*   **Dôvera, bezpečnosť a súlad**: V mnohých aplikáciách je dôležité zabezpečiť, aby sa agenti správali bezpečne a eticky. Pozorovateľnosť poskytuje auditnú stopu činností a rozhodnutí agenta. Túto stopu možno využiť na detekciu a zmiernenie problémov, ako sú prompt injection, generovanie škodlivého obsahu alebo nesprávne zaobchádzanie s osobne identifikovateľnými údajmi (PII). Napríklad môžete prehliadnuť trasy, aby ste pochopili, prečo agent poskytol určitú odpoveď alebo použil konkrétny nástroj.
*   **Smyčky kontinuálneho zlepšovania**: Dáta z pozorovateľnosti sú základom iteratívneho vývojového procesu. Sledovaním výkonu agentov v reálnom svete môžu tímy identifikovať oblasti na zlepšenie, zhromažďovať dáta na doladenie modelov a overovať dopad zmien. To vytvára spätnú väzbu, kde produkčné poznatky z online hodnotenia informujú offline experimentovanie a vylepšovanie, čo vedie k postupnému zlepšovaniu výkonu agentov.

## Kľúčové metriky na sledovanie

Na monitorovanie a pochopenie správania agenta by sa mala sledovať škála metrík a signálov. Konkrétne metriky sa môžu líšiť podľa účelu agenta, ale niektoré sú univerzálne dôležité.

Tu sú niektoré z najbežnejších metrík, ktoré nástroje pozorovateľnosti sledujú:

**Latencia:** Ako rýchlo agent odpovedá? Dlhé čakanie negatívne ovplyvňuje používateľskú skúsenosť. Mali by ste merať latenciu pre úlohy a jednotlivé kroky sledovaním trás behu agenta. Napríklad agent, ktorý potrebuje 20 sekúnd na všetky volania modelu, je možné zrýchliť použitím rýchlejšieho modelu alebo paralelným spustením volaní modelu.

**Náklady:** Aké sú náklady na jeden beh agenta? AI agenti sa spoliehajú na volania LLM účtované za token alebo na externé API. Časté používanie nástrojov alebo viacnásobné promptovanie môže rýchlo zvýšiť náklady. Napríklad, ak agent volá LLM päťkrát pre marginálne zlepšenie kvality, je potrebné zvážiť, či sú náklady opodstatnené, alebo či môžete znížiť počet volaní alebo použiť lacnejší model. Monitorovanie v reálnom čase môže tiež pomôcť odhaliť neočakávané špičky (napr. chyby spôsobujúce nadmerné API slučky).

**Chyby požiadaviek:** Koľko požiadaviek agent zlyhal? Sem môžu patriť chyby API alebo zlyhané volania nástrojov. Aby bol agent v produkcii odolnejší voči týmto chybám, môžete nastaviť fallbacky alebo opakovania. Napr. ak poskytovateľ LLM A nie je dostupný, prepnite na poskytovateľa LLM B ako zálohu.

**Spätná väzba používateľa:** Implementovanie priameho hodnotenia používateľmi poskytuje cenné poznatky. Môže ísť o explicitné hodnotenia (👍palec hore/👎dol, ⭐1-5 hviezdičiek) alebo textové komentáre. Konzistentne negatívna spätná väzba by vás mala upozorniť, pretože to znamená, že agent nefunguje podľa očakávaní.

**Implicitná spätná väzba používateľa:** Správanie používateľov poskytuje nepriame signály aj bez explicitných hodnotení. Môže ísť o okamžité preformulovanie otázky, opakované dotazy alebo kliknutie na tlačidlo opakovať. Napr. ak vidíte, že používatelia opakovane kladú tú istú otázku, je to znak, že agent nefunguje podľa očakávaní.

**Presnosť:** Ako často agent produkuje správne alebo žiaduce výstupy? Definície presnosti sa líšia (napr. správnosť riešenia problémov, presnosť získavania informácií, spokojnosť používateľa). Prvým krokom je definovať, čo pre vášho agenta znamená úspech. Presnosť môžete sledovať pomocou automatizovaných kontrol, evaluačných skóre alebo označení dokončenia úloh. Napríklad označovanie trás ako "succeeded" alebo "failed".

**Automatizované evaluačné metriky:** Môžete tiež nastaviť automatizované hodnotenia. Napríklad môžete použiť LLM na ohodnotenie výstupu agenta, či bol užitočný, presný alebo nie. Existuje tiež niekoľko open source knižníc, ktoré vám pomôžu ohodnotiť rôzne aspekty agenta. Napr. [RAGAS](https://docs.ragas.io/) pre RAG agentov alebo [LLM Guard](https://llm-guard.com/) na detekciu škodlivého jazyka alebo prompt injection.

V praxi poskytuje kombinácia týchto metrík najlepšie pokrytie zdravia AI agenta. V tomto kapitole v [príkladnom notebooku](./code_samples/10-expense_claim-demo.ipynb) vám ukážeme, ako tieto metriky vyzerajú v reálnych príkladoch, ale najprv sa naučíme, ako vyzerá typický evaluačný pracovný tok.

## Instrumentujte svojho agenta

Aby ste zbierali dáta o trasách, budete musieť instrumentovať svoj kód. Cieľom je instrumentovať kód agenta tak, aby emitoval trasy a metriky, ktoré môže zachytiť, spracovať a vizualizovať platforma pozorovateľnosti.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) sa etablovalo ako priemyselný štandard pre pozorovateľnosť LLM. Poskytuje súbor API, SDK a nástrojov na generovanie, zbieranie a export telemetrických dát.

Existuje mnoho instrumentačných knižníc, ktoré obalujú existujúce rámce agentov a uľahčujú export OpenTelemetry úsekov do nástroja pozorovateľnosti. Microsoft Agent Framework sa s OpenTelemetry integruje natívne. Nižšie je príklad instrumentovania MAF agenta:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Vykonávanie agenta sa automaticky sleduje
    pass
```

Príkladný notebook v tejto kapitole ([example notebook](./code_samples/10-expense_claim-demo.ipynb)) ukáže, ako instrumentovať vášho MAF agenta.

**Manuálne vytváranie úsekov:** Hoci instrumentačné knižnice poskytujú dobrý východiskový bod, často sú prípady, kde je potrebné podrobnejšie alebo vlastné informácie. Môžete manuálne vytvárať úseky na pridanie vlastnej aplikačnej logiky. Dôležitejšie je, že môžete obohatiť automaticky alebo manuálne vytvorené úseky o vlastné atribúty (tiež známe ako tagy alebo metadáta). Tieto atribúty môžu zahŕňať biznisovo špecifické údaje, medzivýpočty alebo akýkoľvek kontext, ktorý môže byť užitočný pri ladení alebo analýze, ako napr. `user_id`, `session_id` alebo `model_version`.

Príklad manuálneho vytvárania trás a úsekov s [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Hodnotenie agenta

Pozorovateľnosť nám poskytuje metriky, ale hodnotenie je proces analyzovania týchto dát (a vykonávania testov) s cieľom určiť, ako dobre AI agent funguje a ako ho možno zlepšiť. Inými slovami, keď už máte trasy a metriky, ako ich použijete na posúdenie agenta a prijímanie rozhodnutí?

Pravidelné hodnotenie je dôležité, pretože AI agenti sú často nedeterministickí a môžu sa vyvíjať (prostredníctvom aktualizácií alebo driftu modelu) – bez hodnotenia by ste nevedeli, či váš „inteligentný agent“ skutočne plní svoju úlohu správne alebo či došlo k regresii.

Sú dve kategórie hodnotení pre AI agentov: **online hodnotenie** a **offline hodnotenie**. Obe sú cenné a vzájomne sa dopĺňajú. Zvyčajne začíname offline hodnotením, pretože je to minimálny nevyhnutný krok pred nasadením agenta.

### Offline hodnotenie

![Položky datasetu v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To zahŕňa hodnotenie agenta v kontrolovanom prostredí, zvyčajne pomocou testovacích datasetov, nie živých používateľských dopytov. Používate kurátorské datasety, kde viete, aký je očakávaný výstup alebo správne správanie, a potom spustíte agenta na týchto dátach.

Napríklad, ak ste vytvorili agenta na riešenie slovných matematických úloh, môžete mať [testovací dataset](https://huggingface.co/datasets/gsm8k) so 100 problémami s známymi odpoveďami. Offline hodnotenie sa často vykonáva počas vývoja (a môže byť súčasťou CI/CD pipeline) na overenie zlepšení alebo ochranu pred regresiami. Výhodou je, že je **opakované a môžete získať jasné metriky presnosti, pretože máte referenčnú pravdu**. Môžete tiež simulovať používateľské dotazy a merať odpovede agenta oproti ideálnym odpovediam alebo použiť automatizované metriky, ako bolo opísané vyššie.

Kľúčovou výzvou pri offline hodnotení je zabezpečenie, že váš testovací dataset je komplexný a zostáva relevantný – agent môže mať dobré výsledky na pevnom teste, ale v produkcii sa stretnúť s veľmi odlišnými dopytmi. Preto by ste mali testovacie sady priebežne aktualizovať o nové hraničné prípady a príklady, ktoré odrážajú reálne scenáre. Užitočná je kombinácia malých „smoke testov“ a väčších evaluačných sád: malé sady na rýchle kontroly a väčšie na širšie meranie výkonu.

### Online hodnotenie 

![Prehľad metrík pozorovateľnosti](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Týka sa hodnotenia agenta v živom, reálnom prostredí, t.j. počas skutočného používania v produkcii. Online hodnotenie zahŕňa monitorovanie výkonu agenta na reálnych interakciách používateľov a priebežnú analýzu výsledkov.

Napríklad môžete sledovať miery úspešnosti, skóre spokojnosti používateľov alebo iné metriky na živej prevádzke. Výhodou online hodnotenia je, že **zachytáva veci, ktoré by ste v laboratórnom nastavení nemuseli očakávať** – môžete pozorovať drift modelu v čase (ak účinnosť agenta klesá pri zmene vstupných vzorov) a zachytiť neočakávané dotazy alebo situácie, ktoré neboli v testovacích dátach. Poskytuje skutočný obraz toho, ako sa agent správa v reálnom svete.

Online hodnotenie často zahŕňa zhromažďovanie implicitnej a explicitnej spätnej väzby používateľov, ako bolo diskutované, a prípadne spúšťanie shadow testov alebo A/B testov (kde nová verzia agenta beží paralelne, aby sa porovnala so starou). Výzvou je, že môže byť ťažké získať spoľahlivé označenia alebo skóre pre živé interakcie – možno budete závislí na spätnej väzbe používateľov alebo na downstream metrikách (napr. či používateľ klikol na výsledok).

### Kombinovanie oboch

Online a offline hodnotenia sa nevylučujú; sú vysoko doplňujúce. Poznatky z online monitorovania (napr. nové typy používateľských dopytov, kde agent funguje slabšie) môžu byť použité na rozšírenie a zlepšenie offline testovacích datasetov. Naopak, agenti, ktorí dobre fungujú v offline testoch, môžu byť následne s väčšou istotou nasadení a monitorovaní online.

Mnohé tímy v praxi prijímajú slučku:

_hodnoťte offline -> nasadíte -> monitorujte online -> zbierajte nové chybové prípady -> pridajte do offline datasetu -> zdokonaľte agenta -> opakujte_.

## Bežné problémy

Pri nasadení AI agentov do produkcie sa môžete stretnúť s rôznymi výzvami. Tu sú niektoré bežné problémy a ich možné riešenia:

| **Problém**    | **Možné riešenie**   |
| ------------- | ------------------ |
| Agent AI nevykonáva úlohy konzistentne | - Upresnite prompt, ktorý dávate AI agentovi; buďte jasní v cieľoch.<br>- Identifikujte, kde môže pomôcť rozdelenie úloh na podsúbory a ich spracovanie viacerými agentmi. |
| Agent AI uviazne v nekonečných slučkách  | - Zabezpečte jasné podmienky ukončenia, aby agent vedel, kedy proces zastaviť.<br>- Pre zložité úlohy vyžadujúce uvažovanie a plánovanie použite väčší model špecializovaný na úlohy vyžadujúce dedukciu. |
| Volania nástrojov agenta nefungujú dobre   | - Testujte a validujte výstup nástroja mimo systému agenta.<br>- Upresnite definované parametre, prompty a pomenovanie nástrojov.  |
| Viacagentový systém nefunguje konzistentne | - Upresnite prompty každému agentovi, aby boli špecifické a odlišné medzi sebou.<br>- Postavte hierarchický systém s "routing" alebo kontrolným agentom, ktorý určí, ktorý agent je vhodný. |

Mnohé z týchto problémov je možné identifikovať efektívnejšie s nasadenou pozorovateľnosťou. Trasy a metriky, ktoré sme spomenuli, pomáhajú presne určiť, kde v pracovnom toku agenta problémy vznikajú, čo zefektívňuje ladenie a optimalizáciu.

## Riadenie nákladov
Tu sú niektoré stratégie na riadenie nákladov pri nasadzovaní AI agentov do produkcie:

**Použitie menších modelov:** Small Language Models (SLMs) sa môžu dobre uplatniť v niektorých agentných prípadoch použitia a výrazne znížia náklady. Ako už bolo spomenuté, vytvorenie evaluačného systému na určenie a porovnanie výkonu oproti väčším modelom je najlepší spôsob, ako zistiť, ako dobre sa SLM osvedčí pre váš prípad použitia. Zvážte používanie SLMs pre jednoduchšie úlohy, ako je klasifikácia zámeru alebo extrakcia parametrov, a väčšie modely používajte iba pre zložité odôvodňovanie.

**Použitie smerovacieho modelu:** Podobnou stratégiou je využívať rôznorodosť modelov a veľkostí. Môžete použiť LLM/SLM alebo bezserverovú funkciu na smerovanie požiadaviek podľa zložitosti na najvhodnejšie modely. To tiež pomôže znížiť náklady a zároveň zabezpečiť výkon pri správnych úlohách. Napríklad smerujte jednoduché dotazy na menšie, rýchlejšie modely a drahé veľké modely používajte len pri zložitých úlohách vyžadujúcich odôvodňovanie.

**Kešovanie odpovedí:** Identifikovanie bežných požiadaviek a úloh a poskytnutie odpovedí ešte predtým, než prejdú vaším agentným systémom, je dobrý spôsob, ako znížiť počet podobných požiadaviek. Môžete dokonca implementovať proces na určenie, ako veľmi je požiadavka podobná vašim kešovaným požiadavkám, pomocou jednoduchších AI modelov. Táto stratégia môže významne znížiť náklady pre často kladené otázky alebo bežné pracovné postupy.

## Pozrime sa, ako to funguje v praxi

V [ukážkovom notebooku tejto sekcie](./code_samples/10-expense_claim-demo.ipynb) uvidíme príklady, ako môžeme použiť nástroje na observabilitu na monitorovanie a hodnotenie nášho agenta.

### Máte ďalšie otázky o nasadzovaní AI agentov do produkcie?

Pripojte sa k [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) a stretnite sa s ďalšími študentmi, zúčastnite sa konzultačných hodín a získajte odpovede na svoje otázky o AI agentoch.

## Predchádzajúca lekcia

[Návrhový vzor metakognície](../09-metacognition/README.md)

## Ďalšia lekcia

[Agentné protokoly](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vyhlásenie o vylúčení zodpovednosti:
Tento dokument bol preložený pomocou služby AI prekladu Co‑op Translator (https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, berte prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku treba považovať za rozhodujúci zdroj. Pre kritické informácie odporúčame profesionálny preklad vykonaný človekom. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->