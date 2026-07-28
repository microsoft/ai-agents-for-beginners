---
name: deploying-scalable-agents
license: MIT
---
# Skálázható ügynökök telepítése Microsoft Foundry-val

> Kísérő készség a(z) [16. lecke – Skálázható ügynökök telepítése](../../../16-deploying-scalable-agents/README.md) anyaghoz.
> Használd arra, hogy segíts egy tanulónak az ügynököt a prototípustól egy skálázható, megfigyelhető
> éles környezetbe való telepítésig vinni. Minden ajánlást a lecke tartalmára és a
> futtatható jegyzetfüzetre alapozz; ne találj ki Foundry API-kat.

## Indító feltételek

Ezt a készséget aktiváld, ha egy tanuló szeretne:
- Egy ügynököt Microsoft Foundry-ba telepíteni **hostolt ügynökként**, és verziózást/megjeleníthetőséget biztosítani.
- Választani a **kliens-oldali hosztolt, hostolt ügynök és ügynök-munkafolyamat** telepítési minták között.
- Hozzáadni **modell irányítást**, **válasz gyorsítótárazást**, vagy **kötött konkurenciát** a késleltetés és költség szabályozására.
- Hozzáadni egy **értékelési kaput**, hogy egy rossz ügynök verzió ne kerülhessen kiadásra.
- Hozzáadni egy **emberi jóváhagyási** lépést a magas kockázatú műveletekhez.
- Megfigyelhetőséghez egy ügynököt felszerelni **OpenTelemetry** követéssel.
- Egy telepített ügynök **füsttesztelése** gyors, post-deploy ellenőrzésként.

## Alap mentális modell

Egy éles ügynök legtöbbször az operációs csontváz *a modell körül* (~80%),
nem maga a modell. Map-eld minden ajánlást ezekhez az aggályokhoz:

| Aggály | Prototípus → Éles környezet |
|---------|------------------------|
| Hosztolás | jegyzetfüzet → verziózott hosztolt szolgáltatás |
| Identitás | a te `az login` → kezelt identitás + korlátozott RBAC |
| Állapot | memóriában → külső szál/memória tároló |
| Hibakezelés | híváslánc → újrapróbálkozás, visszaesés, riasztások |
| Költség | "néhány cent" → nyomon követett, irányított, gyorsítótárazott, költségvetett |
| Minőség | szemrevételezés → automatizált értékelési kapu |
| Bizalom | te jóváhagyod → szabályzat + emberi beavatkozás |

## Telepítési minták (válassz egyet vagy kombináld)

1. **Kliens hosztolt** — az értékelési ciklus a te folyamatodban fut. Maximális kontroll; te birtoklod a skálázást/állapotot.
2. **Hostolt ügynök (Foundry Agent Service)** — a Foundry hosztolja a ciklust, tárolja a szálakat, érvényesíti az RBAC/tartalom biztonságot, az ügynök megjelenik a portálon. Kevesebb kontroll, sokkal kisebb működési felület.
3. **Ügynök-munkafolyamat** — több ügynök/eszköz összeállítva gráffá elágazásokkal, jóváhagyási pontokkal és tartós ellenőrző pontokkal.

## Élettartam (az az ciklus, amely egy ügynököt szállít)

`létrehozás → verziózás → értékelés (kapu) → hosztolt telepítés → online megfigyelés → hibák gyűjtése → ismétlés`.
**Az offline értékelés kapu, nem utólagos gondolat** — a verzió nem kerül kiadásra
, hacsak nem haladja meg a küszöböt. Az online megfigyelés visszacsatolja a valódi hibákat
az offline tesztkészletbe.

## Skálázási és költség szabályzók (prioritási sorrendben)

1. **Az optimális modellméret kiválasztása** — használd a legkisebb modellt, amely átmegy az értékelési kapun.
2. **Összetettség szerinti irányítás** — kis/gyors modell az egyszerű kérésekhez, nagy modell az igazi értékeléshez (DIY osztályozó vagy Foundry Model Router).
3. **Gyorsítótárazás** — szolgálj ki majdnem ismétlődő kéréseket modell hívás nélkül.
4. **Állapotmentes tervezés + kötött konkurencia** — externalizáld az állapotot; újrapróbálkozás visszaléptetéssel.

## Fontos minták reprodukálása

Mutasd meg a tanulónak ezeket a jegyzetfüzet alapján
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Kéréskezelő**: gyorsítótár → összetettség szerinti irányítás → követési span → futtatás → gyorsítótár.
- **Értékelési kapu**: egy offline tesztkészlet pontozása; visszatér `pass_rate >= threshold` és csak igaz esetén telepít.
- **Emberi jóváhagyás**: `@tool(approval_mode="always_require")` nagy visszatérítések esetén.
- **Követés**: minden kérés becsomagolása `tracer.start_as_current_span(...)`-ben és attribútumok beállítása, mint `routed.model`, `customer.id`.

## Egy telepített ügynök füsttesztelése

Telepítés után ellenőrizd, hogy a végpont valóban válaszol (a zöld telepítés még lehet némán sikertelen).
Használd az [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
műveletet a(z) [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
fájlon keresztül a [`tests/`](../../../tests/README.md) katalógussal. A futtató POST-olja minden
kérést a címre `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
és ellenőrzi a válasz szöveget. Az identitásnak meg kell kapnia az **Azure AI User** szerepet a
Foundry projekt hatókörében; a token audienciának `https://ai.azure.com/` kell lennie.

Rétegezd a kapukat: **füstteszt** (elérhető/válaszol, minden telepítéskor) → **offline
értékelés** (elég jó a kiadáshoz, promóció előtt) → **online értékelés** (hogyan
teljesít a valóságban, folyamatos).

## Vállalati szabályozók

- **RBAC**: adj minden hosztolt ügynöknek egy legkisebb jogosultságú kezelt identitást.
- **MCP éles környezetben**: minden MCP szervert kezelj megbízhatatlan határként — tűzd le a verziót, határozd meg az identitását, validáld a kimeneteket, korlátozd a forgalmat, soha ne tedd ki titkokat.

## Őrvonalak az asszisztens számára

- Előnyben részesítsd a kanonikus `FoundryChatClient(...)` + `provider.as_agent(...)` mintát, amely az egész tanfolyam során használatos.
- Ne ígérj éles-Azure eredményeket, amelyeket nem ellenőriztél; ajánld a füstteszt munkafolyamatot a telepítés megerősítésére.
- Tartsd összhangban az értékelési és a költség tanácsokat: az értékelés szabja meg a minőségi minimumot, az irányítás/gyorsítótárazás tartja a költséget ezen a minimumon.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->