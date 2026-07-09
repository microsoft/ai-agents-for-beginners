# Inženjering konteksta za AI agente

[![Inženjering konteksta](../../../translated_images/hr/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Kliknite na gornju sliku za pregled videa ove lekcije)_

Razumijevanje složenosti aplikacije za koju gradite AI agenta važno je za izradu pouzdanog agenta. Moramo graditi AI agente koji učinkovito upravljaju informacijama kako bi odgovarali na složene potrebe koje nadilaze samo inženjering promptova.

U ovoj lekciji pogledat ćemo što je inženjering konteksta i njegovu ulogu u izgradnji AI agenata.

## Uvod

Ova lekcija će pokriti:

• **Što je inženjering konteksta** i zašto se razlikuje od inženjeringa promptova.

• **Strategije za učinkovit inženjering konteksta**, uključujući kako pisati, odabrati, komprimirati i izolirati informacije.

• **Česte pogreške u kontekstu** koje mogu sabotirati vašeg AI agenta i kako ih ispraviti.

## Ciljevi učenja

Nakon završetka ove lekcije, razumjet ćete kako:

• **Definirati inženjering konteksta** i razlikovati ga od inženjeringa promptova.

• **Prepoznati ključne komponente konteksta** u aplikacijama velikih jezičnih modela (LLM).

• **Primijeniti strategije za pisanje, odabir, kompresiju i izolaciju konteksta** za poboljšanje izvedbe agenta.

• **Prepoznati česte neuspjehe u kontekstu** kao što su trovanje, distrakcija, zbunjenost i sukob, i primijeniti tehnike ublažavanja.

## Što je inženjering konteksta?

Za AI agente, kontekst je ono što pokreće planiranje AI agenta da poduzme određene radnje. Inženjering konteksta je praksa osiguravanja da AI agent ima prave informacije za dovršetak sljedećeg koraka zadatka. Prozor konteksta je ograničen veličinom, stoga, kao graditelji agenata, trebamo izgraditi sustave i procese za upravljanje dodavanjem, uklanjanjem i sažimanjem informacija u prozoru konteksta.

### Inženjering prompta vs. inženjering konteksta

Inženjering prompta fokusiran je na jedinstveni set statičkih uputa za učinkovito vođenje AI agenata skupom pravila. Inženjering konteksta odnosi se na upravljanje dinamičkim skupom informacija, uključujući početni prompt, kako bi se osiguralo da AI agent ima ono što mu je potrebno tijekom vremena. Glavna ideja oko inženjeringa konteksta je učiniti taj proces ponovljivim i pouzdanim.

### Vrste konteksta

[![Vrste konteksta](../../../translated_images/hr/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Važno je zapamtiti da kontekst nije samo jedna stvar. Informacije koje AI agent treba mogu dolaziti iz različitih izvora i na nama je da osiguramo agentu pristup tim izvorima:

Vrste konteksta koje AI agent može trebati upravljati uključuju:

• **Upute:** Ovo su kao "pravila" agenta – promptovi, sistemske poruke, primjeri few-shot (pokazujući AI kako nešto napraviti) i opisi alata koje može koristiti. Tu se fokus inženjeringa prompta kombinira s inženjeringom konteksta.

• **Znanje:** Obuhvaća činjenice, informacije dohvaćene iz baza podataka ili dugoročna sjećanja koja je agent akumulirao. Ovo uključuje integraciju Retrieval Augmented Generation (RAG) sustava ako agent treba pristup različitim spremištima znanja i bazama podataka.

• **Alati:** To su definicije vanjskih funkcija, API-ja i MCP servera koje agent može pozvati, zajedno s povratnim informacijama (rezultatima) koje dobiva korištenjem tih alata.

• **Povijest razgovora:** Tijekli dijalog s korisnikom. Kako vrijeme prolazi, ti se razgovori produljuju i postaju složeniji što zauzima prostor u prozoru konteksta.

• **Preferencije korisnika:** Informacije naučene o korisnikovim preferencijama ili odbojnostima tijekom vremena. One se mogu pohraniti i koristiti prilikom donošenja ključnih odluka za pomoć korisniku.

## Strategije za učinkoviti inženjering konteksta

### Strategije planiranja

[![Najbolje prakse inženjeringa konteksta](../../../translated_images/hr/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Dobar inženjering konteksta počinje s dobrim planiranjem. Ovo je pristup koji će vam pomoći razmisliti kako primijeniti koncept inženjeringa konteksta:

1. **Definirajte jasne rezultate** - rezultati zadataka koje će AI agenti izvršavati trebaju biti jasno definirani. Odgovorite na pitanje - "Kako će svijet izgledati kada AI agent završi svoj zadatak?" Drugim riječima, kakva promjena, informacija ili odgovor korisnik treba imati nakon interakcije s AI agentom.
2. **Mapirajte kontekst** - nakon što definirate rezultate AI agenta, trebate odgovoriti na pitanje "Koje informacije AI agent treba kako bi dovršio ovaj zadatak?". Tako možete početi mapirati gdje se te informacije mogu nalaziti.
3. **Kreirajte kontekstne pipelineove** - sada kad znate gdje su informacije, morate odgovoriti na pitanje "Kako će agent dobiti ove informacije?". Ovo se može napraviti na različite načine uključujući RAG, korištenje MCP servera i drugih alata.

### Praktične strategije

Planiranje je važno, ali kada informacije počnu pristizati u prozor konteksta agenta, trebamo imati praktične strategije za upravljanje:

#### Upravljanje kontekstom

Dok se neke informacije automatski dodaju u prozor konteksta, inženjering konteksta podrazumijeva aktivnije upravljanje tom informacijom što se može ostvariti kroz nekoliko strategija:

 1. **Bilješke agenta (Agent Scratchpad)**
 Ovo dopušta AI agentu da bilježi relevantne informacije o tekućim zadacima i interakcijama s korisnikom tijekom jedne sesije. Trebalo bi postojati izvan kontekstnog prozora u datoteci ili objektu za vrijeme rada koje agent može kasnije dohvatiti tijekom te sesije ako je potrebno.

 2. **Sjećanja**
 Bilješke su dobre za upravljanje informacijama izvan prozora konteksta jedne sesije. Sjećanja omogućuju agentima pohranu i dohvat relevantnih informacija kroz više sesija. To može uključivati sažetke, korisničke preferencije i povratne informacije za buduća poboljšanja.

 3. **Sažimanje konteksta**
  Kada prozor konteksta raste i približava se svom limitu, mogu se koristiti tehnike poput sažimanja i obrezivanja. To uključuje zadržavanje samo najvažnijih informacija ili uklanjanje starijih poruka.
  
 4. **Više-agentni sustavi**
  Razvijanje više-agentnih sustava je oblik inženjeringa konteksta jer svaki agent ima svoj vlastiti kontekstni prozor. Kako se taj kontekst dijeli i prenosi na različite agente treba planirati prilikom gradnje tih sustava.
  
 5. **Sandbox okruženja**
  Ako agent treba izvršiti neki kod ili obraditi velike količine podataka u dokumentu, to može zahtijevati veliki broj tokena za obradu rezultata. Umjesto da se svi ti podaci pohranjuju u kontekstni prozor, agent može koristiti sandbox okruženje koje izvršava kod i samo čita rezultate i druge relevantne informacije.
  
 6. **Objekti stanja tijekom rada (Runtime State Objects)**
   Ovo se radi stvaranjem spremnika informacija za upravljanje situacijama kada agent treba pristup određenim informacijama. Za složen zadatak, ovo omogućuje agentu pohranu rezultata svake podzadataka korak po korak, dopuštajući kontekstu da ostane povezan samo s tim specifičnim podzadatkom.

#### Inspekcija konteksta

Nakon primjene neke od ovih strategija, korisno je provjeriti što je sljedeći poziv modela zapravo primio. Korisno pitanje za otklanjanje pogrešaka je:

> Je li agent učitao previše konteksta, pogrešan kontekst ili je možda propustio kontekst koji je trebao?

Ne treba se zapisuju sirovi promptovi, izlazi alata ili sadržaji memorije da bi se odgovorilo na to pitanje. U produkciji su poželjni mali zapisi inspekcije konteksta koji bilježe brojeve, id-ove, hash-eve i oznake politika:

- **Izbor:** Pratiti koliko je kandidata (dijelova, alata ili memorija) razmatrano, koliko je odabrano i koje pravilo ili ocjena su uzrokovali filtraciju ostalih.
- **Kompresija:** Zapisati izvorni opseg ili trag id, id sažetka, procijenjeni broj tokena prije i poslije kompresije, i je li sirovi sadržaj isključen iz sljedećeg poziva.
- **Izolacija:** Zabilježiti koji je podzadatak pokrenut u zasebnom agentu, sesiji ili sandboxu, koji sažetak je vraćen i je li veliki izlaz alata ostao izvan glavnog konteksta roditeljskog agenta.
- **Memorija i RAG:** Pohraniti id-ove dokumenata za dohvat, id-ove memorija, ocjene, odabrane id-ove i status cenzure umjesto punog preuzetog teksta.
- **Sigurnost i privatnost:** Preferirati hash-eve, id-ove, token bucket-e i oznake politika umjesto osjetljivog teksta prompta, argumenata alata, rezultata alata ili tijela korisničke memorije.

Cilj nije pohraniti više konteksta. Cilj je ostaviti dovoljno dokaza da programer može reći koja je strategija konteksta primijenjena i je li promijenila sljedeći poziv modela na predviđeni način.

### Primjer inženjeringa konteksta

Recimo da želimo da AI agent **"Rezervira mi putovanje u Pariz."**

• Jednostavan agent koji koristi samo inženjering prompta mogao bi odgovoriti: **"U redu, kada biste željeli ići u Pariz?"**. Obradio je samo vaše izravno pitanje u trenutku kad je korisnik to pitao.

• Agent koji koristi strategije inženjeringa konteksta pokrivene ovdje učinio bi puno više. Prije nego što odgovori, njegov bi sustav mogao:

  ◦ **Provjeriti vaš kalendar** za dostupne datume (dohvaćajući podatke u stvarnom vremenu).

 ◦ **Prisjetiti se prethodnih putnih preferencija** (iz dugoročne memorije) poput vaše omiljene aviokompanije, budžeta ili preferencije za izravne letove.

 ◦ **Identificirati dostupne alate** za rezervaciju leta i hotela.

- Zatim, primjer odgovora mogao bi biti: "Hej [Vaše Ime]! Vidim da ste slobodni prvi tjedan u listopadu. Da li da potražim izravne letove za Pariz na [preferiranoj aviokompaniji] unutar vašeg uobičajenog budžeta od [budžet]?" Ovaj bogatiji, kontekstu prilagođeni odgovor demonstrira moć inženjeringa konteksta.

## Česte pogreške u kontekstu

### Trovanje konteksta

**Što je:** Kada halucinacija (lažna informacija generirana od strane LLM-a) ili pogreška uđu u kontekst i ponavljano se referenciraju, uzrokujući da agent slijedi nemoguće ciljeve ili razvija besmislene strategije.

**Što učiniti:** Provesti **validaciju konteksta** i **karantenu**. Validirati informacije prije nego što se dodaju u dugoročnu memoriju. Ako se detektira moguće trovanje, započeti nove kontekstne threadove kako bi se spriječilo širenje loših informacija.

**Primjer rezervacije putovanja:** Vaš agent halucinira **izravni let sa malog lokalnog aerodroma do udaljenog međunarodnog grada** koji zapravo ne nudi međunarodne letove. Taj nepostojeći detalj leta se sprema u kontekst. Kasnije, kad tražite agentu da rezervira, agent stalno pokušava pronaći karte za ovu nemoguću rutu, što dovodi do ponovljenih pogrešaka.

**Rješenje:** Provesti korak koji **validira postojanje leta i rute pomoću API-ja u stvarnom vremenu** _prije_ no što se detalj leta doda u radni kontekst agenta. Ako validacija ne uspije, pogrešna informacija se "karantenski" izolira i ne koristi dalje.

### Distrakcija konteksta

**Što je:** Kada kontekst postane toliko velik da model previše fokusira na akumuliranu povijest umjesto da koristi ono što je naučio tijekom treniranja, što vodi do ponavljajućih ili neproduktivnih radnji. Modeli mogu početi griješiti čak i prije nego što je prozor konteksta ispunjen.

**Što učiniti:** Koristiti **sažimanje konteksta**. Povremeno sažimati akumulirane informacije u kraće sažetke zadržavajući važne pojedinosti dok se uklanja redundantna povijest. To pomaže "resetirati" fokus.

**Primjer rezervacije putovanja:** Dugotrajno ste pričali o različitim sanjarskim putnim destinacijama, uključujući detaljan opis vašeg backpacking putovanja od prije dvije godine. Kada napokon zatražite **"pronađi mi jeftin let za idući mjesec"**, agent se zaglavi u starim, nevažnim detaljima i stalno vas upitava o vašoj opremi za backpacking ili prošlim itinerarima, zanemarujući vaš trenutni zahtjev.

**Rješenje:** Nakon određenog broja okreta ili kada kontekst postane prevelik, agent treba **sažeti najnovije i relevantne dijelove razgovora** – fokusirajući se na vaše trenutne datume putovanja i destinaciju – i koristiti taj skraćeni sažetak za sljedeći LLM poziv, odbacujući manje relevantni povijesni razgovor.

### Zbunjenost konteksta

**Što je:** Kada nepotreban kontekst, često u obliku previše dostupnih alata, uzrokuje da model generira loše odgovore ili poziva irelevantne alate. Manji modeli su naročito skloni ovome.

**Što učiniti:** Implementirati **upravljanje učitavanjem alata** koristeći RAG tehnike. Spremiti opise alata u vektorsku bazu podataka i odabrati _samo_ najrelevantnije alate za svaki konkretan zadatak. Istraživanja pokazuju da je dobro ograničiti odabir alata na manje od 30.

**Primjer rezervacije putovanja:** Vaš agent ima pristup desecima alata: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations`, itd. Pitate, **"Kako je najbolje kretati se po Parizu?"** Zbog velikog broja alata, agent se zbuni i pokuša pozvati `book_flight` _unutar_ Pariza, ili `rent_car` iako preferirate javni prijevoz, jer se opisi alata mogu preklapati ili jednostavno ne može razlučiti koji je najbolji.

**Rješenje:** Koristiti **RAG na opisima alata**. Kada pitate o kretanju po Parizu, sustav dinamički dohvaća _samo_ najrelevantnije alate kao što su `rent_car` ili `public_transport_info` na temelju vašeg upita, predstavljajući usmjereni "set" alata za LLM.

### Sukob u kontekstu

**Što je:** Kada unutar konteksta postoje kontradiktorne informacije što vodi do nekonzistentnog rezoniranja ili loših konačnih odgovora. To se često događa kada informacije dolaze u fazama, a rani, netočni pretpostavke ostaju u kontekstu.

**Što učiniti:** Koristiti **obrezivanje konteksta** i **prekidno preusmjeravanje**. Obrezivanje znači uklanjanje zastarjelih ili kontradiktornih informacija kako stižu nove pojedinosti. Preusmjeravanje daje modelu zasebni "radni prostor" (scratchpad) za obradu informacija bez zatrpavanja glavnog konteksta.


**Primjer rezervacije putovanja:** U početku kažete svom agentu, **"Želim letjeti u ekonomskoj klasi."** Kasnije u razgovoru promijenite mišljenje i kažete, **"Zapravo, za ovo putovanje idemo u poslovnoj klasi."** Ako obje upute ostanu u kontekstu, agent može dobiti kontradiktorne rezultate pretraživanja ili se zbuniti koja se preferencija treba dati prednost.

**Rješenje:** Implementirajte **rezanje konteksta**. Kada nova uputa kontradiktira staroj, starija uputa se uklanja ili eksplicitno nadjačava u kontekstu. Alternativno, agent može koristiti **radnu bilježnicu** za usklađivanje sukobljenih preferencija prije donošenja odluke, osiguravajući da samo konačna, konzistentna uputa vodi njegove radnje.

## Imate još pitanja o kontekstualnom inženjerstvu?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) zajednici kako biste upoznali druge učenike, sudjelovali na konzultacijama i dobili odgovore na pitanja o AI agentima.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->