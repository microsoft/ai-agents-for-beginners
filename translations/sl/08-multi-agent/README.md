<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T23:14:55+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "sl"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.sl.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kliknite na zgornjo sliko za ogled videoposnetka te lekcije)_

# Vzorci oblikovanja več agentov

Ko začnete delati na projektu, ki vključuje več agentov, morate razmisliti o vzorcu oblikovanja več agentov. Vendar pa morda ni takoj jasno, kdaj preklopiti na več agentov in kakšne so prednosti.

## Uvod

V tej lekciji bomo poskušali odgovoriti na naslednja vprašanja:

- Kateri so scenariji, kjer so več agenti primerni?
- Kakšne so prednosti uporabe več agentov v primerjavi z enim samim agentom, ki opravlja več nalog?
- Kateri so gradniki za implementacijo vzorca oblikovanja več agentov?
- Kako lahko spremljamo, kako več agentov medsebojno sodeluje?

## Cilji učenja

Po tej lekciji boste lahko:

- Prepoznali scenarije, kjer so več agenti primerni.
- Razumeli prednosti uporabe več agentov v primerjavi z enim samim agentom.
- Razumeli gradnike za implementacijo vzorca oblikovanja več agentov.

Kaj je širša slika?

*Več agentov je vzorec oblikovanja, ki omogoča več agentom sodelovanje za dosego skupnega cilja.*

Ta vzorec se pogosto uporablja na različnih področjih, vključno z robotiko, avtonomnimi sistemi in porazdeljenim računalništvom.

## Scenariji, kjer so več agenti primerni

Kateri scenariji so primerni za uporabo več agentov? Odgovor je, da obstaja veliko scenarijev, kjer je uporaba več agentov koristna, zlasti v naslednjih primerih:

- **Velike delovne obremenitve**: Velike delovne obremenitve je mogoče razdeliti na manjše naloge in jih dodeliti različnim agentom, kar omogoča vzporedno obdelavo in hitrejše dokončanje. Primer tega je obdelava velike količine podatkov.
- **Zapletene naloge**: Zapletene naloge, podobno kot velike delovne obremenitve, je mogoče razdeliti na manjše podnaloge in jih dodeliti različnim agentom, ki se specializirajo za določen vidik naloge. Dober primer tega so avtonomna vozila, kjer različni agenti upravljajo navigacijo, zaznavanje ovir in komunikacijo z drugimi vozili.
- **Raznolika strokovnost**: Različni agenti lahko imajo različno strokovnost, kar jim omogoča učinkovitejše obvladovanje različnih vidikov naloge kot enemu samemu agentu. Primer tega je zdravstvena oskrba, kjer agenti upravljajo diagnostiko, načrte zdravljenja in spremljanje pacientov.

## Prednosti uporabe več agentov v primerjavi z enim samim agentom

Sistem z enim samim agentom lahko dobro deluje pri enostavnih nalogah, vendar pri bolj zapletenih nalogah uporaba več agentov prinaša več prednosti:

- **Specializacija**: Vsak agent se lahko specializira za določeno nalogo. Pomanjkanje specializacije pri enem samem agentu pomeni, da imate agenta, ki lahko opravlja vse, vendar se lahko zmede, ko se sooči z zapleteno nalogo. Na primer, lahko opravi nalogo, za katero ni najbolj usposobljen.
- **Razširljivost**: Sisteme je lažje razširiti z dodajanjem več agentov kot z obremenjevanjem enega samega agenta.
- **Odpornost na napake**: Če en agent odpove, lahko drugi še naprej delujejo, kar zagotavlja zanesljivost sistema.

Vzemimo primer rezervacije potovanja za uporabnika. Sistem z enim samim agentom bi moral obravnavati vse vidike postopka rezervacije potovanja, od iskanja letov do rezervacije hotelov in najema avtomobilov. Da bi to dosegel, bi moral imeti agent orodja za obravnavo vseh teh nalog. To bi lahko privedlo do zapletenega in monolitnega sistema, ki ga je težko vzdrževati in razširiti. Sistem z več agenti pa bi lahko imel različne agente, specializirane za iskanje letov, rezervacijo hotelov in najem avtomobilov. To bi sistem naredilo bolj modularen, lažje vzdrževan in razširljiv.

Primerjajte to s turistično agencijo, ki jo vodi družinska trgovina, v primerjavi s turistično agencijo, ki jo vodi franšiza. Družinska trgovina bi imela enega agenta, ki obravnava vse vidike postopka rezervacije potovanja, medtem ko bi franšiza imela različne agente, ki obravnavajo različne vidike postopka rezervacije potovanja.

## Gradniki za implementacijo vzorca oblikovanja več agentov

Preden lahko implementirate vzorec oblikovanja več agentov, morate razumeti gradnike, ki sestavljajo ta vzorec.

Poglejmo to bolj konkretno z zgledom rezervacije potovanja za uporabnika. V tem primeru bi gradniki vključevali:

- **Komunikacija med agenti**: Agenti za iskanje letov, rezervacijo hotelov in najem avtomobilov morajo komunicirati in deliti informacije o uporabnikovih željah in omejitvah. Odločiti se morate o protokolih in metodah za to komunikacijo. Konkretno to pomeni, da mora agent za iskanje letov komunicirati z agentom za rezervacijo hotelov, da zagotovi, da je hotel rezerviran za iste datume kot let. To pomeni, da morajo agenti deliti informacije o uporabnikovih datumih potovanja, kar pomeni, da morate odločiti *kateri agenti delijo informacije in kako jih delijo*.
- **Mehanizmi koordinacije**: Agenti morajo usklajevati svoja dejanja, da zagotovijo, da so uporabnikove želje in omejitve izpolnjene. Uporabnikova želja bi lahko bila, da želi hotel blizu letališča, medtem ko bi omejitev lahko bila, da so najem avtomobili na voljo le na letališču. To pomeni, da mora agent za rezervacijo hotelov usklajevati z agentom za najem avtomobilov, da zagotovi, da so uporabnikove želje in omejitve izpolnjene. To pomeni, da morate odločiti *kako agenti usklajujejo svoja dejanja*.
- **Arhitektura agenta**: Agenti morajo imeti notranjo strukturo za sprejemanje odločitev in učenje iz interakcij z uporabnikom. To pomeni, da mora agent za iskanje letov imeti notranjo strukturo za sprejemanje odločitev o tem, katere lete priporočiti uporabniku. To pomeni, da morate odločiti *kako agenti sprejemajo odločitve in se učijo iz interakcij z uporabnikom*. Primeri, kako se agent uči in izboljšuje, bi lahko bili, da agent za iskanje letov uporablja model strojnega učenja za priporočanje letov uporabniku na podlagi njegovih preteklih želja.
- **Vidljivost interakcij med agenti**: Morate imeti vidljivost, kako več agentov medsebojno sodeluje. To pomeni, da morate imeti orodja in tehnike za sledenje dejavnostim in interakcijam agentov. To bi lahko bilo v obliki orodij za beleženje in spremljanje, orodij za vizualizacijo in meril uspešnosti.
- **Vzorci več agentov**: Obstajajo različni vzorci za implementacijo sistemov z več agenti, kot so centralizirane, decentralizirane in hibridne arhitekture. Odločiti se morate za vzorec, ki najbolje ustreza vašemu primeru uporabe.
- **Človek v zanki**: V večini primerov boste imeli človeka v zanki in morate agentom dati navodila, kdaj naj zaprosijo za človeško posredovanje. To bi lahko bilo v obliki uporabnika, ki zahteva določen hotel ali let, ki ga agenti niso priporočili, ali zahteva potrditev pred rezervacijo leta ali hotela.

## Vidljivost interakcij med agenti

Pomembno je, da imate vidljivost, kako več agentov medsebojno sodeluje. Ta vidljivost je ključna za odpravljanje napak, optimizacijo in zagotavljanje učinkovitosti celotnega sistema. Da to dosežete, morate imeti orodja in tehnike za sledenje dejavnostim in interakcijam agentov. To bi lahko bilo v obliki orodij za beleženje in spremljanje, orodij za vizualizacijo in meril uspešnosti.

Na primer, v primeru rezervacije potovanja za uporabnika bi lahko imeli nadzorno ploščo, ki prikazuje stanje vsakega agenta, uporabnikove želje in omejitve ter interakcije med agenti. Ta nadzorna plošča bi lahko prikazovala uporabnikove datume potovanja, lete, ki jih priporoča agent za lete, hotele, ki jih priporoča agent za hotele, in najem avtomobilov, ki jih priporoča agent za najem avtomobilov. To bi vam dalo jasen pogled na to, kako agenti medsebojno sodelujejo in ali so uporabnikove želje in omejitve izpolnjene.

Poglejmo podrobneje vsak od teh vidikov.

- **Orodja za beleženje in spremljanje**: Želite beležiti vsako dejanje, ki ga izvede agent. Vnos v dnevnik lahko vsebuje informacije o agentu, ki je izvedel dejanje, izvedenem dejanju, času izvedbe dejanja in rezultatu dejanja. Te informacije lahko nato uporabite za odpravljanje napak, optimizacijo in drugo.

- **Orodja za vizualizacijo**: Orodja za vizualizacijo vam lahko pomagajo videti interakcije med agenti na bolj intuitiven način. Na primer, lahko imate graf, ki prikazuje tok informacij med agenti. To vam lahko pomaga prepoznati ozka grla, neučinkovitosti in druge težave v sistemu.

- **Merila uspešnosti**: Merila uspešnosti vam lahko pomagajo spremljati učinkovitost sistema z več agenti. Na primer, lahko spremljate čas, potreben za dokončanje naloge, število nalog, dokončanih na enoto časa, in natančnost priporočil, ki jih podajo agenti. Te informacije vam lahko pomagajo prepoznati področja za izboljšave in optimizirati sistem.

## Vzorci več agentov

Poglejmo nekaj konkretnih vzorcev, ki jih lahko uporabimo za ustvarjanje aplikacij z več agenti. Tukaj je nekaj zanimivih vzorcev, ki jih je vredno upoštevati:

### Skupinski klepet

Ta vzorec je uporaben, ko želite ustvariti aplikacijo za skupinski klepet, kjer lahko več agentov medsebojno komunicira. Tipični primeri uporabe tega vzorca vključujejo sodelovanje v ekipi, podporo strankam in družabna omrežja.

V tem vzorcu vsak agent predstavlja uporabnika v skupinskem klepetu, sporočila pa se izmenjujejo med agenti z uporabo protokola za sporočanje. Agenti lahko pošiljajo sporočila v skupinski klepet, prejemajo sporočila iz skupinskega klepeta in odgovarjajo na sporočila drugih agentov.

Ta vzorec je mogoče implementirati z uporabo centralizirane arhitekture, kjer se vsa sporočila usmerjajo prek centralnega strežnika, ali decentralizirane arhitekture, kjer se sporočila izmenjujejo neposredno.

![Skupinski klepet](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.sl.png)

### Predaja nalog

Ta vzorec je uporaben, ko želite ustvariti aplikacijo, kjer lahko več agentov medsebojno predaja naloge.

Tipični primeri uporabe tega vzorca vključujejo podporo strankam, upravljanje nalog in avtomatizacijo delovnih tokov.

V tem vzorcu vsak agent predstavlja nalogo ali korak v delovnem toku, agenti pa lahko predajajo naloge drugim agentom na podlagi vnaprej določenih pravil.

![Predaja nalog](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.sl.png)

### Sodelovalno filtriranje

Ta vzorec je uporaben, ko želite ustvariti aplikacijo, kjer lahko več agentov sodeluje pri podajanju priporočil uporabnikom.

Zakaj bi želeli, da več agentov sodeluje? Ker ima lahko vsak agent različno strokovnost in lahko na različne načine prispeva k procesu priporočanja.

Vzemimo primer, kjer uporabnik želi priporočilo za najboljšo delnico za nakup na borzi.

- **Strokovnjak za industrijo**: En agent bi lahko bil strokovnjak za določeno industrijo.
- **Tehnična analiza**: Drug agent bi lahko bil strokovnjak za tehnično analizo.
- **Temeljna analiza**: Tretji agent pa bi lahko bil strokovnjak za temeljno analizo. S sodelovanjem lahko ti agenti uporabniku podajo bolj celovito priporočilo.

![Priporočilo](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.sl.png)

## Scenarij: Postopek vračila denarja

Razmislimo o scenariju, kjer stranka poskuša dobiti vračilo za izdelek. V tem procesu je lahko vključenih kar nekaj agentov, vendar jih razdelimo na agente, specifične za ta proces, in splošne agente, ki jih je mogoče uporabiti v drugih procesih.

**Agenti, specifični za postopek vračila denarja**:

Naslednji so nekateri agenti, ki bi lahko bili vključeni v postopek vračila denarja:

- **Agent stranke**: Ta agent predstavlja stranko in je odgovoren za začetek postopka vračila denarja.
- **Agent prodajalca**: Ta agent predstavlja prodajalca in je odgovoren za obdelavo vračila denarja.
- **Agent plačil**: Ta agent predstavlja proces plačil in je odgovoren za vračilo strankinega plačila.
- **Agent za reševanje težav**: Ta agent predstavlja proces reševanja težav in je odgovoren za reševanje morebitnih težav, ki se pojavijo med postopkom vračila denarja.
- **Agent za skladnost**: Ta agent predstavlja proces skladnosti in je odgovoren za zagotavljanje, da postopek vračila denarja ustreza predpisom in politikam.

**Splošni agenti**:

Ti agenti se lahko uporabljajo v drugih delih vašega poslovanja.

- **Agent za pošiljanje**: Ta agent predstavlja proces pošiljanja in je odgovoren za pošiljanje izdelka nazaj prodajalcu. Ta agent se lahko uporablja tako za postopek vračila denarja kot za splošno pošiljanje izdelka, na primer ob nakupu.
- **Agent za povratne informacije**: Ta agent predstavlja proces povratnih informacij in je odgovoren za zbiranje povratnih informacij od stranke. Povratne informacije je mogoče pridobiti kadarkoli, ne le med postopkom vračila denarja.
- **Agent za eskalacijo**: Ta agent predstavlja proces eskalacije in je odgovoren za eskalacijo težav na višjo raven podpore. Ta tip agenta lahko uporabite v kateremkoli procesu, kjer je treba eskalirati težavo.
- **Agent za obveščanje**: Ta agent predstavlja proces obveščanja in je odgovoren za pošiljanje obvestil stranki na različnih stopnjah postopka vračila denarja.
- **Agent za analitiko**: Ta agent predstavlja proces analitike in je odgovoren za analizo podatkov, povezanih s postopkom vračila denarja.
- **Agent za revizijo**: Ta agent predstavlja proces revizije in je odgovoren za revizijo postopka vračila denarja, da zagotovi, da se izvaja pravilno.
- **Agent za poročanje**: Ta agent predstavlja proces poročanja in je odgovoren za ustvarjanje poročil o postopku vračila denarja.
- **Agent za znanje**: Ta agent predstavlja proces znanja in je odgovoren za vzdrževanje baze znanja, povezane s postopkom vračila denarja. Ta agent bi lahko bil seznanjen tako z vračili kot z drugimi deli vašega poslovanja.
- **Agent za varnost**: Ta agent predstavlja proces varnosti in je odgovoren za zagotavljanje varnosti postopka vračila denarja.
- **Agent za kakovost**: Ta agent predstavlja proces kakovosti in je odgovoren za zagotavljanje kakovosti postopka vračila denarja.

Naštetih je kar nekaj agentov, tako za specifični postopek vračila denarja kot za splošne agente, ki jih je mogoče uporabiti v drugih delih vašega poslovanja. Upamo, da vam to daje idejo, kako se lahko odločite, katere agente uporabiti v vašem sistemu z več agenti.

## Naloga
## Oblikovanje večagentnega sistema za proces podpore strankam

Identificirajte agente, vključene v proces, njihove vloge in odgovornosti ter kako medsebojno sodelujejo. Upoštevajte tako agente, specifične za proces podpore strankam, kot tudi splošne agente, ki jih je mogoče uporabiti v drugih delih vašega podjetja.

> Premislite, preden preberete naslednjo rešitev, morda boste potrebovali več agentov, kot si mislite.

> TIP: Razmislite o različnih fazah procesa podpore strankam in tudi o agentih, potrebnih za kateri koli sistem.

## Rešitev

[Rešitev](./solution/solution.md)

## Preverjanje znanja

Vprašanje: Kdaj bi morali razmisliti o uporabi večagentnega sistema?

- [ ] A1: Ko imate majhno delovno obremenitev in preprosto nalogo.
- [ ] A2: Ko imate veliko delovno obremenitev.
- [ ] A3: Ko imate preprosto nalogo.

[Rešitev kviza](./solution/solution-quiz.md)

## Povzetek

V tej lekciji smo obravnavali vzorec oblikovanja večagentnega sistema, vključno s scenariji, kjer so večagentni sistemi uporabni, prednostmi uporabe večagentnih sistemov v primerjavi z enim agentom, gradniki za implementacijo vzorca večagentnega sistema in kako pridobiti vpogled v interakcije med več agenti.

### Imate več vprašanj o vzorcu oblikovanja večagentnega sistema?

Pridružite se [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), da se povežete z drugimi učenci, se udeležite uradnih ur in dobite odgovore na svoja vprašanja o AI agentih.

## Dodatni viri

- 

## Prejšnja lekcija

[Načrtovanje oblikovanja](../07-planning-design/README.md)

## Naslednja lekcija

[Metakognicija pri AI agentih](../09-metacognition/README.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.