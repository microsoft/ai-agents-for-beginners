# AI-agentit aloittelijoille - Kurssi

![Generatiivinen tekoäly aloittelijoille](../../translated_images/fi/repo-thumbnailv2.06f4a48036fde647.webp)

## Kurssi, joka opettaa kaiken, mitä tarvitset AI-agenttien rakentamisen aloittamiseen

[![GitHub-lisenssi](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub-yhteistyökumppanit](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub-ongelmat](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-pyynnöt](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 Monikielinen tuki

#### Tuettu GitHub Actionin kautta (automaattinen & aina ajan tasalla)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[arabia](../ar/README.md) | [bengali](../bn/README.md) | [bulgaria](../bg/README.md) | [burma (Myanmar)](../my/README.md) | [kiina (yksinkertaistettu)](../zh-CN/README.md) | [kiina (perinteinen, Hong Kong)](../zh-HK/README.md) | [kiina (perinteinen, Macao)](../zh-MO/README.md) | [kiina (perinteinen, Taiwan)](../zh-TW/README.md) | [kroatia](../hr/README.md) | [tšekki](../cs/README.md) | [tanska](../da/README.md) | [hollanti](../nl/README.md) | [viro](../et/README.md) | [suomi](./README.md) | [ranska](../fr/README.md) | [saksa](../de/README.md) | [kreikka](../el/README.md) | [heprea](../he/README.md) | [hindi](../hi/README.md) | [unkari](../hu/README.md) | [indonesia](../id/README.md) | [italia](../it/README.md) | [japani](../ja/README.md) | [kannada](../kn/README.md) | [korea](../ko/README.md) | [liettua](../lt/README.md) | [malaiji](../ms/README.md) | [malajalam](../ml/README.md) | [marathi](../mr/README.md) | [nepali](../ne/README.md) | [nigerian pidgin](../pcm/README.md) | [norja](../no/README.md) | [persian (farsi)](../fa/README.md) | [puola](../pl/README.md) | [portugali (Brasilia)](../pt-BR/README.md) | [portugali (Portugali)](../pt-PT/README.md) | [pandžabi (gurmukhi)](../pa/README.md) | [romania](../ro/README.md) | [venäjä](../ru/README.md) | [serbia (kyrillinen)](../sr/README.md) | [slovakki](../sk/README.md) | [sloveeni](../sl/README.md) | [espanja](../es/README.md) | [swahili](../sw/README.md) | [ruotsi](../sv/README.md) | [tagalog (filipino)](../tl/README.md) | [tamil](../ta/README.md) | [telugu](../te/README.md) | [thai](../th/README.md) | [turkki](../tr/README.md) | [ukraina](../uk/README.md) | [urdu](../ur/README.md) | [vietnami](../vi/README.md)

> **Haluatko kloonata paikallisesti?**
>
> Tämä repositorio sisältää yli 50 kielen käännökset, mikä kasvattaa merkittävästi latauskokoa. Kloonaa ilman käännöksiä käyttämällä sparse checkout -toimintoa:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Tämä antaa sinulle kaiken tarvittavan kurssin suorittamiseen paljon nopeammalla latauksella.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Jos haluat, että lisäkielikäännöksiä tuetaan, ne löytyvät [täältä](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

[![GitHub seuraajat](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub haarukat](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub tähdet](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 Aloittaminen

Tässä kurssissa on oppitunteja, jotka kattavat AI-agenttien rakentamisen perusteet. Jokainen oppitunti käsittelee omaa aihettaan, joten voit aloittaa mistä haluat!

Kurssilla on monikielinen tuki. Katso käytettävissä olevat kielet [tästä](../..).

Jos rakennat ensimmäistä kertaa generatiivisten tekoälymallien kanssa, tutustu [Generative AI For Beginners](https://aka.ms/genai-beginners) -kurssiin, joka sisältää 21 oppituntia GenAI:n käytöstä.

Älä unohda [tähdätä (🌟) tätä repositoriota](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ja [haarukoi tämä repo](https://github.com/microsoft/ai-agents-for-beginners/fork) ajaaksesi koodin.

### Tapaa muita oppijoita, saat vastauksia kysymyksiisi

Jos juutut tai sinulla on kysyttävää AI-agenttien rakentamisesta, liity omalle Discord-kanavallemme [Microsoft Foundry Discordissa](https://aka.ms/ai-agents/discord).

### Mitä tarvitset

Jokaisessa kurssin oppitunnissa on mukana koodiesimerkkejä, jotka löytyvät code_samples-kansiosta. Voit [haarukoida tämän repoin](https://github.com/microsoft/ai-agents-for-beginners/fork) luodaksesi oman kopiosi.

Näissä harjoituksissa koodiesimerkit käyttävät Microsoft Agent Frameworkia Azure AI Foundry Agent Service V2:n kanssa:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - vaatii Azure-tilin

Tämä kurssi käyttää seuraavia Microsoftin AI-agenttikehyksiä ja -palveluita:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)


Lisätietoja tämän kurssin koodin suorittamisesta saat [Course Setup](./00-course-setup/README.md) -osiosta.

## 🙏 Haluatko auttaa?

Onko sinulla ehdotuksia tai oletko löytänyt kirjoitus- tai koodivirheitä? [Luo ongelma](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) tai [luo pull-pyyntö](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 Jokainen oppitunti sisältää

- Kirjallisen oppitunnin README-tiedostossa ja lyhyen videon
- Python-koodiesimerkkejä, jotka käyttävät Microsoft Agent Frameworkia Azure AI Foundryn kanssa
- Linkkejä lisäresursseihin oppimisen jatkamiseksi


## 🗃️ Oppitunnit

| **Oppitunti**                                | **Teksti & Koodi**                                 | **Video**                                                  | **Lisäoppiminen**                                                                      |
|---------------------------------------------|-----------------------------------------------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Johdanto AI-agentteihin ja agenttien käyttötapauksiin | [Linkki](./01-intro-to-ai-agents/README.md)          | [Video](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Tutustuminen AI-agenttikehyksiin             | [Linkki](./02-explore-agentic-frameworks/README.md)  | [Video](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI-agenttien suunnittelumallit               | [Linkki](./03-agentic-design-patterns/README.md)     | [Video](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Työkalujen käytön suunnittelumalli            | [Linkki](./04-tool-use/README.md)                    | [Video](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Agenttien RAG-malli                           | [Linkki](./05-agentic-rag/README.md)                 | [Video](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Luotettavien AI-agenttien rakentaminen       | [Linkki](./06-building-trustworthy-agents/README.md) | [Video](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Suunnittelumalli                             | [Linkki](./07-planning-design/README.md)             | [Video](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Moni-agenttien suunnittelumalli               | [Linkki](./08-multi-agent/README.md)                 | [Video](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Metakognitiivinen suunnittelumalli            | [Linkki](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI-agentit tuotannossa                      | [Link](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Agenttiprotokollien käyttäminen (MCP, A2A ja NLWeb) | [Link](./11-agentic-protocols/README.md)           | [Video](https://youtu.be/X-Dh9R3Opn8)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Konteksti-tekniikka AI-agentteja varten            | [Link](./12-context-engineering/README.md)         | [Video](https://youtu.be/F5zqRV7gEag)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Agenttimuistin hallinta                      | [Link](./13-agent-memory/README.md)     |      [Video](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| Microsoft Agent -kehyksen tutkiminen                         | [Link](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| Tietokoneen käyttöagenttien rakentaminen (CUA)           | Tulossa pian                            |                                                            |                                                                                        |
| Skaalautuvien agenttien käyttöönotto                    | Tulossa pian                            |                                                            |                                                                                        |
| Paikallisten AI-agenttien luominen                     | Tulossa pian                               |                                                            |                                                                                        |
| AI-agenttien suojaaminen                           | Tulossa pian                               |                                                            |                                                                                        |

## 🎒 Muut kurssit

Tiimimme tuottaa myös muita kursseja! Tutustu:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j aloittelijoille](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js aloittelijoille](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain aloittelijoille](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agentit
[![AZD aloittelijoille](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI aloittelijoille](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP aloittelijoille](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agentit aloittelijoille](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatiivisen tekoälyn sarja
[![Generatiivinen tekoäly aloittelijoille](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen tekoäly (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen tekoäly (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen tekoäly (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Perusoppiminen
[![Koneoppiminen aloittelijoille](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science aloittelijoille](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI aloittelijoille](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kyberturvallisuus aloittelijoille](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web-kehitys aloittelijoille](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT aloittelijoille](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR-kehitys aloittelijoille](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot-sarja
[![Copilot tekoälypariohjelmointia varten](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET-koodareille](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot-seikkailu](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 Kiitokset yhteisölle

Kiitos [Shivam Goyalille](https://www.linkedin.com/in/shivam2003/) tärkeistä koodiesimerkeistä, jotka demonstroivat Agentic RAG:ia.

## Osallistuminen

Tämä projekti toivottaa tervetulleiksi panokset ja ehdotukset. Useimmat panokset edellyttävät, että hyväksyt
Contributor License Agreement (CLA) -sopimuksen, jossa vakuutat, että sinulla on oikeus ja että myönnät meille
oikeudet käyttää panostasi. Lisätietoja löydät osoitteesta <https://cla.opensource.microsoft.com>.

Kun lähetät pull-pyynnön, CLA-botti määrittää automaattisesti, tarvitsetko toimittaa CLA:n, ja merkitsee PR:n asianmukaisesti (esim. tilantarkistus, kommentti). Noudata vain botin antamia ohjeita. Tätä tarvitsee tehdä vain kerran kaikissa repositorioissa, jotka käyttävät CLA:tamme.

Tämä projekti on ottanut käyttöön [Microsoftin avoimen lähdekoodin käytösnormiston](https://opensource.microsoft.com/codeofconduct/).
Lisätietoja löydät [Käytösnormiston UKK:sta](https://opensource.microsoft.com/codeofconduct/faq/) tai ota yhteyttä osoitteeseen [opencode@microsoft.com](mailto:opencode@microsoft.com) jos sinulla on lisäkysymyksiä tai kommentteja.

## Tavara- ja palvelumerkit

Tässä projektissa voi olla tavara- tai palvelumerkkejä projekteista, tuotteista tai palveluista. Microsoftin tavara- ja palvelumerkkien käyttö on sallittua ja sen on noudatettava
[Microsoftin tavara- ja brändiohjeita](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Microsoftin tavara- tai palvelumerkkien käyttö tämän projektin muokatuissa versioissa ei saa aiheuttaa sekaannusta tai antaa vaikutelmaa Microsoftin sponsoroimasta.
Kolmannen osapuolen tavara- ja palvelumerkkien käyttö on kolmansien osapuolten ehtojen alaista.

## Apua saatavilla

Jos tarvitset apua tai sinulla on kysymyksiä tekoälysovellusten rakentamisesta, liity seuraaviin:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jos sinulla on tuotepalaute tai rakennusvirheitä, käy:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on pidettävä ensisijaisena ja luotettavana lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ota vastuuta mahdollisista väärinymmärryksistä tai virhetulkintojen seurauksista, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->