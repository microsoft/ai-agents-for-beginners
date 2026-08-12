# AI-agentide tootmine: jälgitavus ja hindamine

[![AI-agentide tootmine](../../../translated_images/et/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kui AI-agentid liiguvad eksperimentaalsetelt prototüüpidelt pärismaailma rakendustesse, muutub oluliseks nende käitumise mõistmine, nende jõudluse jälgimine ja nende väljundite süsteemne hindamine.

## Õpieesmärgid

Pärast selle õppetüki läbimist oskad sa/sa mõistad:
- Agentide jälgitavuse ja hindamise põhimõisteid
- Meetodeid agentide jõudluse, kulude ja tõhususe parandamiseks
- Mida ja kuidas oma AI-agente süsteemselt hinnata
- Kuidas kulusid kontrollida AI-agentide tootmisse juurutamisel
- Kuidas instrumendistada Microsoft Agent Frameworkiga loodud agente

Eesmärk on varustada sind teadmistega, et muuta sinu "mustad kasti" agentid läbipaistvateks, hallatavaks ja usaldusväärseteks süsteemideks.

_**Märkus:** Oluline on juurutada AI-agente, mis on turvalised ja usaldusväärsed. Vaata ka [Usaldusväärsete AI-agentide loomine](../06-building-trustworthy-agents/README.md) õppetükki._

## Jäljed ja ulatused

Jälgitavuse tööriistad nagu [Langfuse](https://langfuse.com/) või [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) kujutavad tavaliselt agentide jooksud jälgedena ja ulatustena.

- **Jälg** kujutab terviklikku agentide ülesannet algusest lõpuni (näiteks kasutajaküsimuse käsitlemine).
- **Ulatused** on jälje sees üksikud sammud (näiteks keelemudeli kutsumine või andmete pärimine).

![Jälgede puu Langfuse'is](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Ilma jälgitavuseta võib AI-agent tunduda nagu "must kast" - selle sisemine olek ja loogika on hägused, mistõttu on keeruline vigu diagnoosida või jõudlust optimeerida. Jälgitavusega muutuvad agentid "klaaskastideks", pakkudes läbipaistvust, mis on otsustava tähtsusega usalduse ehitamiseks ja nende oodatud toimimise tagamiseks.

## Miks jälgitavus tootmiskeskkonnas oluline on

AI-agentide viimine tootmiskeskkondadesse seab nende jaoks uued väljakutsed ja nõuded. Jälgitavus ei ole enam "hape", vaid kriitilise tähtsusega võimekus:

*   **Veaparandus ja põhi põhjusanalüüs:** Kui agent ebaõnnestub või annab ootamatu tulemuse, pakuvad jälgitavuse tööriistad vajalikke jälgi vea allika täpseks määramiseks. See on eriti oluline keerukate agentide puhul, mis võivad hõlmata mitut LLMi kõnet, tööriistadega suhtlemist ja tingimusloogikat.
*   **Latentsus ja kulude juhtimine:** AI-agentid sõltuvad sageli LLMidest ja muudest välistest APIdest, mille eest arvestatakse tasu tokeni või kõne alusel. Jälgitavus võimaldab täpset nende kõnede jälgimist, aidates tuvastada liigset aeglust või kallid operatsioonid. See võimaldab optimeerida prompt’e, valida tõhusamaid mudeleid või ümber kujundada töövooge, et hallata tegevuskulusid ja tagada hea kasutajakogemus.
*   **Usaldus, turvalisus ja nõuetele vastavus:** Paljudes rakendustes on oluline tagada, et agent käitub turvaliselt ja eetiliselt. Jälgitavus pakub auditijälge agentide tegevuste ja otsuste kohta. Seda saab kasutada selliste probleemide avastamiseks ja leevendamiseks nagu promptide süstimine, kahjuliku sisu genereerimine või isikuandmete väärkasutus (PII). Näiteks saab jälgedeid vaadata, et mõista, miks agent tegi teatud vastuse või kasutas konkreetset tööriista.
*   **Jätkuvad parendustsüklid:** Jälgitavuse andmed on iteratiivse arendusprotsessi aluseks. Jälgides agentide toimimist päriselus, saavad meeskonnad tuvastada arenguvõimalusi, koguda andmeid modelleerimiseks ja hinnata muudatuste mõju. See tekitab tagasiside tsükli, kus tootmisalased online-hinnangud suunavad offline-katsetust ja täiustamist, viies järjest parema agentide toimimiseni.

## Peamised jälgitavad mõõdikud

Agentide käitumise jälgimiseks ja mõistmiseks tuleks jälgida mitmeid mõõdikuid ja signaale. Kuigi konkreetseid mõõdikuid võib varieeruda vastavalt agentide eesmärgile, on mõned universaalselt olulised.

Siin on mõned jälgitavad kõige levinumad mõõdikud:

**Latentsus:** Kui kiiresti agent vastab? Pikad ooteajad mõjuvad kasutajakogemusele negatiivselt. Latentsust peaks mõõtma ülesannete ja üksikute sammude kaupa, jälgides agentide jooksusid. Näiteks agent, kes kulutab kõikide mudelikõnede jaoks 20 sekundit, võiks kiirendada, kasutades kiirem mudelit või tehes mudelikõned paralleelselt.

**Kulud:** Kui palju maksab agentide üks jooks? AI-agentid sõltuvad LLM-i kõnedest, mille eest arvestatakse tasu tokeni või välise API-ühenduse eest. Tihe tööriistade kasutus või mitmed prompt’id võivad kiiresti kulusid tõsta. Näiteks kui agent kutsub LLM-i viis korda marginaalse kvaliteedi paranduse nimel, tuleb hinnata, kas kulud on õigustatud või kas kõnede arvu võiks vähendada või kasutada odavamat mudelit. Reaalaegne jälgimine aitab avastada ootamatuid kulutõuse (nt vead, mis tekitavad liigseid API-loope).

**Päringuvead:** Kui palju päringuid agent ebaõnnestus? See võib hõlmata API-vigu või ebaõnnestunud tööriistakõnesid. Et muuta agent tootmises vastupidavamaks, saab selliste vigade vastu seadistada varuplaanid või korduskatsed. Näiteks kui LLM-i pakkuja A on maas, lülitad varuvariandina üle pakkujale B.

**Kasutajate tagasiside:** Otsepäringute hindamise rakendamine annab väärtuslikku infot. See võib hõlmata selgesõnalisi hinnanguid (👍heaks/👎halvaks, ⭐1-5 tärni) või tekstilisi kommentaare. Pidev negatiivne tagasiside peaks sind hoiatama, sest see on märk, et agent ei toimi ootuspäraselt. 

**Kaudne kasutajate tagasiside:** Kasutajate käitumine annab kaudset tagasisidet ka ilma selgesõnaliste hinnanguteta. See võib tähendada kohest küsimuse ümber sõnastamist, korduvaid päringuid või uuesti proovi nupule klõpsamist. Näiteks, kui näed, et kasutajad esitavad sama küsimust korduvalt, on see märk, et agent ei toimi ootuspäraselt.

**Täpsus:** Kui tihti agent annab õigeid või soovitud vastuseid? Täpsuse definitsioonid varieeruvad (näiteks probleemilahenduse õigsus, info pärimise täpsus, kasutaja rahulolu). Esimene samm on määratleda, mis on sinu agendi jaoks edu. Sa võid jälgida täpsust automatiseeritud kontrollide, hindamisskooride või ülesande täitmise siltide kaudu. Näiteks märkides jäljed "õnnestunud" või "ebaõnnestunud".

**Automaatse hindamise mõõdikud:** Sa võid seadistada ka automaatseid hindamisi. Näiteks võid kasutada LLM-i, et hinnata agendi väljundit, kas see on kasulik, täpne või mitte. On ka mitmeid avatud lähtekoodiga raamistikke, mis aitavad hinnata agendi erinevaid aspekte. Näiteks [RAGAS](https://docs.ragas.io/) RAG-agentide jaoks või [LLM Guard](https://llm-guard.com/), mis avastab kahjulikku keelt või promptide süstimist.

Praktikas annab nende mõõdikute kombinatsioon parima ülevaate AI-agendi seisundist. Selle peatüki [näitenootebookis](./code_samples/10-expense_claim-demo.ipynb) näitame, kuidas need mõõdikud reaalsetes näidetes välja näevad, ent esmalt õpime tüüpilise hindamisprotsessi.

## Instrumenteerige oma agent

Jälgede andmete kogumiseks tuleb oma koodi instrumendistada. Eesmärk on instrumendistada agentide kood, et saata jälgi ja mõõdikuid, mida jälgitavuse platvorm suudab salvestada, töödelda ja visualiseerida.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) on kujunenud LLM-i jälgitavuse tööstusstandardiks. See pakub API-sid, SDK-sid ja tööriistu telemeetriaandmete genereerimiseks, kogumiseks ja eksportimiseks.

Paljud instrumendistamise raamatukogud sisaldavad olemasolevaid agentide raamistikke ja muudavad OpenTelemetry ulatuste eksportimise jälgitavuse tööriistasse lihtsaks. Microsoft Agent Framework integreerub OpenTelemetry-ga loomulikult. Allpool on näide MAF agenti instrumendist:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agendi täitmist jälgitakse automaatselt
    pass
```

Selle peatüki [näitenootebook](./code_samples/10-expense_claim-demo.ipynb) demonstreerib, kuidas instrumendistada oma MAF agenti.

**Manuaalne ulatuste loomine:** Kuigi instrumendistamise raamatukogud pakuvad head alust, on sageli kohtasid, kus on vaja detailsemaid või kohandatud andmeid. Sa võid manuaalselt luua ulatusi, lisades kohandatud rakenduse loogikat. Veel olulisem, saad rikastada automaatselt või käsitsi loodud ulatusi kohandatud omadustega (tuntud ka kui sildid või metaandmed). Need võivad sisaldada ärispetsiifilisi andmeid, vahepealseid arvutusi või mis tahes konteksti, mis võib aidata vigu parandada või analüüsida, näiteks `user_id`, `session_id` või `model_version`.

Näide jälgede ja ulatuste manuaalsest loomise kohta [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) abil:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agendi hindamine

Jälgitavus annab meile mõõdikuid, aga hindamine on andmete analüüsimise protsess (ja testide läbiviimine), et määrata, kui hästi AI-agent töötab ja kuidas seda saaks paremaks teha. Teisisõnu, kui sul on need jäljed ja mõõdikud olemas, kuidas neid kasutada agendi hindamiseks ja otsuste tegemiseks?

Regulaarne hindamine on oluline, sest AI-agentid on tihti mittetäpsed ja võivad areneda (versiooniuuenduste või mudelikäitumise muutumise kaudu) – ilma hindamiseta ei tea sa, kas sinu "tark agent" teeb oma tööd hästi või on ta regressioonis.

AI-agentide hindamine jaguneb kahele kategooriale: **online-hindamine** ja **offline-hindamine**. Mõlemad on väärtuslikud ja täiendavad teineteist. Tavaliselt alustame offline-hindamisest, sest see on minimaalne samm enne agendi juurutamist.

### Offline-hindamine

![Dataseti elemendid Langfuse’is](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

See tähendab agendi hindamist kontrollitud keskkonnas, tavaliselt testandmestike abil, mitte päris kasutajate päringutega. Kasutatakse kureeritud andmestikke, kus on teada oodatud väljund või korrektne käitumine, ning tark agent jooksutatakse nende andmestike peal.

Näiteks kui oled ehitanud matemaatikaprobleemide agenti, võib sul olla [testandmestik](https://huggingface.co/datasets/gsm8k) 100 ülesandega, mille vastused on teada. Offline-hindamist tehakse sageli arenduse käigus (ja see võib olla osa CI/CD töövoogudest), et kontrollida paranemisi või vältida regressioone. Selle eelis on, et see on **korratav ja annab selgeid täpsuse mõõdikuid, kuna on olemas tõeline vastus**. Samuti võib simuleerida kasutajate päringuid ja mõõta agendi vastuseid ideaalsete vastuste suhtes või kasutada automaatseid mõõdikuid nagu eespool kirjeldatud.

Offline-hindamise suurim väljakutse on tagada, et testandmestik oleks põhjalik ja ajakohane – agent võib sooritada hästi fikseeritud testikomplekti peal, kuid tootmises esineda väga erinevaid päringuid. Seepärast tuleks testkomplekte regulaarselt täiendada uute erandjuhtumite ja näidetega, mis peegeldavad pärismaailma olukordi. Kasulik on segada väikseid "hääletesti" juhtumeid ja suuremaid hindamiskomplekte: väikesi kiireks kontrolliks ja suuremaid laiemate jõudlusmõõdikute jaoks.

### Online-hindamine

![Jälgitavuse mõõdikute ülevaade](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

See tähendab agendi hindamist elavas, päriselulises keskkonnas ehk kasutamise ajal tootmises. Online-hindamine hõlmab agendi jõudluse jälgimist reaalsete kasutajate suhtlustel ja tulemuste pidevat analüüsi.

Näiteks võid jälgida õnnestumismäärasid, kasutajate rahulolu skooridest või muid mõõdikuid reaalsetel päringutel. Online-hindamise eelis on see, et see **tabab asju, mida sa laborikeskkonnas ette ei näe** – näiteks mudelite kõikumisi ajas (kui agendi tõhusus halveneb sisendmustrite muutudes) ning ootamatuid päringuid või olukordi, mis testandmestikus puudusid. See annab reaalse pildi, kuidas agent looduses käitub.

Online-hindamine hõlmab sageli kaudse ja otsese kasutajate tagasiside kogumist ning võib hõlmata varjatud teste või A/B-teste (kus uus agentide versioon töötab paralleelselt vana variandiga võrdluseks). Väljakutse on sageli see, et usaldusväärsete siltide või skooride saamine reaalsete päringute põhjal võib olla keeruline – toetuda võid kasutajate tagasisidele või alluvatele mõõdikutele (näiteks kas kasutaja klikib tulemusele).

### Kahe hindamisviisi kombineerimine

Online- ja offline-hindamised ei ole üksteist välistavad; need täiustavad teineteist. Online-jälgimisega (nt uued kasutajate päringutüübid, kus agent toimib halvasti) saad täiendada ja parandada offline testandmestikke. Vastupidi, hästi offline-testides toimivad agentid saab seejärel enesekindlamalt juurutada ja online-keskkonnas jälgida.

Tegelikult kasutavad paljud meeskonnad järgmist tsüklit:

_offline hindamine -> juurutamine -> online jälgimine -> uute rikete juhtumite kogumine -> lisamine offline andmestikku -> agendi täiustamine -> kordamine_.

## Levinud probleemid

AI-agentide tootmisse viies võid kokku puutuda mitme väljakutsega. Siin on mõned tavalised probleemid ja nende võimalikud lahendused:

| **Probleem**    | **Võimalik lahendus**   |
| ------------- | ------------------ |
| AI-agent ei täida ülesandeid järjekindlalt | - Täiusta agendile antud prompt'i, ole eesmärkides selge.<br>- Määratle kohad, kus ülesande jagamine osadeks ja nende haldamine mitme agenti poolt aitab. |
| AI-agent läbib lõputuid silmuseid  | - Tagada selged lõpetamise tingimused, et agent teaks, millal protsess peatub.<br>- Keerukatele, loogikut ja planeerimist nõudvatele ülesannetele kasuta suuremat mudelit, mis on mõeldud mõtlemise ülesannetele. |
| AI-agendi tööriistade kõned ei tööta korralikult   | - Testi ja kontrolli tööriista väljundit väljaspool agendi süsteemi.<br>- Täiusta määratletud parameetreid, prompt’e ja tööriistade nimetust.  |
| Mitme agente süsteem ei toimi järjekindlalt | - Täiusta iga agendi prompt’e, tagades, et need on spetsiifilised ja teineteisest erinevad.<br>- Ehita hierarhiline süsteem, kasutades "marsruutimise" või kontrolliva agenti, et määrata õige agent. |

Paljusid neist probleemidest saab tõhusamalt tuvastada jälgitavust kasutades. Eelnevalt käsitletud jäljed ja mõõdikud aitavad täpselt tuvastada kohta agentide töövoos, kus probleemid ilmnevad, muutes veaparanduse ja optimeerimise palju tõhusamaks.

## Kulude juhtimine


Siin on mõned strateegiad, kuidas hallata AI agentide tootmisse viimisega seotud kulusid:

**Väiksemate mudelite kasutamine:** Väikesed keelemudelid (SLMd) suudavad mõningatel agentuursetel juhtudel hästi toimida ning vähendavad oluliselt kulusid. Nagu varem mainitud, on parim viis mõista, kui hästi SLM teie kasutusjuhtumis toimib, ehitada hindamissüsteem, mis määrab ja võrdleb jõudlust suuremate mudelitega. Kaaluge SLM-de kasutamist lihtsamate ülesannete jaoks, näiteks kavatsuste klassifitseerimiseks või parameetrite väljavõtmiseks, samal ajal kui keerukama mõtlemise jaoks kasutage suuremaid mudeleid.

**Marsruutimudeli kasutamine:** Sarnane strateegia on kasutada mitmekesiseid mudeleid ja suurusi. Võite kasutada LLM-i/SLM-i või serverivaba funktsiooni, et suunata päringud keerukuse põhjal sobivaimatele mudelitele. See aitab ka kulusid vähendada ning tagab samal ajal jõudluse õigetel ülesannetel. Näiteks suunake lihtsad päringud väiksematele ja kiirematele mudelitele ning kasutage kallimaid suuri mudeleid ainult keerukate mõtlemist vajavate ülesannete jaoks.

**Vastuste vahemällu salvestamine:** Tuntud päringute ja ülesannete tuvastamine ning vastuste pakkumine enne agentuuri süsteemist läbi minemist on hea viis taoliste päringute mahtu vähendada. Võite isegi rakendada voogu, mis määrab, kui sarnane päring on teie vahemällu salvestatud päringutele, kasutades selleks lihtsamaid AI mudeleid. See strateegia võib oluliselt vähendada kulusid sagedasti esitatavate küsimuste või tavapäraste töövoogude puhul.

## Vaatame, kuidas see praktikas töötab

[Selle sektsiooni näitenootbukis](./code_samples/10-expense_claim-demo.ipynb) näeme näiteid sellest, kuidas kasutada jälgimisvahendeid meie agendi jälgimiseks ja hindamiseks.


### Kas sul on AI agentide tootmisse viimise kohta lisaküsimusi?

Liitu [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppijatega, osaleda kõneaegadel ja saada vastused oma AI agentide küsimustele.

## Eelmine õppetund

[Metakognitsiooni disainimuster](../09-metacognition/README.md)

## Järgmine õppetund

[Agentuurprotokollid](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->