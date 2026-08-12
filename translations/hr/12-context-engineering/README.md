# Inženjering konteksta za AI agente

[![Inženjering konteksta](../../../translated_images/hr/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Kliknite sliku iznad za prikaz videa ovog lekcija)_

Razumijevanje složenosti aplikacije za koju gradite AI agenta važno je za izradu pouzdanog. Moramo graditi AI agente koji učinkovito upravljaju informacijama kako bi odgovorili na složene potrebe, što nadilazi samo inženjering podataka.

U ovoj lekciji pogledat ćemo što je inženjering konteksta i njegovu ulogu u izgradnji AI agenata.

## Uvod

Ova lekcija će obuhvatiti:

• **Što je inženjering konteksta** i zašto se razlikuje od inženjeringa podataka.

• **Strategije za učinkovit inženjering konteksta**, uključujući kako pisati, odabrati, sažeti i izolirati informacije.

• **Uobičajene pogreške u kontekstu** koje mogu osujetiti vaš AI agent i kako ih popraviti.

## Ciljevi učenja

Nakon završetka ove lekcije znat ćete kako:

• **Definirati inženjering konteksta** i razlikovati ga od inženjeringa podataka.

• **Prepoznati ključne komponente konteksta** u primjenama velikih jezičnih modela (LLM).

• **Primijeniti strategije pisanja, odabira, sažimanja i izolacije konteksta** za poboljšanje performansi agenta.

• **Prepoznati uobičajene pogreške u kontekstu** poput trovanja, ometanja, zbunjenosti i sukoba, te primijeniti tehnike ublažavanja.

## Što je inženjering konteksta?

Za AI agente, kontekst je ono što pokreće planiranje AI agenta da poduzme određene akcije. Inženjering konteksta je praksa osiguravanja da AI agent ima prave informacije za dovršetak sljedećeg koraka zadatka. Kontekstni prozor je ograničen veličinom, stoga kao konstruktori agenata, trebamo graditi sustave i procese za upravljanje dodavanjem, uklanjanjem i sažimanjem informacija u kontekstnom prozoru.

### Inženjering podataka naspram inženjeringa konteksta

Inženjering podataka fokusira se na jedini set statičnih uputa za učinkovito vođenje AI agenata skupom pravila. Inženjering konteksta odnosi se na upravljanje dinamičnim setom informacija, uključujući početni prompt, kako bi se osiguralo da AI agent ima ono što mu treba tijekom vremena. Glavna ideja inženjeringa konteksta je da ovaj proces bude ponovljiv i pouzdan.

### Vrste konteksta

[![Vrste konteksta](../../../translated_images/hr/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Važno je zapamtiti da kontekst nije samo jedna stvar. Informacije koje AI agent treba mogu doći iz različitih izvora i na nama je da osiguramo da agent ima pristup tim izvorima:

Vrste konteksta koje AI agent može trebati upravljati uključuju:

• **Upute:** To su poput "pravila" agenta – prompti, sistemske poruke, primjeri s nekoliko pokušaja (pokazuju AI-u kako nešto napraviti) i opisi alata koje može koristiti. Ovo je točka gdje se fokus inženjeringa podataka kombinira s inženjeringom konteksta.

• **Znanje:** Obuhvaća činjenice, informacije iz baza podataka ili dugoročna sjećanja koja je agent prikupio. Uključuje integraciju sustava za dohvat pojačanog generiranja (RAG) ako agent treba pristup različitim spremištima znanja i bazama podataka.

• **Alati:** To su definicije vanjskih funkcija, API-ja i MCP servera koje agent može pozvati, zajedno sa povratnim informacijama (rezultatima) koje dobije korištenjem tih alata.

• **Povijest razgovora:** Tijekom trajanja dijaloga s korisnikom. Kako vrijeme prolazi, ti razgovori postaju duži i složeniji, što zauzima prostor u kontekstnom prozoru.

• **Preferencije korisnika:** Informacije naučene o korisnikovim željama ili nevoljama tijekom vremena. Te se informacije mogu pohraniti i pozvati prilikom donošenja važnih odluka za pomoć korisniku.

## Strategije za učinkovit inženjering konteksta

### Strategije planiranja

[![Najbolje prakse inženjeringa konteksta](../../../translated_images/hr/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Dobro inženjering konteksta počinje dobrim planiranjem. Evo pristupa koji će vam pomoći da počnete razmišljati o tome kako primijeniti koncept inženjeringa konteksta:

1. **Definirajte jasne rezultate** - Rezultati zadataka koje će AI agenti imati trebaju biti jasno definirani. Odgovorite na pitanje – "Kako će svijet izgledati kada AI agent dovrši svoj zadatak?" Drugim riječima, kakvu promjenu, informaciju ili odgovor korisnik treba imati nakon interakcije s AI agentom.
2. **Mapirajte kontekst** - Kad ste definirali rezultate AI agenta, morate odgovoriti na pitanje "Koje informacije AI agent treba da dovrši ovaj zadatak?". Ovako možete započeti mapiranje konteksta gdje te informacije mogu biti locirane.
3. **Stvorite tokove konteksta** - Sada kada znate gdje su informacije, morate odgovoriti na pitanje "Kako će agent doći do tih informacija?". To se može učiniti na različite načine uključujući RAG, korištenje MCP servera i drugih alata.

### Praktične strategije

Planiranje je važno, ali kada informacije počnu ulaziti u kontekstni prozor naših agenata, trebamo imati praktične strategije za upravljanje:

#### Upravljanje kontekstom

Dok će se neke informacije automatski dodavati u kontekstni prozor, inženjering konteksta je o aktivnijem upravljanju tim informacijama što se može učiniti nekoliko strategija:

 1. **Radni blok agenta**
 Omogućava AI agentu da bilježi relevantne informacije o trenutnim zadacima i interakcijama s korisnikom tijekom jedne sesije. Ovo bi trebalo postojati izvan kontekstnog prozora, u datoteci ili objektu u runtimeu kojeg agent može kasnije dohvatiti tijekom ove sesije ako je potrebno.

 2. **Sjećanja**
 Radni blokovi su dobri za upravljanje informacijama izvan kontekstnog prozora jedne sesije. Sjećanja omogućuju agentima pohranu i dohvat relevantnih informacija kroz više sesija. To može uključivati sažetke, preferencije korisnika i povratne informacije za buduća poboljšanja.

 3. **Sažimanje konteksta**
  Kada kontekstni prozor naraste i približava se svom ograničenju, mogu se koristiti tehnike poput sažimanja i rezanja. To uključuje zadržavanje samo najrelevantnijih informacija ili uklanjanje starijih poruka.
  
 4. **Sustavi s više agenata**
  Razvijanje sustava s više agenata je oblik inženjeringa konteksta jer svaki agent ima svoj kontekstni prozor. Kako se taj kontekst dijeli i prenosi na različite agente druga je stvar koju treba isplanirati pri izgradnji takvih sustava.
  
 5. **Sandbox okruženja**
  Ako agent treba pokrenuti neki kod ili obraditi velike količine informacija u dokumentu, to može zahtijevati veliki broj tokena za obradu rezultata. Umjesto da se sve to pohranjuje u kontekstni prozor, agent može koristiti sandbox okruženje koje može pokrenuti taj kod i samo pročitati rezultate i druge relevantne informacije.
  
 6. **Objekti stanja pri izvođenju**
   To se ostvaruje stvaranjem spremnika informacija za upravljanje situacijama kada agent treba imati pristup određenim informacijama. Za složen zadatak, to bi omogućilo agentu da pohranjuje rezultate svakog podzadatka korak po korak, dopuštajući da kontekst ostane povezan samo s tim specifičnim podzadatkom.

#### Inspekcija konteksta

Nakon što primijenite neku od ovih strategija, vrijedi provjeriti što je idući poziv modelu zapravo primio. Korisno pitanje za otklanjanje pogrešaka je:

> Je li agent učitao previše konteksta, pogrešan kontekst ili mu je nedostajao potreban kontekst?

Za odgovor na to pitanje ne morate zapisivati sirove promptove, izlaze alata ili sadržaj memorije. U produkciji preferirajte male zapise inspekcije konteksta koji hvataju brojeve, ID-jeve, hash-ove i oznake politika:

- **Odabir:** Pratite koliko je kandidata za dijelove, alate ili sjećanja razmatrano, koliko je odabrano i koje je pravilo ili rezultat filtriralo ostale.
- **Sažimanje:** Zabilježite opseg izvora ili ID traga, ID sažetka, procijenjeni broj tokena prije i poslije sažimanja i je li sirovi sadržaj isključen iz sljedećeg poziva.
- **Izolacija:** Zabilježite koji je podzadatak pokrenut u zasebnom agentu, sesiji ili sandboxu, koji je sažetak ograničen i je li veliki izlaz alata ostao izvan konteksta glavnog agenta.
- **Memorija i RAG:** Pohranite ID-jeve dokumenata za dohvat, ID-jeve memorije, rezultate, odabrane ID-jeve te status redakcije umjesto cjelokupnog dohvaćenog teksta.
- **Sigurnost i privatnost:** Preferirajte hash-ove, ID-jeve, token bucket-e i oznake politika nad osjetljivim tekstom prompta, argumentima alata, rezultatima alata ili tijelima korisničke memorije.

Cilj nije zadržati više konteksta. Cilj je ostaviti dovoljno dokaza da programer može utvrditi koja je strategija konteksta korištena i je li promijenila sljedeći poziv modelu na željeni način.

### Primjer inženjeringa konteksta

Recimo da želimo AI agentu reći **"Rezerviraj mi putovanje u Pariz."**

• Jednostavan agent koji koristi samo inženjering podataka mogao bi samo odgovoriti: **"U redu, kada biste željeli ići u Pariz?"**. Obradio je samo vaše izravno pitanje u trenutku kada ste ga postavili.

• Agent koji koristi strategije inženjeringa konteksta koje smo pokrili učinio bi mnogo više. Prije nego što odgovori, njegov sustav bi mogao:

  ◦ **Provjeriti vaš kalendar** za dostupne datume (dohvaćanje podataka u stvarnom vremenu).

 ◦ **Prisjetiti se prethodnih putnih preferencija** (iz dugotrajne memorije) poput vaše preferirane zrakoplovne kompanije, budžeta ili preferencije za direktne letove.

 ◦ **Prepoznati dostupne alate** za rezervaciju leta i hotela.

- Potom bi primjer odgovora mogao biti:  "Hej [Vaše ime]! Vidim da ste slobodni prvi tjedan listopada. Da li da tražim direktne letove za Pariz na [preferirana zrakoplovna kompanija] unutar vašeg uobičajenog budžeta od [budžet]?" Ovaj bogatiji, kontekstom vođen odgovor pokazuje snagu inženjeringa konteksta.

## Uobičajene pogreške u kontekstu

### Trovanje konteksta

**Što je to:** Kada halucinacija (lažna informacija koju generira LLM) ili pogreška uđe u kontekst i više puta se referencira, što uzrokuje da agent slijedi nemoguće ciljeve ili razvija besmislene strategije.

**Što učiniti:** Implementirati **provjeru valjanosti konteksta** i **karantin**. Validirati informacije prije nego što se dodaju u dugotrajnu memoriju. Ako se otkrije potencijalno trovanje, započnite nove kontekstne niti kako biste spriječili širenje loših informacija.

**Primjer rezervacije putovanja:** Vaš agent halucinira **direktan let s malog lokalnog aerodroma do udaljenog međunarodnog grada** koji zapravo ne nudi međunarodne letove. Taj nepostojeći detalj leta se sprema u kontekst. Kasnije, kad tražite od agenta da rezervira, on nastavlja pokušavati pronaći karte za ovu nemoguću rutu, što dovodi do ponavljajućih pogrešaka.

**Rješenje:** Implementirati korak koji **provjerava postojanje leta i rutu s API-em u stvarnom vremenu** _prije_ nego se detalj leta doda u radni kontekst agenta. Ako provjera nije uspješna, pogrešna informacija se "karantinira" i ne koristi se dalje.

### Ometanje konteksta

**Što je to:** Kada kontekst postane toliko velik da se model previše fokusira na akumuliranu povijest umjesto na ono što je naučio tijekom treninga, što dovodi do ponavljajućih ili neproduktivnih radnji. Modeli mogu početi pogrešivati čak i prije nego što je kontekstni prozor pun.

**Što učiniti:** Koristiti **sažimanje konteksta**. Povremeno sažimajte akumulirane informacije u kraće sažetke, zadržavajući važne detalje dok uklanjate redundantnu povijest. To pomaže "resetirati" fokus.

**Primjer rezervacije putovanja:** Dugo ste razgovarali o različitim destinacijama za sanjarenje o putovanju, uključujući detaljan opis vašeg putovanja s ruksakom od prije dvije godine. Kada konačno zatražite **"pronađi mi jeftin let za sljedeći mjesec,"** agent se gubi u starim, irelevantnim detaljima i stalno vas pita o opremi za ruksak ili prošlim itinerarima, zanemarujući vaš trenutačni zahtjev.

**Rješenje:** Nakon određenog broja okretaja ili kada kontekst postane prevelik, agent bi trebao **sažeti najnovije i najrelevantnije dijelove razgovora** – fokusirajući se na vaše trenutne putne datume i odredište – i koristiti taj sažeti pregled za sljedeći poziv LLM-u, odbacujući manje relevantan povijesni razgovor.

### Zbunjenost u kontekstu

**Što je to:** Kada nepotreban kontekst, često u obliku previše dostupnih alata, uzrokuje da model generira loše odgovore ili poziva irelevantne alate. Manji modeli su posebno skloni tome.

**Što učiniti:** Implementirati **upravljanje odabirom alata** koristeći RAG tehnike. Pohranite opise alata u vektorsku bazu podataka i odaberite _samo_ najrelevantnije alate za svaki konkretan zadatak. Istraživanja pokazuju da je idealno ograničiti odabir alata na manje od 30.

**Primjer rezervacije putovanja:** Vaš agent ima pristup desecima alata: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` itd. Pitate, **"Koji je najbolji način za kretanje po Parizu?"** Zbog velike količine alata, agent se zbuni i pokuša pozvati `book_flight` _unutar_ Pariza ili `rent_car` iako preferirate javni prijevoz, jer se opisi alata mogu preklapati ili jednostavno ne može razaznati najbolji.

**Rješenje:** Koristiti **RAG nad opisima alata**. Kada pitate o kretanju po Parizu, sustav dinamički dohvaća _samo_ najrelevantnije alate poput `rent_car` ili `public_transport_info` na temelju vašeg upita, prikazujući fokusirani "set" alata LLM-u.

### Sukob u kontekstu

**Što je to:** Kada unutar konteksta postoje proturječne informacije, što vodi do nekonzistentnog rezoniranja ili loših konačnih odgovora. Često se događa kada informacije pristižu u fazama, a rane, netočne pretpostavke ostaju u kontekstu.

**Što učiniti:** Koristiti **rezanje konteksta** i **prekid**. Rezanje znači uklanjanje zastarjelih ili kontradiktornih informacija kako nove detalje dolaze. Prekid daje modelu zaseban radni prostor "radnog bloka" za obradu informacija bez neredanja glavnog konteksta.


**Primjer rezervacije putovanja:** Isprva kažete svom agentu, **"Želim letjeti ekonomskom klasom."** Kasnije u razgovoru promijenite mišljenje i kažete, **"Zapravo, za ovo putovanje idemo poslovnom klasom."** Ako obje upute ostanu u kontekstu, agent bi mogao dobiti kontradiktorne rezultate pretrage ili se zbuniti koju preferenciju treba dati prioritet.

**Rješenje:** Implementirati **pruning konteksta**. Kada nova uputa proturječi starijoj, starija uputa se uklanja ili eksplicitno prepisuje u kontekstu. Alternativno, agent može koristiti **papir za bilješke** kako bi uskladio kontradiktorne preferencije prije donošenja odluke, osiguravajući da samo konačna, dosljedna uputa vodi njegove radnje.

## Imate li još pitanja o inženjeringu konteksta?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) da biste se upoznali s drugim učenicima, sudjelovali na radnim satima i dobili odgovore na pitanja o AI agentima.
## Prethodna lekcija

[Agentic Protocols](../11-agentic-protocols/README.md)

## Sljedeća lekcija

[Memory for AI Agents](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->