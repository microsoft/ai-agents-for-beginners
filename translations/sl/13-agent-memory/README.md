# Spomin za AI agente  
[![Agent Memory](../../../translated_images/sl/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Pri razpravi o edinstvenih koristih ustvarjanja AI agentov se največkrat omenjata dve stvari: možnost klica orodij za dokončanje nalog in zmožnost izboljševanja skozi čas. Spomin je temelj ustvarjanja samopoboljšujočih se agentov, ki lahko ustvarijo boljše izkušnje za naše uporabnike.

V tej lekciji si bomo ogledali, kaj je spomin za AI agente in kako ga lahko upravljamo ter uporabljamo v korist naših aplikacij.

## Uvod

Ta lekcija zajema:

• **Razumevanje spomina AI agentov**: Kaj je spomin in zakaj je bistven za agente.

• **Implementacija in shranjevanje spomina**: Praktične metode za dodajanje sposobnosti spomina vašim AI agentom, s poudarkom na kratkoročnem in dolgoročnem spominu.

• **Samopoboljševanje AI agentov**: Kako spomin omogoča agentom učenje iz preteklih interakcij in izboljševanje skozi čas.

## Razpoložljive implementacije

Ta lekcija vključuje dva celovita vodnika v zvezkih:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementacija spomina z uporabo Mem0 in Azure AI Search z Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementacija strukturiranega spomina s Cognee, ki samodejno gradi znanstveni graf, podprt z ugnezditvami, vizualizira graf in omogoča inteligentno pridobivanje

## Cilji učenja

Po končani tej lekciji boste znali:

• **Razločevati med različnimi vrstami spomina AI agentov**, vključno z delovnim, kratkoročnim in dolgoročnim spominom ter specializiranimi oblikami, kot sta persona in epizodični spomin.

• **Implementirati in upravljati kratkoročni in dolgoročni spomin za AI agente** z uporabo Microsoft Agent Framework, kjer izkoriščate orodja, kot so Mem0, Cognee, Whiteboard spomin in integracijo z Azure AI Search.

• **Razumeti načela za samopoboljšanje AI agentov** in kako robustni sistemi upravljanja spomina pripomorejo k neprekinjenemu učenju in prilagajanju.

## Razumevanje spomina AI agentov

V bistvu se **spomin za AI agente nanaša na mehanizme, ki jim omogočajo hranjenje in priklic informacij**. Te informacije so lahko specifični podatki o pogovoru, uporabniške preference, pretekla dejanja ali celo naučeni vzorci.

Brez spomina so AI aplikacije pogosto brezstanje, kar pomeni, da se vsaka interakcija začne na novo. To vodi v ponavljajočo in frustrirajočo uporabniško izkušnjo, kjer agent "pozabi" prejšnji kontekst ali preference.

### Zakaj je spomin pomemben?

Inteligenca agenta je globoko povezana z njegovo sposobnostjo priklica in uporabe preteklih informacij. Spomin omogoča agentom, da so:

• **Reflektivni**: Učenje iz preteklih dejanj in rezultatov.

• **Interaktivni**: Ohranitev konteksta med tekočim pogovorom.

• **Proaktivni in reaktivni**: Predvidevanje potreb ali primerno odzivanje na podlagi zgodovinskih podatkov.

• **Avtonomni**: Delovanje bolj neodvisno s pomočjo shranjenega znanja.

Cilj implementacije spomina je narediti agente bolj **zanesljive in sposobne**.

### Vrste spomina

#### Delovni spomin

To si predstavljajte kot list papirja za zapiske, ki ga agent uporablja med posamezno nalogo ali miselnim procesom. Vsebuje takojšnjo informacijo, potrebno za izračun naslednjega koraka.

Pri AI agentih delovni spomin pogosto zajame najbolj relevantne informacije iz pogovora, tudi če je celotna zgodovina dolga ali prirejena. Osredotoča se na izločanje ključnih elementov, kot so zahteve, predlogi, odločitve in dejanja.

**Primer delovnega spomina**

Pri agentu za rezervacijo potovanja lahko delovni spomin zajame trenutno zahtevo uporabnika, na primer "Želim rezervirati potovanje v Pariz". Ta specifična zahteva se hrani v neposrednem kontekstu agenta za usmerjanje trenutne interakcije.

#### Kratkoročni spomin

Ta vrsta spomina hrani informacije skozi trajanje enega pogovora ali seje. Je kontekst trenutnega klepeta, ki agentu omogoča sklicevanje na prejšnje izmenjave v dialogu.

V [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK vzorcih to ustreza `AgentSession`, ustvarjenemu z `agent.create_session()`. Seja je vgrajeni kratkoročni spomin okvira: hranilnik konteksta pogovora je na voljo, dokler se seja uporablja, vendar se ta kontekst ne ohrani, ko seja konča ali se aplikacija ponovno zažene. Za dejstva in preference, ki morajo preživeti med sejami, uporabite dolgoročni spomin, običajno prek baze podatkov, vektorskega indeksa ali drugega trajnega shranjevanja.

**Primer kratkoročnega spomina**

Če uporabnik vpraša: "Koliko bi stala letalska karta do Pariza?" in nato nadaljuje z "Kaj pa nastanitev tam?", kratkoročni spomin zagotovi, da agent razume, da se "tam" nanaša na "Pariz" v istem pogovoru.

#### Dolgoročni spomin

To je informacija, ki vztraja skozi več pogovorov ali sej. Omogoča agentom, da si zapomnijo uporabniške preference, pretekle interakcije ali splošno znanje skozi daljše časovno obdobje. To je pomembno za personalizacijo.

**Primer dolgoročnega spomina**

Dolgoročni spomin lahko shrani, da "Ben uživa v smučanju in dejavnostih na prostem, rad pije kavo z razgledom na gore in želi preprečiti zahtevne smučarske proge zaradi pretekle poškodbe". Te informacije, pridobljene iz prejšnjih interakcij, vplivajo na priporočila v prihodnjih načrtih potovanj in jih naredijo zelo personalizirane.

#### Persona spomin

Ta specializirana vrsta spomina agentu pomaga razviti dosledno "osebnost" ali "persono". Omogoča, da agent zapomni podrobnosti o samem sebi ali svoji vlogi, kar naredi interakcije bolj tekoče in osredotočene.

**Primer persona spomina**

Če je agent za potovanja zasnovan kot "strokovnjak za načrtovanje smučanja," persona spomin lahko okrepi to vlogo, kar vpliva na njegove odzive, da so skladni s tonom in znanjem strokovnjaka.

#### Spomin delovnega toka / epizodični spomin

Ta spomin hrani zaporedje korakov, ki jih agent izvede pri kompleksni nalogi, vključno z uspehi in neuspehi. Podobno kot zapomniti si specifične "epizode" ali pretekle izkušnje za učenje iz njih.

**Primer epizodičnega spomina**

Če je agent poskušal rezervirati določen let, ki pa je zaradi nedosegljivosti ni uspel izvesti, lahko epizodični spomin zabeleži ta neuspeh, kar agentu omogoči, da preizkusi alternativne lete ali uporabnika obvesti o težavi na bolj informiran način ob naslednjem poskusu.

#### Spomin entitet

Vključuje izluščanje in hranjenje specifičnih entitet (kot so ljudje, kraji ali stvari) in dogodkov iz pogovorov. Agentu omogoča gradnjo strukturiranega razumevanja ključnih elementov, o katerih se razpravlja.

**Primer spomina entitet**

Iz pogovora o preteklem potovanju bi agent lahko izluščil "Pariz", "Eifflov stolp" in "večerjo v restavraciji Le Chat Noir" kot entitete. Pri prihodnji interakciji bi agent lahko priklical "Le Chat Noir" in ponudil, da tam naredi novo rezervacijo.

#### Strukturiran RAG (Retrieval Augmented Generation)

Čeprav je RAG širša tehnika, je "Strukturiran RAG" izpostavljen kot zmogljiva tehnologija spomina. Izlušči gosto, strukturirano informacijo iz različnih virov (pogovori, e-pošta, slike) in jo uporablja za povečanje natančnosti, priklica in hitrosti odgovorov. V nasprotju s klasičnim RAG, ki temelji samo na semantični podobnosti, Strukturiran RAG deluje z inherentno strukturo informacij.

**Primer strukturiranega RAG**

Namesto da samo ujame ključne besede, bi Strukturiran RAG lahko razčlenil podrobnosti lete (destinacija, datum, čas, letalska družba) iz e-pošte in jih shranil strukturirano. To omogoča natančna vprašanja kot na primer "Kateri let sem rezerviral za Pariz v torek?"

## Implementacija in shranjevanje spomina

Implementacija spomina za AI agente vključuje sistematičen proces **upravljanja spomina**, ki zajema ustvarjanje, shranjevanje, pridobivanje, integracijo, posodabljanje in celo "pozabljanje" (ali brisanje) informacij. Pridobivanje je še posebej ključni vidik.

### Specializirana orodja za spomin

#### Mem0

Eden od načinov za shranjevanje in upravljanje spomina agenta je uporaba specializiranih orodij, kot je Mem0. Mem0 deluje kot trajna plast spomina, ki agentom omogoča priklic relevantnih interakcij, shranjevanje uporabniških preferenc in dejanskega konteksta ter učenje iz uspehov in neuspehov skozi čas. Ideja je, da se brezstanje agenti spremenijo v stanje ohranjajoče.

Deluje prek **dvostopenjskega memorijskega tokokroga: ekstrakcija in posodobitev**. Najprej se sporočila, dodana nitim agenta, pošljejo Mem0 storitvi, ki uporablja velik jezikovni model (LLM) za povzetek zgodovine pogovora in izluščitev novih spominov. Nato LLM-ji v posodobitveni fazi določijo, ali dodati, spremeniti ali izbrisati te spomine, ki se shranijo v hibridno podatkovno skladišče, ki lahko vključuje vektorsko, grafično in ključ-vrednost bazo. Sistem podpira tudi različne vrste spomina in lahko vključuje grafični spomin za upravljanje odnosov med entitetami.

#### Cognee

Drug močan pristop je uporaba **Cognee**, odprtokodnega semantičnega spomina za AI agente, ki pretvori strukturirane in nestrukturirane podatke v poizvedljive grafe znanja, podprte z ugnezditvami. Cognee nudi **dvohranilno arhitekturo**, ki združuje iskanje po vektorski podobnosti z grafičnimi povezavami, kar agentom omogoča razumevanje ne samo podobnosti informacij, temveč tudi medsebojnih odnosov med koncepti.

Odlikuje se pri **hibridnem pridobivanju**, ki združuje vektorsko podobnost, grafično strukturo in LLM sklepanje – od iskanja po surovih delih do grafom ozaveščenega odgovarjanja na vprašanja. Sistem ohranja **živi spomin**, ki se razvija in raste, medtem ko ostaja poizvedljiv kot ena povezana grafična struktura ter podpira tako kratkoročni kontekst seje kot dolgoročni trajni spomin.

Vodnik po Cognee zvezku ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) prikazuje gradnjo te enotne memorijske plasti z praktičnimi primeri zajema različnih virov podatkov, vizualizacijo grafa znanja in poizvedovanje z različnimi iskalnimi strategijami, prilagojenimi specifičnim potrebam agenta.

### Shranjevanje spomina z RAG

Poleg specializiranih orodij za spomin, kot je Mem0, lahko izkoristite robustne iskalne storitve, kot je **Azure AI Search kot ozadje za shranjevanje in pridobivanje spominov**, še posebej za strukturiran RAG.

To vam omogoča, da svoje agentove odgovore podkrepite z vašimi lastnimi podatki, kar zagotavlja bolj relevantne in natančne odgovore. Azure AI Search lahko uporablja za shranjevanje uporabniških potovalnih spominov, kataloga izdelkov ali kakršnega koli drugega specifičnega znanja s področja.

Azure AI Search podpira zmogljivosti, kot je **Strukturiran RAG**, ki se odlikuje pri izluščitvi in pridobivanju gostih, strukturiranih informacij iz velikih podatkovnih zbirk, kot so zgodovine pogovorov, e-pošte ali celo slike. To zagotavlja "človeško nadpovprečno natančnost in priklic" v primerjavi s tradicionalnimi pristopi razrezovanja besedila in ugnezditve.

## Samopoboljšanje AI agentov

Pogost vzorec za samopoboljšujoče agente vključuje uvedbo **"agenta znanja"**. Ta ločeni agent opazuje glavni pogovor med uporabnikom in primarnim agentom. Njegova vloga je:

1. **Prepoznati dragocene informacije**: Ugotoviti, ali je del pogovora vreden shranitve kot splošno znanje ali specifična uporabniška preference.

2. **Izluščiti in povzeti**: Izločiti bistveno učenje ali preference iz pogovora.

3. **Shranjeno v bazo znanja**: Ta izluščena informacija se pogosto shrani v vektorsko bazo podatkov, da se lahko pozneje pridobi.

4. **Podpreti prihodnje poizvedbe**: Ko uporabnik sproži novo poizvedbo, agent znanja pridobi relevantne shranjene informacije in jih priloži uporabnikovemu pozivu, kar zagotavlja ključni kontekst primarnemu agentu (na podoben način kot RAG).

### Optimizacije za spomin

• **Upravljanje latence**: Da se ne upočasni uporabniška izmenjava, se lahko sprva uporabi cenejši, hitrejši model, ki hitro preveri, ali so informacije vredne shraniti ali pridobiti, in se kompleksnejši postopek ekstrakcije/pridobivanja sproži le, če je to potrebno.

• **Vzdrževanje baze znanja**: Za rastočo bazo znanja se manj pogosto uporabljene informacije lahko premaknejo v "hladno shrambo" za upravljanje stroškov.

## Imate več vprašanj o spominu agentov?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), da se srečate z drugimi učenci, udeležite uradnih ur in dobite odgovore na vaša vprašanja o AI agentih.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->