# Kontextové inženýrství pro AI agenty

[![Kontextové inženýrství](../../../translated_images/cs/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

Porozumění složitosti aplikace, pro kterou vytváříte AI agenta, je důležité pro vytvoření spolehlivého agenta. Potřebujeme vytvářet AI agenty, kteří efektivně spravují informace k řešení složitých potřeb, což přesahuje prompt engineering.

V této lekci se podíváme na to, co je kontextové inženýrství a jaká je jeho role při vytváření AI agentů.

## Úvod

Tato lekce pokryje:

• **Co je kontextové inženýrství** a proč se liší od prompt engineering.

• **Strategie pro efektivní kontextové inženýrství**, včetně toho, jak psát, vybírat, komprimovat a izolovat informace.

• **Běžné chyby v kontextu**, které mohou vašeho AI agenta vyvést z cesty, a jak je opravit.

## Výukové cíle

Po dokončení této lekce budete rozumět tomu, jak:

• **Definovat kontextové inženýrství** a rozlišovat ho od prompt engineering.

• **Identifikovat klíčové komponenty kontextu** v aplikacích s velkými jazykovými modely (LLM).

• **Používat strategie pro psaní, výběr, komprimaci a izolaci kontextu** ke zlepšení výkonu agenta.

• **Rozpoznat běžné chyby v kontextu** jako je otrava, rozptýlení, zmatek a konflikt a implementovat techniky zmírnění.

## Co je kontextové inženýrství?

Pro AI agenty je kontext tím, co řídí plánování jejich kroků. Kontextové inženýrství je praxe zajištění správných informací, aby AI agent mohl dokončit další krok úkolu. Kontextové okno má omezenou velikost, takže jako tvůrci agentů musíme vytvářet systémy a procesy pro přidávání, odebírání a zhušťování informací v kontextovém okně.

### Prompt Engineering vs Kontextové inženýrství

Prompt engineering se zaměřuje na jednu sadu statických instrukcí, které efektivně vedou AI agenty sadou pravidel. Kontextové inženýrství je správa dynamické sady informací, včetně počátečního promptu, aby AI agent měl potřebné údaje v průběhu času. Hlavní myšlenkou kontextového inženýrství je učinit tento proces opakovatelným a spolehlivým.

### Typy kontextu

[![Typy kontextu](../../../translated_images/cs/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Je důležité pamatovat, že kontext není jen jedna věc. Informace, které AI agent potřebuje, mohou pocházet z různých zdrojů a na nás je zajistit, aby agent k těmto zdrojům měl přístup:

Typy kontextu, které může AI agent potřebovat spravovat, zahrnují:

• **Instrukce:** Jsou to jako "pravidla" agenta – prompty, systémové zprávy, few-shot příklady (ukazující, jak něco dělat), a popisy nástrojů, které může používat. Zde se prolínají zaměření prompt engineering a kontextového inženýrství.

• **Znalosti:** Zahrnují fakta, informace získané z databází nebo dlouhodobé vzpomínky, které agent nasbíral. To zahrnuje integraci systému Retrieval Augmented Generation (RAG), pokud agent potřebuje přístup k různým úložištím znalostí a databázím.

• **Nástroje:** Definice externích funkcí, API a MCP serverů, které agent může volat, spolu s výsledky (zpětnou vazbou), které od nich dostává.

• **Historie konverzace:** Pokračující dialog s uživatelem. Jak čas plyne, tyto rozhovory jsou delší a složitější, což zabírá místo v kontextovém okně.

• **Preference uživatele:** Informace o uživatelových preferencích získané v průběhu času. Mohou být uloženy a použity při důležitých rozhodnutích, aby pomohly uživateli.

## Strategie pro efektivní kontextové inženýrství

### Plánovací strategie

[![Nejlepší praktiky kontextového inženýrství](../../../translated_images/cs/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Dobré kontextové inženýrství začíná dobrým plánováním. Zde je přístup, který vám pomůže začít přemýšlet o tom, jak aplikovat koncept kontextového inženýrství:

1. **Definujte jasné výsledky** - výsledky úkolů, které budou AI agentům zadány, by měly být jasně definovány. Odpovězte na otázku – „Jak bude svět vypadat, až AI agent dokončí svůj úkol?“ Jinými slovy, jaká změna, informace nebo reakce by měl uživatel mít po interakci s AI agentem.
2. **Namapujte kontext** - Jakmile máte definované výsledky AI agenta, musíte odpovědět na otázku „Jaké informace agent potřebuje k dokončení tohoto úkolu?“. Tímto způsobem můžete začít mapovat kontext a kde lze informace nalézt.
3. **Vytvořte kontextové pipeliny** - Nyní, když víte, kde jsou informace, musíte odpovědět na otázku „Jak agent tyto informace získá?“. To lze provést různými způsoby, včetně RAG, použití MCP serverů a dalších nástrojů.

### Praktické strategie

Plánování je důležité, ale jakmile začnou informace proudit do kontextového okna našeho agenta, potřebujeme praktické strategie, jak je spravovat:

#### Správa kontextu

Některé informace budou do kontextového okna přidávány automaticky, ale kontextové inženýrství znamená převzít aktivnější roli s těmito informacemi, což lze dělat pomocí několika strategií:

 1. **Poznámkový blok agenta**
 Umožňuje AI agentovi dělat poznámky o relevantních informacích o aktuálních úkolech a interakcích s uživatelem během jedné relace. Mělo by to existovat mimo kontextové okno, v souboru nebo objektu za běhu, který může agent později během této relace vyhledat podle potřeby.

 2. **Vzpomínky**
 Poznámkové bloky jsou dobré pro správu informací mimo kontextové okno jedné relace. Vzpomínky umožňují agentům ukládat a vybavovat si relevantní informace napříč více relacemi. Mohou zahrnovat souhrny, preference uživatele a zpětnou vazbu pro budoucí zlepšení.

 3. **Kompresí kontextu**
  Jak kontextové okno roste a blíží se svému limitu, lze použít techniky jako shrnutí a zkracování. To znamená buď udržování jen nejrelevantnějších informací, nebo odstraňování starších zpráv.
  
 4. **Systémy s více agenty**
  Vývoj systémů s více agenty je formou kontextového inženýrství, protože každý agent má své vlastní kontextové okno. Jak je tento kontext sdílen a předáván mezi agenty, je další věc, kterou je potřeba naplánovat při tvorbě těchto systémů.
  
 5. **Pískoviště (sandbox) prostředí**
  Pokud agent potřebuje spustit nějaký kód nebo zpracovat velké množství informací v dokumentu, může zpracování výsledků vyžadovat hodně tokenů. Místo toho, aby byly všechny tyto informace uloženy v kontextovém okně, může agent použít sandbox prostředí, které umožní spustit kód a pouze číst výsledky a další relevantní informace.
  
 6. **Objekty stavu za běhu (runtime state)**
   To se provádí vytvářením kontejnerů informací pro správu případů, kdy agent potřebuje přístup k určitým informacím. U složitého úkolu to umožní agentovi ukládat výsledky každého dílčího kroku postupně, což umožní, aby byl kontext spojen pouze s daným dílčím úkolem.

#### Kontrola kontextu

Po aplikaci jedné z těchto strategií stojí za to zkontrolovat, co model při dalším volání skutečně dostal. Užitečná otázka při ladění je:

> Nahrál agent příliš mnoho kontextu, špatný kontext, nebo mu chyběl kontext, který potřeboval?

Pro odpověď na tuto otázku nemusíte zaznamenávat surové prompty, výstupy nástrojů nebo obsah vzpomínek. V produkci upřednostňujte malé záznamy inspekce kontextu, které zachycují počty, ID, hashe a štítky politik:

- **Výběr:** Sledujte, kolik kandidátních bloků, nástrojů nebo vzpomínek bylo zvažováno, kolik vybráno a které pravidlo nebo skóre způsobilo vyřazení ostatních.
- **Kompresí:** Zaznamenejte zdrojový rozsah nebo ID stopy, ID shrnutí, odhadovaný počet tokenů před a po kompresi a zda byl surový obsah vynechán z dalšího volání.
- **Izolace:** Poznamenejte, který dílčí úkol běžel v samostatném agentovi, relaci nebo sandboxu, jaké omezené shrnutí bylo vráceno a zda velké výstupy nástrojů zůstaly mimo kontext rodičovského agenta.
- **Vzpomínky a RAG:** Ukládejte ID dokumentů pro vyhledávání, ID vzpomínek, skóre, vybrané ID a stav redakce místo plného získaného textu.
- **Bezpečnost a soukromí:** Upřednostňujte hashe, ID, tokenové koše a štítky politik před citlivým textem promptu, argumenty nástrojů, výsledky nástrojů nebo tělem uživatelských vzpomínek.

Cílem není uchovávat více kontextu. Cílem je ponechat dostatek důkazů, aby vývojář mohl určit, která strategie kontextu byla použita a zda změnila další volání modelu zamýšleným způsobem.

### Příklad kontextového inženýrství

Řekněme, že chceme, aby AI agent **„zarezervoval cestu do Paříže.“**

• Jednoduchý agent používající jen prompt engineering by mohl odpovědět: **„Dobře, kdy byste chtěli jet do Paříže?“**. Zpracoval jen vaši přímou otázku v okamžiku, kdy jste ji položil.

• Agent používající strategie kontextového inženýrství by udělal mnohem víc. Jeho systém by před odpovědí mohl:

  ◦ **Zkontrolovat váš kalendář** pro dostupné termíny (získávání dat v reálném čase).

 ◦ **Vzpomínat na předchozí cestovní preference** (z dlouhodobé paměti) jako preferovaná letecká společnost, rozpočet nebo zda preferujete přímé lety.

 ◦ **Identifikovat dostupné nástroje** pro rezervaci letu a hotelu.

- Pak by mohl přijít příklad odpovědi: „Ahoj [Vaše jméno]! Vidím, že máte volno první týden v říjnu. Mám hledat přímé lety do Paříže s [preferovaná letecká společnost] v rámci vašeho obvyklého rozpočtu [Rozpočet]?“. Tato bohatší, na kontextu založená odpověď demonstruje sílu kontextového inženýrství.

## Běžné chyby v kontextu

### Otrava kontextu

**Co to je:** Když do kontextu vstoupí halucinace (nepravdivá informace generovaná LLM) nebo chyba, která je opakovaně zmiňována, což vede k tomu, že agent sleduje nemožné cíle nebo vytváří nesmyslné strategie.

**Co dělat:** Zavést **validaci kontextu** a **karanténu**. Validujte informace před přidáním do dlouhodobé paměti. Pokud je zjištěna potenciální otrava, začněte nové vlákno kontextu, aby se zabránilo šíření špatných informací.

**Příklad s rezervací cesty:** Váš agent halucinuje **přímý let z malého místního letiště do vzdáleného mezinárodního města**, které ve skutečnosti žádné mezinárodní lety nenabízí. Tento neexistující let se uloží do kontextu. Později, když požádáte o rezervaci, agent se snaží najít letenky na této nemožné trase, což vede k opakovaným chybám.

**Řešení:** Zavést krok, který **validuje existenci letu a trasy pomocí API v reálném čase** _před_ přidáním letové informace do pracovního kontextu agenta. Pokud validace selže, chybná informace je „karanténována“ a dále se nepoužívá.

### Rozptýlení kontextu

**Co to je:** Když se kontext zvětší natolik, že model se příliš zaměří na nahromaděnou historii místo toho, co se naučil během tréninku, což vede k opakujícím se nebo neefektivním činnostem. Modely mohou začít dělat chyby ještě před naplněním kontextového okna.

**Co dělat:** Použít **shrnutí kontextu**. Pravidelně komprimujte nahromaděné informace do kratších shrnutí, která udrží důležité detaily a odstraní nadbytečnou historii. To pomáhá „resetovat“ fokus.

**Příklad s rezervací cesty:** Dlouho diskutujete o různých vysněných cestách včetně podrobného vyprávění o vaší batůžkové cestě před dvěma lety. Když konečně požádáte o **„nalezení levného letu na příští měsíc“**, agent se zasekne ve starých, irelevantních detailech a neustále se ptá na vaše batůžkové vybavení nebo minulá itineráře, přičemž zanedbává váš aktuální požadavek.

**Řešení:** Po určitém počtu kol nebo při příliš velkém růstu kontextu by měl agent **shrnout nejnovější a nejrelevantnější části konverzace** – zaměřující se na vaše aktuální cestovní datum a destinaci – a toto shrnutí použít pro další volání LLM, přičemž méně relevantní historickou chat vyřadí.

### Zmatek v kontextu

**Co to je:** Když nadbytečný kontext, často ve formě příliš mnoha dostupných nástrojů, způsobí, že model generuje špatné odpovědi nebo volá nerelevantní nástroje. Menší modely jsou k tomu zvláště náchylné.

**Co dělat:** Implementujte **správu nástrojů** pomocí technik RAG. Ukládejte popisy nástrojů do vektorové databáze a vybírejte _pouze_ ty nejrelevantnější nástroje pro konkrétní úkol. Výzkumy ukazují, že je vhodné omezit počet nástrojů na méně než 30.

**Příklad s rezervací cesty:** Váš agent má přístup k desítkám nástrojů: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` atd. Zeptáte se: **„Jak se nejlépe pohybovat po Paříži?“** V důsledku velkého množství nástrojů se agent zmateně pokouší volat `book_flight` _uvnitř_ Paříže nebo `rent_car`, i když preferujete veřejnou dopravu, protože popisy nástrojů se mohou překrývat nebo jednoduše nerozpozná nejlepší možnost.

**Řešení:** Použijte **RAG nad popisy nástrojů**. Když se ptáte na pohyb po Paříži, systém dynamicky načte _pouze_ nejrelevantnější nástroje jako `rent_car` nebo `public_transport_info` na základě vašeho dotazu, což LLM předkládá jako cílenou „sadu nástrojů“.

### Konflikt v kontextu

**Co to je:** Když v kontextu existují protichůdné informace, což vede k nesourodému uvažování nebo špatným konečným odpovědím. Často se to stává, když informace přicházejí po částech a předpoklady, které byly zpočátku nesprávné, zůstávají v kontextu.

**Co dělat:** Použijte **prořezávání kontextu** a **přenos informací mimo hlavní kontext**. Prořezávání znamená odstraňování zastaralých nebo konfliktních informací při příchodu nových detailů. Přenos dává modelu samostatný „poznámkový blok“ (scratchpad) pro zpracování informací, aniž by zahltil hlavní kontext.


**Příklad rezervace cestování:** Nejprve svému agentovi řeknete: **„Chci letět v ekonomické třídě.“** Později během konverzace změníte názor a řeknete: **„Vlastně pro tuto cestu pojďme v business třídě.“** Pokud zůstanou obě instrukce v kontextu, agent může obdržet protichůdné výsledky vyhledávání nebo se zmást, kterou preferenci upřednostnit.

**Řešení:** Implementujte **ořezávání kontextu**. Když nová instrukce odporuje té staré, starší instrukce je z kontextu odstraněna nebo explicitně přepsána. Alternativně může agent použít **scratchpad** k vyřešení protichůdných preferencí před rozhodnutím, čímž zajistí, že jeho činnosti bude řídit pouze konečná, konzistentní instrukce.

## Máte další otázky o inženýrství kontextu?

Připojte se k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), abyste se setkali s dalšími studenty, zúčastnili se konzultačních hodin a získali odpovědi na své otázky týkající se AI agentů.
## Předchozí lekce

[Agentic Protocols](../11-agentic-protocols/README.md)

## Další lekce

[Memory for AI Agents](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->