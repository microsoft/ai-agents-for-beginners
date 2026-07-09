# Vytváření agentů pro používání počítače (CUA)

Agenti pro používání počítače mohou na webových stránkách komunikovat stejným způsobem jako člověk: otevřením prohlížeče, prohlížením stránky a podniknutím nejvhodnějšího dalšího kroku podle toho, co vidí. V této lekci si vytvoříte agenta pro automatizaci prohlížeče, který prohledá Airbnb, extrahuje strukturovaná data z nabídek a identifikuje nejlevnější pobyt ve Stockholmu.

Lekce kombinuje Browser-Use pro navigaci řízenou umělou inteligencí, Playwright a Chrome DevTools Protocol (CDP) pro ovládání prohlížeče, Azure OpenAI pro vizi a rozumění, a Pydantic pro strukturovanou extrakci.

## Úvod

Tato lekce pokrývá:

- Pochopení, kdy jsou agenti pro používání počítače výhodnější než automatizace jen přes API
- Kombinování Browser-Use s Playwright a CDP pro spolehlivou správu životního cyklu prohlížeče
- Použití Azure OpenAI s podporou vidění a strukturovaným výstupem Pydantic pro extrakci dat z dynamických webových stránek
- Rozhodování, kdy použít workflow zaměřené na agenta, aktora nebo hybridní automatizaci prohlížeče

## Cíle učení

Po dokončení této lekce budete umět:

- Konfigurovat Browser-Use s Azure OpenAI a Playwright
- Vytvořit pracovní postup automatizace prohlížeče, který naviguje skutečnou webovou stránkou a zvládá dynamické uživatelské rozhraní
- Extrahovat typované výsledky z viditelného obsahu stránky a přeměnit je na obchodní logiku
- Vybrat mezi vzory agenta a aktora podle předvídatelnosti úkolu v prohlížeči

## Ukázka kódu

Tato lekce obsahuje jedno interaktivní poznámkový blok:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Spouští relaci Chrome přes CDP, vyhledává nabídky ve Stockholmu na Airbnb, extrahuje ceny pomocí Browser-Use vision a vrací nejlevnější možnost jako strukturovaná data.

## Požadavky

- Python 3.12+
- Azure OpenAI nasazení nakonfigurované ve vašem prostředí
- Lokálně nainstalovaný Chrome nebo Chromium
- Nainstalované závislosti Playwright
- Základní znalost asynchronního Pythonu

## Nastavení

Nainstalujte balíčky používané v poznámkovém bloku:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Nastavte proměnné prostředí Azure OpenAI používané poznámkovým blokem:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Nepovinné: pokud není zadáno, použije se nejnovější verze API
AZURE_OPENAI_API_VERSION=...
```

## Přehled architektury

Poznámkový blok demonstruje hybridní pracovní postup automatizace prohlížeče:

1. Chrome je spuštěn s povoleným CDP, aby Playwright i Browser-Use mohly sdílet stejnou relaci prohlížeče.
2. Agent Browser-Use zvládá otevřené navigační úkoly, jako je otevření Airbnb, zavření vyskakovacích oken a vyhledání Stockholmu.
3. Aktivní stránka je zkontrolována pomocí strukturovaného Pydantic schématu pro extrakci názvů nabídek, nočních cen, hodnocení a URL.
4. Pythonovská logika porovnává extrahované nabídky a zvýrazňuje nejlevnější výsledek.

Tento přístup si zachovává flexibilní, na vidění založené rozumění, kterého je Browser-Use schopen, a zároveň vám dává deterministickou kontrolu nad prohlížečem, když ji potřebujete.

## Klíčová poučení a nejlepší praktiky

### Kdy použít agenta a kdy aktora

| Scénář | Použít agenta | Použít aktora |
|----------|-----------|-----------|
| Dynamické rozvržení | Ano, AI se může přizpůsobit změnám stránky | Ne, náchylné selektory mohou selhat |
| Známá struktura | Ne, agent je pomalejší než přímé ovládání | Ano, rychlé a přesné |
| Hledání prvků | Ano, přirozený jazyk funguje dobře | Ne, jsou potřeba přesné selektory |
| Řízení času | Ne, méně předvídatelné | Ano, plná kontrola nad čekáním a opakováním |
| Komplexní pracovní postupy | Ano, zvládá neočekávané stavy UI | Ne, vyžaduje explicitní větvení |

### Nejlepší praktiky pro Browser-Use

1. Začněte s agentem pro průzkum a dynamickou navigaci.
2. Přepněte na přímou kontrolu stránky, když interakce začne být předvídatelná.
3. Používejte modely se strukturovaným výstupem, aby data byla validována a typově bezpečná.
4. Přidávejte záměrné prodlevy po akcích, které vyvolávají viditelné změny UI.
5. Při iteracích pořizujte screenshoty, aby byly chyby snadněji debugovatelné.
6. Očekávejte, že webové stránky se změní, a navrhujte záložní strategie pro vyskakovací okna a posuny rozvržení.
7. Kombinujte vzory agenta a aktora pro získání jak flexibility, tak přesnosti.

### Aplikace ve skutečném světě

- Rezervace cestování a sledování cen
- Porovnání cen a kontrola dostupnosti v e-commerce
- Strukturovaná extrakce z dynamických webových stránek
- Testování a ověřování UI s podporou vidění
- Monitorování webových stránek a upozornění
- Inteligentní vyplňování formulářů v několika krocích

## Příklad ze skutečného světa: Microsoft Project Opal

Agent, kterého v této lekci vytvoříte, je malou, lokální verzí **agenta pro používání počítače (CUA)** — programu, který ovládá prohlížeč způsobem, jaký dělá člověk. Microsoft přináší tento stejný koncept do podnikové sféry s **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, funkcí v rámci Microsoft 365 Copilot.

S Project Opal popíšete úkol a agent pracuje vaším jménem pomocí **používání počítače na zabezpečeném Windows 365 Cloud PC**, operující napříč aplikacemi, weby a daty vaší organizace založenými na prohlížeči. Pracuje **asynchronně na pozadí**, a vy můžete práci řídit, nebo kdykoliv převzít kontrolu. Příklady úloh zahrnují:

- Řízení žádostí o členství ve skupinách zabezpečení
- Shromažďování a ověřování auditních důkazů pro shodu
- Třídění IT incidentů (aktualizace stavu tiketů, přidělování odpovědných, uzavírání duplicit)
- Sestavování dat v Excelu do finanční prezentace

Opal je užitečným referenčním příkladem, jak by měl vypadat **produkční, důvěryhodný** agent pro používání počítače — a posiluje koncepty z předchozích lekcí:

| Koncept v tomto kurzu | Jak ho aplikuje Project Opal |
|------------------------|-----------------------------|
| **Člověk v cyklu** (Lekce 06) | Opal se zastaví kvůli přihlašovacím údajům, citlivým datům nebo nejasným instrukcím a nikdy nezadává hesla ani neodesílá formuláře bez explicitního potvrzení. Můžete *Převzít kontrolu* a *Vrátit kontrolu* v průběhu úkolu. |
| **Důvěryhodní a zabezpečení agenti** (Lekce 06 & 18) | Běží na izolovaném Windows 365 Cloud PC, je standardně pouze v prohlížeči (ostatní přístupy k počítači zablokovány, zabezpečeno přes Intune), používá *vaši* identitu, takže přistupuje jen k oprávněným datům, a zaznamenává každou akci pro účely auditu. |
| **Plánování a metakognice** (Lekce 07 & 09) | Opal nejdříve vytvoří plán úkolu, poté sám dohlíží na své uvažování v každém kroku a zastaví se při podezřelé aktivitě. |
| **Znovupoužitelné schopnosti / nástroje** (Lekce 04) | **Dovednosti** umožňují psát instrukce pro opakující se úkoly (importované z `.md` souboru nebo vytvořené přímo v Opal) a opakovaně je využívat v různých konverzacích. |

> **Dostupnost:** Project Opal je momentálně dostupný uživatelům v [programu předběžného přístupu Frontier](https://adoption.microsoft.com/copilot/frontier-program/) s předplatným Microsoft 365 Copilot a váš správce musí provést nastavení. Protože jde o experimentální funkci Frontier, schopnosti se mohou časem měnit.

## Další zdroje

- [Začínáme s Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Šablona integrace Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parametry aktora Browser-Use a extrakce obsahu](https://docs.browser-use.com/customize/actor/all-parameters)
- [Nastavení kurzu](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->