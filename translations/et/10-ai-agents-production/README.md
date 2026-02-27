# AI agendid tootmises: jälgitavus ja hindamine

[![AI Agents in Production](../../../translated_images/et/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kui tehisintellekti agendid liiguvad eksperimentaalsetest prototüüpidest reaalse maailma rakendusteni, muutub oluliseks mõista nende käitumist, jälgida nende jõudlust ja süsteemselt hinnata nende väljundeid.

## Õpieesmärgid

Selle õppetüki lõpetamise järel oskad sa:
- Agendi jälgitavuse ja hindamise põhikontseptsioone
- Teknikad agendi jõudluse, kulude ja efektiivsuse parandamiseks
- Mida ja kuidas oma AI agente süsteemselt hinnata
- Kuidas kulusid kontrollida AI agentide tootmisse juurutamisel
- Kuidas instrumendistada Microsoft Agent Frameworkiga loodud agendid

Eesmärk on varustada sind teadmistega, mis aitavad muuta sinu "musta kasti" agendid läbipaistvateks, haldatavateks ja usaldusväärseteks süsteemideks.

_**Märkus:** Oluline on juurutada ohutud ja usaldusväärsed AI agendid. Vaata ka õppetundi [Usaldusväärsete AI agentide loomine](./06-building-trustworthy-agents/README.md)._

## Jäljed ja osad

Jälgitavuse tööriistad nagu [Langfuse](https://langfuse.com/) või [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) kujutavad tavaliselt agendi töötsükleid jälgedena ja osadena.

- **Jälg (Trace)** tähistab täielikku agendi ülesannet algusest lõpuni (nagu kasutajapäringu töötlemine).
- **Osad (Spans)** on jälje sees olevad üksikjadad (nt keeletegmudeli kutsumine või andmete hankimine).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Ilma jälgitavuseta võib AI agent tunduda kui "must kast" — selle sisemine olek ja põhjendus on läbipaistmatud, mis muudab probleemide diagnoosimise või jõudluse optimeerimise keeruliseks. Jälgitavusega muutuvad agendid "klaaskastideks", mis pakuvad läbipaistvust, mis on ülioluline usalduse loomiseks ja nende soovitud toimimise tagamiseks.

## Miks jälgitavus tootmiskeskkonnas oluline on

AI agentide viimine tootmiskeskkonda toob kaasa uusi väljakutseid ja nõudmisi. Jälgitavus ei ole enam ainult "ilus lisand", vaid kriitiline võimekus:

* **Veaparandus ja põhjusanalüüs:** Kui agent ebaõnnestub või annab ootamatu tulemuse, annavad jälgitavuse tööriistad vajalikud jäljed vea allika leidmiseks. See on eriti oluline keerukate agentide puhul, mis võivad hõlmata mitut LLM-kutset, tööriistade kasutust ja tingimuslikku loogikat.
* **Latentsus ja kulude haldamine:** AI agendid toetuvad sageli LLM-idele ja teistele välistele API-dele, mis arveldatakse tokeni või kõne alusel. Jälgitavus võimaldab täpselt jälgida neid kõnesid, aidates tuvastada liiga aeglaseid või kulukaid toiminguid. See võimaldab meeskondadel optimeerida käske, valida tõhusamaid mudeleid või ümber kujundada töövooge, et hallata tegevuskulusid ja tagada hea kasutajakogemus.
* **Usaldus, ohutus ja vastavus:** Paljudes rakendustes on oluline tagada, et agendid käituvad ohutult ja eetiliselt. Jälgitavus pakub auditeerimisrajat agendi tegevustest ja otsustest. Seda saab kasutada probleemide, nagu käsu süstimine, kahjuliku sisu genereerimine või isikuandmete väärkasutus, avastamiseks ja leevendamiseks. Näiteks saad jälgi vaadates mõista, miks agent andis teatud vastuse või kasutas kindlat tööriista.
* **Jätkuva parendamise tsüklid:** Jälgitavuse andmed on iteratiivse arendusprotsessi alus. Jälgides, kuidas agendid reaalses maailmas toimivad, saab meeskond tuvastada parendusvaldkondi, koguda andmeid mudelite peenhäälestuseks ja valideerida muutuste mõju. See tekitab tagasisideahela, kus tootmisega seotud veebiinfo aitab analüüsida offline katsetusi ja parandusi, viies järk-järgult parema agendi jõudluseni.

## Peamised jälgitavad mõõdikud

Agendi käitumise jälgimiseks ja mõistmiseks tuleks jälgida mitmeid mõõdikuid ja signaale. Kuigi konkreetseid mõõdikuid võib agentide eesmärgi järgi varieeruda, on mõned universaalselt olulised.

Siin on mõned levinumad jälgitavad mõõdikud:

**Latentsus:** Kui kiiresti agent reageerib? Pikad ooteajad mõjutavad kasutajakogemust negatiivselt. Tuleks mõõta latentsust ülesannete ja üksikute sammude kaupa, jälgides agendi tööd. Näiteks agent, kelle mudelikutsed võtavad kokku 20 sekundit, võiks olla kiirendatav, kasutades kiiremat mudelit või käivitades mudelikutsed paralleelselt.

**Kulud:** Kui suured on kulud ühe agendi töökäigu kohta? AI agendid kasutavad tokenipõhiselt arveldatavaid LLM-kõnesid või väliseid API-sid. Sageli tööriista kasutamine või mitmekordsed käsud võivad kulusid kiiresti suurendada. Näiteks kui agent teostab LLM-kõnesid viis korda marginaalse kvaliteedi parandamise nimel, tuleks hinnata, kas kulu on õigustatud või kas kõnede arvu saaks vähendada või kasutada odavamat mudelit. Reaalaegne jälgimine aitab tuvastada ka ootamatuid kulutõuse (nt vigade tõttu liigsed API-tsüklid).

**Päringuvead:** Mitu päringut agent ei suutnud täita? See võib hõlmata API vigu või tööriistakõnede ebaõnnestumisi. Selliste probleemide vastu vastupidavuse tõstmiseks saab juurutada varuplaanid või korduskatsetused. Nt kui LLM teenusepakkuja A ei tööta, saab lülituda varuks teenusepakkuja B peale.

**Kasutajate tagasiside:** Otsetegevuse hindamine kasutajate poolt annab väärtuslikku infot. See võib sisaldada selget hinnangut (👍heaks/👎halb, ⭐1–5 tähte) või tekstipõhiseid kommentaare. Järjepidev negatiivne tagasiside peaks sind hoiatama kuna see näitab, et agent ei toimi ootuspäraselt.

**Kaudne kasutajate tagasiside:** Kasutajate käitumine annab kaudset tagasisidet isegi ilma otseste hinnanguteta. Selliseks võib olla küsimuse kiire ümberväljendamine, korduvad päringud või nupu "proovi uuesti" klõpsamine. Nt korduvad samade küsimuste esitused võivad viidata sellele, et agent ei tööta ootuspäraselt.

**Täpsus:** Kui sageli agent toodab õigeid või soovitud väljundeid? Täpsuse määratlused võivad erineda (nt probleemide lahendamise täpsus, infootsingu täpsus, kasutajate rahulolu). Esimene samm on määratleda, mida sinu agenti edukas tegutsemine tähendab. Täpsust saad jälgida automatiseeritud kontrollide, hindamisskooride või tööde lõpetamise siltide kaudu. Näiteks märgistades jäljed kui "õnnestunud" või "ebaõnnestunud".

**Automatiseeritud hindemõõdikud:** Võid seadistada ka automaatsed hindamised. Näiteks võid kasutada LLM-i hindamaks agendi väljundit kas see on abistav, täpne või mitte. Samuti on mitmeid avatud lähtekoodiga teeke, mis aitavad agendi eri aspektid hinnata. Nt [RAGAS](https://docs.ragas.io/) RAG-agentidele või [LLM Guard](https://llm-guard.com/) kahjuliku keele või käsu süstimise tuvastamiseks.

Praktikas annab nende mõõdikute kombinatsioon parima ülevaate AI agendi tervisest. Selle peatüki [näite-märkmik](./code_samples/10-expense_claim-demo.ipynb) näitab, kuidas need mõõdikud reaalses näites välja näevad, aga esmalt õpime tüüpilise hindamise töövoo toimimist.

## Instrumendista oma agent

Jälgimisandmete kogumiseks tuleb oma koodi instrumendistada. Eesmärk on instrumendistada agendi kood nii, et saadakse jälgi ja mõõdikuid, mida jälgitavuse platvorm suudab koguda, töödelda ja visualiseerida.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) on välja kujunenud tööstusharu standardiks LLMide jälgitavuses. See pakub mitmeid API-sid, SDK-sid ja tööriistu telemeetriaandmete genereerimiseks, kogumiseks ja eksportimiseks.

On palju instrumentatsiooniraamatukogusid, mis mähivad olemasolevad agentide raamistikud ja võimaldavad hõlpsasti eksportida OpenTelemetry osasid jälgitavustööriistadesse. Microsoft Agent Framework on natiivselt integreeritud OpenTelemetryga. Järgnevalt on näide MAF agendi instrumendistamisest:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agendi täitmist jälgitakse automaatselt
    pass
```


Selle peatüki [näitemärkmik](./code_samples/10-expense_claim-demo.ipynb) demonstreerib, kuidas instrumendistada oma MAF agenti.

**Manuaalne osade loomine:** Kuigi instrumentatsiooniraamatukogud annavad hea baasjoone, on tihti olukordi, kus on vaja detailsemat või kohandatud infot. Sa saad manuaalselt luua osasid, et lisada kohandatud rakendusloogikat. Veel olulisem, saad täiendada automaatselt või käsitsi loodud osasid kohandatud atribuutidega (tuntud ka siltide või metaandmetena). Need atribuudid võivad sisaldada ärispetsiifilisi andmeid, vahetulemusi või konteksti, mis on vajalik silumiseks või analüüsiks, näiteks `user_id`, `session_id` või `model_version`.

Näide jälgede ja osade käsitsi loomisest [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) abil:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```


## Agendi hindamine

Jälgitavus annab meile mõõdikud, kuid hindamine on see protsess, kus neid andmeid analüüsitakse (ja testi tehakse), et hinnata, kui hästi AI agent toimib ja kuidas seda saab parandada. Teisisõnu, kui sul on jäljed ja mõõdikud olemas, kuidas kasutada neid, et hinnata agenti ja teha otsuseid?

Regulaarne hindamine on oluline, sest AI agendid on sageli mittetäpselt juhitavad ja võivad areneda (uuenduste või mudeli käitumise muutumise kaudu) — ilma hindamata sa ei tea, kas sinu „tark agent“ tõesti töötab hästi või on ta hoopis halvemaks läinud.

AI agentide hindamine jaguneb kaheks kategooriaks: **veebipõhine hindamine** ja **offline hindamine**. Mõlemad on väärtuslikud ja täiendavad üksteist. Tavaliselt alustame offline hindamisest, kuna see on minimaalne samm enne agendi juurutamist.

### Offline hindamine

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

See tähendab agendi hindamist kontrollitud keskkonnas, tavaliselt testandmekogude abil, mitte otse kasutajate päringutes. Kasutatakse kureeritud andmekogusid, kus teatakse ootuspärast väljundit või õiget käitumist ning selle põhjal tehakse agendil katseid.

Näiteks, kui oled loonud matemaatilise sõnaprobleemi lahendava agendi, võib sul olla [testandmekogu](https://huggingface.co/datasets/gsm8k) 100 lahendatud ülesandega. Offline hindamist tehakse sageli arendusprotsessis (võib kuuluda CI/CD torujuhtmetesse) muudatuste kontrollimiseks või regressioonide vältimiseks. Eeliseks on see, et see on **korduv ja selgete täpsuse mõõdikutega, kuna sul on olemas tõde**. Võid simuleerida kasutajate päringuid ning mõõta agendi vastuseid ideaalse risti või automatiseeritud mõõdikutega nagu eespool kirjeldatud.

Offline hindamise suurim väljakutse on tagada, et testandmed on piisavalt mahukad ja asjakohased — agent võib fikseeritud testandmekogus hästi töötada, kuid tootmises tulla kokku väga erinevate päringutega. Seetõttu peaks testandmekogud pidevalt täienema uute serva juhtumite ja reaalse maailma olukordadega. Mõistlik on kasutada väikseid „suitsutesti“ kogumeid kiireks kontrolliks ja suuremaid komplekte laiemate jõudlusmõõdikute jaoks.

### Veebipõhine hindamine

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

See tähendab agendi hindamist elavas, reaalses keskkonnas, st tootmises kasutamise ajal. Veebipõhine hindamine hõlmab agendi jõudluse jälgimist reaalsetes kasutajaliikumistes ja tulemuste pidevat analüüsi.

Näiteks võid jälgida õnnestumismäärasid, kasutajate rahulolu skoori või muid mõõdikuid otse liikluses. Veebipõhise hindamise eelis on see, et see **haara ära olukorrad, mida laboris võib ette ei nähtud — saad jälgida mudeli efektiivsuse langust aja jooksul (kui sisuskeemid muutuvad) ja tabada ootamatuid päringuid või olukordi, mis testandmetes puudusid**. See annab põgusa ja realistliku pildi sellest, kuidas agent metsikus keskkonnas käitub.

Veebipõhine hindamine sisaldab kaudse ja otsese kasutajate tagasiside kogumist nagu eelpool mainitud ning võimalike varjatud katsete või A/B testide tegemist (kus uue agenti versioon jookseb paralleelselt vana vastu võrdlemiseks). Väljakutse seisneb usaldusväärsete siltide või hindepunktide saamisel elavate interaktsioonide kohta — sõltutakse kasutajate tagasisidest või järeltulvatest mõõdikutest (nt kas kasutaja klikkas tulemusele).

### Neid kahte ühendades

Veebipõhine ja offline hindamine ei ole teineteist välistavad, vaid hoopis hästi täiendavad. Veebijälgimisega saadud teadmised (nt uued kasutajate päringutüübid, kus agent töötab halvasti) aitavad täiendada ja parandada offline testandmeid. Vastupidi, agentide, kes edukalt läbi offline testide tulevad, saab kindlamalt veebis jooksutada ja jälgida.

Tegelikult paljud meeskonnad kasutavad tsüklit:

_hinda offline -> juuruta -> jälgi veebis -> kogu uued veakohad -> lisa offline komplekti -> täienda agenti -> korda_.

## Levinud probleemid

AI agentide tootmisse juurutamisel võid kokku puutuda mitmete väljakutsetega. Siin on mõned levinud probleemid ja võimalikud lahendused:

| **Probleem**    | **Võimalik lahendus**   |
| ------------- | ------------------ |
| AI agent ei täida järjekindlalt ülesandeid | - Täpsusta AI agendile antud käsku; ole eesmärkides selge.<br>- Tuvasta, kas ülesandeid saab jagada alamülesanneteks ja erinevate agentide vahel jaotada. |
| AI agent satub lõpututesse tsüklitesse | - Veendu, et on määratud selged peatamistingimused ja -reeglid, et agent teaks, millal protsess peatada.<br>- Komplekssete ülesannete puhul, mis nõuavad järeldamist ja planeerimist, kasuta selleks spetsialiseerunud suuremat mudelit. |
| AI agendi tööriistakutsed ei tööta hästi | - Testi ja valideeri tööriista väljund väljaspool agenti.<br>- Täpsusta tööriista määratletud parameetreid, käske ja nimetamist.  |
| Multi-agent süsteem ei tööta järjekindlalt | - Täpsusta iga agendi käsku nii, et need oleksid spetsiifilised ja üksteisest erinevad.<br>- Ehita hierarhiline süsteem, kasutades "marsruutijat" või juhtagent, mis otsustab, kes agentidest on õige lahendaja. |

Paljusid neist probleemidest saab tõhusamalt tuvastada koos jälgitavusega. Varasemalt mainitud jäljed ja mõõdikud aitavad täpselt kindlaks teha, kus agendi töövoos probleemid tekivad, muutes veaparanduse ja optimeerimise palju tõhusamaks.

## Kulude haldamine
Siin on mõned strateegiad, kuidas hallata AI agentide kasutuselevõtu kulusid tootmiskeskkonnas:

**Väiksemate mudelite kasutamine:** Väikesed keelemudelid (SLM-id) võivad teatud agentsetes kasutusjuhtudel hästi toimida ja vähendada kulusid märkimisväärselt. Nagu varem mainitud, on parim viis mõista, kui hästi SLM teie kasutusjuhtumil toimib, ehitada hindamissüsteem, mis määrab ja võrdleb selle jõudlust suuremate mudelitega. Mõelge SLM-ide kasutamisele lihtsamate ülesannete puhul, nagu kavatsuse klassifitseerimine või parameetrite eraldamine, jättes keerukateks järeldusteks suuremad mudelid.

**Router-mudeli kasutamine:** Sarnane strateegia on kasutada mitmekesisust mudelite ja suuruste osas. Võite kasutada LLM-i/SLM-i või serverivaba funktsiooni, mis suunab päringud keerukuse järgi sobivaimatele mudelitele. See aitab samuti kulusid vähendada ja tagada jõudlus õigetel ülesannetel. Näiteks saatke lihtsad päringud väiksematele ja kiirematele mudelitele ning kasutage kallimaid suuri mudeleid ainult keerukate järeldusülesannete jaoks.

**Vastuste vahemällu salvestamine:** Üldiste päringute ja ülesannete tuvastamine ning vastuste pakkumine enne nende agentsetesse süsteemidesse jõudmist on hea viis vähendada sarnaste päringute mahtu. Võite isegi rakendada voogude tuvastamist, kui sarnane on päring teie vahemällu salvestatud päringutele, kasutades selleks lihtsamaid AI mudeleid. See strateegia võib märkimisväärselt vähendada kulusid sagedaste küsimuste või tavapäraste töövoogude puhul.

## Vaatame, kuidas see praktikas toimib

[Selle peatüki näidismärkmikus](./code_samples/10-expense_claim-demo.ipynb) näeme näiteid, kuidas kasutada jälgimisvahendeid oma agendi monitorimiseks ja hindamiseks.


### Kas sul on rohkem küsimusi AI agentide kohta tootmises?

Liitu [Microsoft Foundry Discordiga](https://aka.ms/ai-agents/discord), et kohtuda teiste õppijatega, osaleda kontoritundides ja saada vastused oma AI agentide küsimustele.

## Eelmine õppetund

[Metakognitsiooni disainimuster](../09-metacognition/README.md)

## Järgmine õppetund

[Agentse protokollid](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellekti tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüame täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada usaldusväärseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalse inimtõlke teenust. Me ei vastuta tõlgendustest ega valesti mõistmistest, mis võivad sellest tõlkest tekkida.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->