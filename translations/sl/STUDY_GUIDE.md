# AI agenti za začetnike - študijski vodič in povzetek tečaja

Ta vodič ponuja povzetek tečaja "AI agenti za začetnike" in pojasnjuje ključne koncepte, ogrodja ter oblikovne vzorce za gradnjo AI agentov.

## 1. Uvod v AI agente

**Kaj so AI agenti?**
AI agenti so sistemi, ki razširjajo zmogljivosti velikih jezikovnih modelov (LLM) z omogočanjem dostopa do **orodij**, **znanja** in **spomina**. Za razliko od običajnega LLM klepetalnika, ki le generira besedilo na podlagi učnih podatkov, AI agent lahko:
- **Zaznava** svoje okolje (prek senzorjev ali vhodov).
- **Razmišlja** o tem, kako rešiti problem.
- **Ukrep(a)** za spremembo okolja (prek aktuatorjev ali izvajanja orodij).

**Ključne sestavine agenta:**
- **Okolje**: Prostor, kjer agent deluje (npr. sistem za rezervacije).
- **Senzorji**: Mehanizmi za zbiranje informacij (npr. branje API-ja).
- **Aktuatorji**: Mehanizmi za izvajanje dejanj (npr. pošiljanje e-pošte).
- **Možgani (LLM)**: Razumski motor, ki načrtuje in odloča, katera dejanja izvesti.

## 2. Okvirji za agente

V tečaju se uporablja **Microsoft Agent Framework (MAF)** z **Azure AI Foundry Agent Service V2** za gradnjo agentov:

| Komponenta | Osredotočenost | Najbolj primerno za |
|------------|----------------|---------------------|
| **Microsoft Agent Framework** | Enotno Python/C# SDK za agente, orodja in delovne tokove | Gradnjo agentov z orodji, večagentne delovne tokove in proizvodne vzorce. |
| **Azure AI Foundry Agent Service** | Upravljano oblačno izvajanje | Varen, razširljiv zapis z vgrajenim upravljanjem stanja, opazovanjem in zaupanjem. |

## 3. Oblikovni vzorci za agente

Oblikovni vzorci pomagajo strukturirati delovanje agentov za zanesljivo reševanje problemov.

### **Vzorec uporabe orodij** (Lekcija 4)  
Ta vzorec omogoča agentom interakcijo z zunanjim svetom.
- **Koncept**: Agentu je podana "shema" (seznam razpoložljivih funkcij in njihovih parametrov). LLM se odloči, *katero* orodje poklicati in s *katerimi* argumenti na podlagi uporabnikove zahteve.
- **Potek**: Zahteva uporabnika -> LLM -> **Izbira orodja** -> **Izvajanje orodja** -> LLM (z izhodom orodja) -> Končni odgovor.
- **Primeri uporabe**: Pridobivanje podatkov v realnem času (vreme, cene delnic), izvajanje izračunov, izvajanje kode.

### **Vzorec načrtovanja** (Lekcija 7)  
Ta vzorec omogoča agentom reševanje zapletenih, večstopenjskih nalog.
- **Koncept**: Agent razbije visoko raven cilja v zaporedje manjših podnalog.
- **Pristopi**:  
  - **Razčlenitev naloge**: Razdelitev „Načrtuj potovanje“ na „Rezerviraj let“, „Rezerviraj hotel“, „Najemi avto“.  
  - **Iterativno načrtovanje**: Ponovno ocenjevanje načrta glede na izide prejšnjih korakov (npr. če je let poln, izberi drug datum).  
- **Implementacija**: Pogosto vključuje agenta "Načrtovalca", ki ustvari strukturiran načrt (npr. JSON), ki ga nato izvajajo drugi agenti.

## 4. Oblikovanjske smernice

Pri oblikovanju agentov upoštevajte tri dimenzije:
- **Prostor**: Agenti naj povezujejo ljudi in znanje, naj bodo dostopni, a neopazni.
- **Čas**: Agenti se učijo iz *preteklosti*, nudijo ustrezne spodbude v *sedanjosti* in se prilagajajo za *prihodnost*.
- **Jedro**: Sprejemajte negotovost, a vzpostavite zaupanje z odprtostjo in nadzorom uporabnika.

## 5. Povzetek ključnih lekcij

- **Lekcija 1**: Agenti so sistemi, ne zgolj modeli. Zaznavajo, razmišljajo in ukrepajo.
- **Lekcija 2**: Microsoft Agent Framework poenostavi kompleksnost klicanja orodij in upravljanja stanja.
- **Lekcija 3**: Oblikujte z mislijo na odprtost in nadzor uporabnika.
- **Lekcija 4**: Orodja so "roke" agenta. Definicija sheme je ključna, da LLM razume, kako jih uporabljati.
- **Lekcija 7**: Načrtovanje je "izvršna funkcija" agenta, ki mu omogoča reševanje zahtevnih delovnih tokov.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Originalni dokument v izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne prevzemamo odgovornosti.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->