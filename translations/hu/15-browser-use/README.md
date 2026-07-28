# Számítógép-használati ügynökök (CUA) építése

A számítógép-használati ügynökök ugyanúgy tudnak interakcióba lépni webhelyekkel, mint egy ember: böngészőt nyitnak, megvizsgálják az oldalt, és a látottak alapján a következő legjobb lépést teszik meg. Ebben a leckében egy olyan böngészőautomatizálási ügynököt építesz, amely az Airbnb-n keres kereséseket, strukturált listázási adatokat nyer ki, és azonosítja a legolcsóbb szállást Stockholmban.

A lecke ötvözi a Browser-Use-t az MI-alapú navigációhoz, a Playwrightot és a Chrome DevTools Protokollt (CDP) a böngésző vezérléséhez, az Azure OpenAI-t látásalapú érveléshez, és a Pydantic-ot strukturált kinyeréshez.

## Bevezetés

Ez a lecke lefedi:

- Mikor jobb a számítógép-használati ügynök, mint az API-alapú automatizálás
- A Browser-Use, Playwright és CDP kombinálása megbízható böngésző-életciklus-kezeléshez
- Az Azure OpenAI látás és strukturált Pydantic kimenet használata listázási adatok dinamikus weboldalakról történő kinyeréséhez
- Mikor használjunk ügynököt, színészt vagy hibrid böngészőautomatizálási munkafolyamatot

## Tanulási célok

A lecke elvégzése után tudni fogod, hogyan:

- Állítsd be a Browser-Use-t Azure OpenAI és Playwright integrációval
- Építs böngészőautomatizálási munkafolyamatot, amely egy valódi weboldalon navigál és kezeli a dinamikus felhasználói felületelemeket
- Írj kiírt eredményeket a látható tartalomból és alakítsd át üzleti logikává
- Válassz ügynök vagy színész minták között aszerint, hogy mennyire kiszámítható a böngészőfeladat

## Kódminta

Ez a lecke egy jegyzetfüzet-tutorialt tartalmaz:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Indít egy Chrome munkamenetet CDP-n keresztül, Stockholmra keres az Airbnb-n, árakat nyer Browser-Use látással, és a legolcsóbb lehetőséget adja vissza strukturált adatként.

## Előfeltételek

- Python 3.12+
- Azure OpenAI telepítés környezetben konfigurálva
- Helyileg telepített Chrome vagy Chromium
- Telepített Playwright függőségek
- Alapvető ismeretek aszinkron Pythonról

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
# Opcionális: ha elhagyjuk, az alapértelmezett az legújabb API verzió
AZURE_OPENAI_API_VERSION=...
```

## Architektúra áttekintése

A jegyzetfüzet egy hibrid böngészőautomatizálási munkafolyamatot mutat be:

1. A Chrome CDP-vel indul, hogy a Playwright és a Browser-Use ugyanazt a böngésző-munkamenetet használhassa.
2. Egy Browser-Use ügynök nyitott végű navigációs feladatokat kezel, mint az Airbnb megnyitása, felugró ablakok elutasítása és stockholmi keresés.
3. Az aktív oldalt egy strukturált Pydantic séma segítségével vizsgálja, hogy kinyerje az ingatlancímeket, éjszakánkénti árakat, értékeléseket és URL-eket.
4. A Python logika összehasonlítja a kinyert listázásokat és kiemeli a legolcsóbbat.

Ez a megközelítés megőrzi a Browser-Use rugalmas, látásalapú érvelési képességét, miközben determinisztikus böngészővezérlést biztosít, amikor szükséges.

## Főbb tanulságok és bevált gyakorlatok

### Mikor használjunk ügynököt vagy színészt

| Forgatókönyv | Ügynök használata | Színész használata |
|----------|-----------|-----------|
| Dinamikus elrendezések | Igen, az MI alkalmazkodik az oldalváltozásokhoz | Nem, törékenyek a szelektorok |
| Ismert szerkezet | Nem, az ügynök lassabb, mint a közvetlen vezérlés | Igen, gyors és pontos |
| Elemkeresés | Igen, a természetes nyelv jól működik | Nem, pontos szelektorokat igényel |
| Időzítés szabályozása | Nem, kevésbé kiszámítható | Igen, teljes ellenőrzés a várakozások és ismétlések felett |
| Összetett munkafolyamatok | Igen, kezeli a váratlan UI-állapotokat | Nem, explicit elágazást igényel |

### Browser-Use bevált gyakorlatok

1. Kezdd ügynökkel a felfedezéshez és dinamikus navigációhoz.
2. Válts közvetlen oldalkezelésre, amikor a művelet kiszámíthatóvá válik.
3. Használj strukturált kimeneti modelleket, hogy a kinyert adatok validáltak és típusbiztosak legyenek.
4. Adj szándékos késleltetéseket a látható UI változásokat kiváltó műveletek után.
5. Készíts képernyőképeket iterálás közben, hogy a hibák könnyebben hibakereshetők legyenek.
6. Számíts az oldalak változására, és tervezz visszaesési stratégiákat felugró ablakokra és elrendezés-változásokra.
7. Ötvözd az ügynök és színész mintákat, hogy megkapd a rugalmasságot és a pontosságot.

### Biztonsági keretek a böngészőügynököknek

A böngészőügynökök élő webhelyeken működnek, ezért szorosabb határokra van szükségük, mint egy ismert API-t hívó szkriptnek. Mielőtt egy jegyzetfüzet-demóról valódi munkafolyamatra lépnél, határozd meg a vezérlést arra, hogy mit láthat, kattinthat és küldhet be az ügynök.

1. **Határozd meg a böngészési környezetet.** Fuss az ügynök egy dedikált böngészőprofilon vagy sandboxban, és korlátozd az adott feladathoz szükséges domainekre.
2. **Válaszd külön a megfigyelést és a cselekvést.** Engedd, hogy az ügynök először keressen, olvasson és nyerjen ki adatokat; kérj tőle explicit jóváhagyást, mielőtt űrlapokat küldene, üzenetet tenne, foglalna, vásárolna, törölne rekordokat vagy megváltoztatna fiókbeállításokat.
3. **Tartsd távol a jelszavakat és személyes adatokat a promptokból és nyomkövetésekből.** Ne helyezz jelszavakat, fizetési adatokat, munkamenet sütiket vagy nyers személyes adatokat a modell kontextusába. Hagyd, hogy a felhasználó végezze a hitelesítést, és tüntesse el az érzékeny mezőket a naplókból.
4. **Kezeld az oldal tartalmát megbízhatatlan bemenetként.** Egy webhely tartalmazhat olyan utasításokat, amelyek az ügynöknek szólnak, nem a felhasználónak. Az ügynök hagyja figyelmen kívül az olyan oldal szövegét, amely a cél megváltoztatását, adatok felfedését, védelmi eszközök kikapcsolását vagy irreleváns helyek látogatását kéri.
5. **Használj determinisztikus ellenőrzéseket kockázatos lépések körül.** Ellenőrizd aktuális URL-t, oldal címet, kiválasztott elemet, árat, címzettet és akció összefoglalót kóddal, mielőtt a felhasználó jóváhagyását kéred az utolsó lépéshez.
6. **Állíts be költségvetéseket és leállítási feltételeket.** Határozd meg az agent használható műveleteinek, ismétléseinek, füljeinek és perc időtartamának számát. Állj meg, ha az oldal állapota kétértelmű a további kattintás helyett.
7. **Rögzíts hasznos bizonyítékokat, ne mindent.** Tarts meg akció összefoglalókat, időbélyegeket, URL-eket, kiválasztott elem leírásokat és képernyőkép hivatkozásokat, hogy hibák áttekinthetők legyenek, de ne tárolj felesleges érzékeny oldal tartalmat.

Az Airbnb mintában a biztonságos alapértelmezett a listázások keresése és árak kinyerése. Bejelentkezés, házigazda megkeresése vagy foglalás véglegesítése külön, felhasználó által jóváhagyott lépés legyen.

### Valódi világ alkalmazások

- Utazási foglalás és árfigyelés
- E-kereskedelmi árösszehasonlítás és készletellenőrzés
- Strukturált kinyerés dinamikus webhelyekből
- Látásalapú felhasználói felület tesztelés és ellenőrzés
- Weboldal monitorozás és riasztás
- Intelligens űrlapkitöltés több lépéses folyamatokban

## Valódi világ példa: Microsoft Project Opal

Az ebben a leckében épített ügynök egy kis, helyi változata egy **számítógép-használati ügynöknek (CUA)** – egy olyan programnak, amely a böngészőt úgy vezérli, ahogy egy ember tenné. A Microsoft ezt az ötletet viszi a vállalati szférába a **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)** néven, a Microsoft 365 Copilot szolgáltatás részeként.

A Project Opal segítségével egy feladatot írsz le, és az ügynök a nevedben dolgozik, használva a **számítógép-használatot egy biztonságos Windows 365 Cloud PC-n**, amely a szervezeted böngésző alapú alkalmazásai, webhelyei és adatai között működik. Ez **aszinkron módon fut a háttérben**, és bármikor irányíthatod vagy átveheted a vezérlést. Példák munkákra:

- Biztonsági csoporttagsági kérelmek kezelése
- Audit bizonyítékok gyűjtése és validálása megfelelőséghez
- IT incidensek szűrése (jegyzet állapotának frissítése, tulajdonos kijelölése, duplikátumok lezárása)
- Excel adatok összeállítása pénzügyi záró prezentációba

Az Opal hasznos referencia arra, hogy milyen egy **éles, megbízható** számítógép-használati ügynök — és megerősíti a korábbi leckék fogalmait:

| A tanfolyam fogalma | Hogyan érvényesül a Project Opalban |
|------------------------|-----------------------------|
| **Ember az irányításban (human-in-the-loop)** (06. lecke) | Az Opal megáll bejelentkezéshez, érzékeny adatokhoz vagy kétértelmű utasításokhoz, soha nem viszi be a jelszót vagy nem küld űrlapot jóváhagyás nélkül. Tudsz *Átvenni az irányítást* vagy *Visszaadni az irányítást* menet közben. |
| **Megtartandó és biztonságos ügynökök** (06. és 18. lecke) | Egy izolált Windows 365 Cloud PC-ben fut, alapból csak böngészőhöz fér hozzá (egyéb számítógép-hozzáférés blokkolva, Intune által ellenőrizve), a te identitásoddal dolgozik, így csak jogosult tartalmakhoz fér hozzá, és minden lépést naplóz auditálhatóság céljából. |
| **Tervezés és metakogníció** (07. és 09. lecke) | Az Opal először megtervezi a feladatot, majd minden lépésnél felügyeli a saját érvelését és megáll, ha gyanús tevékenységet észlel. |
| **Újrahasználható képességek/eszközök** (04. lecke) | A **Képességek** (Skills) segítségével ismétlődő feladatokhoz írsz utasításokat (.md fájlból importált vagy Opalban írt), és újrahasználod ezeket beszélgetések között. |

> **Elérhetőség:** A Project Opal jelenleg elérhető a [Frontier korai hozzáférési program](https://adoption.microsoft.com/copilot/frontier-program/) felhasználóinak Microsoft 365 Copilot előfizetéssel, és az adminisztrátornak be kell fejeznie a beállítást. Mivel kísérleti Frontier funkció, a képességek idővel változhatnak.

## További források

- [Kezdj hozzá a Project Opal (Frontier) használatához](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integrációs sablon](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use színész paraméterek és tartalomkivonás](https://docs.browser-use.com/customize/actor/all-parameters)
- [Tanfolyam beállítása](../00-course-setup/README.md)

## Előző lecke

[Microsoft Agent Framework felfedezése](../14-microsoft-agent-framework/README.md)

## Következő lecke

[Méretezhető ügynökök telepítése](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->