# Paggawa ng Computer Use Agents (CUA)

Ang mga computer use agents ay maaaring makipag-ugnayan sa mga website sa parehong paraan ng isang tao: sa pamamagitan ng pagbubukas ng browser, pagsuri sa pahina, at paggawa ng susunod na pinakamainam na hakbang mula sa nakikita nila. Sa araling ito, gagawa ka ng isang browser automation agent na naghahanap sa Airbnb, kumukuha ng nakaayos na data ng mga listahan, at nagtutukoy ng pinakamurang tuluyan sa Stockholm.

Pinagsasama ng araling ito ang Browser-Use para sa AI-driven navigation, Playwright at Chrome DevTools Protocol (CDP) para sa kontrol ng browser, Azure OpenAI para sa vision-enabled na pangangatwiran, at Pydantic para sa nakaayos na pagkuha.

## Panimula

Tatalakayin sa araling ito ang:

- Pag-unawa kung kailan mas angkop ang computer use agents kaysa sa API-only automation
- Pagsasama ng Browser-Use kasama ang Playwright at CDP para sa maaasahang pamamahala ng lifecycle ng browser
- Paggamit ng Azure OpenAI vision at nakaayos na Pydantic output para kumuha ng data ng listahan mula sa mga dynamic na web page
- Pagpapasya kung kailan gagamit ng agent-first, actor-first, o hybrid browser automation workflow

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, malalaman mo kung paano:

- I-configure ang Browser-Use gamit ang Azure OpenAI at Playwright
- Bumuo ng browser automation workflow na nagna-navigate sa totoong website at humahawak ng dynamic na mga elemento ng UI
- Kunin ang mga typed na resulta mula sa nakikitang nilalaman ng pahina at gawing downstream business logic
- Pumili sa pagitan ng agent at actor patterns batay sa gaano kakatagalan ang gawain sa browser

## Halimbawa ng Code

Kasama sa araling ito ang isang notebook tutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Naglulunsad ng Chrome session gamit ang CDP, naghahanap ng mga listahan sa Airbnb para sa Stockholm, kumukuha ng mga presyo gamit ang Browser-Use vision, at ibinabalik ang pinakamurang opsyon bilang nakaayos na data.

## Mga Kinakailangan

- Python 3.12+
- Na-configure na Azure OpenAI deployment sa iyong kapaligiran
- Naka-install na Chrome o Chromium nang lokal
- Naka-install na Playwright dependencies
- Basic na pamilyar sa async Python

## Setup

I-install ang mga package na ginamit sa notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

I-set ang Azure OpenAI environment variables na ginagamit ng notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opsyonal: awtomatikong gagamitin ang pinakabagong bersyon ng API kapag hindi isinama
AZURE_OPENAI_API_VERSION=...
```

## Pangkalahatang-ideya ng Arkitektura

Ipinapakita ng notebook ang isang hybrid na browser automation workflow:

1. Nagsisimula ang Chrome na naka-enable ang CDP upang parehong maibahagi ng Playwright at Browser-Use ang iisang browser session.
2. Isang Browser-Use agent ang humahawak sa open-ended na mga gawain ng pag-navigate gaya ng pagbubukas ng Airbnb, pagtatanggal ng mga pop-ups, at paghahanap para sa Stockholm.
3. Sinusuri ang aktibong pahina gamit ang nakaayos na Pydantic schema para kunin ang mga pamagat ng listahan, presyo kada gabi, rating, at mga URL.
4. Kinukumpara ng Python logic ang mga nakuhang listahan at itinatampok ang pinakamurang resulta.

Pinapanatili ng pamamaraang ito ang flexible, vision-based na pangangatwiran na magaling ang Browser-Use habang binibigyan ka ng deterministikong kontrol sa browser kapag kailangan mo ito.

## Mga Pangunahing Aral at Pinakamahuhusay na Gawi

### Kailan Gagamit ng Agent kumpara sa Actor

| Scenario | Gumamit ng Agent | Gumamit ng Actor |
|----------|------------------|-----------------|
| Dynamic na layout | Oo, kaya ng AI na umangkop sa mga pagbabago sa pahina | Hindi, madaling masira ang mga brittle selector |
| Kilalang istruktura | Hindi, mas mabagal ang agent kaysa sa direktang kontrol | Oo, mabilis at tumpak |
| Paghahanap ng mga elemento | Oo, mahusay ang natural na wika | Hindi, kailangan ang eksaktong selector |
| Kontrol sa timing | Hindi, mas hindi napopredict | Oo, buong kontrol sa paghihintay at retries |
| Komplikadong workflows | Oo, humahawak ng mga hindi inaasahang estado ng UI | Hindi, kailangan ng tahasang branching |

### Pinakamahuhusay na Gawi sa Browser-Use

1. Magsimula sa isang agent para sa eksplorasyon at dynamic na pag-navigate.
2. Lumipat sa direktang kontrol ng pahina kapag naging predictable na ang interaksyon.
3. Gumamit ng mga nakaayos na output model upang masiguro na validated at type-safe ang data na nakuha.
4. Magdagdag ng mga delay nang stratehiko pagkatapos ng mga aksyon na nagdudulot ng nakikitang pagbabago sa UI.
5. Kumuha ng mga screenshot habang nagsusubok upang mas madali ang pag-debug ng mga pagkabigo.
6. Asahan ang mga pagbabago sa mga website at magdisenyo ng fallback strategies para sa mga pop-ups at layout shifts.
7. Pagsamahin ang agent at actor patterns upang makuha ang parehong flexibility at precision.

### Mga Safety Guardrails para sa Browser Agents

Ang mga browser agents ay nagpapatakbo sa mga live na website, kaya nangangailangan sila ng mas mahigpit na hangganan kaysa sa script na tumatawag lamang sa kilalang API. Bago lumipat mula sa notebook demo patungo sa totoong workflow, tukuyin ang mga kontrol kung ano ang makikita, makiklik, at maisusumite ng agent.

1. **Iscope ang browsing environment.** Patakbuhin ang agent sa dedicated na browser profile o sandbox, at limitahan ito sa mga domain na kailangan para sa gawain.
2. **Paghiwalayin ang obserbasyon mula sa aksyon.** Hayaan muna ang agent na maghanap, magbasa, at kumuha ng data; kailangan ng tahasang approval bago ito magsumite ng mga form, magpadala ng mensahe, mag-book ng byahe, bumili, mag-delete ng tala, o magbago ng mga setting ng account.
3. **Panatilihing lihim ang mga sikreto mula sa prompts at traces.** Huwag ilagay ang mga password, detalye ng pagbabayad, session cookies, o raw na personal na data sa context ng modelo. Hayaan ang user na mag-autenticate at itago ang sensitibong mga field mula sa mga log.
4. **Tingnan ang nilalaman ng pahina bilang hindi pinagkakatiwalaang input.** Maaaring may mga tagubilin sa website na para sa agent, hindi para sa user. Dapat balewalain ng agent ang mga teksto sa pahina na hinihiling na baguhin ang layunin nito, ipakita ang data, i-disable ang mga safeguard, o bisitahin ang mga di-kaugnay na site.
5. **Gumamit ng mga deterministic na tseke sa mga mapanganib na hakbang.** Patunayan ang kasalukuyang URL, pamagat ng pahina, napiling item, presyo, tatanggap, at buod ng aksyon gamit ang code bago hilingin sa user ang pag-apruba sa huling hakbang.
6. **Magtakda ng budget at stop conditions.** Limitahan ang bilang ng mga aksyon, retries, tabs, at minuto na magagamit ng agent. Itigil kapag ambiguous ang estado ng pahina sa halip na patuloy na mag-click.
7. **Mag-record ng kapaki-pakinabang na ebidensya, hindi lahat.** Panatilihin ang mga buod ng aksyon, timestamps, URL, deskripsyon ng napiling elemento, at reference ng screenshot upang madali i-review ang mga pagkabigo nang hindi inilalagay ang hindi kinakailangang sensitibong nilalaman ng pahina.

Sa halimbawa ng Airbnb, ang ligtas na default ay maghanap ng mga listahan at kunin ang mga presyo. Ang pag-sign in, pakikipag-ugnayan sa host, o pagkompleto ng booking ay dapat na hiwalay na action na pinahintulutan ng user.

### Mga Aplikasyon sa Totoong Mundo

- Pag-book ng paglalakbay at pagsubaybay ng presyo
- Paghahambing ng presyo at pagsusuri ng availability sa e-commerce
- Nakaayos na pagkuha mula sa dynamic na mga website
- Vision-aware UI testing at beripikasyon
- Pagsubaybay at pagbibigay-alam ng website
- Intelligent form filling sa mga multi-step na proseso

## Halimbawa sa Totoong Mundo: Microsoft Project Opal

Ang agent na gagawin mo sa araling ito ay isang maliit, lokal na bersyon ng isang **computer use agent (CUA)** — isang program na nagpapatakbo ng browser sa paraan ng isang tao. Dinadala ng Microsoft ang parehong ideya sa enterprise gamit ang **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, isang kakayahan sa Microsoft 365 Copilot.

Sa Project Opal, inilalarawan mo ang isang gawain at ang agent ang gagawa nito para sa iyo gamit ang **computer use sa isang secure na Windows 365 Cloud PC**, na nagpapatakbo sa mga browser-based na aplikasyon, site, at data ng iyong organisasyon. Nagtatrabaho ito **ng asynchronous sa background**, at maaari mong gabayan ang trabaho o kontrolin ito anumang oras. Mga halimbawa ng trabaho ay:

- Pamamahala ng mga kahilingan sa miyembro ng security group
- Pagkolekta at pag-validate ng audit evidence para sa mga pagsusuri ng pagsunod
- Pagtatangi ng mga IT incident (pag-update ng estado ng ticket, pagtatalaga ng may-ari, pagsasara ng duplicate)
- Pagsasama-sama ng data ng Excel sa isang financial close deck

Ang Opal ay isang kapaki-pakinabang na sanggunian kung ano ang hitsura ng isang **production-grade, mapagkakatiwalaang** computer use agent — at pinapalakas nito ang mga konsepto mula sa mga naunang aralin:

| Konsepto sa kursong ito | Paano inaaplay ito ng Project Opal |
|------------------------|-------------------------------|
| **Human-in-the-loop** (Lesson 06) | Humihinto si Opal para sa login credentials, sensitibong data, o malabong mga tagubilin, at hindi kailanman naglalagay ng password o nagsusumite ng mga form nang walang tahasang kumpirmasyon. Maaari kang *Kumontrol* at *Ibalik ang Kontrol* sa gitna ng gawain. |
| **Mapagkakatiwalaan at secure na agents** (Lessons 06 & 18) | Nagtatakbo sa isolated Windows 365 Cloud PC, browser-only bilang default (hinarangan ang ibang computer access gamit ang Intune), ginagamit ang *iyong* pagkakakilanlan kaya naa-access lang ang pinahihintulutan mo, at nagla-log ng bawat aksyon para sa auditability. |
| **Planning at metacognition** (Lessons 07 & 09) | Gumagawa si Opal ng plano para sa trabaho, pagkatapos pinangangasiwaan ang sariling pangangatwiran sa bawat hakbang at humihinto kung may natuklasang kahina-hinalang aktibidad. |
| **Reusable na kakayahan / tools** (Lesson 04) | Pinapayagan ka ng **Skills** na magsulat ng mga tagubilin para sa mga paulit-ulit na trabaho (imported mula sa `.md` na file o gawa gamit ang Opal) at gamitin muli ang mga ito sa iba’t ibang pag-uusap. |

> **Availability:** Ang Project Opal ay kasalukuyang available sa mga user sa [Frontier early access program](https://adoption.microsoft.com/copilot/frontier-program/) na may Microsoft 365 Copilot subscription, at kailangang kumpletuhin ng iyong administrator ang setup. Dahil ito ay isang experimental na tampok ng Frontier, maaaring magbago ang mga kakayahan sa paglipas ng panahon.

## Karagdagang Mga Mapagkukunan

- [Simulan gamit ang Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integration template](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use actor parameters at pagkuha ng nilalaman](https://docs.browser-use.com/customize/actor/all-parameters)
- [Course Setup](../00-course-setup/README.md)

## Nakaraang Aralin

[Pagsilip sa Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Susunod na Aralin

[Pag-deploy ng Scalable Agents](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->