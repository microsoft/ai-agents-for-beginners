<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T20:22:55+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "cs"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.cs.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

# Vzory návrhu pro více agentů

Jakmile začnete pracovat na projektu, který zahrnuje více agentů, budete muset zvážit návrhový vzor pro více agentů. Nicméně nemusí být hned jasné, kdy přejít na více agentů a jaké jsou výhody.

## Úvod

V této lekci se snažíme odpovědět na následující otázky:

- Jaké jsou scénáře, kde jsou více agenti vhodní?
- Jaké jsou výhody používání více agentů oproti jednomu agentovi, který vykonává více úkolů?
- Jaké jsou stavební bloky pro implementaci návrhového vzoru pro více agentů?
- Jak zajistit přehled o tom, jak spolu jednotliví agenti komunikují?

## Cíle učení

Po této lekci byste měli být schopni:

- Identifikovat scénáře, kde jsou více agenti vhodní.
- Rozpoznat výhody používání více agentů oproti jednomu agentovi.
- Pochopit stavební bloky pro implementaci návrhového vzoru pro více agentů.

Jaký je širší kontext?

*Více agentů je návrhový vzor, který umožňuje několika agentům spolupracovat na dosažení společného cíle.*

Tento vzor je široce využíván v různých oblastech, včetně robotiky, autonomních systémů a distribuovaného výpočtu.

## Scénáře, kde jsou více agenti vhodní

Tak jaké scénáře jsou vhodné pro použití více agentů? Odpověď je, že existuje mnoho scénářů, kde je využití více agentů přínosné, zejména v následujících případech:

- **Velké pracovní zátěže**: Velké pracovní zátěže lze rozdělit na menší úkoly a přidělit je různým agentům, což umožňuje paralelní zpracování a rychlejší dokončení. Příkladem může být zpracování velkého množství dat.
- **Komplexní úkoly**: Komplexní úkoly, podobně jako velké pracovní zátěže, lze rozdělit na menší podúkoly a přidělit je různým agentům, z nichž každý se specializuje na konkrétní aspekt úkolu. Příkladem může být autonomní vozidlo, kde různí agenti spravují navigaci, detekci překážek a komunikaci s jinými vozidly.
- **Různorodá odbornost**: Různí agenti mohou mít různorodou odbornost, což jim umožňuje efektivněji zvládat různé aspekty úkolu než jeden agent. Příkladem může být zdravotnictví, kde agenti spravují diagnostiku, léčebné plány a monitorování pacientů.

## Výhody používání více agentů oproti jednomu agentovi

Systém s jedním agentem může dobře fungovat pro jednoduché úkoly, ale pro složitější úkoly může použití více agentů přinést několik výhod:

- **Specializace**: Každý agent se může specializovat na konkrétní úkol. Nedostatek specializace u jednoho agenta znamená, že agent může dělat všechno, ale může být zmatený, když čelí složitému úkolu. Může například vykonat úkol, na který není nejlépe vybaven.
- **Škálovatelnost**: Je snazší škálovat systémy přidáním dalších agentů než přetížením jednoho agenta.
- **Odolnost vůči chybám**: Pokud jeden agent selže, ostatní mohou pokračovat ve fungování, což zajišťuje spolehlivost systému.

Pojďme si to ukázat na příkladu. Představme si, že rezervujeme cestu pro uživatele. Systém s jedním agentem by musel zvládnout všechny aspekty procesu rezervace cesty, od hledání letů po rezervaci hotelů a pronájem aut. Aby toho dosáhl, musel by mít nástroje pro všechny tyto úkoly. To by mohlo vést ke složitému a monolitickému systému, který je obtížné udržovat a škálovat. Systém s více agenty by naopak mohl mít různé agenty specializované na hledání letů, rezervaci hotelů a pronájem aut. To by systém učinilo modulárnějším, snadněji udržovatelným a škálovatelným.

Porovnejte to s cestovní kanceláří provozovanou jako rodinný podnik versus cestovní kanceláří provozovanou jako franšíza. Rodinný podnik by měl jednoho agenta, který by zvládal všechny aspekty procesu rezervace cesty, zatímco franšíza by měla různé agenty, kteří by zvládali různé aspekty procesu rezervace cesty.

## Stavební bloky pro implementaci návrhového vzoru pro více agentů

Než budete moci implementovat návrhový vzor pro více agentů, musíte pochopit stavební bloky, které tento vzor tvoří.

Pojďme si to opět konkretizovat na příkladu rezervace cesty pro uživatele. V tomto případě by stavební bloky zahrnovaly:

- **Komunikace mezi agenty**: Agenti pro hledání letů, rezervaci hotelů a pronájem aut musí komunikovat a sdílet informace o preferencích a omezeních uživatele. Musíte rozhodnout o protokolech a metodách této komunikace. Konkrétně to znamená, že agent pro hledání letů musí komunikovat s agentem pro rezervaci hotelů, aby zajistil, že hotel bude rezervován na stejné termíny jako let. To znamená, že agenti musí sdílet informace o termínech cesty uživatele, což znamená, že musíte rozhodnout *kteří agenti sdílejí informace a jak je sdílejí*.
- **Koordinační mechanismy**: Agenti musí koordinovat své akce, aby zajistili, že budou splněny preference a omezení uživatele. Preference uživatele může být například hotel blízko letiště, zatímco omezením může být, že pronájem aut je dostupný pouze na letišti. To znamená, že agent pro rezervaci hotelů musí koordinovat s agentem pro pronájem aut, aby zajistil, že budou splněny preference a omezení uživatele. To znamená, že musíte rozhodnout *jak agenti koordinují své akce*.
- **Architektura agenta**: Agenti musí mít vnitřní strukturu, která jim umožní rozhodovat a učit se z interakcí s uživatelem. To znamená, že agent pro hledání letů musí mít vnitřní strukturu, která mu umožní rozhodovat o tom, které lety doporučit uživateli. To znamená, že musíte rozhodnout *jak agenti rozhodují a učí se z interakcí s uživatelem*. Příklady toho, jak se agent učí a zlepšuje, mohou být, že agent pro hledání letů může používat model strojového učení k doporučování letů uživateli na základě jeho minulých preferencí.
- **Přehled o interakcích mezi agenty**: Musíte mít přehled o tom, jak spolu jednotliví agenti komunikují. To znamená, že musíte mít nástroje a techniky pro sledování aktivit a interakcí agentů. To může být ve formě nástrojů pro logování a monitorování, vizualizačních nástrojů a metrik výkonu.
- **Vzory pro více agentů**: Existují různé vzory pro implementaci systémů s více agenty, jako jsou centralizované, decentralizované a hybridní architektury. Musíte rozhodnout o vzoru, který nejlépe vyhovuje vašemu případu použití.
- **Člověk v procesu**: Ve většině případů budete mít člověka v procesu a musíte agentům instruovat, kdy požádat o lidský zásah. To může být ve formě uživatele, který požádá o konkrétní hotel nebo let, který agenti nedoporučili, nebo požádá o potvrzení před rezervací letu nebo hotelu.

## Přehled o interakcích mezi agenty

Je důležité mít přehled o tom, jak spolu jednotliví agenti komunikují. Tento přehled je zásadní pro ladění, optimalizaci a zajištění celkové efektivity systému. K dosažení tohoto cíle potřebujete nástroje a techniky pro sledování aktivit a interakcí agentů. To může být ve formě nástrojů pro logování a monitorování, vizualizačních nástrojů a metrik výkonu.

Například v případě rezervace cesty pro uživatele byste mohli mít dashboard, který ukazuje stav každého agenta, preference a omezení uživatele a interakce mezi agenty. Tento dashboard by mohl ukazovat termíny cesty uživatele, lety doporučené agentem pro lety, hotely doporučené agentem pro hotely a auta doporučená agentem pro pronájem aut. To by vám poskytlo jasný přehled o tom, jak spolu agenti komunikují a zda jsou splněny preference a omezení uživatele.

Pojďme se podívat na jednotlivé aspekty podrobněji.

- **Nástroje pro logování a monitorování**: Chcete mít logování pro každou akci provedenou agentem. Záznam v logu může obsahovat informace o agentovi, který akci provedl, provedené akci, čase provedení akce a výsledku akce. Tyto informace lze poté použít pro ladění, optimalizaci a další.
- **Vizualizační nástroje**: Vizualizační nástroje vám mohou pomoci vidět interakce mezi agenty intuitivnějším způsobem. Například můžete mít graf, který ukazuje tok informací mezi agenty. To vám může pomoci identifikovat úzká místa, neefektivnosti a další problémy v systému.
- **Metriky výkonu**: Metriky výkonu vám mohou pomoci sledovat efektivitu systému s více agenty. Například můžete sledovat čas potřebný k dokončení úkolu, počet úkolů dokončených za jednotku času a přesnost doporučení agentů. Tyto informace vám mohou pomoci identifikovat oblasti pro zlepšení a optimalizovat systém.

## Vzory pro více agentů

Pojďme se ponořit do konkrétních vzorů, které můžeme použít k vytvoření aplikací s více agenty. Zde jsou některé zajímavé vzory, které stojí za zvážení:

### Skupinový chat

Tento vzor je užitečný, když chcete vytvořit aplikaci pro skupinový chat, kde mohou spolu komunikovat více agenti. Typické případy použití tohoto vzoru zahrnují týmovou spolupráci, zákaznickou podporu a sociální sítě.

V tomto vzoru každý agent představuje uživatele ve skupinovém chatu a zprávy jsou mezi agenty vyměňovány pomocí komunikačního protokolu. Agenti mohou posílat zprávy do skupinového chatu, přijímat zprávy ze skupinového chatu a reagovat na zprávy od jiných agentů.

Tento vzor lze implementovat pomocí centralizované architektury, kde jsou všechny zprávy směrovány přes centrální server, nebo decentralizované architektury, kde jsou zprávy vyměňovány přímo.

![Skupinový chat](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.cs.png)

### Předání úkolu

Tento vzor je užitečný, když chcete vytvořit aplikaci, kde si mohou agenti předávat úkoly.

Typické případy použití tohoto vzoru zahrnují zákaznickou podporu, správu úkolů a automatizaci pracovních postupů.

V tomto vzoru každý agent představuje úkol nebo krok v pracovním postupu a agenti si mohou předávat úkoly na základě předem definovaných pravidel.

![Předání úkolu](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.cs.png)

### Spolupracující filtrování

Tento vzor je užitečný, když chcete vytvořit aplikaci, kde mohou agenti spolupracovat na doporučování uživatelům.

Proč byste chtěli, aby agenti spolupracovali? Protože každý agent může mít jinou odbornost a může přispět k procesu doporučování různými způsoby.

Pojďme si vzít příklad, kdy uživatel chce doporučení na nejlepší akcii ke koupi na burze.

- **Odborník na odvětví**: Jeden agent může být odborníkem na konkrétní odvětví.
- **Technická analýza**: Další agent může být odborníkem na technickou analýzu.
- **Fundamentální analýza**: A další agent může být odborníkem na fundamentální analýzu. Spoluprací mohou tito agenti poskytnout uživateli komplexnější doporučení.

![Doporučení](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.cs.png)

## Scénář: Proces vrácení peněz

Zvažte scénář, kdy se zákazník snaží získat refundaci za produkt. Může být zapojeno poměrně dost agentů, ale rozdělme je na agenty specifické pro tento proces a obecné agenty, které lze použít v jiných procesech.

**Agenti specifické pro proces vrácení peněz**:

Následující jsou někteří agenti, kteří by mohli být zapojeni do procesu vrácení peněz:

- **Agent zákazníka**: Tento agent představuje zákazníka a je zodpovědný za zahájení procesu vrácení peněz.
- **Agent prodejce**: Tento agent představuje prodejce a je zodpovědný za zpracování refundace.
- **Agent platby**: Tento agent představuje platební proces a je zodpovědný za vrácení platby zákazníkovi.
- **Agent řešení problémů**: Tento agent představuje proces řešení problémů a je zodpovědný za řešení jakýchkoli problémů, které během procesu vrácení peněz vzniknou.
- **Agent pro dodržování předpisů**: Tento agent představuje proces dodržování předpisů a je zodpovědný za zajištění, že proces vrácení peněz splňuje předpisy a politiky.

**Obecní agenti**:

Tito agenti mohou být použiti v jiných částech vašeho podnikání.

- **Agent dopravy**: Tento agent představuje proces dopravy a je zodpovědný za dopravu produktu zpět prodejci. Tento agent může být použit jak pro proces vrácení peněz, tak pro obecnou dopravu produktu například při nákupu.
- **Agent zpětné vazby**: Tento agent představuje proces zpětné vazby a je zodpovědný za sběr zpětné vazby od zákazníka. Zpětná vazba může být získána kdykoli, nejen během procesu vrácení peněz.
- **Agent eskalace**: Tento agent představuje proces eskalace a je zodpovědný za eskalaci problémů na vyšší úroveň podpory. Tento typ agenta můžete použít pro jakýkoli proces, kde je potřeba eskalovat problém.
- **Agent notifikací**: Tento agent představuje proces notifikací a je zodpovědný za zasílání notifikací zákazníkovi v různých fázích procesu vrácení peněz.
- **Agent analytiky**: Tento agent představuje proces analytiky a je zodpovědný za analýzu dat souvisejících s procesem vrácení peněz.
- **Agent auditu**: Tento agent představuje proces auditu a je zodpovědný za audit procesu vrácení peněz, aby bylo zajištěno, že je prováděn správně.
- **Agent reportingu**: Tento agent představuje proces reportingu a je zodpovědný za generování reportů o procesu vrácení peněz.
- **Agent znalostí**: Tento agent představuje proces znalostí a je zodpovědný za udržování znalostní báze informací souvisejících s procesem vrácení peněz. Tento agent může být znalý jak o refundacích, tak o jiných částech vašeho podnikání.
- **Agent bezpečnosti**: Tento agent představuje proces bezpečnosti a je zodpovědný za zajištění bezpečnosti procesu vrácení peněz.
- **Agent kvality**: Tento agent představuje proces kvality a je zodpovědný za zajištění kvality procesu vrácení peněz.

Je zde uvedeno poměrně dost agentů, jak pro specifický proces vrácení peněz, tak pro obecné agenty, které lze použít v jiných částech vašeho podnikání. Doufejme, že vám to poskytne představu o tom, jak rozhodnout, které agenty použít ve vašem systému s více agenty.

## Úkol
Navrhněte systém s více agenty pro proces zákaznické podpory. Identifikujte agenty zapojené do procesu, jejich role a odpovědnosti a způsob, jakým spolu komunikují. Zvažte jak agenty specifické pro proces zákaznické podpory, tak obecné agenty, které lze použít v jiných částech vašeho podnikání.

> Zamyslete se, než si přečtete následující řešení, možná budete potřebovat více agentů, než si myslíte.

> TIP: Přemýšlejte o různých fázích procesu zákaznické podpory a také zvažte agenty potřebné pro jakýkoli systém.

## Řešení

[Řešení](./solution/solution.md)

## Kontrolní otázky

Otázka: Kdy byste měli zvážit použití více agentů?

- [ ] A1: Když máte malou pracovní zátěž a jednoduchý úkol.
- [ ] A2: Když máte velkou pracovní zátěž.
- [ ] A3: Když máte jednoduchý úkol.

[Kvíz k řešení](./solution/solution-quiz.md)

## Shrnutí

V této lekci jsme se podívali na návrhový vzor s více agenty, včetně scénářů, kde je použití více agentů vhodné, výhod používání více agentů oproti jednomu agentovi, základních stavebních bloků implementace návrhového vzoru s více agenty a toho, jak mít přehled o tom, jak spolu jednotliví agenti komunikují.

### Máte další otázky k návrhovému vzoru s více agenty?

Připojte se k [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kde se můžete setkat s dalšími studenty, zúčastnit se konzultačních hodin a získat odpovědi na své otázky ohledně AI agentů.

## Další zdroje

- 

## Předchozí lekce

[Návrh plánování](../07-planning-design/README.md)

## Další lekce

[Metakognice u AI agentů](../09-metacognition/README.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.