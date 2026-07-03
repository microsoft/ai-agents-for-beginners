# Pomnilnik za AI agente 
[![Pomnilnik agenta](../../../translated_images/sl/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Ko govorimo o edinstvenih prednostih ustvarjanja AI agentov, se večinoma omenja dve stvari: sposobnost klicanja orodij za dokončanje nalog in sposobnost izboljševanja skozi čas. Pomnilnik je temelj za ustvarjanje agenta, ki se sam izboljšuje in lahko ustvari boljše izkušnje za naše uporabnike.

V tej lekciji bomo pogledali, kaj je pomnilnik za AI agente in kako ga lahko upravljamo ter uporabljamo v korist naših aplikacij.

## Uvod

Ta lekcija bo zajemala:

• **Razumevanje pomnilnika AI agenta**: Kaj je pomnilnik in zakaj je za agente bistven.

• **Implementacija in shranjevanje pomnilnika**: Praktične metode za dodajanje sposobnosti pomnilnika vašim AI agentom, s poudarkom na kratkoročnem in dolgoročnem pomnilniku.

• **Samopopravljači AI agenti**: Kako pomnilnik agentom omogoča učenje iz preteklih interakcij in izboljševanje skozi čas.

## Razpoložljive implementacije

Ta lekcija vključuje dva obsežna učna zvezka:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementira pomnilnik z uporabo Mem0 in Azure AI Search z Microsoft Agent Frameworkom

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementira strukturiran pomnilnik z uporabo Cognee, ki samodejno gradi znanstveni graf, podprt z vdelavami, vizualizira graf in omogoča inteligentno iskanje

## Cilji učenja

Po opravljenem temeljitem pregledu boste znali:

• **Razlikovati med različnimi tipi pomnilnika AI agentov**, vključno z delovnim, kratkoročnim in dolgoročnim pomnilnikom, kot tudi specializiranimi oblikami, kot sta osebni in epizodni pomnilnik.

• **Implementirati in upravljati kratkoročni in dolgoročni pomnilnik za AI agente** z uporabo Microsoft Agent Frameworka, ob uporabi orodij, kot so Mem0, Cognee, Whiteboard pomnilnik ter integracijo z Azure AI Search.

• **Razumeti načela samopopravljačev AI agentov** in kako robustni sistemi upravljanja pomnilnika prispevajo k neprekinjenemu učenju in prilagajanju.

## Razumevanje pomnilnika AI agenta

V jedru **pomnilnik AI agenta pomeni mehanizme, ki mu omogočajo, da si zapomni in prikliče informacije**. Te informacije so lahko specifični podatki o pogovoru, uporabniške preference, pretekla dejanja ali celo naučeni vzorci.

Brez pomnilnika so AI aplikacije pogosto brez stanja, kar pomeni, da se vsak stik začne znova. To vodi do ponavljajoče in frustrirajoče uporabniške izkušnje, kjer agent "pozabi" prejšnji kontekst ali preference.

### Zakaj je pomnilnik pomemben?

Inteligenca agenta je globoko povezana z njegovo sposobnostjo priklica in uporabe preteklih informacij. Pomnilnik agentom omogoča:

• **Reflektivnost**: Učenje iz preteklih dejanj in rezultatov.

• **Interaktivnost**: Ohranitev konteksta med tekočim pogovorom.

• **Proaktivnost in reaktivnost**: Predvidevanje potreb ali ustrezno odzivanje na podlagi preteklih podatkov.

• **Avtonomnost**: Bolj neodvisno delovanje z uporabo shranjenega znanja.

Cilj implementacije pomnilnika je, da so agenti bolj **zanesljivi in sposobni**.

### Vrste pomnilnika

#### Delovni pomnilnik

To lahko razumemo kot kos zvezka, ki ga agent uporablja med eno tekočo nalogo ali miselnim procesom. V njem hrani neposredne informacije, potrebne za izračun naslednjega koraka.

Pri AI agentih delovni pomnilnik pogosto zajame najbolj relevantne informacije iz pogovora, tudi če je celotna zgodovina dolga ali prirejena. Osredotoča se na ključne elemente, kot so zahteve, predlogi, odločitve in dejanja.

**Primer delovnega pomnilnika**

Pri agentu za rezervacijo potovanj bi delovni pomnilnik lahko zajel trenutno zahtevo uporabnika, na primer "Rad bi rezerviral potovanje v Pariz". Ta specifična zahteva je shranjena v neposrednem kontekstu agenta, da usmerja trenutno interakcijo.

#### Kratkoročni pomnilnik

Ta tip pomnilnika ohranja informacije za čas trajanja enega samega pogovora ali seje. To je kontekst trenutnega klepeta, ki agentu omogoča, da se sklicuje na prejšnje zavoje v dialogu.

V primerih Python SDK-ja [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) je to predstavljeno z `AgentSession`, ustvarjenim z `agent.create_session()`. Seja je vgrajen kratkoročni pomnilnik ogrodja: ohranja kontekst pogovora na voljo, dokler se ista seja ponovno uporablja, vendar se ta kontekst ne shrani, ko seja konča ali ko aplikacija znova zažene. Za dejstva in preference, ki morajo preživeti seje, uporabite dolgoročni pomnilnik, običajno preko baze podatkov, vektorskega indeksa ali drugega trajnega shranjevanja.

**Primer kratkoročnega pomnilnika**

Če uporabnik vpraša: "Koliko stane let v Pariz?" in nato doda: "Kaj pa nastanitev tam?", kratkoročni pomnilnik zagotovi, da agent ve, da "tam" pomeni "Pariz" v istem pogovoru.

#### Dolgoročni pomnilnik

To so informacije, ki vztrajajo skozi več pogovorov ali sej. Omogoča agentom, da si zapomnijo uporabniške preference, pretekle interakcije ali splošno znanje za daljše obdobje. To je pomembno za personalizacijo.

**Primer dolgoročnega pomnilnika**

Dolgoročni pomnilnik lahko shrani, da "Ben uživa v smučanju in zunanjih aktivnostih, ima rad kavo z razgledom na gore in se želi izogibati zahtevnim smučarskim progama zaradi pretekle poškodbe". Te informacije, naučene iz prejšnjih interakcij, vplivajo na priporočila v prihodnjih načrtih potovanj in jih naredijo zelo personalizirana.

#### Osebni pomnilnik

Ta specializirana vrsta pomnilnika pomaga agentu razviti dosledno "osebnost" ali "persona". Omogoča agentu, da si zapomni podrobnosti o sebi ali svoji vlogi, kar naredi interakcije bolj tekoče in osredotočene.

**Primer osebnega pomnilnika**  
Če je agent za potovanja zasnovan kot "strokovnjak za načrtovanje smučanja", lahko osebni pomnilnik okrepi to vlogo, kar vpliva na njegove odzive v skladu s tonom in znanjem strokovnjaka.

#### Delovni/epizodni pomnilnik

Ta pomnilnik shranjuje zaporedje korakov, ki jih agent opravi med kompleksno nalogo, vključno z uspehi in neuspehi. Je kot spominjanje določenih "epizod" ali preteklih izkušenj za učenje iz njih.

**Primer epizodnega pomnilnika**

Če je agent poskušal rezervirati določen let, a je to spodletelo zaradi nedosegljivosti, lahko epizodni pomnilnik zabeleži ta neuspeh, kar agenta omogoča, da poskusi alternativne lete ali bolj informirano obvesti uporabnika o težavi pri naslednjem poskusu.

#### Entitetni pomnilnik

Vključuje izvleček in pomnjenje specifičnih entitet (kot so osebe, kraji ali stvari) in dogodkov iz pogovorov. Omogoča agentu, da zgradi strukturirano razumevanje ključnih elementov, o katerih je bilo govorjeno.

**Primer entitetnega pomnilnika**

Iz pogovora o preteklem potovanju bi agent lahko izvlekel "Pariz", "Eifflov stolp" in "večerjo v restavraciji Le Chat Noir" kot entitete. Pri prihodnji interakciji bi agent lahko priklical "Le Chat Noir" in ponudil novo rezervacijo tam.

#### Strukturirani RAG (Retrieval Augmented Generation)

Medtem ko je RAG širša tehnika, je "Strukturirani RAG" poudarjen kot zmogljiva tehnologija pomnilnika. Izvleče goste, strukturirane informacije iz različnih virov (pogovori, e-pošta, slike) in jih uporablja za izboljšanje natančnosti, priklica in hitrosti odgovorov. Za razliko od klasičnega RAG, ki se opira izključno na semantično podobnost, Strukturirani RAG deluje z inerentno strukturo informacij.

**Primer strukturiranega RAG**

Namesto le ujemanja ključnih besed bi Strukturirani RAG lahko razčlenil podatke o letu (destinacija, datum, ura, letalska družba) iz e-pošte in jih shranil na strukturiran način. To omogoča natančna vprašanja, kot je "Kateri let sem rezerviral v Pariz v torek?"

## Implementacija in shranjevanje pomnilnika

Implementacija pomnilnika za AI agente vključuje sistematičen proces **upravljanja pomnilnika**, ki zajema generiranje, shranjevanje, priklic, integracijo, posodabljanje in celo "pozabljanje" (ali brisanje) informacij. Priklic je še posebej pomemben element.

### Specializirana orodja za pomnilnik

#### Mem0

Eden od načinov za shranjevanje in upravljanje pomnilnika agenta je uporaba specializiranih orodij, kot je Mem0. Mem0 deluje kot trajna plast pomnilnika, ki agentom omogoča priklic relevantnih interakcij, shranjevanje uporabniških preferenc in dejanskega konteksta ter učenje iz uspehov in neuspehov skozi čas. Ideja je tu, da se stateless agenti spremenijo v stateful.

Deluje preko **dvofaznega cevovoda pomnilnika: izvleka in posodobitve**. Najprej se sporočila, dodana niti agenta, pošljejo na storitev Mem0, ki uporablja velik jezikovni model (LLM) za povzemanje zgodovine pogovora in izvlečenje novih spominov. Nato faza posodobitve, ki jo vodi LLM, določi, ali se te spomine doda, spremeni ali izbriše, in jih shrani v hibridno podatkovno skladišče, ki lahko vključuje vektorske, grafične in ključ-vrednost baze podatkov. Sistem podpira tudi različne tipe pomnilnika in lahko vključuje grafični pomnilnik za upravljanje odnosov med entitetami.

#### Cognee

Drugi močan pristop je uporaba **Cogneea**, odprtokodnega semantičnega pomnilnika za AI agente, ki pretvarja strukturirane in nestrukturirane podatke v poizvedljiv znanstveni graf, podprt z vdelavami. Cognee zagotavlja **dvoložni arhitekturi**, ki združuje iskanje po vektorski podobnosti z grafičnimi povezavami, kar agentom omogoča razumeti ne le, katere informacije so podobne, ampak kako so koncepti povezani med seboj.

Izstopa pri **hibridnem priklicu**, ki združuje vektorsko podobnost, strukturo grafa in LLM razmišljanje - od preprostega iskanja po koščkih do odgovorov, ki upoštevajo graf. Sistem ohranja **živ pomnilnik**, ki se razvija in raste, hkrati ostaja poizvedljiv kot en povezan graf, podpira tako kratkoročni kontekst seje kot dolgoročni trajni pomnilnik.

Učni zvezek Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) prikazuje gradnjo te združene plasti pomnilnika, s praktičnimi primeri vnosa raznolikih virov podatkov, vizualizacijo znanstvenega grafa in poizvedovanjem z različnimi strategijami iskanja, prilagojenimi specifičnim potrebam agenta.

### Shranjevanje pomnilnika z RAG

Poleg specializiranih orodij za pomnilnik, kot je Mem0, lahko izkoristite robustne iskalne storitve, kot je **Azure AI Search, kot zaledje za shranjevanje in priklic spominov**, še posebej za strukturirani RAG.

To omogoča, da temelji odgovori vašega agenta na lastnih podatkih, s čimer zagotovite relevantnejše in natančnejše odgovore. Azure AI Search se lahko uporablja za shranjevanje uporabniških potovalnih spominov, katalogov izdelkov ali druge domensko specifične vsebine.

Azure AI Search podpira zmogljivosti, kot je **Strukturirani RAG**, ki odlično izvleče in prikliče goste, strukturirane podatke iz velikih podatkovnih nizov, kot so zgodovina pogovorov, e-pošte ali celo slike. To zagotavlja "človeško natančnost in priklic" v primerjavi s tradicionalnimi metodami razbitja besedila in vdelav.

## Spodbujanje samopopravljačev AI agentov

Pogost vzorec za agente, ki se sami izboljšujejo, vključuje uvedbo **"agenta znanja"**. Ta ločeni agent opazuje glavni pogovor med uporabnikom in primarnim agentom. Njegova naloga je:

1. **Prepoznati vredne informacije**: Ugotoviti, ali je del pogovora vreden shranjevanja kot splošno znanje ali specifična uporabniška nastavitev.

2. **Izvleči in povzeti**: Destilirati bistveno učno vsebino ali preferenco iz pogovora.

3. **Shranjevanje v bazo znanja**: Shraniti to izvlečeno informacijo, pogosto v vektorsko bazo podatkov, da je ta kasneje lahko priklicana.

4. **Povečevanje prihodnjih poizvedb**: Ko uporabnik začne novo poizvedbo, agent znanja poišče relevantne shranjene informacije in jih doda uporabniškemu pozivu, s tem pa zagotovi ključen kontekst primarnemu agentu (podobno kot RAG).

### Optimizacije pomnilnika

• **Upravljanje zakasnitve**: Da se ne upočasnijo uporabniške interakcije, se najprej lahko uporabi cenejši, hitrejši model za hitro preverjanje, ali je informacija vredna shranjevanja ali priklica, in šele po potrebi sproži bolj zapleten postopek izvlečka/priklica.

• **Vzdrževanje baze znanja**: Za rastočo bazo znanja se manj pogosto uporabljene informacije lahko preselijo v "hladno shrambo" za znižanje stroškov.

## Imate še več vprašanj glede pomnilnika agentov?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da spoznate druge učence, se udeležite uradnih ur in dobite odgovore na vaša vprašanja o AI agentih.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->