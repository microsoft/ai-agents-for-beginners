# Inženiring konteksta za AI agente

[![Inženiring konteksta](../../../translated_images/sl/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Kliknite zgornjo sliko za ogled videa tega učnega gradiva)_

Razumevanje kompleksnosti aplikacije, za katero razvijate AI agenta, je pomembno za izdelavo zanesljivega agenta. Potrebujemo AI agente, ki učinkovito upravljajo informacije za reševanje kompleksnih potreb, ki presegajo samo inženiring promptov.

V tem učnem gradivu bomo pogledali, kaj je inženiring konteksta in njegova vloga pri gradnji AI agentov.

## Uvod

To učnim gradivu bo zajemalo:

• **Kaj je inženiring konteksta** in zakaj se razlikuje od inženiringa promptov.

• **Strategije za učinkovit inženiring konteksta**, vključno s pisanjem, izbiranjem, stiskanjem in izoliranjem informacij.

• **Pogoste napake v kontekstu**, ki lahko ovirajo vaš AI agent, in kako jih odpraviti.

## Cilji učenja

Po zaključku tega učnega gradiva boste razumeli, kako:

• **Določiti inženiring konteksta** in ga ločiti od inženiringa promptov.

• **Prepoznati ključne komponente konteksta** v aplikacijah velikih jezikovnih modelov (LLM).

• **Uporabiti strategije za pisanje, izbor, stiskanje in izolacijo konteksta**, da izboljšate zmogljivost agenta.

• **Prepoznati pogoste napake v kontekstu**, kot so zastrupljanje, motenje, zmeda in konflikti ter uporabiti tehnike za njihovo ublažitev.

## Kaj je inženiring konteksta?

Za AI agente je kontekst tisto, kar vodi načrtovanje AI agenta za izvedbo določenih dejanj. Inženiring konteksta je praksa zagotavljanja, da AI agent ima prave informacije za dokončanje naslednjega koraka naloge. Okno konteksta je omejeno po velikosti, zato kot graditelji agentov moramo razviti sisteme in procese za upravljanje dodajanja, odstranjevanja in stiskanja informacij v oknu konteksta.

### Inženiring promptov vs inženiring konteksta

Inženiring promptov se osredotoča na en nabor statičnih navodil za učinkovito usmerjanje AI agentov z nizom pravil. Inženiring konteksta pa upravlja dinamičen nabor informacij, vključno z začetnim promptom, da zagotovi, da ima AI agent skozi čas to, kar potrebuje. Glavna ideja inženiringa konteksta je narediti ta proces ponovljiv in zanesljiv.

### Vrste konteksta

[![Vrste konteksta](../../../translated_images/sl/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Pomembno je vedeti, da kontekst ni le ena stvar. Informacije, ki jih AI agent potrebuje, lahko prihajajo iz različnih virov in na nas je, da zagotovimo, da ima agent dostop do teh virov:

Vrste konteksta, ki jih lahko AI agent upravlja, vključujejo:

• **Navodila:** To so kot "pravila" za agenta – prompti, sistemska sporočila, primeri z nekaj poskusi (ki pokažejo AI, kako nekaj narediti) in opisi orodij, ki jih lahko uporablja. Tu se osredotočenost inženiringa promptov povezuje z inženiringom konteksta.

• **Znanje:** To vključuje dejstva, informacije pridobljene iz podatkovnih baz ali dolgoročne spomine, ki jih je agent akumuliral. Vključuje sistem Retrieval Augmented Generation (RAG), če agent potrebuje dostop do različnih skladišč znanja in podatkovnih baz.

• **Orodja:** To so definicije zunanjih funkcij, API-jev in MCP strežnikov, ki jih agent lahko kliče, skupaj s povratnimi informacijami (rezultati), ki jih pridobi z uporabo teh orodij.

• **Zgodovina pogovora:** Trenutni dialog z uporabnikom. S časom ti pogovori postajajo daljši in bolj kompleksni, kar zavzame prostor v oknu konteksta.

• **Uporabniške preference:** Informacije o uporabnikovih všečih in nevšečih skozi čas. Te bi lahko bile shranjene in klicane pri sprejemanju ključnih odločitev, da se uporabniku pomaga.

## Strategije za učinkovit inženiring konteksta

### Strategije načrtovanja

[![Najboljše prakse inženiringa konteksta](../../../translated_images/sl/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Dober inženiring konteksta se začne z dobrim načrtovanjem. Tukaj je pristop, ki vam bo pomagal začeti razmišljati o uporabi koncepta inženiringa konteksta:

1. **Določite jasne rezultate** - Rezultati nalog, ki jih bodo AI agenti opravili, morajo biti jasno določeni. Odgovorite na vprašanje - "Kako bo svet izgledal, ko bo AI agent zaključil svojo nalogo?" Z drugimi besedami, kakšna sprememba, informacija ali odgovor naj uporabnik dobi po interakciji z AI agentom.
2. **Zemljevid konteksta** - Ko določite rezultate AI agenta, morate odgovoriti na vprašanje "Kakšne informacije AI agent potrebuje za dokončanje naloge?". Tako lahko začnete mapirati kontekst, kje so te informacije dostopne.
3. **Ustvarite poti za kontekst** - Zdaj, ko veste, kje so informacije, morate odgovoriti na vprašanje "Kako bo agent pridobil te informacije?". To lahko naredite na različne načine, vključno z RAG, uporabo MCP strežnikov in drugih orodij.

### Praktične strategije

Načrtovanje je pomembno, vendar ko informacije začnejo pritekati v okno konteksta našega agenta, potrebujemo praktične strategije za njihovo upravljanje:

#### Upravljanje konteksta

Medtem ko se nekatere informacije v okno konteksta dodajajo samodejno, je inženiring konteksta aktivno upravljanje s temi informacijami, kar lahko izvedemo s pomočjo nekaj strategij:

 1. **Zapisnik agenta**
 Omogoča AI agentu, da si zabeleži pomembne informacije o trenutnih nalogah in interakcijah z uporabnikom med eno sejo. Ta zapisnik naj obstaja zunaj okna konteksta v datoteki ali objektnem prostoru, ki ga agent lahko pozneje v seji poišče, če je potrebno.

 2. **Spomini**
 Zapisniki so primerni za upravljanje informacij zunaj okna konteksta ene seje. Spomini omogočajo agentom shranjevanje in priklic ustreznih informacij čez več sej. To bi lahko vključevalo povzetke, uporabniške preference in povratne informacije za prihodnje izboljšave.

 3. **Stiskanje konteksta**
  Ko okno konteksta naraste in se približuje svoji omejitvi, lahko uporabimo tehnike, kot sta povzemanje in obrezovanje. To vključuje ohranjanje samo najbolj pomembnih informacij ali odstranitev starejših sporočil.
  
 4. **Sistemi z več agenti**
  Razvijanje sistemov z več agenti je oblika inženiringa konteksta, saj ima vsak agent svoje okno konteksta. Kako se ta kontekst deli in prenaša med različnimi agenti, je nekaj, kar je treba načrtovati pri gradnji teh sistemov.
  
 5. **Sandbox okolja**
  Če agent potrebuje zagnati kodo ali obdelati velike količine informacij v dokumentu, to lahko porabi veliko število tokenov za obdelavo rezultatov. Namesto da bi vse to hranil v oknu konteksta, lahko agent uporabi sandbox okolje, ki lahko zažene kodo in le prebere rezultate ter druge relevantne informacije.
  
 6. **Objekti stanja v izvajanju**
   To dosežemo z ustvarjanjem vsebnikov informacij za upravljanje situacij, ko agent potrebuje dostop do določenih informacij. Pri kompleksni nalogi bi to agentu omogočilo shranjevanje rezultatov vsake podnaloge korak za korakom, kar omogoča, da ostane kontekst povezan samo s to specifično podnalogo.

#### Pregledovanje konteksta

Ko uporabite eno od teh strategij, je vredno preveriti, kaj je dejansko prejela naslednja klic modela. Koristno vprašanje za odpravljanje napak je:

> Ali je agent naložil preveč konteksta, napačen kontekst ali pa je manjkalo potrebnega konteksta?

Za odgovor na to vprašanje ni potrebno beležiti surovih promptov, izhodov orodij ali vsebine spomina. V produkciji raje uporabljajte majhne zapise pregleda konteksta, ki zajamejo število, ID-je, heške in oznake pravil:

- **Izbor:** Spremljajte, koliko kandidatnih kosov, orodij ali spominov je bilo obravnavanih, koliko jih je bilo izbranih in katero pravilo ali ocena je povzročila, da so ostali bili filtrirani.
- **Stiskanje:** Zabeležite območje vira ali sledi ID, ID povzetka, ocenjeno število tokenov pred in po stiskanju ter ali je bila surova vsebina izključena iz naslednjega klica.
- **Izolacija:** Zapišite, katera podnaloga se je izvajala v ločenem agentu, seji ali sandboxu, kateri omejeni povzetek je bil vrnjen in ali so veliki rezultati orodij ostali zunaj konteksta glavnega agenta.
- **Spomin in RAG:** Shranjujte ID-je pridobljenih dokumentov, ID-je spomina, ocene, izbrane ID-je in stanje redakcije namesto celotnega pridobljenega besedila.
- **Varnost in zasebnost:** Raje uporabljajte heške, ID-je, vedra tokenov in oznake pravil namesto občutljivega besedila prompta, argumentov orodij, rezultatov orodij ali teles uporabniškega spomina.

Cilj ni hraniti več konteksta. Cilj je pustiti dovolj dokazov, da razvijalec lahko ugotovi, katera strategija konteksta je bila uporabljena in ali je spremenila naslednji klic modela na namenjen način.

### Primer inženiringa konteksta

Recimo, da želimo, da AI agent **"Rezervira potovanje v Pariz."**

• Preprost agent, ki uporablja samo inženiring promptov, bi morda samo odgovoril: **"V redu, kdaj želite iti v Pariz?**". Takrat je obdelal samo vaše neposredno vprašanje.

• Agent, ki uporablja strategije inženiringa konteksta, kot smo jih opisali, bi naredil veliko več. Preden odgovori, bi njegov sistem lahko:

  ◦ **Preveril koledar** za razpoložljive datume (pridobivanje podatkov v realnem času).

 ◦ **Poklical pretekle potovalne preference** (iz dolgoročnega spomina), kot so vaša izbrana letalska družba, proračun ali ali imate raje direktne lete.

 ◦ **Prepoznal razpoložljiva orodja** za rezervacijo letov in hotelov.

- Nato bi bil primer odgovora:  "Hej [Vaše ime]! Vidim, da ste prvi teden oktobra prosti. Naj poiščem direktne lete v Pariz na [izbrani letalski družbi] znotraj vašega običajnega proračuna [proračun]?". Ta bogatejši, kontekstualno ozaveščen odgovor kaže moč inženiringa konteksta.

## Pogoste napake v kontekstu

### Zastrupljanje konteksta

**Kaj je to:** Ko halucinacija (napačna informacija, generirana z LLM) ali napaka vstopi v kontekst in se večkrat omenja, kar povzroči, da agent zasleduje nemogoče cilje ali razvije nesmiselne strategije.

**Kaj storiti:** Uporabite **preverjanje konteksta** in **izolacijo**. Validirajte informacije, preden jih dodate v dolgoročni spomin. Če zaznate možno zastrupljanje, začnite nove nitke konteksta, da preprečite širjenje napačnih informacij.

**Primer rezervacije potovanja:** Vaš agent halucinira **direkten let z majhnega lokalnega letališča do oddaljenega mednarodnega mesta**, ki dejansko ne omogoča mednarodnih letov. Ta neobstoječi podatek o letu se shrani v kontekst. Kasneje, ko prosite agenta za rezervacijo, vztrajno išče vozovnice za to nemogočo pot, kar vodi do ponavljajočih napak.

**Rešitev:** Vključite korak, ki **preveri obstoj in poti letov s pomočjo API-ja v realnem času** _preden_ dodate podatek o letu v delovni kontekst agenta. Če validacija ne uspe, so napačne informacije "izolirane" in se ne uporabljajo naprej.

### Moteči kontekst

**Kaj je to:** Ko kontekst postane tako obsežen, da se model preveč osredotoči na nabrano zgodovino namesto na znanje iz usposabljanja, kar vodi do ponavljajočih ali neuporabnih dejanj. Modeli lahko začnejo delati napake že preden je okno konteksta polno.

**Kaj storiti:** Uporabljajte **povzemanje konteksta**. Občasno stiskajte nabrane informacije v krajše povzetke, pri čemer ohranite pomembne podrobnosti in odstranite ponavljajočo se zgodovino. To pomaga "ponastaviti" fokus.

**Primer rezervacije potovanja:** Dolgo ste razpravljali o različnih sanjskih destinacijah za potovanje, vključno s podrobnim opisom vaše nahrbtnikarske poti od pred dvema letoma. Ko nazadnje prosite, da vam **"najdem poceni let za naslednji mesec,"** se agent zatakne na stare, nepomembne podrobnosti in nenehno sprašuje o vaši nahrbtnikarski opremi ali preteklih itinerarijih, pri tem pa zanemarja vašo aktualno zahtevo.

**Rešitev:** Po določenem številu zamenjav ali ko kontekst preveč naraste, naj agent **povzame najnovejše in najbolj relevantne dele pogovora** – osredotočanje na trenutne datume potovanja in destinacijo – ter uporabi ta strnjen povzetek za naslednji klic LLM, medtem ko ne relevantni zgodovinski pogovor zavrže.

### Konfuzija konteksta

**Kaj je to:** Ko nepotreben kontekst, pogosto v obliki prevelikega števila razpoložljivih orodij, povzroči, da model ustvari slabe odgovore ali kliče nepomembna orodja. Manjši modeli so še posebej dovzetni za to.

**Kaj storiti:** Uporabite **upravljanje izbire orodij** s tehnikami RAG. Shranjujte opise orodij v vektorski podatkovni bazi in izberite _samo_ najbolj relevantna orodja za vsako specifično nalogo. Raziskave kažejo, da je priporočljivo omejiti izbor orodij na manj kot 30.

**Primer rezervacije potovanja:** Vaš agent ima dostop do desetine orodij: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` itd. Vprašate: **"Kakšen je najboljši način za premikanje po Parizu?"** Zaradi velikega števila orodij se agent zmede in poskuša klicati `book_flight` _znotraj_ Pariza ali `rent_car`, čeprav raje uporabljate javni prevoz, ker se opisi orodij lahko prekrivajo ali pa preprosto ne zna izbrati najboljšega.

**Rešitev:** Uporabite **RAG nad opisi orodij**. Ko vprašate o premikanju po Parizu, sistem dinamično pridobi _samo_ najbolj relevantna orodja, kot so `rent_car` ali `public_transport_info`, glede na vaš poizvedbo, ter predstavi osredotočeno "izbor" orodij LLM-u.

### Konflikt konteksta

**Kaj je to:** Ko obstajajo nasprotujoče si informacije v kontekstu, kar vodi do nekonsistentnega sklepanja ali slabih končnih odgovorov. To se pogosto zgodi, ko informacije prihajajo postopoma, in zgodnje, napačne predpostavke ostanejo v kontekstu.

**Kaj storiti:** Uporabite **obrezovanje konteksta** in **odtovoritev**. Obrezovanje pomeni odstranjevanje zastarelih ali nasprotujočih informacij, ko prispejo novi podatki. Odtovoritev modelu da ločen "zapisnik" delovni prostor, da lahko obdeluje informacije brez natrpanosti glavnega konteksta.


**Primer rezervacije potovanja:** Sprva svojemu agentu povedo, **"Želim leteti v ekonomski razred."** Kasneje v pogovoru spremenite mnenje in rečete, **"Pravzaprav pojdiva na tem potovanju v poslovni razred."** Če obe navodili ostaneta v kontekstu, lahko agent prejme nasprotujoče si rezultate iskanja ali pa se zmede glede tega, katero preference naj daje prednost.

**Rešitev:** Uvedite **pruning konteksta**. Ko novo navodilo nasprotuje staremu, se starejše navodilo odstrani ali eksplicitno omogoči nadomestitev v kontekstu. Alternativno lahko agent uporabi **zvezek za beležke**, da uskladi nasprotujoče preference, preden se odloči, s čimer zagotovi, da ga pri dejavnostih vodi le končno, skladno navodilo.

## Imate še več vprašanj o inženirstvu konteksta?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da spoznate druge učence, se udeležite uradnih ur in dobite odgovore na svoja vprašanja o AI agentih.
## Prejšnja lekcija

[Agentni protokoli](../11-agentic-protocols/README.md)

## Naslednja lekcija

[Spomin za AI agente](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->