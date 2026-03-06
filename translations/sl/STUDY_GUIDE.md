# AI agenti za začetnike - študijski vodič in povzetek tečaja

Ta vodič povzame tečaj "AI agenti za začetnike" in razloži ključne koncepte, okvire in oblikovalske vzorce za gradnjo AI agentov.

## 1. Uvod v AI agente

**Kaj so AI agenti?**  
AI agenti so sistemi, ki razširjajo zmogljivosti velikih jezikovnih modelov (LLM) tako, da jim omogočajo dostop do **orodij**, **znanja** in **spomina**. V nasprotju z običajnim LLM klepetalnikom, ki generira samo besedilo na podlagi učnih podatkov, lahko AI agent:  
- **Zaznava** svoje okolje (prek senzorjev ali vhodov).  
- **Premišljuje** o tem, kako rešiti problem.  
- **Ukrepati**, da spremeni okolje (prek izvrševalcev ali orodij).

**Ključni elementi agenta:**  
- **Okolje**: prostor, kjer agent deluje (npr. sistem za rezervacije).  
- **Senzorji**: mehanizmi za zbiranje informacij (npr. branje API-ja).  
- **Izvrševalci**: mehanizmi za izvajanje dejanj (npr. pošiljanje e-pošte).  
- **Možgani (LLM)**: računski motor, ki načrtuje in odloča, katera dejanja sprejeti.

## 2. Agentni okviri

Tečaj uporablja **Microsoft Agent Framework (MAF)** z **Azure AI Foundry Agent Service V2** za gradnjo agentov:

| Komponenta | Fokus | Najbolj primerno za |
|------------|-------|---------------------|
| **Microsoft Agent Framework** | Enoten Python/C# SDK za agente, orodja in delovne tokove | Gradnjo agentov z orodji, večagentne delovne tokove in proizvodne vzorce. |
| **Azure AI Foundry Agent Service** | Upravljano oblačno okolje | Zanesljiva, razširljiva namestitev z vgrajenim upravljanjem stanja, opazovanjem in zaupanje. |

## 3. Agentni oblikovalski vzorci

Oblikovalski vzorci pomagajo strukturirati delovanje agentov za zanesljivo reševanje problemov.

### **Vzorec uporabe orodij** (Lekcija 4)  
Ta vzorec omogoča agentom interakcijo z zunanjim svetom.  
- **Koncept**: agentu je na voljo "shema" (seznam funkcij in njihovih parametrov). LLM odloči, *katero* orodje poklicati in s *katerimi* argumenti na podlagi uporabnikove zahteve.  
- **Potek**: Uporabnikova zahteva -> LLM -> **izbira orodja** -> **izvajanje orodja** -> LLM (z izhodom orodja) -> končni odgovor.  
- **Primeri uporabe**: pridobivanje aktualnih podatkov (vreme, cene delnic), izvajanje računov, poganjanje kode.

### **Vzorec načrtovanja** (Lekcija 7)  
Ta vzorec omogoča agentom reševanje zapletenih, večstopenjskih nalog.  
- **Koncept**: agent razdeli visokonivojski cilj na niz manjših podnalog.  
- **Pristopi**:  
  - **Razčlenitev naloge**: razdelitev "Načrtuj potovanje" na "Rezerviraj let", "Rezerviraj hotel", "Izposodi avto".  
  - **Iterativno načrtovanje**: ponovno ocenjevanje načrta glede na rezultate prejšnjih korakov (npr. če je let poln, izberi drug datum).  
- **Izvedba**: pogosto vključuje "planer" agenta, ki generira strukturiran načrt (npr. JSON), ki ga nato izvajajo drugi agenti.

## 4. Načela oblikovanja

Pri oblikovanju agentov upoštevajte tri dimenzije:  
- **Prostor**: agenti naj povezujejo ljudi in znanje, naj bodo dostopni, a neopazni.  
- **Čas**: agenti naj se učijo iz *preteklosti*, nudijo relevantne spodbude v *sedanjosti* in se prilagajajo za *prihodnost*.  
- **Jedro**: sprejmite negotovost, a vzpostavite zaupanje s transparentnostjo in nadzorom uporabnika.

## 5. Povzetek ključnih lekcij

- **Lekcija 1**: Agenti so sistemi, ne samo modeli. Zaznavajo, premišljajo, ukrepajo.  
- **Lekcija 2**: Microsoft Agent Framework poenostavlja kompleksnost klicev orodij in upravljanje stanja.  
- **Lekcija 3**: Oblikujte z mislijo na transparentnost in uporabniški nadzor.  
- **Lekcija 4**: Orodja so "roke" agenta. Definicija sheme je ključna, da LLM ve, kako jih uporabljati.  
- **Lekcija 7**: Načrtovanje je "izvršna funkcija" agenta, ki mu omogoča reševanje zapletenih delovnih tokov.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Opozorilo**:
To besedilo je bilo prevedeno z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvorni jezik šteje za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->