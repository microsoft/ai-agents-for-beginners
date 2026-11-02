[![Jak navrhnout dobré AI agenty](../../../translated_images/cs/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Klikněte na obrázek výše pro zhlédnutí videa k této lekci)_
# Principy návrhu AI agentů

## Úvod

Existuje mnoho způsobů, jak přemýšlet o budování AI agentních systémů. Vzhledem k tomu, že nejednoznačnost je vlastnost a ne chyba v návrhu generativní AI, je pro inženýry někdy obtížné vůbec vědět, kde začít. Vytvořili jsme sadu uživatelsky orientovaných principů UX návrhu, které umožňují vývojářům budovat zákaznicky orientované agentní systémy k řešení jejich obchodních potřeb. Tyto návrhové principy nejsou předpisovou architekturou, ale spíše výchozím bodem pro týmy, které definují a vytvářejí zkušenosti agentů.

Obecně by agenti měli:

- Rozšiřovat a škálovat lidské schopnosti (brainstorming, řešení problémů, automatizace atd.)
- Vyplnit znalostní mezery (dohnat mě v oblasti znalostí, překlad atd.)
- Umožňovat a podporovat spolupráci způsoby, jakými jako jednotlivci preferujeme pracovat s ostatními
- Udělat z nás lepší verze sebe samých (např. životní kouč/úkolový mistr, pomáhat nám naučit se regulaci emocí a dovednosti mindfulness, budování odolnosti atd.)

## Co tato lekce pokryje

- Co jsou principy agentního návrhu
- Jaké jsou některé směrnice pro implementaci těchto principů návrhu
- Několik příkladů použití principů návrhu

## Cíle učení

Po dokončení této lekce budete schopni:

1. Vysvětlit, co jsou principy agentního návrhu
2. Vysvětlit směrnice pro použití principů agentního návrhu
3. Pochopit, jak vytvořit agenta pomocí principů agentního návrhu

## Principy agentního návrhu

![Principy agentního návrhu](../../../translated_images/cs/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (prostor)

Toto je prostředí, ve kterém agent operuje. Tyto principy ovlivňují, jak navrhujeme agenty pro zapojení do fyzických a digitálních světů.

- **Spojování, ne kolaps** – pomáhat spojovat lidi s ostatními lidmi, událostmi a akčními znalostmi, aby byla umožněna spolupráce a propojení.
- Agenti pomáhají spojovat události, znalosti a lidi.
- Agenti přibližují lidi k sobě. Nejsou navrženi k nahrazení nebo znehodnocení lidí.
- **Snadno dostupný, ale občas neviditelný** – agent většinou funguje na pozadí a upozorní nás pouze, když je to relevantní a vhodné.
  - Agent je snadno objevitelný a dostupný pro autorizované uživatele na jakémkoli zařízení nebo platformě.
  - Agent podporuje multimodální vstupy a výstupy (zvuk, hlas, text atd.).
  - Agent může plynule přecházet mezi popředím a pozadím; mezi proaktivním a reaktivním podle své schopnosti vnímat potřeby uživatele.
  - Agent může fungovat v neviditelné formě, přičemž jeho proces na pozadí a spolupráce s ostatními agenty jsou uživateli transparentní a ovladatelné.

### Agent (čas)

Toto je způsob, jakým agent funguje v čase. Tyto principy ovlivňují, jak navrhujeme agenty interagující napříč minulostí, přítomností a budoucností.

- **Minulost**: Reflexe historie, která zahrnuje stav i kontext.
  - Agent poskytuje relevantnější výsledky na základě analýzy bohatších historických dat přesahujících pouze událost, lidi nebo stavy.
  - Agent vytváří spojení z minulých událostí a aktivně reflektuje paměť, aby se zapojil do současných situací.
- **Nyní**: Pobízení více než upozorňování.
  - Agent ztělesňuje komplexní přístup k interakci s lidmi. Když nastane událost, agent jde nad rámec statického upozornění nebo jiné statické formality. Agent může zjednodušit postupy nebo dynamicky generovat podněty k upoutání pozornosti uživatele ve správný moment.
  - Agent dodává informace na základě kontextuálního prostředí, sociálních a kulturních změn a upravených podle záměru uživatele.
  - Interakce s agentem může být postupná, vyvíjející se/rostoucí v komplexnosti, aby posilovala uživatele dlouhodobě.
- **Budoucnost**: Přizpůsobování a vývoj.
  - Agent se přizpůsobuje různým zařízením, platformám a modalitám.
  - Agent se přizpůsobuje uživatelskému chování, potřebám přístupnosti a je volně přizpůsobitelný.
  - Agent je formován a vyvíjí se prostřednictvím kontinuální uživatelské interakce.

### Agent (jádro)

Toto jsou klíčové prvky v jádru návrhu agenta.

- **Přijměte nejistotu, ale nastavte důvěru**.
  - Určitá míra nejistoty agenta je očekávaná. Nejistota je klíčovým prvkem návrhu agentů.
  - Důvěra a transparentnost jsou základními vrstvami návrhu agenta.
  - Lidé mají kontrolu nad tím, kdy je agent zapnutý/vypnutý a stav agenta je vždy jasně viditelný.

## Směrnice pro implementaci těchto principů

Když používáte výše uvedené principy návrhu, dodržujte následující směrnice:

1. **Transparentnost**: Informujte uživatele, že je zapojena AI, jak funguje (včetně minulých akcí) a jak dávat zpětnou vazbu a upravovat systém.
2. **Kontrola**: Umožněte uživateli přizpůsobit, upřesnit preference a personalizovat a mít kontrolu nad systémem a jeho atributy (včetně možnosti zapomenutí).
3. **Konzistence**: Usilujte o konzistentní multimodální zážitky napříč zařízeními a koncovými body. Používejte známé prvky UI/UX, kde je to možné (např. ikona mikrofonu pro hlasovou interakci) a minimalizujte kognitivní zatížení zákazníka co nejvíce (např. cílit na stručné odpovědi, vizuální pomůcky a obsah „Zjistit více“).

## Jak navrhnout cestovního agenta pomocí těchto principů a směrnic

Představte si, že navrhujete cestovního agenta, zde je, jak byste mohli přemýšlet o použití principů návrhu a směrnic:

1. **Transparentnost** – Ujistěte uživatele, že cestovní agent je agent s podporou AI. Poskytněte základní instrukce, jak začít (např. uvítací zpráva „Ahoj“, ukázkové dotazy). Jasně to zdokumentujte na stránce produktu. Ukažte seznam dotazů, které uživatel položil v minulosti. Jasně uveďte, jak dát zpětnou vazbu (palec nahoru/dolů, tlačítko Odeslat zpětnou vazbu atd.). Jasně sdělte, zda má agent omezení v používání nebo tématech.
2. **Kontrola** – Ujistěte se, že je jasné, jak může uživatel po vytvoření agenta modifikovat věci jako systémový prompt. Umožněte uživateli zvolit si, jak podrobný agent je, jeho styl psaní a jakákoliv omezení, o čem agent nemá mluvit. Dovolte uživateli zobrazit a odstranit jakékoli související soubory nebo data, dotazy a minulé konverzace.
3. **Konzistence** – Ujistěte se, že ikony pro Sdílení dotazu, přidání souboru nebo fotografie a označení někoho či něčeho jsou standardní a rozpoznatelné. Použijte ikonu kancelářské sponky pro nahrání/sdílení souboru s agentem a ikonu obrázku pro nahrání grafiky.

## Ukázkové kódy

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Máte další otázky ohledně designových vzorů AI agentů?

Připojte se k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde se setkáte s dalšími studenty, zúčastníte se konzultačních hodin a získáte odpovědi na své otázky ohledně AI agentů.

## Další zdroje

- <a href="https://openai.com" target="_blank">Praktiky pro správu agentních AI systémů | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Projekt HAX Toolkit - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Nástrojový balíček odpovědné AI</a>

## Předchozí lekce

[Prozkoumávání agentních rámců](../02-explore-agentic-frameworks/README.md)

## Další lekce

[Vzor návrhu používání nástrojů](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->