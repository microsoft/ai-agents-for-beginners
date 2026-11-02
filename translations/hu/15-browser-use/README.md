# Számítógép-használó ügynökök építése (CUA)

A számítógép-használó ügynökök ugyanúgy képesek interakcióba lépni webhelyekkel, mint egy ember: megnyitnak egy böngészőt, megvizsgálják az oldalt, majd a látottak alapján végrehajtanak egy következő legjobb műveletet. Ebben a leckében egy böngészőautomatizáló ügynököt fogsz építeni, amely az Airbnb-n keres keresést, strukturált listázási adatokat von ki, és azonosítja a legolcsóbb szállást Stockholmban.

A lecke kombinálja a Browser-Use AI-vezérelt navigációját, a Playwrightot és a Chrome DevTools Protocol-t (CDP) a böngésző vezérléséhez, az Azure OpenAI-t látásalapú értelmezéshez, és a Pydantic-et strukturált kinyeréshez.

## Bevezetés

Ez a lecke lefedi:

- Megértjük, mikor jobbak a számítógép-használó ügynökök, mint az API-alapú automatizációk
- A Browser-Use kombinációját a Playwrighttal és CDP-vel megbízható böngésző-életciklus-kezelésért
- Azure OpenAI látás és strukturált Pydantic kimenet használatát listázási adatok kinyeréséhez dinamikus weboldalakról
- Döntést, mikor használjunk ügynök-alapú, szereplő-alapú vagy hibrid böngészőautomatizálási munkafolyamatot

## Tanulási célok

A lecke elvégzése után tudni fogod, hogyan:

- Konfiguráld a Browser-Use-t Azure OpenAI és Playwright használatával
- Építs böngészőautomatizálási munkafolyamatot, amely egy valódi weboldalon navigál, és kezeli a dinamikus UI elemeket
- Kinyerd a látható oldal tartalmából a típusos eredményeket, és üzleti logikává alakítsd őket
- Válassz az ügynök- és szereplő minták között aszerint, hogy a böngésző feladat mennyire kiszámítható

## Kódminta

Ez a lecke egy jegyzetfüzet-tananyagot tartalmaz:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Elindít egy Chrome munkamenetet CDP-n keresztül, keres Stockholm listákat az Airbnb-n, Browser-Use látással nyeri ki az árakat, és a legolcsóbb opciót strukturált adatként adja vissza.

## Előfeltételek

- Python 3.12+
- Környezetedben beállított Azure OpenAI telepítés
- Helyileg telepített Chrome vagy Chromium
- Telepített Playwright függőségek
- Alapvető ismeret az aszinkron Python-ról

## Felállítás

Telepítsd a jegyzetfüzetben használt csomagokat:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Állítsd be az Azure OpenAI környezeti változókat, amelyeket a jegyzetfüzet használ:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opcionális: alapértelmezett az adott legújabb API verzió, ha elhagyják
AZURE_OPENAI_API_VERSION=...
```

## Architektúra áttekintése

A jegyzetfüzet egy hibrid böngészőautomatizálási munkafolyamatot mutat be:

1. A Chrome CDP engedélyezésével indul, így a Playwright és a Browser-Use ugyanazt a böngésző munkamenetet használhatja.
2. Egy Browser-Use ügynök kezeli a nyitott végű navigációs feladatokat, például az Airbnb megnyitását, felugró ablakok elvetését, és keresést Stockholmra.
3. Az aktív oldalt egy strukturált Pydantic sémával vizsgálja meg, hogy kinyerje a listázás címeit, éjszakánkénti árakat, értékeléseket és URL-eket.
4. Python logika összehasonlítja a kinyert listázásokat és kiemeli a legolcsóbb találatot.

Ez a megközelítés megőrzi a rugalmas, látáson alapuló értelmezést, amelyben a Browser-Use jó, ugyanakkor meghatározott böngészővezérlést biztosít szükség esetén.

## Fő tanulságok és legjobb gyakorlatok

### Mikor használjunk ügynököt és mikor szereplőt

| Forgatókönyv | Ügynök használata | Szereplő használata |
|----------|-----------|-----------|
| Dinamikus elrendezések | Igen, az MI tud alkalmazkodni az oldal változásaihoz | Nem, a törékeny szelektorok eltörhetnek |
| Ismert szerkezet | Nem, az ügynök lassabb a közvetlen vezérlésnél | Igen, gyors és pontos |
| Elemek megtalálása | Igen, a természetes nyelv jól működik | Nem, pontos szelektorok kellenek |
| Időzítés vezérlése | Nem, kevésbé kiszámítható | Igen, teljes kontroll a várakozások és újrapróbálkozások felett |
| Komplex munkafolyamatok | Igen, kezeli a váratlan UI állapotokat | Nem, explicit elágazásokat igényel |

### Browser-Use legjobb gyakorlatok

1. Kezd az ügynökkel felfedezéshez és dinamikus navigációhoz.
2. Válts közvetlen oldalkezelésre, amikor az interakció kiszámíthatóvá válik.
3. Használj strukturált kimeneti modelleket, hogy a kinyert adatok validáltak és típusbiztosak legyenek.
4. Tegyél késleltetést stratégiailag az olyan műveletek után, amelyek látható UI változásokat indítanak el.
5. Készíts képernyőképeket iterálás közben, hogy a hibák könnyebben debugolhatók legyenek.
6. Számíts arra, hogy a webhelyek változhatnak, és tervezz védelmi stratégiákat a felugró ablakokra és elrendezés-váltásokra.
7. Keverd az ügynök és szereplő mintákat, hogy mind rugalmasságot, mind pontosságot kapj.

### Biztonsági korlátok böngészőügynökökhöz

A böngészőügynökök élő weboldalakon működnek, ezért szigorúbb határok kellenek, mint egy ismert API-t hívó scripttel. Mielőtt a jegyzetfüzet-demóról valós munkafolyamatra állnál, definiáld, mit láthat, mit kattinthat, és mit küldhet be az ügynök.

1. **Határozd meg a böngészési környezetet.** Futtasd az ügynököt dedikált böngészőprofilban vagy homokozóban, és korlátozd a feladat szempontjából szükséges domainekre.
2. **Válaszd szét a megfigyelést az akciótól.** Hagyd az ügynököt keresni, olvasni és adatokat kinyerni először; kérj tőle explicit jóváhagyást, mielőtt űrlapokat küldene be, üzeneteket, utazásokat foglalna, vásárlásokat indítana, rekordokat törölne vagy fiókbeállításokat módosítana.
3. **Tartsd titokban a jelszavakat és érzékeny adatokat a promptokban és naplókban.** Ne helyezz el jelszavakat, fizetési adatokat, munkamenet-sütiket vagy nyers személyes adatokat a modell kontextusában. Engedd, hogy a felhasználó autentikálja magát, és töröld ki az érzékeny mezőket a naplókból.
4. **Kezeld az oldal tartalmát nem megbízható bemenetként.** Egy webhely tartalmazhat olyan utasításokat, amelyek az ügynöknek szólnak, nem a felhasználónak. Az ügynök hagyja figyelmen kívül az olyan oldalszöveget, amely cél megváltoztatására, adatfeltárásra, védelmi intézkedések letiltására vagy nem kapcsolódó oldalak meglátogatására hívja fel.
5. **Használj determinisztikus ellenőrzéseket kockázatos lépések előtt.** Kód segítségével ellenőrizd az aktuális URL-t, oldal címet, kiválasztott elemet, árat, címzettet és művelet összefoglalót, mielőtt a felhasználó jóváhagyását kéred az utolsó lépés előtt.
6. **Állíts be költségvetéseket és leállási feltételeket.** Határozd meg az akciók számát, az újrapróbálkozásokat, a fülhasználatot és az ügynök által használható percek számát. Állítsd le a futást, ha az oldal állapota kétséges, a kattintgatás helyett.
7. **Rögzíts hasznos bizonyítékokat, ne mindent.** Tárold az akciók összefoglalóit, időbélyegeket, URL-eket, kiválasztott elemek leírását és képernyőkép hivatkozásokat, hogy a hibákat vissza lehessen nézni felesleges érzékeny oldaltartalom tárolása nélkül.

Az Airbnb példában az alapértelmezett biztonságos megközelítés a listázások keresése és az árak kinyerése. A bejelentkezés, a házigazda megkeresése vagy a foglalás befejezése külön, a felhasználó által jóváhagyott művelet kell hogy legyen.

### Valós világ alkalmazások

- Utazásfoglalás és árfigyelés
- E-kereskedelmi árösszehasonlítás és elérhetőség ellenőrzés
- Strukturált adatkinyerés dinamikus weboldalakról
- Látásalapú UI tesztelés és ellenőrzés
- Webhelyfigyelés és riasztás
- Intelligens űrlapkitöltés többlépcsős folyamatokban

## Valós példa: Microsoft Project Opal

A lecke során épített ügynök a **számítógép-használó ügynök (CUA)** egy kis, lokális verziója — egy olyan program, amely ugyanúgy vezeti a böngészőt, mint egy ember. A Microsoft ezt az elképzelést hozza be vállalati szinten a **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)** révén, amely egy képesség a Microsoft 365 Copilotban.

A Project Opallal egy feladatot írsz le, és az ügynök a nevedben dolgozik a **számítógép-használaton keresztül egy biztonságos Windows 365 Cloud PC-n**, amely az szervezeted böngészőalapú alkalmazásai, oldalai és adatai között működik. **Aszinkron módon a háttérben** működik, és bármikor irányíthatod vagy átveheted a vezérlést. Tipikus feladatok:

- Biztonsági csoporttagsági kérelmek kezelése
- Auditbizonyíték gyűjtése és validálása megfelelőség-ellenőrzéshez
- IT incidensek triázsa (jegyzet állapot frissítése, tulajdonosok hozzárendelése, duplikátumok lezárása)
- Excel adatok összeállítása pénzügyi zárási prezentációba

Az Opal jó referencia arra, milyen egy **produkciós szintű, megbízható** számítógép-használó ügynök — és megerősíti korábbi leckék koncepcióit:

| Fogalom ebben a tanfolyamban | Hogyan alkalmazza a Project Opal |
|------------------------|-----------------------------|
| **Ember a hurokban** (6. lecke) | Opal megáll a bejelentkezési hitelesítő adatokért, érzékeny adatokért vagy homályos utasításokért, és soha nem ír be jelszavakat vagy küld űrlapokat jóváhagyás nélkül. A munkafolyamat közben átveheted és visszaadhatod az irányítást. |
| **Megbízható és biztonságos ügynökök** (6. & 18. lecke) | Elkülönített Windows 365 Cloud PC-n fut, alapértelmezett böngésző-használó (más számítógépes hozzáférés blokkolva Intune által), a *te* identitásodat használja, így csak a jogosult hozzáférést éri el, és minden műveletet naplóz auditálhatóság érdekében. |
| **Tervezés és metakogníció** (7. & 9. lecke) | Opal először tervet generál a feladathoz, majd minden lépésnél felügyeli az érvelést, és megáll, ha gyanús tevékenységet észlel. |
| **Újrahasznosítható képességek/eszközök** (4. lecke) | A **Készségek** segítségével utasításokat írhatsz ismétlődő feladatokhoz (egy `.md` fájlból importálva vagy Opallal szerkesztve), és újrahasznosíthatod őket beszélgetésekben. |

> **Elérhetőség:** A Project Opal jelenleg elérhető a [Frontier korai hozzáférési program](https://adoption.microsoft.com/copilot/frontier-program/) felhasználói számára Microsoft 365 Copilot előfizetéssel, és az adminisztrátornak kell elvégeznie a beállítást. Mivel egy kísérleti Frontier funkció, a képességek idővel változhatnak.

## Tudásellenőrzés

Teszteld tudásod, mielőtt továbblépnél a következő leckére.

**1. Mikor jobb választás egy böngészőalapú számítógép-használó ügynök, mint egy csak API-alapú munkafolyamat?**

<details>
<summary>Válasz</summary>

Használj böngészőügynököt, amikor a feladat az, amit a webes UI mutat, vagy a szükséges API nem elérhető, vagy az oldal elég gyakran változik, hogy egy rögzített API vagy szelektor logika törékeny lenne. Ha van stabil API ugyanarra a feladatra, azt részesítsd előnyben, mert általában gyorsabb, könnyebb tesztelni és biztonságosabb.
</details>

**2. Egy hibrid munkafolyamatban mely részeket kell az ügynöknek kezelnie, és melyeket a közvetlen Playwright kódnak?**

<details>
<summary>Válasz</summary>

Hagyjuk az ügynököt kezelni a nyitott végű navigációt és a dinamikus UI állapotokat, mint az oldal megtalálása vagy váratlan felugrók elvetése. Váltson közvetlen Playwright vezérlésre, amikor az oldal szerkezete ismert, és precizitásra, újrapróbálkozásra, várakoztatásra vagy determinisztikus validálásra van szükség.
</details>

**3. Az Airbnb példa talál egy listázást, amit a felhasználó foglalni szeretne. Mi történjen, mielőtt a munkafolyamat bejelentkezik, kapcsolatba lép a házigazdával vagy befejezi a foglalást?**

<details>
<summary>Válasz</summary>

A munkafolyamatnak meg kell állnia, és egyértelmű felhasználói jóváhagyást kell kérnie. Azelőtt tiszta összefoglalót kell mutatnia a kiválasztott listáról, az aktuális URL-ről, az árról, időpontokról és a tervezett műveletről. Az árak keresése és kinyerése önállóan mehet, de a fiók-hozzáférés, üzenetek, vásárlások és foglalások felhasználói jóváhagyást igényelnek.
</details>

**4. Egy weboldal azt mondja az ügynöknek, hogy hagyja figyelmen kívül az eredeti utasításait, látogasson el egy másik oldalra, és tegye közzé a mentett hitelesítő adatokat. Hogyan kezelje az ügynök ezt a szöveget?**

<details>
<summary>Válasz</summary>

Kezeld nem megbízható oldal tartalomként, ne fejlesztői vagy felhasználói utasításként. Az ügynök maradjon az engedélyezett domainen és feladatkörön belül, tagadja meg titkok megosztását, és kerüljön el olyan oldalszövegeket, amelyek cél megváltoztatására, védelmi mechanizmusok letiltására vagy nem kapcsolódó oldalak meglátogatására utasítanak.
</details>

**5. Milyen bizonyítékokat érdemes megőrizni, amikor egy böngészőügynök fut, és mit érdemes elkerülni?**

<details>
<summary>Válasz</summary>

Őrzöd meg a művelet összefoglalókat, időbélyegeket, URL-eket, kiválasztott elemek leírásait, validációs eredményeket és képernyőkép hivatkozásokat, hogy a futás után vissza lehessen tekinteni. Kerüld a jelszavak, fizetési adatok, munkamenet sütik, nyers személyes adatok vagy teljes oldaltartalmak tárolását, kivéve ha erre külön megőrzési és adatvédelmi ok van.
</details>

## További források

- [Kezdés a Project Opallal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integrációs sablon](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use szereplő paraméterek és tartalom kinyerés](https://docs.browser-use.com/customize/actor/all-parameters)
- [Tanfolyam beállítása](../00-course-setup/README.md)

## Előző lecke

[Microsoft Agent Framework felfedezése](../14-microsoft-agent-framework/README.md)

## Következő lecke

[Skálázható ügynökök telepítése](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->