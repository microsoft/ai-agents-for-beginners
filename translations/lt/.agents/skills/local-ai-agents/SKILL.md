---
name: local-ai-agents
license: MIT
---
# Vietinių DI agentų kūrimas naudojant Foundry Local ir Qwen

> Papildomoji užduotis prie [17 pamoka – Vietinių DI agentų kūrimas](../../../17-creating-local-ai-agents/README.md).
> Naudokite ją, kad padėtumėte besimokančiajam sukurti agentą, kuris mąsto, kviečia įrankius ir ieško
> dokumentacijos visiškai savo kompiuteryje – be debesijos apdorojimo. Pagrįskite kiekvieną
> rekomendaciją pamokos turiniu ir vykdomu užrašu.

## Suveikimai

Aktyvinkite šią įgūdį, kai besimokantis nori:
- Vykdyti agentą **visiškai įrenginyje** dėl privatumo, sąnaudų ar neprisijungimo priežasčių.
- Vietoje aptarnauti modelį naudojant **Foundry Local** ir prisijungti per OpenAI suderinamą galutinį tašką.
- Naudoti **Qwen funkcijų kvietimo** modelį patikimam vietiniam įrankių kvietimui.
- Pridėti **vietinį RAG** (Chroma) arba **vietinį MCP serverį**.
- Sukurti **hibridinę** vietinės/debesijos maršruto strategiją.

## Pagrindinė minties schema

SLM mainais į privatumo, sąnaudų ir neprisijungimo privalumus aukoja žinių įvairovę. Pergalės
strategija: **leisk SLM valdyti procesą, o įrankiams atlikti sunkų darbą.** Modeliui nereikia
*žinoti* kodo bazės – jam svarbu žinoti, kada kvieti
`read_file` ir `search_docs`. Tai atitinka SLM stipriąsias puses (riboto pobūdžio sprendimai,
pvz., įrankių pasirinkimas) ir mažina jo silpnybę (plati žinių apimtis, ilgas daugiapakopis
mąstymas).

## Kodėl būtent šios dalys

- **Foundry Local** siūlo **OpenAI suderinamą HTTP galinį tašką**, todėl debesijos agentų kodas persikelia keičiant tik `base_url` (ir naudojant vietinį vietos rezervavimo API raktą). Jis taip pat automatiškai parenka geriausią versiją (CPU/GPU/NPU) įrenginiui.
- **Qwen** modeliai treniruojami funkcijų kvietimams ir nuosekliai generuoja taisyklingus įrankių kvietimus – tai verčia vietinį *pokalbio* modelį tapti vietiniu *agentu*.
- **Chroma** veikia proceso viduje ir saugo vektorius diske, todėl visas RAG procesas (užkoduoti → saugoti → išrinkti → mąstyti) lieka vietinis.
- **MCP** yra transporto protokolas, o ne debesijos paslauga: MCP serverį galima paleisti vietoje per `stdio`.

## Pagrindiniai nustatymai

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # vietos rezervas
```

Apytikslis minimumas – apie 8 GB RAM; GPU/NPU padeda, bet nėra būtinas.

## Pagrindiniai atkartotini šablonai

Nurodykite besimokančiajam užrašą
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Izoliuoti įrankiai**: kiekvienas failų įrankis tikrina kelią ir neleidžia patekti už vienos projekto šaknies – net vietoje įrankis veikia su vartotojo teisėmis.
- **Įrankių kvietimo kilpa**: registruok įrankius su OpenAI įrankių schema, vykdyk prašomus įrankius vietoje, sugrąžink rezultatus, kartok iki galutinio atsakymo.
- **Vietinis RAG**: įrašyk dokumentus į Chroma kolekciją; `search_docs` grąžina geriausias dalis.
- **Vietinis MCP**: prisijunk prie vietinio serverio per `stdio`; aprėpk projektą ir patikrink išvestį.

## Hibridinis maršrutavimas (vietinis kaip vienas iš modelių)

| Situacija | Kur vykdomas |
|-----------|---------------|
| Konfidencialūs duomenys / neprisijungus | Vietinis SLM |
| Paprasta, ribota užduotis | Vietinis SLM (pigus, greitas) |
| Sudėtingas daugiapakopis mąstymas su nekonfidencialiais duomenimis | Debesijos modelis |
| Debesijos klaida | Vietinis SLM (sklandus kokybės praradimas) |

Tai atitinka modelių maršrutavimo idėją iš 16 pamokos, kai darbo stotis yra viena
iš eilių. Pirmenybė teikiama sprendimams, kurie nukrypsta į vietinį režimą, kad agento kokybė
gerėtų, o ne visiškai gestų.

## Pagalbinės taisyklės asistentui

- Laikyk visus failų/įrankių veiksmus apribotus izoliuotame projekto kataloge.
- Neperkėlinėk kodo ar duomenų į debesį, jei besimokantysis nurodė tikslą dėl privatumo/neprisijungimo – išlaikyk visą procesą vietinį.
- Nustatyk realistiškus lūkesčius dėl SLM kokybės; remkis įrankiais ir RAG, o ne modelio išmoktomis žiniomis.
- Atkreipk dėmesį, kad 17 pamoka neturi **Foundry Responses** galinio taško, todėl debesijos testavimas netaikomas – tikrink vykdydamas užrašą vietoje.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->