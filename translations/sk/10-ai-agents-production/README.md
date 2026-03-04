# AI agenti v produkcii: Pozorovateľnosť a hodnotenie

[![AI agenti v produkcii](../../../translated_images/sk/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Keď sa AI agenti presúvajú z experimentálnych prototypov do reálnych aplikácií, schopnosť porozumieť ich správaniu, monitorovať ich výkon a systematicky hodnotiť ich výstupy sa stáva dôležitou.

## Ciele učenia

Po dokončení tejto lekcie budete vedieť/rozumieť:
- Základné pojmy pozorovateľnosti a hodnotenia agentov
- Techniky na zlepšenie výkonu, nákladov a efektívnosti agentov
- Čo a ako systematicky hodnotiť vašich AI agentov
- Ako kontrolovať náklady pri nasadzovaní AI agentov do produkcie
- Ako instrumentovať agentov vytvorených pomocou AutoGen

Cieľom je vybaviť vás poznatkami, ktoré premenia vaše „čierne skrinky“ agentov na priehľadné, spravovateľné a spoľahlivé systémy.

_**Poznámka:** Je dôležité nasadzovať AI agentov, ktorí sú bezpeční a dôveryhodní. Pozrite si tiež lekciu [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Trasy (traces) a úseky (spans)

Nástroje pre pozorovateľnosť, ako napr. [Langfuse](https://langfuse.com/) alebo [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), zvyčajne reprezentujú behy agentov ako trasy (traces) a úseky (spans).

- **Trasa (Trace)** reprezentuje kompletnú úlohu agenta od začiatku do konca (napr. spracovanie používateľského dopytu).
- **Úseky (Spans)** sú jednotlivé kroky v trase (napr. volanie jazykového modelu alebo získavanie dát).

![Strom trasy v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Bez pozorovateľnosti môže AI agent pôsobiť ako „čierna skrinka“ – jeho vnútorný stav a uvažovanie sú nepriehľadné, čo sťažuje diagnostiku problémov alebo optimalizáciu výkonu. S pozorovateľnosťou sa agenti stávajú „sklenenými skrinkami“, ktoré poskytujú priehľadnosť nevyhnutnú na budovanie dôvery a zaistenie správnej činnosti.

## Prečo je pozorovateľnosť dôležitá v produkčnom prostredí

Prechod AI agentov do produkčných prostredí prináša novú sadu výziev a požiadaviek. Pozorovateľnosť už nie je „príjemným doplnkom“, ale kritickou schopnosťou:

*   **Ladenie a analýza koreňových príčin**: Keď agent zlyhá alebo vygeneruje neočakávaný výstup, nástroje pre pozorovateľnosť poskytnú trasy potrebné na určenie zdroja chyby. To je obzvlášť dôležité pri zložitých agentoch, ktoré môžu zahŕňať viacero volaní LLM, interakcie s nástrojmi a podmienenú logiku.
*   **Riadenie latencie a nákladov**: AI agenti často závisia od LLM a iných externých API, ktoré sa účtujú za token alebo za volanie. Pozorovateľnosť umožňuje presné sledovanie týchto volaní a pomáha identifikovať operácie, ktoré sú nadmerne pomalé alebo nákladné. To umožňuje tímom optimalizovať promptovanie, vybrať efektívnejšie modely alebo prerobiť pracovné toky tak, aby sa riadili prevádzkové náklady a zabezpečila dobrá používateľská skúsenosť.
*   **Dôvera, bezpečnosť a súlad**: V mnohých aplikáciách je dôležité zabezpečiť, aby sa agenti správali bezpečne a eticky. Pozorovateľnosť poskytuje auditnú stopu akcií a rozhodnutí agenta. Túto stopu je možné využiť na detekciu a zmiernenie problémov, ako sú prompt injection, generovanie škodlivého obsahu alebo nesprávne zaobchádzanie s osobnými údajmi (PII). Napríklad môžete preskúmať trasy, aby ste pochopili, prečo agent poskytol určitú odpoveď alebo použil konkrétny nástroj.
*   **Cykly kontinuálneho zlepšovania**: Dáta z pozorovateľnosti sú základom iteratívneho vývojového procesu. Monitorovaním, ako sa agenti správajú v reálnom svete, tím môže identifikovať oblasti na zlepšenie, zbierať dáta pre doladenie modelov a overovať dopad zmien. To vytvára spätnú väzbu, kde produkčné poznatky z online hodnotenia informujú offline experimentovanie a zdokonaľovanie, čo vedie k postupnému zlepšovaniu výkonu agenta.

## Kľúčové metriky na sledovanie

Na monitorovanie a pochopenie správania agenta by sa mala sledovať rada metrík a signálov. Konkrétne metriky sa môžu líšiť podľa účelu agenta, ale niektoré sú univerzálne dôležité.

Tu sú niektoré z najbežnejších metrík, ktoré nástroje pre pozorovateľnosť sledujú:

**Latencia:** Ako rýchlo agent odpovedá? Dlhé čakanie negatívne ovplyvňuje používateľskú skúsenosť. Mali by ste merať latenciu pre úlohy a jednotlivé kroky sledovaním trás behov agenta. Napr. agent, ktorý potrebuje 20 sekúnd pre všetky volania modelu, by sa dal zrýchliť použitím rýchlejšieho modelu alebo spustením volaní modelu paralelne.

**Náklady:** Aké sú náklady na jeden beh agenta? AI agenti závisia na volaniach LLM účtovaných za token alebo na externých API. Časté používanie nástrojov alebo viacero promptov môže rýchlo zvýšiť náklady. Napr. ak agent volá LLM päťkrát pre marginálne zlepšenie kvality, musíte zvážiť, či sú náklady oprávnené alebo či môžete znížiť počet volaní alebo použiť lacnejší model. Monitorovanie v reálnom čase tiež môže pomôcť identifikovať neočakávané výkyvy (napr. chyby spôsobujúce nadmerné opakované volania API).

**Chyby požiadaviek:** Koľko požiadaviek agent zlyhal? To môže zahŕňať chyby API alebo zlyhané volania nástrojov. Aby bol agent v produkcii robustnejší voči týmto chybám, môžete nastaviť fallback mechanizmy alebo opakovania. Napr. ak poskytovateľ LLM A je nedostupný, prepnite na poskytovateľa B ako zálohu.

**Spätná väzba od používateľov:** Implementácia priameho hodnotenia používateľmi poskytuje cenné informácie. Môže to zahŕňať explicitné hodnotenia (👍palec hore/👎dole, ⭐1–5 hviezdičiek) alebo textové komentáre. Konzistentne negatívna spätná väzba by vás mala upozorniť, pretože je to znak, že agent nefunguje podľa očakávania.

**Implicitná spätná väzba od používateľov:** Správanie používateľov poskytuje nepriamu spätnú väzbu aj bez explicitného hodnotenia. Môže to zahŕňať okamžité preformulovanie otázky, opakované dopyty alebo kliknutie na tlačidlo opakovania. Napr. ak vidíte, že používatelia opakovane kladú rovnakú otázku, je to znak, že agent nefunguje očakávane.

**Presnosť:** Ako často agent generuje správne alebo požadované výstupy? Definície presnosti sa líšia (napr. správnosť riešenia úloh, presnosť vyhľadávania informácií, spokojnosť používateľa). Prvým krokom je definovať, ako vyzerá úspech pre vášho agenta. Presnosť môžete sledovať cez automatizované kontroly, evaluačné skóre alebo označenia dokončenia úloh. Napr. označovanie trás ako „succeeded“ alebo „failed“.

**Automatizované metriky hodnotenia:** Môžete tiež nastaviť automatizované hodnotenia. Napr. môžete použiť LLM na ohodnotenie výstupu agenta, či je užitočný, presný alebo nie. Existuje aj niekoľko open-source knižníc, ktoré pomáhajú skórovať rôzne aspekty agenta, napr. [RAGAS](https://docs.ragas.io/) pre RAG agentov alebo [LLM Guard](https://llm-guard.com/) na detekciu škodlivého jazyka alebo prompt injection.

V praxi kombinácia týchto metrík poskytuje najlepšie pokrytie zdravia AI agenta. V tomto kapitole v [ukážkovom notebooku](./code_samples/10_autogen_evaluation.ipynb) vám ukážeme, ako tieto metriky vyzerajú na reálnych príkladoch, ale najprv sa naučíme, ako vyzerá typický evaluačný pracovný tok.

## Instrumentujte svojho agenta

Na zhromažďovanie sledovacích dát budete musieť instrumentovať svoj kód. Cieľom je instrumentovať kód agenta tak, aby emitoval trasy a metriky, ktoré môže zachytiť, spracovať a vizualizovať platforma pre pozorovateľnosť.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) sa etabloval ako priemyselný štandard pre pozorovateľnosť LLM. Poskytuje sadu API, SDK a nástrojov na generovanie, zber a export telemetrických dát.

Existuje mnoho instrumentačných knižníc, ktoré obalia existujúce rámce agentov a uľahčujú export OpenTelemetry spanov do nástroja pre pozorovateľnosť. Nižšie je príklad instrumentácie AutoGen agenta s použitím knižnice [OpenLit instrumentation](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

V [ukážkovom notebooku](./code_samples/10_autogen_evaluation.ipynb) v tejto kapitole vám ukážeme, ako instrumentovať váš AutoGen agent.

**Manuálne vytváranie spanov:** Hoci instrumentačné knižnice poskytujú dobrý východiskový bod, často sú prípady, kde potrebujete detailnejšie alebo vlastné informácie. Môžete manuálne vytvárať spany na pridanie vlastnej aplikačnej logiky. Dôležitejšie je, že môžu obohatiť automaticky alebo manuálne vytvorené spany o vlastné atribúty (známe tiež ako tagy alebo metadata). Tieto atribúty môžu obsahovať obchodne špecifické dáta, medzivýpočty alebo akýkoľvek kontext, ktorý môže byť užitočný pri ladení alebo analýze, napr. `user_id`, `session_id` alebo `model_version`.

Príklad manuálneho vytvorenia trás a spanov s [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Hodnotenie agenta

Pozorovateľnosť nám poskytuje metriky, ale hodnotenie je proces analýzy týchto dát (a vykonávania testov) s cieľom určiť, ako dobre AI agent funguje a ako ho možno zlepšiť. Inými slovami, keď máte tieto trasy a metriky, ako ich používate na zhodnotenie agenta a prijímanie rozhodnutí?

Pravidelné hodnotenie je dôležité, pretože AI agenti často nie sú deterministickí a môžu sa vyvíjať (cez aktualizácie alebo driftovanie správania modelu) – bez hodnotenia by ste nevedeli, či váš „inteligentný agent“ skutočne plní svoje úlohy dobre alebo či nedošlo k regresii.

Existujú dve kategórie hodnotení AI agentov: **online hodnotenie** a **offline hodnotenie**. Obe sú cenné a dopĺňajú sa navzájom. Zvyčajne začíname offline hodnotením, keďže je to minimálny potrebný krok pred nasadením akéhokoľvek agenta.

### Offline hodnotenie

![Položky datasetu v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To zahŕňa hodnotenie agenta v kontrolovanom prostredí, typicky s použitím testovacích datasetov, nie s živými používateľskými dopytmi. Používate kurátorské datasety, kde viete, aký očakávaný výstup alebo správne správanie má byť, a potom na nich spustíte agenta.

Napríklad, ak ste vytvorili agenta na riešenie slovných úloh z matematiky, môžete mať [testovací dataset](https://huggingface.co/datasets/gsm8k) 100 problémov so známymi odpoveďami. Offline hodnotenie sa často vykonáva počas vývoja (a môže byť súčasťou CI/CD) na overenie zlepšení alebo ochrany pred regresiami. Výhodou je, že je **opakovateľné a môžete získať jasné metriky presnosti, pretože máte ground truth**. Môžete tiež simulovať používateľské dopyty a merať odpovede agenta oproti ideálnym odpovediam alebo použiť automatizované metriky, ako boli popísané vyššie.

Kľúčovou výzvou offline hodnotenia je zabezpečiť, že váš testovací dataset je komplexný a zostáva relevantný – agent môže dobre prechádzať fixným testom, no v produkcii sa stretnúť s veľmi odlišnými dopytmi. Preto by ste mali udržiavať testovacie sady aktualizované o nové hraničné prípady a príklady, ktoré odrážajú reálne scenáre​. Užitočná je kombinácia malých „smoke testov“ a väčších evaluačných sád: malé sú na rýchle kontroly, veľké na širšie metriky výkonu​.

### Online hodnotenie

![Prehľad metrík pozorovateľnosti](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

To sa týka hodnotenia agenta v živom, reálnom prostredí, t.j. počas skutočného používania v produkcii. Online hodnotenie zahŕňa monitorovanie výkonu agenta pri reálnych používateľských interakciách a kontinuálnu analýzu výsledkov.

Napríklad môžete sledovať mieru úspešnosti, skóre spokojnosti používateľov alebo iné metriky na živej prevádzke. Výhodou online hodnotenia je, že **zachytáva veci, ktoré v laboratórnom prostredí možno neočakávate** – môžete pozorovať drift modelu v čase (ak efektívnosť agenta klesá, keď sa menia vstupné vzorce) a zachytiť neočakávané dopyty alebo situácie, ktoré neboli v testovacích dátach​. Poskytuje skutočný obraz o tom, ako sa agent správa v teréne.

Online hodnotenie často zahŕňa zber implicitnej a explicitnej spätnej väzby od používateľov, ako už bolo diskutované, a prípadne spúšťanie shadow testov alebo A/B testov (kde nová verzia agenta beží paralelne pre porovnanie so starou). Výzvou je získať spoľahlivé štítky alebo skóre pre živé interakcie – možno budete spoliehať na spätnú väzbu používateľov alebo downstream metriky (napr. či používateľ klikol na výsledok).

### Kombinácia oboch

Online a offline hodnotenia sa nevylučujú; sú veľmi komplementárne. Poznatky z online monitorovania (napr. nové typy používateľských dopytov, kde agent nepracuje dobre) môžu byť použité na rozšírenie a zlepšenie offline testovacích datasetov. Naopak, agenti, ktorí dobre prechádzajú offline testami, môžu byť následne so väčšou istotou nasadení a monitorovaní online.

V skutočnosti mnoho tímov prijíma cyklus:

_vyhodnotiť offline -> nasadiť -> monitorovať online -> zhromaždiť nové chybné prípady -> pridať do offline datasetu -> vylepšiť agenta -> opakovať_.

## Bežné problémy

Pri nasadzovaní AI agentov do produkcie môžete naraziť na rôzne výzvy. Tu sú niektoré bežné problémy a ich možné riešenia:

| **Problém**    | **Možné riešenie**   |
| ------------- | ------------------ |
| AI agent nevykonáva úlohy konzistentne | - Zlepšite prompt (výzvu) poskytnutú AI agentovi; buďte jasní v cieľoch.<br>- Identifikujte, kde môže pomôcť rozdeliť úlohy na podúlohy a priradiť ich viacerým agentom. |
| AI agent sa dostáva do nekonečných slučiek  | - Uistite sa, že máte jasné podmienky ukončenia, aby agent vedel, kedy proces ukončiť.<br>- Pre komplexné úlohy, ktoré vyžadujú uvažovanie a plánovanie, použite väčší model špecializovaný na rozumové úlohy. |
| Volania nástrojov AI agenta nefungujú dobre   | - Otestujte a overte výstup nástroja mimo systému agenta.<br>- Vylepšite definované parametre, prompty a pomenovanie nástrojov.  |
| Systém viacerých agentov nefunguje konzistentne | - Vylepšite prompty pre každého agenta tak, aby boli špecifické a odlišné medzi sebou.<br>- Vytvorte hierarchický systém pomocou „routing“ alebo kontrolného agenta na určenie, ktorý agent je správny. |

Mnohé z týchto problémov možno efektívnejšie identifikovať s implementovanou pozorovateľnosťou. Trasy a metriky, o ktorých sme hovorili, pomáhajú presne určiť, kde v pracovnom toku agenta sa problémy vyskytujú, čo výrazne zefektívňuje ladenie a optimalizáciu.

## Riadenie nákladov
Tu sú niektoré stratégie na riadenie nákladov pri nasadzovaní AI agentov do produkcie:

**Používanie menších modelov:** Malé jazykové modely (SLMs) môžu dobre fungovať v niektorých scenároch s agentmi a výrazne znížia náklady. Ako už bolo spomenuté, najlepší spôsob, ako pochopiť, ako dobre bude SLM fungovať pre váš prípad použitia, je vybudovať hodnotiaci systém na určenie a porovnanie výkonu oproti väčším modelom. Zvážte použitie SLM pre jednoduchšie úlohy, ako je klasifikácia zámeru alebo extrakcia parametrov, a väčšie modely si nechajte na komplexné uvažovanie.

**Používanie smerovacieho modelu:** Podobnou stratégiou je používať rôznorodé modely a veľkosti. Môžete použiť LLM/SLM alebo bezserverovú funkciu na presmerovanie požiadaviek podľa ich zložitosti na najvhodnejšie modely. To tiež pomôže znížiť náklady a zároveň zabezpečiť výkon pri správnych úlohách. Napríklad presmerujte jednoduché dotazy na menšie, rýchlejšie modely a nákladné veľké modely používajte len na úlohy vyžadujúce komplexné uvažovanie.

**Kešovanie odpovedí:** Identifikovanie bežných požiadaviek a úloh a poskytovanie odpovedí ešte predtým, než prejdú vaším agentným systémom, je dobrý spôsob, ako znížiť objem podobných požiadaviek. Dokonca môžete implementovať tok na zistenie, ako veľmi je požiadavka podobná vašim uloženým požiadavkám s využitím jednoduchších AI modelov. Táto stratégia môže výrazne znížiť náklady pri často kladených otázkach alebo bežných pracovných postupoch.

## Pozrime sa, ako to funguje v praxi

V [ukážkovom notebooku tejto sekcie](./code_samples/10_autogen_evaluation.ipynb) uvidíme príklady toho, ako môžeme použiť nástroje na pozorovateľnosť na monitorovanie a hodnotenie nášho agenta.


### Máte ďalšie otázky o AI agentoch v produkcii?

Pridajte sa na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby ste sa stretli s ďalšími študentmi, zúčastnili sa konzultačných hodín a získali odpovede na svoje otázky o AI agentoch.

## Predchádzajúca lekcia

[Návrhový vzor metakognície](../09-metacognition/README.md)

## Nasledujúca lekcia

[Agentné protokoly](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Upozornenie:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa usilujeme o presnosť, majte prosím na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho originálnom jazyku by sa mal považovať za záväzný zdroj. Pri kritických informáciách sa odporúča profesionálny ľudský preklad. Neberieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->