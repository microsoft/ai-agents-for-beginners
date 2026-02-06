# Dirbtinio intelekto agentai pradedantiesiems - kursas

![Generatyvus dirbtinis intelektas pradedantiesiems](../../translated_images/lt/repo-thumbnailv2.06f4a48036fde647.webp)

## Kursas, mokantis visko, ką reikia žinoti norint pradėti kurti DI agentus

[![GitHub licencija](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub indėlininkai](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub problemos](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-užklausos](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 Daugiakalbė palaikymas

#### Palaikoma per GitHub Action (automatiškai ir visuomet atnaujinta)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabų](../ar/README.md) | [Bengalų](../bn/README.md) | [Bulgarų](../bg/README.md) | [Birmos (Mianmaras)](../my/README.md) | [Kinų (supaprastinta)](../zh-CN/README.md) | [Kinų (tradicinė, Honkongas)](../zh-HK/README.md) | [Kinų (tradicinė, Makao)](../zh-MO/README.md) | [Kinų (tradicinė, Taivanas)](../zh-TW/README.md) | [Kroatų](../hr/README.md) | [Čekų](../cs/README.md) | [Danų](../da/README.md) | [Olandų](../nl/README.md) | [Estų](../et/README.md) | [Suomių](../fi/README.md) | [Prancūzų](../fr/README.md) | [Vokiečių](../de/README.md) | [Graikų](../el/README.md) | [Hebrajų](../he/README.md) | [Hindi](../hi/README.md) | [Vengrų](../hu/README.md) | [Indoneziečių](../id/README.md) | [Italų](../it/README.md) | [Japonų](../ja/README.md) | [Kannada](../kn/README.md) | [Korėjiečių](../ko/README.md) | [Lietuvių](./README.md) | [Malajiečių](../ms/README.md) | [Malajalamų](../ml/README.md) | [Maratų](../mr/README.md) | [Nepalų](../ne/README.md) | [Nigerijos pidžinų](../pcm/README.md) | [Norvegų](../no/README.md) | [Persų (farsi)](../fa/README.md) | [Lenkų](../pl/README.md) | [Portugalų (Brazilija)](../pt-BR/README.md) | [Portugalų (Portugalija)](../pt-PT/README.md) | [Pandžabi (Gurmukhi)](../pa/README.md) | [Rumunų](../ro/README.md) | [Rusų](../ru/README.md) | [Serbų (kirilica)](../sr/README.md) | [Slovakų](../sk/README.md) | [Slovėnų](../sl/README.md) | [Ispanų](../es/README.md) | [Svasilio](../sw/README.md) | [Švedų](../sv/README.md) | [Tagalogų (filipiniečių)](../tl/README.md) | [Tamilų](../ta/README.md) | [Telugų](../te/README.md) | [Tajų](../th/README.md) | [Turkų](../tr/README.md) | [Ukrainiečių](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamių](../vi/README.md)

> **Norite klonuoti vietoje?**

> Ši saugykla talpina per 50 kalbų vertimų, kurie gerokai padidina atsisiuntimo dydį. Norėdami klonuoti be vertimų, naudokite ribotą patikrinimą (sparse checkout):
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Tai suteiks viską, ko jums reikia kursui baigti, žymiai greičiau parsisiunčiant.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Jei norite, kad būtų palaikomos papildomos vertimo kalbos, jos išvardytos [čia](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

[![GitHub stebėtojai](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub šakos](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub žvaigždės](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 Pradžia

Šis kursas apima pamokas, kurios supažindina su DI agentų kuriimo pagrindais. Kiekviena pamoka apima atskirą temą, tad galite pradėti nuo bet kurios jums patinkančios!

Šiam kursui yra daugiakalbė palaikymas. Žr. mūsų [galimų kalbų sąrašą čia](../..).

Jeigu pirmą kartą dirbate su generatyviais DI modeliais, peržiūrėkite mūsų [Generatyvaus DI pradedantiesiems](https://aka.ms/genai-beginners) kursą, kuriame yra 21 pamoka apie darbą su GenAI.

Nepamirškite [pažymėti šią saugyklą žvaigždute (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ir [padaryti fork šiai saugyklai](https://github.com/microsoft/ai-agents-for-beginners/fork), kad galėtumėte vykdyti kodą.

### Susipažinkite su kitais besimokančiaisiais, gaukite atsakymus į klausimus

Jei įstringate ar turite klausimų apie DI agentų kūrimą, prisijunkite prie mūsų specialios Discord kanalo [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord).

### Ko jums reikia

Kiekviena pamoka apima kodo pavyzdžius, esančius kataloge code_samples. Galite [padaryti fork šiai saugyklai](https://github.com/microsoft/ai-agents-for-beginners/fork), kad sukurtumėte savo kopiją.

Šių pratimų kodo pavyzdžiai naudoja Azure AI Foundry ir GitHub modelių katalogus darbui su kalbos modeliais:

- [Github modeliai](https://aka.ms/ai-agents-beginners/github-models) - nemokama / ribota
- [Azure AI Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - reikalinga Azure paskyra

Šis kursas taip pat naudoja šias DI agentų sistemas ir paslaugas iš Microsoft:

- [Microsoft agentų sistema (MAF) - nauja!](https://aka.ms/ai-agents-beginners/agent-framewrok)
- [Azure AI agentų paslauga](https://aka.ms/ai-agents-beginners/ai-agent-service)
- [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel)
- [AutoGen](https://aka.ms/ai-agents/autogen)

Dėl daugiau informacijos, kaip paleisti šio kurso kodą, eikite į [Course Setup](./00-course-setup/README.md).

## 🙏 Norite padėti?

Ar turite pasiūlymų ar radote rašybos ar kodo klaidų? [Praneškite apie problemą](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) arba [sukurkite pull request](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 Kiekviena pamoka apima

- Rašytinę pamoką README faile ir trumpą video
- Python kodo pavyzdžius, palaikančius Azure AI Foundry ir Github modelius (nemokami)
- Nuorodas į papildomus išteklius toliau mokytis


## 🗃️ Pamokos

| **Pamoka**                                  | **Tekstas ir kodas**                              | **Video**                                                  | **Papildomas mokymasis**                                                                       |
|---------------------------------------------|---------------------------------------------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Įvadas į DI agentus ir jų taikymus          | [Nuoroda](./01-intro-to-ai-agents/README.md)      | [Video](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [Nuoroda](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)       |
| DI agentų sistemų tyrinėjimas                | [Nuoroda](./02-explore-agentic-frameworks/README.md) | [Video](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [Nuoroda](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)       |
| DI agentų kūrimo dizaino modeliai            | [Nuoroda](./03-agentic-design-patterns/README.md) | [Video](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [Nuoroda](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)       |
| Įrankių naudojimo dizaino modelis             | [Nuoroda](./04-tool-use/README.md)                 | [Video](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [Nuoroda](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)       |
| Agentic RAG                                  | [Nuoroda](./05-agentic-rag/README.md)              | [Video](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [Nuoroda](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)       |
| Pasitikėjimą kuriančių DI agentų kūrimas    | [Nuoroda](./06-building-trustworthy-agents/README.md) | [Video](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [Nuoroda](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)       |
| Planavimo dizaino modelis                      | [Nuoroda](./07-planning-design/README.md)          | [Video](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [Nuoroda](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)       |
| Multi-agentų dizaino modelis                   | [Nuoroda](./08-multi-agent/README.md)              | [Video](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [Nuoroda](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)       |
| Metakognityvinio dizaino šablonas                 | [Nuoroda](./09-metacognition/README.md)               | [Vaizdo įrašas](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Nuoroda](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Dirbtinio intelekto agentai gamyboje                      | [Nuoroda](./10-ai-agents-production/README.md)        | [Vaizdo įrašas](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Nuoroda](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Agentinių protokolų naudojimas (MCP, A2A ir NLWeb) | [Nuoroda](./11-agentic-protocols/README.md)           | [Vaizdo įrašas](https://youtu.be/X-Dh9R3Opn8)                                 | [Nuoroda](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Konteksto inžinerija AI agentams            | [Nuoroda](./12-context-engineering/README.md)         | [Vaizdo įrašas](https://youtu.be/F5zqRV7gEag)                                 | [Nuoroda](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Agentinės atminties valdymas                      | [Nuoroda](./13-agent-memory/README.md)     |      [Vaizdo įrašas](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| Microsoft agentų sistemos tyrinėjimas                         | [Nuoroda](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| Kompiuterinių vartotojų agentų (CUA) kūrimas           | Greitai                            |                                                            |                                                                                        |
| Masto agentų diegimas                    | Greitai                            |                                                            |                                                                                        |
| Vietinių AI agentų kūrimas                     | Greitai                               |                                                            |                                                                                        |
| AI agentų saugumas                           | Greitai                               |                                                            |                                                                                        |

## 🎒 Kiti kursai

Mūsų komanda kuria ir kitus kursus! Peržiūrėkite:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j pradedantiesiems](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js pradedantiesiems](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain pradedantiesiems](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agentai
[![AZD pradedantiesiems](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pradedantiesiems](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pradedantiesiems](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agentai pradedantiesiems](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatyvioji DI serija
[![Generatyvioji DI pradedantiesiems](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatyvioji DI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatyvioji DI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatyvioji DI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Pagrindiniai mokymai
[![ML pradedantiesiems](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Duomenų mokslas pradedantiesiems](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![DI pradedantiesiems](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kibernetinis saugumas pradedantiesiems](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Tinklalapių kūrimas pradedantiesiems](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![Daiktų internetas pradedantiesiems](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR kūrimas pradedantiesiems](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot serija
[![Copilot dirbtinio intelekto poriniam programavimui](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot nuotykiai](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 Bendruomenės padėka

Dėkojame [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) už svarbių kodų pavyzdžių, demonstruojančių agentinį RAG, pateikimą.

## Dalyvavimas

Šis projektas kviečia prisidėti ir teikti pasiūlymus. Daugumai indėlių reikės sutikti su
Indėlio Licencijos Sutartimi (CLA), deklaruojančia, kad turite teisę ir iš tiesų suteikiate mums
teisę naudoti jūsų indėlį. Daugiau sužinoti galima adresu <https://cla.opensource.microsoft.com>.

Pateikus pull request'ą, CLA robotas automatiškai nustatys, ar reikia pateikti
CLA ir tinkamai pažymės PR (pvz., būsena, komentaras). Tiesiog sekite roboto pateiktas instrukcijas.
Tai reikia padaryti tik kartą visuose repozitorijuose, kuriuose naudojama mūsų CLA.

Šis projektas priėmė [Microsoft atvirojo kodo elgesio kodeksą](https://opensource.microsoft.com/codeofconduct/).
Daugiau informacijos rasite [Elgesio kodekso DUK](https://opensource.microsoft.com/codeofconduct/faq/) arba kreipkitės į [opencode@microsoft.com](mailto:opencode@microsoft.com) dėl papildomų klausimų ar pastabų.

## Prekių ženklai

Šis projektas gali turėti prekių ženklus arba logotipus, susijusius su projektais, produktais ar paslaugomis. Leidžiamas Microsoft
prekių ženklų ar logotipų naudojimas yra reglamentuojamas ir turi laikytis
[Microsoft prekių ženklų ir ženklinimo gairių](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Microsoft prekių ženklų ar logotipų naudojimas projektų modifikuotose versijose neturi sukelti painiavos ar rodyti Microsoft rėmimą.
Trečiųjų šalių prekių ženklų ar logotipų naudojimas yra reglamentuojamas atitinkamų trečiųjų šalių politikos.

## Pagalbos gavimas


Jei įstrigote arba turite klausimų apie DI programėlių kūrimą, prisijunkite prie:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jei turite produkto atsiliepimų arba klaidų kuriant, apsilankykite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Pirminis dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama pasitelkti profesionalų vertimą žmogaus. Mes neatsakome už bet kokius nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->