# AI-agentit aloittelijoille - kurssi

![AI Agents for Beginners](../../translated_images/fi/repo-thumbnailv2.06f4a48036fde647.webp)

## Kurssi, joka opettaa kaiken tarpeellisen AI-agenttien rakentamisen aloittamiseksi

[![GitHub license](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 Monikielituki

#### Tuettu GitHub Actionin avulla (automaattinen & aina ajan tasalla)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](./README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Haluatko mieluummin kloonata paikallisesti?**
>
> Tämä arkisto sisältää yli 50 kieliversiota, mikä lisää merkittävästi latauskokoa. Jos haluat kloonata ilman käännöksiä, käytä sparse checkout -toimintoa:
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
> Saat kaiken tarpeellisen kurssin läpikäymiseen huomattavasti nopeammalla latauksella.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Jos haluat, että muita käännöskieliä tuetaan, ne ovat listattuna [tässä](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 Aloittaminen

Tämä kurssi kattaa AI-agenttien rakentamisen perusteet. Jokainen oppitunti käsittelee omaa aihettaan, joten voit aloittaa sieltä, mistä haluat!

Kurssilla on monikielituki. Tutustu saatavilla oleviin kieliin kohdassa [monikielituki](#-multi-language-support).

Jos tämä on ensimmäinen kerta, kun rakennat generatiivisen tekoälyn malleilla, tutustu [Generatiivinen tekoäly aloittelijoille](https://aka.ms/genai-beginners) -kurssiimme, joka sisältää 21 oppituntia GenAI:n kanssa rakentamisesta.

Muista myös [tähtätä (🌟) tämä repositorio](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ja [forkkaa tämä repositorio](https://github.com/microsoft/ai-agents-for-beginners/fork) suorittaaksesi koodin.

### Tapaa muita oppijoita, saat vastauksia kysymyksiisi

Jos jumitut tai sinulla on kysyttävää AI-agenttien rakentamisesta, liity omistettuun Discord-kanavaamme [Microsoft Foundry Discordissa](https://aka.ms/ai-agents/discord).

### Tarvittavat välineet

Jokainen tämän kurssin oppitunti sisältää koodiesimerkkejä, jotka löytyvät code_samples-kansiosta. Voit [forkata tämän repositorion](https://github.com/microsoft/ai-agents-for-beginners/fork) luodaksesi oman kopiosi.

Näiden harjoitusten koodiesimerkeissä käytetään Microsoft Agent Frameworkia Azure AI Foundry Agent Service V2:n kanssa:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - vaatii Azure-tilin

Tämä kurssi käyttää seuraavia Microsoftin AI-agenttikehyksiä ja -palveluja:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

Jotkut koodiesimerkit tukevat myös vaihtoehtoisia OpenAI-yhteensopivia palveluntarjoajia, kuten [MiniMax](https://platform.minimaxi.com/), joka tarjoaa suurikapasiteettisia malleja (jopa 204K tokenia). Katso [kurssin asennus](./00-course-setup/README.md) asetusohjeet.

Lisätietoja koodin suorittamisesta tälle kurssille löydät [kurssin asennuksesta](./00-course-setup/README.md).

## 🙏 Haluatko auttaa?

Onko sinulla ehdotuksia tai löysitkö kirjoitus- tai koodivirheitä? [Luo issue](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) tai [tee pull request](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 Jokainen oppitunti sisältää

- Kirjallisen oppitunnin README-tiedostossa ja lyhyen videon
- Python-koodiesimerkkejä Microsoft Agent Frameworkin ja Azure AI Foundryn kanssa
- Linkkejä lisämateriaaleihin oppimisen jatkamista varten


## 🗃️ Oppitunnit

| **Oppitunti**                            | **Teksti & Koodi**                                 | **Video**                                                   | **Lisäopiskelu**                                                                       |
|-----------------------------------------|---------------------------------------------------|-------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Johdatus AI-agentteihin ja käyttötapauksiin | [Linkki](./01-intro-to-ai-agents/README.md)       | [Video](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)   | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI-agenttikehysten tutkiminen           | [Linkki](./02-explore-agentic-frameworks/README.md) | [Video](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)   | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI-agenttien suunnittelumallien ymmärtäminen | [Linkki](./03-agentic-design-patterns/README.md)  | [Video](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)   | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Työkalujen käyttösuunnittelumalli       | [Linkki](./04-tool-use/README.md)                  | [Video](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)   | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Agenttinen RAG                         | [Linkki](./05-agentic-rag/README.md)               | [Video](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)   | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Luotettavien AI-agenttien rakentaminen | [Linkki](./06-building-trustworthy-agents/README.md) | [Video](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK )  | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Suunnittelumalli                        | [Linkki](./07-planning-design/README.md)           | [Video](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)   | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Moni-agenttinen suunnittelumalli        | [Linkki](./08-multi-agent/README.md)               | [Video](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)   | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Metakognitiomallin suunnittelu                 | [Linkki](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI-agentit tuotannossa                      | [Linkki](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Agenttisprotokollien käyttö (MCP, A2A ja NLWeb) | [Linkki](./11-agentic-protocols/README.md)           | [Video](https://youtu.be/X-Dh9R3Opn8)                                 | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Konteksti-insinöörityö AI-agenteille            | [Linkki](./12-context-engineering/README.md)         | [Video](https://youtu.be/F5zqRV7gEag)                                 | [Linkki](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Agenttimuistin hallinta                      | [Linkki](./13-agent-memory/README.md)     |      [Video](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| Microsoft Agent Frameworkin tutkiminen                         | [Linkki](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| Tietokoneen käyttöagenttien rakentaminen (CUA)           | [Linkki](./15-browser-use/README.md)     |                                                            | [Linkki](https://docs.browser-use.com/examples/templates/playwright-integration)         |
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
[![AI-agentit aloittelijoille](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Generatiivisen tekoälyn sarja
[![Generatiivinen tekoäly aloittelijoille](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen tekoäly (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen tekoäly (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen tekoäly (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### Peruskoulutus
[![ML aloittelijoille](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science aloittelijoille](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI aloittelijoille](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kyberturvallisuus aloittelijoille](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web-kehitys aloittelijoille](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT aloittelijoille](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR-kehitys aloittelijoille](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Copilot-sarja
[![Copilot tekoälyn pari-ohjelmointiin](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET:lle](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot-seikkailu](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 Yhteisön kiitokset

Kiitos [Shivam Goyalille](https://www.linkedin.com/in/shivam2003/) tärkeistä koodiesimerkeistä, jotka demonstroivat Agenttista RAG:ia. 

## Osallistuminen

Tämä projekti toivottaa tervetulleeksi osallistumisen ja ehdotukset. Useimmat osallistumiset edellyttävät,
että hyväksyt Osallistujan lisenssisopimuksen (Contributor License Agreement, CLA), jossa vakuutat
omistavasi oikeudet ja myöntäväsi meille oikeudet käyttää panostustasi. Lisätietoja löytyy osoitteesta <https://cla.opensource.microsoft.com>.

Kun lähetät pull-pyynnön, CLA-botti määrittää automaattisesti, tarvitseeko sinun toimittaa
CLA ja merkitsee PR:n asianmukaisesti (esim. tilantarkistus, kommentti). Noudata vain botin antamia ohjeita.
Tämä tulee tehdä vain kerran kaikissa CLA:ta käyttävissä repositorioissa.

Tämä projekti on ottanut käyttöön [Microsoftin avoimen lähdekoodin käytösohjeet](https://opensource.microsoft.com/codeofconduct/).
Lisätietoja löytyy [Käyttöohjeen UKK:sta](https://opensource.microsoft.com/codeofconduct/faq/) tai
ota yhteyttä sähköpostitse osoitteeseen [opencode@microsoft.com](mailto:opencode@microsoft.com), jos sinulla on lisäkysymyksiä tai kommentteja.

## Tavamerkit

Tämä projekti voi sisältää tavamerkkejä tai logoja projekteille, tuotteille tai palveluille. Microsoftin
tavamerkkien tai logojen hyväksytty käyttö edellyttää ja noudattaa
[Microsoftin tavamerkkien ja brändiohjeita](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Microsoftin tavamerkkien tai logojen käyttö muokatuissa versioissa ei saa aiheuttaa sekaannusta tai antaa ymmärtää Microsoftin sponsoroivan projektia.
Kolmansien osapuolten tavamerkkien tai logojen käyttö on kolmansien osapuolten sääntöjen mukaista.

## Apua

Jos jumitut tai sinulla on kysyttävää tekoälysovellusten rakentamisesta, liity mukaan:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jos sinulla on palautetta tuotteesta tai virheitä rakentamisen aikana, käy:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, tulee ottaa huomioon, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on katsottava viralliseksi lähteeksi. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->