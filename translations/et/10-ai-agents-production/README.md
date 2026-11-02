# Tehisintellekti agendid tootmises: jälgitavus ja hindamine

[![AI Agents in Production](../../../translated_images/et/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kui tehisintellekti agendid liiguvad katseversioonidest pärismaailma rakendustesse, muutub oluliseks nende käitumise mõistmine, jõudluse jälgimine ja toodete süsteemne hindamine.

## Õpieesmärgid

Pärast selle õppetüki lõpetamist oskad/saad aru:
- Agendi jälgitavuse ja hindamise põhikontseptsioonidest
- Agendi jõudluse, kulude ja tõhususe parandamise tehnikatest
- Kuidas oma tehisintellekti agente süsteemselt hinnata
- Kuidas kontrollida kulusid tehisintellekti agentide tootmisesse juurutamisel
- Kuidas tööriistaga Microsoft Agent Framework ehitatud agente instrumendiga varustada

Eesmärk on varustada sind teadmistega, et muuta sinu „musta kasti“ agendid läbipaistvateks, hallatavateks ja usaldusväärseteks süsteemideks.

_**Märkus:** Oluline on juurutada turvalisi ja usaldusväärseid tehisintellekti agente. Vaata ka õppetükki [Usaldusväärsete tehisintellekti agentide loomine](../06-building-trustworthy-agents/README.md)._

## Jäljed ja ulatused

Jälgitavuse tööriistad nagu [Langfuse](https://langfuse.com/) või [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) kujutavad tavaliselt agendi töid jälgedena ja ulatustena.

- **Jälg** esindab täielikku agendi ülesannet algusest lõpuni (nt kasutajaküsimuse käsitlemine).
- **Ulatused** on jälje üksikud sammud (nt keeledemudeli kutsumine või andmete päring).

![Jälje puu Langfuses](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Pildilingi säilitatud illustratsiooniks -->

Ilma jälgitavuseta võib tehisintellekti agent tunduda „must kast“ – tema sisemine olek ja põhjendus on läbipaistmatud, mis raskendab vigade diagnoosimist või jõudluse optimeerimist. Jälgitavusega muutuvad agendid „klaaskastideks“, pakkudes läbipaistvust, mis on usalduse loomiseks ja ootuspäraseks toimimiseks hädavajalik.

## Miks on jälgitavus tootmiskeskkondades oluline

Tehisintellekti agentide üleminek tootmiskeskkonda toob kaasa uued väljakutsed ja nõuded. Jälgitavus ei ole enam lihtsalt "mugavus" vaid kriitiline võimekus:

*   **Silumine ja põhjuslike vigade analüüs**: Kui agent ebaõnnestub või annab ootamatu tulemuse, annavad jälgitavuse tööriistad vajaliku jälje vea allika täpsustamiseks. See on eriti tähtis keeruliste agentide puhul, kus võib olla mitu LLM-i kutsungit, tööriistade vastastikmõjusid ja tingimuslikku loogikat.
*   **Latentsus ja kulude haldamine**: Tehisintellekti agendid tuginevad sageli LLM-idele ja teistele välistele API-dele, mida arvestatakse tokeni või kutsungi põhjal. Jälgitavus võimaldab täpset kutsungite jälgimist, aidates tuvastada protsesse, mis on liigselt aeglased või kallid. See võimaldab meeskondadel optimeerida käske, valida tõhusamaid mudeleid või ümber kujundada töövooge, et hallata kulusid ja tagada hea kasutajakogemus.
*   **Usaldus, turvalisus ja vastavus nõuetele**: Paljude rakenduste puhul on oluline tagada, et agendid käituvad turvaliselt ja eetiliselt. Jälgitavus annab auditijälje agendi tegevustest ja otsustest. Seda saab kasutada selliste probleemide avastamiseks ja leevendamiseks nagu promptide manipuleerimine, kahjuliku sisu genereerimine või isikuandmete (PII) väärkasutus. Näiteks saab jälgi läbi vaadata, et mõista, miks agent andis teatud vastuse või kasutas konkreetset tööriista.
*   **Jätkuvad parendusringid**: Jälgitavuse andmed on iteratiivse arendusprotsessi alus. Reaalmaailmas agentide jõudlust jälgides saab meeskond tuvastada parendusvaldkondi, koguda andmeid mudelite täpsustamiseks ja kinnitada muudatuste mõju. See loob tagasisidetsükli, kus tootmisest saadud teadmised veebipõhisest hindamisest täiustavad võrguväliseid eksperimente ja parendusi, viies järk-järgult parema agendi jõudluseni.

## Peamised mõõdikud, mida jälgida

Agendi käitumise jälgimiseks ja mõistmiseks tuleks jälgida mitmeid mõõdikuid ja signaale. Kuigi konkreetsed mõõdikud võivad sõltuda agendi eesmärgist, on mõned universaalselt tähtsad.

Siin on mõned enim jälgitavad mõõdikud:

**Latentsus:** Kui kiiresti agent reageerib? Pikad ooteajad mõjuvad kasutajakogemusele halvasti. Tuleks mõõta latentsust ülesannete ja üksikute sammude kaupa, jälgides agendi tööprotsesse. Näiteks agent, kes kulutab kõigile mudelikutsungitele 20 sekundit, võiks kiireneda, kasutades kiirem mudelit või tehes kutsungid paralleelselt.

**Kulud:** Milline on kulu ühe agendi töö korral? AI agendid kasutavad LLM-kutsungeid, mida arvestatakse tokeni või välise API-kutsungi kohta. Tööriistade sagedane kasutamine või mitmed käsud võivad kulusid kiiresti kasvatada. Näiteks kui agent kutsub LLM-i viis korda marginaalse kvaliteedi paranduse pärast, tuleb hinnata, kas kulu on õigustatud või kas võiks vähendada kutsungite arvu või valida odavama mudeli. Reaalajas jälgimine aitab tuvastada ootamatuid piike (nt vead, mis põhjustavad liigseid API-tsükleid).

**Päringuvead:** Mitu päringut agent ebaõnnestus täitma? See võib hõlmata API vigu või nurjunud tööriista kutsungeid. Et muuta agent tootmises vastupidavamaks, saab seejärel seadistada tagavarakäske või kordusi. Näiteks kui LLM pakkuja A on maas, lülituda LLM pakkujale B reservvaruna.

**Kasutajate tagasiside:** Otse kasutajate hinnangute kaasamine annab väärtuslikku infot. See võib olla selged hinnangud (👍meeldib/👎ei meeldi, ⭐1-5 tärni) või tekstilised kommentaarid. Pidev negatiivne tagasiside peaks hoiatama, sest see tähendab, et agent ei tööta oodatult.

**Kaudne kasutajate tagasiside:** Kasutajate käitumine annab kaudset tagasisidet ilma otseste hinnanguteta. See võib sisaldada küsimuse kiiret ümber sõnastamist, korduvaid päringuid või valikut proovida uuesti. Näiteks kui näed, et kasutajad esitavad sama küsimust korduvalt, on see märk, et agent ei tööta oodatult.

**Täpsus:** Kui tihti agent annab õigeid või soovitud vastuseid? Täpsus võib tähendada erinevaid asju (probleemilahenduse täpsus, infootsingu õigsus, kasutajate rahulolu). Esimene samm on määratleda, mida edu sinu agendil tähendab. Täpsust võib jälgida automaatsete kontrollide, hindamisskooride või ülesande täitmise siltide kaudu. Näiteks märgistada jäljed kui „õnnestunud“ või „ebaõnnestunud“.

**Automatiseeritud hindamismõõdikud:** Võid seadistada ka automatiseeritud hindamisi. Näiteks saad kasutada LLM-i agendi väljundi hindamiseks selle abil, kas see on abiks, täpne või mitte. On ka mitmeid avatud lähtekoodiga teeke, mis aitavad hinnata erinevaid agendi aspekte. Nt [RAGAS](https://docs.ragas.io/) RAG agentidele või [LLM Guard](https://github.com/protectai/llm-guard) kahjuliku keele tuvastamiseks või prompt-põhise manipulatsiooni avastamiseks.

Praktikas annab nende mõõdikute kombinatsioon parima ülevaate AI agendi seisundist. Käesoleva peatüki [näite märkmik](./code_samples/10-expense_claim-demo.ipynb) demonstreerib, kuidas need mõõdikud näevad välja reaalsetes näidetes, aga esmalt õpime, milline on tüüpiline hindamisprotsess.

## Instrumendi kasutamise paigaldamine agendile

Jälgede kogumiseks on vaja instrumenteerida koodi. Eesmärk on instrumendiga varustada agent kood nii, et ta eraldaks jälgi ja mõõdikuid, mida jälgitavuse platvorm suudab püüda, töödelda ja visualiseerida.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) on kujunenud tööstusharu standardiks LLM-jälgitavuses. See pakub API-sid, SDK-sid ja tööriistu telemeetria andmete genereerimiseks, kogumiseks ja eksportimiseks.

On palju instrumenteerimisteeke, mis pakivad olemasolevaid agendiraamistikke ja teevad lihtsaks OpenTelemetry ulatuste eksportimise jälgitavustööriista. Microsoft Agent Framework integreerub OpenTelemetry-ga loomulikult. Järgnevalt on näide MAF agendi instrumendi kasutamisest:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agent execution is traced automatically
    pass
```

Käesoleva peatüki [näite märkmik](./code_samples/10-expense_claim-demo.ipynb) demonstreerib, kuidas oma MAF agenti instrumendi kaudu varustada.

**Ulatuste käsitsi loomine:** Kuigi instrumenteerimisteegid annavad hea algusbaasi, on sageli juhtumeid, kus on vaja detailsemat või kohandatud infot. Võid käsitsi luua ulatusi, et lisada kohandatud rakendusloogikat. Veelgi tähtsam, saab automaatselt või käsitsi loodud ulatustele lisada kohandatud atribuute (tuntud ka kui sildid või metaandmed). Need atribuudid võivad sisaldada ärispetsiifilisi andmeid, vahepealseid arvutusi või konteksti, mis on kasulik silumiseks või analüüsiks, näiteks `user_id`, `session_id` või `model_version`.

Näide jälgede ja ulatuste käsitsi loomisest [Langfuse Python SDK-ga](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agendi hindamine

Jälgitavus annab meile mõõdikud, kuid hindamine on protsess, mis analüüsib neid andmeid (ja viib läbi teste), et määrata, kui hästi tehisintellekti agent töötab ja kuidas seda saab parandada. Teisisõnu, kui sul on jäljed ja mõõdikud olemas, kuidas neid kasutada agendi hindamiseks ja otsustamiseks?

Regulaarne hindamine on oluline, sest AI agendid on sageli mitte-determineeruvad ja võivad areneda (kusjuures mudeli käitumine võib muutuda või nihkuda) – ilma hindamiseta ei teaks sa, kas sinu „tark agent“ tõesti hästi töötab või on ta halvemaks läinud.

AI agentide hindamisel on kaks kategooriat: **võrguvaba (offline) hindamine** ja **veebipõhine (online) hindamine**. Mõlemad on väärtuslikud ja täiendavad üksteist. Tavaliselt alustame võrguvaba hindamisega, kuna see on minimaalne vajalik samm enne agendi tootmisesse juurutamist.

### Võrguvaba hindamine

![Andmete komplekti üksused Langfuses](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

See hõlmab agendi hindamist kontrollitud keskkonnas, tavaliselt testandmekogude abil, mitte reaalsete kasutajaküsimustega. Kasutatakse kureeritud andmekogusid, kus teatakse oodatud väljundit või korrektset käitumist, ja siis agent töötab nende andmetega.

Näiteks, kui oled loonud matemaatiliste sõnaprobleemide agendi, võib sul olla [testandmekogu](https://huggingface.co/datasets/openai/gsm8k), mis sisaldab 100 probleemi koos teadaolevate vastustega. Võrguvaba hindamine toimub sageli arendusperioodil (võib olla osa CI/CD torujuhtmetest), et kontrollida parendusi või vältida regressioone. Eelis on see, et see on **korduv ja saad selgeid täpsuse mõõdikuid, kuna on olemas tõde**. Samuti võid simuleerida kasutajaküsimusi ja mõõta agendi vastuseid ideaalse vastu või kasutada eespool kirjeldatud automatiseeritud mõõdikuid.

Võrguvaba hindamise suurim väljakutse on tagada, et testandmekogu oleks põhjalik ja jääks relevantseks – agent võib teha head tööd fikseeritud testkogul, kuid tootmises tulla toime väga erinevate päringutega. Seega peaksid testkogusid regulaarselt uuendama uute servajuhtumite ja näidetega, mis peegeldavad pärismaailma olukordi. Kasulik on segu väikestest „suitsutest“ juhtumitest ja suurematest hindamiskogudest: väikesed kiirkontrolliks ja suured laiaulatuslikumate jõudlusmõõdikute jaoks.

### Veebipõhine hindamine

![Jälgitavuse mõõdikute ülevaade](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

See tähendab agendi hindamist elavas pärismaailma keskkonnas, st tegelikul tootmiskasutamisel. Veebipõhine hindamine hõlmab agendi jõudluse jälgimist päriskasutaja interaktsioonidel ja tulemuste pidevat analüüsi.

Näiteks võid jälgida õnnestumisprotsente, kasutajate rahulolu skoori või muid mõõdikuid reaalsete andmete põhjal. Veebipõhise hindamise eelis on see, et see **tabab asju, mida sa laboris ei pruugi oodata** – saad jälgida mudeli nihkumist aja jooksul (kui agendi efektiivsus väheneb, kui sisend mustrid muutuvad) ja tabada ootamatuid päringuid või olukordi, mida sinu testandmed ei hõlmanud. See annab tõelise pildi, kuidas agent käitub pärismaailmas.

Veebipõhine hindamine hõlmab sageli nii kaudse kui ka otsese kasutajate tagasiside kogumist ja võib sisaldada varjuteste või A/B teste (kus uus agentide versioon jookseb paralleelselt vana vastu võrdlemiseks). Väljakutseks on usaldusväärsete siltide või skooride saamine reaalajas interaktsioonide kohta – sageli toetutakse kasutajate tagasisidele või alluvatele mõõdikutele (nt kas kasutaja klõpsas tulemust).

### Kahe meetodi ühendamine

Veebipõhine ja võrguvaba hindamine ei ole vastastikku välistavad, vaid täiendavad teineteist. Veebipõhise jälgimise põhjal saadud teadmisi (nt uute kasutajapäringutüüpide kohta, kus agent töötab halvasti) saab kasutada võrguvabade andmekogude täiustamiseks ja parandamiseks. Vastupidi, agentide, kes on võrgus hästi sooritanud, saab seejärel kindlamalt juurutada ja veebis jälgida.

Tegelikult paljud meeskonnad järgivad tsüklit:

_võrguvaba hindamine -> juurutamine -> veebijälgimine -> uute tõrketu juhtumite kogumine -> lisamine võrguvabale andmekogule -> agendi täpsustamine -> kordamine_.

## Levinud probleemid

Järgnevalt mõned levinud probleemid ja võimalikud lahendused tehisintellekti agentide tootmisse juurutamisel:

| **Probleem**    | **Võimalik lahendus**   |
| ------------- | ------------------ |
| AI Agent ei täida ülesandeid ühtlaselt | - Täpsustage agentidele antud käske; olge eesmärkides selged.<br>- Identifitseerige, kus ülesanne jagamine alamülesanneteks ja mitme agendi kaasamine võib aidata. |
| AI Agent satub lõpututesse tsüklitesse  | - Tagage selged lõpetamise tingimused, et agent teaks, millal lõpetada protsess.<br>- Kasutage keeruliste ülesannete jaoks suuremat mudelit, mis on spetsialiseerunud põhjendamisele ja planeerimisele. |
| AI Agendi tööriistade kutsed ei toimi hästi   | - Testige ja valideerige tööriista väljund väljaspool agendi süsteemi.<br>- Täpsustage tööriistade parameetreid, käske ja nimetusi.  |
| Mitme agendi süsteem ei tööta ühtlaselt | - Täpsustage iga agendi käsud, et need oleksid spetsiifilised ja erinevad.<br>- Ehitage hierarhiline süsteem kasutades „suunamis“ või kontroller-agenti, kes otsustab, milline agent on õige. |

Paljusid neist probleemidest saab tõhusamalt avastada olemasoleva jälgitavuse abil. Varasemalt mainitud jäljed ja mõõdikud aitavad tuvastada täpselt, kus agendi töövoogu esineb probleeme, muutes silumise ja optimeerimise palju efektiivsemaks.

## Kulude haldamine

Siin on mõned strateegiad tehisintellekti agentide tootmisse juurutamise kulude haldamiseks:

**Väiksemate mudelite kasutamine:** Väikesed keelemudelid (SLMid) võivad teatud agendi kasutusjuhtudel hästi toimida ja vähendada oluliselt kulusid. Nagu varem mainitud, on parim viis mõista, kui hästi SLM teie kasutusjuhtumil toimib, ehitada hindamissüsteem, mis määrab ja võrdleb jõudlust suuremate mudelitega. Mõelge SLM-ide kasutamisele lihtsamate ülesannete jaoks nagu kavatsuse klassifitseerimine või parameetrite väljavõtmine, samas kui keerukate mõtlemisülesannete jaoks reserveerige suuremad mudelid.

**Lülitusmudeli kasutamine:** Sarnane strateegia on kasutada erinevaid mudeleid ja suurusi. Võite kasutada LLM-i/SLM-i või servita kaugfunktsiooni, et saata päringuid vastavalt keerukusele kõige sobivamatele mudelitele. See aitab samuti kulusid vähendada ja samal ajal tagada jõudluse õigetel ülesannetel. Näiteks suunake lihtsad päringud väiksematele, kiirematele mudelitele ning kasutage kallimaid suuri mudeleid ainult keerukate mõtlemisülesannete jaoks.

**Vastuste vahemällu salvestamine:** Üldlevinud päringute ja ülesannete tuvastamine ning vastuste pakkumine enne, kui need läbivad teie agendi süsteemi, on hea viis sarnaste päringute mahu vähendamiseks. Võite isegi rakendada voogu, et tuvastada, kui sarnane päring on teie vahemällu salvestatud päringutega, kasutades selleks lihtsamaid tehisintellekti mudeleid. See strateegia võib märkimisväärselt vähendada kulusid sagedamini esitatavate küsimuste või tavapäraste töövoogude korral.

## Vaatame, kuidas see praktikas toimib

Selles [peatüki näidis-märkmikus](./code_samples/10-expense_claim-demo.ipynb) näeme näiteid, kuidas saame kasutada jälgimistööriistu oma agendi jälgimiseks ja hindamiseks.


### Kas sul on AI-agentide tootmises kasutamise kohta veel küsimusi?

Liitu [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppijatega, osaleda kontoritundides ja saada vastused oma AI-agentide küsimustele.

## Eelmine õppetund

[Metakognitsiooni disainimuster](../09-metacognition/README.md)

## Järgmine õppetund

[Agentlikud protokollid](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->