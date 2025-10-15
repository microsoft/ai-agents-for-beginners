<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T11:58:36+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "lt"
}
-->
# Kursų nustatymas

## Įvadas

Ši pamoka apims, kaip paleisti šio kurso kodų pavyzdžius.

## Prisijunkite prie kitų mokinių ir gaukite pagalbos

Prieš pradėdami klonuoti savo saugyklą, prisijunkite prie [AI Agents For Beginners Discord kanalo](https://aka.ms/ai-agents/discord), kad gautumėte pagalbos dėl nustatymo, atsakymų į klausimus apie kursą arba susisiektumėte su kitais mokiniais.

## Klonuokite arba šakokite šią saugyklą

Norėdami pradėti, prašome klonuoti arba šakoti GitHub saugyklą. Tai sukurs jūsų asmeninę kurso medžiagos versiją, kad galėtumėte paleisti, testuoti ir koreguoti kodą!

Tai galima padaryti paspaudžiant nuorodą <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">šakoti saugyklą</a>.

Dabar turėtumėte turėti savo šakotą šio kurso versiją šioje nuorodoje:

![Šakota saugykla](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.lt.png)

### Paviršutiniškas klonavimas (rekomenduojama dirbtuvėms / Codespaces)

  >Visa saugykla gali būti didelė (~3 GB), kai atsisiunčiate visą istoriją ir visus failus. Jei dalyvaujate tik dirbtuvėse arba jums reikia tik kelių pamokų aplankų, paviršutiniškas klonavimas (arba dalinis klonavimas) leidžia išvengti didžiosios dalies atsisiuntimo, sutrumpinant istoriją ir/arba praleidžiant failus.

#### Greitas paviršutiniškas klonavimas — minimalus istorijos kiekis, visi failai

Pakeiskite `<your-username>` žemiau pateiktuose komanduose savo šakos URL (arba pirminį URL, jei pageidaujate).

Norėdami klonuoti tik naujausią istorijos įrašą (mažas atsisiuntimas):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Norėdami klonuoti konkrečią šaką:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Dalinis (dalinis) klonavimas — minimalūs failai + tik pasirinkti aplankai

Tai naudoja dalinį klonavimą ir dalinį patikrinimą (reikalinga Git 2.25+ ir rekomenduojama moderni Git versija su dalinio klonavimo palaikymu):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pereikite į saugyklos aplanką:

Bash:

```bash
cd ai-agents-for-beginners
```

Powershell:

```powershell
Set-Location ai-agents-for-beginners
```

Tada nurodykite, kuriuos aplankus norite (pavyzdys žemiau rodo du aplankus):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po klonavimo ir failų patikrinimo, jei jums reikia tik failų ir norite atlaisvinti vietą (be git istorijos), prašome ištrinti saugyklos metaduomenis (💀negrįžtama — prarasite visą Git funkcionalumą: jokių įrašų, traukimų, stūmimų ar istorijos prieigos).

Linux/macOS:

```bash
rm -rf .git
```

Windows:

```powershell
Remove-Item -Recurse -Force .git
```

#### Naudojant GitHub Codespaces (rekomenduojama išvengti vietinių didelių atsisiuntimų)

- Sukurkite naują Codespace šiai saugyklai per [GitHub UI](https://github.com/codespaces).  

- Naujoje Codespace terminale paleiskite vieną iš paviršutiniško/dalinio klonavimo komandų, kad įtrauktumėte tik jums reikalingus pamokų aplankus į Codespace darbo aplinką.
- Pasirinktinai: po klonavimo Codespaces viduje, pašalinkite .git, kad atgautumėte papildomą vietą (žr. pašalinimo komandas aukščiau).
- Pastaba: Jei pageidaujate atidaryti saugyklą tiesiogiai Codespaces (be papildomo klonavimo), atkreipkite dėmesį, kad Codespaces sukurs devcontainer aplinką ir gali vis tiek paruošti daugiau nei jums reikia. Klonuojant paviršutinišką kopiją šviežioje Codespace suteikia daugiau kontrolės disko naudojimui.

#### Patarimai

- Visada pakeiskite klonavimo URL savo šaka, jei norite redaguoti/įrašyti.
- Jei vėliau jums reikia daugiau istorijos ar failų, galite juos gauti arba koreguoti dalinį patikrinimą, kad įtrauktumėte papildomus aplankus.

## Kodo paleidimas

Šis kursas siūlo seriją Jupyter Notebooks, kuriuos galite paleisti, kad praktiškai išmoktumėte kurti AI agentus.

Kodo pavyzdžiai naudoja:

**Reikalinga GitHub paskyra - nemokama**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Pažymėta kaip (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Pažymėta kaip (autogen.ipynb)

**Reikalinga Azure prenumerata**:
3) Azure AI Foundry + Azure AI Agent Service. Pažymėta kaip (azureaiagent.ipynb)

Rekomenduojame išbandyti visus tris pavyzdžių tipus, kad pamatytumėte, kuris jums geriausiai tinka.

Kurią parinktį pasirinksite, tai nulems, kokius nustatymo veiksmus turėsite atlikti toliau:

## Reikalavimai

- Python 3.12+
  - **PASTABA**: Jei neturite įdiegto Python3.12, įsitikinkite, kad jį įdiegėte. Tada sukurkite savo venv naudodami python3.12, kad užtikrintumėte, jog iš requirements.txt failo bus įdiegta tinkama versija.
  
    >Pavyzdys

    Sukurkite Python venv katalogą:

    ``` bash
    python3 -m venv venv
    ```

    Tada aktyvuokite venv aplinką:

    macOS ir Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- GitHub paskyra - prieiga prie GitHub Models Marketplace
- Azure prenumerata - prieiga prie Azure AI Foundry
- Azure AI Foundry paskyra - prieiga prie Azure AI Agent Service

Mes įtraukėme `requirements.txt` failą šios saugyklos šaknyje, kuriame yra visi reikalingi Python paketai, kad galėtumėte paleisti kodo pavyzdžius.

Juos galite įdiegti paleisdami šią komandą savo terminale saugyklos šaknyje:

```bash
pip install -r requirements.txt
```
Rekomenduojame sukurti Python virtualią aplinką, kad išvengtumėte konfliktų ir problemų.

## VSCode nustatymas
Įsitikinkite, kad naudojate tinkamą Python versiją VSCode.

![vaizdas](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nustatymas pavyzdžiams naudojant GitHub modelius 

### 1 žingsnis: Gaukite savo GitHub asmeninį prieigos raktą (PAT)

Šis kursas naudoja GitHub Models Marketplace, suteikiant nemokamą prieigą prie didelių kalbos modelių (LLMs), kuriuos naudosite kurdami AI agentus.

Norėdami naudoti GitHub modelius, turėsite sukurti [GitHub asmeninį prieigos raktą](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Tai galima padaryti einant į savo <a href="https://github.com/settings/personal-access-tokens" target="_blank">asmeninių prieigos raktų nustatymus</a> savo GitHub paskyroje.

Prašome laikytis [mažiausios privilegijos principo](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) kuriant savo raktą. Tai reiškia, kad turėtumėte suteikti raktui tik tas teises, kurių reikia šio kurso kodo pavyzdžiams paleisti.

1. Pasirinkite `Fine-grained tokens` parinktį kairėje ekrano pusėje, eidami į **Developer settings**.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.lt.png)

    Tada pasirinkite `Generate new token`.

    ![Sukurti raktą](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.lt.png)

2. Įveskite aprašomąjį pavadinimą savo raktui, kuris atspindi jo paskirtį, kad vėliau būtų lengva jį identifikuoti.


    🔐 Rekomenduojama rakto trukmė

    Rekomenduojama trukmė: 30 dienų
    Dėl saugesnės pozicijos galite pasirinkti trumpesnį laikotarpį, pvz., 7 dienas 🛡️
    Tai puikus būdas nustatyti asmeninį tikslą ir baigti kursą, kol jūsų mokymosi tempas yra aukštas 🚀.

    ![Rakto pavadinimas ir galiojimo data](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.lt.png)

3. Apribokite rakto taikymo sritį savo šakos saugyklai.

    ![Apriboti taikymo sritį šakos saugyklai](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.lt.png)

4. Apribokite rakto teises: Skiltyje **Permissions**, spustelėkite **Account** skirtuką ir spustelėkite "+ Add permissions" mygtuką. Atsiras išskleidžiamasis meniu. Prašome ieškoti **Models** ir pažymėti langelį.
    ![Pridėti modelių teises](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.lt.png)

5. Patikrinkite reikalingas teises prieš generuodami raktą. ![Patikrinti teises](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.lt.png)

6. Prieš generuodami raktą, įsitikinkite, kad esate pasiruošę saugoti raktą saugioje vietoje, pvz., slaptažodžių valdymo saugykloje, nes jis nebus rodomas dar kartą po sukūrimo. ![Saugiai saugoti raktą](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.lt.png)

Nukopijuokite naują raktą, kurį ką tik sukūrėte. Dabar pridėsite jį prie savo `.env` failo, įtraukto į šį kursą.


### 2 žingsnis: Sukurkite savo `.env` failą

Norėdami sukurti `.env` failą, paleiskite šią komandą savo terminale.

```bash
cp .env.example .env
```

Tai nukopijuos pavyzdinį failą ir sukurs `.env` jūsų kataloge, kur užpildysite aplinkos kintamųjų reikšmes.

Nukopijavę savo raktą, atidarykite `.env` failą savo mėgstamiausiame teksto redaktoriuje ir įklijuokite savo raktą į `GITHUB_TOKEN` lauką.
![GitHub rakto laukas](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.lt.png)


Dabar turėtumėte galėti paleisti šio kurso kodo pavyzdžius.

## Nustatymas pavyzdžiams naudojant Azure AI Foundry ir Azure AI Agent Service

### 1 žingsnis: Gaukite savo Azure projekto galutinį tašką


Sekite veiksmus, kaip sukurti centrą ir projektą Azure AI Foundry, pateiktus čia: [Hub resursų apžvalga](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)


Kai sukursite savo projektą, turėsite gauti savo projekto prisijungimo eilutę.

Tai galima padaryti einant į **Apžvalga** puslapį savo projekte Azure AI Foundry portale.

![Projekto prisijungimo eilutė](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.lt.png)

### 2 žingsnis: Sukurkite savo `.env` failą

Norėdami sukurti `.env` failą, paleiskite šią komandą savo terminale.

```bash
cp .env.example .env
```

Tai nukopijuos pavyzdinį failą ir sukurs `.env` jūsų kataloge, kur užpildysite aplinkos kintamųjų reikšmes.

Nukopijavę savo raktą, atidarykite `.env` failą savo mėgstamiausiame teksto redaktoriuje ir įklijuokite savo raktą į `PROJECT_ENDPOINT` lauką.

### 3 žingsnis: Prisijunkite prie Azure

Kaip saugumo geriausia praktika, naudosime [autentifikaciją be rakto](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst), kad autentifikuotume prie Azure OpenAI su Microsoft Entra ID. 

Tada atidarykite terminalą ir paleiskite `az login --use-device-code`, kad prisijungtumėte prie savo Azure paskyros.

Kai prisijungsite, pasirinkite savo prenumeratą terminale.


## Papildomi aplinkos kintamieji - Azure Search ir Azure OpenAI 

Agentic RAG pamokai - Pamoka 5 - yra pavyzdžių, kurie naudoja Azure Search ir Azure OpenAI.

Jei norite paleisti šiuos pavyzdžius, turėsite pridėti šiuos aplinkos kintamuosius į savo `.env` failą:

### Apžvalgos puslapis (Projektas)

- `AZURE_SUBSCRIPTION_ID` - Patikrinkite **Projekto detales** **Apžvalgos** puslapyje savo projekte.

- `AZURE_AI_PROJECT_NAME` - Pažvelkite į **Apžvalgos** puslapio viršų savo projekte.

- `AZURE_OPENAI_SERVICE` - Raskite tai **Įtrauktų galimybių** skirtuke **Azure OpenAI Service** **Apžvalgos** puslapyje.

### Valdymo centras

- `AZURE_OPENAI_RESOURCE_GROUP` - Eikite į **Projekto savybes** **Apžvalgos** puslapyje **Valdymo centre**.

- `GLOBAL_LLM_SERVICE` - Skiltyje **Prijungti resursai**, raskite **Azure AI Services** prisijungimo pavadinimą. Jei neįtraukta, patikrinkite **Azure portalą** savo resursų grupėje dėl AI Services resurso pavadinimo.

### Modeliai + Galutiniai taškai puslapis

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Pasirinkite savo įterpimo modelį (pvz., `text-embedding-ada-002`) ir atkreipkite dėmesį į **Diegimo pavadinimą** iš modelio detalių.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Pasirinkite savo pokalbio modelį (pvz., `gpt-4o-mini`) ir atkreipkite dėmesį į **Diegimo pavadinimą** iš modelio detalių.

### Azure portalas

- `AZURE_OPENAI_ENDPOINT` - Ieškokite **Azure AI services**, spustelėkite ant jo, tada eikite į **Resursų valdymas**, **Raktai ir galutiniai taškai**, slinkite žemyn iki "Azure OpenAI galutiniai taškai" ir nukopijuokite tą, kuris sako "Kalbos API".

- `AZURE_OPENAI_API_KEY` - Iš to paties ekrano nukopijuokite RAKTĄ 1 arba RAKTĄ 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Raskite savo **Azure AI Search** resursą, spustelėkite jį ir peržiūrėkite **Apžvalga**.

- `AZURE_SEARCH_API_KEY` - Tada eikite į **Nustatymai** ir tada **Raktai**, kad nukopijuotumėte pirminį arba antrinį administratoriaus raktą.

### Išorinė svetainė

- `AZURE_OPENAI_API_VERSION` - Apsilankykite [API versijos gyvavimo ciklo](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) puslapyje skiltyje **Naujausia GA API versija**.

### Nustatykite autentifikaciją be rakto

Užuot kodavę savo kredencialus, naudosime ryšį be rakto su Azure OpenAI. Tam importuosime `DefaultAzureCredential` ir vėliau iškviesime `DefaultAzureCredential` funkciją, kad gautume kredencialą.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Užstrigote kažkur?
Jei kyla problemų naudojant šį nustatymą, prisijunkite prie mūsų <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI bendruomenės Discord</a> arba <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">sukurkite problemos pranešimą</a>.

## Kita pamoka

Dabar esate pasiruošę vykdyti šio kurso kodą. Smagaus mokymosi apie AI agentų pasaulį!

[Įvadas į AI agentus ir agentų naudojimo atvejus](../01-intro-to-ai-agents/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius naudojant šį vertimą.