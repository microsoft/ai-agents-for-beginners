# AI-agentit aloittelijoille - Opas ja kurssin yhteenveto

Tämä opas tarjoaa yhteenvetona "AI Agents for Beginners" -kurssin ja selittää keskeiset käsitteet, kehykset ja suunnittelumallit AI-agenttien rakentamiseen.

## 1. Johdanto AI-agentteihin

**Mitä AI-agentit ovat?**  
AI-agentit ovat järjestelmiä, jotka laajentavat suurten kielimallien (LLM) kykyjä antamalla niille pääsyn **työkaluihin**, **tietoon** ja **muistiin**. Toisin kuin tavallinen LLM-pohjainen chatbot, joka vain tuottaa tekstiä koulutusdatan perusteella, AI-agentti voi:  
- **Havaita** ympäristönsä (sensoreiden tai syötteiden kautta).  
- **Päättää** miten ratkaista ongelma.  
- **Toimia** ympäristön muuttamiseksi (toimilaitteiden tai työkalujen suorittamisen kautta).  

**Agentin keskeiset osat:**  
- **Ympäristö**: tila, jossa agentti toimii (esim. varausjärjestelmä).  
- **Sensorit**: mekanismit tiedon keräämiseen (esim. API-kutsun lukeminen).  
- **Toimilaitteet**: mekanismit toimien suorittamiseen (esim. sähköpostin lähettäminen).  
- **Aivot (LLM)**: päättelymoottori, joka suunnittelee ja päättää toiminnoista.

## 2. Agenttikehykset

Kurssilla käsitellään kolmea pääkehystä agenttien rakentamiseen:

| Kehys | Keskittyminen | Paras käyttötarkoitus |
|-------|---------------|----------------------|
| **Semantic Kernel** | Tuotantovalmis SDK .NET/Python-käyttöön | Yrityssovellukset, tekoälyn integrointi olemassa olevaan koodiin. |
| **AutoGen** | Moni-agenttiyhteistyö | Monimutkaiset tilanteet, joissa useat erikoistuneet agentit kommunikoivat keskenään. |
| **Azure AI Agent Service** | Hallittu pilvipalvelu | Turvallinen, skaalautuva käyttöönotto sisäänrakennetulla tilanhallinnalla. |

## 3. Agenttien suunnittelumallit

Suunnittelumallit auttavat jäsentämään, miten agentit toimivat luotettavasti ongelmanratkaisussa.

### **Työkalujen käyttö -malli** (Luku 4)  
Tämä malli mahdollistaa agenttien vuorovaikutuksen ulkomaailman kanssa.  
- **Käsite**: Agentille annetaan "skeema" (lista käytettävissä olevista funktioista ja niiden parametreistä). LLM päättää *minkä* työkalun kutsuu ja *millä* argumenteilla käyttäjän pyynnön perusteella.  
- **Virtaus**: Käyttäjän pyyntö -> LLM -> **Työkalun valinta** -> **Työkalun suoritus** -> LLM (työkalun tuloksella) -> Loppuvastaus.  
- **Käyttötapaukset**: Reaaliaikaisen datan hakeminen (sää, osakekurssit), laskelmien tekeminen, koodin suoritus.

### **Suunnittelumalli** (Luku 7)  
Tämä malli mahdollistaa agenttien ratkaista monimutkaisia, vaiheittaisia tehtäviä.  
- **Käsite**: Agentti pilkkoo korkean tason tavoitteen useisiin pienempiin alatehtäviin.  
- **Lähestymistavat**:  
  - **Tehtävien pilkkominen**: "Suunnittele matka" jaetaan "Varaa lento", "Varaa hotelli", "Vuokraa auto".  
  - **Iteratiivinen suunnittelu**: Suunnitelman arviointi uudelleen aiempien vaiheiden tulosten perusteella (esim. jos lento on täynnä, valitaan toinen päivä).  
- **Toteutus**: Usein "Suunnittelija"-agentti luo rakenteellisen suunnitelman (esim. JSON-muodossa), jonka muut agentit toteuttavat.

## 4. Suunnitteluperiaatteet

Agentteja suunniteltaessa on otettava huomioon kolme ulottuvuutta:  
- **Tila**: Agenttien tulee yhdistää ihmiset ja tieto, olla saavutettavia mutta huomaamattomia.  
- **Aika**: Agenttien tulee oppia *menneisyydestä*, tarjota olennaisia vihjeitä *nyt* ja sopeutua *tulevaisuutta* varten.  
- **Ydin**: Hyväksy epävarmuus mutta luo luottamus avoimuuden ja käyttäjän hallinnan avulla.

## 5. Keskeisten oppien yhteenveto

- **Luku 1**: Agentit ovat järjestelmiä, eivät pelkästään malleja. Ne havaitsevat, päättävät ja toimivat.  
- **Luku 2**: Kehykset kuten Semantic Kernel ja AutoGen abstrahoivat työkalupyyntöjen ja tilanhallinnan monimutkaisuutta.  
- **Luku 3**: Suunnittele avoimuus ja käyttäjän hallinta mielessä.  
- **Luku 4**: Työkalut ovat agentin "kädet". Skeeman määrittely on ratkaisevaa, jotta LLM ymmärtää työkalujen käytön.  
- **Luku 7**: Suunnittelu on agentin "toiminnanjohto", joka mahdollistaa monimutkaisten prosessien hallinnan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta ole hyvä ja huomioi, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on ratkaiseva lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai virheellisistä tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->