# Atmintis AI agentams  
[![Agent Memory](../../../translated_images/lt/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kalbant apie unikalius AI agentų kūrimo privalumus, dažniausiai aptariami du dalykai: galimybė naudotis įrankiais užduotims atlikti ir gebėjimas tobulėti laikui bėgant. Atmintis yra savęs tobulinančio agento kūrimo pagrindas, leidžiantis kurti geresnę patirtį mūsų naudotojams.

Šioje pamokoje apžvelgsime, kas yra atmintis AI agentams, kaip ją valdyti ir naudoti mūsų programų naudai.

## Įvadas

Ši pamoka apims:

• **AI agentų atminties supratimą**: Kas yra atmintis ir kodėl ji svarbi agentams.

• **Atminties įgyvendinimą ir saugojimą**: Praktinius būdus, kaip suteikti atminties galimybes savo AI agentams, akcentuojant trumpalaikę ir ilgalaikę atmintį.

• **AI agentų savęs tobulinimą**: Kaip atmintis leidžia agentams mokytis iš ankstesnių sąveikų ir tobulėti laikui bėgant.

## Galimos įgyvendinimo versijos

Šioje pamokoje pateikiami du išsamūs užrašų knygelės vadovėliai:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Įgyvendina atmintį naudojant Mem0 ir Azure AI Search su Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Įgyvendina struktūrizuotą atmintį naudojant Cognee, automatiškai kuria žinių grafą, pagrįstą įterpimais, vizualizuoja grafiką ir protingą paiešką

## Mokymosi tikslai

Baigę šią pamoką jūs sugebėsite:

• **Skirti įvairius AI agentų atminties tipus**, įskaitant darbo, trumpalaikę ir ilgalaikę atmintį, taip pat specializuotas formas, kaip persona ir epizodinė atmintis.

• **Įgyvendinti ir valdyti trumpalaikę bei ilgalaikę atmintį AI agentams** naudojant Microsoft Agent Framework, pasitelkiant įrankius kaip Mem0, Cognee, Whiteboard atmintį ir integruojant su Azure AI Search.

• **Suprasti savęs tobulinančių AI agentų principus** ir kaip tvirti atminties valdymo mechanizmai prisideda prie nuolatinio mokymosi ir prisitaikymo.

## AI agentų atminties supratimas

Pagrindinė AI agentų atmintis reiškia mechanizmus, leidžiančius jiems išlaikyti ir atsiminti informaciją. Ši informacija gali būti specifiniai pokalbio duomenys, naudotojo pageidavimai, praeities veiksmai ar net išmokti modeliai.

Be atminties AI programėlės dažnai būna be būsenos, tai reiškia, kad kiekviena sąveika prasideda iš naujo. Tai sukuria pasikartojančią ir varginančią naudotojo patirtį, kai agentas „pamiršta“ ankstesnį kontekstą ar pageidavimus.

### Kodėl atmintis svarbi?

Agento intelektas glaudžiai susijęs su gebėjimu prisiminti ir naudoti praeities informaciją. Atmintis leidžia agentams būti:

• **Reflektuojančiais**: mokytis iš praeities veiksmų ir rezultatų.

• **Interaktyviais**: palaikyti kontekstą vykstant pokalbiui.

• **Proaktyviais ir reaguojančiais**: numatyti poreikius arba reaguoti tinkamai, remiantis istoriniais duomenimis.

• **Autonominiais**: veikti nepriklausomiau, pasitelkiant saugomą žinių bazę.

Įgyvendinant atmintį siekiama padaryti agentus patikimesnius ir kompetentingesnius.

### Atminties tipai

#### Darbinė atmintis

Įsivaizduokite tai kaip užrašų popierių, kurį agentas naudoja vykdant vieną užduotį ar mąstymo procesą. Ji laiko informaciją, reikalingą kitam žingsniui apskaičiuoti.

AI agentų darbinė atmintis dažnai fiksuoja svarbiausią pokalbio informaciją, net jei visas pokalbio istorijos ilgis yra ilgas arba sutrumpintas. Ji koncentruojasi į pagrindinių elementų, tokių kaip reikalavimai, pasiūlymai, sprendimai ir veiksmai, išgavimą.

**Darbinės atminties pavyzdys**

Kelionių užsakymo agentas gali fiksuoti vartotojo specifinį prašymą, pvz., „Noriu užsakyti kelionę į Paryžių“. Šis reikalavimas laikomas tiesioginiame agente esančiame kontekste, kad nukreiptų esamą sąveiką.

#### Trumpalaikė atmintis

Šis atminties tipas saugo informaciją vieno pokalbio ar sesijos metu. Tai esamo pokalbio kontekstas, leidžiantis agentui grįžti prie ankstesnių dialogo posūkių.

[Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK pavyzdžiuose tai atitinka `AgentSession`, sukurtą naudojant `agent.create_session()`. Sesija yra framework įmontuota trumpalaikė atmintis: ji palaiko pokalbio kontekstą, kol ta pati sesija naudojama, tačiau šis kontekstas neišsaugomas, kai sesija baigiasi arba programa paleidžiama iš naujo. Naudokite ilgalaikę atmintį faktams ir pageidavimams, kuriuos reikia išlaikyti per sesijas, dažniausiai per duomenų bazę, vektorių indeksą ar kitą nuolatinę saugyklą.

**Trumpalaikės atminties pavyzdys**

Jei vartotojas klausia „Kiek kainuotų skrydis į Paryžių?“ ir po to priduria „O kaip dėl apgyvendinimo ten?“, trumpalaikė atmintis užtikrina, kad agentas supranta, jog „ten“ tas pats kaip „Paryžiuje“ šiame pokalbyje.

#### Ilgalaikė atmintis

Tai informacija, kuri išlieka per daugelį pokalbių ar sesijų. Ji leidžia agentams prisiminti vartotojo pageidavimus, istorines sąveikas ar bendrą žinių bazę ilgesniam laikui. Tai svarbu personalizavimui.

**Ilgalaikės atminties pavyzdys**

Ilgalaikė atmintis gali saugoti, kad „Ben mėgsta slidinėjimą ir lauko veiklas, mėgsta kavą su kalnų vaizdu ir vengia pažengusių slidinėjimo trasų dėl praeities traumos“. Ši informacija, surinkta iš ankstesnių sąveikų, įtakoja rekomendacijas būsimose kelionių planavimo sesijose, darant jas labai suasmenintas.

#### Persona atmintis

Šis specializuotas atminties tipas padeda agentui ugdyti nuoseklią „asmenybę“ arba „personą“. Ji leidžia agentui atsiminti detales apie save ar savo numatytą vaidmenį, todėl sąveikos tampa sklandesnės ir labiau orientuotos.

**Persona atminties pavyzdys**  
Jei kelionių agentas yra sukurtas kaip „ekspertas slidinėjimo planuotojas“, persona atmintis gali sustiprinti šį vaidmenį, veikiant atsakymams, atitinkantiems eksperto toną ir žinias.

#### Darbo eigų / epizodinė atmintis

Ši atmintis saugo veiksmų seką, kurią agentas atlieka sudėtingos užduoties metu, įtraukiant sėkmes ir nesėkmes. Tai tarsi prisiminimas apie konkrečius „epizodus“ ar patirtis, kad būtų galima iš jų mokytis.

**Epizodinės atminties pavyzdys**

Jei agentas bandė užsakyti konkretų skrydį, bet nepavyko dėl prieinamumo trūkumo, epizodinė atmintis gali įrašyti šią nesėkmę, leidžiant agentui bandyti kitus skrydžius arba informuoti vartotoją apie problemą labiau informuotai vėlesniu bandymu.

#### Subjekto atmintis

Tai apima konkrečių subjektų (kaip žmonės, vietos ar daiktai) ir įvykių iš pokalbių išgavimą ir įsimintį. Tai leidžia agentui sukurti struktūruotą supratimą apie aptartus svarbius elementus.

**Subjekto atminties pavyzdys**

Iš pokalbio apie praeitą kelionę agentas gali išskirti „Paryžių“, „Eifelio bokštą“ ir „vakarienę restorane Le Chat Noir“ kaip subjektus. Ateities sąveikoje agentas galėtų prisiminti „Le Chat Noir“ ir pasiūlyti padaryti naują rezervaciją.

#### Struktūrizuota RAG (Retrieval Augmented Generation)

Nors RAG yra platesnė technika, „Struktūrizuota RAG“ išskiriama kaip galinga atminties technologija. Ji ištraukia tankią, struktūruotą informaciją iš įvairių šaltinių (pokalbių, el. laiškų, vaizdų) ir naudoja ją tikslumui, atgaminimui ir greičiui pagerinti atsakymuose. Skirtingai nuo klasikinio RAG, kuris remiasi tik semantiniu panašumu, Struktūrizuota RAG veikia pagal esamą informacijos struktūrą.

**Struktūrizuotos RAG pavyzdys**

Užuot tik suradusi raktinius žodžius, Struktūrizuota RAG gali išanalizuoti skrydžio detales (vietą, datą, laiką, oro linijas) iš el. laiško ir saugoti juos struktūruotu formatu. Tai leidžia užduoti tikslius klausimus, pvz., „Kokį skrydį į Paryžių užsakiau antradienį?“

## Atminties įgyvendinimas ir saugojimas

Atminties įgyvendinimas AI agentams apima sistemingą **atminties valdymo** procesą, įskaitant generavimą, saugojimą, gavimą, integravimą, atnaujinimą ir net „pamiršimą“ (arba ištrynimą) informacijos. Ypatingai svarbus yra informacijos gavimas.

### Specializuoti atminties įrankiai

#### Mem0

Vienas iš būdų saugoti ir valdyti agentų atmintį yra naudoti specializuotus įrankius, kaip Mem0. Mem0 veikia kaip nuolatinis atminties sluoksnis, leidžiantis agentams prisiminti svarbias sąveikas, saugoti naudotojų pageidavimus ir faktinį kontekstą bei mokytis iš sėkmių ir nesėkmių laikui bėgant. Idėja yra, kad be būsenos agentai tampa būseną turinčiais.

Jis veikia per **dvikartį atminties srautą: išgavimą ir atnaujinimą**. Pirmiausia, žinutės, pridėtos prie agento siūlo, siunčiamos Mem0 paslaugai, kuri naudoja Didelį Kalbos Modelį (LLM), apibendrinti pokalbio istoriją ir išgauti naujas atmintis. Vėliau LLM valdomas atnaujinimo etapas nusprendžia, ar pridėti, pakeisti ar ištrinti šias atmintis, saugodamas jas mišriame duomenų saugyklos pavidale, apimančiame vektorių, grafo ir reikšmių porų duomenų bazes. Ši sistema taip pat palaiko įvairius atminties tipus ir gali įtraukti grafo atmintį santykiams tarp subjektų valdyti.

#### Cognee

Kita galinga priemonė yra **Cognee**, atviro kodo semantinė atmintis AI agentams, kuri paverčia struktūruotus ir nestruktūruotus duomenis į užklausomus žinių grafus, pagrįstus įterpimais. Cognee siūlo **dvigubos saugyklos architektūrą**, kuri apjungia vektorių panašumo paiešką su grafo ryšiais, leidžiančią agentams suprasti ne tik ką informacija yra panaši, bet ir kaip sąvokos yra susijusios.

Jis puikiai tinka **mišriai paieškai**, kuri sujungia vektorių panašumą, grafo struktūrą ir LLM loginį samprotavimą - nuo žaliavinių fragmentų paieškos iki klausimų atsakymo, žinančio grafo kontekstą. Ši sistema palaiko **gyvą atmintį**, kuri vystosi ir auga, tuo pačiu išlikdama užklausoma kaip viena sujungta grafo struktūra, palaikydama tiek trumpalaikį sesijos kontekstą, tiek ilgalaikę nuolatinę atmintį.

Cognee užrašų knygelės vadovėlis ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstruoja šio vieningo atminties sluoksnio kūrimą, pateikdamas praktinius pavyzdžius, kaip įvesti įvairius duomenų šaltinius, vizualizuoti žinių grafiką ir užduoti klausimus su skirtingomis paieškos strategijomis, pritaikytomis konkretiems agentų poreikiams.

### Atminties saugojimas naudojant RAG

Be specializuotų atminties įrankių, kaip Mem0, galite pasinaudoti galingomis paieškos paslaugomis, kaip **Azure AI Search**, kaip atminties saugojimo ir gavimo dalimi, ypač struktūrizuotam RAG.

Tai leidžia pagrįsti agentų atsakymus savo duomenimis, užtikrinant labiau aktualius ir tikslius atsakymus. Azure AI Search gali būti naudojama saugoti vartotojo specifines kelionių atmintis, produktų katalogus ar bet kokias kitas domenų žinias.

Azure AI Search palaiko tokias galimybes kaip **Struktūrizuota RAG**, kuri puikiai ištraukia ir gauna tankią, struktūruotą informaciją iš didelių duomenų rinkinių, kaip pokalbių istorijos, el. laiškai ar net vaizdai. Tai suteikia „superžmogišką tikslumą ir išsaugojimą“ lyginant su tradiciniais teksto fragmentų ir įterpimų metodais.

## Kaip padaryti AI agentus savęs tobulinančiais

Dažnas savęs tobulinančių agentų modelis apima **„žinių agento“** įvedimą. Šis atskiras agentas stebi pagrindinį pokalbį tarp vartotojo ir pagrindinio agento. Jo vaidmuo yra:

1. **Identifikuoti vertingą informaciją**: nustatyti, ar bet kuri pokalbio dalis verta išsaugoti kaip bendrą žinią arba specifinį vartotojo pageidavimą.

2. **Išgauti ir apibendrinti**: sutraukti esmę arba pageidavimą iš pokalbio.

3. **Saugyklos žinių bazėje**: išsaugoti šią informaciją, dažnai vektorinėse duomenų bazėse, kad galėtų būti vėliau pasiimta.

4. **Papildyti būsimus užklausimus**: kai vartotojas pateikia naują užklausą, žinių agentas surenka atitinkamą saugomą informaciją ir prideda ją prie vartotojo užklausos, suteikdamas svarbų kontekstą pagrindiniam agentui (panašiai kaip RAG).

### Atminties optimizavimai

• **Vėlinimo valdymas**: siekiant išvengti naudotojo sąveikų sulėtėjimo, pradžioje galima naudoti pigesnį ir greitesnį modelį, kuris greitai patikrina, ar informacija verta saugoti ar gauti, o sudėtingesnę ištraukimo / gavimo procedūrą aktyvuoja tik prireikus.

• **Žinių bazės priežiūra**: didėjant žinių bazei, rečiau naudojama informacija gali būti perkelta į „šaltą saugyklą“, siekiant sumažinti išlaidas.

## Ar turite daugiau klausimų apie agentų atmintį?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), susipažinkite su kitais besimokančiais, dalyvaukite konsultacijose ir gaukite atsakymus į klausimus apie AI agentus.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->