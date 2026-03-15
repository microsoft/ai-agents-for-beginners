# AI Agentid tootmises: vaatlusvõime & hindamine

[![AI Agentid tootmises](../../../translated_images/et/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kui AI agentid liiguvad eksperimentaalsetest prototüüpidest reaalse maailma rakendusteni, muutub oluliseks mõista nende käitumist, jälgida nende jõudlust ja süsteemselt hinnata nende tulemusi.

## Õpieesmärgid

Pärast selle õppetüki lõpetamist sa tead/saad aru:
- Agentide vaatlusvõime ja hindamise põhikontseptsioonidest
- Tehnikatest agentide jõudluse, kulude ja efektiivsuse parandamiseks
- Mida ja kuidas oma AI agente süsteemselt hinnata
- Kuidas kulusid kontrollida, kui AI agente tootmisse juurutad
- Kuidas instrumendistada Microsoft Agent Frameworkiga loodud agente

Eesmärk on varustada sind teadmistega, et muuta su "must kast" agentidest läbipaistvad, hallatavad ja usaldusväärsed süsteemid.

_**Märkus:** Oluline on juurutada ohutuid ja usaldusväärseid AI agente. Vaata ka õppetükki [Usaldusväärsete AI Agentide Loomine](./06-building-trustworthy-agents/README.md)._

## Jäljed ja ulatused

Vaatlusvahendid nagu [Langfuse](https://langfuse.com/) või [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) esitavad tavaliselt agendi töötlused jälgedena ja ulatustena.

- **Jälg** esindab täielikku agendi ülesannet algusest lõpuni (näiteks kasutaja päringuga tegelemine).
- **Ulatused** on jälje üksikud sammud (näiteks keelemudeli kutsumine või andmete hankimine).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Ilma vaatlusvõimeta võib AI agent tunda end nagu "must kast" – selle sisemine olek ja põhjendus on läbipaistmatud, muutes vigade diagnoosimise või jõudluse optimeerimise keeruliseks. Vaatlusvõimega muutuvad agentideks "klaaskastid", mis pakuvad läbipaistvust, mis on oluline usalduse ülesehitamiseks ja tagamaks, et nad toimivad kavandatult.

## Miks vaatlusvõime tootmiskeskkondades oluline on

AI agentide üleminek tootmiskeskkondadesse toob kaasa uusi väljakutseid ja nõudmisi. Vaatlusvõime ei ole enam "ilus lisafunktsioon", vaid kriitiline võimekus:

*   **Silumine ja põhjuslike vigade analüüs**: Kui agent ebaõnnestub või toodab ootamatut väljundit, annavad vaatlusvahendid vajalikud jäljed vea allika paiknemiseks. See on eriti oluline keerulistes agentides, kus võib olla mitu LLM-i kutsumist, töövahendite interaktsioone ja tingimusloogikat.
*   **Latentsuse ja kulude haldamine**: AI agentid tuginevad sageli LLM-idele ja teistele välistele API-dele, mille eest arve esitatakse märksõnade või kõnede järgi. Vaatlusvõime võimaldab neid kõnesid täpselt jälgida, aidates tuvastada liialt aeglaseid või kulukaid operatsioone. See võimaldab meeskondadel optimeerida prompt'e, valida tõhusamaid mudeleid või ümber kujundada töövooge, et hallata tegevuskulusid ja tagada hea kasutajakogemus.
*   **Usaldus, ohutus ja vastavus**: Paljudes rakendustes on oluline tagada agentide ohutu ja eetiline käitumine. Vaatlusvõime pakub auditijälge agendi toimingute ja otsuste kohta. Seda saab kasutada probleemide nagu prompti süstimine, kahjuliku sisu genereerimine või isikustatud tuvastatavate andmete (PII) väärkasutuse tuvastamiseks ja leevendamiseks. Näiteks võid uurida jälgi, et mõista, miks agent andis konkreetse vastuse või kasutas kindlat tööriista.
*   **Jätkuva täiustamise tsüklid**: Vaatlusandmed on iteratiivse arendusprotsessi alus. Jälgides, kuidas agentid reaalses maailmas toimivad, saavad meeskonnad tuvastada parenduskohti, koguda andmeid mudelite täpsustamiseks ja valideerida muudatuste mõju. See loob tagasiside tsükli, kus tootmiskogemused võrgus toimuvast hindamisest suunavad võrguvälise katsetamise ja täiendamise, viies järjest parema agendi jõudluseni.

## Peamised jälgitavad mõõdikud

Agendi käitumise jälgimiseks ja mõistmiseks tuleks jälgida mitmesuguseid mõõdikuid ja signaale. Kuigi konkreetsed mõõdikud võivad sõltuda agendi eesmärgist, on mõned universaalselt olulised.

Siin on mõned tavalisemad mõõdikud, mida vaatlusvahendid jälgivad:

**Latentsus:** Kui kiiresti agent vastab? Pikad ooteajad mõjutavad kasutajakogemust negatiivselt. Tuleb mõõta latentsust ülesannete ja üksikute sammude kaupa, jälgides agendi toiminguid. Näiteks agent, kes kasutab kõigi mudelikõnede jaoks 20 sekundit, võiks kiirendada kiirema mudeli kasutamise või kõnede paralleelseks käivitamisega.

**Kulud:** Millised on kulud ühe agendi töötamise kohta? AI agentid tuginevad LLM-i kõnedele, mille eest arve esitatakse märksõnade kaupa või välistele API-dele. Sageli tööriistade kasutamine või mitmed promptid võivad kiiresti kulusid tõsta. Näiteks kui agent kutsub LLM-i viis korda vaid marginaalse kvaliteediparanduse nimel, tuleb hinnata, kas kulud on õigustatud või kas kõnede arvu saaks vähendada või odavamat mudelit kasutada. Reaalajas jälgimine võib aidata tuvastada ootamatuid kulukasvude tippe (nt vigade tõttu käimas olevad liialt pikad API-tsüklid).

**Päringute vead:** Kui palju päringuid agent ebaõnnestus täitma? See võib hõlmata API vigu või ebaõnnestunud tööriistakutseid. Tootmises agenti vastupidavamaks muuta saab siis, kui seadistatakse varuplaanid või kordused. Näiteks, kui LLM teenusepakkuja A on maas, lülituda automaatselt üle teenusepakkujale B.

**Kasutajate tagasiside:** Otse kasutajalt saadav hindamine annab väärtuslikku infot. Näiteks selged hinnangud (👍meeldib/👎ei meeldi, ⭐1-5 tärni) või tekstilised kommentaarid. Järjepidev negatiivne tagasiside peaks hoiatama, sest see näitab, et agent ei tööta ootuspäraselt.

**Kaudne kasutajate tagasiside:** Kasutajate käitumine annab kaudset tagasisidet isegi ilma otseste hinnanguteta. Näiteks kohene päringu ümber sõnastamine, korduvad küsimused või proovimisnupu klõpsamine. Näiteks, kui näed, et kasutajad küsivad sama küsimust korduvalt, on see märk, et agent ei tööta ootuspäraselt.

**Täpsus:** Kui sageli agent toodab õigeid või soovitud tulemusi? Täpsuse määratlused erinevad (nt probleemide lahendamise õigsus, infootsingu täpsus, kasutajate rahulolu). Esimene samm on defineerida, mis on su agenti jaoks edukas tulemus. Täpsust saab jälgida automatiseeritud kontrollide, hindamisskooride või ülesande täitmise siltide abil. Näiteks tähistada jäljed kui "õnnestunud" või "ebaõnnestunud".

**Automatiseeritud hindamismõõdikud:** Võid ka seadistada automaatsed hinnangud. Näiteks saad kasutada LLM-i, et anda hinnang agendi väljundile, kas see on abiks, täpne või mitte. On ka mitmeid avatud lähtekoodi raamatukogusid, mis aitavad hinnata erinevaid agendi aspekte. Nt [RAGAS](https://docs.ragas.io/) RAG agentide jaoks või [LLM Guard](https://llm-guard.com/), mis tuvastab kahjulikku keelt või prompti süstimist.

Praktikas annab nende mõõdikute kombineerimine parima ülevaate AI agendi seisundist. Käesoleva peatüki [näidisnotebookis](./code_samples/10-expense_claim-demo.ipynb) näitame, kuidas need mõõdikud reaalses näites välja näevad, aga kõigepealt õpime, milline näeb välja tüüpiline hindamisprotsess.

## Instrumendista oma agent

Jälgimisandmete kogumiseks on vaja instrumendistada oma kood. Eesmärk on lisada agendi koodile sellised vahendid, et saata jälgi ja mõõdikuid, mida vaatlusplatvorm saab koguda, töödelda ja visualiseerida.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) on saanud tööstusharu standardiks LLM-i vaatlusvõime jaoks. See pakub API-sid, SDK-sid ja tööriistu telemeetria andmete genereerimiseks, kogumiseks ja eksportimiseks. 

On palju instrumendistamise raamatukogusid, mis mähivad olemasolevad agentide raamistikud ja lihtsustavad OpenTelemetry ulatuste eksporti vaatlusvahendisse. Microsoft Agent Framework integreerub OpenTelemetryga loomulikult. Järgnevalt on näide MAF agendi instrumendistamisest:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agendi täitmist jälgitakse automaatselt
    pass
```

Selle peatüki [näidisnotebook](./code_samples/10-expense_claim-demo.ipynb) demonstreerib, kuidas instrumendistada oma MAF agent.

**Ulatusede käsitsi loomine:** Kuigi instrumendistamise raamatukogud annavad hea lähtepunkti, on tihti vaja detailsemat või kohandatud infot. Saad ulatusi käsitsi luua, lisades kohandatud rakenduse loogikat. Veelgi olulisem on see, et automaatselt või käsitsi loodud ulatuseid saab täiendada kohandatud atribuutidega (tuntud ka kui sildid või metaandmed). Neisse saab lisada ärispetsiifilisi andmeid, vahepealseid arvutusi või konteksti, mis võib aidata silumisel või analüüsil, näiteks `user_id`, `session_id`, või `model_version`.

Näide jälgede ja ulatuste käsitsi loomisest [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) abil: 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agendi hindamine

Vaatlus annab meile mõõdikud, kuid hindamine on see protsess, kus neid andmeid analüüsitakse (ja testitakse), et teha kindlaks, kui hästi AI agent toimib ja kuidas seda saaks parandada. Teisisõnu, kui sul on need jäljed ja mõõdikud olemas, kuidas sa neid kasutad agendi hindamiseks ja otsuste tegemiseks?

Regulaarne hindamine on oluline, sest AI agentidel on sageli mitte-deterministlik käitumine ja nad võivad areneda (värskenduste või mudelikäitumise nihkumise kaudu) – ilma hindamiseta sa ei tea, kas su "tark agent" tegelikult töötab hästi või on ta halvemaks läinud.

AI agentide hindamisel on kaks kategooriat: **võrguväline hindamine** ja **võrguhindamine**. Mõlemad on väärtuslikud ja täiendavad teineteist. Tavaliselt alustame võrguvälise hindamisega, sest see on minimaalne vajalik samm enne agendi juurutamist.

### Võrguväline hindamine

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

See tähendab agendi hindamist kontrollitud keskkonnas, tavaliselt testandmekogumite abil, mitte reaalsete kasutajapäringute peal. Kasutatakse kureeritud andmekogumeid, kus on teada ootuspärane väljund või korrektne käitumine, ja seejärel käivitatakse agent nende peal.

Näiteks kui sa oled loonud matemaatikaprobleemide agenti, võib sul olla [testandmekogum](https://huggingface.co/datasets/gsm8k) 100 ülesandega, mille vastused on teada. Võrguväline hindamine toimub sageli arenduse ajal (ja võib olla CI/CD torustike osa), et kontrollida paranemisi või kaitsta regressiooni eest. Selle eelis on see, et see on **korduv ja sa saad selged täpsusmõõdikud, sest sul on tõeväärtus olemas**. Võid ka simuleerida kasutajapäringuid ja võrrelda agendi vastuseid ideaalse väljundiga või kasutada automaatseid mõõdikuid nagu eespool kirjeldatud. 

Peamine väljakutse võrguvälises hindamises on tagada, et sinu testandmekogu on põhjalik ja eti jätkusuutlik – agent võib hästi hakkama saada fikseeritud testkogumiga, kuid tootmises võib kohtuda väga erinevate päringutega. Seetõttu peaksid testkogumeid regulaarselt täiendama uute äärejuhtumite ja reaalse maailma stsenaariumit peegeldavate näidetega​. Väike "tuitest" kogum kiireks kontrolliks ja suurem hindamiskogu laialdaseks mõõtmiseks on kasulik: väikesed kogumid kiireteks testideks ja suuremad üldiseks jõudlusanalüüsiks​.

### Võrguhindamine

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

See tähendab agendi hindamist elavas, reaalses keskkonnas, st tegeliku tootmiskasutuse ajal. Võrguhindamine hõlmab agendi jõudluse jälgimist tõeliste kasutajate interaktsioonide peal ja tulemuste pidevat analüüsi.

Näiteks võid jälgida õnnestumise määra, kasutajate rahulolu skoori või muid mõõdikuid reaalajas. Võrguhindamise eelis on see, et see **tabab asju, mida sa pole labsättes ette näinud** – näed mudeli nihkumist aja jooksul (kui agendi efektiivsus langeb sisendi mustrite muutumise tõttu) ja avastad ootamatuid päringuid või olukordi, mida testandmetes polnud​. See annab tõelise ülevaate sellest, kuidas agent metsas käitub.

Võrguhindamine sisaldab sageli nii implitsiitset kui ka eksplitsiitset kasutajate tagasisidet, nagu varem arutatud, ning võib hõlmata varjatud katseid või A/B teste (kus uus agentide versioon töötab paralleelselt vana vastu võrdluseks). Väljakutseks on, et võib olla keeruline saada usaldusväärseid silte või skooringuid elavas keskkonnas – võid sõltuda kasutajate tagasisidest või mõõdikutest allapoole (näiteks kas kasutaja klikib tulemust).

### Mõlema kombineerimine

Võrguhindamine ja võrguväline hindamine ei välista teineteist; need täiustavad üksteist. Võrgujälgimise info (nt uued kasutajapäringute tüübid, kus agent töötab halvasti) aitab täiendada ja parandada võrguväliseid testandmekogumeid. Samas, agentide puhul, kes võrguvälises testis hästi toimivad, saab neid kindlamalt juurutada ja võrgus jälgida.

Tegelikult järgivad paljud meeskonnad tsüklit:

_hinda võrguväliselt -> juuruta -> jälgi võrgus -> kogu uusi ebaõnnestumisi -> lisa võrguvälisesse andmekogusse -> täienda agenti -> korda_.

## Levinud probleemid

AI agentide tootmisse juurutamisel võid kohata erinevaid väljakutseid. Siin on mõned tavalised probleemid ja nende võimalikud lahendused:

| **Probleem**    | **Võimalik lahendus**   |
| ------------- | ------------------ |
| AI agent ei täida ülesandeid järjepidevalt | - Täpsusta agendile antud prompti, ole eesmärkides selge.<br>- Määratle kohad, kus ülesanded saab jaotada alamosadeks ja neid käitada mitme agendi abil. |
| AI agent satub lõpututesse tsüklitesse  | - Määra kindlad lõpetamise tingimused, et agent teaks, millal protsess peatada.<br>- Komplekssed ülesanded, mis vajavad mõtlemist ja planeerimist, proovi lahendada suurema ja spetsialiseerunud mudeliga. |
| AI agendi tööriista kutsed ei tööta korralikult   | - Testi ja valideeri tööriista väljund väljaspool agendi süsteemi.<br>- Täienda määratletud parameetreid, prompt'e ja tööriistade nimetusi.  |
| Multi-agendi süsteem töötab ebaühtlaselt | - Täpsusta iga agendi prompti, et need oleksid spetsiifilised ja teineteisest erinevad.<br>- Loo hierarhiline süsteem, kasutades "marsruutimise" või kontroller-agenti, kes otsustab, milline agent on õige. |

Paljusid neist probleemidest saab efektsemalt tuvastada, kui on paigas vaatlusvõime. Varem arutatud jäljed ja mõõdikud aitavad täpselt kindlaks teha, kus agentide töövoos probleemid tekivad, muutes silumise ja optimeerimise palju tõhusamaks.

## Kulude haldamine
Siin on mõned strateegiad, kuidas hallata AI agentide tootmisse juurutamise kulusid:

**Väiksemate mudelite kasutamine:** Väikesed keelemudelid (SLM-id) võivad teatud agentuursetes juhtumites hästi töötada ning vähendada kulusid märkimisväärselt. Nagu eelnevalt mainitud, on parim viis mõista, kui hästi SLM teie kasutusjuhtumil toimib, ehitada hindamissüsteem, mis määrab ja võrdleb tulemuslikkust suuremate mudelitega. Kaaluge SLM-ide kasutamist lihtsamate ülesannete jaoks nagu kavatsuse klassifitseerimine või parameetrite eraldamine, samal ajal kui keerukate mõtlemiste jaoks reserveerige suuremad mudelid.

**Ruuderi mudeli kasutamine:** Sarnane strateegia on kasutada erinevaid mudeleid ja suurusi. Võite kasutada LLM-i/SLM-i või serverivaba funktsiooni, et suunata päringud keerukuse alusel sobivamate mudelite juurde. See aitab samuti kulusid vähendada ja tagada õige jõudlus õigetel ülesannetel. Näiteks suunake lihtsad päringud väiksemate ja kiirematega mudelite juurde ning keerukate mõtlemist nõudvate ülesannete jaoks kasutage ainult kallimaid suuremaid mudeleid.

**Vastuste vahemällu salvestamine:** Üldiste päringute ja ülesannete tuvastamine ning vastuste pakkumine enne nende läbimist teie agentuursüsteemist on hea viis vähendada sarnaste päringute mahtu. Saate isegi rakendada voogu, mis tuvastab, kui sarnane on päring teie vahemällu salvestatud päringutega, kasutades selleks lihtsemaid AI mudeleid. See strateegia võib märkimisväärselt vähendada kulusid sagedasema küsimuste või tavaliste töövoogude korral.

## Vaatame, kuidas see praktikas töötab

Selles osa [näidismärkmikus](./code_samples/10-expense_claim-demo.ipynb) näeme näiteid, kuidas saame kasutada jälgimisvahendeid oma agendi jälgimiseks ja hindamiseks.

### Kas teil on AI agentide tootmises kohta veel küsimusi?

Liituge [Microsoft Foundry Discordiga](https://aka.ms/ai-agents/discord), et kohtuda teiste õppijatega, osaleda tööaegadel ning saada vastused oma AI agentide küsimustele.

## Eelmine õppetund

[Metakognitsiooni disainimuster](../09-metacognition/README.md)

## Järgmine õppetund

[Agentuursed protokollid](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellekti tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame täpsust, tuleb arvestada, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selles emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tingitud arusaamatuste ega väärarusaamade eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->