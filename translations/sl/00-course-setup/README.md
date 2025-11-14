<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86273689a010b5efecaf7fa23104e0fb",
  "translation_date": "2025-11-07T08:50:24+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sl"
}
-->
# Nastavitev tečaja

## Uvod

Ta lekcija bo zajemala, kako zagnati vzorčne kode tega tečaja.

## Pridružite se drugim udeležencem in pridobite pomoč

Preden začnete klonirati svoj repozitorij, se pridružite [Discord kanalu AI Agents For Beginners](https://aka.ms/ai-agents/discord), kjer lahko dobite pomoč pri nastavitvi, postavite vprašanja o tečaju ali se povežete z drugimi udeleženci.

## Klonirajte ali razvejite ta repozitorij

Za začetek prosimo, da klonirate ali razvejite GitHub repozitorij. Tako boste ustvarili svojo različico gradiva tečaja, da boste lahko zagnali, testirali in prilagodili kodo!

To lahko storite s klikom na povezavo za <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">razvejitev repozitorija</a>.

Zdaj bi morali imeti svojo razvejano različico tega tečaja na naslednji povezavi:

![Razvejan repozitorij](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.sl.png)

### Plitvo kloniranje (priporočeno za delavnice / Codespaces)

  >Celoten repozitorij je lahko velik (~3 GB), če prenesete celotno zgodovino in vse datoteke. Če se udeležujete le delavnice ali potrebujete le nekaj map lekcij, plitvo kloniranje (ali redko kloniranje) prepreči večino tega prenosa s skrajšanjem zgodovine in/ali preskakovanjem datotek.

#### Hitro plitvo kloniranje — minimalna zgodovina, vse datoteke

Zamenjajte `<your-username>` v spodnjih ukazih z URL-jem vaše razvejane različice (ali z URL-jem izvornega repozitorija, če to raje).

Za kloniranje samo najnovejše zgodovine (majhen prenos):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Za kloniranje določene veje:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Delno (redko) kloniranje — minimalne datoteke + samo izbrane mape

To uporablja delno kloniranje in redko preverjanje (zahteva Git 2.25+ in priporočeno sodobno Git različico s podporo za delno kloniranje):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Premaknite se v mapo repozitorija:

```bash|powershell
cd ai-agents-for-beginners
```

Nato določite, katere mape želite (spodnji primer prikazuje dve mapi):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po kloniranju in preverjanju datotek, če potrebujete le datoteke in želite sprostiti prostor (brez zgodovine Git), prosimo, izbrišite metapodatke repozitorija (💀nepovratno — izgubili boste vse funkcionalnosti Git: brez commitov, pullov, pushov ali dostopa do zgodovine).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Uporaba GitHub Codespaces (priporočeno za izogibanje lokalnim velikim prenosom)

- Ustvarite nov Codespace za ta repozitorij prek [GitHub uporabniškega vmesnika](https://github.com/codespaces).  

- V terminalu na novo ustvarjenega Codespace-a zaženite enega od ukazov za plitvo/redko kloniranje zgoraj, da v delovni prostor Codespace-a prenesete samo mape lekcij, ki jih potrebujete.
- Opcijsko: po kloniranju znotraj Codespaces odstranite .git za sprostitev dodatnega prostora (glejte zgornje ukaze za odstranitev).
- Opomba: Če raje odprete repozitorij neposredno v Codespaces (brez dodatnega kloniranja), bodite pozorni, da bo Codespaces zgradil okolje devcontainer in morda še vedno zagotovil več, kot potrebujete. Kloniranje plitke kopije znotraj svežega Codespace-a vam daje več nadzora nad uporabo diska.

#### Nasveti

- Vedno zamenjajte URL za kloniranje z vašo razvejano različico, če želite urejati/commitat.
- Če kasneje potrebujete več zgodovine ali datotek, jih lahko pridobite ali prilagodite redko preverjanje, da vključite dodatne mape.

## Zagon kode

Ta tečaj ponuja serijo Jupyter Notebookov, ki jih lahko zaženete za praktično izkušnjo pri gradnji AI agentov.

Vzorčne kode uporabljajo:

**Zahteva GitHub račun - Brezplačno**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Označeno kot (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Označeno kot (autogen.ipynb)

**Zahteva naročnino na Azure**:
3) Azure AI Foundry + Azure AI Agent Service. Označeno kot (azureaiagent.ipynb)

Spodbujamo vas, da preizkusite vse tri vrste primerov, da vidite, kateri vam najbolj ustreza.

Katero koli možnost izberete, bo določila, katere korake za nastavitev morate slediti spodaj:

## Zahteve

- Python 3.12+
  - **NOTE**: Če nimate nameščenega Python3.12, poskrbite, da ga namestite. Nato ustvarite svoj venv z uporabo python3.12, da zagotovite pravilne različice, nameščene iz datoteke requirements.txt.
  
    >Primer

    Ustvarite mapo za Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    Nato aktivirajte venv okolje za:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Za vzorčne kode, ki uporabljajo .NET, poskrbite, da namestite [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ali novejši. Nato preverite nameščeno različico .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- GitHub račun - Za dostop do GitHub Models Marketplace
- Naročnina na Azure - Za dostop do Azure AI Foundry
- Azure AI Foundry račun - Za dostop do Azure AI Agent Service

V korenskem direktoriju tega repozitorija smo vključili datoteko `requirements.txt`, ki vsebuje vse potrebne Python pakete za zagon vzorčnih kod.

Namestite jih lahko z naslednjim ukazom v terminalu v korenskem direktoriju repozitorija:

```bash|powershell
pip install -r requirements.txt
```

Priporočamo ustvarjanje virtualnega okolja Python, da se izognete konfliktom in težavam.

## Nastavitev VSCode

Poskrbite, da uporabljate pravo različico Python v VSCode.

![slika](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavitev za vzorce, ki uporabljajo GitHub modele 

### Korak 1: Pridobite svoj GitHub osebni dostopni žeton (PAT)

Ta tečaj uporablja GitHub Models Marketplace, ki omogoča brezplačen dostop do velikih jezikovnih modelov (LLM), ki jih boste uporabili za gradnjo AI agentov.

Za uporabo GitHub modelov boste morali ustvariti [GitHub osebni dostopni žeton](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

To lahko storite tako, da obiščete <a href="https://github.com/settings/personal-access-tokens" target="_blank">nastavitve osebnih dostopnih žetonov</a> v svojem GitHub računu.

Prosimo, da sledite [načelu najmanjše privilegiranosti](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) pri ustvarjanju žetona. To pomeni, da žetonu dodelite le dovoljenja, ki jih potrebuje za zagon vzorčnih kod v tem tečaju.

1. Na levi strani zaslona izberite možnost `Fine-grained tokens` z navigacijo do **Developer settings**.

   ![Nastavitve razvijalca](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.sl.png)

   Nato izberite `Generate new token`.

   ![Ustvari žeton](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.sl.png)

2. Vnesite opisno ime za svoj žeton, ki odraža njegov namen, da ga boste kasneje lažje prepoznali.

    🔐 Priporočilo za trajanje žetona

    Priporočeno trajanje: 30 dni
    Za bolj varno držo lahko izberete krajše obdobje—na primer 7 dni 🛡️
    To je odličen način za postavitev osebnega cilja in dokončanje tečaja, medtem ko je vaša učna motivacija visoka 🚀.

    ![Ime žetona in datum poteka](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.sl.png)

3. Omejite obseg žetona na svojo razvejano različico tega repozitorija.

    ![Omejitev obsega na razvejano različico repozitorija](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.sl.png)

4. Omejite dovoljenja žetona: Pod **Permissions**, kliknite zavihek **Account** in nato gumb "+ Add permissions". Prikaže se spustni meni. Prosimo, poiščite **Models** in označite polje zanj.

    ![Dodaj dovoljenje za modele](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.sl.png)

5. Preden ustvarite žeton, preverite potrebna dovoljenja. ![Preverite dovoljenja](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.sl.png)

6. Preden ustvarite žeton, poskrbite, da ga boste shranili na varno mesto, kot je trezor za gesla, saj ga po ustvarjanju ne boste več videli. ![Varno shranite žeton](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.sl.png)

Kopirajte svoj nov žeton, ki ste ga pravkar ustvarili. Zdaj ga boste dodali v svojo `.env` datoteko, vključeno v ta tečaj.

### Korak 2: Ustvarite svojo `.env` datoteko

Za ustvarjanje `.env` datoteke zaženite naslednji ukaz v terminalu.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

To bo kopiralo primer datoteke in ustvarilo `.env` v vašem direktoriju, kjer izpolnite vrednosti za okoljske spremenljivke.

S kopiranim žetonom odprite `.env` datoteko v svojem najljubšem urejevalniku besedila in prilepite žeton v polje `GITHUB_TOKEN`.

![Polje za GitHub žeton](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.sl.png)

Zdaj bi morali biti sposobni zagnati vzorčne kode tega tečaja.

## Nastavitev za vzorce, ki uporabljajo Azure AI Foundry in Azure AI Agent Service

### Korak 1: Pridobite končno točko svojega Azure projekta

Sledite korakom za ustvarjanje vozlišča in projekta v Azure AI Foundry, ki jih najdete tukaj: [Pregled virov vozlišča](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)

Ko ustvarite svoj projekt, boste morali pridobiti povezovalni niz za svoj projekt.

To lahko storite tako, da obiščete stran **Overview** svojega projekta v portalu Azure AI Foundry.

![Povezovalni niz projekta](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.sl.png)

### Korak 2: Ustvarite svojo `.env` datoteko

Za ustvarjanje `.env` datoteke zaženite naslednji ukaz v terminalu.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

To bo kopiralo primer datoteke in ustvarilo `.env` v vašem direktoriju, kjer izpolnite vrednosti za okoljske spremenljivke.

S kopiranim žetonom odprite `.env` datoteko v svojem najljubšem urejevalniku besedila in prilepite žeton v polje `PROJECT_ENDPOINT`.

### Korak 3: Prijavite se v Azure

Kot varnostno najboljšo prakso bomo uporabili [avtentikacijo brez ključev](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) za avtentikacijo v Azure OpenAI z Microsoft Entra ID. 

Nato odprite terminal in zaženite `az login --use-device-code`, da se prijavite v svoj Azure račun.

Ko se prijavite, v terminalu izberite svojo naročnino.

## Dodatne okoljske spremenljivke - Azure Search in Azure OpenAI 

Za lekcijo Agentic RAG - Lekcija 5 - so vključeni vzorci, ki uporabljajo Azure Search in Azure OpenAI.

Če želite zagnati te vzorce, boste morali dodati naslednje okoljske spremenljivke v svojo `.env` datoteko:

### Pregledna stran (Projekt)

- `AZURE_SUBSCRIPTION_ID` - Preverite **Podrobnosti projekta** na strani **Overview** vašega projekta.

- `AZURE_AI_PROJECT_NAME` - Poglejte na vrh strani **Overview** vašega projekta.

- `AZURE_OPENAI_SERVICE` - Poiščite to na zavihku **Included capabilities** za **Azure OpenAI Service** na strani **Overview**.

### Center za upravljanje

- `AZURE_OPENAI_RESOURCE_GROUP` - Pojdite na **Lastnosti projekta** na strani **Overview** v **Management Center**.

- `GLOBAL_LLM_SERVICE` - Pod **Connected resources**, poiščite ime povezave **Azure AI Services**. Če ni navedeno, preverite **Azure portal** pod svojo skupino virov za ime vira AI Services.

### Stran z modeli + končnimi točkami

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Izberite svoj model za vdelavo (npr. `text-embedding-ada-002`) in zabeležite **Deployment name** iz podrobnosti modela.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Izberite svoj model za klepet (npr. `gpt-4o-mini`) in zabeležite **Deployment name** iz podrobnosti modela.

### Azure portal

- `AZURE_OPENAI_ENDPOINT` - Poiščite **Azure AI services**, kliknite nanj, nato pojdite na **Resource Management**, **Keys and Endpoint**, pomaknite se navzdol do "Azure OpenAI endpoints" in kopirajte tistega, ki pravi "Language APIs".

- `AZURE_OPENAI_API_KEY` - Na istem zaslonu kopirajte KLJUČ 1 ali KLJUČ 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Poiščite svoj **Azure AI Search** vir, kliknite nanj in si oglejte **Overview**.

- `AZURE_SEARCH_API_KEY` - Nato pojdite na **Settings** in nato **Keys**, da kopirate primarni ali sekundarni skrbniški ključ.

### Zunanja spletna stran

- `AZURE_OPENAI_API_VERSION` - Obiščite stran [API različica življenjskega cikla](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) pod **Latest GA API release**.

### Nastavitev avtentikacije brez ključev

Namesto da bi trdo kodirali svoje poverilnice, bomo uporabili povezavo brez ključev z Azure OpenAI. Za to bomo uvozili `DefaultAzureCredential` in kasneje poklicali funkcijo `DefaultAzureCredential`, da pridobimo poverilnico.

```python
# Python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Ste se kje zataknili?
Če imate kakršne koli težave pri izvajanju te nastavitve, se pridružite našemu <a href="https://discord.gg/kzRShWzttr" target="_blank">Discordu skupnosti Azure AI</a> ali <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ustvarite težavo</a>.

## Naslednja lekcija

Sedaj ste pripravljeni za zagon kode tega tečaja. Veselo raziskovanje sveta AI agentov!

[Uvod v AI agente in primere uporabe agentov](../01-intro-to-ai-agents/README.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.