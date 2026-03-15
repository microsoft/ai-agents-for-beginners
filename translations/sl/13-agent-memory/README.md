# Pomnilnik za AI agente 
[![Pomnilnik agenta](../../../translated_images/sl/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Ko govorimo o edinstvenih prednostih ustvarjanja AI agentov, se predvsem izpostavljata dve stvari: možnost klicanja orodij za izvajanje nalog in sposobnost izboljševanja skozi čas. Pomnilnik je temelj ustvarjanja samoizboljšujočega se agenta, ki lahko ustvari boljše izkušnje za naše uporabnike.

V tej lekciji bomo pogledali, kaj je pomnilnik za AI agente in kako ga lahko upravljamo ter uporabljamo v prid našim aplikacijam.

## Uvod

Ta lekcija bo zajemala:

• **Razumevanje pomnilnika AI agentov**: Kaj je pomnilnik in zakaj je pomemben za agente.

• **Implementacija in shranjevanje pomnilnika**: Praktične metode za dodajanje sposobnosti pomnilnika vašim AI agentom, s poudarkom na kratkoročnem in dolgoročnem pomnilniku.

• **Kako narediti AI agente samoizboljšujoče**: Kako pomnilnik omogoča agentom, da se učijo iz preteklih interakcij in se skozi čas izboljšujejo.

## Razpoložljive implementacije

Ta lekcija vključuje dva obsežna vajinska zvezka:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementira pomnilnik z Mem0 in Azure AI Search v Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementira strukturiran pomnilnik z uporabo Cognee, samodejno gradi znanstveni graf podprt z vgrajenimi predstavitvami (embeddings), vizualizira graf in omogoča inteligentno pridobivanje

## Cilji učenja

Po zaključku te lekcije boste znali:

• **Razločiti med različnimi vrstami pomnilnika AI agentov**, vključno z delovnim, kratkoročnim in dolgoročnim pomnilnikom, pa tudi specializiranimi oblikami, kot sta persona in epizodični pomnilnik.

• **Implementirati in upravljati kratkoročni in dolgoročni pomnilnik za AI agente** z uporabo Microsoft Agent Framework, izkoriščati orodja, kot so Mem0, Cognee, Whiteboard memory, in integrirati z Azure AI Search.

• **Razumeti načela samopopravljajočih se AI agentov** in kako robustni sistemi upravljanja pomnilnika prispevajo k stalnemu učenju in prilagajanju.

## Razumevanje pomnilnika AI agentov

V svoji jedri, **pomnilnik za AI agente se nanaša na mehanizme, ki jim omogočajo, da ohranijo in prikličejo informacije**. Te informacije so lahko specifični podatki o pogovoru, uporabniške preference, pretekla dejanja ali celo naučeni vzorci.

Brez pomnilnika so AI aplikacije pogosto brezstanje (stateless), kar pomeni, da se vsaka interakcija začne znova. To vodi v ponavljajočo se in frustrirajočo uporabniško izkušnjo, kjer agent "pozabi" prejšnji kontekst ali preference.

### Zakaj je pomnilnik pomemben?

inteligenca agenta je močno povezana z njegovo sposobnostjo priklica in uporabe preteklih informacij. Pomnilnik agentom omogoča, da so:

• **Reflektivni**: Učijo se iz preteklih dejanj in izidov.

• **Interaktivni**: Ohranjajo kontekst skozi tekoč pogovor.

• **Proaktivni in reaktivni**: Predvidevajo potrebe ali ustrezno odgovarjajo na podlagi zgodovinskih podatkov.

• **Avtonomni**: Delujejo bolj samostojno z oslanjanjem na shranjeno znanje.

Cilj implementacije pomnilnika je narediti agente bolj **zanesljive in sposobne**.

### Vrste pomnilnika

#### Delovni pomnilnik

Mislite na to kot kos beležke, ki jo agent uporablja med eno, tekočo nalogo ali miselnim procesom. Vsebuje takojšnje informacije, potrebne za izračun naslednjega koraka.

Za AI agente delovni pomnilnik pogosto zajema najbolj relevantne informacije iz pogovora, tudi če je celotna zgodovina chata dolga ali skrajšana. Osredotoča se na izluščevanje ključnih elementov, kot so zahteve, predlogi, odločitve in dejanja.

**Primer delovnega pomnilnika**

Pri agentu za rezervacijo potovanj bi delovni pomnilnik lahko zajel uporabnikovo trenutno zahtevo, na primer "Želim rezervirati potovanje v Pariz". Ta specifična zahteva se hrani v takojšnjem kontekstu agenta, da vodi trenutno interakcijo.

#### Kratkoročni pomnilnik

Ta vrsta pomnilnika obdrži informacije za čas trajanja enega pogovora ali seje. To je kontekst trenutnega chata, ki agentu omogoča, da se sklicuje na prejšnje kroge v dialogu.

**Primer kratkoročnega pomnilnika**

Če uporabnik vpraša: "Koliko bi stal let v Pariz?" in nato nadaljuje z "Kaj pa nastanitev tam?", kratkoročni pomnilnik zagotovi, da agent ve, da "tam" v istem pogovoru pomeni "Pariz".

#### Dolgoročni pomnilnik

To so informacije, ki vztrajajo skozi več pogovorov ali sej. Omogoča agentom, da si zapomnijo uporabniške preference, zgodovinske interakcije ali splošno znanje skozi daljše časovno obdobje. To je pomembno za personalizacijo.

**Primer dolgoročnega pomnilnika**

Dolgoročni pomnilnik bi lahko shranil, da "Ben uživa v smučanju in zunanjih aktivnostih, ima rad kavo z razgledom na gore in želi izogibati se zahtevnim smučarskim progam zaradi pretekle poškodbe". Te informacije, pridobljene iz prejšnjih interakcij, vplivajo na priporočila v prihodnjih sejah načrtovanja potovanj in jih močno personalizirajo.

#### Persona pomnilnik

Ta specializirana vrsta pomnilnika pomaga agentu razviti konsistentno "osebnost" ali "persono". Agentu omogoča, da si zapomni podrobnosti o sebi ali svoji predvideni vlogi, zaradi česar so interakcije bolj tekoče in osredotočene.

**Primer persona pomnilnika**
Če je agent za potovanja zasnovan kot "strokovnjak za smučanje", bi persona pomnilnik lahko okrepil to vlogo in vplival na njegove odgovore, da se ujemajo s tonom in znanjem strokovnjaka.

#### Delovni/epizodični pomnilnik

Ta pomnilnik hrani zaporedje korakov, ki jih agent izvede med kompleksno nalogo, vključno s uspehi in napakami. To je kot zapisovanje specifičnih "epizod" ali preteklih izkušenj, da se iz njih uči.

**Primer epizodičnega pomnilnika**

Če je agent poskušal rezervirati določen let, a je uspelo zaradi nedosegljivosti, bi epizodični pomnilnik lahko zabeležil ta neuspeh, kar bi agentu omogočilo poskus alternativnih letov ali bolj informirano obvestilo uporabniku o težavi pri naslednjem poskusu.

#### Entitetni pomnilnik

To vključuje izluščevanje in zapomnitev specifičnih entitet (kot so ljudje, kraji ali stvari) in dogodkov iz pogovorov. Omogoča agentu gradnjo strukturiranega razumevanja ključnih elementov razprave.

**Primer entitetnega pomnilnika**

Iz pogovora o preteklem potovanju bi agent lahko izluščil "Pariz", "Eifflov stolp" in "večerja v restavraciji Le Chat Noir" kot entitete. V prihodnji interakciji bi agent lahko priklical "Le Chat Noir" in ponudil, da tam znova rezervira mizo.

#### Strukturiran RAG (Retrieval Augmented Generation)

Medtem ko je RAG širša tehnika, je "Strukturiran RAG" izpostavljen kot močna tehnologija pomnilnika. Izlušči goste, strukturirane informacije iz različnih virov (pogovori, e-pošta, slike) in jih uporablja za izboljšanje natančnosti, priklica in hitrosti odgovorov. V nasprotju s klasičnim RAG, ki se zanaša zgolj na semantično podobnost, Strukturiran RAG deluje z inherentno strukturo informacij.

**Primer Strukturiranega RAG**

Namesto le ujemanja ključnih besed, bi Strukturiran RAG lahko iz e-pošte razčlenil podatke leta (destinacija, datum, ura, letalska družba) in jih shranil na strukturiran način. To omogoča natančna poizvedovanja, kot je "Kateri let sem rezerviral v Pariz v torek?"

## Implementacija in shranjevanje pomnilnika

Implementacija pomnilnika za AI agente vključuje sistematičen proces **upravljanja pomnilnika**, ki vključuje generiranje, shranjevanje, pridobivanje, integracijo, posodabljanje in celo "pozabljanje" (ali brisanje) informacij. Pridobivanje je še posebej ključno.

### Specializirana orodja za pomnilnik

#### Mem0

En način za shranjevanje in upravljanje pomnilnika agenta je uporaba specializiranih orodij, kot je Mem0. Mem0 deluje kot trajna plast pomnilnika, ki agentom omogoča priklic relevantnih interakcij, shranjevanje uporabniških preferenc in dejanskega konteksta ter učenje iz uspehov in neuspehov skozi čas. Ideja je, da se brezstanjskim agentom omogoči, da postanejo s stanjem.

Deluje skozi **dvofazni pomnilniški cevovod: ekstrakcija in posodobitev**. Najprej so sporočila, dodana v nit agenta, poslana storitvi Mem0, ki uporablja velik jezikovni model (LLM) za povzetek zgodovine pogovora in izluščitev novih spominov. Nato faza posodobitve, vodena z LLM, odloči, ali dodati, spremeniti ali izbrisati te spomine in jih shrani v hibridno podatkovno skladišče, ki lahko vključuje vektorsko, grafično in ključ-vrednost bazo. Ta sistem podpira tudi različne vrste pomnilnika in lahko vključi grafični pomnilnik za upravljanje odnosov med entitetami.

#### Cognee

Druga zmogljiva pristop je uporaba **Cognee**, odprtokodnega semantičnega pomnilnika za AI agente, ki pretvori strukturirane in nestrukturirane podatke v poizvedljiv znanstveni graf, podprt z embeddings. Cognee nudi **dvo-skladiščno arhitekturo**, ki združuje iskanje po vektorski podobnosti z grafičnimi povezavami, kar agentom omogoča razumevanje ne le kaj je podobno, ampak kako so pojmi med seboj povezani.

Izstopa pri **hibridnem pridobivanju**, ki združuje vektorsko podobnost, grafično strukturo in LLM-razmišljanje - od preprostega iskanja kosov do vprašanj, ki upoštevajo graf. Sistem vzdržuje **živi pomnilnik**, ki se razvija in raste, pri čemer ostaja poizvedljivo kot en povezan graf, podpira tako kratkoročni kontekst seje kot dolgoročni trajni pomnilnik.

Vadbena beležnica Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) prikazuje gradnjo te združene plasti pomnilnika, s praktičnimi primeri vnosa raznolikih virov podatkov, vizualizacijo znanstvenega grafa in poizvedovanje z različnimi iskalnimi strategijami, prilagojenimi specifičnim potrebam agenta.

### Shranjevanje pomnilnika z RAG

Poleg specializiranih orodij za pomnilnik, kot je mem0 , lahko izkoristite robustne iskalne storitve, kot je **Azure AI Search**, kot back-end za shranjevanje in pridobivanje spominov, še posebej za strukturiran RAG.

To omogoča, da svoje agentove odgovore utemeljite z lastnimi podatki, kar zagotavlja bolj relevantne in natančne odgovore. Azure AI Search lahko uporablja za shranjevanje uporabniško specifičnih spominov potovanj, katalogov izdelkov ali katerega koli drugega domeno-specifičnega znanja.

Azure AI Search podpira zmogljivosti, kot je **Strukturiran RAG**, ki je odlična pri izluščevanju in pridobivanju gostih, strukturiranih informacij iz velikih podatkovnih zbirk, kot so zgodovine pogovorov, e-pošta ali celo slike. To ponuja "nadčloveško natančnost in priklic" v primerjavi s tradicionalnimi pristopi razrezovanja besedila in embeddings.

## Kako narediti AI agente samoizboljšujoče

Pogost vzorec za samoizboljšujoče agente vključuje uvedbo **"agenta za znanje"**. Ta ločen agent opazuje glavni pogovor med uporabnikom in primarnim agentom. Njegova vloga je:

1. **Prepoznati dragoceno informacijo**: Ugotoviti, ali je del pogovora vreden shranitve kot splošno znanje ali specifična uporabniška preference.

2. **Izluščiti in povzeti**: Destilirati bistveno učno vsebino ali preference iz pogovora.

3. **Shranjevanje v bazo znanja**: Utrditi to izluščeno informacijo, pogosto v vektorsko bazo podatkov, da jo je mogoče kasneje pridobiti.

4. **Ojačati prihodnje poizvedbe**: Ko uporabnik začne novo poizvedbo, agent za znanje pridobi relevantne shranjene informacije in jih pripne k uporabnikovemu pozivu, s čimer zagotovi ključen kontekst primarnemu agentu (podobno kot RAG).

### Optimizacije za pomnilnik

• **Upravljanje latence**: Da se prepreči upočasnitev uporabniških interakcij, je lahko sprva uporabljen cenejši, hitrejši model za hitro preverjanje, ali je informacija vredna shranjevanja ali pridobivanja, in le po potrebi se sproži bolj kompleksen postopek ekstrakcije/pridobivanja.

• **Vzdrževanje baze znanja**: Za rastočo bazo znanja se lahko manj pogosto uporabljene informacije premaknejo v "hladno skladišče", da se obvladujejo stroški.

## Imate še vprašanja o pomnilniku agentov?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) in se povežite z drugimi učenci, udeležite ur za vprašanja ter dobite odgovore na vaša vprašanja o AI agentih.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Izjava o omejitvi odgovornosti:
Ta dokument je bil preveden z uporabo storitve prevajanja z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v izvirnem jeziku naj se šteje za avtoritativni vir. Za kritične informacije priporočamo strokovni prevod, opravljen s strani človeka. Ne odgovarjamo za morebitna nerazumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->