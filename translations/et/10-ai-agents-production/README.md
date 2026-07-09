# AI-agendid tootmises: jälgitavus ja hindamine

[![AI Agents in Production](../../../translated_images/et/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kui AI-agendid liiguvad katsetest reaalmaailma rakendustesse, muutub oluliseks nende käitumise mõistmine, nende toimivuse jälgimine ja väljundite süsteemne hindamine.

## Õpieesmärgid

Selle peatüki lõpetamisel tead ja mõistad:
- Agendi jälgitavuse ja hindamise põhimõisteid
- Meetodeid agendi toimivuse, kulude ja efektiivsuse parandamiseks
- Kuidas süsteemselt hinnata oma AI-agente
- Kuidas kontrollida kulusid AI-agendi tootmiskeskkonda juurutamisel
- Kuidas instrumendata agenti, mis on loodud Microsoft Agent Frameworkiga

Eesmärk on anda sulle teadmised, et muuta sinu "mustad kastid" läbipaistvateks, hallatavateks ja usaldusväärseteks süsteemideks.

_**Märkus:** Oluline on juurutada ohutuid ja usaldusväärseid AI-agente. Vaata ka [Usaldusväärsete AI-agendide loomise](../06-building-trustworthy-agents/README.md) peatükki._

## Jäljed ja ajendid

Jälgitavustööriistad nagu [Langfuse](https://langfuse.com/) või [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) kujutavad agendi täitmisi tavaliselt jälgede ja ajenditena.

- **Jälg** esindab agendi ülesande koguulatuslikku täitmist algusest lõpuni (näiteks kasutajapäringu töötlemine).
- **Ajendid** on jälje üksikud sammud (näiteks keelemudeli välja kutsumine või andmete pärimine).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Ilma jälgitavuseta võib AI-agent tunduda kui "must kast" – tema sisemine olek ja argumentatsioon on läbipaistmatud, mis teeb vigade diagnoosimise ja jõudluse optimeerimise keeruliseks. Jälgitavusega muutuvad agendid "klaaskastideks", pakkudes läbipaistvust, mis on usalduse ehitamiseks ja oluliste protsesside toimimiseks hädavajalik.

## Miks jälgitavus tootmiskeskkonnas oluline on

AI-agentide üleminek tootmiskeskkondadesse toob kaasa uued väljakutsed ja nõudmised. Jälgitavus ei ole enam "mugavusfunktsioon", vaid kriitiline võimekus:

*   **Tõrkeotsing ja põhjuse analüüs**: Kui agent ebaõnnestub või annab ootamatu tulemuse, annavad jälgitavuse tööriistad vajaliku jälje vea allika täpseks tuvastamiseks. See on eriti oluline keerukate agentide puhul, mis võivad hõlmata mitut LLM-kõnet, tööriistade interaktsioone ja tingimusloogikat.
*   **Latentsus ja kulude juhtimine**: AI-agendid sõltuvad sageli LLM-idest ja teistest välis-API-dest, mille eest arvestatakse tasu märgi või kõne pealt. Jälgitavus võimaldab täpselt jälgida neid kõnesid, aidates tuvastada ülemäära aeglasi või kulukaid operatsioone. See võimaldab meeskondadel optimeerida prompt'e, valida tõhusamaid mudeleid või kujundada töövoogusid ümber, et hallata tegevuskulusid ja tagada hea kasutajakogemus.
*   **Usaldus, ohutus ja vastavus**: Paljudes rakendustes on oluline tagada agentide ohutu ja eetiline käitumine. Jälgitavus annab ülevaate agendi tegevustest ja otsustest auditijälje kujul. Seda saab kasutada selliste probleemide tuvastamiseks ja leevendamiseks nagu prompti manipuleerimine, kahjuliku sisu genereerimine või isikuandmete väärkasutus. Näiteks võid jälgi vaadates mõista, miks agent andis teatud vastuse või kasutas kindlat tööriista.
*   **Pideva täiustamise tsüklid**: Jälgitavuse andmed on iteratiivse arendusprotsessi alus. Jälgides agentide toimivust reaalajas, saab meeskond tuvastada parendusvaldkondi, koguda andmeid mudelite täpsustamiseks ja kinnitada muudatuste mõju. See loob tagasisidega tsükli, kus tootmisandmed veebipõhisest hindamisest suunavad offline katseid ja täiustamist, viies järk-järgult parema agendi toimivuseni.

## Peamised jälgitavad mõõdikud

Agendi käitumise jälgimiseks ja mõistmiseks tuleks jälgida mitmesuguseid mõõdikuid ja signaale. Kuigi konkreetsetel mõõdikutel võib olenevalt agendi eesmärgist varieeruda, on mõned üldiselt olulised.

Siin on mõned kõige tavalisemad mõõdikud, mida jälgitavuse tööriistad kontrollivad:

**Latentsus:** Kui kiiresti agent reageerib? Pikad ootamisajad mõjuvad kasutajakogemusele negatiivselt. Tuleb mõõta latentsust ülesannete ja üksikute sammude kaupa, jälgides agendi täitmisi. Näiteks agent, kes kasutab kõigi mudelikõnede jaoks 20 sekundit, võiks kiirendada, kasutades kiiremat mudelit või astudes kõned paralleelselt.

**Kulud:** Kui palju maksab ühe agendi töö käivitamine? AI-agendid sõltuvad LLM-kõnedest, mida arvestatakse märgi või API-kõne hinnaga. Sageli kasutatavad tööriistad või mitu prompt'i võivad kulusid kiiresti suurendada. Näiteks, kui agent teeb LLM-ile viis kõnet marginaalse kvaliteedi paranduse nimel, tuleks hinnata, kas see kulu on õigustatud või kas kõnede arvu saab vähendada või kasutada odavamat mudelit. Reaalaegne jälgimine aitab tuvastada ka ootamatuid kulutõuse (nt vigade tõttu tekkinud liigsed API-kõned).

**Päringuvead:** Kui palju päringuid ebaõnnestus agentil? Sellesse võivad kuuluda API-vead või tööriistade kõnede ebaõnnestumised. Et muuta agent tootmises robustsemaks, saab seadistada tagavaramehhanisme või taaskäivitusi. Näiteks kui LLM-teenusepakkuja A on maas, lülitud varuvariandina üle LLM-teenusepakkuja B peale.

**Kasutajate tagasiside:** Otsese kasutajahinnangu rakendamine annab väärtuslikku teavet. See võib olla tekstiline hinnang (👍heakskiit/👎hinnangu langetamine, ⭐1-5 tärni) või kirjeldavad kommentaarid. Järjepidev negatiivne tagasiside peaks sind hoiatama, sest see näitab, et agent ei tööta ootuspäraselt.

**Kaudne kasutajate tagasiside:** Kasutajate käitumine annab kaudset tagasisidet isegi ilma otseste hinnanguteta. See võib hõlmata kohest küsimuse ümbervormistamist, korduvaid päringuid või nupu "proovi uuesti" klikkimist. Näiteks kui kasutajad kordavad sama küsimust, on see märk, et agent ei tööta ootuspäraselt.

**Täpsus:** Kui tihti agent genereerib täpseid või sobivaid väljundeid? Täpsuse defineerimine varieerub (nt õige lahenduse leidmine, infootsingu täpsus, kasutajate rahulolu). Esimene samm on määratleda, milline edu sinu agendile tähendab. Täpsust saab jälgida automatiseeritud kontrollide, hindamisskooride või ülesande täitmise märkide kaudu. Näiteks jälgede märkimine kui "õnnestunud" või "ebaõnnestunud".

**Automatiseeritud hindamismõõdikud:** Võid seadistada ka automatiseeritud hinnanguid. Näiteks võid kasutada LLM-i, et hinnata agendi väljundit selle kohta, kas see on kasulik, täpne või mitte. Samuti on mitmeid avatud lähtekoodiga raamatukogusid, mis aitavad hinnata erinevaid agendi aspekte. Näiteks [RAGAS](https://docs.ragas.io/) RAG agentide jaoks või [LLM Guard](https://llm-guard.com/), mis aitab tuvastada kahjulikku keelekasutust või prompti süstimist.

Praktikas annab nende mõõdikute kombinatsioon parima ülevaate AI-agendi tervisest. Selle peatüki [näidisnotoobis](./code_samples/10-expense_claim-demo.ipynb) näitame, kuidas need mõõdikud reaalses näites välja näevad, kuid kõigepealt õpime tüüpilise hindamisprotsessi.

## Instrumendi lisamine agenti

Jäljeandmete kogumiseks tuleb kood instrumendata. Eesmärk on instrumendata agendi kood nii, et saadaks jälgi ja mõõdikuid, mida suudab jälgitavuse platvorm koguda, töödelda ja visualiseerida.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) on kujunenud LLM-i jälgitavuse tööstusstandardiks. See pakub komplekti API-sid, SDK-sid ja tööriistu telemeetriandmete genereerimiseks, kogumiseks ja ekspordiks.

On palju instrumendiraamatukogusid, mis ümbritsevad olemasolevaid agendifraeworke ja võimaldavad OpenTelemetry ajendite lihtsat eksporti jälgitavuse tööriista. Microsoft Agent Framework on OpenTelemetry-ga loomulikult integreeritud. Järgnevalt on näide MAF agendi instrumendamisest:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agendi täitmist jälgitakse automaatselt
    pass
```

Selle peatüki [näidisnotoobis](./code_samples/10-expense_claim-demo.ipynb) demonstreeritakse, kuidas instrumendata oma MAF agent.

**Ajendite käsitsi loomine:** Kuigi instrumendiraamatukogud annavad hea alguspunkti, on sageli juhtumeid, kus on vaja detailsemat või kohandatud teavet. Sa võid käsitsi luua ajendeid, et lisada kohandatud rakendusloogikat. Olulisem on see, et saad automaatselt või käsitsi loodud ajendeid täiendada kohandatud atribuutidega (tuntud ka kui sildid või metaandmed). Need atribuudid võivad sisaldada ärispetsiifilisi andmeid, vahelistöötlusi või mis tahes konteksti, mis võiks olla abiks tõrkeotsingul või analüüsil, näiteks `user_id`, `session_id` või `model_version`.

Näide jälgede ja ajendite käsitsi loomise kohta [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) abil:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agendi hindamine

Jälgitavus annab meile mõõdikud, kuid hindamine on see protsess, kus neid andmeid analüüsitakse (ja teste tehakse), et hinnata AI-agendi toimivust ja selle võimalikku parendamist. Teisisõnu, kui sul on need jäljed ja mõõdikud olemas, kuidas sa neid kasutad agendi hindamiseks ja otsuste tegemiseks?

Regulaarne hindamine on oluline, sest AI-agendid on sageli mittemääratletud ja võivad areneda (uuenduste või mudelikäitumise nihkega) – ilma hindamiseta ei tea sa, kas sinu "tark agent" teeb oma tööd hästi või on ta tahapoole läinud.

AI-agendide hindamine jaguneb kaheks kategooriaks: **veebipõhine hindamine** ja **võrgust väljas hindamine**. Mõlemad on väärtuslikud ja täiendavad teineteist. Tavaliselt alustame võrguvälist hindamist, kuna see on minimaalne vajalik samm enne agendi juurutamist.

### Võrguväline hindamine

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

See hõlmab agendi hindamist kontrollitud keskkonnas, tavaliselt testandmete hulga põhjal, mitte otsepäringutega kasutajatelt. Kasutatakse kureeritud andmekogumeid, kus on teada ootuspärane tulemus või õige käitumine, ja käivitatakse agent nende peal.

Näiteks kui sa ehitasid matemaatika sõnaprobleemide lahendaja agendi, võib sul olla [testandmekogu](https://huggingface.co/datasets/gsm8k) 100 probleemiga, kus on teada vastused. Võrguvälist hindamist tehakse sageli arenduse käigus (võib olla osa CI/CD torustikest), et kontrollida parendusi või takistada regressioone. Kasu on selles, et see on **korduv ja seal saab selgeid täpsuse mõõdikuid tänu tõele vastavusele**. Võid ka simuleerida kasutajapäringuid ja mõõta agendi vastuseid ideaalse vastusega või kasutada eespool kirjeldatud automatiseeritud mõõdikuid.

Võrguvälise hindamise peamine väljakutse on tagada, et testandmestik oleks põhjalik ja püsiks asjakohane – agent võib hästi toimida fikseeritud testkategoorias, kuid tootmises tuleb ta kokku hoopis erinevate päringutega. Seepärast peaksid hoida testandmed ajakohastatuna uute äärejuhtumite ja reaalsete stsenaariumite näidetega. Väikesed „suitsutestid“ ja suuremad hindamisandmekogumid on kasulik segu: väikesed kiireks kontrolliks ja suured laiemate soorituse mõõdikute saamiseks.

### Veebipõhine hindamine

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

See tähendab agendi hindamist elavas reaalmaailma keskkonnas, st tootmises toimival kasutamisel. Veebipõhine hindamine hõlmab agendi soorituse pidevat jälgimist reaalse kasutajate kogemuse põhjal ja tulemuste analüüsi.

Näiteks võid jälgida eduprotsente, kasutajate rahulolu skoori või muid mõõdikuid otse kasutajakogemuse pealt. Veebipõhise hindamise eelis on see, et see **tabab asju, mida laboris ei pruugi ette näha** – saab jälgida mudeli nihkumist aja jooksul (kui agendi efektiivsus väheneb sisendmustrite muutudes) ja tabada ootamatuid päringuid või olukordi, mida sinu testandmed ei hõlmanud. See annab tõelise pildi, kuidas agent metsikus keskkonnas käitub.

Veebipõhine hindamine hõlmab sageli nii kaudset kui otsest kasutajate tagasisidet ja võib kaasata varjuteste või A/B-teste (kus uus agentide versioon töötab paralleelselt, et võrrelda vana versiooniga). Probleemiks on tihti usaldusväärsete siltide või skooride saamine elavate interaktsioonide kohta – selleks võidakse toetuda kasutajate tagasisidele või järeltulevatele mõõdikutele (nt kas kasutaja klikkas tulemuse peal).

### Kahe hindamismeetodi kombineerimine

Veebipõhised ja võrguvälised hindamised ei ole teineteist välistavad, vaid täiendavad suurepäraselt üksteist. Veebipõhise jälgimise kaudu saadud teadmised (nt uued kasutajapäringu tüübid, kus agent ei toimi hästi) aitavad täiendada ja parandada võrguväliseid testandmeid. Vastupidi, võrguvälisel hindamisel hästi toimivad agendid saab seejärel kindluse tundega veebis juurutada ja jälgida.

Paljud meeskonnad kasutavad tegelikult tsüklit:

_hindamine võrguvälises keskkonnas -> juurutamine -> veebipõhine jälgimine -> uute tõrkejuhtumite kogumine -> lisamine võrguvälisesse andmestikku -> agendi täpsustamine -> kordamine_.

## Levinud probleemid

AI-agentide tootmisse juurutamisel võid kokku puutuda mitmesuguste väljakutsetega. Siin on mõned levinumad probleemid ja nende võimalikud lahendused:

| **Probleem**    | **Võimalik lahendus**   |
| ------------- | ------------------ |
| AI-agent ei täida ülesandeid järjepidevalt | - Täienda AI-agendile antavat prompti; ole eesmärkides selge.<br>- Tuvasta, kas ülesande jagamine osadeks ja seejärel mitme agendi abi kasutamine aitab. |
| AI-agent satub lõpututesse tsüklitesse  | - Tagada selged lõpetamise tingimused, et agent teaks, millal protsess peatada.<br>- Keeruliste ülesannete puhul, mis nõuavad arutlemist ja planeerimist, kasuta suuremat spetsialiseerunud mudelit. |
| AI-agendi tööriistakutsed ei toimi hästi   | - Testi ja valideeri tööriista väljund väljaspool agendisüsteemi.<br>- Täienda tööriista parameetreid, prompt'e ja nimetamist.  |
| Mitme agendiga süsteem ei tööta stabiilselt | - Täienda iga agendi prompt'e, et need oleksid spetsiifilised ja üksteisest erinevad.<br>- Ehita hierarhiline süsteem, kasutades "marsruutimist" või juhitavat agenti, mis määrab õige agendi. |

Paljusid neid probleeme saab tõhusamalt tuvastada jälgitavuse olemasolul. Jäljed ja mõõdikud, mida eelnevalt käsitlesime, aitavad täpselt tuvastada, kus agendi töövoos probleemid esinevad, muutes tõrkeotsingu ja optimeerimise palju efektiivsemaks.

## Kulude juhtimine


Siin on mõned strateegiad AI agentide tootmisse juurutamise kulude haldamiseks:

**Väiksemate mudelite kasutamine:** Väikesed keelemudelid (SLM-id) suudavad teatud agentilistes kasutusjuhtudes hästi toimida ning vähendavad kulusid märkimisväärselt. Nagu varem mainitud, on parim viis mõista, kui hästi SLM teie kasutusjuhtumil toimib, ehitada hindamissüsteem, mis määrab ja võrdleb sooritust suurte mudelitega. Kaaluge SLM-ide kasutamist lihtsamate ülesannete jaoks, nagu kavatsuste klassifitseerimine või parameetrite eraldamine, samas kui keerulisemate mõtlemist vajavate ülesannete jaoks kasutage suuremaid mudeleid.

**Router-mudeli kasutamine:** Sarnane strateegia on kasutada erinevaid mudeleid ja suurusi. Võite kasutada LLM-i/SLM-i või serverivaba funktsiooni, et keerukuse põhjal päringuid parimatele sobivatele mudelitele suunata. See aitab samuti kulusid vähendada ning tagab soorituse õigetel ülesannetel. Näiteks suunake lihtsad päringud väiksematele ja kiirematele mudelitele ning kasutage kallimaid suuri mudeleid ainult keerukatele mõtlemist nõudvatele ülesannetele.

**Vastuste vahemällu salvestamine:** Leitud sagedased päringud ja ülesanded ning nende vastuste andmine enne, kui need teie agentlussüsteemi läbivad, on hea viis vähendada sarnaste päringute mahtu. Võite isegi rakendada voogu, mis tuvastab, kui sarnane päring on teie vahemällu salvestatud päringutega, kasutades selleks lihtsamaid AI mudeleid. See strateegia võib oluliselt vähendada sagedaste küsimuste või tavapäraste töövoogude kulusid.

## Vaatame, kuidas see praktikas töötab

[Selle osa näidis-märkmikus](./code_samples/10-expense_claim-demo.ipynb) näeme näiteid, kuidas saame kasutada jälgimisvahendeid oma agendi jälgimiseks ja hindamiseks.


### Kas teil on AI agentide tootmises kasutamise kohta rohkem küsimusi?

Liituge [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et suhelda teiste õppijatega, osaleda kontorite tundides ja saada vastused oma AI agentide küsimustele.

## Eelmine õppetükk

[Metakognitsiooni kujundusmuster](../09-metacognition/README.md)

## Järgmine õppetükk

[Agentlikud protokollid](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->