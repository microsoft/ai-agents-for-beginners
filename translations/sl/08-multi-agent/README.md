[![Multi-agentni oblikovalski vzorci](../../../translated_images/sl/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kliknite zgornjo sliko za ogled videa te lekcije)_

# Multi-agentni oblikovalski vzorci

Takoj, ko začnete delati na projektu, ki vključuje več agentov, boste morali upoštevati multi-agentni oblikovalski vzorec. Vendar pa morda takoj ni jasno, kdaj preiti na več agentov in kakšne so prednosti.

## Uvod

V tej lekciji bomo poskušali odgovoriti na naslednja vprašanja:

- Kateri scenariji so primerni za uporabo več agentov?
- Kakšne so prednosti uporabe več agentov v primerjavi s samo enim agentom, ki opravlja več nalog?
- Kateri so gradniki za implementacijo multi-agentnega oblikovalskega vzorca?
- Kako lahko vidimo, kako si med seboj medsebojno delujejo različni agenti?

## Cilji učenja

Po tej lekciji bi morali znati:

- Prepoznati scenarije, kjer so primerni multi-agentni sistemi
- Prepoznati prednosti uporabe več agentov v primerjavi z enim samim agentom.
- Razumeti gradnike implementacije multi-agentnega oblikovalskega vzorca.

Kaj je širša slika?

*Multi-agentni sistemi so oblikovalski vzorec, ki omogoča, da več agentov sodeluje pri doseganju skupnega cilja*.

Ta vzorec se široko uporablja na različnih področjih, vključno z robotiko, avtonomnimi sistemi in distribuiranim računalništvom.

## Scenariji, kjer so primerni multi-agenti

Kateri scenariji so torej primerna uporaba multi-agentov? Odgovor je, da je veliko scenarijev, kjer je koristno uporabiti več agentov, zlasti v naslednjih primerih:

- **Velike delovne obremenitve**: Velike delovne naloge je mogoče razdeliti na manjše naloge in jih dodeliti različnim agentom, kar omogoča vzporedno obdelavo in hitrejšo izvedbo. Primer tega je primer velike naloge obdelave podatkov.
- **Zapletene naloge**: Zapletene naloge, podobno kot velike delovne obremenitve, lahko razdelimo na manjše podnaloge in jih dodelimo različnim agentom, ki so specializirani za določen vidik naloge. Dober primer tega so avtonomna vozila, kjer različni agenti upravljajo navigacijo, zaznavanje ovir in komunikacijo z drugimi vozili.
- **Različne strokovnosti**: Različni agenti imajo lahko različne strokovne veščine, kar jim omogoča, da učinkoviteje obvladujejo različne vidike naloge kot en sam agent. Dober primer tega je zdravstvena oskrba, kjer agenti upravljajo diagnostiko, načrte zdravljenja in spremljanje pacienta.

## Prednosti uporabe multi-agentov v primerjavi z enim samim agentom

Sistem z enim samim agentom bi lahko deloval dobro za preproste naloge, vendar pa uporaba več agentov za bolj zahtevne naloge prinaša več prednosti:

- **Specializacija**: Vsak agent je lahko specializiran za določeno nalogo. Pomanjkanje specializacije pri enem agentu pomeni, da agent lahko opravlja vse, a se lahko zmede pri zahtevnih nalogah. Na primer lahko opravi nalogo, za katero ni najbolj primeren.
- **Razširljivost**: Lažje je razširjati sisteme z dodajanjem več agentov kot preobremenitvijo enega samega agenta.
- **Odpornost na napake**: Če eden od agentov odpove, drugi lahko nadaljujejo z delovanjem, kar zagotavlja zanesljivost sistema.

Vzemimo primer, rezervirajmo potovanje za uporabnika. Sistem z enim agentom bi moral obvladati vse vidike postopka rezervacije, od iskanja letov do rezervacije hotelov in izposoje vozil. Da to doseže z enim agentom, bi ta agent potreboval orodja za vse te naloge, kar bi lahko privedlo do kompleksnega in monolitnega sistema, ki je težko vzdrževati in razširiti. Multi-agentni sistem pa lahko ima različne agente, specializirane za iskanje letov, rezervacijo hotelov in izposojo avtomobilov. To naredi sistem bolj modularen, lažji za vzdrževanje in razširljiv.

Primerjajmo to z potovalno agencijo v lasti družine proti franšizi potovalnih agencij. Družinska agencija bi imela enega agenta, ki upravlja vse vidike postopka rezervacije, medtem ko bi franšiza imela različne agente, ki upravljajo različne vidike postopka rezervacije.

## Gradniki implementacije multi-agentnega oblikovalskega vzorca

Preden lahko implementirate multi-agentni oblikovalski vzorec, morate razumeti gradnike, ki sestavljajo vzorec.

Ponovno naredimo primer bolj konkreten z rezervacijo potovanja za uporabnika. V tem primeru gradniki vključujejo:

- **Komunikacija agentov**: Agenti za iskanje letov, rezervacijo hotelov in avtomobilov morajo komunicirati in si izmenjevati informacije o preferencah in omejitvah uporabnika. Odločiti se morate o protokolih in metodah te komunikacije. Konkretno to pomeni, da mora agent za iskanje letov komunicirati z agentom za rezervacijo hotelov, da zagotovi, da je hotel rezerviran za enake datume kot let. To pomeni, da si morajo agenti deliti informacije o datumih potovanja uporabnika, kar pomeni, da morate odločiti *kateri agenti si delijo informacije in kako si jih delijo*.
- **Koordinacijski mehanizmi**: Agenti morajo usklajevati svoja dejanja, da zagotovijo, da se upoštevajo preference in omejitve uporabnika. Uporabnikova preference bi lahko bila, da želi hotel blizu letališča, medtem ko je omejitev, da so najemi avtomobilov na voljo samo na letališču. To pomeni, da mora agent za rezervacijo hotelov koordinirati z agentom za rezervacijo avtomobilov, da se upoštevajo preference in omejitve uporabnika. To pomeni, da morate odločiti *kako agenti usklajujejo svoja dejanja*.
- **Arhitektura agentov**: Agenti morajo imeti notranjo strukturo za sprejemanje odločitev in učenje iz interakcij z uporabnikom. To pomeni, da mora agent za iskanje letov imeti notranjo strukturo za odločanje o tem, katere lete priporočiti uporabniku. To pomeni, da morate odločiti *kako agenti sprejemajo odločitve in se učijo iz interakcij z uporabnikom*. Primer, kako se agent uči in izboljšuje, je, da bi agent za iskanje letov lahko uporabil model strojnega učenja za priporočanje letov uporabniku na podlagi preteklih preferenc.
- **Vidljivost interakcij med agenti**: Potrebujete vidljivost, kako si med seboj medsebojno delujejo mnogi agenti. To pomeni, da potrebujete orodja in tehnike za spremljanje aktivnosti in interakcij agentov. To je lahko v obliki orodij za beleženje in nadzor, vizualizacijskih orodij in metrik zmogljivosti.
- **Vzorci multi-agentnih sistemov**: Obstajajo različni vzorci za implementacijo multi-agentnih sistemov, kot so centralizirane, decentralizirane in hibridne arhitekture. Potrebno je odločiti se za vzorec, ki najbolje ustreza vašemu primeru uporabe.
- **Človek v zanki**: V večini primerov bo človek v zanki in morate agente navesti, kdaj naj zahtevajo človeški poseg. To je lahko v obliki uporabnika, ki zahteva določen hotel ali let, ki ga agenti niso priporočili, ali zahtevajo potrditev pred rezervacijo leta ali hotela.

## Vidljivost v interakcije med multi-agenti

Pomembno je, da imate vidljivost, kako si med seboj medsebojno delujejo mnogi agenti. Ta vidljivost je bistvena za odpravljanje napak, optimizacijo in zagotavljanje splošne učinkovitosti sistema. Da bi to dosegli, potrebujete orodja in tehnike za sledenje aktivnosti in interakcij agentov. To je lahko v obliki orodij za beleženje in nadzor, vizualizacijskih orodij in meritev zmogljivosti.

Na primer, pri rezervaciji potovanja za uporabnika bi lahko imeli nadzorno ploščo, ki prikazuje stanje vsakega agenta, uporabniške preference in omejitve ter interakcije med agenti. Ta nadzorna plošča bi lahko prikazovala datume potovanja uporabnika, lete, ki jih priporoča agent za lete, hotele, ki jih priporočajo agenti za hotele, in avtomobile za najem, ki jih priporočajo agenti za avtomobile. Tako bi imeli jasen pregled, kako se agenti medsebojno obnašajo in ali se upoštevajo uporabniške preference in omejitve.

Podrobneje si oglejmo vsak od teh vidikov.

- **Orodja za beleženje in nadzor**: Želite beležiti vsako dejanje, ki ga izvede agent. Vnos v dnevnik bi lahko shranil informacije o agentu, ki je izvedel dejanje, katero dejanje je bilo izvedeno, kdaj je bilo izvedeno in kakšen je bil izid. Te informacije se lahko nato uporabijo za odpravljanje napak, optimizacijo in drugo.

- **Vizualizacijska orodja**: Vizualizacijska orodja vam lahko pomagajo videti interakcije med agenti na bolj intuitiven način. Na primer, lahko imate graf, ki prikazuje potek informacij med agenti. To vam lahko pomaga prepoznati ozka grla, neučinkovitosti in druge težave v sistemu.

- **Metrike zmogljivosti**: Metrike zmogljivosti vam lahko pomagajo spremljati učinkovitost multi-agentnega sistema. Na primer, lahko merite čas, potreben za dokončanje naloge, število opravljenih nalog na enoto časa in natančnost priporočil, ki jih podajo agenti. Te informacije vam lahko pomagajo prepoznati področja za izboljšave in optimizacijo sistema.

## Multi-agentni vzorci

Pogledali si bomo nekaj konkretnih vzorcev, ki jih lahko uporabimo za ustvarjanje multi-agentnih aplikacij. Tukaj je nekaj zanimivih vzorcev, ki jih je vredno upoštevati:

### Skupinski klepet

Ta vzorec je uporaben, če želite ustvariti aplikacijo za skupinski klepet, kjer lahko več agentov komunicira med seboj. Tipični primeri uporabe za ta vzorec vključujejo timsko sodelovanje, podporo strankam in družbena omrežja.

V tem vzorcu vsak agent predstavlja uporabnika v skupinskem klepetu, sporočila pa si izmenjujejo med agenti z uporabo protokola za sporočanje. Agenti lahko pošiljajo sporočila v skupinski klepet, prejemajo sporočila iz skupinskega klepeta in odgovarjajo na sporočila drugih agentov.

Ta vzorec je mogoče implementirati z centralizirano arhitekturo, kjer so vsa sporočila usmerjena skozi osrednji strežnik, ali decentralizirano arhitekturo, kjer se sporočila izmenjujejo neposredno.

![Skupinski klepet](../../../translated_images/sl/multi-agent-group-chat.ec10f4cde556babd.webp)

### Prenos nalog (Hand-off)

Ta vzorec je uporaben, če želite ustvariti aplikacijo, kjer si lahko več agentov prenaša naloge.

Tipični primeri uporabe tega vzorca vključujejo podporo strankam, upravljanje nalog in avtomatizacijo delovnih procesov.

V tem vzorcu vsak agent predstavlja nalogo ali korak v delovnem toku, agenti pa lahko naloge prenašajo drugim agentom glede na vnaprej določena pravila.

![Prenos nalog](../../../translated_images/sl/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Kolaborativno filtriranje

Ta vzorec je uporaben, če želite ustvariti aplikacijo, kjer lahko več agentov sodeluje pri izdelavi priporočil uporabnikom.

Razlog, zakaj želite, da več agentov sodeluje, je, da ima lahko vsak agent različne strokovne veščine in lahko na različne načine prispeva k postopku priporočanja.

Vzemimo primer, kjer uporabnik želi priporočilo za najboljši delniški nakup na borzi.

- **Strokovnjak za industrijo**: eden od agentov bi lahko bil strokovnjak za določeno industrijo.
- **Tehnična analiza**: drug agent bi lahko bil strokovnjak za tehnično analizo.
- **Temeljna analiza**: tretji agent bi lahko bil strokovnjak za temeljno analizo. Z medsebojnim sodelovanjem lahko ti agenti zagotovijo bolj celovito priporočilo uporabniku.

![Priporočilo](../../../translated_images/sl/multi-agent-filtering.d959cb129dc9f608.webp)

## Primer: Postopek vračila denarja

Upoštevajte scenarij, kjer kupec želi dobiti vračilo za izdelek, pri tem je lahko v postopek vključenih precej agentov, a jih bomo razdelili na agente, specifične za ta postopek, in splošne agente, ki jih lahko uporabljamo tudi za druge postopke.

**Agenti specifični za postopek vračila:**

Spodaj je nekaj agentov, ki bi lahko sodelovali v postopku vračila:

- **Agent za stranko**: ta agent predstavlja kupca in je odgovoren za začetek postopka vračila.
- **Agent za prodajalca**: ta agent predstavlja prodajalca in je odgovoren za obdelavo vračila.
- **Agent za plačila**: ta agent predstavlja postopek plačila in je odgovoren za vračilo plačila kupcu.
- **Agent za rešitve**: ta agent predstavlja postopek reševanja in je odgovoren za reševanje morebitnih težav med postopkom vračila.
- **Agent za skladnost**: ta agent predstavlja postopek skladnosti in je odgovoren za zagotavljanje, da postopek vračila ustreza predpisom in politikam.

**Splošni agenti:**

Ti agenti se lahko uporabljajo tudi v drugih delih vašega poslovanja.

- **Agent za pošiljanje**: ta agent predstavlja postopek pošiljanja in je odgovoren za vračilo izdelka prodajalcu. Ta agent se lahko uporablja tako za postopek vračila kot tudi za splošno pošiljanje izdelka ob nakupu.
- **Agent za povratne informacije**: ta agent predstavlja postopek zbiranja povratnih informacij in je odgovoren za zbiranje povratnih informacij od kupca. Povratne informacije lahko zbirate kadar koli, ne le med postopkom vračila.
- **Agent za eskalacijo**: ta agent predstavlja postopek eskalacije in je odgovoren za prenos težav na višjo raven podpore. Takšnega agenta lahko uporabite za vsak postopek, kjer je potrebna eskalacija.
- **Agent za obveščanje**: ta agent predstavlja postopek obveščanja in je odgovoren za pošiljanje obvestil kupcu v različnih fazah postopka vračila.
- **Agent za analitiko**: ta agent predstavlja analitični postopek in je odgovoren za analizo podatkov, povezanih s postopkom vračila.
- **Agent za revizijo**: ta agent predstavlja revizijski postopek in je odgovoren za pregled postopka vračila, da zagotovi, da poteka pravilno.
- **Agent za poročanje**: ta agent predstavlja poročevalski postopek in je odgovoren za ustvarjanje poročil o postopku vračila.
- **Agent za znanje**: ta agent predstavlja postopek upravljanja z znanjem in je odgovoren za vzdrževanje baze znanja informacij, povezanih s postopkom vračila. Ta agent bi lahko bil seznanjen tako z vračili kot drugimi deli vašega poslovanja.
- **Agent za varnost**: ta agent predstavlja varnostni postopek in je odgovoren za zagotavljanje varnosti postopka vračila.
- **Agent za kakovost**: ta agent predstavlja postopek nadzora kakovosti in je odgovoren za zagotavljanje kakovosti postopka vračila.

Prej je bilo naštetih kar nekaj agentov, tako za specifičen postopek vračila kot za splošne agente, ki jih lahko uporabljate tudi v drugih delih vašega poslovanja. Upamo, da vam to daje idejo, kako se lahko odločite, katere agente uporabiti v vašem multi-agentnem sistemu.

## Naloga

Oblikujte multi-agentni sistem za postopek podpore strankam. Prepoznajte agente, vključene v postopek, njihove vloge in odgovornosti ter kako medsebojno delujejo. Upoštevajte tako agente, specifične za postopek podpore strankam, kot tudi splošne agente, ki jih lahko uporabljate v drugih delih vašega poslovanja.


> Preden preberete naslednjo rešitev, malo pomislite, morda boste potrebovali več agentov, kot mislite.

> NAMIG: Razmislite o različnih fazah procesa podpore strankam in upoštevajte tudi agente, potrebne za kakršenkoli sistem.

## Rešitev

[Rešitev](./solution/solution.md)

## Preverjanje znanja

### Vprašanje 1

Kateri scenarij je najbolj primeren za sistem z več agenti?

- [ ] A1: Podporni bot odgovarja na pogosta vprašanja z uporabo ene baze znanja in majhne zbirke orodij.
- [ ] A2: Postopek vračila zahteva ločene vloge za prevarante, plačila in skladnost, vsak z lastnimi orodji, njihovi rezultati pa morajo biti usklajeni.
- [ ] A3: Enako preprosto zahtevo za klasifikacijo prejmemo na tisoče krat na uro.

### Vprašanje 2

Kdaj je običajno boljša izbira en sam agent?

- [ ] A1: Nalogo lahko obdelamo z eno skupino navodil in orodij, brez predaje specialistom.
- [ ] A2: Agent ima dostop do več kot enega orodja.
- [ ] A3: Postopek zahteva ločene vloge z različnimi dovoljenji in neodvisnimi revizijskimi sledmi.

[Rešitev kviza](./solution/solution-quiz.md)

## Povzetek

V tej lekciji smo si ogledali vzorec načrtovanja več agentov, vključno s scenariji, kjer so več agenti uporabni, prednostmi uporabe več agentov namesto enega samega, gradniki za implementacijo vzorca načrtovanja več agentov in kako imeti pregled nad tem, kako si med seboj medsebojno sodelujejo.

### Imate več vprašanj o vzorcu načrtovanja več agentov?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da se srečate z drugimi učenci, se udeležite uric in dobite odgovore na vprašanja o AI agentih.

## Dodatni viri

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentacija Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentni vzorci načrtovanja</a>


## Prejšnja lekcija

[Načrtovanje oblikovanja](../07-planning-design/README.md)

## Naslednja lekcija

[Metakognicija v AI agentih](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->