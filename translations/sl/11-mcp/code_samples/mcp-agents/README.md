<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5cc6836626047aa055e8960c8484a7d0",
  "translation_date": "2025-08-21T13:41:47+00:00",
  "source_file": "11-mcp/code_samples/mcp-agents/README.md",
  "language_code": "sl"
}
-->
# Gradnja sistemov za komunikacijo med agenti z MCP

> TL;DR - Ali lahko zgradite komunikacijo Agent2Agent na MCP? Da!

MCP se je bistveno razvil od svoje prvotne naloge "zagotavljanja konteksta za LLM-je". Z nedavnimi izboljšavami, kot so [ponovno vzpostavljive tokove](https://modelcontextprotocol.io/docs/concepts/transports#resumability-and-redelivery), [elicitacija](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation), [vzorčenje](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling) in obvestila ([napredek](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/progress) ter [viri](https://modelcontextprotocol.io/specification/2025-06-18/schema#resourceupdatednotification)), MCP zdaj zagotavlja robustno osnovo za gradnjo kompleksnih sistemov komunikacije med agenti.

## Napačno razumevanje agentov in orodij

Ko se vedno več razvijalcev ukvarja z orodji, ki imajo agentne lastnosti (delujejo dalj časa, morda potrebujejo dodatne vnose med izvajanjem itd.), se pogosto pojavi napačno prepričanje, da MCP ni primeren, predvsem zato, ker so zgodnji primeri njegove primitivne funkcije orodij temeljili na preprostih vzorcih zahteva-odgovor.

To prepričanje je zastarelo. Specifikacija MCP je bila v zadnjih mesecih bistveno izboljšana z zmogljivostmi, ki zapolnjujejo vrzel pri gradnji dolgotrajnega agentnega vedenja:

- **Pretakanje in delni rezultati**: Posodobitve napredka v realnem času med izvajanjem
- **Ponovna vzpostavitev**: Odjemalci se lahko ponovno povežejo in nadaljujejo po prekinitvi
- **Vzdržljivost**: Rezultati preživijo ponovni zagon strežnika (npr. prek povezav do virov)
- **Večkratni obrati**: Interaktivni vnosi med izvajanjem prek elicitacije in vzorčenja

Te funkcije je mogoče sestaviti za omogočanje kompleksnih agentnih in večagentnih aplikacij, vse pa so nameščene na MCP protokolu.

Za referenco bomo agenta imenovali "orodje", ki je na voljo na MCP strežniku. To pomeni obstoj gostiteljske aplikacije, ki implementira MCP odjemalca, vzpostavi sejo z MCP strežnikom in lahko kliče agenta.

## Kaj naredi MCP orodje "agentno"?

Preden se lotimo implementacije, opredelimo, katere infrastrukturne zmogljivosti so potrebne za podporo dolgotrajnih agentov.

> Agenta bomo opredelili kot entiteto, ki lahko deluje avtonomno dalj časa, sposobno obravnavati kompleksne naloge, ki lahko zahtevajo več interakcij ali prilagoditev na podlagi povratnih informacij v realnem času.

### 1. Pretakanje in delni rezultati

Tradicionalni vzorci zahteva-odgovor ne delujejo za dolgotrajne naloge. Agenti morajo zagotavljati:

- Posodobitve napredka v realnem času
- Vmesne rezultate

**Podpora MCP**: Obvestila o posodobitvi virov omogočajo pretakanje delnih rezultatov, čeprav to zahteva skrbno načrtovanje, da se izognemo konfliktom z modelom 1:1 zahteva/odgovor JSON-RPC.

| Funkcija                  | Primer uporabe                                                                                                                                                                       | Podpora MCP                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Posodobitve napredka v realnem času | Uporabnik zahteva nalogo migracije kode. Agent pretaka napredek: "10% - Analiza odvisnosti... 25% - Pretvorba datotek TypeScript... 50% - Posodabljanje uvozov..."          | ✅ Obvestila o napredku                                                                  |
| Delni rezultati            | Naloga "Ustvari knjigo" pretaka delne rezultate, npr. 1) Oris zgodbe, 2) Seznam poglavij, 3) Vsako dokončano poglavje. Gostitelj lahko pregleda, prekliče ali preusmeri v katerem koli trenutku. | ✅ Obvestila je mogoče "razširiti", da vključujejo delne rezultate, glejte predloge na PR 383, 776 |

### 2. Ponovna vzpostavitev

Agenti morajo obravnavati prekinitve omrežja brez težav:

- Ponovna povezava po prekinitvi (odjemalca)
- Nadaljevanje od tam, kjer so končali (ponovna dostava sporočil)

**Podpora MCP**: MCP StreamableHTTP transport danes podpira obnovitev sej in ponovno dostavo sporočil z ID-ji sej in ID-ji zadnjih dogodkov. Pomembno je, da strežnik implementira EventStore, ki omogoča ponovitev dogodkov ob ponovni povezavi odjemalca.  
Opomba: obstaja predlog skupnosti (PR #975), ki raziskuje transportno neodvisne obnovljive tokove.

| Funkcija      | Primer uporabe                                                                                                                                                   | Podpora MCP                                                                |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Ponovna vzpostavitev | Odjemalec se prekine med dolgotrajno nalogo. Ob ponovni povezavi se seja nadaljuje z ponovljenimi dogodki, ki omogočajo nemoteno nadaljevanje od tam, kjer je končal. | ✅ StreamableHTTP transport z ID-ji sej, ponovitvijo dogodkov in EventStore |

### 3. Vzdržljivost

Dolgotrajni agenti potrebujejo trajno stanje:

- Rezultati preživijo ponovni zagon strežnika
- Status je mogoče pridobiti zunaj seje
- Sledenje napredku med sejami

**Podpora MCP**: MCP zdaj podpira vrsto vrnitve povezave do virov za klice orodij. Danes je možen vzorec zasnovati orodje, ki ustvari vir in takoj vrne povezavo do vira. Orodje lahko nadaljuje z obravnavo naloge v ozadju in posodablja vir. Odjemalec lahko nato izbere, ali bo preverjal stanje tega vira za pridobitev delnih ali celotnih rezultatov (glede na to, katere posodobitve virov strežnik zagotavlja) ali se naročil na vir za obvestila o posodobitvah.

### 4. Večkratne interakcije

Agenti pogosto potrebujejo dodatne vnose med izvajanjem:

- Človeška pojasnila ali odobritev
- AI pomoč pri kompleksnih odločitvah
- Dinamična prilagoditev parametrov

**Podpora MCP**: Popolnoma podprto prek vzorčenja (za AI vnose) in elicitacije (za človeške vnose).

| Funkcija                 | Primer uporabe                                                                                                                                     | Podpora MCP                                           |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Večkratne interakcije | Agent za rezervacijo potovanj zahteva potrditev cene od uporabnika, nato prosi AI za povzetek podatkov o potovanju, preden zaključi transakcijo rezervacije. | ✅ Elicitacija za človeške vnose, vzorčenje za AI vnose |

## Implementacija dolgotrajnih agentov na MCP - Pregled kode

Kot del tega članka ponujamo [repozitorij kode](https://github.com/victordibia/ai-tutorials/tree/main/MCP%20Agents), ki vsebuje popolno implementacijo dolgotrajnih agentov z uporabo MCP Python SDK z StreamableHTTP transportom za obnovitev sej in ponovno dostavo sporočil. Implementacija prikazuje, kako je mogoče zmogljivosti MCP sestaviti za omogočanje sofisticiranega agentnega vedenja.

Specifično implementiramo strežnik z dvema primarnima orodjema agentov:

- **Agent za potovanja** - Simulira storitev rezervacije potovanj s potrditvijo cene prek elicitacije
- **Raziskovalni agent** - Izvaja raziskovalne naloge s povzetki, ki jih pomaga ustvariti AI, prek vzorčenja

Oba agenta prikazujeta posodobitve napredka v realnem času, interaktivne potrditve in popolne zmogljivosti obnove sej.

## Zaključek

Izboljšane zmogljivosti MCP - obvestila o virih, elicitacija/vzorčenje, obnovljivi tokovi in trajni viri - omogočajo kompleksne interakcije med agenti, hkrati pa ohranjajo preprostost protokola.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.