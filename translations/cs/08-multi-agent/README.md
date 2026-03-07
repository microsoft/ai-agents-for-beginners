[![Víceagentní návrhové vzory](../../../translated_images/cs/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

# Víceagentní návrhové vzory

Jakmile začnete pracovat na projektu, který zahrnuje více agentů, budete muset zvážit víceagentní návrhový vzor. Není však vždy ihned jasné, kdy přejít na více agentů a jaké jsou výhody.

## Úvod

V této lekci se pokusíme odpovědět na následující otázky:

- Jaké scénáře jsou vhodné pro použití více agentů?
- Jaké jsou výhody použití více agentů oproti pouze jednomu agentovi, který vykonává více úkolů?
- Jaké jsou stavební bloky pro implementaci víceagentního návrhového vzoru?
- Jak získat přehled o tom, jak spolu více agentů vzájemně interaguje?

## Cíle učení

Po této lekci byste měli být schopni:

- Identifikovat scénáře, kde je použití více agentů vhodné
- Rozpoznat výhody použití více agentů oproti jednomu agentovi.
- Porozumět stavebním blokům implementace víceagentního návrhového vzoru.

Jaký je širší kontext?

*Více agentů je návrhový vzor, který umožňuje více agentům spolupracovat na dosažení společného cíle.*

Tento vzor je široce využíván v různých oblastech, včetně robotiky, autonomních systémů a distribuovaného výpočtu.

## Scénáře, kde je použití více agentů vhodné

Jaké scénáře jsou tedy vhodným případem pro použití více agentů? Odpověď je, že existuje mnoho scénářů, kde je výhodné použít více agentů, zejména v těchto případech:

- **Velké zatížení úkoly**: Velké množství úkolů lze rozdělit na menší dílčí úkoly a přiřadit různým agentům, což umožňuje paralelní zpracování a rychlejší dokončení. Příkladem je rozsáhlý úkol zpracování dat.
- **Složité úkoly**: Složité úkoly, podobně jako velké zátěže, mohou být rozděleny na menší podúkoly a přiděleny různým agentům, přičemž každý se specializuje na konkrétní aspekt úkolu. Dobrou ukázkou jsou autonomní vozidla, kde různí agenti spravují navigaci, detekci překážek a komunikaci s ostatními vozidly.
- **Různorodá odbornost**: Různí agenti mohou mít různorodou odbornost, což jim umožňuje efektivněji zvládnout různé aspekty úkolu než jeden agent. Příkladem je oblast zdravotnictví, kde agenti mohou spravovat diagnostiku, léčebné plány a monitorování pacientů.

## Výhody použití více agentů oproti jednomu agentovi

Systém s jedním agentem by mohl fungovat dobře pro jednoduché úkoly, ale u složitějších úkolů může použití více agentů přinést několik výhod:

- **Specializace**: Každý agent může být specializovaný na konkrétní úkol. Nedostatek specializace u jednoho agenta znamená, že agent může dělat vše, ale může mít problém rozhodnout se, co dělat u složitých úkolů. Například může skončit tím, že vykoná úkol, na který není nejlépe vybaven.
- **Škálovatelnost**: Je snazší škálovat systém přidáním dalších agentů než přetěžováním jednoho agenta.
- **Odolnost vůči chybám**: Pokud jeden agent selže, ostatní mohou pokračovat v činnosti, což zajišťuje spolehlivost systému.

Uveďme příklad: rezervace cesty pro uživatele. Systém s jedním agentem by musel řešit všechny aspekty procesu rezervace cesty, od hledání letů po rezervaci hotelů a pronájem aut. Aby toto zvládl jediný agent, musel by mít nástroje pro všechny tyto úkoly. To by mohlo vést ke složitému a monolitickému systému, který je obtížné udržovat a škálovat. Víceagentní systém by naopak mohl mít různé agenty specializované na hledání letů, rezervaci hotelů a pronájem aut. To by systém zpřehlednilo, usnadnilo jeho údržbu a škálování.

Porovnejte to s cestovní kanceláří provozovanou jako rodinný obchod versus cestovní kanceláří ve formě franšízy. Rodinný obchod by měl jednoho agenta řešícího všechny aspekty rezervace, zatímco franšíza by měla různé agenty řešící různé části procesu.

## Stavební bloky implementace víceagentního návrhového vzoru

Než začnete implementovat víceagentní návrhový vzor, musíte pochopit stavební bloky, které tento vzor tvoří.

Pojďme to uvést na konkrétním příkladu rezervace cesty pro uživatele. V tomto případě by stavební bloky zahrnovaly:

- **Komunikace mezi agenty**: Agenti pro hledání letů, rezervaci hotelů a pronájem aut musí komunikovat a sdílet informace o uživatelských preferencích a omezeních. Musíte rozhodnout o protokolech a metodách této komunikace. Konkrétně to znamená, že agent hledající lety musí komunikovat s agentem rezervujícím hotely, aby bylo zajištěno, že hotel je rezervován na stejné datum jako let. To znamená, že agenti musí sdílet informace o cestovních datech uživatele, což vyžaduje rozhodnutí, *kteří agenti si informace sdílejí a jak je sdílejí*.
- **Koordinační mechanismy**: Agenti musí koordinovat své akce, aby byly splněny uživatelské preference a omezení. Uživatelská preference může být například hotel blízko letiště, zatímco omezení může znamenat, že pronájem aut je možný pouze na letišti. To znamená, že agent pro rezervaci hotelu musí koordinovat s agentem pro pronájem aut, aby byly dodrženy preference a omezení uživatele. Musíte tedy rozhodnout, *jak agenti koordinují své akce*.
- **Architektura agenta**: Agenti musí mít vnitřní strukturu pro rozhodování a učení se z interakcí s uživatelem. To znamená, že agent pro hledání letů musí mít strukturu umožňující rozhodovat o tom, které lety doporučit uživateli. Musíte rozhodnout, *jak agenti činí rozhodnutí a učí se z interakcí s uživatelem*. Příkladem může být, že agent pro hledání letů využívá model strojového učení k doporučení letů na základě předchozích preferencí uživatele.
- **Přehled o interakcích více agentů**: Potřebujete mít přehled o tom, jak spolu více agentů interaguje. To znamená, že potřebujete nástroje a techniky pro sledování aktivit a interakcí agentů. Může to být ve formě nástrojů pro logování a monitorování, vizualizačních nástrojů a výkonových metrik.
- **Vzory více agentů**: Existují různé vzory pro implementaci víceagentních systémů, například centralizovaná, decentralizovaná a hybridní architektura. Musíte zvolit vzor, který nejlépe vyhovuje vašemu případu použití.
- **Člověk v procesu**: Ve většině případů bude člověk zapojen a je potřeba agentům říct, kdy mají požádat o lidský zásah. Může jít například o uživatele, který vyžaduje konkrétní hotel nebo let, které agenti nedoporučili, nebo žádost o potvrzení před rezervací letu či hotelu.

## Přehled o interakcích více agentů

Je důležité mít přehled o tom, jak více agentů vzájemně interaguje. Tento přehled je nezbytný pro ladění, optimalizaci a zajištění celkové účinnosti systému. K dosažení toho potřebujete nástroje a techniky pro sledování aktivit a interakcí agentů. Může jít o nástroje pro logování a monitorování, vizualizaci a výkonové metriky.

Například v případě rezervace cesty pro uživatele můžete mít dashboard zobrazující stav každého agenta, uživatelské preference a omezení a interakce mezi agenty. Tento dashboard může ukazovat cestovní data uživatele, lety doporučené agentem pro lety, hotely doporučené agentem pro hotely a pronájem aut doporučený agentem pro pronájem aut. Díky tomu máte jasný přehled o tom, jak agenti spolupracují a zda jsou preference a omezení uživatele splněny.

Podívejme se podrobněji na jednotlivé aspekty.

- **Nástroje pro logování a monitorování**: Chcete zaznamenávat každou akcí, kterou agent provede. Záznam může obsahovat informace o agentovi, který akci provedl, provedené akci, čase provedení a výsledku akce. Tyto informace lze pak použít pro ladění, optimalizaci a další účely.

- **Vizualizační nástroje**: Nástroje pro vizualizaci vám pomohou vidět interakce mezi agenty srozumitelnějším způsobem. Například můžete mít graf znázorňující tok informací mezi agenty. To vám může pomoci identifikovat úzká místa, neefektivnosti a další problémy v systému.

- **Výkonové metriky**: Výkonové metriky vám pomohou sledovat účinnost víceagentního systému. Například můžete sledovat čas potřebný k dokončení úkolu, počet dokončených úkolů za jednotku času či přesnost doporučení poskytovaných agenti. Tyto informace vám pomohou identifikovat oblasti pro zlepšení a optimalizovat systém.

## Vzory více agentů

Pojďme se ponořit do konkrétních vzorů, které můžeme použít k tvorbě víceagentních aplikací. Zde jsou některé zajímavé vzory, které stojí za zvážení:

### Skupinový chat

Tento vzor je užitečný, když chcete vytvořit aplikaci pro skupinový chat, kde mezi sebou může komunikovat více agentů. Typické případy použití zahrnují týmovou spolupráci, zákaznickou podporu a sociální sítě.

V tomto vzoru každý agent reprezentuje uživatele ve skupinovém chatu a zprávy se mezi agenty vyměňují pomocí komunikačního protokolu. Agenti mohou odesílat zprávy do skupiny, přijímat zprávy ze skupiny a odpovídat na zprávy ostatních agentů.

Tento vzor lze implementovat pomocí centralizované architektury, kde všechny zprávy procházejí centrálním serverem, nebo decentralizované architektury, kde se zprávy vyměňují přímo.

![Skupinový chat](../../../translated_images/cs/multi-agent-group-chat.ec10f4cde556babd.webp)

### Předání úkolu

Tento vzor je užitečný, pokud chcete vytvořit aplikaci, kde si více agentů může předávat úkoly.

Typické případy použití tohoto vzoru zahrnují zákaznickou podporu, správu úkolů a automatizaci pracovních postupů.

V tomto vzoru každý agent představuje úkol nebo krok v pracovním postupu a agenti si mohou předávat úkoly na základě předem definovaných pravidel.

![Předání úkolu](../../../translated_images/cs/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Spolupracující filtrování

Tento vzor je vhodný, pokud chcete vytvořit aplikaci, kde může více agentů spolupracovat na doporučeních pro uživatele.

Proč chcete, aby více agentů spolupracovalo? Každý agent může mít jinou odbornost a přispívat do doporučovacího procesu různými způsoby.

Uveďme příklad, kdy uživatel chce doporučení na nejlepší akcii k nákupu na akciovém trhu.

- **Odborník na odvětví**: Jeden agent může být odborníkem na konkrétní odvětví.
- **Technická analýza**: Jiný agent může být odborníkem na technickou analýzu.
- **Fundamentální analýza**: A další agent může být expertem na fundamentální analýzu. Spoluprací mohou tito agenti poskytnout komplexnější doporučení uživateli.

![Doporučení](../../../translated_images/cs/multi-agent-filtering.d959cb129dc9f608.webp)

## Scénář: Proces vrácení peněz

Zvažte scénář, kdy zákazník žádá o vrácení peněz za produkt – do tohoto procesu může být zapojeno mnoho agentů, ale rozdělme je na agenty specifické pro tento proces a obecné agenty, které lze použít i v jiných procesech.

**Agenti specifické pro proces vrácení peněz**:

Někteří agenti, kteří by mohli být zapojeni do procesu vrácení peněz:

- **Agent zákazníka**: Tento agent zastupuje zákazníka a je odpovědný za zahájení procesu vrácení peněz.
- **Agent prodejce**: Tento agent zastupuje prodejce a je zodpovědný za zpracování vrácení peněz.
- **Agent plateb**: Tento agent zastupuje platební proces a má na starosti vrácení peněz zákazníkovi.
- **Agenti řešení**: Tento agent zastupuje proces řešení a je odpovědný za řešení jakýchkoli problémů, které během vrácení nastanou.
- **Agent souladu**: Tento agent zastupuje proces souladu a je odpovědný za zajištění, že proces vrácení odpovídá předpisům a politikám.

**Obecní agenti**:

Tyto agenty lze použít i v jiných částech vašeho podnikání.

- **Agent dopravy**: Tento agent zastupuje proces dopravy a je zodpovědný za zaslání produktu zpět prodejci. Tento agent lze využít jak pro proces vrácení peněz, tak pro obecný proces dopravy produktu například po nákupu.
- **Agent zpětné vazby**: Tento agent se stará o proces sběru zpětné vazby od zákazníka. Zpětnou vazbu lze získávat kdykoli, nejen v průběhu procesu vrácení peněz.
- **Agent eskalace**: Tento agent zodpovídá za eskalaci problémů na vyšší úroveň podpory. Tento typ agenta lze použít v jakémkoli procesu, kde je potřeba eskalovat problém.
- **Agent oznámení**: Tento agent odpovídá za zasílání oznámení zákazníkovi v různých fázích procesu vrácení.
- **Agent analýzy**: Tento agent se stará o analyzování dat souvisejících s procesem vrácení.
- **Agent auditu**: Tento agent audituje proces vrácení, aby zajistil jeho správné provádění.
- **Agent reportingu**: Tento agent zodpovídá za vytváření reportů o procesu vrácení.
- **Agent znalostí**: Tento agent udržuje znalostní bázi informací týkajících se procesu vrácení. Tento agent může být znalý jak o vráceních, tak o dalších částech vašeho podnikání.
- **Agent bezpečnosti**: Tento agent zajišťuje bezpečnost procesu vrácení.
- **Agent kvality**: Tento agent dohlíží na kvalitu procesu vrácení.

V předchozím seznamu je poměrně mnoho agentů, a to jak pro specifický proces vrácení peněz, tak i pro obecné agenty, kteří lze využít v jiných částech vašeho podnikání. Doufejme, že vám to poskytne představu o tom, jak se rozhodovat, které agenty použít ve vašem víceagentním systému.

## Zadání

Navrhněte víceagentní systém pro proces zákaznické podpory. Identifikujte agenty zapojené do procesu, jejich role a odpovědnosti a jak spolu interagují. Zvažte jak agenty specifické pro proces zákaznické podpory, tak obecné agenty, kteří mohou být využiti v jiných částech vašeho podnikání.
> Zamyslete se, než si přečtete následující řešení, možná budete potřebovat více agentů, než si myslíte.

> TIP: Zamyslete se nad různými fázemi procesu zákaznické podpory a také zvažte agenty potřebné pro jakýkoli systém.

## Řešení

[Řešení](./solution/solution.md)

## Kontroly znalostí

Otázka: Kdy byste měli zvážit použití více agentů?

- [ ] A1: Když máte malou pracovní zátěž a jednoduchý úkol.
- [ ] A2: Když máte velkou pracovní zátěž
- [ ] A3: Když máte jednoduchý úkol.

[Řešení kvízu](./solution/solution-quiz.md)

## Shrnutí

V této lekci jsme se zabývali návrhovým vzorem více agentů, včetně scénářů, kde je použití více agentů vhodné, výhod používání více agentů oproti jednomu agentovi, stavebních bloků implementace návrhového vzoru více agentů a jak získat přehled o tom, jak jednotliví agenti vzájemně spolupracují.

### Máte více otázek ohledně návrhového vzoru více agentů?

Připojte se k [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kde se setkáte s dalšími studenty, budete moci navštívit konzultační hodiny a nechat si zodpovědět své otázky ohledně AI agentů.

## Další zdroje

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentace Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentické návrhové vzory</a>


## Předchozí lekce

[Plánování návrhu](../07-planning-design/README.md)

## Další lekce

[Metakognice v AI agentech](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornění**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace je doporučován profesionální lidský překlad. Nezodpovídáme za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->