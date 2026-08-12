# AI-agentit aloittelijoille - Opas ja kurssiyhteenveto

Tämä opas tarjoaa yhteenvedon "AI Agents for Beginners" -kurssista ja selittää keskeiset käsitteet, kehykset ja suunnittelumallit AI-agenttien rakentamiseen.

## 1. Johdatus AI-agentteihin

**Mitä AI-agentit ovat?**  
AI-agentit ovat järjestelmiä, jotka laajentavat suurten kielimallien (LLM) kykyjä antamalla niille pääsyn **työkaluihin**, **tietoon** ja **muistiin**. Toisin kuin tavallinen LLM-chatbot, joka tuottaa tekstiä vain koulutusdatan perusteella, AI-agentti voi:  
- **Havaita** ympäristönsä (antureiden tai syötteiden kautta).  
- **Päättellä**, miten ongelma ratkaistaan.  
- **Toimia** muutoksen aikaansaamiseksi ympäristössä (toimilaitteiden tai työkalujen avulla).

**Agentin keskeiset osat:**  
- **Ympäristö**: Tilatila, jossa agentti toimii (esim. varausjärjestelmä).  
- **Anturit**: Tiedonkeruumenetelmät (esim. API-kutsun lukeminen).  
- **Toimilaitteet**: Toimintojen suorittamisen menetelmät (esim. sähköpostin lähetys).  
- **Aivot (LLM)**: Päättelymoottori, joka suunnittelee ja päättää toimenpiteistä.

## 2. Agenttikehykset

Kurssilla käytetään **Microsoft Agent Framework (MAF)** -kehystä ja **Azure AI Foundry Agent Service V2** -palvelua agenttien rakentamiseen:

| Komponentti | Keskittyminen | Paras käyttö |
|-------------|---------------|--------------|
| **Microsoft Agent Framework** | Yhtenäinen Python/C#-SDK agenteille, työkaluissa ja työnkuluissa | Agenttien rakentaminen työkaluilla, moniagenttityönkulut ja tuotantokuvioissa. |
| **Azure AI Foundry Agent Service** | Hallittu pilviajoaika | Turvallinen, skaalautuva käyttöönotto sisäänrakennetulla tilanhallinnalla, valvonnalla ja luottamuksella. |

## 3. Agenttisuunnittelumallit

Suunnittelumallit auttavat jäsentämään, miten agentit toimivat luotettavasti ongelmien ratkaisemiseksi.

### **Työkalujen käyttömalli** (Luento 4)  
Tämä malli mahdollistaa agenttien vuorovaikutuksen ulkomaailman kanssa.  
- **Käsite**: Agentille annetaan "skeema" (lista käytettävissä olevista funktioista ja niiden parametreista). LLM päättää, *minkä* työkalun kutsuu ja *millä* argumenteilla käyttäjän pyynnön perusteella.  
- **Kulku**: Käyttäjän pyyntö -> LLM -> **Työkalun valinta** -> **Työkalun suoritus** -> LLM (työkalun tuloksilla) -> Lopullinen vastaus.  
- **Käyttötapaukset**: Reaaliaikaisen datan hakeminen (sää, osakekurssit), laskentojen tekeminen, koodin suoritus.

### **Suunnittelumalli** (Luento 7)  
Tämä malli mahdollistaa agenttien monivaiheisten, monimutkaisten tehtävien ratkaisun.  
- **Käsite**: Agentti jakaa korkean tason tavoitteen pienempiin osatehtäviin.  
- **Lähestymistavat**:  
  - **Tehtävien pilkkominen**: Esim. "Suunnittele matka" pilkotaan "Varaa lento", "Varaa hotelli", "Vuokraa auto" -osiksi.  
  - **Iteratiivinen suunnittelu**: Suunnitelman uudelleenarviointi aiempien vaiheiden tulosten perusteella (esim. jos lento on täynnä, valitaan eri päivä).  
- **Toteutus**: Usein "Suunnittelija"-agentti generoi rakenteellisen suunnitelman (esim. JSON), jonka muut agentit toteuttavat.

## 4. Suunnitteluperiaatteet

Agentteja suunniteltaessa on otettava huomioon kolme ulottuvuutta:  
- **Tila**: Agenttien tulisi yhdistää ihmiset ja tieto, olla saavutettavissa mutta huomaamattomia.  
- **Aika**: Agenttien tulisi oppia *menneestä*, tarjota merkityksellisiä vihjeitä *nykyhetkessä* ja sopeutua *tulevaan*.  
- **Ydin**: Hyväksy epävarmuus mutta rakenna luottamus avoimuuden ja käyttäjän ohjauksen kautta.

## 5. Keskeiset oppitunnit lyhyesti

- **Luento 1**: Agentit ovat järjestelmiä, eivät pelkästään malleja. Ne havaitsevat, päättävät ja toimivat.  
- **Luento 2**: Microsoft Agent Framework abstrahoi työkalukutsujen ja tilanhallinnan monimutkaisuuden.  
- **Luento 3**: Suunnittele avoimuutta ja käyttäjän hallintaa ajatellen.  
- **Luento 4**: Työkalut ovat agentin "kädet". Skeeman määrittely on ratkaisevaa, jotta LLM ymmärtää niiden käytön.  
- **Luento 7**: Suunnittelu on agentin "johtotoiminto", joka mahdollistaa monimutkaisten työnkulkujen hallinnan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta ota huomioon, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä tiedoissa suosittelemme ammattimaisen kääntäjän käyttöä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->