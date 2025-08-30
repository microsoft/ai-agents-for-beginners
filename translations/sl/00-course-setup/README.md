<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c55b973b1562abf5aadf6a4028265ac5",
  "translation_date": "2025-08-30T09:20:44+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sl"
}
-->
# Nastavitev tečaja

## Uvod

V tej lekciji bomo obravnavali, kako zagnati primere kode za ta tečaj.

## Pridružite se drugim učencem in poiščite pomoč

Preden začnete klonirati svoje repozitorije, se pridružite [kanalu Discord za začetnike AI agentov](https://aka.ms/ai-agents/discord), kjer lahko dobite pomoč pri nastavitvi, postavite vprašanja o tečaju ali se povežete z drugimi učenci.

## Klonirajte ali forknite ta repozitorij

Za začetek prosimo, da klonirate ali forknite GitHub repozitorij. Tako boste ustvarili svojo različico gradiva za tečaj, da boste lahko zagnali, testirali in prilagodili kodo!

To lahko storite s klikom na povezavo do

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.sl.png)

## Zagon kode

Ta tečaj ponuja serijo Jupyter zvezkov, ki jih lahko zaženete za praktično izkušnjo pri gradnji AI agentov.

Primeri kode uporabljajo eno od naslednjih možnosti:

**Zahteva GitHub račun - brezplačno**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Označeno kot (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Označeno kot (autogen.ipynb)

**Zahteva naročnino na Azure**:
3) Azure AI Foundry + Azure AI Agent Service. Označeno kot (azureaiagent.ipynb)

Priporočamo, da preizkusite vse tri vrste primerov, da ugotovite, katera možnost vam najbolj ustreza.

Ne glede na to, katero možnost izberete, bo to določilo, katere korake za nastavitev morate slediti spodaj:

## Zahteve

- Python 3.12+
  - **OPOMBA**: Če nimate nameščenega Python 3.12, ga namestite. Nato ustvarite svoj virtualni okolje (venv) z uporabo python3.12, da zagotovite pravilno namestitev različic iz datoteke requirements.txt.
- GitHub račun - za dostop do GitHub Models Marketplace
- Naročnina na Azure - za dostop do Azure AI Foundry
- Azure AI Foundry račun - za dostop do Azure AI Agent Service

V korenskem imeniku tega repozitorija smo vključili datoteko `requirements.txt`, ki vsebuje vse potrebne Python pakete za zagon primerov kode.

Namestite jih lahko z zagonom naslednjega ukaza v terminalu v korenskem imeniku repozitorija:

```bash
pip install -r requirements.txt
```
Priporočamo, da ustvarite Python virtualno okolje, da se izognete morebitnim konfliktom in težavam.

## Nastavitev VSCode
Prepričajte se, da uporabljate pravilno različico Pythona v VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavitev za primere z uporabo GitHub modelov 

### Korak 1: Pridobite svoj GitHub osebni dostopni žeton (PAT)

Ta tečaj uporablja GitHub Models Marketplace, ki omogoča brezplačen dostop do velikih jezikovnih modelov (LLM), ki jih boste uporabili za gradnjo AI agentov.

Za uporabo GitHub modelov boste morali ustvariti [GitHub osebni dostopni žeton](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

To lahko storite tako, da obiščete svoj

Prosimo, da pri ustvarjanju žetona sledite [načelu najmanjših privilegijev](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely). To pomeni, da žetonu dodelite samo tista dovoljenja, ki so potrebna za zagon primerov kode v tem tečaju.

1. Na levi strani zaslona izberite možnost `Fine-grained tokens` tako, da se pomaknete do **Developer settings**.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.sl.png)

    Nato izberite `Generate new token`.

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.sl.png)

2. Vnesite opisno ime za svoj žeton, ki odraža njegov namen, da ga boste kasneje lažje prepoznali.

    🔐 Priporočilo za trajanje žetona

    Priporočeno trajanje: 30 dni  
    Za boljšo varnost lahko izberete krajše obdobje, na primer 7 dni 🛡️.  
    To je odličen način, da si postavite osebni cilj in dokončate tečaj, medtem ko je vaša motivacija visoka 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.sl.png)

3. Omejite obseg žetona na svoj fork tega repozitorija.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.sl.png)

4. Omejite dovoljenja žetona: Pod **Permissions** kliknite zavihek **Account** in nato gumb "+ Add permissions". Prikaže se spustni meni. Poiščite **Models** in označite polje zanj.
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.sl.png)

5. Preden ustvarite žeton, preverite zahtevana dovoljenja. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.sl.png)

6. Preden ustvarite žeton, se prepričajte, da ste pripravljeni shraniti žeton na varno mesto, kot je trezor za gesla, saj ga po ustvarjanju ne boste mogli več videti. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.sl.png)

Kopirajte svoj novi žeton, ki ste ga pravkar ustvarili. Zdaj ga boste dodali v svojo `.env` datoteko, ki je vključena v ta tečaj.

### Korak 2: Ustvarite svojo `.env` datoteko

Za ustvarjanje `.env` datoteke zaženite naslednji ukaz v terminalu.

```bash
cp .env.example .env
```

To bo kopiralo primer datoteke in ustvarilo `.env` v vašem imeniku, kjer boste izpolnili vrednosti za okoljske spremenljivke.

S kopiranim žetonom odprite `.env` datoteko v svojem najljubšem urejevalniku besedila in prilepite žeton v polje `GITHUB_TOKEN`.  
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.sl.png)

Zdaj bi morali biti sposobni zagnati primere kode tega tečaja.

## Nastavitev za primere z uporabo Azure AI Foundry in Azure AI Agent Service

### Korak 1: Pridobite končno točko svojega Azure projekta

Sledite korakom za ustvarjanje vozlišča in projekta v Azure AI Foundry, ki jih najdete tukaj: [Pregled virov vozlišča](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Ko ustvarite svoj projekt, boste morali pridobiti povezovalni niz za svoj projekt.

To lahko storite tako, da obiščete stran **Overview** svojega projekta v portalu Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.sl.png)

### Korak 2: Ustvarite svojo `.env` datoteko

Za ustvarjanje `.env` datoteke zaženite naslednji ukaz v terminalu.

```bash
cp .env.example .env
```

To bo kopiralo primer datoteke in ustvarilo `.env` v vašem imeniku, kjer boste izpolnili vrednosti za okoljske spremenljivke.

S kopiranim žetonom odprite `.env` datoteko v svojem najljubšem urejevalniku besedila in prilepite žeton v polje `PROJECT_ENDPOINT`.

### Korak 3: Prijavite se v Azure

Kot najboljšo varnostno prakso bomo uporabili [avtentikacijo brez ključev](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) za avtentikacijo v Azure OpenAI z Microsoft Entra ID.

Nato odprite terminal in zaženite `az login --use-device-code`, da se prijavite v svoj Azure račun.

Ko se prijavite, v terminalu izberite svojo naročnino.

## Dodatne okoljske spremenljivke - Azure Search in Azure OpenAI

Za lekcijo Agentic RAG - Lekcija 5 - so na voljo primeri, ki uporabljajo Azure Search in Azure OpenAI.

Če želite zagnati te primere, boste morali dodati naslednje okoljske spremenljivke v svojo `.env` datoteko:

### Stran Pregled (Projekt)

- `AZURE_SUBSCRIPTION_ID` - Preverite **Project details** na strani **Overview** svojega projekta.

- `AZURE_AI_PROJECT_NAME` - Poglejte na vrh strani **Overview** svojega projekta.

- `AZURE_OPENAI_SERVICE` - Poiščite to na zavihku **Included capabilities** za **Azure OpenAI Service** na strani **Overview**.

### Upravljalni center

- `AZURE_OPENAI_RESOURCE_GROUP` - Pojdite na **Project properties** na strani **Overview** v **Management Center**.

- `GLOBAL_LLM_SERVICE` - Pod **Connected resources** poiščite ime povezave za **Azure AI Services**. Če ni navedeno, preverite **Azure portal** pod svojo skupino virov za ime vira AI Services.

### Stran Models + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Izberite svoj model za vdelavo (npr. `text-embedding-ada-002`) in zabeležite **Deployment name** iz podrobnosti modela.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Izberite svoj model za klepet (npr. `gpt-4o-mini`) in zabeležite **Deployment name** iz podrobnosti modela.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - Poiščite **Azure AI services**, kliknite nanj, nato pojdite na **Resource Management**, **Keys and Endpoint**, se pomaknite navzdol do "Azure OpenAI endpoints" in kopirajte tistega, ki pravi "Language APIs".

- `AZURE_OPENAI_API_KEY` - Na istem zaslonu kopirajte KLJUČ 1 ali KLJUČ 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Poiščite svoj vir **Azure AI Search**, kliknite nanj in si oglejte **Overview**.

- `AZURE_SEARCH_API_KEY` - Nato pojdite na **Settings** in nato **Keys**, da kopirate primarni ali sekundarni skrbniški ključ.

### Zunanja spletna stran

- `AZURE_OPENAI_API_VERSION` - Obiščite stran [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) pod **Latest GA API release**.

### Nastavitev avtentikacije brez ključev

Namesto da bi svoje poverilnice trdo kodirali, bomo uporabili povezavo brez ključev z Azure OpenAI. Za to bomo uvozili `DefaultAzureCredential` in kasneje poklicali funkcijo `DefaultAzureCredential`, da pridobimo poverilnico.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Ste se kje zataknili?

Če imate kakršne koli težave pri izvajanju te nastavitve, se pridružite našemu

## Naslednja lekcija

Zdaj ste pripravljeni na zagon kode za ta tečaj. Veselo učenje o svetu AI agentov!

[Uvod v AI agente in primere uporabe agentov](../01-intro-to-ai-agents/README.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.