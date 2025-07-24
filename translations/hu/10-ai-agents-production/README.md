<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8164484c16b1ed3287ef9dae9fc437c1",
  "translation_date": "2025-07-24T08:56:15+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "hu"
}
-->
# AI-ügynökök a gyakorlatban: Megfigyelhetőség és értékelés

Ahogy az AI-ügynökök kísérleti prototípusokból valós alkalmazásokká válnak, egyre fontosabbá válik viselkedésük megértése, teljesítményük nyomon követése és kimeneteik rendszerszintű értékelése.

## Tanulási célok

A lecke elvégzése után képes leszel:
- Megérteni az ügynökök megfigyelhetőségének és értékelésének alapfogalmait
- Technikákat alkalmazni az ügynökök teljesítményének, költségeinek és hatékonyságának javítására
- Szisztematikusan értékelni az AI-ügynökeidet
- Költségeket kontrollálni az AI-ügynökök éles környezetbe történő telepítésekor
- Az AutoGen-nel épített ügynököket megfelelően instrumentálni

A cél az, hogy olyan tudással ruházzunk fel, amely lehetővé teszi, hogy a "fekete doboz" ügynökeidet átlátható, kezelhető és megbízható rendszerekké alakítsd.

_**Megjegyzés:** Fontos, hogy biztonságos és megbízható AI-ügynököket telepíts. Nézd meg a [Megbízható AI-ügynökök építése](./06-building-trustworthy-agents/README.md) leckét is._

## Nyomok és szakaszok

A megfigyelhetőségi eszközök, mint például a [Langfuse](https://langfuse.com/) vagy az [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), általában az ügynök futásait nyomokként és szakaszokként ábrázolják.

- **Nyom**: Egy teljes ügynökfeladatot képvisel az elejétől a végéig (például egy felhasználói kérdés kezelése).
- **Szakaszok**: A nyomon belüli egyes lépések (például egy nyelvi modell hívása vagy adatok lekérése).

![Nyomfa a Langfuse-ban](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Megfigyelhetőség nélkül egy AI-ügynök "fekete doboznak" tűnhet – belső állapota és érvelése átláthatatlan, ami megnehezíti a problémák diagnosztizálását vagy a teljesítmény optimalizálását. A megfigyelhetőséggel az ügynökök "üvegdobozokká" válnak, átláthatóságot biztosítva, amely elengedhetetlen a bizalom kiépítéséhez és annak biztosításához, hogy az ügynökök a kívánt módon működjenek.

## Miért fontos a megfigyelhetőség éles környezetben?

Az AI-ügynökök éles környezetbe történő átültetése új kihívásokat és követelményeket hoz magával. A megfigyelhetőség már nem "jó, ha van", hanem kritikus képesség:

*   **Hibakeresés és gyökérok-elemzés**: Ha egy ügynök hibázik vagy váratlan kimenetet produkál, a megfigyelhetőségi eszközök nyomokat biztosítanak a hiba forrásának azonosításához. Ez különösen fontos összetett ügynököknél, amelyek több LLM-hívást, eszközinterakciót és feltételes logikát is magukban foglalhatnak.
*   **Késleltetés és költségkezelés**: Az AI-ügynökök gyakran támaszkodnak LLM-ekre és más külső API-kra, amelyek tokenenként vagy hívásonként kerülnek számlázásra. A megfigyelhetőség lehetővé teszi ezeknek a hívásoknak a pontos nyomon követését, segítve azonosítani a túl lassú vagy drága műveleteket. Ezáltal a csapatok optimalizálhatják a promptokat, hatékonyabb modelleket választhatnak, vagy áttervezhetik a munkafolyamatokat az üzemeltetési költségek kezelése és a jó felhasználói élmény biztosítása érdekében.
*   **Bizalom, biztonság és megfelelőség**: Számos alkalmazásban fontos biztosítani, hogy az ügynökök biztonságosan és etikusan viselkedjenek. A megfigyelhetőség auditnyomvonalat biztosít az ügynökök cselekedeteiről és döntéseiről. Ez felhasználható olyan problémák észlelésére és enyhítésére, mint a prompt injekció, káros tartalom generálása vagy a személyes adatok (PII) helytelen kezelése. Például nyomokat vizsgálhatsz meg, hogy megértsd, miért adott az ügynök egy adott választ, vagy miért használt egy adott eszközt.
*   **Folyamatos fejlesztési ciklusok**: A megfigyelhetőségi adatok az iteratív fejlesztési folyamat alapját képezik. Azáltal, hogy nyomon követed, hogyan teljesítenek az ügynökök a valós világban, a csapatok azonosíthatják a fejlesztési területeket, adatokat gyűjthetnek a modellek finomhangolásához, és érvényesíthetik a változtatások hatását. Ez egy visszacsatolási hurkot hoz létre, ahol az online értékelésből származó gyártási betekintések tájékoztatják az offline kísérletezést és finomítást, ami fokozatosan jobb ügynökteljesítményhez vezet.

## Kulcsfontosságú mérőszámok nyomon követése

Az ügynök viselkedésének nyomon követéséhez és megértéséhez számos mérőszámot és jelet kell figyelni. Bár a konkrét mérőszámok az ügynök céljától függően változhatnak, néhány univerzálisan fontos.

Íme néhány a leggyakoribb mérőszámok közül, amelyeket a megfigyelhetőségi eszközök figyelnek:

**Késleltetés:** Milyen gyorsan válaszol az ügynök? A hosszú várakozási idők negatívan befolyásolják a felhasználói élményt. Mérd a késleltetést a feladatok és az egyes lépések szintjén az ügynök futásainak nyomon követésével. Például egy ügynök, amely 20 másodpercet vesz igénybe az összes modellhívásra, felgyorsítható egy gyorsabb modell használatával vagy a modellhívások párhuzamos futtatásával.

**Költségek:** Mennyibe kerül egy ügynök futtatása? Az AI-ügynökök LLM-hívásokra támaszkodnak, amelyek tokenenként vagy külső API-ként kerülnek számlázásra. A gyakori eszközhasználat vagy több prompt gyorsan növelheti a költségeket. Például, ha egy ügynök ötször hív egy LLM-et a marginális minőségjavítás érdekében, értékelned kell, hogy a költség indokolt-e, vagy csökkentheted a hívások számát, illetve használhatsz olcsóbb modellt. A valós idejű monitorozás segíthet azonosítani a váratlan kiugrásokat is (például hibák, amelyek túlzott API-hurkokat okoznak).

**Kéréshibák:** Hány kérést nem sikerült teljesítenie az ügynöknek? Ez magában foglalhatja az API-hibákat vagy a sikertelen eszközhívásokat. Az ügynök robusztusabbá tétele érdekében éles környezetben beállíthatsz tartalék megoldásokat vagy újrapróbálkozásokat. Például, ha az A LLM-szolgáltató nem elérhető, válthatsz a B LLM-szolgáltatóra tartalékként.

**Felhasználói visszajelzés:** A közvetlen felhasználói értékelések értékes betekintést nyújtanak. Ez magában foglalhatja az explicit értékeléseket (👍fel vagy 👎le, ⭐1-5 csillag) vagy szöveges megjegyzéseket. A következetesen negatív visszajelzések figyelmeztethetnek, hogy az ügynök nem működik megfelelően.

**Implicit felhasználói visszajelzés:** A felhasználói viselkedések közvetett visszajelzést nyújtanak még explicit értékelések nélkül is. Ez magában foglalhatja az azonnali kérdésátfogalmazást, ismételt lekérdezéseket vagy egy újrapróbálkozás gomb megnyomását. Például, ha azt látod, hogy a felhasználók ismételten ugyanazt a kérdést teszik fel, ez annak a jele, hogy az ügynök nem működik megfelelően.

**Pontosság:** Milyen gyakran produkál az ügynök helyes vagy kívánatos kimeneteket? A pontosság definíciói változhatnak (például problémamegoldási helyesség, információ-visszakeresési pontosság, felhasználói elégedettség). Az első lépés annak meghatározása, hogy mit jelent a siker az ügynök számára. A pontosságot automatizált ellenőrzésekkel, értékelési pontszámokkal vagy feladatbefejezési címkékkel követheted nyomon. Például a nyomokat "sikeres" vagy "sikertelen" címkékkel láthatod el.

**Automatizált értékelési mérőszámok:** Beállíthatsz automatizált értékeléseket is. Például használhatsz egy LLM-et az ügynök kimenetének pontozására, például hogy az hasznos, pontos vagy sem. Számos nyílt forráskódú könyvtár is segít az ügynök különböző aspektusainak pontozásában. Például [RAGAS](https://docs.ragas.io/) RAG-ügynökökhöz vagy [LLM Guard](https://llm-guard.com/) káros nyelvezet vagy prompt injekció észlelésére.

A gyakorlatban ezeknek a mérőszámoknak a kombinációja nyújtja a legjobb lefedettséget egy AI-ügynök egészségi állapotáról. Ebben a fejezetben az [példa notebookban](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) megmutatjuk, hogyan néznek ki ezek a mérőszámok valós példákban, de először megismerjük, hogyan néz ki egy tipikus értékelési munkafolyamat.

- Finomítsd a meghatározott paramétereket, utasításokat és az eszközök elnevezését.  |
| A többügynökös rendszer nem működik következetesen | - Finomítsd az egyes ügynököknek adott utasításokat, hogy specifikusak és egymástól jól elkülöníthetők legyenek.<br>- Építs egy hierarchikus rendszert egy "irányító" vagy vezérlő ügynök segítségével, amely meghatározza, melyik ügynök a megfelelő. |

Sok ilyen probléma hatékonyabban azonosítható, ha megfigyelhetőség van beépítve. Az előzőekben tárgyalt nyomkövetések és metrikák segítenek pontosan meghatározni, hogy az ügynök munkafolyamatának mely pontján jelentkeznek problémák, így a hibakeresés és az optimalizálás sokkal hatékonyabbá válik.

## Költségek kezelése

Íme néhány stratégia az AI ügynökök éles környezetbe történő telepítésének költségeinek kezelésére:

**Kisebb modellek használata:** A kis nyelvi modellek (SLM-ek) bizonyos ügynöki felhasználási esetekben jól teljesíthetnek, és jelentősen csökkenthetik a költségeket. Ahogy korábban említettük, egy értékelési rendszer kiépítése, amely összehasonlítja a teljesítményt a nagyobb modellekkel, a legjobb módja annak, hogy megértsük, mennyire jól teljesít egy SLM az adott felhasználási esetben. Fontold meg SLM-ek használatát egyszerűbb feladatokhoz, például szándékosztályozáshoz vagy paraméterek kinyeréséhez, míg a nagyobb modelleket tartogasd az összetettebb érvelési feladatokra.

**Irányító modell használata:** Egy hasonló stratégia a különböző méretű és típusú modellek használata. Használhatsz egy LLM/SLM-et vagy szerver nélküli funkciót, hogy az összetettség alapján irányítsd a kéréseket a legmegfelelőbb modellekhez. Ez nemcsak a költségeket csökkenti, hanem biztosítja a megfelelő teljesítményt is a megfelelő feladatokon. Például az egyszerű lekérdezéseket kisebb, gyorsabb modellekhez irányítsd, és csak az összetett érvelési feladatokhoz használd a drágább nagy modelleket.

**Válaszok gyorsítótárazása:** Az ismétlődő kérések és feladatok azonosítása, valamint a válaszok előzetes biztosítása az ügynöki rendszerbe való belépés előtt jó módja a hasonló kérések mennyiségének csökkentésére. Akár egy olyan folyamatot is bevezethetsz, amely azonosítja, hogy egy kérés mennyire hasonlít a gyorsítótárban lévő kérésekhez, egyszerűbb AI modellek segítségével. Ez a stratégia jelentősen csökkentheti a költségeket a gyakran ismétlődő kérdések vagy munkafolyamatok esetén.

## Nézzük, hogyan működik ez a gyakorlatban

A [szakasz példafüzetében](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) példákat láthatunk arra, hogyan használhatunk megfigyelési eszközöket az ügynökök monitorozására és értékelésére.

## Előző lecke

[Metakogníció tervezési minta](../09-metacognition/README.md)

## Következő lecke

[MCP](../11-mcp/README.md)

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.