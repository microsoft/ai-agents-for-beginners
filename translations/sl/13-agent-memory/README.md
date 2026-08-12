# Pomnilnik za AI agente
[![Pomnilnik agenta](../../../translated_images/sl/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Ko razpravljamo o edinstvenih koristih ustvarjanja AI agentov, se večinoma govorita dve stvari: možnost klicanja orodij za dokončanje nalog in sposobnost izboljševanja skozi čas. Pomnilnik je temelj ustvarjanja samoučečega se agenta, ki lahko ustvarja boljše izkušnje za naše uporabnike.

V tej lekciji si bomo ogledali, kaj je pomnilnik za AI agente in kako ga lahko upravljamo ter uporabljamo v dobro naših aplikacij.

## Uvod

Ta lekcija bo pokrila:

• **Razumevanje pomnilnika AI agenta**: Kaj je pomnilnik in zakaj je za agente ključen.

• **Implementacija in shranjevanje pomnilnika**: Praktične metode za dodajanje zmogljivosti pomnilnika vašim AI agentom, s poudarkom na kratkoročnem in dolgoročnem pomnilniku.

• **Samoučeči se AI agenti**: Kako pomnilnik omogoča agentom, da se učijo iz preteklih interakcij in se izboljšujejo skozi čas.

## Razpoložljive implementacije

Ta lekcija vključuje dva obsežna vodiča v zvezkih:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementira pomnilnik z uporabo Mem0 in Azure AI Search z Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementira strukturiran pomnilnik z uporabo Cognee, ki samodejno gradi graf znanja, podprt z vdelavami, vizualizira graf in omogoča inteligentno iskanje

## Cilji učenja

Po zaključku te lekcije boste znali:

• **Ločiti med različnimi vrstami pomnilnika AI agentov**, vključno z delovnim, kratkoročnim in dolgoročnim pomnilnikom, pa tudi specializiranimi oblikami, kot sta persona in epizodični pomnilnik.

• **Implementirati in upravljati kratkoročni in dolgoročni pomnilnik za AI agente** z uporabo Microsoft Agent Framework, pri čemer izkoristite orodja, kot so Mem0, Cognee, Whiteboard memory ter integracijo z Azure AI Search.

• **Razumeti načela samoučečih se AI agentov** in kako robustni sistemi upravljanja pomnilnika prispevajo k neprestanemu učenju in prilagajanju.

## Razumevanje pomnilnika AI agenta

V svoji jedrnatosti **pomnilnik za AI agente pomeni mehanizme, ki jim dovolijo ohraniti in priklicati informacije**. Te informacije so lahko posebni podatki o pogovoru, uporabniške preference, pretekla dejanja ali celo naučeni vzorci.

Brez pomnilnika so AI aplikacije pogosto brezstatične, kar pomeni, da se vsak stik začne znova. To vodi do ponavljajoče in frustrirajoče uporabniške izkušnje, kjer agent "pozabi" prejšnji kontekst ali preference.

### Zakaj je pomnilnik pomemben?

Inteligenca agenta je močno povezana z njegovo sposobnostjo priklica in uporabe preteklih informacij. Pomnilnik agentom omogoča:

• **Reflektivnost**: Učenje iz preteklih dejanj in rezultatov.

• **Interaktivnost**: Ohranjanje konteksta skozi tekoči pogovor.

• **Proaktivnost in reaktivnost**: Predvidevanje potreb ali primeren odziv na podlagi zgodovinskih podatkov.

• **Avtonomnost**: Delovanje bolj samostojno, z uporabo shranjenega znanja.

Cilj implementacije pomnilnika je, da so agenti bolj **zanesljivi in zmogljivi**.

### Vrste pomnilnika

#### Delovni pomnilnik

Razmislite o tem kot o listu za priboljške, ki ga agent uporablja med eno tekočo nalogo ali miselnim procesom. Vsebuje neposredne informacije, potrebne za izračun naslednjega koraka.

Za AI agente delovni pomnilnik pogosto zajema najbolj pomembne informacije iz pogovora, tudi če je cela zgodovina pogovora dolga ali okrnjena. Osredotoča se na izluščitev ključnih elementov, kot so zahteve, predlogi, odločitve in dejanja.

**Primer delovnega pomnilnika**

Pri agentu za rezervacijo potovanj bi delovni pomnilnik lahko zajel trenutno uporabnikovo zahtevo, na primer "Želim rezervirati potovanje v Pariz". Ta specifična zahteva je shranjena v neposrednem kontekstu agenta za usmerjanje trenutne interakcije.

#### Kratkoročni pomnilnik

Ta vrsta pomnilnika ohranja informacije za trajanje enega pogovora ali seje. Je kontekst trenutnega klepeta, ki agentu omogoča sklicevanje nazaj na prejšnje zanke v dialogu.

V vzorcih Python SDK Microsoft Agent Frameworka ([https://github.com/microsoft/agent-framework](https://github.com/microsoft/agent-framework)) to ustreza `AgentSession`, ki je ustvarjen z `agent.create_session()`. Seja je vgrajeni kratkoročni pomnilnik v okviru: ohranja kontekst pogovora med uporabo iste seje, vendar ta kontekst ne vztraja, ko seja konča ali ko se aplikacija ponovno zažene. Za dejstva in preference, ki morajo preživeti več sej, uporabite dolgoročni pomnilnik, običajno preko baze podatkov, vektorskega indeksa ali druge trajne shrambe.

**Primer kratkoročnega pomnilnika**

Če uporabnik vpraša, "Koliko bi stal let v Pariz?" in nato nadaljuje z "Kaj pa nastanitev tam?", kratkoročni pomnilnik zagotovi, da agent ve, da "tam" znotraj istega pogovora pomeni "Pariz".

#### Dolgoročni pomnilnik

To so informacije, ki ostajajo ohranjene skozi več pogovorov ali sej. Omogoča agentom, da si zapomnijo uporabniške preference, zgodovinske interakcije ali splošno znanje skozi daljša obdobja. To je pomembno za personalizacijo.

**Primer dolgoročnega pomnilnika**

Dolgoročni pomnilnik bi lahko shranil, da "Ben uživa v smučanju in dejavnostih na prostem, rad pije kavo s pogledom na gore in se želi izogibati zahtevnim smučarskim progama zaradi pretekle poškodbe". Te informacije, pridobljene iz prejšnjih interakcij, vplivajo na priporočila v prihodnjih sejah načrtovanja potovanj, zaradi česar so zelo personalizirana.

#### Persona pomnilnik

Ta specializirana vrsta pomnilnika pomaga agentu razviti dosledno "osebnost" ali "persono". Omogoča agentu, da si zapomni podrobnosti o sebi ali svoji predvideni vlogi, zaradi česar so interakcije bolj tekoče in osredotočene.

**Primer persona pomnilnika**
Če je potovalni agent zasnovan kot "strokovnjak za smučarsko načrtovanje", lahko persona pomnilnik poudari to vlogo, s čimer njegovi odzivi odražajo ton in znanje strokovnjaka.

#### Delovni/epizodični pomnilnik

Ta pomnilnik shranjuje zaporedje korakov, ki jih agent opravi med zapleteno nalogo, vključno z uspehi in neuspehi. Je kot spominjanje določenih "epizod" ali preteklih izkušenj za učenje iz njih.

**Primer epizodičnega pomnilnika**

Če je agent poskušal rezervirati določen let, pa je bil neuspešen zaradi razpoložljivosti, bi epizodični pomnilnik lahko zabeležil ta neuspeh, kar agentu omogoča, da poskusi alternativne lete ali uporabnika bolj informirano obvesti o težavi ob naslednjem poskusu.

#### Pomnilnik entitet

To vključuje izluščanje in pomnjenje določenih entitet (kot so ljudje, kraji ali stvari) in dogodkov iz pogovorov. Omogoča agentu, da ustvari strukturiran pregled ključnih obravnavanih elementov.

**Primer pomnilnika entitet**

Iz pogovora o preteklem potovanju bi agent lahko izluščil "Pariz", "Eifflov stolp" in "večerja v restavraciji Le Chat Noir" kot entitete. Pri prihodnji interakciji bi se agent lahko spomnil "Le Chat Noir" in ponudil novo rezervacijo tam.

#### Strukturirani RAG (Retrieval Augmented Generation)

Medtem ko je RAG širša tehnika, je "Strukturirani RAG" izpostavljen kot zmogljiva tehnologija pomnilnika. Izlušči gosto, strukturirano informacijo iz različnih virov (pogovori, e-pošta, slike) in jo uporablja za izboljšanje natančnosti, priklica in hitrosti odgovorov. Za razliko od klasičnega RAG, ki temelji zgolj na semantični podobnosti, strukturirani RAG deluje z inherentno strukturo informacij.

**Primer strukturiranega RAG-a**

Namesto da se ustavi pri ujemanju ključnih besed, bi strukturirani RAG lahko razčlenil podrobnosti leta (destinacija, datum, čas, letalska družba) iz e-pošte in jih shranil strukturirano. To omogoča natančna vprašanja, kot npr. "Kateri let sem rezerviral za Pariz v torek?"

## Implementacija in shranjevanje pomnilnika

Implementacija pomnilnika za AI agente vključuje sistematičen postopek **upravljanja pomnilnika**, ki vključuje ustvarjanje, shranjevanje, priklic, integracijo, posodabljanje in celo "pozabljanje" (ali brisanje) informacij. Priklic je še posebej ključni vidik.

### Specializirana orodja za pomnilnik

#### Mem0

Eden od načinov za shranjevanje in upravljanje pomnilnika agenta je uporaba specializiranih orodij, kot je Mem0. Mem0 deluje kot trajna plast pomnilnika, ki agentom omogoča priklic relevantnih interakcij, shranjevanje uporabniških preferenc in dejanskega konteksta ter učenje iz uspehov in neuspehov skozi čas. Ideja je tukaj, da se stateless agenti spremenijo v stateful.

Deluje skozi **dvostopenjski proces pomnilnika: izvleček in posodobitev**. Najprej se sporočila, dodana v nit agenta, pošljejo storitvi Mem0, ki uporablja velik jezikovni model (LLM) za povzetek zgodovine pogovora in izluščitev novih spominov. Nato faza posodobitve, ki jo vodi LLM, odloči, ali je treba te spomine dodati, spremeniti ali izbrisati, pri čemer jih shrani v hibridni podatkovni sistem, ki lahko vključuje vektorske, grafične in ključ-vrednost baze podatkov. Ta sistem podpira različne vrste pomnilnika ter lahko vključi tudi grafični pomnilnik za upravljanje odnosov med entitetami.

#### Cognee

Drugi zmogljiv pristop je uporaba **Cognee**, odprtokodnega semantičnega pomnilnika za AI agente, ki pretvarja strukturirane in nestrukturirane podatke v poizvedljiv graf znanja, podprt z vdelavami. Cognee nudi **dvo-trgovinsko arhitekturo** koja združuje vektorsko iskanje podobnosti z grafičnimi odnosi, kar agentom omogoča razumevanje ne le podobnosti informacij, ampak tudi, kako so pojmi medsebojno povezani.

Izjemen je v **hibridnem priklicu**, ki združuje vektorsko podobnost, grafično strukturo in sklepanje LLM – od iskanja surovih kosov podatkov do odgovarjanja s pomočjo grafov. Sistem vzdržuje **živi pomnilnik**, ki se razvija in raste, hkrati pa ostaja poizvedljiv kot ena povezana grafična struktura, podpira tako kratkoročni kontekst seje kot dolgoročni trajni pomnilnik.

Vodič v zvezku Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) prikazuje gradnjo te enotne pomnilniške plasti, s praktičnimi primeri vnosa različnih podatkovnih virov, vizualizacije grafa znanja in poizvedovanja z različnimi strategijami iskanja, prilagojenimi specifičnim potrebam agenta.

### Shranjevanje pomnilnika z RAG

Poleg specializiranih orodij za pomnilnik, kot je Mem0, lahko izkoristite zmogljive iskalne storitve, kot je **Azure AI Search kot podlago za shranjevanje in priklic spominov**, še posebej za strukturirani RAG.

To omogoča, da so odgovori vašega agenta utemeljeni na vaših podatkih, kar zagotavlja relevantnejše in natančnejše odgovore. Azure AI Search lahko uporablja za shranjevanje uporabniških spominov o potovanjih, katalogov izdelkov ali katerega koli drugega specifičnega področja.

Azure AI Search podpira zmožnosti, kot je **strukturirani RAG**, ki odlično izvleče in pridobi gosto, strukturirano informacijo iz velikih zbirk podatkov, kot so zgodovine pogovorov, e-pošta ali celo slike. To nudi "nadčloveško natančnost in priklic" v primerjavi s tradicionalnim razbijanjem besedila in pristopi z vdelavami.

## Samopopravila AI agentov

Pogost vzorec za samopopravila agente vključuje uvedbo **"agenta znanja"**. Ta ločeni agent opazuje glavni pogovor med uporabnikom in primarnim agentom. Njegova vloga je:

1. **Identificirati dragocene informacije**: Določiti, ali je del pogovora vreden shranjevanja kot splošno znanje ali specifično uporabniško preferenco.

2. **Izluščiti in povzeti**: Izluščiti bistveno učno vsebino ali preferenco iz pogovora.

3. **Shranjeno v bazo znanja**: Trajno shraniti to izluščeno informacijo, pogosto v vektorski bazi podatkov, da jo je mogoče pozneje priklicati.

4. **Dopolniti prihodnje poizvedbe**: Ko uporabnik sproži novo poizvedbo, agent znanja prikliče relevantne shranjene informacije in jih doda uporabnikovemu pozivu, s čimer zagotovi ključen kontekst primarnemu agentu (podobno kot RAG).

### Optimizacije za pomnilnik

• **Upravljanje zamud (latency)**: Da se izognemo upočasnitvi uporabniških interakcij, se lahko sprva uporablja cenejši in hitrejši model za hitro preverjanje, ali so informacije vredne shranjevanja ali priklica, pri čemer se bolj zapleten postopek izvlečka/priklica sproži le po potrebi.

• **Vzdrževanje baze znanja**: Za rastočo bazo znanja se manj pogosto uporabljene informacije lahko premaknejo v "hladno shrambo", da se zmanjša stroške.

## Imate več vprašanj o pomnilniku agenta?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) za srečanje z drugimi učenci, udeležbo na urah odprtih vrat in odgovore na vaša vprašanja o AI agentih.
## Prejšnja lekcija

[Inženiring konteksta za AI agente](../12-context-engineering/README.md)

## Naslednja lekcija

[Raziščite Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->