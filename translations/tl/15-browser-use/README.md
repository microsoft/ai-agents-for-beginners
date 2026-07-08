# Paggawa ng Mga Ahente sa Paggamit ng Kompyuter (CUA)

Ang mga ahente sa paggamit ng kompyuter ay maaaring makipag-ugnayan sa mga website sa parehas na paraan ng isang tao: sa pamamagitan ng pagbukas ng browser, pagsisiyasat sa pahina, at paggawa ng susunod na pinakamainam na aksyon mula sa kanilang nakita. Sa araling ito, gagawa ka ng isang ahente ng browser automation na naghahanap sa Airbnb, kumukuha ng nakaayos na datos ng listahan, at tinutukoy ang pinakamurang pampalipas-oras sa Stockholm.

Pinagsasama ng araling ito ang Browser-Use para sa AI-na pinapatakbong pag-navigate, Playwright at Chrome DevTools Protocol (CDP) para sa kontrol ng browser, Azure OpenAI para sa vision-enabled na pangangatwiran, at Pydantic para sa nakaayos na pagkuha.

## Panimula

Tatalakayin sa araling ito ang:

- Pag-unawa kung kailan mas angkop ang mga ahente sa paggamit ng kompyuter kaysa sa automation na API-only
- Pagsasama ng Browser-Use kasama ang Playwright at CDP para sa maasahang pamamahala ng lifecycle ng browser
- Paggamit ng Azure OpenAI vision at nakaayos na output ng Pydantic para kumuha ng datos ng listahan mula sa mga dynamic na web page
- Pagpapasya kung kailan gagamit ng agent-first, actor-first, o hybrid na workflow sa browser automation

## Mga Layunin sa Pag-aaral

Pagkatapos makumpleto ang araling ito, malalaman mo kung paano:

- I-configure ang Browser-Use kasama ang Azure OpenAI at Playwright
- Bumuo ng isang browser automation workflow na nagba-browse sa isang totoong website at humahawak ng mga dynamic na UI element
- Mag-extract ng mga typed na resulta mula sa nakikitang nilalaman ng pahina at gawing downstream na negosyo lohika
- Pumili sa pagitan ng mga pattern ng agent at actor batay sa kung gaano predictable ang gawain sa browser

## Halimbawa ng Code

Kasama sa araling ito ang isang notebook tutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Naglulunsad ng isang session ng Chrome sa CDP, naghahanap sa Airbnb para sa mga listahan sa Stockholm, kumukuha ng mga presyo gamit ang Browser-Use vision, at ibinabalik ang pinakamurang opsyon bilang nakaayos na datos.

## Mga Kinakailangan

- Python 3.12+
- Azure OpenAI deployment na naka-configure sa iyong kapaligiran
- Chrome o Chromium na naka-install nang lokal
- Mga dependency ng Playwright na naka-install
- Pangunahing kaalaman sa async Python

## Pagsisimula

I-install ang mga package na ginamit sa notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Itakda ang mga Azure OpenAI environment variables na ginagamit ng notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opsyonal: awtomatikong ginagamit ang pinakabagong bersyon ng API kapag hindi inilagay
AZURE_OPENAI_API_VERSION=...
```

## Pangkalahatang-ideya ng Arkitektura

Ipinapakita ng notebook ang isang hybrid na workflow ng browser automation:

1. Nagsisimula ang Chrome na may CDP na naka-enable upang parehong magamit ng Playwright at Browser-Use ang parehong browser session.
2. Isang Browser-Use agent ang humahawak sa mga open-ended navigation task gaya ng pagbukas ng Airbnb, pagtanggi sa mga pop-up, at paghahanap sa Stockholm.
3. Sinusuri ang aktibong pahina gamit ang nakaayos na Pydantic schema para kumuha ng mga pamagat ng listahan, presyo kada gabi, rating, at mga URL.
4. Kinukumpara ng Python logic ang mga nakuha na listahan at pina-highlight ang pinakamurang resulta.

Pinananatili ng pamamaraang ito ang flexible, vision-based reasoning na mahusay sa Browser-Use habang nagbibigay pa rin ng deterministic na kontrol sa browser kapag kinakailangan.

## Pangunahing Mga Aral at Mga Pinakamahusay na Gawain

### Kailan Gagamit ng Agent kumpara sa Actor

| Sitwasyon | Gamitin ang Agent | Gamitin ang Actor |
|----------|-----------------|-----------------|
| Dynamic layouts | Oo, kaya ng AI na umangkop sa mga pagbabago sa pahina | Hindi, maaaring masira ang mga madaling masira na selector |
| Kilalang estruktura | Hindi, mas mabagal ang agent kaysa direktang kontrol | Oo, mabilis at tumpak |
| Paghahanap ng mga elemento | Oo, mabisa ang natural na wika | Hindi, kailangan ng eksaktong selector |
| Kontrol sa timing | Hindi, hindi gaanong predictable | Oo, lubusang kontrol sa paghihintay at pag-uulit |
| Masalimuot na workflow | Oo, humahawak sa mga hindi inaasahang estado ng UI | Hindi, nangangailangan ng tahasang pag-branch |

### Pinakamahusay na Gawain para sa Browser-Use

1. Magsimula sa isang agent para sa eksplorasyon at dynamic na pag-navigate.
2. Lumipat sa direktang kontrol ng pahina kapag naging predictable na ang interaksyon.
3. Gumamit ng mga nakaayos na output model upang masigurong validated at type-safe ang nakuha na data.
4. Magdagdag ng mga delay nang maayos pagkatapos ng mga aksyon na nagpap-trigger ng nakikitang pagbabago sa UI.
5. Kumuha ng mga screenshot habang inuulit-ulit para madali ang pag-debug ng mga pagkakamali.
6. Asahan ang pagbabago ng mga website at magdisenyo ng mga fallback na estratehiya para sa mga pop-up at pagbabago sa layout.
7. Pagsamahin ang mga pattern ng agent at actor para makuha ang parehong flexibility at katumpakan.

### Mga Aplikasyon sa Totoong Mundo

- Pag-book ng biyahe at pagmamanman ng presyo
- Paghahambing ng presyo at pagcheck ng availability sa e-commerce
- Nakaayos na pagkuha mula sa mga dynamic na website
- Vision-aware na UI testing at beripikasyon
- Pagmo-monitor ng website at alerto
- Matalinong pagpuno ng mga form sa maraming-hakbang na proseso

## Halimbawa sa Totoong Mundo: Microsoft Project Opal

Ang ahenteng binubuo mo sa araling ito ay isang maliit, lokal na bersyon ng isang **computer use agent (CUA)** — isang programa na nagpapatakbo ng browser gaya ng isang tao. Dinadala ng Microsoft ang parehong ideya na ito sa enterprise gamit ang **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, isang kakayahan sa Microsoft 365 Copilot.

Sa Project Opal, inilalarawan mo ang isang gawain at gumagana ang ahente sa iyong ngalan gamit ang **computer use sa isang secure na Windows 365 Cloud PC**, na nagpapatakbo sa mga browser-based na aplikasyon, site, at datos ng iyong organisasyon. Ito ay gumagana **nang asynchronous sa background**, at maaari mong gabayan ang gawain o kontrolin ito anumang oras. Halimbawa ng mga trabaho ang:

- Pamamahala ng mga kahilingan sa membership ng security group
- Pangangalap at pag-validate ng audit evidence para sa mga compliance review
- Pagtugon sa mga IT incident (pag-update ng status ng tiket, pagtatalaga ng mga may-ari, pagsasara ng mga duplicate)
- Paglikom ng Excel data para sa financial close deck

Ang Opal ay isang kapaki-pakinabang na sanggunian para sa hitsura ng isang **production-grade, mapagkakatiwalaang** computer use agent — at pinatitibay nito ang mga konsepto mula sa mga naunang aralin:

| Konsepto sa kursong ito | Paano ito inilalapat ng Project Opal |
|------------------------|------------------------------|
| **Human-in-the-loop** (Aralin 06) | Humihinto ang Opal para sa login credentials, sensitibong datos, o malabong mga tagubilin, at hindi kailanman pumapasok ng mga password o nagsusumite ng mga form nang walang tahasang kumpirmasyon. Maaari kang *Kulutin ang Kontrol* at *Ibalik ang Kontrol* habang nasa kalagitnaan ng gawain. |
| **Mapagkakatiwalaan at ligtas na mga ahente** (Aralin 06 at 18) | Naka-run sa isang isolated Windows 365 Cloud PC, browser-only bilang default (ang ibang computer access ay naka-block, pini-prisinteng sa pamamagitan ng Intune), gamit ang *inyong* identidad kaya tanging ang mga awtorisadong access lang ang nasasaklaw, at nagla-log ng bawat aksyon para sa audit. |
| **Pagpaplano at metacognition** (Aralin 07 at 09) | Gumagawa muna ang Opal ng plano para sa gawain, pagkatapos ay inoobserbahan ang sariling pangangatwiran sa bawat hakbang at humihinto kung may hinala sa kahina-hinalang aktibidad. |
| **Muling nagagamit na kakayahan/kagamitan** (Aralin 04) | Pinapayagan ka ng **Skills** na magsulat ng mga tagubilin para sa mga paulit-ulit na gawain (ini-import mula sa `.md` file o ginawang Opal) at muling gamitin ito sa iba't ibang pag-uusap. |

> **Kamag-anakan:** Ang Project Opal ay kasalukuyang available sa mga user sa [Frontier early access program](https://adoption.microsoft.com/copilot/frontier-program/) na may Microsoft 365 Copilot subscription, at kailangang kumpletuhin ng iyong administrator ang setup. Dahil isang experimental na Frontier feature ito, maaaring magbago ang mga kakayahan dito sa pagdaan ng panahon.

## Karagdagang Mga Pinagkukunan

- [Magsimula sa Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integration template](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Mga parameter ng Browser-Use actor at pagkuha ng nilalaman](https://docs.browser-use.com/customize/actor/all-parameters)
- [Pagsisimula ng Kurso](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->