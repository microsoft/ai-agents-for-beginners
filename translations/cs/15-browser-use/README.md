# Tvorba agentů pro používání počítače (CUA)

Agenti pro používání počítače mohou komunikovat s webovými stránkami stejným způsobem jako člověk: otevřou prohlížeč, prozkoumají stránku a provedou další nejlepší akci podle toho, co vidí. V této lekci vytvoříte agenta pro automatizaci prohlížeče, který vyhledá na Airbnb, extrahuje strukturovaná data o nabídkách a identifikuje nejlevnější pobyt ve Stockholmu.

Lekce kombinuje Browser-Use pro navigaci řízenou AI, Playwright a Chrome DevTools Protocol (CDP) pro kontrolu prohlížeče, Azure OpenAI pro zpracování s vizuálním vnímáním a Pydantic pro strukturovanou extrakci.

## Úvod

Tato lekce pokryje:

- Pochopení, kdy jsou agenti pro používání počítače vhodnější než pouze API automatizace
- Kombinaci Browser-Use s Playwright a CDP pro spolehlivou správu životního cyklu prohlížeče
- Použití Azure OpenAI s vizí a strukturovanými výstupy Pydantic pro extrakci dat o nabídkách z dynamických webových stránek
- Rozhodování, kdy použít workflow prohlížeče založené na agentovi, na aktérovi nebo hybridní

## Výukové cíle

Po dokončení této lekce budete umět:

- Nakonfigurovat Browser-Use s Azure OpenAI a Playwright
- Vytvořit workflow automatizace prohlížeče, které prochází reálnou webovou stránku a pracuje s dynamickými UI prvky
- Extrahovat typované výsledky z viditelného obsahu stránky a přeměnit je na další obchodní logiku
- Vybrat mezi vzory agenta a aktéra podle toho, jak předvídatelný je úkol v prohlížeči

## Ukázka kódu

Tato lekce obsahuje jeden sešit s tutoriálem:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Spustí relaci Chrome přes CDP, vyhledá nabídky ve Stockholmu na Airbnb, extrahuje ceny pomocí Browser-Use s vizí a vrátí nejlevnější možnost jako strukturovaná data.

## Předpoklady

- Python 3.12+
- Azure OpenAI nasazení nakonfigurované ve vašem prostředí
- Lokálně nainstalovaný Chrome nebo Chromium
- Nainstalované závislosti Playwright
- Základní znalost asynchronního Pythonu

## Nastavení

Nainstalujte balíčky použité v sešitu:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Nastavte environmentální proměnné Azure OpenAI používané v sešitu:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Volitelné: pokud je vynecháno, použije se nejnovější verze API
AZURE_OPENAI_API_VERSION=...
```

## Přehled architektury

Sešit ukazuje hybridní workflow automatizace prohlížeče:

1. Chrome je spuštěn s povoleným CDP, takže Playwright i Browser-Use sdílejí stejnou relaci prohlížeče.
2. Agent Browser-Use řeší otevřené navigační úkoly jako otevření Airbnb, zavření vyskakovacích oken a vyhledávání Stockholmu.
3. Aktivní stránka je analyzována pomocí strukturovaného Pydantic schématu k extrakci názvů nabídek, cen za noc, hodnocení a URL.
4. Python logika porovná extrahované nabídky a zvýrazní nejlevnější výsledek.

Tento přístup zachovává flexibilní uvažování založené na vizuálním vnímání, v čemž je Browser-Use silný, a zároveň poskytuje deterministickou kontrolu prohlížeče, když ji potřebujete.

## Hlavní poznatky a nejlepší praktiky

### Kdy použít agenta vs aktéra

| Scénář | Použít agenta | Použít aktéra |
|----------|-----------|-----------|
| Dynamické rozložení | Ano, AI se přizpůsobí změnám stránky | Ne, křehké selektory mohou prasknout |
| Známá struktura | Ne, agent je pomalejší než přímá kontrola | Ano, rychlé a přesné |
| Nalezení prvků | Ano, přirozený jazyk funguje dobře | Ne, jsou potřeba přesné selektory |
| Řízení času | Ne, méně předvídatelné | Ano, plná kontrola čekání a opakování |
| Složité workflow | Ano, zvládá neočekávané UI stavy | Ne, vyžaduje explicitní větvení |

### Nejlepší praktiky Browser-Use

1. Začněte s agentem pro průzkum a dynamickou navigaci.
2. Přepněte na přímou kontrolu stránky, když se interakce stane předvídatelnou.
3. Používejte strukturované výstupní modely, aby extrahovaná data byla validována a typově bezpečná.
4. Přidávejte záměrné prodlevy po akcích, které vyvolají viditelné změny UI.
5. Při iteracích zaznamenávejte snímky obrazovky, aby bylo snadnější ladit chyby.
6. Očekávejte změny webových stránek a navrhujte záložní strategie pro vyskakovací okna a posuny rozvržení.
7. Kombinujte vzory agenta a aktéra, abyste získali jak flexibilitu, tak přesnost.

### Bezpečnostní opatření pro browser agenty

Agentům pro prohlížeč, kteří pracují na živých webech, musíte nastavit přísnější hranice než skriptu, který jen volá známé API. Před převedením demonstračního sešitu do reálného workflow definujte pravidla, co agent může vidět, na co kliknout a co odeslat.

1. **Omezte prostředí prohlížeče.** Spouštějte agenta v odděleném profilu prohlížeče nebo sandboxu a omezte jej na domény potřebné pro úkol.
2. **Oddělte pozorování od akce.** Nechte agenta nejdřív hledat, číst a extrahovat data; vyžadujte explicitní krok schválení před odesláním formulářů, zasláním zpráv, rezervacemi, nákupy, mazáním záznamů nebo změnami nastavení účtu.
3. **Nepoužívejte tajné údaje v dotazech a trasách.** Nepokládejte hesla, platební údaje, cookies relací ani osobní údaje do kontextu modelu. Nechte uživatele, aby se autentizoval a vymazal citlivá pole z protokolů.
4. **Považujte obsah stránky za nedůvěryhodný vstup.** Web může obsahovat instrukce určené agentovi, ne uživateli. Agent by měl ignorovat text, který žádá o změnu cíle, zpřístupnění dat, deaktivaci ochrany nebo návštěvu nesouvisejících stránek.
5. **Používejte deterministické kontroly kolem rizikových kroků.** Před tím, než požádáte uživatele o schválení finálního kroku, ověřte aktuální URL, titul stránky, vybraný prvek, cenu, příjemce a shrnutí akce kódem.
6. **Nastavte limity a podmínky zastavení.** Omezte počet akcí, opakování, záložek a minut, které agent může použít. Zastavte, pokud je stav stránky nejasný místo pokračování v klikání.
7. **Zaznamenávejte užitečné důkazy, nikoliv všechno.** Uchovávejte shrnutí akcí, časová razítka, URL, popisy vybraných prvků a odkazy na snímky obrazovky, aby bylo možné chyby zkontrolovat bez ukládání zbytečného citlivého obsahu stránky.

V ukázce Airbnb je bezpečné výchozí nastavení vyhledávat nabídky a extrahovat ceny. Přihlášení, kontaktování hostitele nebo dokončení rezervace by měly být separátní akce schválené uživatelem.

### Aplikace v reálném světě

- Rezervace cest a sledování cen
- Porovnávání cen v e-commerce a kontrola dostupnosti
- Strukturovaná extrakce z dynamických webů
- Testování a ověřování UI s vědomím vidění
- Monitoring webových stránek a upozornění
- Inteligentní vyplňování formulářů v několika krocích

## Příklad z praxe: Microsoft Project Opal

Agent, kterého v této lekci vytvoříte, je malou, lokální verzí **agenta pro používání počítače (CUA)** — programu, který ovládá prohlížeč stejným způsobem jako člověk. Microsoft přináší tento stejný koncept do firem pomocí **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, funkce v Microsoft 365 Copilotu.

S projektem Opal popíšete úkol a agent za vás pracuje pomocí **používání počítače na zabezpečeném Windows 365 Cloud PC**, funguje napříč aplikacemi, stránkami a daty v prohlížeči vaší organizace. Pracuje **asynchronně na pozadí** a můžete práci kdykoliv ovládat nebo převzít kontrolu. Mezi příklady úkolů patří:

- Správa požadavků na členství v bezpečnostní skupině
- Sbírání a ověřování auditních důkazů pro kontrolu souladu
- Řízení IT incidentů (aktualizace stavu ticketu, přidělování vlastníků, zavírání duplicit)
- Sestavování dat z Excelu do finanční závěrky

Opal je užitečnou referencí, jak vypadá **produkční a důvěryhodný** agent pro používání počítače — a podporuje koncepty z předchozích lekcí:

| Koncept v tomto kurzu | Jak to použije Project Opal |
|------------------------|-----------------------------|
| **Člověk ve smyčce** (Lekce 06) | Opal zastaví pro přihlašovací údaje, citlivá data nebo nejasné instrukce a nikdy nezadává hesla ani neodesílá formuláře bez výslovného potvrzení. Můžete *převzít kontrolu* a *vrátit kontrolu* uprostřed úkolu. |
| **Důvěryhodní a zabezpečení agenti** (Lekce 06 a 18) | Běží v izolovaném Windows 365 Cloud PC, je ve výchozím stavu pouze prohlížečový (ostatní přístupy k počítači blokovány, vynucováno Intune), používá *vaši* identitu a přistupuje jen k tomu, na co máte oprávnění, a zaznamenává každou akci pro auditovatelnost. |
| **Plánování a metakognice** (Lekce 07 a 09) | Opal nejprve vygeneruje plán úkolu, pak dohlíží na své vlastní uvažování v každém kroku a zastaví se, pokud detekuje podezřelou aktivitu. |
| **Znovupoužitelné schopnosti / nástroje** (Lekce 04) | **Dovednosti** vám umožňují psát instrukce pro opakované úkoly (importované z `.md` souboru nebo psané pomocí Opalu) a znovu je používat v různých konverzacích. |

> **Dostupnost:** Project Opal je momentálně dostupný uživatelům v rámci [programu raného přístupu Frontier](https://adoption.microsoft.com/copilot/frontier-program/) s předplatným Microsoft 365 Copilot a váš správce musí provést nastavení. Protože jde o experimentální funkci Frontier, schopnosti se mohou postupem času měnit.

## Další zdroje

- [Začínáme s Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Šablona integrace Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parametry Browser-Use aktéra a extrakce obsahu](https://docs.browser-use.com/customize/actor/all-parameters)
- [Nastavení kurzu](../00-course-setup/README.md)

## Předchozí lekce

[Průzkum Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Další lekce

[Nasazení škálovatelných agentů](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->