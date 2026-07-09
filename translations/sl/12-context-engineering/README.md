# Inženiring konteksta za AI agente

[![Inženiring konteksta](../../../translated_images/sl/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Kliknite na zgornjo sliko za ogled videa tega lekcijona)_

Razumevanje kompleksnosti aplikacije, za katero gradite AI agenta, je pomembno za izdelavo zanesljivega agenta. Potrebujemo AI agente, ki učinkovito upravljajo informacije za reševanje kompleksnih potreb, ki presegajo samo oblikovanje pozivov.

V tem lekcijonu si bomo ogledali, kaj je inženiring konteksta in kakšna je njegova vloga pri izdelavi AI agentov.

## Uvod

Ta lekcija bo zajemala:

• **Kaj je inženiring konteksta** in zakaj se razlikuje od oblikovanja pozivov.

• **Strategije za učinkovit inženiring konteksta**, vključno s tem, kako pisati, izbirati, stiskati in izolirati informacije.

• **Pogoste napake konteksta**, ki lahko pokvarijo vašega AI agenta in kako jih odpraviti.

## Cilji učenja

Po zaključku te lekcije boste razumeli, kako:

• **Določiti inženiring konteksta** in ga razlikovati od oblikovanja pozivov.

• **Prepoznati ključne komponente konteksta** v aplikacijah velikih jezikovnih modelov (LLM).

• **Uporabiti strategije za pisanje, izbiro, stiskanje in izolacijo konteksta** za izboljšanje zmogljivosti agentov.

• **Prepoznati pogoste napake konteksta**, kot so zastrupitev, motenje, zmeda in konflikt, ter uvesti tehnike za njihovo omilitev.

## Kaj je inženiring konteksta?

Za AI agente je kontekst tisto, kar usmerja načrtovanje AI agenta za izvedbo določenih dejanj. Inženiring konteksta je praksa zagotavljanja, da AI agent ima pravilne informacije za dokončanje naslednjega koraka naloge. Okno konteksta je omejeno po velikosti, zato kot razvijalci agentov moramo zgraditi sisteme in postopke za upravljanje dodajanja, odstranjevanja in kondenzacije informacij v oknu konteksta.

### Oblikovanje pozivov proti inženiringu konteksta

Oblikovanje pozivov se osredotoča na en niz statičnih navodil za učinkovito usmerjanje AI agentov z nizom pravil. Inženiring konteksta pa pomeni upravljanje dinamičnega nabora informacij, vključno z začetnim pozivom, da se zagotovi, da ima AI agent skozi čas, kar potrebuje. Glavna ideja inženiringa konteksta je, da se ta proces naredi ponovljiv in zanesljiv.

### Vrste konteksta

[![Vrste konteksta](../../../translated_images/sl/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Pomembno je zapomniti si, da kontekst ni le ena stvar. Informacije, ki jih AI agent potrebuje, lahko prihajajo iz različnih virov in naša naloga je zagotoviti, da ima agent dostop do teh virov:

Vrste konteksta, ki jih mora AI agent morda upravljati, vključujejo:

• **Navodila:** To so kot "pravila" agenta – pozivi, sistemska sporočila, primeri z nekaj primeri (ki AI pokažejo, kako nekaj narediti) in opisi orodij, ki jih lahko uporablja. Tukaj se področji oblikovanja pozivov in inženiringa konteksta prepletata.

• **Znanje:** To pokriva dejstva, informacije, pridobljene iz baz podatkov, ali dolgoročne spomine, ki jih je agent zbral. Vključuje tudi integracijo sistema Retrieval Augmented Generation (RAG), če agent potrebuje dostop do različnih shramb znanja in baz podatkov.

• **Orodja:** To so definicije zunanjih funkcij, API-jev in MCP strežnikov, do katerih lahko agent dostopa, skupaj s povratnimi informacijami (rezultati), ki jih prejme z njihovo uporabo.

• **Zgodovina pogovora:** Neprekinjen dialog z uporabnikom. S časom ti pogovori postajajo daljši in bolj kompleksni, kar zavzame prostor v oknu konteksta.

• **Uporabniške preference:** Informacije, ki so bile sčasoma zbrane o uporabnikovih željah ali nepripravah. Te se lahko shranjujejo in kličeta ob ključnih odločitvah za pomoč uporabniku.

## Strategije za učinkovit inženiring konteksta

### Strategije načrtovanja

[![Najboljše prakse inženiringa konteksta](../../../translated_images/sl/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Dober inženiring konteksta se začne z dobrim načrtovanjem. Tukaj je pristop, ki vam bo pomagal začeti razmišljati o tem, kako uporabiti koncept inženiringa konteksta:

1. **Določite jasne rezultate** - Rezultati nalog, ki jih bodo AI agenti izvedli, morajo biti jasno opredeljeni. Odgovorite na vprašanje - "Kako bo svet izgledal, ko bo AI agent opravil svojo nalogo?" Z drugimi besedami, kakšna sprememba, informacija ali odgovor naj bi uporabnik prejel po interakciji z AI agentom.
2. **Mapirajte kontekst** - Ko določite rezultate AI agenta, morate odgovoriti na vprašanje "Kakšne informacije potrebuje AI agent za dokončanje te naloge?". Tako lahko začnete mapirati kontekst, kje so te informacije lahko locirane.
3. **Ustvarite kontekstualne cevovode** - Ko veste, kje so informacije, morate odgovoriti na vprašanje "Kako bo agent dobil te informacije?". To je mogoče narediti na različne načine, vključno z RAG, uporabo MCP strežnikov in drugih orodij.

### Praktične strategije

Načrtovanje je pomembno, toda ko informacije začnejo pritekati v okno našega agenta, potrebujemo praktične strategije za njihovo upravljanje:

#### Upravljanje konteksta

Medtem ko se nekatere informacije samodejno dodajo v okno konteksta, je inženiring konteksta o bolj aktivnem obvladovanju teh informacij, kar lahko naredimo z nekaj strategijami:

 1. **Beležnica agenta**
 Omogoča, da AI agent med eno sejo beleži pomembne informacije o trenutnih nalogah in interakcijah z uporabnikom. Ta bi morala biti zunaj okna konteksta, v datoteki ali ob objektu za izvajanje, ki jih lahko agent pozneje pridobi med to sejo, če je potrebno.

 2. **Spomini**
 Beležnice so dobre za upravljanje informacij zunaj okna konteksta ene seje. Spomini omogočajo agentom shranjevanje in pridobivanje relevantnih informacij preko več sej. To lahko vključuje povzetke, uporabniške preference in povratne informacije za izboljšave v prihodnosti.

 3. **Stiskanje konteksta**
  Ko okno konteksta raste in se bliža svoji meji, lahko uporabimo tehnike, kot so povzema in rezanje. To vključuje ohranjanje samo najbolj relevantnih informacij ali odstranjevanje starejših sporočil.
  
 4. **Sistemi z več agenti**
  Razvoj sistema z več agenti je oblika inženiringa konteksta, saj ima vsak agent svoje okno konteksta. Kako se ta kontekst deli in prenaša med različnimi agenti, je še ena stvar, ki jo je treba načrtovati pri gradnji teh sistemov.
  
 5. **Sandbox okolja**
  Če agent potrebuje zagnati kakšno kodo ali procesirati velike količine informacij v dokumentu, to lahko zahteva veliko število tokenov za obdelavo rezultatov. Namesto da bi vse to shranili v oknu konteksta, agent lahko uporabi sandbox okolje, ki lahko zažene to kodo in prebere samo rezultate in druge relevantne informacije.
  
 6. **Objekti stanja pri izvajanju**
   To se naredi z ustvarjanjem vsebnikov informacij za upravljanje situacij, ko agent potrebuje dostop do določenih informacij. Za kompleksno nalogo bi to omogočilo agentu shranjevanje rezultatov posameznih podnalog korak za korakom, kar omogoča, da kontekst ostane povezan samo z določeno podnalogo.

#### Pregledovanje konteksta

Ko uporabite eno od teh strategij, je vredno preveriti, kaj je naslednji klic modela dejansko prejel. Koristno vprašanje za odpravljanje napak je:

> Ali je agent naložil preveč konteksta, napačen kontekst ali pa manjkajoče informacije, ki jih je potreboval?

Za odgovor na to vprašanje ne potrebujete beležiti surovih pozivov, rezultatov orodij ali vsebine spomina. V produkciji raje uporabite majhne zapise o pregledu konteksta, ki zajemajo število, id-je, hashe in oznake pravil:

- **Izbira:** Sledite, koliko kandidatskih kosov, orodij ali spominov je bilo upoštevano, koliko jih je bilo izbranih in katero pravilo ali rezultat je povzročil filtriranje ostalih.
- **Stiskanje:** Zabeležite obseg vira ali sledilni id, id povzetka, ocenjeni števec tokenov pred in po stiskanju ter ali je bila surova vsebina izključena iz naslednjega klica.
- **Izolacija:** Zabeležite, katera podnaloga je tekla v ločenem agentu, seji ali sandboxu, kateri omejeni povzetek je bil vrnjen in ali je izhod velikega orodja ostal zunaj konteksta matičnega agenta.
- **Spomini in RAG:** Shranite id-je dokumentov za pridobivanje, id-je spomina, ocene, izbrane id-je in status cenzure namesto celotnega pridobljenega besedila.
- **Varnost in zasebnost:** Raje izberite hashe, id-je, token vedra in oznake pravil namesto občutljivega besedila poziva, argumentov orodij, rezultatov orodij ali vsebine uporabniških spominov.

Cilj ni obdržati več konteksta, ampak pustiti dovolj dokazov, da razvijalec lahko pove, katera strategija konteksta je bila uporabljena in ali je sprememba vplivala na naslednji klic modela na želeni način.

### Primer inženiringa konteksta

Recimo, da želimo, da AI agent **"Rezervira potovanje v Pariz."**

• Preprost agent, ki uporablja le oblikovanje pozivov, bi morda preprosto odgovoril: **"V redu, kdaj bi radi šli v Pariz?"**. Obdelal je samo vaše neposredno vprašanje v času, ko je bilo zastavljeno.

• Agent, ki uporablja strategije inženiringa konteksta, bi naredil veliko več. Preden odgovori, bi njegov sistem morda:

  ◦ **Preveril vaš koledar** za razpoložljive datume (pridobivanje podatkov v realnem času).

 ◦ **Poklical prejšnje potovalne preference** (iz dolgoročnega spomina), kot so vaša priljubljena letalska družba, proračun ali ali raje imate neposredne lete.

 ◦ **Ugotovil razpoložljiva orodja** za rezervacijo letov in hotelov.

- Nato bi lahko bil primer odgovora: "Hej [Vaše ime]! Vidim, da ste prvi teden oktobra prosti. Naj poiščem neposredne lete v Pariz z [Priljubljena letalska družba] v okviru vašega običajnega proračuna [Proračun]?" Ta bogatejši, kontekstno ozaveščen odgovor prikazuje moč inženiringa konteksta.

## Pogoste napake konteksta

### Zastrupitev konteksta

**Kaj je to:** Ko v kontekst vstopi halucinacija (napačna informacija, ki jo generira LLM) ali napaka in je večkrat omenjeno, zaradi česar agent sledi nemogočim ciljem ali razvije nesmiselne strategije.

**Kaj storiti:** Uvedite **validacijo konteksta** in **karanteno**. Validirajte informacije preden jih dodate v dolgoročni spomin. Če je zaznana možna zastrupitev, začnite nove nitke konteksta, da preprečite širjenje slabih informacij.

**Primer rezervacije potovanja:** Vaš agent halucinira **neposredni let iz majhnega lokalnega letališča v oddaljeno mednarodno mesto**, ki dejansko ne nudi mednarodnih letov. Ta neobstoječi podatek o letu se shrani v kontekst. Kasneje, ko agentu naročite rezervacijo, še naprej poskuša najti vozovnice za to nemogočo pot, kar povzroča ponavljajoče se napake.

**Rešitev:** Uvedite korak, ki **validira obstoj leta in poti z API-jem v realnem času** _preden_ dodate podatek o letu v delovni kontekst agenta. Če validacija ne uspe, se napačna informacija "karanteni", zato se ne uporablja naprej.

### Motenje konteksta

**Kaj je to:** Ko kontekst postane tako velik, da se model preveč osredotoči na kopičeno zgodovino namesto na tisto, kar se je naučil med usposabljanjem, kar vodi do ponavljajočih se ali neučinkovitih dejanj. Modeli lahko začnejo delati napake že preden je okno konteksta polno.

**Kaj storiti:** Uporabite **povzemanje konteksta**. Občasno stisnite nabrane informacije v krajše povzetke, ki ohranijo pomembne podrobnosti in odstranijo odvečno zgodovino. To pomaga pri "ponastavitvi" fokusa.

**Primer rezervacije potovanja:** Dolgo ste razpravljali o različnih sanjskih destinacijah, vključno z natančnim opisom vašega potovanja s nahrbtnikom pred dvema letoma. Ko končno vprašate za **"najti poceni let za naslednji mesec,"** se agent zatakne v starih, nepomembnih podrobnostih in stalno sprašuje o vaši opremi za nahrbtnik ali preteklih načrtih ter zanemarja vašo trenutno zahtevo.

**Rešitev:** Po določenem številu krogov ali ko kontekst preraste mejo, naj agent **povzame najnovejše in najbolj relevantne dele pogovora** – osredotočeno na vaše trenutne datume potovanja in destinacijo – in ta strnjen povzetek uporabi za naslednji klic LLM, medtem ko odstrani manj relevantni zgodovinski pogovor.

### Zmeda konteksta

**Kaj je to:** Ko nepotreben kontekst, pogosto v obliki prevelikega števila razpoložljivih orodij, povzroči, da model generira slabe odgovore ali kliče nepomembna orodja. Manjši modeli so za to še posebej dovzetni.

**Kaj storiti:** Uvedite **upravljanje nalaganja orodij** z uporabo RAG tehnik. Shranjujte opise orodij v vektorski bazi podatkov in izbirajte _le_ najbolj relevantna orodja za vsak specifičen zadatak. Raziskave kažejo, da je smiselno omejiti izbiro orodij na manj kot 30.

**Primer rezervacije potovanja:** Vaš agent ima dostop do ducatov orodij: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` itd. Vprašate: **"Kakšen je najboljši način gibanja po Parizu?"** Zaradi velikega števila orodij se agent zmede in poskuša poklicati `book_flight` _znotraj_ Pariza ali `rent_car`, čeprav raje uporabljate javni prevoz, saj se opisi orodij lahko prekrivajo ali pa preprosto ne zna razločiti najboljšega.

**Rešitev:** Uporabite **RAG nad opisi orodij**. Ko vprašate, kako se gibati po Parizu, sistem dinamično pridobi _le_ najbolj relevantna orodja, kot so `rent_car` ali `public_transport_info` glede na vaš poizvedbo, in predstavi osredotočen "nabor" orodij LLM-u.

### Konflikt konteksta

**Kaj je to:** Ko v kontekstu obstajajo nasprotujoče si informacije, kar vodi do nekonsistentnega sklepanja ali slabih končnih odgovorov. To se pogosto zgodi, ko informacije prihajajo v fazah, in zgodnje, napačne predpostavke ostanejo v kontekstu.

**Kaj storiti:** Uporabite **obrezovanje konteksta** in **odlaganje**. Obrezovanje pomeni odstranjevanje zastarelih ali nasprotujočih informacij, ko prispejo novi podatki. Odlaganje daje modelu ločeno delovno območje ("beležnico"), kjer lahko procesuira informacije brez zasičenja glavnega konteksta.


**Primer rezervacije potovanja:** Sprva agentu poveste, **"Želim leteti v ekonomski razred."** Kasneje v pogovoru spremenite mnenje in rečete, **"Pravzaprav pojdimo za to potovanje v poslovni razred."** Če obe navodili ostaneta v kontekstu, lahko agent prejme nasprotujoče si rezultate iskanja ali pa se zmede glede tega, katero preference naj da v ospredje.

**Rešitev:** Uvedite **obrezovanje konteksta**. Ko novo navodilo nasprotuje staremu, se starejše navodilo odstrani ali eksplicitno nadomesti v kontekstu. Alternativno lahko agent uporabi **osnutek** za uskladitev nasprotujočih si preferenc, preden se odloči, s čimer se zagotovi, da samo končno, skladno navodilo vodi njegove ukrepe.

## Imate še več vprašanj o inženirstvu konteksta?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da se srečate z drugimi učenci, obiščete uradne ure in dobite odgovore na vprašanja o umetni inteligenci agentov.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->