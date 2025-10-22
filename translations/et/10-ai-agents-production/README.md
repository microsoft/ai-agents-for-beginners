<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cdfd0acc8592c1af14f8637833450375",
  "translation_date": "2025-10-11T11:13:56+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "et"
}
-->
# AI-agentide kasutamine tootmises: Jälgitavus ja hindamine

[![AI-agentid tootmises](../../../translated_images/lesson-10-thumbnail.2b79a30773db093e0b4fb47aaa618069e0afb4745fad4836526cf51df87f9ac9.et.png)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kui AI-agentid liiguvad eksperimentaalsetest prototüüpidest reaalse maailma rakendustesse, muutub nende käitumise mõistmine, jõudluse jälgimine ja väljundite süstemaatiline hindamine üha olulisemaks.

## Õpieesmärgid

Pärast selle õppetunni läbimist oskad/saad aru:
- Agentide jälgitavuse ja hindamise põhikontseptsioonidest
- Tehnikatest agentide jõudluse, kulude ja tõhususe parandamiseks
- Mida ja kuidas oma AI-agente süstemaatiliselt hinnata
- Kuidas kontrollida kulusid AI-agentide tootmises kasutamisel
- Kuidas instrumenteerida AutoGeniga loodud agente

Eesmärk on anda sulle teadmised, et muuta oma "must kast" agentid läbipaistvateks, hallatavateks ja usaldusväärseteks süsteemideks.

_**Märkus:** Oluline on juurutada AI-agente, mis on turvalised ja usaldusväärsed. Vaata [Usaldusväärsete AI-agentide loomine](./06-building-trustworthy-agents/README.md) õppetundi._

## Jäljed ja lõigud

Jälgitavuse tööriistad, nagu [Langfuse](https://langfuse.com/) või [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), esindavad agentide töövooge tavaliselt jälgede ja lõikudena.

- **Jälg** tähistab täielikku agenti ülesannet algusest lõpuni (näiteks kasutaja päringu käsitlemine).
- **Lõigud** on individuaalsed sammud jälje sees (näiteks keelemudeli kutsumine või andmete hankimine).

![Jälgede puu Langfuses](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Ilma jälgitavuseta võib AI-agent tunduda nagu "must kast" – selle sisemine olek ja põhjendused on läbipaistmatud, mistõttu on raske probleeme diagnoosida või jõudlust optimeerida. Jälgitavusega muutuvad agendid "klaaskastideks", pakkudes läbipaistvust, mis on hädavajalik usalduse loomiseks ja tagamaks, et nad töötavad kavandatud viisil.

## Miks jälgitavus on tootmiskeskkondades oluline

AI-agentide viimine tootmiskeskkondadesse toob kaasa uued väljakutsed ja nõuded. Jälgitavus ei ole enam lihtsalt "hea, kui on", vaid kriitiline võimekus:

*   **Vigade ja algpõhjuste analüüs:** Kui agent ebaõnnestub või annab ootamatu väljundi, pakuvad jälgitavuse tööriistad vajalikke jälgi, et tuvastada vea allikas. See on eriti oluline keerukate agentide puhul, mis võivad hõlmata mitut LLM-i kutset, tööriistade interaktsioone ja tingimuslikku loogikat.
*   **Latentsuse ja kulude haldamine:** AI-agentid tuginevad sageli LLM-idele ja teistele välistele API-dele, mille eest arveldatakse märgi või kutse alusel. Jälgitavus võimaldab täpselt jälgida neid kutseid, aidates tuvastada operatsioone, mis on liialt aeglased või kallid. See võimaldab meeskondadel optimeerida juhiseid, valida tõhusamaid mudeleid või ümber kujundada töövooge, et hallata tegevuskulusid ja tagada hea kasutajakogemus.
*   **Usaldus, turvalisus ja vastavus:** Paljudes rakendustes on oluline tagada, et agendid käituksid turvaliselt ja eetiliselt. Jälgitavus pakub agentide tegevuste ja otsuste auditeerimisjälge. Seda saab kasutada probleemide, nagu juhiste süstimine, kahjuliku sisu genereerimine või isikuandmete väärkasutamine, tuvastamiseks ja leevendamiseks. Näiteks saate jälgi üle vaadata, et mõista, miks agent andis teatud vastuse või kasutas konkreetset tööriista.
*   **Pideva täiustamise tsüklid:** Jälgitavuse andmed on iteratiivse arendusprotsessi alus. Jälgides, kuidas agendid päriselus toimivad, saavad meeskonnad tuvastada parendamisvaldkondi, koguda andmeid mudelite peenhäälestamiseks ja valideerida muudatuste mõju. See loob tagasiside tsükli, kus tootmise ülevaated veebipõhisest hindamisest informeerivad offline-eksperimente ja täiustusi, viies järk-järgult parema agentide jõudluseni.

## Olulised mõõdikud jälgimiseks

Agentide käitumise jälgimiseks ja mõistmiseks tuleks jälgida mitmesuguseid mõõdikuid ja signaale. Kuigi konkreetsed mõõdikud võivad varieeruda sõltuvalt agendi eesmärgist, on mõned universaalselt olulised.

Siin on mõned kõige levinumad mõõdikud, mida jälgitavuse tööriistad jälgivad:

**Latentsus:** Kui kiiresti agent reageerib? Pikad ooteajad mõjutavad kasutajakogemust negatiivselt. Latentsust tuleks mõõta nii ülesannete kui ka individuaalsete sammude puhul, jälgides agentide töövooge. Näiteks agent, kes kulutab kõigile mudelikutsetele 20 sekundit, võiks kiirendada, kasutades kiiremat mudelit või käivitades mudelikutsed paralleelselt.

**Kulud:** Milline on kulu agendi töövoo kohta? AI-agentid tuginevad LLM-kutsetele, mille eest arveldatakse märgi alusel, või välistele API-dele. Sagedane tööriistade kasutamine või mitmed juhised võivad kulud kiiresti tõsta. Näiteks kui agent kutsub LLM-i viis korda marginaalse kvaliteedi parandamiseks, tuleb hinnata, kas kulu on õigustatud või kas kutsete arvu saab vähendada või kasutada odavamat mudelit. Reaalajas jälgimine aitab tuvastada ka ootamatuid kulutõuse (nt vead, mis põhjustavad liigseid API-tsükleid).

**Päringute vead:** Kui palju päringuid agent ebaõnnestus? See võib hõlmata API-vigu või ebaõnnestunud tööriistakutseid. Agendi tootmises vastupidavamaks muutmiseks saate seadistada varuplaanid või korduskatsed. Näiteks kui LLM-i pakkuja A on maas, lülitute varuplaanina LLM-i pakkujale B.

**Kasutajate tagasiside:** Otsene kasutajate hindamine annab väärtuslikku teavet. See võib hõlmata selgeid hinnanguid (👍pöidlad üles/👎alla, ⭐1-5 tärni) või tekstilisi kommentaare. Pidev negatiivne tagasiside peaks teid hoiatama, kuna see viitab sellele, et agent ei tööta ootuspäraselt.

**Kaudne kasutajate tagasiside:** Kasutajate käitumine annab kaudset tagasisidet isegi ilma selgete hinnanguteta. See võib hõlmata kohest küsimuse ümber sõnastamist, korduvaid päringuid või nupule "proovi uuesti" klõpsamist. Näiteks kui näete, et kasutajad küsivad korduvalt sama küsimust, on see märk, et agent ei tööta ootuspäraselt.

**Täpsus:** Kui sageli agent genereerib õigeid või soovitud väljundeid? Täpsuse määratlused varieeruvad (nt probleemide lahendamise korrektsus, teabe hankimise täpsus, kasutajate rahulolu). Esimene samm on määratleda, milline edu agendi jaoks välja näeb. Täpsust saab jälgida automatiseeritud kontrollide, hindamisskooride või ülesannete lõpetamise siltide kaudu. Näiteks jälgede märkimine kui "õnnestunud" või "ebaõnnestunud".

**Automatiseeritud hindamismõõdikud:** Võite seadistada ka automatiseeritud hindamisi. Näiteks saate kasutada LLM-i, et hinnata agendi väljundit, nt kas see on kasulik, täpne või mitte. Samuti on mitmeid avatud lähtekoodiga teeke, mis aitavad hinnata agendi erinevaid aspekte. Näiteks [RAGAS](https://docs.ragas.io/) RAG-agentide jaoks või [LLM Guard](https://llm-guard.com/) kahjuliku keele või juhiste süstimise tuvastamiseks.

Praktikas annab nende mõõdikute kombinatsioon parima ülevaate AI-agendi tervisest. Selle peatüki [näidispäevikus](./code_samples/10_autogen_evaluation.ipynb) näitame, kuidas need mõõdikud näevad välja reaalsetes näidetes, kuid kõigepealt õpime, kuidas tüüpiline hindamisvoog välja näeb.

## Instrumenteerige oma agent

Jälgimisandmete kogumiseks peate oma koodi instrumenteerima. Eesmärk on instrumenteerida agendi kood nii, et see edastaks jälgi ja mõõdikuid, mida jälgitavuse platvorm saab koguda, töödelda ja visualiseerida.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) on kujunenud tööstusstandardiks LLM-i jälgitavuse jaoks. See pakub API-de, SDK-de ja tööriistade komplekti telemeetriaandmete genereerimiseks, kogumiseks ja eksportimiseks.

On palju instrumenteerimise teeke, mis pakuvad olemasolevatele agendiraamistikele mähiseid ja muudavad OpenTelemetry lõikude eksportimise jälgitavuse tööriistale lihtsaks. Allpool on näide AutoGen-agendi instrumenteerimisest [OpenLit instrumenteerimise teegiga](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

Selle peatüki [näidispäevik](./code_samples/10_autogen_evaluation.ipynb) demonstreerib, kuidas instrumenteerida oma AutoGen-agent.

**Manuaalne lõikude loomine:** Kuigi instrumenteerimise teegid pakuvad head alust, on sageli juhtumeid, kus on vaja üksikasjalikumat või kohandatud teavet. Lõike saab käsitsi luua, et lisada kohandatud rakendusloogikat. Veelgi olulisem on see, et automaatselt või käsitsi loodud lõike saab rikastada kohandatud atribuutidega (tuntud ka kui sildid või metaandmed). Need atribuudid võivad hõlmata ärispetsiifilisi andmeid, vahepealseid arvutusi või konteksti, mis võib olla kasulik silumiseks või analüüsiks, näiteks `user_id`, `session_id` või `model_version`.

Näide jälgede ja lõikude käsitsi loomisest [Langfuse Python SDK-ga](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agendi hindamine

Jälgitavus annab meile mõõdikud, kuid hindamine on protsess, kus neid andmeid analüüsitakse (ja teste tehakse), et määrata, kui hästi AI-agent toimib ja kuidas seda saab parandada. Teisisõnu, kui teil on need jäljed ja mõõdikud, kuidas neid kasutada agendi hindamiseks ja otsuste tegemiseks?

Regulaarne hindamine on oluline, kuna AI-agentid on sageli mitte-deterministlikud ja võivad areneda (läbi uuenduste või mudeli käitumise muutumise) – ilma hindamiseta ei tea, kas teie "nutikas agent" teeb tegelikult oma tööd hästi või on ta halvenenud.

AI-agentide hindamiseks on kaks kategooriat: **veebipõhine hindamine** ja **offline-hindamine**. Mõlemad on väärtuslikud ja täiendavad teineteist. Tavaliselt alustame offline-hindamisest, kuna see on minimaalne vajalik samm enne agendi juurutamist.

### Offline-hindamine

![Andmekogumi üksused Langfuses](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

See hõlmab agendi hindamist kontrollitud keskkonnas, tavaliselt testandmekogumite abil, mitte reaalajas kasutajapäringutega. Kasutatakse kureeritud andmekogumeid, kus teate, milline on oodatav väljund või õige käitumine, ja seejärel käivitate agendi nende peal.

Näiteks kui olete loonud matemaatiliste sõnaprobleemide agendi, võib teil olla [testandmekogum](https://huggingface.co/datasets/gsm8k) 100 probleemiga, mille vastused on teada. Offline-hindamist tehakse sageli arenduse ajal (ja see võib olla osa CI/CD torujuhtmetest), et kontrollida täiustusi või kaitsta regressioonide eest. Eeliseks on see, et see on **korduv ja saate selged täpsusmõõdikud, kuna teil on tõeandmed**. Võite simuleerida ka kasutajapäringuid ja mõõta agendi vastuseid ideaalsete vastuste vastu või kasutada automatiseeritud mõõdikuid, nagu eespool kirjeldatud.

Offline-hindamise peamine väljakutse on tagada, et teie testandmekogum oleks terviklik ja jääks asjakohaseks – agent võib fikseeritud testikomplektis hästi toimida, kuid tootmises kohtab väga erinevaid päringuid. Seetõttu peaksite testikomplekte värskendama uute erandjuhtumite ja näidetega, mis kajastavad reaalseid stsenaariume​. Kasulik on kasutada väikeste "kiirtestide" juhtumite ja suuremate hindamiskomplektide segu: väikesed komplektid kiireks kontrolliks ja suuremad laiemate jõudlusmõõdikute jaoks​.

### Veebipõhine hindamine

![Jälgitavuse mõõdikute ülevaade](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

See viitab agendi hindamisele reaalajas, reaalses keskkonnas, st tootmises tegeliku kasutamise ajal. Veebipõhine hindamine hõlmab agendi jõudluse jälgimist reaalsete kasutajate interaktsioonide põhjal ja tulemuste pidevat analüüsi.

Näiteks võite jälgida edukuse määrasid, kasutajate rahulolu skoori või muid mõõdikuid reaalajas liikluse põhjal. Veebipõhise hindamise eeliseks on see, et see **püüab kinni asju, mida te laborikeskkonnas ei pruugi ette näha** – saate jälgida mudeli triivimist aja jooksul (kui agendi tõhusus halveneb sisendmustrite muutumisel) ja tuvastada ootamatuid päringuid või olukordi, mida teie testandmetes ei olnud​. See annab tõese pildi sellest, kuidas agent metsikus looduses käitub.

Veebipõhine hindamine hõlmab sageli kaudse ja otsese kasutajate tagasiside kogumist, nagu eespool arutatud, ning võimalusel varjuteste või A/B-testide läbiviimist (kus agendi uus versioon töötab paralleelselt vana versiooniga võrdlemiseks). Väljakutseks on see, et reaalajas interaktsioonide jaoks usaldusväärsete siltide või skooride saamine võib olla keeruline – võite tugineda kasutajate tagasisidele või allavoolu mõõdikutele (näiteks kas kasutaja klõpsas tulemusel).

### Kahe kombineerimine

Veebipõhine ja offline-hindamine ei ole vastastikku välistavad; need täiendavad teineteist suurepäraselt. Veebipõhise jälgimise ülevaated (nt uued kasutajapäringute tüübid, kus agent halvasti toimib) saab kasutada offline-testandmekogumite täiendamiseks ja parandamiseks. Vastupidi, agendid, kes offline-testides hästi toimivad, saab seejärel enesekindlamalt juurutada ja veebis jälgida.

Tegelikult kasutavad paljud meeskonnad tsüklit:

_hinda offline -> juuruta -> jälgi veebis -> kogu uusi ebaõnnestumisi -> lisa offline-andmekogumisse -> täiusta agenti -> korda_.

## Levinud probleemid

AI-agentide tootmises juurutamisel võite kohata mitmesuguseid väljakutseid. Siin on mõned levinud probleemid ja nende võimalikud lahendused:

| **Probleem**    | **Võimalik lahendus**   |
| ------------- | ------------------ |
| AI-agent ei täida ülesandeid järjekindlalt | - Täpsusta agendile antud juhiseid; ole eesmärkides selge.<br>- Tuvasta, kus ülesannete jagamine alamülesanneteks ja nende käsitlemine mitme agendi poolt võib aidata. |
| AI-agent satub pidevatesse tsüklitesse  | - Veendu, et sul oleksid selged lõpetamise tingimused, et agent teaks, millal protsess lõpetada.<br>- Keerukate ülesannete puhul, mis nõuavad põhjendamist ja planeerimist, kasuta suuremat mudelit, mis on spetsialiseerunud põhjendamisülesannetele. |
| AI-agendi tööriistakutsed ei toimi hästi   | - Testi ja valideeri tööriista väljund
Siin on mõned strateegiad, kuidas hallata AI agentide tootmisesse juurutamise kulusid:

**Väiksemate mudelite kasutamine:** Väikesed keelemudelid (SLM-id) võivad teatud agentlike kasutusjuhtude puhul hästi toimida ja kulusid oluliselt vähendada. Nagu varem mainitud, on parim viis mõista, kui hästi SLM teie kasutusjuhtumi puhul toimib, luua hindamissüsteem, et määrata ja võrrelda nende jõudlust suuremate mudelitega. Kaaluge SLM-ide kasutamist lihtsamate ülesannete jaoks, nagu kavatsuste klassifitseerimine või parameetrite eraldamine, ning jätke suuremad mudelid keerukamate mõtlemisülesannete jaoks.

**Routingu mudeli kasutamine:** Sarnane strateegia on kasutada erinevaid mudeleid ja suurusi. Võite kasutada LLM/SLM-i või serverivaba funktsiooni, et suunata päringud keerukuse alusel sobivaimatele mudelitele. See aitab samuti kulusid vähendada, tagades samal ajal õige ülesande jaoks sobiva jõudluse. Näiteks suunake lihtsad päringud väiksematele ja kiirematele mudelitele ning kasutage kallimaid suuri mudeleid ainult keerukate mõtlemisülesannete jaoks.

**Vastuste vahemällu salvestamine:** Tavaliste päringute ja ülesannete tuvastamine ning vastuste pakkumine enne, kui need jõuavad teie agentlikku süsteemi, on hea viis sarnaste päringute mahu vähendamiseks. Võite isegi rakendada voogu, et tuvastada, kui sarnane päring on teie vahemällu salvestatud päringutega, kasutades lihtsamaid AI-mudeleid. See strateegia võib märkimisväärselt vähendada kulusid korduma kippuvate küsimuste või tavapäraste töövoogude puhul.

## Vaatame, kuidas see praktikas toimib

Selle jaotise [näidispäevikus](./code_samples/10_autogen_evaluation.ipynb) näeme näiteid, kuidas kasutada jälgitavuse tööriistu oma agendi jälgimiseks ja hindamiseks.

### Kas teil on rohkem küsimusi AI agentide tootmisesse viimise kohta?

Liituge [Azure AI Foundry Discordiga](https://aka.ms/ai-agents/discord), et kohtuda teiste õppijatega, osaleda vastuvõtutundides ja saada vastuseid oma AI agentide küsimustele.

## Eelmine õppetund

[Metakognitsiooni disainimuster](../09-metacognition/README.md)

## Järgmine õppetund

[Agentlikud protokollid](../11-agentic-protocols/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.