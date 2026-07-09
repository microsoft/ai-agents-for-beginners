# Dirbtinio intelekto agentai pradedantiesiems – studijų vadovas

Naudokite šį vadovą kaip praktinį palydovą, kol pereinate kursą. Jis
nėra skirtas pamokų pakeitimui. Jis padeda nuspręsti, nuo ko pradėti, ką
ieškoti kiekvienoje pamokoje ir kaip sujungti idėjas į mažą veikiančio agento
demonstraciją.

Jei čia esate pirmą kartą, pradėkite paprastai:

1. Perskaitykite [Kurso nustatymas](./00-course-setup/README.md).
2. Atlikite pamokas 01–06 iš eilės.
3. Mokymosi metu turėkite omenyje vieną mažą demonstracinę idėją.
4. Po kiekvienos pamokos klauskite: „Ką mano agentas gali daryti dabar, ko
   anksčiau negalėjo?“

## Paprasta demonstracija, kurią verta turėti omenyje

Geras būdas mokytis apie agentus – per visą kursą sekti vieną demonstracinę idėją.

Demonstracijos pavyzdys: **kurso pagalbos agentas**.

Vartotojas klausia:

> „Noriu išmokti, kaip agentai naudoja įrankius. Rask tinkamas pamokas, apibendrink,
> ką pirmiausia turėčiau perskaityti, ir duok trumpą praktinį užduotį.“

Paprastasis pokalbių botas gali atsakyti remdamasis tuo, ką jis jau žino. Agentas gali daugiau:

1. **Skaityti arba ieškoti kurso failuose**, kad surastų tinkamas pamokas.
2. **Naudoti įrankius** pamokų nuorodoms, pavyzdžiams ar papildomai medžiagai gauti.
3. **Planuoti** trumpą mokymosi kelią vietoje vieno ilgo atsakymo.
4. **Naudoti kontekstą** iš dabartinio pokalbio, kad išliktų sutelktas į mokinio tikslą.
5. **Prisiminti naudingas nuostatas**, jei taikymas palaiko atmintį.
6. **Rodyti pėdsakus, citatas ar žurnalus**, kad vartotojas suprastų, kas įvyko.
7. **Taikyti saugiklių priemones** prieš atlikdami rizikingus veiksmus ar naudodami jautrius duomenis.





## Ko siekiate sukurti

Baigę kursą turėtumėte sugebėti paaiškinti ir kurti agentų sistemas,
kurios sujungia šias dalis:

| Dalys | Paprastas paaiškinimas | Demonstracijoje |
|------|-----------------------|---------------|
| Modelis | Samprotavimo variklis, kuris interpretuoja vartotojo užklausą | Supranta, kad mokinys nori pamokų apie įrankių naudojimą |
| Įrankiai | Funkcijos, API, failai, naršyklės ar paslaugos, kuriomis agentas gali naudotis | Ieško saugykloje arba gauna pamokų turinį |
| Žinios | Dokumentai ar duomenys, kuriuos agentas naudoja atsakymo pagrindimui | Kurso README failai ir pamokų medžiaga |
| Kontekstas | Informacija, perduodama kitam modelio kvietimui | Vartotojo tikslas ir įrankių rezultatai |
| Atmintis | Informacija, išsaugota vėlesniam naudojimui | Mokinys teikia pirmenybę praktiniams Python pavyzdžiams |
| Planavimas | Didelio tikslo suskaidymas į mažesnius žingsnius | Surasti pamokas, jas apibendrinti, pasiūlyti praktikumą |
| Orkestracija | Darbo paskirstymas tarp įrankių, žingsnių ar agentų | Planuotojas iškviečia paieškos įrankį, tada santraukų sudarytoją |
| Pasitikėjimas | Saugumas, vertinimas ir stebėjimas | Fiksuoja įrankių iškvietimus ir klausia prieš atliekant reikšmingus veiksmus |

## Modeliai ir teikėjai

Kurso kodo pavyzdžiai naudoja **Microsoft Agent Framework (MAF)** ir taikosi į **Azure OpenAI Responses API** – rekomenduojamą API ateityje, kuri sujungia pokalbių užbaigimus, įrankių iškvietimus, daugiarūšį įvestį ir būsenos išlaikymo pokalbius vienoje API sąsajoje. Jūs jungiatės arba per **Microsoft Foundry** projektą (su `FoundryChatClient`), arba tiesiogiai prie Azure OpenAI (su `OpenAIChatClient`).

Mokydamiesi pamokas, turite kelias teikėjų opcijas:

- **Microsoft Foundry / Azure OpenAI (Responses API)** – pagrindinis kelias, naudojamas per visas pamokas. Prisijunkite su `az login` be raktų, naudojant Entra ID autentifikaciją.
- **Foundry Local** – paleiskite modelius visiškai įrenginyje per OpenAI suderinamą API (be debesies, be API raktų). Idealu naudoti neprisijungus arba be papildomų išlaidų. Žr. [Kurso nustatymas](./00-course-setup/README.md).
- **MiniMax** – OpenAI suderinamas teikėjas su didelės apimties konteksto modeliais, naudojamas kaip be problemų pakeičiantis variantas.

> **Pastaba:** GitHub Models nebepalaikomas (nutraukiamas 2026 m. liepos mėn.) ir nepalaiko Responses API. Pavyzdžiai buvo atnaujinti, kad naudotų Azure OpenAI / Microsoft Foundry.

## Pasirinkite savo mokymosi kelią

Galite pereiti visą kursą iš eilės arba pasirinkti kelią pagal tai, ką norite
sukurti.

| Jei jūsų tikslas yra... | Pradėkite nuo | Tada studijuokite |
|-----------------------|--------------|--------------|
| Suprasti, kas yra agentai | 01, 02, 03 | 04, 05, 06 |
| Sukurti agentą, kuris naudoja įrankius | 04 | 05, 07, 14 |
| Sukurti agentą, pagrįstą RAG | 05 | 04, 06, 12 |
| Kurti kelių žingsnių darbo eigos | 07 | 08, 09, 14 |
| Suprasti daugiagentines sistemas | 08 | 07, 09, 11 |
| Paruošti agentus gamybai | 06, 10 | 12, 13, 18 |
| Ištirti protokolus ir naršyklės automatizavimą | 11, 15 | 10, 18 |

Patarimas: jei esate naujokas agentuose, nepraleiskite pamokų 01-06. Jos suteiks
jums reikalingą žodyną visam likusiam kursui.

## Pamoka po pamokos vadovas

| Pamoka | Ko išmoksite | Išbandykite po pamokos |
|--------|--------------|------------------------|
| [01 – Dirbtinio intelekto agentų įvadas](./01-intro-to-ai-agents/README.md) | Kas agentą skiria nuo paprasto pokalbių boto. | Paaiškinkite savo demonstracijos idėją kaip agentą, o ne tik kaip pokalbių programėlę. |
| [02 – Agentinio karkaso tyrinėjimas](./02-explore-agentic-frameworks/README.md) | Kaip karkasai padeda su modeliais, įrankiais, būsena ir darbo eigomis. | Nustatykite, kurios demonstracijos dalys būtų valdomos karkaso. |
| [03 – Agentinio dizaino šablonai](./03-agentic-design-patterns/README.md) | Dažni šablonai agentų elgesiui kurti. | Nupieškite vartotojo kelionę prieš rašydami kodą. |
| [04 – Įrankių naudojimas](./04-tool-use/README.md) | Kaip agentai iškviečia įrankius duomenims gauti ar veiksmams atlikti. | Apibrėžkite vieną įrankį, kurio reiktų jūsų demonstracijos agentui. |
| [05 – Agentinis RAG](./05-agentic-rag/README.md) | Kaip paieška pagrindžia agentų atsakymus dokumentais ar duomenimis. | Nuspręskite, kokį žinių šaltinį jūsų demonstracija turėtų ieškoti. |
| [06 – Patikimi agentai](./06-building-trustworthy-agents/README.md) | Kaip pridėti saugiklių, priežiūrą ir saugesnį elgesį. | Įtraukite vieną taisyklę, kada agentas turėtų pirmiausia paklausti vartotojo. |
| [07 – Planavimo dizainas](./07-planning-design/README.md) | Kaip agentai suskaido didelius tikslus į mažesnius žingsnius. | Parašykite trijų žingsnių planą savo demonstracijos užklausai. |

| [08 - Daugiagentinis dizainas](./08-multi-agent/README.md) | Kada darbą paskirstyti specializuotiems agentams. | Nuspręskite, ar jūsų demonstracija reikia vieno agento, ar kelių. |
| [09 - Metakognicija](./09-metacognition/README.md) | Kaip agentai gali peržiūrėti ir tobulinti savo rezultatus. | Pridėkite galutinį savikontrolės žingsnį prieš agentui atsakant. |
| [10 - DI agentai gamyboje](./10-ai-agents-production/README.md) | Kas keičiasi, kai agentas pereina iš demonstracijos į gamybą. | Išvardykite, ką stebėtumėte: kokybę, sąnaudas, delsą, gedimus. |
| [11 - Agentiniai protokolai](./11-agentic-protocols/README.md) | Kaip protokolai jungia agentus prie įrankių ir kitų agentų. | Identifikuokite, kur standartinis protokolas galėtų supaprastinti integraciją. |
| [12 - Konteksto inžinerija](./12-context-engineering/README.md) | Kaip pasirinkti, apriboti, izoliuoti ir valdyti kontekstą. | Nuspręskite, kas privalo būti užduotyje ir kas turėtų likti už jo ribų. |
| [13 - Agento atmintis](./13-agent-memory/README.md) | Kaip agentai gali saugoti naudingą informaciją per sąveikas. | Pasirinkite vieną saugią nuostatą, kurią jūsų demonstracija galėtų prisiminti. |
| [14 - Microsoft agentų sistema](./14-microsoft-agent-framework/README.md) | Sistemos specifiniai agentų ir darbo srautų statybiniai blokai, bei LangChain/LangGraph agentų talpinimas Microsoft Foundry. | Susiekite savo demonstracijos žingsnius su sistemos sąvokomis. |
| [15 - Kompiuterio naudojimo agentai](./15-browser-use/README.md) | Kaip agentai gali sąveikauti su naršykle ar vartotojo sąsaja, įskaitant realius pavyzdžius kaip Microsoft Project Opal. | Pasirinkite vieną naršyklės užduotį, kuriai vis dar reikėtų vartotojo patvirtinimo. |
| [18 - DI agentų saugumas](./18-securing-ai-agents/README.md) | Kaip padaryti agentų veiksmus labiau audituojamus ir aptinkamus klastojimui. | Nuspręskite, kokie veiksmai jūsų demonstracijoje turėtų būti įrašomi arba registruojami. |

16 ir 17 pamokos nurodytos pagrindiniame README kaip netrukus pasirodysiančios. Pridėkite jas savo
mokymosi planui, kai turinys taps prieinamas.

## Pagrindinės idėjos pradedantiesiems suprantama kalba

### Įrankiai

Įrankis yra tai, ką agentas gali iškviesti darbui atlikti už modelio ribų. Geras įrankis
turi aiškų pavadinimą, siaurą paskirtį, tipizuotus įvestis, prognozuojamą išvestį ir saugų
nesėkmės būdą.

Demo kursų pagalbai įrankis gali būti:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG ir žinios

RAG padeda agentui atsakyti remiantis šaltinio medžiaga, o ne spėliojant. Šiame
kurse šaltinio medžiaga gali būti pamokų README failai, kodo pavyzdžiai ar išoriniai
ištekliai, susieti su pamokomis.

Naudokite RAG, kai atsakymas turi būti pagrįstas dokumentais, duomenimis arba esamais
projekto failais.

### Planavimas

Planavimas naudingas, kai užklausa apima daugiau nei vieną veiksmą. Laikykite planus trumpus ir
pakankamai matomus, kad kūrėjas arba vartotojas galėtų juos peržiūrėti.

Demo atveju planas gali būti:

1. Surasti pamokas, susijusias su įrankių naudojimu.
2. Apibendrinti aktualiausias pamokas.
3. Pasiūlyti vieną praktikos užduotį.

### Kontextas

Kontextas yra tai, ką modelis mato šiuo metu. Per mažai konteksto gali priversti agentą
praleisti svarbias detales. Per daug konteksto gali sulėtinti agentą, padidinti
sąnaudas arba apsunkinti supratimą.

Gera konteksto inžinerija reiškia tinkamos informacijos pasirinkimą kitam modeliui

skambutis.

### Atmintis

Atmintis yra informacija, išsaugota vėlesniam laikui. Nesaugokite visko. Išsaugokite informaciją
tik tada, kai ji yra naudinga, saugi ir lengvai atnaujinama arba galima ją ištrinti.

Pavyzdžiui, gali būti naudinga prisiminti, kad "mokymosi dalyvis teikia pirmenybę Python pavyzdžiams".
Paprastai jautrių asmeninių duomenų prisiminimas nėra tinkamas.

### Vertinimas ir Observabilumas

Vertinimas klausia: ar agentas padarė teisingą veiksmą?

Observabilumas klausia: ar galime matyti, kaip tai įvyko?

Gamyboje esančių agentų atveju stebėkite modelio skambučius, įrankių skambučius, gautą kontekstą,
delsą, kaštus, klaidas ir vartotojo atsiliepimus.

### Pasitikėjimas ir Saugumas

Pasitikėjimą keliančiam agentui reikia daugiau nei naudingos užklausos. Naudokite minimalias teises turinčius įrankius,
žmogaus patvirtinimą svarbiems veiksmams, duomenų redagavimą, kur reikia, ir veiksmų žurnalus ar
kvitus, kuriuos reikia patikrinti.

## 15 minučių peržiūros rutina

Naudokite šią rutiną po kiekvienos pamokos:

1. **Apibendrinkite pamoką vienu sakiniu.**
2. **Įvardinkite naują agento gebėjimą.** Pavyzdžiui: įrankių naudojimas, paieška,
   planavimas, atmintis, observabilumas arba saugumas.
3. **Pridėkite tai prie kurso pagalbinio demonstravimo.** Ką dabar pakeitė demonstracija?
4. **Nustatykite riziką.** Kas galėtų nutikti, jei šis gebėjimas būtų blogai naudojamas?
5. **Parašykite vieną testavimo klausimą.** Kaip patikrintumėte, ar agentas elgiasi tinkamai?

## Greita savitikra

Prieš tęsiant, pabandykite atsakyti į šiuos klausimus:

1. Ką agentas gali daryti, ko paprastas pokalbių robotas pats negali?
2. Kokių įrankių agentui reikėtų pirmiausia ir kodėl?
3. Kokie žinių šaltiniai turėtų pagrįsti agento atsakymą?
4. Koks kontekstas turėtų būti įtrauktas į kitą modelio skambutį?
5. Ką agentas turėtų prisiminti, ir ko reikėtų vengti saugoti?
6. Kada agentas turėtų prašyti žmogaus patvirtinimo?
7. Kokie žurnalai, sekos ar kvitai padėtų jums vėliau derinti arba audituoti agentą?

## Siūloma baigiamasis pratimas

Kurso pabaigoje sukurkite nedidelį agentą, kuris padėtų mokiniui naršyti šią
saugyklą.

Minimalus variantas:

- Priimti temą iš vartotojo.
- Rasti svarbiausias pamokas.
- Apibendrinti, ką skaityti pirmiausia.
- Pasiūlyti vieną praktinį užduotį.
- Rodyti, kurie pamokų failai ar nuorodos buvo naudojami.

Platus variantas:

- Prisiminėti mokinio pageidaujamą programavimo kalbą.
- Naudoti paprastą planą atsakymo prieš tai.
- Pridėti savitikros žingsnį prieš galutinį atsakymą.
- Žurnaluoti įrankių skambučius ir gautus šaltinius.
- Prašyti patvirtinimo prieš atidarant naršyklę ar UI automatizacijos užduotis.

Tai suteikia mažą, bet realų būdą praktikuoti įrankius, RAG, planavimą,
kontekstą, atmintį, observabilumą ir pasitikėjimą viename projekte.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->