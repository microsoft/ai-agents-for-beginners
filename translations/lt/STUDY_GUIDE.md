# Dirbtinio intelekto agentai pradedantiesiems – studijų vadovas

Naudokite šį vadovą kaip praktinį palydovą, judėdami per kursą. Jis
nėra skirtas pamokų pakeitimui. Jis padeda nuspręsti, nuo ko pradėti, ką
ieškoti kiekvienoje pamokoje ir kaip sujungti idėjas į mažą veikiančio agento
demonstraciją.

Jei čia esate pirmą kartą, pradėkite paprastai:

1. Perskaitykite [kurso sąranką](./00-course-setup/README.md).
2. Baigkite 01–06 pamokas vieną po kitos.
3. Mokydamiesi turėkite omenyje vieną mažą demonstracijos idėją.
4. Po kiekvienos pamokos paklauskite: „Ką mano agentas dabar gali, ko negalėjo
   anksčiau?“

## Paprasta demonstracija, kurią verta turėti omenyje

Geras būdas mokytis apie agentus – viso kurso metu sekti vieną demonstracijos idėją.

Demonstracijos pavyzdys: **kurso pagalbinis agentas**.

Vartotojas klausia:

> „Noriu sužinoti, kaip agentai naudoja įrankius. Rask tinkamas pamokas, apibendrink,
> ką turėčiau perskaityti pirmiausia, ir duok trumpą praktikos užduotį.“

Įprastas pokalbių botas gali atsakyti iš to, ką jau žino. Agentas gali daugiau:

1. **Skaityti arba ieškoti kurso failuose**, kad surastų tinkamas pamokas.
2. **Naudoti įrankius**, kad gautų pamokų nuorodas, pavyzdžius ar papildomą medžiagą.
3. **Planuoti** trumpą mokymosi kelią, o ne duoti vieną ilgą atsakymą.
4. **Naudoti kontekstą** iš dabartinės pokalbio dalies, kad liktų susitelkęs į mokinio
   tikslą.
5. **Prisiminti naudingas nuostatas**, jei programa palaiko atmintį.
6. **Rodyti sekas, citatas ar žurnalus**, kad vartotojas suprastų, kas įvyko.
7. **Taikyti saugumo priemones** prieš imantis rizikingų veiksmų ar naudojant jautrius duomenis.

Mokydamiesi kiekvienos pamokos, grįžkite prie šios demonstracijos ir klauskite: kokią naują funkciją
ši pamoka pridėtų?

## Link ko siekiate

Kurso pabaigoje turėtumėte sugebėti paaiškinti ir sukurti agentų sistemas,
apimančias šias dalis:

| Dalys | Kas reiškia paprastai | Demonstracijoje |
|-------|----------------------|---------------|
| Modelis | Loginis variklis, interpretuojantis vartotojo užklausą | Supranta, kad mokinys nori pamokų apie įrankių naudojimą |
| Įrankiai | Funkcijos, API, failai, naršyklės ar paslaugos, kurias agentas gali naudoti | Ieško repo arba gauna pamokų turinį |
| Žinios | Dokumentai ar duomenys, kuriais grindžiamas atsakymas | Kurso README failai ir pamokų medžiaga |
| Kontekstas | Informacija, įtraukta į kitą modelio užklausą | Vartotojo tikslas ir įrankių rezultatai |
| Atmintis | Informacija, išsaugota vėlesniam naudojimui | Mokinys renkasi praktinius Python pavyzdžius |
| Planavimas | Didelio tikslo skaidymas į mažesnius žingsnius | Rasti pamokas, jas apibendrinti, pasiūlyti praktiką |
| Orkestracija | Darbo paskirstymas tarp įrankių, žingsnių ar agentų | Planavimo modulis iškviečia paieškos įrankį, po to santrauką sudarantį įrankį |
| Pasitikėjimas | Saugumas, apsauga, vertinimas ir stebėsena | Įrašo įrankių kvietimus ir klausia prieš svarbius veiksmus |

## Modeliai ir tiekėjai

Kodo pavyzdžiai kurse naudoja **Microsoft Agent Framework (MAF)** ir taiko **Azure OpenAI Responses API** — rekomenduojamą API ateičiai, apjungiantią pokalbių užbaigimą, įrankių iškvietimą, multimodalinį įvestį ir būsenos palaikymą vienoje API sąsajoje. Jūs jungiatės per **Microsoft Foundry** projektą (naudojant `FoundryChatClient`) arba tiesiogiai prie Azure OpenAI (naudojant `OpenAIChatClient`).


Dirbdami su pamokomis, turite keletą paslaugų teikėjo pasirinkimų:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — pagrindinis kelias, naudojamas per visas pamokas. Prisijunkite su `az login` be raktų su Entra ID autentifikacija.
- **Foundry vietinis** — modelius galite vykdyti visiškai vietoje per OpenAI suderinamą API (be debesies, be API raktų). Idealu bandymams be interneto ar nemokamai. Žr. [Kurso parengimą](./00-course-setup/README.md).
- **MiniMax** — OpenAI suderinamas tiekėjas su didelio konteksto modeliais, naudojamas kaip alternatyva.

> **Pastaba:** GitHub modeliai yra pasenę (nutraukiami 2026 m. liepos mėn.) ir nepalaiko Responses API. Pavyzdžiai buvo atnaujinti naudoti Azure OpenAI / Microsoft Foundry.

## Pasirinkite savo mokymosi kelią

Galite eiti per pilną kursą iš eilės arba pereiti prie kelio pagal tai, ką norite
sukurti.

| Jei jūsų tikslas yra... | Pradėkite nuo | Tada nagrinėkite |
|-----------------------|--------------|--------------|
| Suprasti, kas yra agentai | 01, 02, 03 | 04, 05, 06 |
| Sukurti agentą, kuris naudoja įrankius | 04 | 05, 07, 14 |
| Sukurti RAG pagrindu veikiantį agentą | 05 | 04, 06, 12 |
| Kurti kelių žingsnių darbo eigas | 07 | 08, 09, 14 |
| Suprasti daugiaagentines sistemas | 08 | 07, 09, 11 |
| Paruošti agentus gamybai | 06, 10 | 12, 13, 16, 18 |
| Diegti ir skalauti agentus Foundry aplinkoje | 10, 16 | 06, 13, 18 |
| Kurti vietinius / pirmiausia neveikiančius su internetu agentus | 17 | 04, 05, 11 |
| Tirti protokolus ir naršyklės automatizavimą | 11, 15 | 10, 18 |

Patarimas: jei esate naujokas agentų srityje, nepraleiskite pamokų 01-06. Jose įgysite
žodyną, kurio prireiks likusiam kursui.

## Pamoka po pamokos vadovas

| Pamoka | Ką sužinote | Išbandykite po pamokos |
|--------|-------------|-----------------------|
| [01 - Įvadas į AI agentus](./01-intro-to-ai-agents/README.md) | Kas skiria agentą nuo paprasto pokalbių roboto. | Paaiškinkite savo demonstracinę idėją kaip agentą, ne tik kaip pokalbių programą. |
| [02 - Agentiniai karkasai](./02-explore-agentic-frameworks/README.md) | Kaip karkasai padeda su modeliais, įrankiais, būsena ir darbo eiga. | Nustatykite, kurios jūsų demonstracijos dalys būtų valdomos karkaso. |
| [03 - Agentų dizaino šablonai](./03-agentic-design-patterns/README.md) | Įprasti šablonai agentų elgesiui kurti. | Nubrėžkite naudotojo kelionę prieš rašydami kodą. |
| [04 - Įrankių naudojimas](./04-tool-use/README.md) | Kaip agentai kreipiasi į įrankius, kad gautų duomenis ar imtųsi veiksmų. | Apibrėžkite vieną įrankį, kurio reikėtų jūsų demonstracijos agentui. |
| [05 - Agentinis RAG](./05-agentic-rag/README.md) | Kaip paieška pagrindžia agentų atsakymus dokumentais ar duomenimis. | Nuspręskite, kokio žinių šaltinio turėtų ieškoti jūsų demonstracija. |

| [06 - Patikimi agentai](./06-building-trustworthy-agents/README.md) | Kaip pridėti apsaugas, priežiūrą ir saugesnį elgesį. | Pridėkite vieną taisyklę, kada agentas turėtų pirmiausia paklausti naudotojo. |
| [07 - Planavimo dizainas](./07-planning-design/README.md) | Kaip agentai padalina didesnius tikslus į mažesnius veiksmus. | Parašykite trijų žingsnių planą savo demonstraciniam užklausai. |
| [08 - Daugagentinis dizainas](./08-multi-agent/README.md) | Kada paskirstyti darbą specializuotiems agentams. | Nuspręskite, ar jūsų demonstracijai reikia vieno agente, ar kelių. |
| [09 - Metakognicija](./09-metacognition/README.md) | Kaip agentai gali peržiūrėti ir pagerinti savo rezultatus. | Pridėkite galutinę savikontrolę prieš agentui atsakant. |
| [10 - AI agentai produkcijoje](./10-ai-agents-production/README.md) | Kas keičiasi, kai agentas pereina nuo demonstracijos prie produkcijos. | Išvardinkite, ką stebėtumėte: kokybę, kainą, delsą, gedimus. |
| [11 - Agentiniai protokolai](./11-agentic-protocols/README.md) | Kaip protokolai jungia agentus prie įrankių ir kitų agentų. | Nustatykite, kur standartinis protokolas galėtų supaprastinti integraciją. |
| [12 - Konteksto inžinerija](./12-context-engineering/README.md) | Kaip pasirinkti, apkarpyti, atskirti ir valdyti kontekstą. | Nuspręskite, kas turi būti užklausoje ir kas turėtų likti už jos ribų. |
| [13 - Agentų atmintis](./13-agent-memory/README.md) | Kaip agentai gali saugoti naudingą informaciją per sąveikas. | Pasirinkite vieną saugią nuostatą, kurią jūsų demonstracija galėtų įsiminti. |
| [14 - Microsoft agentų karkasas](./14-microsoft-agent-framework/README.md) | Karkaso specifinės agentų ir darbo srautų sudedamosios dalys bei LangChain/LangGraph agentų priegloba Microsoft Foundry aplinkoje. | Susiekite savo demonstracijos žingsnius su karkaso koncepcijomis. |
| [15 - Kompiuterio naudojimo agentai](./15-browser-use/README.md) | Kaip agentai gali sąveikauti su naršyklės ar vartotojo sąsajos paviršiais, pateikiant realius pavyzdžius kaip Microsoft Project Opal. | Pasirinkite vieną naršyklės užduotį, kuri vis dar turėtų reikalauti naudotojo patvirtinimo. |
| [16 - Skalinių agentų diegimas](./16-deploying-scalable-agents/README.md) | Kaip perkelti agentą nuo prototipo prie skirtos, stebimos gamybinės diegimo Microsoft Foundry aplinkoje (priglobti agentai, modelių maršrutizavimas, kešavimas, vertinimo varteliai, dūmų testai). | Išvardinkite gamybinio naudojimo klausimus, kuriuos jūsų demonstracija dar turi spręsti: talpinimas, maršrutizavimas, kaina, vertinimas. |
| [17 - Vietinių AI agentų kūrimas](./17-creating-local-ai-agents/README.md) | Kaip kurti vietinius agentus, kurie veikia visiškai jūsų mašinoje naudojant Foundry Local ir Qwen (vietiniai įrankiai, vietinis RAG, vietinis MCP). | Nuspręskite, kurios jūsų demonstracijos dalys turėtų likti privatumai ir veikti vietoje. |
| [18 - AI agentų saugumo užtikrinimas](./18-securing-ai-agents/README.md) | Kaip padaryti agentų veiksmus patikimesnius audito ir pažeidžiamumo požiūriu. | Nuspręskite, kurie veiksmai jūsų demonstracijoje turėtų būti registruojami arba patvirtinami. |

## Diegtų agentų patikra naudojant dūmų testus

Kai jūs diegiate agentą (16 pamoka), **dūmų testas** yra pigiausias pirmasis
patikrinimas, kuris faktiškai įvertina diegimą. Ši saugykla teikia paruoštus
katalogus po [tests/](./tests/README.md) skiriamus agentams iš pamokų
01, 04, 05 ir 16, susietiems su

[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
veiksmas. Vykdykite juos skirtuke **Actions** po to, kai įdiegiate pamokos agentą.
Dūmų testai yra pirmasis filtras – neprisijungęs ir prisijungęs vertinimas (10 ir 16 pamokos)
parodo, koks *geras* agentas yra.

## Pagrindinės idėjos pradedančiajam patrauklia kalba

### Įrankiai

Įrankis yra tai, ką agentas gali iškviesti, kad atliktų darbą už modelio ribų. Geras įrankis
turi aiškų pavadinimą, siaurą funkciją, tipizuotus įvesties duomenis, prognozuojamą rezultatą ir saugų būdą
sugriūti.

Kursų pagalbos demonstracijoje įrankis galėtų būti:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG ir žinios

RAG padeda agentui atsakyti remiantis šaltiniais, o ne spėlioti. Šiame
kurse šaltinio medžiaga gali būti pamokų README failai, kodo pavyzdžiai arba išorinės
medžiagos, susietos su pamokomis.

Naudokite RAG, kai atsakymas turėtų būti pagrįstas dokumentais, duomenimis ar esamais
projekto failais.

### Planavimas

Planavimas naudingas, kai užklausa turi daugiau nei vieną žingsnį. Laikykite planus trumpus ir
pakankamai matomus, kad programuotojas ar vartotojas galėtų juos peržiūrėti.

Demonstracijoje planas galėtų būti:

1. Rasti pamokas, susijusias su įrankių naudojimu.
2. Apibendrinti labiausiai aktualias pamokas.
3. Rekomenduoti vieną praktikos užduotį.

### Kontekstas

Kontekstas yra tai, ką modelis mato dabar. Per mažai konteksto gali privesti agentą
praleisti svarbias detales. Per daug konteksto gali padaryti agentą lėtesnį, brangesnį
arba lengviau suklaidinti.

Geras konteksto valdymas reiškia tinkamos informacijos pasirinkimą kitam modelio
kvietimui.

### Atmintis

Atmintis yra informacija, išsaugota vėlesniam laikui. Nesuaukite visko. Išsaugokite informaciją
tik kai ji naudinga, saugi ir lengvai atnaujinama ar pašalinama.

Pavyzdžiui, prisiminti „mokymosi metu pirmenybę teikia Python pavyzdžiams“ gali būti naudinga.
Prisiminimas jautrios asmeninės informacijos dažniausiai nėra.

### Vertinimas ir stebimas veikimas

Vertinimas klausia: ar agentas atliko teisingą veiksmą?

Stebimas veikimas klausia: ar galime pamatyti, kaip tai įvyko?

Realaus naudojimo agentams sekti modelio kvietimus, įrankių iškvietimus, gautą kontekstą,
vėlavimą, kainą, klaidas ir vartotojų atsiliepimus.

### Pasitikėjimas ir saugumas

Patikimi agentai reikia daugiau nei naudingos užklausos. Naudokite minimalias privilegijas turinčius įrankius,
žmogaus patvirtinimą svarbiems veiksmams, duomenų slėpimą, kur reikia, ir žurnalus arba
kvitus veiksmams, kuriuos reikia auditui.

## 15 minučių apžvalgos rutina

Naudokite šią rutiną po kiekvienos pamokos:

1. **Apibendrinkite pamoką vienu sakiniu.**
2. **Įvardinkite naują agento gebėjimą.** Pavyzdžiui: įrankių naudojimas, paieška,
   planavimas, atmintis, stebimas veikimas arba saugumas.
3. **Pridėkite jį prie kursų pagalbos demonstracijos.** Kas dabar pasikeitė demonstracijoje?
4. **Nustatykite riziką.** Kas gali nutikti, jei šis gebėjimas bus piktnaudžiaujamas?
5. **Parašykite vieną klausimą testui.** Kaip patikrintumėte, ar agentas elgiasi teisingai?

## Greita savitikra

Prieš tęsdami, pabandykite atsakyti į šiuos klausimus:

1. Ką gali agentas, ko pats paprastas pokalbių robotas negali?
2. Koks įrankis būtų pirmas, kurio agentui reikėtų, ir kodėl?
3. Koks žinių šaltinis turėtų pagrįsti agento atsakymą?
4. Koks kontekstas turėtų būti įtrauktas į kitą modelio kvietimą?

5. Ką agentas turėtų prisiminti, o ko vengti saugoti?
6. Kada agentas turėtų paprašyti žmogaus patvirtinimo?
7. Kokie žurnalai, pėdsakai ar kvitai padėtų jums vėliau išanalizuoti arba patikrinti agentą?


## Siūlomas baigiamasis pratimas

Kurso pabaigoje sukurkite mažą agentą, kuris padėtų mokiniui naršyti šiame
saugykloje.

Minimali versija:

- Priimti temą iš vartotojo.
- Rasti aktualiausias pamokas.
- Apibendrinti, ką skaityti pirmiausia.
- Pasiūlyti vieną praktinį užduotį.
- Rodyti, kurios pamokų bylos ar nuorodos buvo naudotos.

Išplėstinė versija:

- Atsiminti mokinio pageidaujamą programavimo kalbą.
- Naudoti paprastą planą prieš atsakant.
- Pridėti savitikros žingsnį prieš galutinį atsakymą.
- Fiksuoti įrankių kvietimus ir gautus šaltinius.
- Prašyti patvirtinimo prieš atidarant naršyklę ar UI automatizacijos užduotis.

Tai suteikia nedidelį, bet realistišką būdą praktikuoti įrankius, RAG, planavimą,
kontekstą, atmintį, stebėseną ir pasitikėjimą viename projekte.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->