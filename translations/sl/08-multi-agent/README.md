[![Večagentni načrti](../../../translated_images/sl/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kliknite zgornjo sliko za ogled videa te lekcije)_

# Večagentni načrti oblikovanja

Takoj, ko začnete delati na projektu, ki vključuje več agentov, je treba upoštevati večagentni vzorec oblikovanja. Vendar pa morda ni takoj jasno, kdaj preiti na več agente in kakšne so prednosti.

## Uvod

V tej lekciji si bomo odgovorili na naslednja vprašanja:

- V katerih scenarijih se več agentov uporablja?
- Kakšne so prednosti uporabe več agentov v primerjavi z enim samim agentom, ki opravlja več nalog?
- Kateri so gradniki za implementacijo večagentnega vzorca oblikovanja?
- Kako lahko vidimo, kako več agentov medsebojno sodeluje?

## Cilji učenja

Po tej lekciji boste znali:

- Prepoznati scenarije, kjer so več agentov primerni
- Razumeti prednosti uporabe več agentov v primerjavi z enim samim agentom.
- Poglobljeno razumeti gradnike za implementacijo večagentnega vzorca oblikovanja.

Kakšna je širša slika?

*Več agentov je vzorec oblikovanja, ki omogoča več agentom sodelovanje za dosego skupnega cilja*.

Ta vzorec se pogosto uporablja na različnih področjih, vključno z robotiko, avtonomnimi sistemi in distribuiranim računalništvom.

## Scenariji, kjer so več agentov primerni

Kateri scenariji so primerni za uporabo več agentov? Odgovor je, da je veliko scenarijev, kjer je uporaba več agentov koristna, posebej v naslednjih primerih:

- **Velike delovne obremenitve**: Velike delovne obremenitve je mogoče razdeliti na manjše naloge in dodeliti različnim agentom, kar omogoča vzporedno obdelavo in hitrejše dokončanje. Primer tega je velika naloga obdelave podatkov.
- **Zahtevne naloge**: Zahtevne naloge, podobno kot velike delovne obremenitve, je mogoče razdeliti na manjše podnaloge in dodeliti različnim agentom, ki se specializirajo za določen vidik naloge. Dober primer so avtonomna vozila, kjer različni agenti upravljajo navigacijo, zaznavanje ovir in komunikacijo z drugimi vozili.
- **Raznolika strokovnost**: Različni agenti imajo lahko različno strokovnost, kar jim omogoča učinkovitejše ravnanje z različnimi vidiki naloge kot en sam agent. Dober primer je zdravstvo, kjer agenti upravljajo diagnostiko, načrte zdravljenja in nadzor bolnikov.

## Prednosti uporabe več agentov v primerjavi z enim samim agentom

Ena-agentni sistem lahko dobro deluje za preproste naloge, vendar pa uporaba več agentov pri bolj zahtevnih nalogah prinaša več prednosti:

- **Specializacija**: Vsak agent se lahko specializira za določeno nalogo. Pomanjkanje specializacije pri enem agentu pomeni, da ima ta agent naloge vsega, vendar se lahko zmede pri zapleteni nalogi in morda opravlja nalogo, za katero ni najbolj primeren.
- **Razširljivost**: Lažje je razširiti sistem z dodajanjem več agentov kot z obremenjevanjem enega samega agenta.
- **Odpornost na napake**: Če en agent odpove, drugi lahko nadaljujejo s svojo funkcijo, kar zagotavlja zanesljivost sistema.

Poglejmo primer – rezervirajmo potovanje za uporabnika. Ena-agentni sistem bi moral upravljati vse aspekte postopka rezervacije, od iskanja letov do rezervacije hotelov in najema avtomobilov. Za to bi potreboval orodja za vse te naloge, kar bi lahko povzročilo kompleksen in monolitni sistem, ki ga je težko vzdrževati in razširjati. Sistem z več agenti pa bi imel različne agente, specializirane za iskanje letov, rezervacijo hotelov in najem avtomobilov. To bi sistem naredilo modularnejši, lažji za vzdrževanje in razširljiv.

Primerjajte to s potovalno agencijo, ki deluje kot majhna družinska trgovina, v nasprotju s franšizo potovalnih agencij. Majhna družinska trgovina ima enega agenta, ki upravlja vse vidike rezervacije, medtem ko ima franšiza različne agente za različne vidike procesa rezervacije.

## Gradniki za implementacijo večagentnega vzorca oblikovanja

Preden lahko implementirate večagentni vzorec oblikovanja, morate razumeti gradnike, ki sestavljajo ta vzorec.

To naredimo bolj konkretno na primeru rezervacije potovanja za uporabnika. Gradniki vključujejo:

- **Komunikacija med agenti**: Agenti za iskanje letov, rezervacijo hotelov in najem avtomobilov morajo komunicirati in deliti informacije o uporabnikovih željah in omejitvah. Treba je določiti protokole in metode za to komunikacijo. Konkretno to pomeni, da mora agent za iskanje letov komunicirati z agentom za rezervacijo hotelov, da zagotovita, da je hotel rezerviran za iste datume kot let. To zahteva, da si agenti delijo podatke o uporabnikovih potovalnih datumih, kar pomeni, da morate določiti *kateri agenti delijo informacije in kako jih delijo*.
- **Mehanizmi koordinacije**: Agenti morajo usklajevati svoja dejanja, da zagotovijo, da so izpolnjene uporabnikove želje in omejitve. Uporabnikova želja bi lahko bila, da želi hotel blizu letališča, medtem ko je omejitev, da so avtomobili za najem na voljo samo na letališču. To pomeni, da mora agent za rezervacijo hotelov sodelovati z agentom za najem avtomobilov, da zagotovita skladnost s željami in omejitvami uporabnika. Potrebno je določiti *kako agenti usklajujejo svoja dejanja*.
- **Arhitektura agenta**: Agenti morajo imeti notranjo strukturo za sprejemanje odločitev in učenje iz interakcij z uporabnikom. To pomeni, da mora agent za iskanje letov imeti strukturo za odločanje o tem, katere lete priporočiti uporabniku. To pomeni, da morate določiti *kako agenti sprejemajo odločitve in se učijo iz interakcij z uporabnikom*. Primer tega je, da agent za iskanje letov uporablja strojno učenje za priporočanje letov na podlagi preteklih želja uporabnika.
- **Vidljivost v interakcije več agentov**: Potrebno je imeti pregled nad tem, kako več agentov medsebojno sodeluje. To zahteva orodja in tehnike za sledenje aktivnostim in interakcijam agentov. To so lahko orodja za beleženje in nadzor, orodja za vizualizacijo in merilniki uspešnosti.
- **Vzorce več agentov**: Obstajajo različni vzorci za implementacijo večagentnih sistemov, kot so centralizirana, decentralizirana in hibridna arhitektura. Treba je izbrati vzorec, ki najbolj ustreza vaši uporabi.
- **Človek v zanki**: V večini primerov imate v sistemu tudi človeka, ki ga morate usmeriti, kdaj naj agenti zahtevajo človeški poseg. To je lahko v obliki uporabnika, ki zahteva določen hotel ali let, ki ga agenti niso priporočili, ali pa zahteva potrditev pred rezervacijo leta ali hotela.

## Vidljivost v interakcije več agentov

Pomembno je, da imate jasno sliko o tem, kako več agentov medsebojno deluje. Ta vidljivost je ključna za odpravljanje napak, optimizacijo in zagotavljanje učinkovitosti celotnega sistema. Za to potrebujete orodja in metode za sledenje aktivnosti in interakciji agentov. To so lahko orodja za beleženje in nadzor, vizualizacijska orodja in metrika uspešnosti.

Na primer, pri rezervaciji potovanja za uporabnika bi lahko imeli nadzorno ploščo, ki prikazuje stanje posameznih agentov, uporabnikove želje in omejitve ter interakcije med agenti. Ta plošča bi pokazala potovalne datume uporabnika, lete, ki jih priporoča agent za lete, hotele, ki jih priporoča hotel agent, in avtomobile za najem, ki jih priporoča agent za najem avtomobilov. Tako bi dobili jasen vpogled v to, kako agenti sodelujejo in ali so upoštevane želje in omejitve uporabnika.

Poglejmo podrobneje te vidike.

- **Orodja za beleženje in nadzor**: Želite zabeležiti vsako dejanje agenta. Vpis v dnevnik lahko shrani podatke o agentu, ki je izvedel dejanje, dejanje samo, čas izvedbe in rezultat dejanja. Te informacije se nato uporabijo za odpravljanje napak, optimizacijo in drugo.
- **Vizualizacijska orodja**: Vizualizacija lahko pomaga videti interakcije med agenti na intuitiven način. Na primer, lahko imate graf, ki prikazuje tok informacij med agenti. To lahko pomaga prepoznati ozka grla, neučinkovitosti in druge težave v sistemu.
- **Meritve uspešnosti**: Merilniki uspešnosti pomagajo spremljati učinkovitost večagentnega sistema. Na primer, spremljate lahko čas za opravljanje naloge, število opravljenih nalog na enoto časa in natančnost priporočil agentov. Te informacije pomagajo prepoznati možnosti za izboljšave in optimizirati sistem.

## Vzorci več agentov

Poglejmo si nekaj konkretnih vzorcev, ki jih lahko uporabimo za ustvarjanje večagentnih aplikacij. Tukaj je nekaj zanimivih vzorcev:

### Skupinski pogovor

Ta vzorec je uporaben, ko želite ustvariti aplikacijo za skupinski pogovor, kjer lahko več agentov medsebojno komunicira. Tipični primeri uporabe so timsko sodelovanje, podpora strankam in družabna omrežja.

V tem vzorcu vsak agent predstavlja uporabnika v skupinskem pogovoru, sporočila pa se izmenjujejo med agenti prek protokola sporočanja. Agenti lahko pošiljajo sporočila v skupinski pogovor, prejemajo sporočila iz skupine in odgovarjajo na sporočila drugih agentov.

Ta vzorec se lahko implementira z centralizirano arhitekturo, kjer so vsa sporočila posredovana prek centralnega strežnika, ali decentralizirano arhitekturo, kjer se sporočila izmenjujejo neposredno.

![Skupinski pogovor](../../../translated_images/sl/multi-agent-group-chat.ec10f4cde556babd.webp)

### Prenos nalog

Ta vzorec je uporaben, ko želite ustvariti aplikacijo, kjer lahko več agentov prenaša naloge drug drugemu.

Tipični primeri uporabe vključujejo podporo strankam, upravljanje nalog in avtomatizacijo delovnih tokov.

V tem vzorcu vsak agent predstavlja nalogo ali korak v delovnem toku, agenti pa lahko naloge prenašajo drugim agentom na podlagi vnaprej določenih pravil.

![Prenos nalog](../../../translated_images/sl/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Sodelovalno filtriranje

Ta vzorec je uporaben, ko želite ustvariti aplikacijo, kjer lahko več agentov sodeluje pri pripravi priporočil za uporabnike.

Razlog za sodelovanje več agentov je ta, da ima vsak agent drugačno strokovno znanje in lahko na različne načine prispeva k postopku priporočanja.

Vzemimo primer, kjer uporabnik želi priporočilo za najboljšo delnico za nakup na borzi.

- **Strokovnjak za panogo**: Eden izmed agentov je strokovnjak za določeno industrijo.
- **Tehnična analiza**: Drugi agent je strokovnjak za tehnično analizo.
- **Temeljna analiza**: Tretji agent je strokovnjak za temeljno analizo. S sodelovanjem ti agenti lahko uporabniku ponudijo bolj celovito priporočilo.

![Priporočilo](../../../translated_images/sl/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenarij: Postopek vračila

Predstavljajte si scenarij, kjer stranka poskuša dobiti vračilo za izdelek. V tem postopku je lahko vključenih kar nekaj agentov, vendar jih razdelimo na agente, specifične za ta postopek, in splošne agente, ki se uporabljajo tudi v drugih postopkih.

**Agenti, specifični za postopek vračila**:

Naslednji agenti bi lahko bili vključeni v postopek vračila:

- **Agent za stranko**: Ta agent predstavlja stranko in je odgovoren za začetek postopka vračila.
- **Agent za prodajalca**: Ta agent predstavlja prodajalca in je odgovoren za obdelavo vračila.
- **Agent za plačilo**: Ta agent predstavlja plačilni proces in je odgovoren za vračilo plačila stranki.
- **Agent za rešitve**: Ta agent predstavlja rešitev težav in je odgovoren za reševanje težav, ki nastanejo med postopkom vračila.
- **Agent za skladnost**: Ta agent zagotavlja, da postopek vračila ustreza zakonodaji in interno politiko.

**Splošni agenti**:

Ti agenti se lahko uporabljajo tudi v drugih delih vašega poslovanja.

- **Agent za pošiljanje**: Ta agent upravlja postopke pošiljanja in je odgovoren za vračilo izdelka prodajalcu. Uporablja se lahko tako v postopku vračila kot pri splošni dostavi izdelkov.
- **Agent za povratne informacije**: Ta agent zbira povratne informacije strank. Povratne informacije se lahko zbirajo kadarkoli, ne samo med postopkom vračila.
- **Agent za eskalacijo**: Ta agent je odgovoren za eskalacijo težav na višjo raven podpore. Takšnega agenta lahko uporabite v katerem koli postopku, kjer je potrebna eskalacija.
- **Agent za obveščanje**: Agent, ki pošilja obvestila stranki v različnih fazah postopka vračila.
- **Agent za analitiko**: Ta agent analizira podatke, povezane s postopkom vračila.
- **Agent za revizijo**: Ta agent preverja postopek vračila, da zagotovi pravilno izvedbo.
- **Agent za poročanje**: Ta agent pripravlja poročila o postopku vračila.
- **Agent za znanje**: Ta agent vzdržuje bazo znanja, povezano s postopkom vračila. Lahko ima znanje tako o vračilih kot tudi o drugih delih vašega poslovanja.
- **Agent za varnost**: Ta agent zagotavlja varnost procesa vračila.
- **Agent za kakovost**: Ta agent skrbi za zagotavljanje kakovosti postopka vračila.

Naštetih je kar nekaj agentov, tako specifičnih za postopek vračila kot tudi splošnih, ki se lahko uporabljajo v drugih delih vašega poslovanja. Upamo, da vam to pomaga razumeti, kako se odločiti, katere agente uporabiti v vašem večagentnem sistemu.

## Naloga

Naredite načrt večagentnega sistema za postopek podpore strankam. Prepoznajte vključene agente, njihove vloge in odgovornosti ter način njihovega medsebojnega sodelovanja. Upoštevajte tako agente, specifične za podporo strankam, kot tudi splošne agente, ki se lahko uporabljajo v drugih delih vašega poslovanja.
> Premislite, preden preberete naslednjo rešitev, morda potrebujete več agentov, kot mislite.

> NAMIG: Pomislite na različne faze procesa podpore strankam in tudi na agente, potrebne za vsak sistem.

## Rešitev

[Rešitev](./solution/solution.md)

## Preverjanje znanja

Vprašanje: Kdaj bi morali razmisliti o uporabi več agentov?

- [ ] A1: Ko imate majhno delovno obremenitev in enostavno nalogo.
- [ ] A2: Ko imate veliko delovno obremenitev
- [ ] A3: Ko imate enostavno nalogo.

[Rešitev kviza](./solution/solution-quiz.md)

## Povzetek

V tej lekciji smo si ogledali vzorec večagentnega oblikovanja, vključno s scenariji, kjer je uporaba več agentov primerna, prednosti uporabe več agentov v primerjavi z enim samim agentom, gradnike za izvajanje vzorca večagentnega oblikovanja in kako dobiti pregled nad tem, kako medsebojno delujejo različni agenti.

### Imate več vprašanj o večagentnem vzorcu oblikovanja?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), da se srečate z drugimi učenci, sodelujete v urah za vprašanja in dobite odgovore na vaša vprašanja o AI agentih.

## Dodatni viri

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentacija Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Vzorce agentnega oblikovanja</a>

## Prejšnja lekcija

[Načrtovanje oblikovanja](../07-planning-design/README.md)

## Naslednja lekcija

[Metakognicija v AI agentih](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Opozorilo**:  
Ta dokument je bil preveden z uporabo storitve za AI prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->