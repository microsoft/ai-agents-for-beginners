<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2c9703548140bafa2d6a77406552542",
  "translation_date": "2025-10-03T15:11:08+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "sl"
}
-->
# Spomin za AI agente
[![Spomin agenta](../../../translated_images/lesson-13-thumbnail.959e3bc52d210c64a614a3bece6b170a2c472138dc0a14c7fbde07306ef95ae7.sl.png)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Ko govorimo o edinstvenih prednostih ustvarjanja AI agentov, sta dve stvari pogosto v ospredju: sposobnost uporabe orodij za dokončanje nalog in sposobnost izboljševanja skozi čas. Spomin je temelj za ustvarjanje samopopravljajočega agenta, ki lahko zagotovi boljše izkušnje za naše uporabnike.

V tej lekciji bomo raziskali, kaj spomin pomeni za AI agente, kako ga lahko upravljamo in uporabljamo za izboljšanje naših aplikacij.

## Uvod

Ta lekcija bo obravnavala:

• **Razumevanje spomina AI agenta**: Kaj je spomin in zakaj je ključen za agente.

• **Implementacija in shranjevanje spomina**: Praktične metode za dodajanje sposobnosti spomina vašim AI agentom, s poudarkom na kratkoročnem in dolgoročnem spominu.

• **Kako narediti AI agente samopopravljajoče**: Kako spomin omogoča agentom, da se učijo iz preteklih interakcij in se izboljšujejo skozi čas.

## Cilji učenja

Po zaključku te lekcije boste znali:

• **Razlikovati med različnimi vrstami spomina AI agenta**, vključno z delovnim, kratkoročnim in dolgoročnim spominom ter specializiranimi oblikami, kot sta osebnostni in epizodni spomin.

• **Implementirati in upravljati kratkoročni in dolgoročni spomin za AI agente** z uporabo okvira Semantic Kernel, orodij, kot sta Mem0 in Whiteboard memory, ter integracijo z Azure AI Search.

• **Razumeti načela samopopravljajočih AI agentov** in kako robustni sistemi za upravljanje spomina prispevajo k stalnemu učenju in prilagajanju.

## Razumevanje spomina AI agenta

V svojem bistvu **spomin za AI agente pomeni mehanizme, ki jim omogočajo ohranjanje in priklic informacij**. Te informacije lahko vključujejo specifične podrobnosti o pogovoru, uporabniške preference, pretekla dejanja ali celo naučene vzorce.

Brez spomina so AI aplikacije pogosto brez stanja, kar pomeni, da se vsaka interakcija začne od začetka. To vodi v ponavljajočo in frustrirajočo uporabniško izkušnjo, kjer agent "pozabi" prejšnji kontekst ali preference.

### Zakaj je spomin pomemben?

Inteligenca agenta je tesno povezana z njegovo sposobnostjo priklica in uporabe preteklih informacij. Spomin omogoča agentom, da so:

• **Refleksivni**: Učijo se iz preteklih dejanj in rezultatov.

• **Interaktivni**: Ohranjajo kontekst med tekočim pogovorom.

• **Proaktivni in reaktivni**: Predvidevajo potrebe ali ustrezno reagirajo na podlagi zgodovinskih podatkov.

• **Avtonomni**: Delujejo bolj neodvisno z uporabo shranjenega znanja.

Cilj implementacije spomina je narediti agente bolj **zanesljive in sposobne**.

### Vrste spomina

#### Delovni spomin

Pomislite na to kot na kos papirja, ki ga agent uporablja med eno samo, tekočo nalogo ali procesom razmišljanja. Zadrži takojšnje informacije, potrebne za izračun naslednjega koraka.

Za AI agente delovni spomin pogosto zajame najbolj relevantne informacije iz pogovora, tudi če je celotna zgodovina klepeta dolga ali skrajšana. Osredotoča se na ključne elemente, kot so zahteve, predlogi, odločitve in dejanja.

**Primer delovnega spomina**

Pri agentu za rezervacijo potovanj bi delovni spomin lahko zajel trenutno zahtevo uporabnika, na primer "Želim rezervirati potovanje v Pariz". Ta specifična zahteva je zadržana v trenutnem kontekstu agenta za vodenje interakcije.

#### Kratkoročni spomin

Ta vrsta spomina ohranja informacije za trajanje enega samega pogovora ali seje. To je kontekst trenutnega klepeta, ki agentu omogoča, da se sklicuje na prejšnje korake v dialogu.

**Primer kratkoročnega spomina**

Če uporabnik vpraša: "Koliko bi stal let v Pariz?" in nato nadaljuje z "Kaj pa nastanitev tam?", kratkoročni spomin zagotavlja, da agent ve, da "tam" pomeni "Pariz" v istem pogovoru.

#### Dolgoročni spomin

To so informacije, ki trajajo skozi več pogovorov ali sej. Omogoča agentom, da si zapomnijo uporabniške preference, zgodovinske interakcije ali splošno znanje skozi daljše obdobje. To je pomembno za personalizacijo.

**Primer dolgoročnega spomina**

Dolgoročni spomin bi lahko shranil, da "Ben uživa v smučanju in dejavnostih na prostem, ima rad kavo z razgledom na gore in se želi izogniti zahtevnim smučarskim progam zaradi pretekle poškodbe". Te informacije, pridobljene iz prejšnjih interakcij, vplivajo na priporočila v prihodnjih sejah načrtovanja potovanj, kar jih naredi zelo personalizirane.

#### Osebnostni spomin

Ta specializirana vrsta spomina pomaga agentu razviti dosledno "osebnost" ali "vlogo". Omogoča agentu, da si zapomni podrobnosti o sebi ali svoji predvideni vlogi, kar naredi interakcije bolj tekoče in osredotočene.

**Primer osebnostnega spomina**

Če je agent za potovanja zasnovan kot "strokovnjak za načrtovanje smučarskih počitnic", bi osebnostni spomin lahko okrepil to vlogo, kar bi vplivalo na njegove odgovore, da se ujemajo s tonom in znanjem strokovnjaka.

#### Epizodni spomin

Ta spomin shranjuje zaporedje korakov, ki jih agent izvede med kompleksno nalogo, vključno z uspehi in neuspehi. Je kot spomin na specifične "epizode" ali pretekle izkušnje, iz katerih se lahko uči.

**Primer epizodnega spomina**

Če je agent poskušal rezervirati določen let, vendar je to spodletelo zaradi nedostopnosti, bi epizodni spomin lahko zabeležil ta neuspeh, kar bi agentu omogočilo, da poskusi alternativne lete ali uporabnika obvesti o težavi na bolj informiran način med naslednjim poskusom.

#### Spomin na entitete

Ta spomin vključuje izvlečenje in zapomnitev specifičnih entitet (kot so ljudje, kraji ali stvari) in dogodkov iz pogovorov. Omogoča agentu, da zgradi strukturirano razumevanje ključnih elementov, o katerih se razpravlja.

**Primer spomina na entitete**

Iz pogovora o preteklem potovanju bi agent lahko izvlekel "Pariz", "Eifflov stolp" in "večerja v restavraciji Le Chat Noir" kot entitete. V prihodnji interakciji bi agent lahko priklical "Le Chat Noir" in ponudil, da tam rezervira novo večerjo.

#### Strukturirani RAG (Retrieval Augmented Generation)

Medtem ko je RAG širša tehnika, je "strukturirani RAG" izpostavljen kot močna tehnologija spomina. Izvleče gosto, strukturirano informacijo iz različnih virov (pogovori, e-pošte, slike) in jo uporablja za izboljšanje natančnosti, priklica in hitrosti odgovorov. Za razliko od klasičnega RAG, ki se zanaša zgolj na semantično podobnost, strukturirani RAG deluje z inherentno strukturo informacij.

**Primer strukturiranega RAG**

Namesto da bi zgolj ujemal ključne besede, bi strukturirani RAG lahko analiziral podrobnosti leta (destinacija, datum, čas, letalska družba) iz e-pošte in jih shranil na strukturiran način. To omogoča natančna vprašanja, kot je "Kateri let sem rezerviral za Pariz v torek?"

## Implementacija in shranjevanje spomina

Implementacija spomina za AI agente vključuje sistematičen proces **upravljanja spomina**, ki vključuje generiranje, shranjevanje, priklic, integracijo, posodabljanje in celo "pozabljanje" (ali brisanje) informacij. Priklic je še posebej ključni vidik.

### Specializirana orodja za spomin

Eden od načinov za shranjevanje in upravljanje spomina agenta je uporaba specializiranih orodij, kot je Mem0. Mem0 deluje kot trajna plast spomina, ki agentom omogoča priklic relevantnih interakcij, shranjevanje uporabniških preferenc in dejanskega konteksta ter učenje iz uspehov in neuspehov skozi čas. Ideja je, da se agenti brez stanja spremenijo v agente s stanjem.

Deluje skozi **dvofazni proces spomina: ekstrakcija in posodobitev**. Najprej se sporočila, dodana v nit agenta, pošljejo storitvi Mem0, ki uporablja Large Language Model (LLM) za povzetek zgodovine pogovora in izvleček novih spominov. Nato faza posodobitve, ki jo vodi LLM, določi, ali je treba te spomine dodati, spremeniti ali izbrisati, ter jih shrani v hibridno podatkovno shrambo, ki lahko vključuje vektorske, grafične in ključ-vrednostne baze podatkov. Ta sistem podpira tudi različne vrste spomina in lahko vključuje grafični spomin za upravljanje odnosov med entitetami.

### Shranjevanje spomina z RAG

Poleg specializiranih orodij za spomin, kot je Mem0, lahko uporabite robustne iskalne storitve, kot je **Azure AI Search kot zaledje za shranjevanje in priklic spominov**, še posebej za strukturirani RAG.

To omogoča, da utemeljite odgovore agenta z lastnimi podatki, kar zagotavlja bolj relevantne in natančne odgovore. Azure AI Search se lahko uporablja za shranjevanje uporabniških spominov o potovanjih, katalogov izdelkov ali katere koli druge domensko specifične informacije.

Azure AI Search podpira zmogljivosti, kot je **strukturirani RAG**, ki odlično izvleče in prikliče gosto, strukturirano informacijo iz velikih podatkovnih nizov, kot so zgodovine pogovorov, e-pošte ali celo slike. To zagotavlja "nadčloveško natančnost in priklic" v primerjavi s tradicionalnimi pristopi razdeljevanja besedila in vgrajevanja.

## Kako narediti AI agente samopopravljajoče

Pogost vzorec za samopopravljajoče agente vključuje uvedbo **"agenta za znanje"**. Ta ločen agent opazuje glavni pogovor med uporabnikom in primarnim agentom. Njegova vloga je:

1. **Prepoznati dragocene informacije**: Določiti, ali je kateri koli del pogovora vreden shranjevanja kot splošno znanje ali specifična uporabniška preferenca.

2. **Izvleči in povzeti**: Destilirati bistveno učenje ali preferenco iz pogovora.

3. **Shranjevanje v bazo znanja**: Ohranjati te izvlečene informacije, pogosto v vektorski podatkovni bazi, da jih je mogoče priklicati kasneje.

4. **Dopolnjevanje prihodnjih poizvedb**: Ko uporabnik začne novo poizvedbo, agent za znanje prikliče relevantne shranjene informacije in jih doda uporabnikovemu pozivu, kar zagotavlja ključen kontekst primarnemu agentu (podobno kot RAG).

### Optimizacije za spomin

• **Upravljanje zakasnitve**: Da bi se izognili upočasnjevanju interakcij z uporabnikom, se lahko najprej uporabi cenejši, hitrejši model za hitro preverjanje, ali je informacija vredna shranjevanja ali priklica, pri čemer se bolj kompleksni proces ekstrakcije/priklica sproži le, ko je to potrebno.

• **Vzdrževanje baze znanja**: Za rastočo bazo znanja se lahko manj pogosto uporabljene informacije premaknejo v "hladno shrambo" za upravljanje stroškov.

## Imate več vprašanj o spominu agenta?

Pridružite se [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kjer lahko srečate druge učence, se udeležite uradnih ur in dobite odgovore na svoja vprašanja o AI agentih.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.