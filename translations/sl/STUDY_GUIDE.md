# AI agenti za začetnike - študijski vodič in povzetek tečaja

Ta vodič ponuja povzetek tečaja "AI agenti za začetnike" in pojasnjuje ključne koncepte, okvire in oblikovne vzorce za gradnjo AI agentov.

## 1. Uvod v AI agente

**Kaj so AI agenti?**  
AI agenti so sistemi, ki razširjajo zmožnosti velikih jezikovnih modelov (LLM) tako, da jim omogočajo dostop do **orodij**, **znanja** in **spomina**. V nasprotju s standardnim klepetalnim robotom LLM, ki le generira besedilo na podlagi učnih podatkov, AI agent lahko:  
- **Zaznava** svoje okolje (prek senzorjev ali vhodov).  
- **Razmišlja** o tem, kako rešiti problem.  
- **Ukvarja se** s spreminjanjem okolja (prek aktuatorjev ali izvrševanja orodij).

**Ključne sestavine agenta:**  
- **Okolje**: prostor, kjer agent deluje (npr. sistem za rezervacije).  
- **Senzorji**: mehanizmi za zbiranje informacij (npr. branje API-ja).  
- **Aktuatorji**: mehanizmi za izvajanje dejanj (npr. pošiljanje e-pošte).  
- **Možgani (LLM)**: sistem za razmišljanje, ki načrtuje in odloča, katera dejanja izvesti.

## 2. Okviri za agente

Tečaj pokriva tri glavne okvire za gradnjo agentov:

| Okvir | Osredotočenost | Najprimernejši za |
|-----------|-------|----------|
| **Semantic Kernel** | SDK pripravljen za produkcijo za .NET/Python | Poslovne aplikacije, integracijo AI z obstoječo kodo. |
| **AutoGen** | Sodelovanje več agentov | Kompleksni scenariji, ki zahtevajo več specializiranih agentov, ki medsebojno komunicirajo. |
| **Azure AI Agent Service** | Upravljana oblačna storitev | Varnostna, razširljiva namestitev z vgrajenim upravljanjem stanja. |

## 3. Oblikovni vzorci za agente

Oblikovni vzorci pomagajo strukturirati način delovanja agentov za zanesljivo reševanje problemov.

### **Vzorec uporabe orodij** (Lekcija 4)  
Ta vzorec omogoča agentom, da komunicirajo z zunanjim svetom.  
- **Koncept**: Agentu je na voljo "shema" (seznam razpoložljivih funkcij in njihovih parametrov). LLM se odloči, *katero* orodje poklicati in s *katerimi* argumenti na podlagi uporabnikove zahteve.  
- **Tok**: Uporabnikova zahteva -> LLM -> **Izbira orodja** -> **Izvajanje orodja** -> LLM (z izhodom orodja) -> Končni odgovor.  
- **Uporabe**: Pridobivanje podatkov v realnem času (vreme, cene delnic), izvajanje izračunov, izvajanje kode.

### **Vzorec načrtovanja** (Lekcija 7)  
Ta vzorec omogoča agentom reševanje kompleksnih, večfaznih nalog.  
- **Koncept**: Agent razčleni visok nivo cilj v vrsto manjših podnalog.  
- **Pristopi**:  
  - **Razčlenitev naloge**: razdelitev "Načrtuj potovanje" na "Rezerviraj let", "Rezerviraj hotel", "Najemi avto".  
  - **Iterativno načrtovanje**: ponovno vrednotenje načrta na podlagi rezultatov prejšnjih korakov (npr. če je let poln, izberi drug datum).  
- **Izvedba**: Pogosto vključuje agenta "načrtovalca", ki ustvari strukturiran načrt (npr. JSON), ki ga nato izvajajo drugi agenti.

## 4. Načela oblikovanja

Pri oblikovanju agentov upoštevajte tri dimenzije:  
- **Prostor**: Agenti naj povezujejo ljudi in znanje, naj bodo dostopni, a nevsiljivi.  
- **Čas**: Agenti se učijo iz *preteklosti*, nudijo ustrezne spodbude v *sedanjosti* in se prilagajajo za *prihodnost*.  
- **Jezgro**: Sprejmite negotovost, a vzpostavite zaupanje z uporabo preglednosti in nadzora uporabnika.

## 5. Povzetek ključnih lekcij

- **Lekcija 1**: Agenti so sistemi, ne le modeli. Zaznavajo, razmišljajo in ukrepajo.  
- **Lekcija 2**: Okviri, kot sta Semantic Kernel in AutoGen, poenostavljajo kompleksnost klicanja orodij in upravljanje stanja.  
- **Lekcija 3**: Oblikujte z mislijo na preglednost in nadzor uporabnika.  
- **Lekcija 4**: Orodja so "roke" agenta. Definicija sheme je ključna, da LLM razume, kako jih uporabljati.  
- **Lekcija 7**: Načrtovanje je "izvršna funkcija" agenta, ki mu omogoča reševanje kompleksnih delovnih tokov.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvornega jeziku velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->