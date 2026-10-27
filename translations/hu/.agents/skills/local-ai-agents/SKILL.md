---
name: local-ai-agents
license: MIT
---
# Helyi MI ügynökök létrehozása Foundry Local és Qwen segítségével

> Kísérő készség a [17. Lecke – Helyi MI ügynökök létrehozása](../../../17-creating-local-ai-agents/README.md) számára.
> Használd arra, hogy segíts egy tanulónak olyan ügynököt építeni, amely önállóan gondolkodik, eszközöket hív meg, és dokumentációt keres
> teljes egészében a saját gépén – felhő alapú számítás nélkül. Minden
> ajánlást a lecke tartalmára és a futtatható jegyzetfüzetre alapozz.

## Aktiválási feltételek

Aktiváld ezt a készséget, ha a tanuló:
- Teljes mértékben **helyi eszközön** szeretne futtatni egy ügynököt adatvédelem, költség vagy offline működés miatt.
- Modellje helyben szeretne szolgáltatni **Foundry Local** segítségével, és az OpenAI-kompatibilis végponton keresztül csatlakozni.
- Megbízható helyi eszközmeghíváshoz **Qwen függvénymodellezést** szeretne használni.
- **Helyi RAG**-et (Chroma) vagy **helyi MCP szervert** szeretne hozzáadni.
- Hibrid helyi/felhő alapú irányítási stratégiát kíván tervezni.

## Alapvető gondolati modell

Egy SLM az adatvédelmet, költséget és offline működést preferálja a szélesség helyett. A nyerő
stratégia: **hagyd, hogy az SLM szervezzen, az eszközök pedig végezzék a nehéz munkát.** A
modellnek nem kell *ismernie* a kódot – csak azt kell tudnia, mikor hívja meg a
`read_file` és `search_docs`-et. Ez egy olyan terület, ahol egy SLM erős (korlátozott döntések,
például eszközválasztás), és elkerüli a gyengeségét (széleskörű tudás, hosszú többlépéses
érvelés).

## Miért ezek az elemek

- A **Foundry Local** egy **OpenAI-kompatibilis HTTP végpontot** biztosít, így a felhő alapú ügynökkód csak az `base_url` megváltoztatásával helyben is futtatható (helyi helyettesítő API kulccsal). Automatikusan kiválasztja a géphez legjobb buildet (CPU/GPU/NPU).
- A **Qwen** modelleket függvényhívásra képezték ki, és következetesen jól formált eszközmeghívásokat generálnak – ez az, ami a helyi *chat* modellt helyi *ügynökké* alakítja.
- A **Chroma** processzben fut, és vektorokat tárol lemezen, így az egész RAG folyamat (beágyazás → tárolás → lekérdezés → érvelés) helyben marad.
- Az **MCP** egy szállítási protokoll, nem felhőszolgáltatás: egy MCP szerver helyben futtatható `stdio` felett.

## Beállítás alapjai

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # local placeholder
```

Körülbelül 8 GB RAM reális minimum; GPU/NPU segít, de nem kötelező.

## Fontos minták újraalkotása

Mutasd meg a tanulónak a jegyzetfüzetet
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Sandboxolt eszközök**: minden fájeszköz feloldja az útvonalakat, és elutasít mindent, ami nem egyetlen projekt gyökerén belül van – még helyben is, az eszköz a felhasználói jogosultságokkal fut.
- **Eszközhívási ciklus**: regisztrálni kell az eszközöket az OpenAI eszközsémájába, futtatni a kért eszközöket helyben, visszatáplálni az eredményeket, és ismételni, amíg végleges válasz nem készül.
- **Helyi RAG**: dokumentumokat felvenni egy Chroma gyűjteménybe; `search_docs` a legjobb k darabot adja vissza.
- **Helyi MCP**: csatlakozz egy helyi szerverhez `stdio` felett; köss hozzá egy projekt könyvtárat és érvényesítsd az eredményeket.

## Hibrid útválasztás (helyi, mint az egyik modell)

| Helyzet | Hol fut |
|-----------|---------------|
| Érzékeny adat / offline | Helyi SLM |
| Egyszerű, korlátozott feladat | Helyi SLM (olcsó, gyors) |
| Nehéz többlépéses érvelés nem érzékeny adaton | Felhő modell |
| Felhő kiesés | Helyi SLM (zökkenőmentes leépülés) |

Ez tükrözi a modellirányítás ötletét a 16. leckéből, a munkaállomással egy az útvonalak között. Részesítsd előnyben azokat a terveket, amelyek visszatérnek a helyi megoldáshoz, így az ügynök minősége csökken, ahelyett hogy teljesen meghiúsulna.



## Biztonsági intézkedések a segédhez

- Minden fájl/eszköz műveletet egy sandboxolt projektkönyvtárra korlátozz.
- Ne küldj kódot vagy adatot a felhőbe, ha a tanuló adatvédelmi vagy offline célt jelölt meg – az egész folyamatot helyben tartsd.
- Állíts be reális elvárásokat az SLM minőségével kapcsolatban; inkább az eszközökre és a RAG-re támaszkodj, ne a modell memorizált tudására.
- Figyeld meg, hogy a 17. leckének **nincs** Foundry Responses végpontja, így a felhős gyors teszt nem alkalmazható – a validálást helyi futtatással végezd.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->