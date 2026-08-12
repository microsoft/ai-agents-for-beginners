# Konteksto Inžinerija DI Agentams

[![Konteksto Inžinerija](../../../translated_images/lt/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Spustelėkite aukščiau esantį paveikslėlį, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

Svarbu suprasti programos, kuriai kuriate DI agentą, sudėtingumą, norint sukurti patikimą agentą. Turime kurti DI agentus, kurie efektyviai valdo informaciją, kad spręstų sudėtingus poreikius, viršijančius tik promptų inžineriją.

Šioje pamokoje pažvelgsime, kas yra konteksto inžinerija ir kokį vaidmenį ji atlieka kuriant DI agentus.

## Įvadas

Šioje pamokoje aptarsime:

• **Kas yra konteksto inžinerija** ir kodėl ji skiriasi nuo promptų inžinerijos.

• **Efektyvios konteksto inžinerijos strategijas**, įskaitant, kaip rašyti, pasirinkti, suspausti ir izoliuoti informaciją.

• **Dažnas konteksto klaidas**, kurios gali sugadinti DI agentą, ir kaip jas ištaisyti.

## Mokymosi Tikslai

Baigę šią pamoką suprasite, kaip:

• **Apibrėžti konteksto inžineriją** ir atskirti ją nuo promptų inžinerijos.

• **Nustatyti pagrindinius konteksto komponentus** Didelių Kalbinių Modelių (LLM) programose.

• **Taikyti strategijas rašant, pasirenkant, suspaudžiant ir izoliuojant kontekstą**, kad pagerintumėte agento veikimą.

• **Atpažinti dažnas konteksto klaidas**, tokias kaip užterštumas, atitraukimas, painiava ir konfliktas, bei įgyvendinti jų šalinimo metodus.

## Kas yra konteksto inžinerija?

DI agentams kontekstas yra tai, kas lemia agento planavimą imtis tam tikrų veiksmų. Konteksto inžinerija - tai praktika užtikrinti, kad DI agentas turėtų tinkamą informaciją kitam užduoties žingsniui atlikti. Konteksto langas yra riboto dydžio, todėl kaip agentų kūrėjai turime kurti sistemas ir procesus, skirtus valdyti informacijos įtraukimą, pašalinimą ir suspaudimą konteksto lange.

### Promptų inžinerija vs konteksto inžinerija

Promptų inžinerija orientuota į vieną statinių nurodymų rinkinį, kuris efektyviai nukreipia DI agentus naudodamas taisyklių rinkinį. Konteksto inžinerija - tai dinamiškos informacijos valdymas, įskaitant pradinį promptą, siekiant užtikrinti, kad DI agentas turėtų reikiamą informaciją laikui bėgant. Pagrindinė konteksto inžinerijos mintis yra padaryti šį procesą pakartojamą ir patikimą.

### Konteksto tipai

[![Konteksto tipai](../../../translated_images/lt/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Svarbu prisiminti, kad kontekstas nėra vienas dalykas. Informacija, kurios DI agentui reikia, gali kilti iš įvairių šaltinių, ir nuo mūsų priklauso užtikrinti, kad agentas turėtų prieigą prie šių šaltinių:

DI agentui gali reikėti valdyti šiuos konteksto tipus:

• **Nurodymai:** Tai tarsi agento "taisyklių" rinkinys – promptai, sistemos pranešimai, kelių pavyzdžių rodymas (kaip DI daryti kažką) ir įrankių aprašymai, kuriuos agentas gali naudoti. Čia promptų inžinerija susilieja su konteksto inžinerija.

• **Žinios:** Tai faktai, informacija gauta iš duomenų bazių arba ilgalaikių prisiminimų, kuriuos agentas sukaupė. Tai apima ir Retrieval Augmented Generation (RAG) sistemos integravimą, jei agentui reikia prieigos prie skirtingų žinių kaupiklių ar duomenų bazių.

• **Įrankiai:** Tai apibrėžimai išorinių funkcijų, API ir MCP serverių, kuriuos agentas gali iškviesti, kartu su rezultatais, gautais juos naudojant.

• **Pokalbių Istorija:** Nuolatinis dialogas su vartotoju. Laikui bėgant šie pokalbiai ilgėja ir komplikuojasi, todėl užima vietos konteksto lange.

• **Vartotojo pageidavimai:** Informacija apie vartotojo pomėgius ar nepatinkančius dalykus, sužinoma laikui bėgant. Ši informacija gali būti saugoma ir naudojama priimant svarbius sprendimus, siekiant padėti vartotojui.

## Efektyvios konteksto inžinerijos strategijos

### Planavimo strategijos

[![Konteksto inžinerijos gerosios praktikos](../../../translated_images/lt/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Gera konteksto inžinerija prasideda nuo gero planavimo. Štai požiūris, kuris padės pradėti mąstyti, kaip taikyti konteksto inžinerijos koncepciją:

1. **Aiškiai apibrėžti rezultatus** – Užduočių, kurias atliks DI agentai, rezultatai turi būti aiškiai apibrėžti. Atsakykite į klausimą – „Kaip atrodys pasaulis, kai DI agentas baigs savo užduotį?“ Kitaip tariant, kokį pokytį, informaciją ar atsakymą vartotojas turėtų gauti po sąveikos su DI agentu.
2. **Žemėlapiuoti kontekstą** – Kai apibrėžiate DI agento rezultatus, turite atsakyti į klausimą „Kokią informaciją DI agentas turi turėti, kad įvykdytų šią užduotį?“. Taip galite pradėti žemėlapiuoti, kur ta informacija gali būti randama.
3. **Kurti konteksto srautus** – Dabar, kai žinote, kur yra informacija, turite atsakyti į klausimą „Kaip agentas gaus šią informaciją?“. Tai galima atlikti įvairiais būdais, įskaitant RAG, MCP serverių ir kitų įrankių naudojimą.

### Praktinės strategijos

Planavimas svarbus, tačiau kai informacija pradeda tekėti į agento konteksto langą, turime turėti praktinių strategijų ją valdyti:

#### Konteksto valdymas

Nors dalis informacijos į konteksto langą bus dedama automatiškai, konteksto inžinerija reiškia aktyvesnį požiūrį į šią informaciją, ką galima pasiekti keliais būdais:

 1. **Agentų užrašų knygelė**
 Tai leidžia DI agentui fiksuoti svarbią informaciją apie esamas užduotis ir vartotojo sąveikas per vieną sesiją. Ši informacija turėtų būti saugoma už konteksto lango ribų, pavyzdžiui, faile arba vykdymo objekte, kurį agentas vėliau gali pasiekti šios sesijos metu, jei reikės.

 2. **Prisiminimai**
 Užrašų knygelės tinka valdyti informaciją už vienos sesijos konteksto lango ribų. Prisiminimai leidžia agentams saugoti ir gauti svarbią informaciją per kelias sesijas. Tai gali apimti santraukas, vartotojo pageidavimus ir atsiliepimus dėl tobulinimų ateityje.

 3. **Konteksto suspaudimas**
  Kai konteksto langas didėja ir artėja prie ribos, galima taikyti tokias technikas kaip santraukų sudarymas ir trynimas. Tai apima arba tik svarbiausios informacijos išlaikymą, arba senesnių pranešimų pašalinimą.
  
 4. **Daugiagentinės sistemos**
  Daugiagentinės sistemos kūrimas yra konteksto inžinerijos forma, nes kiekvienas agentas turi savo konteksto langą. Kaip šis kontekstas dalijamasi ir perduodamas įvairiems agentams – tai dar viena planavimo dalis kuriant šias sistemas.
  
 5. **Sandbox aplinkos**
  Jei agentui reikia vykdyti tam tikrą kodą arba apdoroti didelius informacijos kiekius dokumente, tai gali užimti daug tokenų rezultatams apdoroti. Užuot visa tai saugojus konteksto lange, agentas gali naudoti sandbox aplinką, kurioje galima vykdyti kodą ir tik perskaityti rezultatus bei kitą svarbią informaciją.
  
 6. **Vykdymo laikotarpio būsenos objektai**
   Tai vykdoma kuriant informacijos konteinerius, kad būtų valdomos situacijos, kai agentui reikia prieigos prie tam tikros informacijos. Sudėtingai užduočiai tai leistų agentui rezultatų saugojimą žingsnis po žingsnio, leidžiant kontekstui ateiti tik prie konkrečios užduoties dalies.

#### Konteksto tikrinimas

Pritaikius vieną iš šių strategijų verta patikrinti, ką iš tiesų gavo kitas modelio kvietimas. Naudingas derinimo klausimas yra:

> Ar agentas užkrautų per daug konteksto, netinkamą kontekstą ar praleistą reikalingą kontekstą?

Kad atsakytumėte į šį klausimą, nereikia registruoti žalių promptų, įrankių išvesties ar atminties turinio. Produkcijoje rekomenduojama naudoti mažus konteksto patikrinimo įrašus, apimančius kiekius, ID, hašus ir politikos etiketes:

- **Pasirinkimas:** Sekite, kiek kandidatų dalių, įrankių ar atminties buvo svarstyta, kiek iš jų buvo pasirinkta ir kuri taisyklė ar balas lėmė kitų filtravimą.
- **Suspaudimas:** Užfiksuokite šaltinio diapazoną arba sekos ID, santraukos ID, įvertintą tokenų skaičių prieš ir po suspaudimo, bei ar žali turinys buvo pašalintas iš kito kvietimo.
- **Izoliacija:** Užfiksuokite, kuri įmenama užduotis vyko atskirame agento, sesijos ar sandbox aplinkoje, kokia ribojanti santrauka buvo grąžinta, ir ar didelė įrankio išvestis liko už pagrindinio agento konteksto ribų.
- **Atmintis ir RAG:** Saugo retrieval dokumentų ID, atminties ID, balus, pasirinktus ID ir redagavimo statusą vietoje viso gauto teksto.
- **Saugumas ir privatumas:** Rinkitės hašus, ID, tokenų skaičių ir politikos etiketes vietoje jautrių promptų tekstų, įrankių argumentų, jų rezultatų ar vartotojo atminties turinio.

Tikslas nėra saugoti daugiau konteksto. Tikslas – palikti pakankamai įrodymų, kad kūrėjas galėtų pasakyti, kokia konteksto strategija buvo vykdoma ir ar ji pakeitė kitą modelio kvietimą numatytu būdu.

### Konteksto inžinerijos pavyzdys

Tarkime, norime, kad DI agentas **„užsakyčiau kelionę į Paryžių.“**

• Paprastas agentas, naudojantis tik promptų inžineriją, gali atsakyti: **„Gerai, kada norėtumėte vykti į Paryžių?“** Jis apdorojęs tik jūsų tiesioginį klausimą tuo momentu, kai vartotojas uždavė.

• Agentas, taikantis aptartas konteksto inžinerijos strategijas, padarytų daug daugiau. Net neatsakęs, jo sistema galėtų:

  ◦ **Patikrinti jūsų kalendorių** dėl laisvų datų (gaunant realaus laiko duomenis).

 ◦ **Prisiminimų ištraukimą** apie ankstesnius kelionių pageidavimus (iš ilgalaikės atminties), pavyzdžiui, pageidaujamą oro liniją, biudžetą ar tiesioginius skrydžius.

 ◦ **Galimų įrankių** nustatymą, skirtą skrydžių ir viešbučių užsakymui.

- Tada pavyzdinis atsakymas galėtų būti: „Sveikas, [Jūsų Vardas]! Matau, kad esate laisvas spalio pirmąją savaitę. Ar ieškoti tiesioginių skrydžių į Paryžių su [Pageidaujama oro linija] jūsų įprastame biudžete [Biudžetas]?“. Šis turiningas, kontekstą atsižvelgiantis atsakymas iliustruoja konteksto inžinerijos galią.

## Dažnos konteksto klaidos

### Konteksto užterštumas

**Kas tai yra:** Kai LLM sukurta haliucinacija (klaidinga informacija) arba klaida patenka į kontekstą ir yra nuolat cituojama, dėl ko agentas siekia neįmanomų tikslų arba kuria nesąmoningas strategijas.

**Ką daryti:** Įgyvendinti **konteksto validaciją** ir **karantiną**. Patikrinti informaciją prieš ją pridedant prie ilgalaikės atminties. Jei įtariamas užterštumas, pradėti naujus švarius konteksto srautus, kad bloga informacija nesiplėstų.

**Kelionių užsakymo pavyzdys:** Jūsų agentas sukuria haliucinaciją apie **tiesioginį skrydį iš mažo vietinio oro uosto į tolimą tarptautinį miestą**, kurio iš tiesų nėra. Ši neegzistuojanti skrydžio detalė įrašoma į kontekstą. Vėliau, kai prašote agento užsakyti bilietą, jis nuolat bando rasti bilietus šiam neįmanomam maršrutui, sukeldamas pasikartojančias klaidas.

**Sprendimas:** Prieš pridedant skrydžio detalę į agento darbo kontekstą, įvykdyti žingsnį, kuris **valiuduoja skrydžio egzistavimą ir maršrutus su realaus laiko API**. Jei validacija nepavyksta, klaidinga informacija yra „karantinuojama“ ir toliau nenaudojama.

### Konteksto atitraukimas

**Kas tai yra:** Kai kontekstas tampa per didelis, modelis pernelyg daug dėmesio skiria sukauptai istorijai, o ne mokymosi laikotarpiu išmoktam žinių naudojimui, dėl ko pasikartoja nereikalingi ar beprasmiški veiksmai. Modeliai gali pradėti klysti dar prieš pasiekiant konteksto lango ribą.

**Ką daryti:** Naudoti **konteksto santrauką**. Periodiškai suspausti sukauptą informaciją į trumpesnes santraukas, išlaikant svarbiausias detales ir pašalinant pasikartojančią istoriją. Tai padeda „atstatyti“ dėmesį.

**Kelionių užsakymo pavyzdys:** Jūs ilgai kalbėjote apie svajonių kelionių vietas, įskaitant išsamų jūsų kuprinės kelionės prieš dvejus metus pasakojimą. Kai galiausiai klausi: **„rask man pigius skrydžius kitam mėnesiui“**, agentas įstringa senose, nereikšmingose detalėse ir nuolat klausia apie jūsų kuprinės įrangą ar ankstesnius maršrutus, nekreipdamas dėmesio į dabartinį prašymą.

**Sprendimas:** Po tam tikro užduočių skaičiaus arba kai kontekstas tampa per didelis, agentas turėtų **apibendrinti naujausias ir svarbiausias pokalbio dalis** – koncentruodamasis į jūsų dabartines kelionės datas ir tikslą – ir naudoti tą suspaustą santrauką kitam LLM kvietimui, atsisakydamas mažiau svarbios istorinės diskusijos.

### Konteksto painiava

**Kas tai yra:** Kai nereikalingas kontekstas, dažnai per daug prieinamų įrankių forma, verčia modelį gaminti netinkamus atsakymus arba kviesti netinkamus įrankius. Mažesni modeliai ypač linkę į tai.

**Ką daryti:** Įgyvendinti **įrankių komplekto valdymą** naudojant RAG metodus. Aprašymus apie įrankius saugoti vektorinėje duomenų bazėje ir rinktis _tiktai_ svarbiausius įrankius konkrečiai užduočiai. Tyrimai rodo, kad verta riboti įrankių pasirinkimą iki mažiau nei 30.

**Kelionių užsakymo pavyzdys:** Jūsų agentas turi prieigą prie dešimčių įrankių: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` ir kt. Jūs klausiate, **„Koks geriausias būdas judėti Paryžiuje?“** Dėl daugumos įrankių agentas supainioja ir bando išsinuomoti automobilį miesto viduje, nors jūs rinkotės viešąjį transportą, arba kviečia skrendimą Paryžiaus viduje, nes įrankių aprašymai gali dublikuotis arba jis tiesiog negali apsispręsti, kuris geriausias.

**Sprendimas:** Naudoti **RAG įrankių aprašymams**. Kai klausiate apie judėjimą Paryžiuje, sistema dinamiškai parenka _tiktai_ svarbiausius įrankius, tokius kaip `rent_car` arba `public_transport_info`, pristatydama LLM fokusuotą įrankių rinkinį.

### Konteksto konfliktas

**Kas tai yra:** Kai kontekste egzistuoja prieštaringa informacija, sukelianti prieštaringą mąstymą ar blogus galutinius atsakymus. Dažnai taip nutinka, kai informacija ateina etapais, o ankstesnės klaidingos prielaidos lieka kontekste.

**Ką daryti:** Naudoti **konteksto apkarpymą** ir **perkėlimą**. Apkarpymas reiškia pasenusių ar prieštaringų duomenų pašalinimą atvykstant naujiems duomenims. Perkėlimas suteikia modeliui atskirą „užrašų knygelės“ erdvę informacijai apdoroti, nekliudant pagrindiniam kontekstui.


**Kelionės užsakymo pavyzdys:** Iš pradžių sakote savo agentui, **„Noriu skristi ekonomine klase.“** Vėliau pokalbio metu savo nuomonę pakeičiate ir sakote, **„Iš tiesų, šiai kelionei pasirinkime verslo klasę.“** Jei abi instrukcijos išlieka kontekste, agentas gali gauti prieštaringus paieškos rezultatus arba susipainioti, kurią nuostatą teikti pirmenybę.

**Sprendimas:** Įgyvendinkite **konteksto apkarpymą**. Kai nauja instrukcija prieštarauja senajai, senoji instrukcija pašalinama arba aiškiai panaikinama kontekste. Alternatyviai agentas gali naudoti **užrašų knygelę** (scratchpad), kad suderintų prieštaringas nuostatas prieš priimdamas sprendimą, užtikrindamas, kad tik galutinė, nuosekli instrukcija nurodytų jo veiksmus.

## Ar turite daugiau klausimų apie konteksto inžineriją?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kad susitiktumėte su kitais besimokančiais, dalyvautumėte darbo valandose ir gautumėte atsakymus į savo AI agentų klausimus.
## Ankstesnė pamoka

[Agentų protokolai](../11-agentic-protocols/README.md)

## Kita pamoka

[Atmintis AI agentams](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->