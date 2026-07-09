# Pomnilnik za AI agente 
[![Agent Memory](../../../translated_images/sl/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Ko govorimo o edinstvenih prednostih ustvarjanja AI agentov, se običajno omenjata dve stvari: sposobnost klicanja orodij za dokončanje nalog in sposobnost izboljševanja skozi čas. Pomnilnik je temelj za ustvarjanje samoiniciativno izboljšujočega se agenta, ki lahko ustvarja boljše izkušnje za naše uporabnike.

V tej lekciji bomo pogledali, kaj je pomnilnik za AI agente in kako ga lahko upravljamo ter uporabljamo v korist naših aplikacij.

## Uvod

Ta lekcija bo zajemala:

• **Razumevanje pomnilnika AI agentov**: Kaj je pomnilnik in zakaj je bistven za agente.

• **Implementacija in shranjevanje pomnilnika**: Praktične metode za dodajanje zmogljivosti pomnilnika vašim AI agentom, s poudarkom na kratkoročnem in dolgoročnem pomnilniku.

• **Kako narediti AI agente samoiniciativno izboljšujoče**: Kako pomnilnik agentom omogoča učenje iz preteklih interakcij in izboljševanje skozi čas.

## Razpoložljive implementacije

Ta lekcija vključuje dva obsežna vadbenika v zvezku:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementira pomnilnik z uporabo Mem0 in Azure AI Search z Microsoft Agent Frameworkom

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementira strukturiran pomnilnik z uporabo Cognee, ki samodejno gradi znanstveni graf podprt z vdelavami, vizualizacijo grafa in inteligentnim iskanjem

## Cilji učenja

Po zaključku te lekcije boste vedeli, kako:

• **Razlikovati med različnimi vrstami pomnilnika AI agentov**, vključno s delovnim, kratkoročnim in dolgoročnim pomnilnikom, pa tudi specializiranimi oblikami, kot sta persona in epizodični pomnilnik.

• **Implementirati in upravljati kratkoročni in dolgoročni pomnilnik AI agentov** z uporabo Microsoft Agent Frameworka, pri čemer izkoristite orodja, kot so Mem0, Cognee, pomnilnik Whiteboard in integracija z Azure AI Search.

• **Razumeti načela delovanja samopopravčnih AI agentov** in kako robustni sistemi za upravljanje pomnilnika prispevajo k neprekinjenemu učenju in prilagajanju.

## Razumevanje pomnilnika AI agentov

V svoji jedrni funkciji **pomnilnik za AI agente označuje mehanizme, ki jim omogočajo hranjenje in priklic informacij**. Te informacije so lahko specifični podatki o pogovoru, uporabniške preference, pretekla dejanja ali celo naučeni vzorci.

Brez pomnilnika so AI aplikacije pogosto brez stanja, kar pomeni, da se vsaka interakcija začne znova. To vodi v ponavljajočo in frustrirajočo uporabniško izkušnjo, kjer agent "pozabi" prejšnji kontekst ali preference.

### Zakaj je pomnilnik pomemben?

Inteligenca agenta je tesno povezana z njegovo sposobnostjo priklica in uporabe preteklih informacij. Pomnilnik agentom omogoča, da so:

• **Refleksivni**: Učenje iz preteklih dejanj in rezultatov.

• **Interaktivni**: Ohranjanje konteksta skozi tekoči pogovor.

• **Proaktivni in reaktivni**: Predvidevanje potreb ali ustrezno odzivanje na osnovi zgodovinskih podatkov.

• **Avtonomni**: Delovanje bolj samostojno z uporabo shranjenega znanja.

Cilj implementacije pomnilnika je, da agenti postanejo bolj **zanesljivi in sposobni**.

### Vrste pomnilnika

#### Delovni pomnilnik

To lahko razumemo kot košček zvezka, ki ga agent uporablja med eno, tekočo nalogo ali miselnim procesom. Vsebuje takojšnje informacije, potrebne za izračun naslednjega koraka.

Za AI agente delovni pomnilnik pogosto zajame najpomembnejše informacije iz pogovora, tudi če je celotna zgodovina pogovora dolga ali omejena. Osredotoča se na izločanje ključnih elementov, kot so zahteve, predlogi, odločitve in dejanja.

**Primer delovnega pomnilnika**

V agentu za rezervacijo potovanj delovni pomnilnik lahko zajame trenutno zahtevo uporabnika, na primer "Želim rezervirati potovanje v Pariz". Ta specifična zahteva je v takojšnjem kontekstu agenta, da usmeri trenutno interakcijo.

#### Kratkoročni pomnilnik

Ta vrsta pomnilnika hrani informacije za trajanje posameznega pogovora ali seje. To je kontekst trenutnega klepeta, ki agentu omogoča sklicevanje na prejšnje poteze v dialogu.

V vzorcih Python SDK-ja [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) to ustreza `AgentSession`, ustvarjenemu z `agent.create_session()`. Seja je vgrajeni kratkoročni pomnilnik frameworka: ohranja kontekst pogovora na voljo med uporabo iste seje, vendar ta kontekst ni trajno shranjen, ko seja konča ali se aplikacija znova zažene. Za dejstva in preference, ki morajo preživeti sezono, uporabite dolgoročni pomnilnik, običajno prek baze podatkov, vektorskega indeksa ali drugega trajnega shranjevanja.

**Primer kratkoročnega pomnilnika**

Če uporabnik vpraša: "Koliko bi stal let v Pariz?" in nato nadaljuje s "Kaj pa nastanitev tam?", kratkoročni pomnilnik zagotovi, da agent ve, da "tam" v istem pogovoru pomeni "Pariz".

#### Dolgoročni pomnilnik

To so informacije, ki trajajo skozi več pogovorov ali sej. Omogoča agentom, da si zapomnijo uporabniške preference, zgodovinske interakcije ali splošno znanje za daljše obdobje. To je pomembno za personalizacijo.

**Primer dolgoročnega pomnilnika**

Dolgoročni pomnilnik lahko shrani, da "Ben uživa v smučanju in aktivnostih na prostem, rad pije kavo z razgledom na gore in želi se izogniti zahtevnim smučarskim progам zaradi pretekle poškodbe". Te informacije, pridobljene iz prejšnjih interakcij, vplivajo na priporočila v prihodnjih načrtih potovanj, zaradi česar so zelo personalizirana.

#### Pomnilnik personae

Ta specializirana vrsta pomnilnika agentu pomaga razviti dosledno "osebnost" ali "persono". Omogoča agentu, da si zapomni podrobnosti o sebi ali svoji vlogi, kar naredi interakcije bolj tekoče in osredotočene.

**Primer pomnilnika personae**
Če je agent za potovanja zasnovan kot "strokovnjak za načrtovanje smučanja," lahko pomnilnik personae okrepi to vlogo in vpliva na odgovore, ki ustrezajo tonu in znanju strokovnjaka.

#### Delovni/epizodični pomnilnik

Ta pomnilnik shranjuje zaporedje korakov, ki jih agent izvede med zapleteno nalogo, vključno z uspehi in neuspehi. Podobno kot pomnjenje določenih "epizod" ali preteklih izkušenj za učenje iz njih.

**Primer epizodičnega pomnilnika**

Če je agent poskušal rezervirati določen let, vendar je neuspešno zaradi nedosegljivosti, lahko epizodični pomnilnik zabeleži ta neuspeh, kar agentu omogoča poskus z alternativnimi leti ali bolj informirano obvestilo uporabniku o težavi pri naslednjem poskusu.

#### Pomnilnik entitet

Ta vključuje izločanje in pomnjenje specifičnih entitet (kot so osebe, kraji ali stvari) in dogodkov iz pogovorov. Omogoča agentu, da zgradi strukturirano razumevanje ključnih elementov, o katerih se pogovarjajo.

**Primer pomnilnika entitet**

Iz pogovora o preteklem potovanju bi agent lahko izločil "Pariz," "Eifflov stolp" in "večerja v restavraciji Le Chat Noir" kot entitete. V prihodnji interakciji bi agent lahko priklical "Le Chat Noir" in ponudil novo rezervacijo tam.

#### Strukturirani RAG (Retrieval Augmented Generation)

Medtem ko je RAG širša tehnika, je "strukturirani RAG" izpostavljen kot močna tehnologija pomnilnika. Izvleče gosto, strukturirano informacijo iz različnih virov (pogovorov, elektronskih sporočil, slik) in jo uporablja za izboljšanje natančnosti, priklica in hitrosti odgovorov. Za razliko od klasičnega RAG, ki se opira samo na semantično podobnost, strukturirani RAG dela z inherentno strukturo informacij.

**Primer strukturiranega RAG**

Namesto da zgolj primerja ključne besede, lahko strukturirani RAG izlušči podrobnosti o letu (cilj, datum, čas, letalska družba) iz e-pošte in jih shrani na strukturiran način. To omogoča natančna poizvedovanja, kot je "Kateri let sem rezerviral za Pariz v torek?"

## Implementacija in shranjevanje pomnilnika

Implementacija pomnilnika za AI agente vključuje sistematičen proces **upravljanja pomnilnika**, ki vključuje generiranje, shranjevanje, priklic, integracijo, posodabljanje in celo "pozabljanje" (ali brisanje) informacij. Priklic je še posebej ključen vidik.

### Specializirana orodja za pomnilnik

#### Mem0

Eden od načinov za shranjevanje in upravljanje pomnilnika agenta je uporaba specializiranih orodij, kot je Mem0. Mem0 deluje kot trajna plast pomnilnika, ki agentom omogoča priklic relevantnih interakcij, shranjevanje uporabniških preferenc in dejanskega konteksta ter učenje iz uspehov in neuspehov skozi čas. Ideja je, da se brezstanični agenti spremenijo v statične.

Deluje skozi **dvofazni proces pomnilnika: izvleček in posodobitev**. Najprej so sporočila, dodana v nit agenta, poslana storitvi Mem0, ki z uporabo velikega jezikovnega modela (LLM) povzema zgodovino pogovora in izvleče nove spomine. Nato faza posodobitve, ki jo vodi LLM, določi, ali jih je treba dodati, spremeniti ali izbrisati, in jih shrani v hibridno bazo podatkov, ki lahko vključuje vektorske, grafične in ključ-vrednost baze. Ta sistem podpira različne vrste pomnilnika in lahko vključuje grafični pomnilnik za upravljanje odnosov med entitetami.

#### Cognee

Drugi zmogljiv pristop je uporaba **Cognee**, odprtokodnega semantičnega pomnilnika za AI agente, ki strukturirane in nestrukturirane podatke pretvori v graf znanja, ki ga podpirajo vdelave. Cognee ponuja **dvojno arhitekturo shranjevanja**, ki združuje iskanje po vektorski podobnosti z grafskimi povezavami, kar agentom omogoča razumevanje ne samo podobnosti informacij, ampak tudi povezav med koncepti.

Odlikuje se v **hibridnem priklicu**, ki združuje vektorsko podobnost, grafično strukturo in sklepanje LLM - od iskanja surovih sekcij do odgovarjanja na vprašanja z zavedanjem grafa. Sistem ohranja **živi pomnilnik**, ki se razvija in raste, hkrati pa ostaja iskalno dostopen kot enoten povezan graf, podpira tako kratkoročni kontekst seje kot dolgoročni trajni pomnilnik.

Vadbenik v zvezku Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) prikazuje gradnjo te združene plasti pomnilnika, z praktičnimi primeri vključevanja različnih virov podatkov, vizualizacije grafa znanja in poizvedovanja z različnimi strategijami iskanja, prilagojenimi specifičnim potrebam agentov.

### Shranjevanje pomnilnika z RAG

Poleg specializiranih orodij za pomnilnik, kot je Mem0, lahko uporabite robustne storitve iskanja, kot je **Azure AI Search kot zadnjo plast za shranjevanje in priklic spominov**, še posebej za strukturirani RAG.

To vam omogoča, da vaše odgovore agenta temelje na lastnih podatkih, s čimer zagotavljate bolj relevantne in natančne odgovore. Azure AI Search se lahko uporablja za shranjevanje uporabniško specifičnih spominov potovanj, katalogov izdelkov ali katerega koli drugega domenskega znanja.

Azure AI Search podpira zmogljivosti, kot je **Strukturirani RAG**, ki se odlično obnese pri izvleku in priklicu gostih, strukturiranih informacij iz velikih zbirk podatkov, kot so zgodovine pogovorov, e-pošte ali celo slike. To omogoča "nadčloveško natančnost in priklic" v primerjavi s klasičnimi metodami razbijanja besedila na dele in vdelave.

## Kako narediti AI agente samopopolnjujoče

Pogosta metoda za samopopolnjujoče se agente vključuje uvedbo **"agenta za znanje"**. Ta ločeni agent opazuje glavni pogovor med uporabnikom in primarnim agentom. Njegova vloga je:

1. **Prepoznati dragocene informacije**: Ugotoviti, ali je del pogovora vreden shranjevanja kot splošno znanje ali specifična uporabniška preferenca.

2. **Izluščiti in povzeti**: Destilirati bistveno učenje ali preference iz pogovora.

3. **Shranjeno v bazo znanja**: Trajno shraniti te izluščene informacije, pogosto v vektorsko bazo, da jih je mogoče kasneje priklicati.

4. **Ojačiti prihodnje poizvedbe**: Ko uporabnik začne novo poizvedbo, agent za znanje prikliče relevantne shranjene informacije in jih doda uporabnikovemu pozivu, s čimer zagotovi ključen kontekst primarnemu agentu (podobno kot RAG).

### Optimizacije za pomnilnik

• **Upravljanje latence**: Da se izogne upočasnitvi uporabniških interakcij, se lahko sprva uporabi cenejši in hitrejši model za hitro preverjanje, ali je informacija vredna shranjevanja ali priklica, bolj zapleten postopek izvlečkov/priklica pa se sproži le po potrebi.

• **Vzdrževanje baze znanja**: Za rastočo bazo znanja lahko manj pogosto uporabljene informacije premaknete v "hladno skladišče", da upravljate stroške.

## Imate še vprašanja o pomnilniku agentov?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da spoznate druge učence, se udeležite uradnih ur in dobite odgovore na vaša vprašanja o AI agentih.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->