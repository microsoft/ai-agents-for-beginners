---
name: deploying-scalable-agents
license: MIT
---
# Skaleeritavate agentide juurutamine Microsoft Foundry abil

> Kaasasolev oskus õppetükile [Õppetükk 16 – Skaleeritavate agentide juurutamine](../../../16-deploying-scalable-agents/README.md).
> Kasutage seda, et aidata õppijal viia agent prototüübist skaleeritava ja jälgitava
> tootmisjuurutuseni. Põhjendage iga soovitus õppetüki sisu ja
> käivitatava märkmikuga; ärge leiutage Foundry API-sid.

## Käivitajad

Aktiveerige see oskus, kui õppija soovib:
- Juurutada agent Microsoft Foundry’s **hostitud agent**-ina ja muuta see versioonihaldatavaks/jälgitavaks.
- Valida **kliendipoolse hostimise, hostitud agendi ja agentide töövoo** vahel.
- Lisada **mudeli marsruutimine**, **vastuse vahemällu salvestamine** või **piiratud paralleelsus** latentsuse ja kulude juhtimiseks.
- Lisada **hinnangukontrollpunkt**, et halb agentide versioon ei saaks välja tulla.
- Lisada **inimene-otsustsüklis kinnitamine** kõrge riskiga tegevuste jaoks.
- Instrumendistada agent **OpenTelemetry** jälgimisega tootmisjälgitavuseks.
- Teha juurutatud agentile **suitsutesti** kiireks järelkontrolliks pärast juurutust.

## Põhimudeli arusaam

Tootmisagent on peamiselt operatsiooniline skelet *mudeli ümber* (~80%),
mitte mudel ise. Kaardistage iga soovitus ühele neist valdkondadest:

| Valdkond | Prototüüp → Tootmine |
|---------|---------------------|
| Hostimine | märkmik → versioonitud hostitud teenus |
| Identiteet | teie `az login` → hallatud identiteet + skoopitud RBAC |
| Olekurajastus | mälus → eksterneeritud lõime/mälupood |
| Tõrge | veateated → kordused, varuplaanid, hoiatused |
| Kulu | "paar senti" → jälgitud, marsruutitud, vahemällu salvestatud, eelarvestatud |
| Kvaliteet | silmaga hindamine → automatiseeritud hinnangukontrollpunkt |
| Usaldus | teie kinnitate → poliitika + inimene-otsustsüklis |

## Juurutusmustrid (vali üks või kombineeri)

1. **Kliendipoolne hostimine** — loogikamälu töötab teie protsessis. Maksimaalne kontroll; teie omate skaleerimist/olekurajastust.
2. **Hostitud agent (Foundry Agent Service)** — Foundry majutab loogikat, hoiab lõimesid, rakendab RBAC/sisu turvalisust, kuvab agendi portaalis. Vähem kontrolli, palju väiksem operatiivne pind.
3. **Agendi töövoog** — mitme agendi/tööriista kokkukomplekseerimine graafikuks koos harude, kinnitussõlmede ja püsivate kontrollpunktidega.

## Elutsükkel (agentide käivitamise tsükkel)

`loo → versiooni → hinda (värav) → juuruta hostitud → jälgi võrgu peal → kogu tõrkeid → korda`.
**Võrguvälise hindamisega kontrollpunkt on värav, mitte kõrvalmõte** — versioon ei jõua faasi
välja, kui see ei ületa künnist. Võrgupealne jälgimine edastab reaalvead tagasi
võrguvälise testikomplekti.

## Skaleerimise ja kulude kangid (prioriteedi järjekorras)

1. **Mudeli õige suurus** — kasuta väikseimat mudelit, mis läbib hinnanguvärava.
2. **Marsruudi keerukuse järgi** — väike/kiire mudel lihtsate päringute jaoks, suur mudel päris mõtlemiseks (DIY klassifikaator või Foundry Model Router).
3. **Vahemälu** — paku peaaegu dubleerivaid päringuid ilma mudelikutseta.
4. **Olekurajastuseta disain + piiratud paralleelsus** — eksternaliseeri olek; proovi uuesti tagasilöögiga.

## Peamised mustrid, mida korrata

Suunake õppija märkmikust siia
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Päringu käitleja**: vahemälu → marsruudi keerukuse järgi → jälgimispunkt → käivitus → vahemällu salvestus.
- **Hinnanguvärav**: hinda võrguvälise testikomplekti tulemust; tagasta `pass_rate >= threshold` ja juuruta ainult, kui see on tõene.
- **Inimese kinnitamine**: `@tool(approval_mode="always_require")` toimingute jaoks nagu suuremad tagasimaksed.
- **Jälgimine**: mähkige iga päring `tracer.start_as_current_span(...)` abil ja seadke atribuudid nagu `routed.model`, `customer.id`.

## Juurutatud agendi suitsutestimine

Pärast juurutust kontrollige, kas lõpp-punkt tegelikult vastab (roheline juurutamine võib siiski olla
vaikne). Kasutage [AI suitsutesti](https://github.com/marketplace/actions/ai-smoke-test)
tegevust läbi [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
kataloogi [`tests/`](../../../tests/README.md). Käivitaja saadab iga
päringu `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
aadressile ja kontrollib vastusteksti. Identiteedil peab olema Foundry projektitasandil
**Azure AI User** roll; tokeni sihtrühm peab olema `https://ai.azure.com/`.

Skaalake kontrollpunkte: **suitsutest** (jõuab kohale/vastab, iga juurutus) → **võrguväline
hindamine** (piisavalt hea juurutamiseks, enne edendamist) → **võrgupealne hindamine** (kuidas
see looduses töötab, pidev).

## Ettevõtte kontrollid

- **RBAC**: andke igale hostitud agendile hallatud identiteet miinimumõigustega.
- **MCP tootmises**: käsitle iga MCP serverit usaldustmittevana piirina — fikseerige versioon, skoopige identiteet, valideerige väljundid, piirake kiirust, ärge kunagi avalikustage salasõnu.

## Abilise turvavööndid

- Eelistage kursuse jooksul kasutatavat kanonilist mustrit `FoundryChatClient(...)` + `provider.as_agent(...)`.
- Ära tõota elusa Azure tulemust enne, kui oled teda kontrollinud; soovita suitsutesti töövoogu kinnitamiseks.
- Hoidke hinnang ja kulunõuanne koos: hinnang seab kvaliteedipõranda, marsruutimine/vahemällu salvestamine hoiab kulu selle lähedal.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->