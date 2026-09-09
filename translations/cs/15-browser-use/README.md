# Vytváření agentů pro používání počítače (CUA)

Agenti používající počítač mohou komunikovat s webovými stránkami stejným způsobem jako člověk: otevřením prohlížeče, prozkoumáním stránky a provedením nejlepší dostupné akce podle toho, co vidí. V této lekci vytvoříte agenta pro automatizaci prohlížeče, který vyhledá na Airbnb, extrahuje strukturovaná data o nabídkách a identifikuje nejlevnější ubytování ve Stockholmu.

Lekce kombinuje Browser-Use pro navigaci řízenou AI, Playwright a Chrome DevTools Protocol (CDP) pro ovládání prohlížeče, Azure OpenAI pro rozpoznávání s vizí a Pydantic pro strukturovanou extrakci.

## Úvod

Tato lekce pokryje:

- Porozumění, kdy jsou agenti používající počítač vhodnější než automatizace pouze přes API
- Kombinaci Browser-Use s Playwright a CDP pro spolehlivé řízení životního cyklu prohlížeče
- Použití Azure OpenAI s vizí a strukturovaný výstup Pydantic pro extrakci dat nabídek z dynamických webových stránek
- Rozhodování, kdy použít agent-first, actor-first nebo hybridní pracovní postup automatizace prohlížeče

## Cíle učení

Po dokončení této lekce budete umět:

- Nakonfigurovat Browser-Use s Azure OpenAI a Playwright
- Vytvořit pracovní postup automatizace prohlížeče, který naviguje na skutečné webové stránce a pracuje s dynamickými prvky UI
- Extrahovat typované výsledky z viditelného obsahu stránky a převést je do následné obchodní logiky
- Volit mezi vzory agenta a aktora na základě toho, jak předvídatelná je úloha v prohlížeči

## Ukázkový kód

Tato lekce obsahuje jeden tutoriál v notebooku:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Spustí se Chrome přes CDP, vyhledá nabídky Airbnb ve Stockholmu, extrahuje ceny pomocí Browser-Use vision a vrátí nejlevnější možnost jako strukturovaná data.

## Požadavky

- Python 3.12+
- Nasazené Azure OpenAI nakonfigurované ve vašem prostředí
- Místně nainstalovaný Chrome nebo Chromium
- Nainstalované závislosti Playwright
- Základní znalost asynchronního Pythonu

## Nastavení

Nainstalujte balíčky používané v notebooku:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Nastavte proměnné prostředí Azure OpenAI používané notebookem:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Volitelné: pokud není uvedeno, použije se nejnovější verze API
AZURE_OPENAI_API_VERSION=...
```

## Přehled architektury

Notebook demonstruje hybridní pracovní postup automatizace prohlížeče:

1. Chrome se spustí s povoleným CDP, takže Playwright i Browser-Use mohou sdílet stejnou relaci prohlížeče.
2. Agent Browser-Use zvládá otevřené úlohy navigace, jako je otevření Airbnb, zavření vyskakovacích oken a hledání Stockholmu.
3. Aktivní stránka je prozkoumána pomocí strukturovaného schématu Pydantic pro extrakci názvů nabídek, cen za noc, hodnocení a URL.
4. Pythonovská logika porovnává extrahované nabídky a zvýrazní nejlevnější výsledek.

Tento přístup udržuje flexibilní úsudek založený na vidění, ve kterém je Browser-Use dobrý, a zároveň poskytuje deterministické ovládání prohlížeče, když jej potřebujete.

## Klíčové poznatky a nejlepší postupy

### Kdy použít agenta versus aktora

| Scénář | Použít agenta | Použít aktora |
|----------|-----------|-----------|
| Dynamické rozvržení | Ano, AI se přizpůsobí změnám na stránce | Ne, křehké selektory mohou selhat |
| Známá struktura | Ne, agent je pomalejší než přímé ovládání | Ano, rychlé a přesné |
| Nalezení prvků | Ano, přirozený jazyk funguje dobře | Ne, vyžadují se přesné selektory |
| Řízení časování | Ne, méně předvídatelné | Ano, plná kontrola nad čekáním a opakováními |
| Složité pracovní postupy | Ano, zvládá neočekávané stavy UI | Ne, vyžaduje explicitní větvení |

### Nejlepší postupy Browser-Use

1. Začněte s agentem pro průzkum a dynamickou navigaci.
2. Přepněte na přímé ovládání stránky, když je interakce předvídatelná.
3. Používejte strukturované výstupní modely, aby extrahovaná data byla validována a typově bezpečná.
4. Přidávejte záměrné zpoždění po akcích, které vyvolají viditelné změny UI.
5. Zachycujte screenshoty během iterací, aby byly chyby snadněji laditelné.
6. Počítejte s tím, že se webové stránky mění, a navrhujte záložní strategie pro vyskakovací okna a posuny rozvržení.
7. Kombinujte vzory agenta a aktora, abyste získali jak flexibilitu, tak přesnost.

### Bezpečnostní omezení pro browser agenty

Agenti prohlížeče pracují na živých webových stránkách, takže potřebují přísnější hranice než skript, který pouze volá známé API. Před přechodem z demo notebooku na reálný pracovní postup definujte kontroly toho, co agent může vidět, kliknout a odeslat.

1. **Omezte prostředí pro prohlížení.** Spusťte agenta v dedikovaném profilu prohlížeče nebo sandboxu a omezte jej na domény potřebné pro úlohu.
2. **Oddělte pozorování od akce.** Nechte agenta nejprve vyhledávat, číst a extrahovat data; vyžadujte explicitní schvalovací krok před odesláním formulářů, zpráv, rezervací, nákupů, mazání záznamů nebo změnou nastavení účtu.
3. **Neukládejte tajné údaje do promptů a stop.** Neumísťujte hesla, platební údaje, session cookies ani surová osobní data do kontextu modelu. Nechte uživatele provést autentizaci a odstraňovat citlivá data z logů.
4. **Považujte obsah stránky za nedůvěryhodný vstup.** Webová stránka může obsahovat pokyny určené agentovi, nikoli uživateli. Agent by měl ignorovat text na stránce, který ho žádá o změnu cíle, zveřejnění dat, deaktivaci ochrany nebo návštěvu nesouvisejících stránek.
5. **Používejte deterministické kontroly při rizikových krocích.** Ověřte aktuální URL, název stránky, vybranou položku, cenu, příjemce a shrnutí akce v kódu, než požádáte uživatele o schválení finálního kroku.
6. **Nastavte rozpočty a podmínky zastavení.** Omezte počet akcí, pokusů, záložek a minut, které může agent použít. Zastavte, pokud je stav stránky nejasný, místo pokračování v klikání.
7. **Ukládejte užitečné důkazy, nikoli vše.** Uchovávejte shrnutí akcí, časová razítka, URL, popisy vybraných prvků a odkazy na screenshoty, aby bylo možné chyby přezkoumat bez ukládání zbytečného citlivého obsahu.

V ukázce Airbnb je bezpečnou výchozí volbou vyhledávání nabídek a extrakce cen. Přihlášení, kontaktování hostitele nebo dokončení rezervace by mělo být uživatelem schválené samostatné opatření.

### Příklady z reálného světa

- Rezervace cest a sledování cen
- Porovnávání cen v e-commerce a kontrola dostupnosti
- Strukturovaná extrakce z dynamických webových stránek
- Testování a ověřování UI s podporou vidění
- Sledování webových stránek a upozornění
- Inteligentní vyplňování formulářů v rámci vícekrokových procesů

## Příklad z reálného světa: Microsoft Project Opal

Agent, kterého vytvoříte v této lekci, je malá, lokální verze **agenta používajícího počítač (CUA)** — programu, který ovládá prohlížeč stejně jako člověk. Microsoft přináší tento stejný koncept do podnikového prostředí s **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, schopností v Microsoft 365 Copilot.

S Project Opal popíšete úlohu a agent za vás pracuje pomocí **používání počítače na zabezpečeném Windows 365 Cloud PC**, fungujícím přes prohlížeč založené aplikace, stránky a data vaší organizace. Pracuje **asynchronně na pozadí** a můžete jej kdykoli navádět nebo převzít kontrolu. Příklady úkolů zahrnují:

- Správa žádostí o členství v bezpečnostních skupinách
- Shromažďování a ověřování auditních důkazů pro compliance kontroly
- Řešení IT incidentů (aktualizace stavu ticketu, přiřazování vlastníků, uzavírání duplicit)
- Kompilace dat z Excelu do finanční závěrky

Opal je užitečnou referencí toho, jak vypadá **produkční, důvěryhodný** agent používající počítač — a posiluje koncepty z předchozích lekcí:

| Koncept v tomto kurzu | Jak se to uplatňuje v Project Opal |
|------------------------|-----------------------------|
| **Člověk v procesu** (lekce 06) | Opal pozastavuje proces pro přihlašovací údaje, citlivá data nebo nejednoznačné instrukce a nikdy nezadává hesla ani neodesílá formuláře bez explicitního potvrzení. Můžete *Převzít kontrolu* a *Vrátit kontrolu* uprostřed úlohy. |
| **Důvěryhodní a bezpeční agenti** (lekce 06 a 18) | Běží v izolovaném Windows 365 Cloud PC, standardně pouze v prohlížeči (ostatní přístup k počítači blokován, vynucováno přes Intune), používá *vaši* identitu, takže přistupuje jen k tomu, na co máte oprávnění, a loguje každou akci pro audit. |
| **Plánování a metakognice** (lekce 07 a 09) | Opal nejprve generuje plán úlohy, pak dohlíží na vlastní úsudek v každém kroku a pozastavuje, pokud detekuje podezřelou činnost. |
| **Znovupoužitelné schopnosti / nástroje** (lekce 04) | **Dovednosti** umožňují psát instrukce pro opakované úkoly (importované z `.md` souboru nebo vytvořené v Opalu) a opakovaně je používat v konverzacích. |

> **Dostupnost:** Project Opal je aktuálně dostupný uživatelům v [programu včasného přístupu Frontier](https://adoption.microsoft.com/copilot/frontier-program/) s předplatným Microsoft 365 Copilot a administrátor musí provést nastavení. Protože je to experimentální funkce Frontier, schopnosti se mohou časem měnit.

## Kontrola znalostí

Otestujte své porozumění před přechodem na další lekci.

**1. Kdy je agent používající prohlížeč vhodnější než pracovní postup založený pouze na API?**

<details>
<summary>Odpověď</summary>

Použijte agenta s prohlížečem, když úloha závisí na tom, co je viditelné v uživatelském rozhraní webu, stránka neumožňuje potřebné API nebo se stránka mění natolik často, že by pevná logika API nebo selektorů byla křehká. Pokud pro stejný úkol existuje stabilní API, upřednostněte API, protože je obvykle rychlejší, jednodušší na testování a bezpečnější.
</details>

**2. V hybridním pracovním postupu, které části by měl řešit agent a které by měl řídit přímý kód Playwright?**

<details>
<summary>Odpověď</summary>

Nechte agenta řešit otevřené navigační úkoly a dynamické stavy UI, jako je nalezení správné stránky nebo zavření neočekávaných vyskakovacích oken. Přepněte na přímé řízení Playwrightu, když je struktura stránky známá a akce vyžaduje přesnost, opakování, čekání nebo deterministickou validaci.
</details>

**3. Ukázka Airbnb najde nabídku, kterou by uživatel mohl chtít zamluvit. Co by se mělo stát před přihlášením, kontaktováním hostitele nebo dokončením rezervace?**

<details>
<summary>Odpověď</summary>

Pracovní postup by se měl pozastavit a požádat o explicitní souhlas uživatele. Než toto požádá, měl by zobrazit jasné shrnutí vybrané nabídky, aktuální URL, cenu, data a zamýšlenou akci. Vyhledávání a extrakce cen může být autonomní; přístup k účtu, zprávy, nákupy a rezervace by měly být schváleny uživatelem.
</details>

**4. Webová stránka říká agentovi, aby ignoroval původní instrukce, navštívil jiný web a odhalil uložené přihlašovací údaje. Jak by měl agent tento text brát?**

<details>
<summary>Odpověď</summary>

Považujte to za nedůvěryhodný obsah stránky, ne jako pokyny od vývojáře nebo uživatele. Agent by měl zůstat v povolené doméně a rozsahu úkolu, odmítat odhalení tajemství a vyhýbat se sledování textu na stránce, který mění cíl, deaktivuje ochrany nebo ho posílá na nesouvisející stránky.
</details>

**5. Jaké důkazy je užitečné uchovávat, když agent prohlížeče běží, a čemu je třeba se vyhnout?**

<details>
<summary>Odpověď</summary>

Uchovávejte shrnutí akcí, časová razítka, URL, popisy vybraných prvků, výsledky validací a odkazy na screenshoty, aby bylo možné běh zkontrolovat. Vyhněte se ukládání hesel, platebních údajů, session cookies, surových osobních dat nebo celého obsahu stránky, pokud není konkrétní důvod z hlediska uchovávání a soukromí.
</details>

## Další zdroje

- [Začínáme s Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Šablona integrace Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parametry aktora Browser-Use a extrakce obsahu](https://docs.browser-use.com/customize/actor/all-parameters)
- [Nastavení kurzu](../00-course-setup/README.md)

## Předchozí lekce

[Prozkoumání Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Další lekce

[Nasazení škálovatelných agentů](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->