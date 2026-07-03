[![Multi-Agent Design](../../../translated_images/sl/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kliknite na zgornjo sliko za ogled videa te lekcije)_

# Vzorce večagentnega oblikovanja

Takoj, ko začnete delati na projektu, ki vključuje več agentov, boste morali upoštevati vzorec večagentnega oblikovanja. Vendar morda ni takoj jasno, kdaj preiti na več agentov in kakšne so prednosti.

## Uvod

V tej lekciji želimo odgovoriti na naslednja vprašanja:

- Kateri so scenariji, kjer je uporaba več agentov smiselna?
- Kakšne so prednosti uporabe več agentov v primerjavi z enim samim agentom, ki opravlja več nalog?
- Kakšni so gradniki za izvedbo vzorca večagentnega oblikovanja?
- Kako pridobimo pregled nad tem, kako se več agentov medsebojno povezuje?

## Cilji učenja

Po tej lekciji bi morali biti sposobni:

- Prepoznati scenarije, kjer je uporaba več agentov upravičena
- Prepoznati prednosti uporabe več agentov v primerjavi z enim agentom.
- Razumeti gradnike za izvedbo vzorca večagentnega oblikovanja.

Kakšna je širša slika?

*Več agentov je vzorec oblikovanja, ki omogoča, da več agentov sodeluje za dosego skupnega cilja*.

Ta vzorec se pogosto uporablja na različnih področjih, vključno z robotiko, avtonomnimi sistemi in distribuiranim računanjem.

## Scenariji, kjer je uporaba več agentov primerna

Kateri so torej scenariji, kjer je uporaba več agentov smiselna? Odgovor je, da je veliko scenarijev, kjer je uporaba več agentov koristna, zlasti v naslednjih primerih:

- **Velika delovna obremenitev**: Velike delovne obremenitve se lahko razdelijo na manjše naloge in dodelijo različnim agentom, kar omogoča vzporedno obdelavo in hitrejšo izvedbo. Primer tega je obdelava velikega podatkovnega nabora.
- **Zahtevne naloge**: Zahtevne naloge, podobno kot velike delovne obremenitve, je mogoče razdeliti na manjše podnaloge, ki jih izvajajo različni agenti, pri čemer vsak specializira določen vidik naloge. Dober primer je pri avtonomnih vozilih, kjer različni agenti upravljajo navigacijo, zaznavanje ovir in komunikacijo z drugimi vozili.
- **Raznolika ekspertiza**: Različni agenti imajo lahko raznolike strokovne sposobnosti, kar jim omogoča učinkovitejše reševanje različnih vidikov naloge kot en sam agent. Dober primer tega je v zdravstvu, kjer agenti upravljajo diagnostiko, načrte zdravljenja in spremljanje bolnikov.

## Prednosti uporabe več agentov v primerjavi z enim samim agentom

Sistem z enim agentom bi lahko dobro deloval za preproste naloge, vendar pa za bolj zahtevne naloge uporaba več agentov prinaša več prednosti:

- **Specializacija**: Vsak agent se lahko specializira za določeno nalogo. Pomanjkanje specializacije pri enem samem agentu pomeni, da ima agent zmožnost opravljati vse, a se lahko zmede pri zahtevnih nalogah. Na primer, lahko začne izvajati nalogo, za katero ni najbolj primeren.
- **Razširljivost**: Lažje je razširiti sistem z dodajanjem več agentov, namesto da bi preobremenjevali en sam agent.
- **Odpornost na napake**: Če en agent odpove, lahko drugi še naprej delujejo, kar zagotavlja zanesljivost sistema.

Vzemimo primer — rezervirajmo potovanje za uporabnika. Sistem z enim samim agentom bi moral obravnavati vse vidike procesa rezervacije potovanja, od iskanja letov do rezervacije hotelov in najema avta. Da bi to izvedel s samo enim agentom, bi agent potreboval orodja za upravljanje vseh teh nalog. To lahko privede do kompleksnega, monolitnega sistema, ki je težaven za vzdrževanje in razširjanje. Večagentni sistem pa lahko uporablja različne agente, specializirane za iskanje letov, rezervacijo hotelov in najem avtomobilov. To naredi sistem bolj modularen, lažji za vzdrževanje in razširljiv.

Primerjajmo to z agencijo za potovanja, ki jo vodi družinski par, v primerjavi z agencijo, ki deluje kot franšiza. V družinski agenciji bi en agent urejal vse vidike rezervacije potovanja, medtem ko bi v franšizi različni agenti urejali različne vidike procesa.

## Gradniki za izvedbo vzorca večagentnega oblikovanja

Preden lahko izvedete vzorec večagentnega oblikovanja, morate razumeti gradnike, ki tvorijo vzorec.

Naj to konkretiziramo z zgledom rezervacije potovanja za uporabnika. V tem primeru gradniki vključujejo:

- **Komunikacija agentov**: Agenti za iskanje letov, rezervacijo hotelov in najem avtomobilov morajo med seboj komunicirati ter si deliti informacije o uporabnikovih željah in omejitvah. Potrebno je določiti protokole in metode komunikacije. To pomeni konkretno, da agent, ki išče lete, mora komunicirati z agentom za rezervacijo hotelov, da se zagotovi, da je hotel rezerviran za iste datume kot let. To pomeni, da si agenti morajo deliti informacije o uporabnikovih datumih potovanja, kar pomeni, da je treba določiti, *kateri agenti delijo informacije in kako jih delijo*.
- **Mehanizmi koordinacije**: Agenti morajo usklajevati svoja dejanja, da zagotovijo, da so zadovoljene uporabnikove želje in omejitve. Na primer, uporabnikova želja je lahko hotel blizu letališča, medtem ko je omejitev, da so avtomobili za najem na voljo samo na letališču. Zato mora agent za rezervacijo hotelov sodelovati z agentom za najem avtomobilov, da se te želje in omejitve upoštevajo. To pomeni, da je treba določiti, *kako agenti usklajujejo svoja dejanja*.
- **Arhitektura agentov**: Agenti morajo imeti notranjo zgradbo za sprejemanje odločitev in učenje iz svojih interakcij z uporabnikom. To pomeni, da mora agent za iskanje letov imeti notranjo strukturo za odločanje o tem, katere lete priporočiti uporabniku. To pomeni, da je treba določiti, *kako agenti sprejemajo odločitve in se učijo iz interakcij z uporabnikom*. Primeri, kako agent uči in izboljšuje delovanje, so lahko, da agent za iskanje letov uporablja model strojnega učenja za priporočanje letov uporabniku na podlagi njegovih preteklih želja.
- **Pregled nad interakcijami več agentov**: Potrebujete pregled nad tem, kako se več agentov med seboj povezuje. To pomeni, da potrebujete orodja in tehnike za spremljanje dejavnosti in interakcij agentov. To je lahko v obliki beleženja in spremljanja, orodij za vizualizacijo ter metrik uspešnosti.
- **Vzorce večagentnega delovanja**: Za izvedbo večagentnih sistemov obstajajo različni vzorci, kot so centralizirane, decentralizirane in hibridne arhitekture. Potrebno je izbrati vzorec, ki najbolje ustreza vaši uporabi.
- **Človek v zanki**: V večini primerov boste imeli človeka v zanki in agentom boste morali navesti, kdaj naj zahtevajo človeško posredovanje. To je lahko v obliki uporabnika, ki zahteva določen hotel ali let, ki ga agenti niso priporočili, ali potrditve pred rezervacijo leta ali hotela.

## Pregled nad interakcijami več agentov

Pomembno je, da imate pregled nad tem, kako se več agentov med seboj povezuje. Ta pregled je ključen za odpravljanje napak, optimizacijo in zagotavljanje učinkovitosti sistema. Za dosego tega potrebujete orodja in tehnike za spremljanje dejavnosti in interakcij agentov. To je lahko v obliki beleženja in spremljanja, orodij za vizualizacijo in meril uspešnosti.

Na primer, pri rezervaciji potovanja uporabnika lahko imate nadzorno ploščo, ki prikazuje status vsakega agenta, uporabnikove želje in omejitve ter interakcije med agenti. Ta nadzorna plošča lahko prikazuje datume potovanja uporabnika, lete, ki jih je priporočil agent za lete, hotele, ki jih je priporočil agent za hotele, in avtomobile za najem, ki jih je priporočil agent za najem avtomobilov. To vam daje jasen vpogled v to, kako agenti sodelujejo, in ali so uporabnikove želje ter omejitve izpolnjene.

Poglejmo si te vidike podrobneje.

- **Orodja za beleženje in spremljanje**: Želite beležiti vsako dejanje, ki ga opravi agent. Vpis v dnevnik lahko shrani informacije o agentu, ki je izvedel dejanje, katere dejanje je bilo, kdaj je bilo izvedeno in rezultat dejanja. Te informacije se uporabljajo za odpravljanje napak, optimizacijo in več.
- **Orodja za vizualizacijo**: Vizualizacijska orodja pomagajo videti interakcije med agenti na bolj intuitiven način. Na primer, lahko imate graf, ki prikazuje tok informacij med agenti. To vam lahko pomaga odkriti ozka grla, neučinkovitosti in druge težave v sistemu.
- **Metrične merilke uspešnosti**: Merilke uspešnosti vam pomagajo spremljati učinkovitost večagentnega sistema. Na primer, lahko spremljate čas, potreben za dokončanje naloge, število nalog, opravljenih v določenem času, in natančnost priporočil, ki jih agenti dajajo. Te informacije pomagajo prepoznati področja za izboljšave in optimizirati sistem.

## Vzorci več agentov

Poglobimo se v nekaj konkretnih vzorcev, ki jih lahko uporabimo za ustvarjanje večagentnih aplikacij. Tukaj je nekaj zanimivih vzorcev, ki jih je vredno razmisliti:

### Skupinski klepet

Ta vzorec je uporaben, ko želite ustvariti aplikacijo skupinskega klepeta, kjer lahko več agentov medsebojno komunicira. Tipične uporabe vključujejo sodelovanje v ekipah, podporo strankam in socialna omrežja.

V tem vzorcu vsak agent predstavlja uporabnika v skupinskem klepetu, sporočila pa se izmenjujejo med agenti z uporabo protokola za sporočila. Agenti lahko pošiljajo sporočila v skupinski klepet, prejemajo sporočila od skupinskega klepeta in odgovarjajo na sporočila drugih agentov.

Ta vzorec se lahko uresniči z centralizirano arhitekturo, kjer so vsa sporočila usmerjena preko osrednjega strežnika, ali z decentralizirano arhitekturo, kjer se sporočila izmenjujejo neposredno.

![Group chat](../../../translated_images/sl/multi-agent-group-chat.ec10f4cde556babd.webp)

### Predaja

Ta vzorec je uporaben, ko želite ustvariti aplikacijo, kjer lahko več agentov medsebojno predaja naloge.

Tipične uporabe vključujejo podporo strankam, upravljanje nalog in avtomatizacijo delovnih tokov.

V tem vzorcu vsak agent predstavlja nalogo ali korak v delovnem toku, agenti pa lahko naloge predajajo drugim agentom na podlagi predhodno določenih pravil.

![Hand off](../../../translated_images/sl/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Sodelovalno filtriranje

Ta vzorec je uporaben, ko želite ustvariti aplikacijo, kjer lahko več agentov sodeluje pri podajanju priporočil uporabnikom.

Razlog za sodelovanje več agentov je, da ima vsak agent različna strokovna znanja in lahko na različne načine prispeva k procesu priporočanja.

Vzemimo primer, kjer uporabnik želi priporočilo za najboljšo delnico za nakup na borzi.

- **Strokovnjak za industrijo**: En agent je lahko strokovnjak za določeno industrijo.
- **Tehnična analiza**: Drug agent je lahko strokovnjak za tehnično analizo.
- **Temeljna analiza**: Tretji agent pa je lahko strokovnjak za temeljno analizo. S sodelovanjem lahko ti agenti uporabniku zagotovijo bolj celovito priporočilo.

![Recommendation](../../../translated_images/sl/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenarij: Postopek vračila

Predstavljajte si scenarij, kjer stranka poskuša dobiti vračilo za izdelek. V tem procesu lahko sodeluje precej agentov, vendar jih razdelimo na agente, specifične za ta postopek, in na splošne agente, ki jih lahko uporabljamo v drugih procesih.

**Agenti, specifični za postopek vračila**:

Naslednji agenti bi lahko sodelovali v postopku vračila:

- **Agent kupca**: Ta agent predstavlja kupca in je odgovoren za začetek postopka vračila.
- **Agent prodajalca**: Ta agent predstavlja prodajalca in je odgovoren za obdelavo vračila.
- **Agent za plačila**: Ta agent predstavlja plačilni proces in je odgovoren za vračilo kupčevega plačila.
- **Agent za reševanje**: Ta agent upravlja proces reševanja morebitnih težav, ki se pojavijo med vračilom.
- **Agent za skladnost**: Ta agent zagotavlja, da postopek vračila ustreza vsem pravilnikom in predpisom.

**Splošni agenti**:

Te agente lahko uporabljajo tudi drugi deli vašega poslovanja.

- **Agent za dostavo**: Ta agent predstavlja proces dostave in je odgovoren za vračilo izdelka prodajalcu. Lahko se uporablja tako v postopku vračila kot za splošno pošiljanje izdelka ob nakupu.
- **Agent za povratne informacije**: Ta agent upravlja z zbiranjem povratnih informacij od kupcev. Povratne informacije so lahko zbrane kadar koli in ne zgolj med postopkom vračila.
- **Agent za eskalacijo**: Ta agent je odgovoren za eskalacijo težav na višjo raven podpore. Takšnega agenta lahko uporabite za vsak proces, kjer je potrebna eskalacija težav.
- **Agent za pošiljanje obvestil**: Ta agent pošilja obvestila kupcu v različnih fazah postopka vračila.
- **Agent za analitiko**: Ta agent analizira podatke, povezane s postopkom vračila.
- **Agent za revizijo**: Ta agent opravlja revizijo postopka vračila, da zagotovi pravilno izvedbo.
- **Agent za poročanje**: Ta agent generira poročila o postopku vračila.
- **Agent za znanje**: Ta agent upravlja z bazo znanja, povezano s postopkom vračila. Ta agent je lahko usposobljen tako za vračila kot tudi za druge dele vašega poslovanja.
- **Agent za varnost**: Ta agent skrbi za varnost postopka vračila.
- **Agent za kakovost**: Ta agent zagotavlja kakovost postopka vračila.

Prej je bilo navedenih precej agentov, tako za specifični postopek vračila kot tudi za splošne agente, ki jih lahko uporabljate v drugih delih vašega poslovanja. Upamo, da vam to daje predstavo, kako lahko določite, katere agente uporabiti v vašem večagentnem sistemu.

## Naloga

Oblikujte večagentni sistem za proces podpore strankam. Določite agente, vključene v proces, njihove vloge in odgovornosti ter kako medsebojno sodelujejo. Upoštevajte tako agente, specifične za proces podpore strankam, kot tudi splošne agente, ki jih lahko uporabljate v drugih delih vašega poslovanja.
> Premislite, preden preberete naslednjo rešitev, morda boste potrebovali več agentov, kot mislite.

> NAMIG: Premislite o različnih fazah procesa podpore strankam in upoštevajte tudi agente, ki so potrebni za vsak sistem.

## Rešitev

[Rešitev](./solution/solution.md)

## Preverjanja znanja

Vprašanje: Kdaj bi morali razmisliti o uporabi več agentov?

- [ ] A1: Ko imate malo dela in preprosto nalogo.
- [ ] A2: Ko imate veliko dela
- [ ] A3: Ko imate preprosto nalogo.

[Rešitev kviz](./solution/solution-quiz.md)

## Povzetek

V tej lekciji smo si ogledali vzorec načrtovanja več agentov, vključno s scenariji, kjer so več agenti primerni, prednosti uporabe več agentov pred enim samim agentom, gradnike za implementacijo vzorca načrtovanja več agentov in kako pridobiti vpogled v to, kako več agentov sodeluje med seboj.

### Imate več vprašanj o vzorcu načrtovanja več agentov?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da se srečate z drugimi učenci, udeležite ur uradnih ur in dobite odgovore na vaša vprašanja o AI agentih.

## Dodatni viri

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentacija Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentic vzorci načrtovanja</a>


## Prejšnja lekcija

[Načrtovanje oblikovanja](../07-planning-design/README.md)

## Naslednja lekcija

[Metakognicija v AI agentih](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->