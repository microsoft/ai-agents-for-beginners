# AI Agents in Production: Observability & Evaluation

[![AI agenti v produkcii](../../../translated_images/sk/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Keď sa AI agenti presúvajú z experimentálnych prototypov do reálnych aplikácií, schopnosť porozumieť ich správaniu, sledovať ich výkon a systematicky vyhodnocovať ich výstupy sa stáva dôležitou.

## Learning Goals

Po dokončení tejto lekcie budete vedieť/rozumieť:
- Základným konceptom observability a vyhodnocovania agentov
- Techníkam na zlepšenie výkonu, nákladov a efektívnosti agentov
- Čomu a ako systematicky vyhodnocovať vašich AI agentov
- Ako kontrolovať náklady pri nasadzovaní AI agentov do produkcie
- Ako instrumentovať agentov postavených pomocou Microsoft Agent Framework

Cieľom je vybaviť vás poznatkami, ktoré premenia vaše „čierne skrinky“ agentov na transparentné, spravovateľné a spoľahlivé systémy.

_**Poznámka:** Je dôležité nasadzovať AI agentov, ktorí sú bezpeční a dôveryhodní. Pozrite si aj lekciu [Budovanie dôveryhodných AI agentov](./06-building-trustworthy-agents/README.md)._

## Traces and Spans

Observability nástroje ako [Langfuse](https://langfuse.com/) alebo [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) zvyčajne reprezentujú behy agenta ako traces a spans.

- **Trace** predstavuje kompletnú úlohu agenta od začiatku do konca (napríklad spracovanie užívateľského dopytu).
- **Spans** sú jednotlivé kroky v trace (napríklad volanie jazykového modelu alebo načítanie dát).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez observability môže AI agent pôsobiť ako „čierna skrinka“ — jeho vnútorný stav a uvažovanie sú nepriehľadné, čo sťažuje diagnostiku problémov alebo optimalizáciu výkonu. S observabilitou sa agenti menia na „sklenené krabičky“, ktoré ponúkajú transparentnosť nevyhnutnú na budovanie dôvery a zabezpečenie, že fungujú podľa očakávaní. 

## Prečo je observabilita dôležitá v produkčnom prostredí

Presun AI agentov do produkcie prináša novú sadu výziev a požiadaviek. Observabilita už nie je „príjemný doplnok“, ale kritická schopnosť:

*   **Ladenie a analýza koreňovej príčiny**: Keď agent zlyhá alebo vygeneruje neočakávaný výstup, observability nástroje poskytujú trace potrebné na presné určenie zdroja chyby. To je obzvlášť dôležité v zložitých agentoch, ktoré môžu zahŕňať viaceré volania LLM, interakcie s nástrojmi a podmienenú logiku.
*   **Riadenie latencie a nákladov**: AI agenti často využívajú LLM a iné externé API, ktoré sú účtované za token alebo za volanie. Observabilita umožňuje presné sledovanie týchto volaní a pomáha identifikovať operácie, ktoré sú príliš pomalé alebo drahé. Tím tak môže optimalizovať promptovanie, vybrať efektívnejší model alebo prerobiť pracovné toky tak, aby zvládal prevádzkové náklady a zabezpečil dobrý používateľský zážitok.
*   **Dôvera, bezpečnosť a súlad s predpismi**: V mnohých aplikáciách je dôležité zabezpečiť, aby agenti konali bezpečne a eticky. Observabilita poskytuje auditnú stopu akcií a rozhodnutí agenta. Táto stopa sa dá využiť na detekciu a zmiernenie problémov, ako je prompt injection, generovanie škodlivého obsahu alebo nesprávne zaobchádzanie s osobne identifikovateľnými informáciami (PII). Napríklad môžete prehliadnuť trace, aby ste pochopili, prečo agent poskytol určitú odpoveď alebo použil konkrétny nástroj.
*   **Cykly kontinuálneho zlepšovania**: Observability dáta sú základom iteratívneho vývoja. Monitorovaním výkonu agentov v reálnom svete tímy dokážu identifikovať oblasti na zlepšenie, zhromažďovať dáta na doladenie modelov a overovať dopad zmien. To vytvára spätnú väzbu, kde produkčné poznatky z online vyhodnocovania informujú offline experimentovanie a vylepšovanie, čo vedie k postupnému zlepšovaniu výkonu agenta.

## Kľúčové metriky na sledovanie

Na sledovanie a pochopenie správania agenta by sa mala zaznamenávať škála metrík a signálov. Konkrétne metriky sa môžu líšiť v závislosti od účelu agenta, niektoré sú však univerzálne dôležité.

Tu sú niektoré z najbežnejších metrík, ktoré observability nástroje sledujú:

**Latency:** Ako rýchlo agent odpovedá? Dlhé čakanie negatívne vplýva na používateľský zážitok. Mali by ste merať latenciu pre úlohy a jednotlivé kroky sledovaním runov agenta. Napríklad agent, ktorý potrebuje 20 sekúnd na všetky volania modelu, sa dá zrýchliť použitím rýchlejšieho modelu alebo paralelným spustením volaní modelu.

**Costs:** Aké sú náklady na jeden beh agenta? AI agenti sa spoliehajú na volania LLM účtované za token alebo externé API. Časté používanie nástrojov alebo viaceré promptovania môžu náklady rýchlo zvýšiť. Napríklad ak agent volá LLM päťkrát pre marginálne zlepšenie kvality, musíte zvážiť, či sú náklady odôvodnené, alebo či by ste nemohli znížiť počet volaní alebo použiť lacnejší model. Monitorovanie v reálnom čase tiež pomôže identifikovať neočakávané nárasty (napr. chyby spôsobujúce nadmerné API slučky).

**Request Errors:** Koľko požiadaviek agent zlyhal? To môže zahŕňať chyby API alebo neúspešné volania nástrojov. Aby ste zvýšili odolnosť agenta v produkcii, môžete nasadiť fallbacky alebo opakovania (retries). Napr. ak LLM poskytovateľ A je nedostupný, prepnite na LLM poskytovateľa B ako záložný.

**User Feedback:** Implementovanie priameho hodnotenia používateľmi poskytuje cenné informácie. Môže ísť o explicitné hodnotenia (👍palec hore/👎palec dole, ⭐1-5 hviezdičiek) alebo textové komentáre. Konzistentne negatívna spätná väzba by vás mala upozorniť, pretože je to znak, že agent nefunguje podľa očakávaní.

**Implicit User Feedback:** Správanie používateľov poskytuje nepriamu spätnú väzbu aj bez explicitných hodnotení. Môže ísť o okamžité preformulovanie otázky, opakované dotazy alebo kliknutie na tlačidlo opakovať. Napr. ak vidíte, že používatelia opakovane kladú rovnakú otázku, je to znak, že agent nefunguje podľa očakávaní.

**Accuracy:** Ako často agent generuje správne alebo žiaduce výstupy? Definície presnosti sa líšia (napr. správnosť riešenia, presnosť vyhľadávania informácií, spokojnosť používateľa). Prvým krokom je definovať, ako vyzerá úspech pre vášho agenta. Presnosť môžete sledovať cez automatizované kontroly, skóre vyhodnotenia alebo označenia dokončenia úlohy. Napríklad označovanie trace ako „succeeded“ alebo „failed“.

**Automated Evaluation Metrics:** Môžete tiež nastaviť automatizované vyhodnotenia. Napríklad môžete použiť LLM na skórovanie výstupu agenta, či je užitočný, presný alebo nie. Existuje aj niekoľko open source knižníc, ktoré vám pomôžu skórovať rôzne aspekty agenta. Napr. [RAGAS](https://docs.ragas.io/) pre RAG agentov alebo [LLM Guard](https://llm-guard.com/) na detekciu škodlivého jazyka alebo prompt injection.

V praxi kombinácia týchto metrík poskytuje najlepšie pokrytie zdravia AI agenta. V tomto kapitole [príkladnom notebooku](./code_samples/10-expense_claim-demo.ipynb) vám ukážeme, ako tieto metriky vyzerajú v reálnych príkladoch, ale najprv sa naučíme, ako vyzerá typický pracovný postup vyhodnocovania.

## Instrument your Agent

Aby ste zhromažďovali trace dáta, budete musieť instrumentovať svoj kód. Cieľom je instrumentovať kód agenta tak, aby emitoval traces a metriky, ktoré môže zachytávať, spracúvať a vizualizovať platforma na observabilitu.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) sa etabloval ako priemyselný štandard pre observabilitu LLM. Poskytuje súbor API, SDK a nástrojov na generovanie, zhromažďovanie a export telemetrických dát.

Existuje mnoho instrumentačných knižníc, ktoré zabalujú existujúce agentné frameworky a uľahčujú export OpenTelemetry spanov do observability nástroja. Microsoft Agent Framework sa natívne integruje s OpenTelemetry. Nižšie je príklad instrumentácie MAF agenta:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Vykonávanie agenta sa automaticky sleduje.
    pass
```

V [príkladnom notebooku](./code_samples/10-expense_claim-demo.ipynb) v tejto kapitole vám ukážeme, ako instrumentovať váš MAF agent.

**Manuálne vytváranie spanov:** Hoci instrumentačné knižnice poskytujú dobrý základ, často sú prípady, kde je potrebné podrobnejšie alebo vlastné informácie. Môžete manuálne vytvárať span-y a pridať vlastnú aplikačnú logiku. Dôležité je, že môžu obohatiť automaticky alebo manuálne vytvorené span-y o vlastné atribúty (tiež známe ako tagy alebo metadata). Tieto atribúty môžu obsahovať obchodné špecifické dáta, medzipočty alebo akýkoľvek kontext užitočný pri ladení alebo analýze, napr. `user_id`, `session_id` alebo `model_version`.

Príklad manuálneho vytvárania traces a span-ov pomocou [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent Evaluation

Observabilita nám poskytuje metriky, ale vyhodnocovanie je proces analýzy týchto dát (a vykonávania testov), aby sa určilo, ako dobre AI agent funguje a ako ho možno zlepšiť. Inými slovami, keď už máte trace a metriky, ako ich použijete na posúdenie agenta a prijímanie rozhodnutí?

Pravidelné vyhodnocovanie je dôležité, pretože AI agenti sú často nedeterministickí a môžu sa vyvíjať (prostredníctvom aktualizácií alebo driftu správania modelu) – bez vyhodnocovania by ste nevedeli, či váš „chytrý agent“ skutočne vykonáva svoju úlohu dobre alebo či došlo k regresii.

Existujú dve kategórie vyhodnocovania AI agentov: **online vyhodnocovanie** a **offline vyhodnocovanie**. Obe sú hodnotné a dopĺňajú sa. Zvyčajne začíname offline vyhodnocovaním, pretože je to minimálny potrebný krok pred nasadením agenta.

### Offline vyhodnocovanie

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To zahŕňa hodnotenie agenta v kontrolovanom prostredí, typicky pomocou testovacích datasetov, nie živých používateľských dopytov. Používate kurátorské dataset-y, kde viete, aký je očakávaný výstup alebo správne správanie, a potom spustíte svojho agenta na nich.

Napríklad, ak ste vytvorili agenta na riešenie slovných úloh z matematiky, môžete mať [testovací dataset](https://huggingface.co/datasets/gsm8k) 100 problémov so známymi odpoveďami. Offline vyhodnocovanie sa často vykonáva počas vývoja (a môže byť súčasťou CI/CD pipeline) na kontrolu zlepšení alebo ochranu pred regresiami. Výhodou je, že je to **opakované a môžete získať jasné metriky presnosti, pretože máte ground truth**. Môžete tiež simulovať používateľské dopyty a merať odpovede agenta voči ideálnym odpovediam alebo použiť automatizované metriky, ako je popísané vyššie.

Hlavnou výzvou offline vyhodnocovania je zabezpečiť, aby bol váš testovací dataset komplexný a zostal relevantný – agent sa môže správať dobre na pevnom testovacom sete, ale v produkcii narážať na veľmi odlišné dopyty. Preto by ste testovacie sety mali priebežne aktualizovať o nové hraničné prípady a príklady, ktoré odrážajú reálne scenáre. Užitočná je zmes malých „smoke testov“ a väčších evaluačných setov: malé sety na rýchle kontroly a väčšie na širšie metriky výkonu.

### Online vyhodnocovanie 

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Toto sa týka hodnotenia agenta v živom, reálnom prostredí, teda počas skutočného používania v produkcii. Online vyhodnocovanie zahŕňa sledovanie výkonu agenta na reálnych používateľských interakciách a nepretržitú analýzu výsledkov.

Napríklad môžete sledovať mieru úspešnosti, skóre spokojnosti používateľov alebo iné metriky na živom trafficu. Výhodou online vyhodnocovania je, že **zachytáva veci, ktoré by ste v laboratórnom nastavení nemuseli očakávať** – môžete pozorovať drift modelu v čase (ak účinnosť agenta klesá pri zmene vstupných vzorcov) a zachytiť neočakávané dopyty alebo situácie, ktoré neboli v testovacích dátach. Poskytuje skutočný obraz o tom, ako sa agent správa v teréne.

Online vyhodnocovanie často zahŕňa zhromažďovanie implicitnej a explicitnej spätnej väzby od používateľov, ako bolo diskutované, a prípadne spúšťanie shadow testov alebo A/B testov (kde nová verzia agenta beží paralelne, aby sa porovnala so starou). Výzvou je, že môže byť zložité získať spoľahlivé štítky alebo skóre pre živé interakcie – môžete sa spoliehať na spätnú väzbu používateľov alebo downstream metriky (napr. či používateľ klikol na výsledok).

### Kombinovanie oboch

Online a offline vyhodnocovania sa nevylučujú; sú vysoko komplementárne. Poznatky z online monitoringu (napr. nové typy používateľských dopytov, kde agent nefunguje dobre) sa dajú použiť na rozšírenie a vylepšenie offline testovacích datasetov. Naopak, agenti, ktorí sa dobre správajú na offline testoch, môžu byť s väčšou istotou nasadení a monitorovaní online.

Mnohé tímy zavádzajú cyklus:

_evaluate offline -> deploy -> monitor online -> collect new failure cases -> add to offline dataset -> refine agent -> repeat_.

## Bežné problémy

Pri nasadzovaní AI agentov do produkcie môžete naraziť na rôzne výzvy. Tu sú niektoré bežné problémy a ich možné riešenia:

| **Problém**    | **Možné riešenie**   |
| ------------- | ------------------ |
| AI agent nevykonáva úlohy konzistentne | - Upresnite prompt, ktorý dávate AI agentovi; buďte jasní na cieľoch.<br>- Identifikujte, kde môže pomôcť rozdelenie úloh na podúlohy a ich spracovanie viacerými agentmi. |
| AI agent sa dostáva do nekonečných slučiek  | - Uistite sa, že máte jasné terminačné podmienky, aby agent vedel, kedy proces ukončiť.<br>- Pre zložité úlohy vyžadujúce uvažovanie a plánovanie použite väčší model špecializovaný na rozumové úlohy. |
| Volania nástrojov agenta nefungujú dobre   | - Testujte a validujte výstup nástroja mimo agenta.<br>- Upresnite definované parametre, promptovanie a pomenovanie nástrojov.  |
| Multi-agentný systém nefunguje konzistentne | - Upresnite prompty pre každého agenta, aby boli špecifické a odlíšené od seba.<br>- Vytvorte hierarchický systém pomocou „routing“ alebo kontrolného agenta, ktorý určí, ktorý agent je správny. |

Mnohé z týchto problémov sa dajú efektívnejšie identifikovať, ak máte nasadenú observabilitu. Trace a metriky, o ktorých sme hovorili, pomáhajú presne určiť, kde v pracovnom toku agenta problémy vznikajú, čo výrazne zefektívňuje ladenie a optimalizáciu.

## Riadenie nákladov
Here are some strategies to manage the costs of deploying AI agents to production:

**Using Smaller Models:** Small Language Models (SLMs) can perform well on certain agentic use-cases and will reduce costs significantly. As mentioned earlier, building an evaluation system to determine and compare performance vs larger models is the best way to understand how well an SLM will perform on your use case. Consider using SLMs for simpler tasks like intent classification or parameter extraction, while reserving larger models for complex reasoning.

**Using a Router Model:** A similar strategy is to use a diversity of models and sizes. You can use an LLM/SLM or serverless function to route requests based on complexity to the best fit models. This will also help reduce costs while also ensuring performance on the right tasks. For example, route simple queries to smaller, faster models, and only use expensive large models for complex reasoning tasks.

**Caching Responses:** Identifying common requests and tasks and providing the responses before they go through your agentic system is a good way to reduce the volume of similar requests. You can even implement a flow to identify how similar a request is to your cached requests using more basic AI models. This strategy can significantly reduce costs for frequently asked questions or common workflows.

## Poďme sa pozrieť, ako to funguje v praxi

In the [ukážkový notebook tejto sekcie](./code_samples/10-expense_claim-demo.ipynb), we’ll see examples of how we can use observability tools to monitor and evaluate our agent.


### Máte ďalšie otázky o AI agentoch v produkcii?

Pripojte sa na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) aby ste sa stretli s ďalšími študentmi, zúčastnili sa konzultačných hodín a získali odpovede na svoje otázky o AI agentoch.

## Predchádzajúca lekcia

[Návrhový vzor metakognície](../09-metacognition/README.md)

## Nasledujúca lekcia

[Agentické protokoly](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vylúčenie zodpovednosti:
Tento dokument bol preložený pomocou služby prekladu založenej na AI [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by sa mal považovať za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo mylné výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->