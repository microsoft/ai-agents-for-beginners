<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T20:06:44+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "hu"
}
-->
[![Többügynökös tervezés](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.hu.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kattints a fenti képre a leckéhez tartozó videó megtekintéséhez)_

# Többügynökös tervezési minták

Amint elkezdesz egy olyan projekten dolgozni, amely több ügynököt is magában foglal, figyelembe kell venned a többügynökös tervezési mintát. Azonban nem mindig egyértelmű, mikor érdemes több ügynökre váltani, és mik az előnyei.

## Bevezetés

Ebben a leckében a következő kérdésekre keressük a választ:

- Milyen forgatókönyvekben alkalmazható a többügynökös megközelítés?
- Milyen előnyei vannak a többügynökös rendszernek az egyetlen ügynökkel szemben, amely több feladatot lát el?
- Mik a többügynökös tervezési minta megvalósításának építőkövei?
- Hogyan biztosítható az átláthatóság az ügynökök közötti interakciókban?

## Tanulási célok

A lecke végére képes leszel:

- Azonosítani azokat a forgatókönyveket, ahol a többügynökös megközelítés alkalmazható.
- Felismerni a többügynökös rendszer előnyeit az egyetlen ügynökkel szemben.
- Megérteni a többügynökös tervezési minta megvalósításának építőköveit.

Mi a nagyobb kép?

*A többügynökös rendszer egy olyan tervezési minta, amely lehetővé teszi, hogy több ügynök együttműködve érjen el egy közös célt.*

Ez a minta széles körben alkalmazott különböző területeken, például robotikában, autonóm rendszerekben és elosztott számítástechnikában.

## Forgatókönyvek, ahol a többügynökös megközelítés alkalmazható

Milyen forgatókönyvekben érdemes több ügynököt alkalmazni? A válasz az, hogy számos esetben előnyös lehet több ügynök alkalmazása, különösen az alábbi helyzetekben:

- **Nagy munkaterhelés**: A nagy munkaterhelést kisebb feladatokra lehet bontani, és különböző ügynökökre osztani, lehetővé téve a párhuzamos feldolgozást és a gyorsabb befejezést. Példa erre egy nagy adatfeldolgozási feladat.
- **Komplex feladatok**: A komplex feladatokat, hasonlóan a nagy munkaterheléshez, kisebb részfeladatokra lehet bontani, és különböző ügynökökre bízni, amelyek egy-egy specifikus részfeladatra specializálódtak. Jó példa erre az autonóm járművek esete, ahol különböző ügynökök kezelik a navigációt, az akadályok észlelését, valamint a többi járművel való kommunikációt.
- **Sokféle szakértelem**: Különböző ügynökök eltérő szakértelemmel rendelkezhetnek, így hatékonyabban tudják kezelni a feladat különböző aspektusait, mint egyetlen ügynök. Példa erre az egészségügy, ahol az ügynökök kezelhetik a diagnosztikát, a kezelési terveket és a betegmegfigyelést.

## A többügynökös rendszer előnyei az egyetlen ügynökkel szemben

Egyetlen ügynökös rendszer jól működhet egyszerű feladatok esetén, de összetettebb feladatoknál a többügynökös megközelítés számos előnnyel járhat:

- **Specializáció**: Minden ügynök egy adott feladatra specializálódhat. Egyetlen ügynök specializációjának hiánya azt eredményezheti, hogy az ügynök összezavarodik egy komplex feladat esetén, és esetleg olyan feladatot végez el, amelyre nem a legalkalmasabb.
- **Skálázhatóság**: Könnyebb a rendszert bővíteni további ügynökök hozzáadásával, mint egyetlen ügynök túlterhelésével.
- **Hibatűrés**: Ha egy ügynök meghibásodik, a többi továbbra is működhet, biztosítva a rendszer megbízhatóságát.

Vegyünk egy példát: egy felhasználó számára utazást kell lefoglalni. Egyetlen ügynökös rendszernek az utazásfoglalási folyamat minden aspektusát kezelnie kellene, a repülőjáratok keresésétől a szállodák és bérautók foglalásáig. Ehhez az ügynöknek minden feladat kezelésére alkalmas eszközökkel kellene rendelkeznie, ami egy bonyolult és monolitikus rendszert eredményezne, amelyet nehéz karbantartani és skálázni. Ezzel szemben egy többügynökös rendszerben különböző ügynökök specializálódhatnak a repülőjáratok keresésére, a szállodák foglalására és a bérautók kezelésére. Ez a rendszer modulárisabb, könnyebben karbantartható és skálázható lenne.

Hasonlítsuk ezt össze egy kis családi utazási irodával és egy franchise rendszerben működő utazási irodával. A családi üzletben egyetlen ügynök kezelné az utazásfoglalási folyamat minden aspektusát, míg a franchise rendszerben különböző ügynökök foglalkoznának az utazás különböző aspektusaival.

## A többügynökös tervezési minta megvalósításának építőkövei

Mielőtt megvalósítanád a többügynökös tervezési mintát, meg kell értened a minta építőköveit.

Tegyük ezt konkrétabbá azzal, hogy ismét az utazásfoglalás példáját vesszük alapul. Ebben az esetben az építőkövek a következők lennének:

- **Ügynökök közötti kommunikáció**: Az ügynököknek, amelyek a repülőjáratok keresésével, a szállodák foglalásával és a bérautók kezelésével foglalkoznak, kommunikálniuk kell egymással, és meg kell osztaniuk az információkat a felhasználó preferenciáiról és korlátairól. El kell döntened, hogy milyen protokollokat és módszereket használsz ehhez a kommunikációhoz. Ez konkrétan azt jelenti, hogy a repülőjáratokat kereső ügynöknek kommunikálnia kell a szállodafoglaló ügynökkel, hogy a szálloda ugyanarra az időpontra legyen lefoglalva, mint a repülőjárat.
- **Koordinációs mechanizmusok**: Az ügynököknek össze kell hangolniuk a tevékenységeiket, hogy biztosítsák a felhasználó preferenciáinak és korlátainak teljesülését. Például, ha a felhasználó azt szeretné, hogy a szálloda közel legyen a repülőtérhez, akkor a szállodafoglaló ügynöknek koordinálnia kell a bérautó-foglaló ügynökkel.
- **Ügynökök architektúrája**: Az ügynököknek rendelkezniük kell egy belső struktúrával, amely lehetővé teszi számukra a döntéshozatalt és a felhasználóval való interakciókból való tanulást.
- **Átláthatóság az ügynökök közötti interakciókban**: Fontos, hogy átlátható legyen, hogyan működnek együtt az ügynökök. Ehhez eszközökre és technikákra van szükség az ügynökök tevékenységeinek és interakcióinak nyomon követésére.
- **Többügynökös minták**: Különböző minták léteznek a többügynökös rendszerek megvalósítására, például központosított, decentralizált és hibrid architektúrák. El kell döntened, melyik minta illik legjobban az adott felhasználási esetedhez.
- **Emberi beavatkozás**: A legtöbb esetben szükség lesz emberi beavatkozásra, és meg kell határoznod, hogy az ügynökök mikor kérjenek emberi segítséget.

## Átláthatóság az ügynökök közötti interakciókban

Fontos, hogy átlátható legyen, hogyan működnek együtt az ügynökök. Ez elengedhetetlen a hibakereséshez, az optimalizáláshoz és a rendszer hatékonyságának biztosításához. Ehhez eszközökre és technikákra van szükség az ügynökök tevékenységeinek és interakcióinak nyomon követésére.

Például az utazásfoglalás esetében lehetne egy irányítópult, amely megmutatja az egyes ügynökök állapotát, a felhasználó preferenciáit és korlátait, valamint az ügynökök közötti interakciókat.

- **Naplózási és monitorozási eszközök**: Minden ügynök által végrehajtott műveletet naplózni kell. Egy naplóbejegyzés tartalmazhatja az ügynök nevét, a végrehajtott műveletet, az időpontot és az eredményt.
- **Vizualizációs eszközök**: Ezek segíthetnek az ügynökök közötti interakciók intuitívabb megértésében, például egy grafikon formájában, amely az információáramlást mutatja.
- **Teljesítménymutatók**: Ezek segíthetnek a többügynökös rendszer hatékonyságának nyomon követésében, például a feladatok elvégzéséhez szükséges idő, az egységnyi idő alatt elvégzett feladatok száma és az ügynökök ajánlásainak pontossága alapján.

## Többügynökös minták

Nézzünk meg néhány konkrét mintát, amelyeket többügynökös alkalmazások létrehozásához használhatunk:

### Csoportos csevegés

Ez a minta akkor hasznos, ha csoportos csevegőalkalmazást szeretnél létrehozni, ahol több ügynök kommunikálhat egymással. Tipikus felhasználási esetek: csapatmunka, ügyfélszolgálat és közösségi hálózatok.

![Csoportos csevegés](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.hu.png)

### Feladatátadás

Ez a minta akkor hasznos, ha olyan alkalmazást szeretnél létrehozni, ahol az ügynökök átadhatják egymásnak a feladatokat.

![Feladatátadás](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.hu.png)

### Közös ajánlás

Ez a minta akkor hasznos, ha olyan alkalmazást szeretnél létrehozni, ahol több ügynök együttműködve tesz ajánlásokat a felhasználóknak.

![Ajánlás](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.hu.png)

## Forgatókönyv: Visszatérítési folyamat

Vegyünk egy példát, ahol egy ügyfél visszatérítést szeretne kérni egy termékért. Ebben a folyamatban több ügynök is részt vehet, amelyeket két csoportra oszthatunk: a visszatérítési folyamathoz specifikus ügynökök és általános ügynökök.

**A visszatérítési folyamathoz specifikus ügynökök**:

- **Ügyfélügynök**: Az ügyfelet képviseli, és felelős a visszatérítési folyamat elindításáért.
- **Eladóügynök**: Az eladót képviseli, és felelős a visszatérítés feldolgozásáért.
- **Fizetési ügynök**: A fizetési folyamatot képviseli, és felelős az ügyfél pénzének visszatérítéséért.
- **Megoldási ügynök**: A problémák megoldásáért felelős, amelyek a visszatérítési folyamat során merülnek fel.
- **Megfelelőségi ügynök**: Biztosítja, hogy a visszatérítési folyamat megfeleljen a szabályozásoknak és irányelveknek.

**Általános ügynökök**:

- **Szállítási ügynök**: A szállítási folyamatot képviseli, és felelős a termék visszaküldéséért az eladónak.
- **Visszajelzési ügynök**: Az ügyfél visszajelzéseinek gyűjtéséért felelős.
- **Eszkalációs ügynök**: A problémák magasabb szintű támogatásra történő továbbításáért felelős.
- **Értesítési ügynök**: Az ügyfél értesítéséért felelős a visszatérítési folyamat különböző szakaszaiban.
- **Elemzési ügynök**: Az adatok elemzéséért felelős.
- **Audit ügynök**: A visszatérítési folyamat helyességének ellenőrzéséért felelős.
- **Jelentési ügynök**: Jelentések készítéséért felelős.
- **Tudásügynök**: A visszatérítési folyamathoz kapcsolódó tudásbázis karbantartásáért felelős.
- **Biztonsági ügynök**: A visszatérítési folyamat biztonságának biztosításáért felelős.
- **Minőségügyi ügynök**: A visszatérítési folyamat minőségének biztosításáért felelős.

Remélhetőleg ez az áttekintés segít abban, hogy eldöntsd, mely ügynököket érdemes használni a többügynökös rendszeredben.

## Feladat
Tervezzen egy többügynökös rendszert az ügyfélszolgálati folyamat számára. Határozza meg a folyamatban részt vevő ügynököket, azok szerepeit és felelősségeit, valamint azt, hogyan lépnek kapcsolatba egymással. Vegye figyelembe az ügyfélszolgálati folyamathoz specifikus ügynököket, valamint azokat az általános ügynököket, amelyek az üzlet más részein is használhatók.

> Gondolja át, mielőtt elolvassa a következő megoldást, lehet, hogy több ügynökre van szüksége, mint gondolná.

> TIP: Gondoljon az ügyfélszolgálati folyamat különböző szakaszaira, és vegye figyelembe az ügynököket, amelyek bármely rendszerhez szükségesek lehetnek.

## Megoldás

[Megoldás](./solution/solution.md)

## Tudásellenőrzés

Kérdés: Mikor érdemes többügynökös rendszert használni?

- [ ] A1: Ha kis munkaterhelés és egyszerű feladat van.
- [ ] A2: Ha nagy munkaterhelés van.
- [ ] A3: Ha egyszerű feladat van.

[Megoldás kvíz](./solution/solution-quiz.md)

## Összefoglaló

Ebben a leckében megvizsgáltuk a többügynökös tervezési mintát, beleértve azokat a helyzeteket, ahol a többügynökös megközelítés alkalmazható, a többügynökös rendszerek előnyeit az egyetlen ügynökhöz képest, a többügynökös tervezési minta megvalósításának építőelemeit, valamint azt, hogyan lehet átlátni, hogy az ügynökök hogyan lépnek kapcsolatba egymással.

### További kérdései vannak a többügynökös tervezési mintával kapcsolatban?

Csatlakozzon az [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) közösséghez, hogy találkozzon más tanulókkal, részt vegyen konzultációkon, és választ kapjon az AI ügynökökkel kapcsolatos kérdéseire.

## További források

- 

## Előző lecke

[Tervezési tervezés](../07-planning-design/README.md)

## Következő lecke

[Metakogníció az AI ügynökökben](../09-metacognition/README.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.