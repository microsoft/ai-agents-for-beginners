# Paggawa ng Mga Ahente sa Paggamit ng Kompyuter (CUA)

Ang mga ahente sa paggamit ng kompyuter ay maaaring makipag-ugnayan sa mga website sa parehong paraan na ginagawa ng tao: sa pamamagitan ng pagbubukas ng browser, pagsiyasat sa pahina, at paggawa ng susunod na pinakamahusay na aksyon base sa kanilang nakikita. Sa araling ito, gagawa ka ng isang ahente ng awtomasyon ng browser na naghahanap sa Airbnb, kumukuha ng nakaayos na datos ng listahan, at tinutukoy ang pinakamurang pananatili sa Stockholm.

Pinagsasama-sama ng araling ito ang Browser-Use para sa AI-driven na pag-navigate, Playwright at Chrome DevTools Protocol (CDP) para sa kontrol ng browser, Azure OpenAI para sa vision-enabled na pangangatwiran, at Pydantic para sa nakaayos na pagkuha.

## Panimula

Tatalakayin sa araling ito ang:

- Pag-unawa kung kailan mas angkop ang mga ahente sa paggamit ng kompyuter kaysa API-only na awtomasyon
- Pagsasama ng Browser-Use sa Playwright at CDP para sa maasahang pamamahala ng lifecycle ng browser
- Paggamit ng Azure OpenAI vision at nakaayos na output ng Pydantic upang kunin ang datos ng listahan mula sa mga dynamic na web page
- Pagpapasya kung kailan gagamit ng agent-first, actor-first, o hybrid na workflow ng awtomasyon ng browser

## Mga Layunin ng Pagkatuto

Pagkatapos makumpleto ang araling ito, malalaman mo kung paano:

- I-configure ang Browser-Use gamit ang Azure OpenAI at Playwright
- Gumawa ng workflow ng awtomasyon ng browser na nag-navigate sa totoong website at humaharap sa mga dynamic na UI element
- Kunin ang mga tinype na resulta mula sa nakikitang nilalaman ng pahina at gawing downstream na business logic
- Pumili sa pagitan ng agent at actor patterns base sa kung gaano kapredictable ang gawain sa browser

## Halimbawa ng Code

Kasama sa araling ito ang isang notebook tutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Nagpapasimula ng sesyon ng Chrome gamit ang CDP, naghahanap sa Airbnb para sa mga listahan ng Stockholm, kumukuha ng mga presyo gamit ang Browser-Use vision, at ibinabalik ang pinakamurang opsyon bilang nakaayos na datos.

## Mga Kinakailangan

- Python 3.12+
- Azure OpenAI deployment na naka-configure sa iyong kapaligiran
- Chrome o Chromium na naka-install nang lokal
- Mga dependency ng Playwright na na-install
- Pangunahing pamilyar sa async Python

## Setup

I-install ang mga package na ginamit sa notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

I-set ang mga environment variable ng Azure OpenAI na ginagamit ng notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opsyonal: awtomatikong ginagamit ang pinakabagong bersyon ng API kapag hindi ipinasa
AZURE_OPENAI_API_VERSION=...
```

## Pangkalahatang-ideya ng Arkitektura

Ipinapakita ng notebook ang isang hybrid na workflow ng awtomasyon ng browser:

1. Sinisimulan ang Chrome na may CDP na naka-enable para sabay na magamit ng Playwright at Browser-Use ang parehong session ng browser.
2. Isang Browser-Use agent ang humahawak sa mga open-ended na gawain ng pag-navigate tulad ng pagbubukas ng Airbnb, pagtanggi sa mga pop-up, at paghahanap ng Stockholm.
3. Sinusuri ang aktibong pahina gamit ang isang nakaayos na Pydantic schema upang makuha ang mga pamagat ng listahan, mga presyo kada gabi, mga rating, at mga URL.
4. Kinukumpara ng lohika ng Python ang mga nakuha na listahan at itinatampok ang pinakamurang resulta.

Pinananatili ng pamamaraan na ito ang flexible, vision-based reasoning na mahusay sa Browser-Use habang nagbibigay pa rin ng deterministic na kontrol ng browser kapag kailangan.

## Pangunahing Mga Aral at Pinakamahuhusay na Gawi

### Kailan Gagamit ng Agent vs Actor

| Senaryo | Gamitin ang Agent | Gamitin ang Actor |
|----------|----------------|---------------|
| Dynamic na mga layout | Oo, kayang umangkop ng AI sa mga pagbabago sa pahina | Hindi, maaaring masira ang mga marupok na selector |
| Kilalang estruktura | Hindi, mas mabagal ang agent kaysa sa direktang kontrol | Oo, mabilis at tumpak |
| Paghahanap ng mga elemento | Oo, mahusay ang natural na wika | Hindi, kailangan ng tumpak na selector |
| Kontrol sa timing | Hindi, hindi gaanong predictible | Oo, kumpletong kontrol sa paghihintay at pag-uulit |
| Komplikadong workflow | Oo, humahawak ng mga hindi inaasahang estado ng UI | Hindi, kailangan ng tahasang branching |

### Pinakamahuhusay na Gawi sa Browser-Use

1. Magsimula sa isang agent para sa eksplorasyon at dynamic na pag-navigate.
2. Lumipat sa direktang kontrol ng pahina kapag predictable na ang interaksyon.
3. Gumamit ng nakaayos na mga output model upang mapatunayan at maging type-safe ang nakuha na datos.
4. Magdagdag ng mga delay nang maayos pagkatapos ng mga aksyong nagpapahiwatig ng pagbabago sa UI.
5. Kumuha ng mga screenshot habang nag-iiterate upang maging mas madali ang pag-debug ng mga pagkabigo.
6. Asahan na magbabago ang mga website at magdisenyo ng mga fallback na estratehiya para sa pop-ups at mga layout shift.
7. Pagsamahin ang mga agent at actor pattern upang makuha ang parehong flexibility at precision.

### Mga Pananggalang sa Kaligtasan para sa Mga Ahente ng Browser

Ang mga browser agent ay gumagana sa mga live na website, kaya't kailangan nila ng mas mahigpit na hangganan kaysa sa script na tumatawag lang ng kilalang API. Bago lumipat mula sa notebook demo patungo sa totoong workflow, tukuyin ang mga kontrol sa paligid ng kung ano ang maaaring makita, i-click, at isubmit ng agent.

1. **Limitahan ang kapaligiran sa pag-browse.** Patakbuhin ang agent sa isang dedikadong profile ng browser o sandbox, at limitahan ito sa mga domain na kinakailangan para sa gawain.
2. **Paghiwalayin ang pagmamasid mula sa aksyon.** Hayaan munang maghanap, magbasa, at kumuha ng datos ang agent; kailangan ng tahasang apruba bago magsumite ng mga form, magpadala ng mensahe, mag-book ng biyahe, gumawa ng mga pagbili, magtanggal ng rekord, o magbago ng mga setting ng account.
3. **Itago ang mga sikreto mula sa mga prompt at trace.** Huwag ilagay ang mga password, detalye ng pagbabayad, session cookies, o mga raw na personal na datos sa konteksto ng modelo. Hayaan ang user ang humawak sa authentication at i-redact ang mga sensitibong field mula sa mga log.
4. **Turingin ang nilalaman ng pahina bilang hindi pinagkakatiwalaang input.** Maaaring may mga instruksyon ang website na para sa agent, hindi para sa user. Dapat balewalain ng agent ang text sa pahina na nag-uutos na baguhin ang layunin, ilantad ang datos, i-disable ang mga pananggalang, o bisitahin ang mga hindi kaugnay na site.
5. **Gumamit ng deterministic checks sa mga mapanganib na hakbang.** Patunayan ang kasalukuyang URL, pamagat ng pahina, piniling item, presyo, tatanggap, at buod ng aksyon gamit ang code bago hingin ang apruba ng user para sa huling hakbang.
6. **Magtakda ng mga budget at stop condition.** Limitahan ang bilang ng aksyon, pag-uulit, tab, at minuto na maaaring gamitin ng agent. Huminto kapag malabo na ang estado ng pahina imbes na patuloy na mag-click.
7. **Itala ang mahalagang ebidensya, hindi lahat.** Itago ang mga buod ng aksyon, timestamp, URL, deskripsyon ng piniling elemento, at mga sanggunian sa screenshot upang masuri ang mga pagkabigo nang hindi nag-iimbak ng hindi kinakailangang sensitibong nilalaman ng pahina.

Sa sample ng Airbnb, ang ligtas na default ay maghanap ng mga listahan at kunin ang mga presyo. Ang pag-sign in, pakikipag-ugnayan sa host, o pagkumpleto ng booking ay dapat na isang hiwalay na aksyong inaprubahan ng user.

### Mga Aplikasyong Totoong Mundo

- Pag-book ng biyahe at pagmamanman ng presyo
- Paghahambing ng presyo at pagsuri ng availability sa e-commerce
- Nakaayos na pagkuha mula sa mga dynamic na website
- Vision-aware UI testing at beripikasyon
- Pagsubaybay sa website at alerto
- Intelihenteng pag-fill ng form sa mga multi-step na daloy

## Halimbawa sa Totoong Mundo: Microsoft Project Opal

Ang ahenteng ginagawa mo sa araling ito ay isang maliit, lokal na bersyon ng isang **computer use agent (CUA)** — isang programa na nagmamaneho ng browser sa paraang ginagawa ng tao. Dinadala ng Microsoft ang parehong ideya sa enterprise gamit ang **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, isang kakayahan sa Microsoft 365 Copilot.

Sa Project Opal, inilalarawan mo ang isang gawain at ang ahente ay gumagana sa iyong ngalan gamit ang **computer use sa isang secure na Windows 365 Cloud PC**, na nagpapatakbo sa mga browser-based na aplikasyon, site, at datos ng iyong organisasyon. Ito ay gumagana **asynchronously sa background**, at maaari mong gabayan ang trabaho o kontrolin ito anumang oras. Ilang halimbawa ng trabaho ay:

- Pamamahala sa mga kahilingan sa membership ng security group
- Pangangalap at pag-verify ng audit evidence para sa compliance reviews
- Triaging ng mga IT incident (pag-update ng status ng ticket, pagtatalaga ng mga may-ari, pagsasara ng mga duplicate)
- Pag-compila ng datos sa Excel para sa financial close deck

Ang Opal ay isang kapaki-pakinabang na sanggunian para sa kung ano ang hitsura ng isang **production-grade, trustworthy** computer use agent — at pinagtitibay nito ang mga konsepto mula sa mga naunang aralin:

| Konsepto sa kursong ito | Paano ito inilalapat ng Project Opal |
|-----------------------|--------------------------------|
| **Human-in-the-loop** (Aralin 06) | Humihinto ang Opal para sa login credentials, sensitibong datos, o malabong instruksyon, at hindi kailanman naglalagay ng mga password o nagsusumite ng mga form nang walang tahasang kumpirmasyon. Maaari kang *Kunin ang Kontrol* at *Ibalik ang Kontrol* sa gitna ng gawain. |
| **Mapagkakatiwalaan at secure na mga ahente** (Aralin 06 at 18) | Tumakbo sa isang hiwalay na Windows 365 Cloud PC, browser-only bilang default (naharang ang iba pang computer access, ipinatutupad via Intune), ginagamit ang *iyong* pagkakakilanlan kaya naa-access lang nito ang pinapayagan, at nagla-log ng bawat aksyon para sa auditability. |
| **Pagpaplano at metacognition** (Aralin 07 at 09) | Gumagawa muna ang Opal ng plano para sa trabaho, saka mino-monitor ang sariling pangangatwiran sa bawat hakbang at humihinto kapag nakakita ng kahina-hinalang gawain. |
| **Reusableng kakayahan / kasangkapan** (Aralin 04) | Pinahihintulutan ka ng **Skills** na magsulat ng mga instruksyon para sa mga paulit-ulit na trabaho (inarere-import mula sa `.md` file o nililikha gamit ang Opal) at gamitin ito sa iba't ibang usapan. |

> **Availability:** Ang Project Opal ay kasalukuyang available sa mga gumagamit sa [Frontier early access program](https://adoption.microsoft.com/copilot/frontier-program/) na may Microsoft 365 Copilot subscription, at kailangang matapos ng iyong administrator ang setup. Dahil ito ay isang eksperimentong tampok ng Frontier, maaaring magbago ang mga kakayahan sa paglipas ng panahon.

## Pagsusulit sa Kaalaman

Subukan ang iyong pag-unawa bago lumipat sa susunod na aralin.

**1. Kailan mas angkop ang isang browser-based computer use agent kaysa sa isang API-only workflow?**

<details>
<summary>Sagot</summary>

Gumamit ng browser agent kapag nakadepende ang gawain sa kung ano ang nakikita sa web UI, hindi inihahayag ng site ang kinakailangang API, o madalas magbago ang pahina kaya't magiging marupok ang fixed API o selector logic. Kung mayroong stable na API para sa parehong gawain, mas piliin ang API dahil karaniwan itong mas mabilis, mas madaling subukan, at mas madaling siguraduhin.
</details>

**2. Sa isang hybrid workflow, aling mga bahagi ang dapat hawakan ng agent at alin ang dapat hawakan ng direktang code ng Playwright?**

<details>
<summary>Sagot</summary>

Hayaan ang agent ang humawak sa open-ended na pag-navigate at mga dynamic na estado ng UI, tulad ng paghahanap ng tamang pahina o pagtanggi sa hindi inaasahang mga pop-up. Lumipat sa direktang kontrol ng Playwright kapag kilala na ang estruktura ng pahina at kailangan ang precision, retries, waits, o deterministic validation sa aksyon.
</details>

**3. Nakakita ang sample ng Airbnb ng listahan na maaaring gustuhin ng user na i-book. Ano ang dapat mangyari bago mag-sign in, makipag-ugnayan sa host, o tapusin ang booking?**

<details>
<summary>Sagot</summary>

Dapat huminto ang workflow at hingin ang tahasang apruba ng user. Bago humingi, dapat ipakita ang malinaw na buod ng piniling listahan, kasalukuyang URL, presyo, mga petsa, at intensyon ng aksyon. Maaaring autonomous ang paghahanap at pagkuha ng mga presyo; ang pag-access sa account, mga mensahe, pagbili, at booking ay dapat aprubahan ng user.
</details>

**4. Sinasabi ng isang web page sa agent na balewalain ang orihinal nitong instruksyon, bisitahin ang ibang site, at ilantad ang mga nakalistang credentials. Paano dapat tratuhin ng agent ang tekstong iyon?**

<details>
<summary>Sagot</summary>

Tratuhin ito bilang hindi pinagkakatiwalaang nilalaman ng pahina, hindi bilang instruksyon ng developer o user. Dapat manatili ang agent sa loob ng pinapayagang domain at saklaw ng gawain, tanggihan ang paglabas ng mga sikreto, at iwasang sundan ang text sa pahina na nagbabago ng layunin, nag-disable ng mga pananggalang, o nagpadadala sa hindi kaugnay na mga site.
</details>

**5. Anong ebidensya ang kapaki-pakinabang itago kapag tumatakbo ang browser agent, at ano ang dapat iwasan?**

<details>
<summary>Sagot</summary>

Itago ang mga buod ng aksyon, mga timestamp, mga URL, mga deskripsyon ng piniling elemento, mga resulta ng pag-validate, at mga sanggunian ng screenshot upang masuri ang takbo. Iwasang mag-imbak ng mga password, detalye ng pagbabayad, session cookies, raw personal na datos, o buong nilalaman ng pahina maliban kung may partikular na dahilan para sa retention at privacy.
</details>

## Karagdagang Mga Sanggunian

- [Simulan ang Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integration template](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use actor parameters at pagkuha ng nilalaman](https://docs.browser-use.com/customize/actor/all-parameters)
- [Course Setup](../00-course-setup/README.md)

## Nakaraang Aralin

[Pagsilip sa Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Susunod na Aralin

[Pagdeploy ng Scalable Agents](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->