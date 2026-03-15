[![Bevezetés az AI ügynökökhöz](../../../translated_images/hu/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kattintson a fenti képre a videó megtekintéséhez)_


# Bevezetés az AI ügynökökbe és ügynökhöz tartozó felhasználási esetekbe

Üdvözöljük az „AI ügynökök kezdőknek” tanfolyamon! Ez a tanfolyam alapvető ismereteket és gyakorlati példákat nyújt az AI ügynökök építéséhez.

Csatlakozzon az <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord közösséghez</a>, hogy találkozzon más tanulókkal és AI ügynök építőkkel, és tegye fel kérdéseit a tanfolyammal kapcsolatban.

A tanfolyam elindításához először jobban megértjük, mik az AI ügynökök, és hogyan tudjuk őket használni az általaunk épített alkalmazásokban és munkafolyamatokban.

## Bevezetés

Ez a lecke a következőket tárgyalja:

- Mik az AI ügynökök és mik az ügynökök különböző típusai?
- Milyen felhasználási esetekhez a legalkalmasabbak az AI ügynökök, és hogyan segíthetnek nekünk?
- Melyek az alapvető építőkövek egy ügynöki megoldás tervezésekor?

## Tanulási célok
A lecke elvégzése után képesnek kell lennie:

- Megérteni az AI ügynökök fogalmait és azt, hogy miben különböznek más AI megoldásoktól.
- Leghatékonyabban alkalmazni az AI ügynököket.
- Termelékenyen tervezni ügynöki megoldásokat mind a felhasználók, mind az ügyfelek számára.

## AI ügynökök meghatározása és AI ügynök típusok

### Mik az AI ügynökök?

Az AI ügynökök olyan **rendszerek**, amelyek lehetővé teszik a **nagy nyelvi modelleknek (LLM-eknek)**, hogy **műveleteket hajtsanak végre** azáltal, hogy kibővítik a képességeiket azzal, hogy az LLM-ek **hozzáférést kapnak eszközökhöz** és **tudáshoz**.

Nézzük meg ezt a meghatározást kisebb részekre bontva:

- **Rendszer** – Fontos, hogy az ügynököket ne csak mint egyetlen komponenst, hanem sok komponensből álló rendszerként tekintsük. Egy AI ügynök alapvető komponensei:
  - **Környezet** – A meghatározott tér, ahol az AI ügynök működik. Például ha lenne egy utazási foglalási AI ügynökünk, a környezet lehet maga az utazási foglalási rendszer, amelyet az ügynök használ a feladatok elvégzéséhez.
  - **Érzékelők** – A környezetek információval rendelkeznek és visszajelzést adnak. Az AI ügynökök érzékelőket használnak, hogy összegyűjtsék és értelmezzék a környezet aktuális állapotáról szóló információkat. Az utazási foglalási ügynök példájában az utazási rendszer például szálláshely elérhetőséget vagy repülőjegyárakat tud adni.
  - **Kivitelezők** – Miután az AI ügynök megkapta a környezet jelenlegi állapotát, az adott feladatra meghatározza, hogy milyen műveletet hajtson végre a környezet megváltoztatása érdekében. Az utazási ügynök esetében ez lehet egy szabad szoba lefoglalása a felhasználónak.

![Mik az AI ügynökök?](../../../translated_images/hu/what-are-ai-agents.1ec8c4d548af601a.webp)

**Nagy nyelvi modellek** – Az ügynökök fogalma már az LLM-ek létrejötte előtt is létezett. Az AI ügynökök LLM-ekkel való építésének előnye, hogy képesek értelmezni az emberi nyelvet és az adatokat. Ez a képesség lehetővé teszi, hogy az LLM-ek értelmezzék a környezeti információkat és meghatározzák a környezet megváltoztatására irányuló tervet.

**Műveletek végrehajtása** – Az AI ügynök rendszereken kívül az LLM-ek korlátozottak olyan helyzetekben, ahol az akció tartalom vagy információ generálása egy felhasználói bemenet alapján. Az AI ügynök rendszeren belül az LLM-ek képesek feladatokat végrehajtani azáltal, hogy értelmezik a felhasználó kéréseit és eszközöket használnak, amelyek elérhetők a környezetükben.

**Hozzáférés eszközökhöz** – Az, hogy milyen eszközökhöz fér hozzá egy LLM, 1) a működési környezettől, és 2) az AI ügynök fejlesztőjétől függ. Utazási ügynök példánkban az ügynök eszközeit a foglalási rendszeren belüli műveletek korlátozzák, illetve a fejlesztő az eszközhozzáférést korlátozhatja például csak repülőjegyekre.

**Memória+Tudás** – A memória lehet rövid távú a felhasználó és az ügynök közti beszélgetés kontextusában. Hosszú távon, a környezet által szolgáltatott információn túl az AI ügynökök tudást is elő tudnak hívni más rendszerekből, szolgáltatásokból, eszközökből és akár más ügynököktől. Utazási ügynök példánkban ez a tudás lehet a felhasználó utazási preferenciáiról szóló információ egy ügyféladatbázisban.

### Az ügynökök különböző típusai

Most, hogy van egy általános meghatározásunk az AI ügynökökről, nézzünk meg néhány konkrét ügynöktípust, és azt, hogy ezek hogyan alkalmazhatók egy utazási foglalási AI ügynökre.

| **Ügynök típusa**              | **Leírás**                                                                                                                             | **Példa**                                                                                                                                                                                                                   |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Egyszerű reflex ügynökök**   | Azonnali műveleteket hajtanak végre előre definiált szabályok alapján.                                                                   | Az utazási ügynök értelmezi az e-mail kontextusát, és utazási panaszokat továbbít az ügyfélszolgálatnak.                                                                                                                    |
| **Modell-alapú reflex ügynökök**| A világ modellje és annak változásai alapján hajtanak végre műveleteket.                                                               | Az utazási ügynök előnyben részesíti azokat az útvonalakat, ahol jelentős árváltozás történt, a múltbeli áradatokhoz való hozzáférés alapján.                                                                               |
| **Cél-alapú ügynökök**          | Terveket készítenek egy adott cél elérésére azzal, hogy értelmezik a célt és meghatározzák a hozzá vezető lépéseket.                      | Az utazási ügynök lefoglal egy utat azzal, hogy meghatározza a szükséges utazási lépéseket (autó, tömegközlekedés, repülőjegyek) a kiinduló helytől a célállomásig.                                                              |
| **Haszon-alapú ügynökök**       | Számításba veszik a preferenciákat és numerikusan mérlegelik az előnyöket és hátrányokat a célok elérésének módjának meghatározásához.    | Az utazási ügynök maximalizálja a hasznosságot azáltal, hogy az utazás lefoglalásakor mérlegeli a kényelmet és a költséget.                                                                                                   |
| **Tanuló ügynökök**             | Idővel javulnak a visszacsatolásokra reagálva és az azok alapján történő akciók módosításával.                                            | Az utazási ügynök a visszajelzések alapján javul a felhasználói felmérések után, és ennek alapján módosítja a jövőbeli foglalásokat.                                                                                         |
| **Hierarchikus ügynökök**       | Több ügynök alkot egy hierarchikus rendszert, ahol a felsőbb szintű ügynökök bontják tovább a feladatokat az alsóbb szintű ügynököknek.  | Az utazási ügynök egy utazás törlését feladatokra bontja (például specifikus foglalások törlése), majd az alsóbb szintű ügynökök elvégzik őket, és visszajelzést adnak a felsőbb szintű ügynöknek.                                   |
| **Többügynökös rendszerek (MAS)** | Az ügynökök önállóan teljesítik a feladatokat, akár együttműködve, akár versengve.                                                      | Együttműködés: Több ügynök különféle utazási szolgáltatásokat foglal, például szállodákat, repülőjegyeket és programokat. Versengés: Több ügynök menedzsel egy megosztott szállodafoglalási naptárat, hogy vendégeket foglaljon be. |

## Mikor érdemes AI ügynököket használni

Az előző szakaszban az utazási ügynök példájával mutattuk be, hogy a különböző típusú ügynökök hogyan használhatók különféle utazási foglalási helyzetekben. Ezt az alkalmazást a tanfolyam során is használjuk.

Nézzük meg azokat az eseteket, amikor az AI ügynökök a legalkalmasabbak:

![Mikor használjunk AI ügynököket?](../../../translated_images/hu/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Nyitott végű problémák** – amikor az LLM határozza meg a feladat elvégzéséhez szükséges lépéseket, mert azokat nem mindig lehet keményen kódolni egy munkafolyamatba.
- **Többlépcsős folyamatok** – feladatok, amelyek komplexitásuk miatt megkövetelik, hogy az AI ügynök több lépésben használjon eszközöket vagy információkat egyetlen lekérdezés helyett.  
- **Folyamatos javulás idővel** – olyan feladatok, ahol az ügynök idővel javulhat, ha visszacsatolást kap a környezetétől vagy felhasználóktól a jobb hasznosság érdekében.

További megfontolásokat az AI ügynökök használatával kapcsolatban a Megbízható AI ügynökök építése leckében talál.

## Ügynöki megoldások alapjai

### Ügynök fejlesztés

Az AI ügynök rendszer tervezésének első lépése az eszközök, műveletek és viselkedések meghatározása. Ebben a tanfolyamban az **Azure AI Agent Service** használatára összpontosítunk az ügynökök meghatározásához. Ez a szolgáltatás olyan funkciókat kínál, mint:

- Nyílt modellek kiválasztása, például OpenAI, Mistral és Llama
- Engedélyezett adatok használata, például a Tripadvisor szolgáltatóitól
- Szabványosított OpenAPI 3.0 eszközök használata

### Ügynöki minták

A kommunikáció az LLM-ekkel promptokon keresztül történik. Az AI ügynökök félig autonóm jellegéből adódóan nem mindig lehetséges vagy szükséges az LLM újrakérését manuálisan elvégezni a környezet változásai után. Az **ügynöki mintákat** használjuk, amelyek lehetővé teszik, hogy az LLM-et több lépésben, skálázható módon promptoljuk.

Ez a tanfolyam a jelenleg népszerű ügynöki minták egy részére oszlik.

### Ügynöki keretrendszerek

Az ügynöki keretrendszerek lehetővé teszik a fejlesztők számára, hogy kódon keresztül implementáljanak ügynöki mintákat. Ezek a keretrendszerek sablonokat, pluginokat és eszközöket kínálnak a jobb AI ügynök együttműködéshez. Ezek az előnyök jobb megfigyelhetőséget és hibakeresést tesznek lehetővé az AI ügynök rendszerek esetén.

Ebben a tanfolyamban a Microsoft Agent Frameworköt (MAF) fogjuk felfedezni az éles környezetbe szánt AI ügynökök építésére.

## Példakódok

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## További kérdései vannak az AI ügynökökről?

Csatlakozzon a [Microsoft Foundry Discordhoz](https://aka.ms/ai-agents/discord), hogy találkozhasson más tanulókkal, részt vehessen konzultációkon, és választ kapjon AI ügynökökkel kapcsolatos kérdéseire.

## Előző lecke

[Kurzus beállítása](../00-course-setup/README.md)

## Következő lecke

[Az ügynöki keretrendszerek felfedezése](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum a saját nyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->