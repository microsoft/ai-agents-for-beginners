[![Víceagentní návrhové vzory](../../../translated_images/cs/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

# Víceagentní návrhové vzory

Jakmile začnete pracovat na projektu, který zahrnuje více agentů, budete muset zvážit víceagentní návrhový vzor. Nicméně nemusí být okamžitě jasné, kdy přejít na více agentů a jaké jsou výhody.

## Úvod

V této lekci se pokusíme odpovědět na následující otázky:

- V jakých scénářích jsou víceagentní systémy použitelné?
- Jaké jsou výhody používání více agentů oproti jedinému agentovi vykonávajícímu více úkolů?
- Jaké jsou stavební bloky pro implementaci víceagentního návrhového vzoru?
- Jak získat přehled o vzájemné interakci mezi více agenty?

## Výukové cíle

Po této lekci byste měli být schopni:

- Identifikovat scénáře, kde jsou víceagentní systémy vhodné
- Rozpoznat výhody používání více agentů oproti jedinému agentovi.
- Pochopit stavební bloky implementace víceagentního návrhového vzoru.

Jaký je širší kontext?

*Více agentů je návrhový vzor, který umožňuje více agentům spolupracovat za účelem dosažení společného cíle*.

Tento vzor je široce využíván v různých oblastech, včetně robotiky, autonomních systémů a distribuovaného výpočtu.

## Scénáře, kde jsou víceagentní systémy vhodné

Jaké scénáře jsou tedy vhodné pro použití více agentů? Odpověď zní, že existuje mnoho situací, kdy je užitečné použít více agentů, zejména v následujících případech:

- **Velké zatížení**: Velké pracovní zátěže lze rozdělit na menší úkoly a přidělit různým agentům, což umožňuje paralelní zpracování a rychlejší dokončení. Příkladem je například rozsáhlý úkol zpracování dat.
- **Komplexní úkoly**: Komplexní úkoly, podobně jako velké zátěže, lze rozdělit na menší podúkoly a přidělit je agentům, z nichž každý se specializuje na konkrétní aspekt úkolu. Příkladem jsou autonomní vozidla, kde různí agenti spravují navigaci, detekci překážek a komunikaci s ostatními vozidly.
- **Rozmanité odbornosti**: Různí agenti mohou mít různorodé odbornosti, což jim umožňuje efektivněji řešit různé aspekty úkolu než jediný agent. Příkladem je oblast zdravotnictví, kde agenti spravují diagnostiku, léčebné plány a monitorování pacienta.

## Výhody používání více agentů oproti jedinému agentovi

Jediný agent by mohl dobře fungovat pro jednoduché úkoly, ale u složitějších úkolů může použití více agentů přinést několik výhod:

- **Specializace**: Každý agent se může specializovat na konkrétní úkol. Nedostatek specializace u jediného agenta znamená, že máte agenta, který může dělat všechno, ale může být zmatený, když čelí složitému úkolu. Může například skončit tím, že dělá úkol, pro který není nejvhodnější.
- **Škálovatelnost**: Je snazší systém škálovat přidáním více agentů než přetěžováním jediného agenta.
- **Odolnost vůči chybám**: Pokud jeden agent selže, ostatní mohou pokračovat v činnosti, což zajišťuje spolehlivost systému.

Uveďme si příklad: rezervujeme uživateli cestu. Jediný agent by musel zvládnout všechny aspekty procesu rezervace, od hledání letů po rezervaci hotelů a půjčení auta. Pro tento případ by agent potřeboval nástroje pro všechny tyto úkoly, což by mohlo vést k složitému a monolitickému systému, který je obtížné udržovat a škálovat. Víceagentní systém by naopak mohl mít různé agenty specializované na vyhledávání letů, rezervaci hotelů a půjčení aut. To by systém udělalo modulárnějším, snáze udržovatelným a škálovatelným.

Porovnejte to s cestovní kanceláří provozovanou jako rodinný podnik versus franšízou. Rodinný podnik by měl jediného agenta, který řeší všechny aspekty rezervace, zatímco franšíza by měla různé agenty pro jednotlivé části procesu rezervace.

## Stavební bloky implementace víceagentního návrhového vzoru

Než můžete implementovat víceagentní návrhový vzor, musíte pochopit stavební bloky, které tento vzor tvoří.

Opět si uvedeme konkrétní příklad rezervace cesty pro uživatele. V tomto případě by stavebními bloky byly:

- **Komunikace agentů**: Agenti pro hledání letů, rezervaci hotelů a půjčení aut musí komunikovat a sdílet informace o preferencích a omezeních uživatele. Musíte rozhodnout o protokolech a metodách této komunikace. Konkrétně to znamená, že agent pro hledání letů musí komunikovat s agentem pro rezervaci hotelů, aby bylo zajištěno, že hotel je rezervován na stejné datum jako let. To znamená, že agenti musejí sdílet informace o cestovních datech uživatele, takže je třeba rozhodnout *kteří agenti sdílí informace a jak je sdílí*.
- **Koordinační mechanismy**: Agenti musí koordinovat své kroky, aby byly splněny preference a omezení uživatele. Například uživatel může preferovat hotel blízko letiště, ale omezením může být, že půjčovna aut je pouze na letišti. To znamená, že agent pro rezervaci hotelů musí koordinovat svou činnost s agentem pro půjčování aut, aby byly splněny preference a omezení uživatele. Musíte tedy rozhodnout *jak agenti koordinují své činnosti*.
- **Architektura agenta**: Agenti musí mít vnitřní strukturu pro rozhodování a učení se z interakcí s uživatelem. Například agent pro hledání letů musí mít vnitřní strukturu na rozhodování o tom, které lety doporučit uživateli. Musíte tedy rozhodnout *jak agenti dělají rozhodnutí a učí se z interakcí s uživatelem*. Příkladem učení agenta může být použití modelu strojového učení agentem pro hledání letů k doporučování letů na základě minulých preferencí uživatele.
- **Viditelnost interakcí více agentů**: Musíte mít přehled o tom, jak více agentů vzájemně interaguje. To znamená, že potřebujete nástroje a techniky pro sledování činností a interakcí agentů. To může být ve formě nástrojů pro logování a monitorování, vizualizačních nástrojů a metrik výkonu.
- **Vzorové struktury více agentů**: Existují různé vzory implementace víceagentních systémů, například centralizované, decentralizované a hybridní architektury. Musíte rozhodnout, který vzor nejlépe vyhovuje vašemu případu použití.
- **Člověk v procesu**: Ve většině případů je ve smyčce lidský uživatel a musíte agenty naučit, kdy požádat o lidský zásah. Může to být například, když uživatel požaduje konkrétní hotel nebo let, který agenti neodporučili, nebo žádost o potvrzení před rezervací letu či hotelu.

## Viditelnost interakcí více agentů

Je důležité mít přehled o tom, jak více agentů vzájemně interaguje. Tento přehled je nezbytný pro ladění, optimalizaci a zajištění celkové efektivity systému. Pro tento účel potřebujete nástroje a techniky pro sledování aktivit a interakcí agentů. Může se jednat o nástroje pro logování a monitorování, vizualizaci a metriky výkonu.

Například při rezervaci cesty pro uživatele byste mohli mít přehledovou obrazovku, která zobrazuje stav jednotlivých agentů, preference a omezení uživatele a vzájemnou interakci agentů. Tato obrazovka by mohla ukazovat cestovní data uživatele, lety doporučené agentem pro lety, hotely doporučené agentem pro hotely a půjčovny aut doporučené agentem pro půjčování aut. To by vám poskytlo jasný pohled na to, jak agenti mezi sebou komunikují a zda jsou preference a omezení uživatele splněny.

Podívejme se nyní detailně na jednotlivé aspekty.

- **Nástroje pro logování a monitorování**: Chcete mít zaznamenán každý krok, který agent provede. Záznam může obsahovat informace o agentovi, který provedl akci, jaká akce to byla, čas provedení a výsledek akce. Tyto informace lze využít pro ladění, optimalizaci a další účely.

- **Vizualizační nástroje**: Pomáhají vám lépe vnímat interakce mezi agenty. Můžete si například představit graf, který ukazuje tok informací mezi agenty. To vám pomůže identifikovat úzká místa, neefektivnosti a další problémy v systému.

- **Výkonnostní metriky**: Pomáhají vám sledovat efektivitu víceagentního systému. Můžete například sledovat dobu dokončení úkolu, počet dokončených úkolů za jednotku času a přesnost doporučení agentů. Tyto informace mohou pomoci odhalit oblasti k vylepšení a systém optimalizovat.

## Víceagentní vzory

Pojďme se podívat na konkrétní vzory, které můžeme použít pro tvorbu víceagentních aplikací. Zde je několik zajímavých vzorů, které stojí za zvážení:

### Skupinový chat

Tento vzor je užitečný, pokud chcete vytvořit skupinovou chatovou aplikaci, kde může více agentů mezi sebou komunikovat. Typické případy použití zahrnují týmovou spolupráci, zákaznickou podporu a sociální sítě.

V tomto vzoru každý agent představuje uživatele ve skupinovém chatu a zprávy jsou mezi agenty předávány pomocí protokolu zpráv. Agenti mohou posílat zprávy do skupinového chatu, přijímat zprávy ze skupinového chatu a reagovat na zprávy od ostatních agentů.

Tento vzor lze implementovat pomocí centralizované architektury, kde všechny zprávy procházejí centrálním serverem, nebo decentralizované architektury, kde si agenti zprávy vyměňují přímo.

![Skupinový chat](../../../translated_images/cs/multi-agent-group-chat.ec10f4cde556babd.webp)

### Předání úkolu

Tento vzor je užitečný, chcete-li vytvořit aplikaci, kde si více agentů může předávat úkoly.

Typické případy použití zahrnují zákaznickou podporu, řízení úkolů a automatizaci pracovních postupů.

V tomto vzoru každý agent představuje úkol nebo krok v pracovním postupu a agenti si mohou předávat úkoly jiným agentům podle předem definovaných pravidel.

![Předání](../../../translated_images/cs/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Spolupracující filtrování

Tento vzor je užitečný, pokud chcete vytvořit aplikaci, kde více agentů spolupracuje na poskytování doporučení uživatelům.

Důvodem, proč chcete, aby více agentů spolupracovalo, je to, že každý agent může mít odlišnou odbornost a může přispívat do procesu doporučování různými způsoby.

Uveďme příklad, kdy uživatel chce doporučení, jakou akcii koupit na burze.

- **Odborník na průmysl**: Jeden agent může být odborník na konkrétní odvětví.
- **Technická analýza**: Další agent může být odborník na technickou analýzu.
- **Fundamentální analýza**: Třetí agent může být odborník na fundamentální analýzu. Spoluprací tito agenti poskytnou uživateli komplexnější doporučení.

![Doporučení](../../../translated_images/cs/multi-agent-filtering.d959cb129dc9f608.webp)

## Scénář: Proces vrácení peněz

Uvažujme scénář, kdy zákazník žádá o vrácení peněz za produkt. Tento proces může zahrnovat celou řadu agentů, ale rozdělíme je na agenty specifické pro tento proces a obecné agenty, které lze použít v jiných procesech.

**Agenti specifickí pro proces vrácení peněz**:

Následující agenti by se mohli podílet na procesu vrácení peněz:

- **Agent zákazníka**: Tento agent představuje zákazníka a je zodpovědný za zahájení procesu vrácení peněz.
- **Agent prodejce**: Tento agent představuje prodejce a je zodpovědný za zpracování žádosti o vrácení peněz.
- **Agent plateb**: Tento agent představuje platební proces a je zodpovědný za vrácení peněz zákazníkovi.
- **Agent pro řešení sporů**: Tento agent představuje proces řešení problémů, které mohou nastat během vrácení peněz.
- **Agent pro dodržování předpisů**: Tento agent dohlíží na to, aby proces vrácení peněz odpovídal pravidlům a politikám.

**Obecní agenti**:

Tito agenti mohou být využiti i v jiných částech vašeho podnikání.

- **Agent dopravy**: Tento agent zajišťuje proces dopravy a je zodpovědný za odeslání produktu zpět prodejci. Tento agent lze použít jak pro proces vrácení peněz, tak i pro běžné doručení produktu při nákupu.
- **Agent zpětné vazby**: Tento agent shromažďuje zpětnou vazbu od zákazníka. Zpětná vazba může být pořizována kdykoli, nejen během procesu vrácení peněz.
- **Agent eskalace**: Tento agent řeší eskalaci problémů na vyšší úroveň podpory. Tento typ agenta lze využít v jakémkoli procesu, kde je potřeba eskalovat problém.
- **Agent notifikace**: Tento agent zajišťuje zasílání oznámení zákazníkovi v různých fázích procesu vrácení peněz.
- **Agent analytiky**: Tento agent analyzuje data související s procesem vrácení peněz.
- **Agent auditu**: Tento agent provádí audit procesu vrácení peněz, aby zajistil správný průběh.
- **Agent reportování**: Tento agent vytváří zprávy o průběhu procesu vrácení peněz.
- **Agent znalostí**: Tento agent udržuje znalostní bázi informací týkajících se procesu vrácení peněz. Může být znalý jak vrácení peněz, tak i dalších částí vašeho podnikání.
- **Agent bezpečnosti**: Tento agent dohlíží na bezpečnost procesu vrácení peněz.
- **Agent kvality**: Tento agent zajišťuje kvalitu procesu vrácení peněz.

Předchozí výčet agentů obsahuje poměrně mnoho agentů jak specifických pro proces vrácení peněz, tak i obecnějších agentů použitelných v jiných částech vašeho podnikání. Doufejme, že vám to poskytuje představu, jak si vybrat agenty pro váš víceagentní systém.

## Zadání

Navrhněte víceagentní systém pro proces zákaznické podpory. Identifikujte agenty zapojené do procesu, jejich role a odpovědnosti a jak spolu interagují. Zvažte jak agenty specifické pro proces zákaznické podpory, tak i obecné agenty použitelné v jiných částech vašeho podnikání.


> Zamyslete se, než si přečtete následující řešení, možná budete potřebovat víc agentů, než si myslíte.

> TIP: Zamyslete se nad různými fázemi procesu zákaznické podpory a také zvažte agenty potřebné pro jakýkoli systém.

## Řešení

[Řešení](./solution/solution.md)

## Kontroly znalostí

### Otázka 1

Který scénář nejlépe odpovídá systému s více agenty?

- [ ] A1: Podpůrný bot odpovídá na běžné dotazy pomocí jedné znalostní databáze a malé sady nástrojů.
- [ ] A2: Pracovní postup vrácení peněz vyžaduje oddělené role pro podvody, platby a dodržování předpisů, každá s vlastními nástroji, a jejich výsledky musí být koordinovány.
- [ ] A3: Stejný jednoduchý požadavek na klasifikaci přichází tisícekrát za hodinu.

### Otázka 2

Kdy je jednotlivý agent obvykle lepší volbou?

- [ ] A1: Úkol lze zvládnout s jednou sadou instrukcí a nástrojů, bez specialistických předání.
- [ ] A2: Agent má přístup k více než jednomu nástroji.
- [ ] A3: Pracovní postup vyžaduje oddělené role s různými oprávněními a nezávislé auditní stopy.

[Řešení kvízu](./solution/solution-quiz.md)

## Shrnutí

V této lekci jsme se podívali na návrhový vzor multi-agent, včetně scénářů, kde jsou multi-agentní systémy použitelné, výhod používání multi-agentů oproti jednomu agentovi, stavebních bloků implementace multi-agentního návrhového vzoru a jak mít přehled o vzájemné interakci několika agentů.

### Máte další otázky ohledně návrhového vzoru Multi-Agent?

Připojte se na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde se můžete setkat s dalšími studenty, navštívit konzultační hodiny a získat odpovědi na své otázky o AI Agentech.

## Další zdroje

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentace Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentní návrhové vzory</a>


## Předchozí lekce

[Plánování designu](../07-planning-design/README.md)

## Následující lekce

[Metakognice u AI agentů](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->