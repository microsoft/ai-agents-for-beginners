# Számítógéphasználati ügynökök (CUA) építése

A számítógéphasználati ügynökök ugyanúgy képesek weboldalakkal interakcióba lépni, mint egy ember: böngészőt nyitnak, megvizsgálják az oldalt, és a látottak alapján a következő legjobb lépést teszik meg. Ebben a leckében egy böngésző-automatizációs ügynököt építesz, amely az Airbnb-t keres meg, strukturált listázási adatokat gyűjt, és azonosítja a legolcsóbb tartózkodást Stockholmban.

A lecke ötvözi a Browser-Use AI-alapú navigációját, a Playwrightot és a Chrome DevTools Protocolt (CDP) a böngésző-vezérléshez, az Azure OpenAI-t látás-alapú értelmezéshez, valamint a Pydanticket strukturált adatkinyeréshez.

## Bevezetés

Ez a lecke az alábbiakat tárgyalja:

- Mikor jobb a számítógéphasználati ügynököt választani, mint kizárólag API-alapú automatizációt
- A Browser-Use, Playwright és CDP kombinációja megbízható böngésző-életciklus-kezelésért
- Dinamikus weboldalakról történő listázási adatok kinyerése Azure OpenAI látás és strukturált Pydantic kimenet segítségével
- Mikor alkalmazzunk ügynök-első, aktor-első vagy hibrid böngésző-automatizációs munkafolyamatot

## Tanulási célok

A lecke elvégzése után tudni fogod, hogyan:

- Konfiguráld a Browser-Use-t Azure OpenAI-val és Playwrighttal
- Építs böngésző-automatizációs munkafolyamatot, amely valós weboldalon navigál és kezeli a dinamikus UI elemeket
- Tipizált eredményeket nyerj ki a látható oldal tartalmából és alakítsd át üzleti logikává
- Válassz az ügynök és aktor minták között a böngészőfeladat kiszámíthatósága alapján

## Kódminta

Ez a lecke egy jegyzetfüzet oktatómunkát tartalmaz:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Chrome munkamenetet indít CDP-n keresztül, az Airbnb-n Stockholm-listázást keres, árakat nyer ki Browser-Use látással, és a legolcsóbb lehetőséget strukturált adatként adja vissza.

## Előfeltételek

- Python 3.12+
- Azure OpenAI telepítés környezetben konfigurálva
- Helyileg telepített Chrome vagy Chromium
- Telepített Playwright függőségek
- Alapszintű ismeret az async Pythonból

## Beállítás

Telepítsd a jegyzetfüzetben használt csomagokat:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Állítsd be a jegyzetfüzet által használt Azure OpenAI környezeti változókat:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opcionális: alapértelmezés szerint a legújabb API verziót használja, ha nincs megadva
AZURE_OPENAI_API_VERSION=...
```

## Architektúra áttekintése

A jegyzetfüzet egy hibrid böngésző-automatizációs munkafolyamatot mutat be:

1. A Chrome CDP-vel indul, így a Playwright és a Browser-Use megoszthatja ugyanazt a böngésző-munkamenetet.
2. A Browser-Use ügynök kezeli a nyílt végű navigációs feladatokat, mint az Airbnb megnyitása, felugró ablakok elvetése és Stockholm keresése.
3. Az aktív oldalt strukturált Pydantic séma segítségével vizsgálja meg, hogy kinyerje a listázás címeit, éjszakánkénti árakat, értékeléseket és URL-eket.
4. Python logika összehasonlítja a kinyert listázásokat és kiemeli a legolcsóbb eredményt.

Ez a megközelítés megőrzi a Browser-Use rugalmas, látásalapú értelmezését, miközben meghatározott böngésző-vezérlést biztosít, amikor szükség van rá.

## Főbb tanulságok és bevált gyakorlatok

### Mikor használjunk ügynököt vagy aktort

| Forgatókönyv | Ügynök használata | Aktor használata |
|----------|-----------|-----------|
| Dinamikus elrendezések | Igen, az AI alkalmazkodni tud az oldalak változásaihoz | Nem, a törékeny szelektorok eltörhetnek |
| Ismert struktúra | Nem, az ügynök lassabb a közvetlen vezérlésnél | Igen, gyors és pontos |
| Elemek megtalálása | Igen, a természetes nyelv jól működik | Nem, pontos szelektorok kellenek |
| Időzítés vezérlés | Nem, kevésbé kiszámítható | Igen, teljes kontroll a várakozás és újrapróbálkozás felett |
| Összetett munkafolyamatok | Igen, kezeli a váratlan UI állapotokat | Nem, explicit elágazásokat igényel |

### Browser-Use bevált gyakorlatok

1. Kezdd ügynökkel felfedezéshez és dinamikus navigációhoz.
2. Válts közvetlen oldalvezérlésre, amikor az interakció kiszámíthatóvá válik.
3. Használj strukturált kimeneti modelleket, hogy a kinyert adatok validáltak és típusbiztosak legyenek.
4. Tegyél be késleltetéseket stratégiailag azok után a lépések után, amelyek látható UI változásokat indítanak el.
5. Készíts képernyőképeket az iteráció során, hogy a hibák könnyebben hibakereshetők legyenek.
6. Számíts arra, hogy a webhelyek változnak, és tervezz tartalék megoldásokat a felugró ablakokra és elrendezés-változásokra.
7. Keverd az ügynök és aktor mintákat, hogy egyszerre kapj rugalmasságot és pontosságot.

### Valós alkalmazások

- Utazásfoglalás és árfigyelés
- E-kereskedelmi árösszehasonlítás és elérhetőség ellenőrzés
- Strukturált adatkinyerés dinamikus webhelyekről
- Látás-alapú UI tesztelés és verifikáció
- Webhelymonitorozás és riasztás
- Intelligens űrlapkitöltés többlépéses folyamatok során

## Valós példa: Microsoft Project Opal

Ebben a leckében egy kis, helyi verzióját építed meg a **számítógéphasználati ügynöknek (CUA)** — egy olyan programnak, amely ugyanúgy vezeti a böngészőt, mint egy ember. A Microsoft ugyanezt az elképzelést viszi be a vállalati szférába a **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)** nevű képességgel a Microsoft 365 Copilot részeként.

A Project Opallal leírsz egy feladatot, és az ügynök a nevedben dolgozik a **számítógéphasználaton keresztül egy biztonságos Windows 365 Cloud PC-n**, a szervezet böngésző-alapú alkalmazásai, oldalai és adatai között működve. Ez **aszinkron módon a háttérben fut**, és bármikor irányíthatod a munkát vagy átveheted az irányítást. Példák feladatokra:

- Biztonsági csoport tagsági kérelmek kezelése
- Audit bizonyítékok gyűjtése és érvényesítése megfelelőségi felülvizsgálatokhoz
- IT incidensek triázsa (jegyzet állapotának frissítése, felelősök hozzárendelése, duplikátumok lezárása)
- Excel-adatok összesítése pénzügyi zárási prezentációba

Az Opal hasznos referencia arra, hogy milyen egy **termelési környezetbe alkalmas, megbízható** számítógéphasználati ügynök — és megerősíti a korábbi leckékben tanultakat:

| Tanult koncepció | Hogyan alkalmazza a Project Opal |
|------------------------|-----------------------------|
| **Ember a hurkon belül** (06. lecke) | Az Opal megáll a bejelentkezési adatok, érzékeny információ vagy kétértelmű utasítások esetén, és soha nem adja meg a jelszavakat vagy küldi el az űrlapokat megerősítés nélkül. Bármikor átveheted az irányítást és visszaadhatod azt a feladat közben. |
| **Megbízható és biztonságos ügynökök** (06. és 18. lecke) | Elkülönített Windows 365 Cloud PC-n fut, alapból csak böngészőhozzáféréssel (egyéb géphasználat tiltva, Intune által érvényesítve), a *te* azonosítóddal fut, így csak az engedélyezett adatokhoz fér hozzá, és minden lépést naplóz auditálhatóság céljából. |
| **Tervezés & metakogníció** (07. és 09. lecke) | Az Opal először megtervezi a feladatot, majd minden lépésnél felügyeli saját értelmezését, és megáll gyanús tevékenység észlelésekor. |
| **Újrafelhasználható képességek / eszközök** (04. lecke) | A **Skills** lehetővé teszi ismétlődő feladatok utasításainak írását (`.md` fájlból importálva vagy Opallal szerkesztve), és azok újrafelhasználását beszélgetések között. |

> **Elérhetőség:** A Project Opal jelenleg elérhető a [Frontier korai hozzáférési programban](https://adoption.microsoft.com/copilot/frontier-program/) Microsoft 365 Copilot előfizetéssel rendelkező felhasználóknak, és az adminisztrátornak el kell végeznie a beállítást. Mivel kísérleti Frontier funkcióról van szó, a képességek idővel változhatnak.

## További források

- [Project Opal (Frontier) használatának kezdete](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)

- [Browser-Use Playwright integrációs sablon](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use színész paraméterek és tartalom kinyerés](https://docs.browser-use.com/customize/actor/all-parameters)
- [Tanfolyam Beállítása](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->