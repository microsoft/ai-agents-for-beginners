# AI-agentit aloittelijoille - Opas ja kurssin yhteenveto

Tämä opas tarjoaa yhteenvedon "AI Agents for Beginners" -kurssista ja selittää keskeisiä käsitteitä, kehyksiä ja suunnittelumalleja AI-agenttien rakentamiseen.

## 1. Johdanto AI-agentteihin

**Mitä AI-agentit ovat?**  
AI-agentit ovat järjestelmiä, jotka laajentavat suurien kielimallien (LLM) kyvykkyyksiä antamalla niille pääsyn **työkaluihin**, **tietoon** ja **muistiin**. Toisin kuin tavallinen LLM-pohjainen chatbot, joka ainoastaan tuottaa tekstiä koulutusdatan perusteella, AI-agentti voi:  
- **Havainnoida** ympäristöään (antureiden tai syötteiden kautta).  
- **Pohdiskella** ongelmanratkaisua.  
- **Toimia** muuttaakseen ympäristöä (toimintamekanismien tai työkalujen avulla).

**Agentin keskeiset osat:**  
- **Ympäristö**: Tila, jossa agentti toimii (esim. varausjärjestelmä).  
- **Anturit**: Tiedonkeruumenetelmät (esim. API-kutsun lukeminen).  
- **Toimijat**: Toimintamekanismit (esim. sähköpostin lähetys).  
- **Aivot (LLM)**: Päättelymoottori, joka suunnittelee ja päättää toimenpiteistä.

## 2. Agenttikehykset

Kurssi käyttää **Microsoft Agent Frameworkia (MAF)** ja **Azure AI Foundry Agent Service V2:**ta agenttien rakentamiseen:

| Komponentti | Painopiste | Parhaiten soveltuu |
|-------------|------------|--------------------|
| **Microsoft Agent Framework** | Yhtenäinen Python/C# SDK agenteille, työkaluille ja työnkuluillle | Agenttien rakentamiseen työkaluilla, moniagenttityönkuluille ja tuotantomalleille. |
| **Azure AI Foundry Agent Service** | Hallittu pilvitoiminta-aika | Turvallinen, skaalautuva käyttöönotto sisäisellä tilanhallinnalla, havaittavuudella ja luottamuksella. |

## 3. Agenttien suunnittelumallit

Suunnittelumallit auttavat jäsentämään, miten agentit toimivat ongelmien ratkaisemiseksi luotettavasti.

### **Työkalun käyttö -malli** (Luento 4)  
Tämä malli mahdollistaa agenttien vuorovaikutuksen ulkomaailman kanssa.  
- **Käsite**: Agentille annetaan "skeema" (lista käytettävissä olevista funktioista ja niiden parametreista). LLM päättää *minkä* työkalun kutsuu ja *millä* argumenteilla käyttäjän pyynnön perusteella.  
- **Toimintaketju**: Käyttäjän pyyntö -> LLM -> **Työkalun valinta** -> **Työkalun suoritus** -> LLM (työkalun tulosten kanssa) -> Lopullinen vastaus.  
- **Käyttötapaukset**: Reaaliaikaisen datan hakeminen (sää, osakekurssit), laskelmien tekeminen, koodin suoritus.

### **Suunnittelumalli** (Luento 7)  
Tämä malli mahdollistaa agenttien ratkaista monimutkaisia, usean vaiheen tehtäviä.  
- **Käsite**: Agentti pilkkoo korkean tason tavoitteen sarjaksi pienempiä alatehtäviä.  
- **Lähestymistavat**:  
  - **Tehtävän pilkkominen**: "Suunnittele matka" jaetaan "Varaa lento", "Varaa hotelli", "Vuokraa auto" -osatehtäviin.  
  - **Iteratiivinen suunnittelu**: Suunnitelman uudelleenarviointi aiempien vaiheiden tulosten perusteella (esim. jos lento on täynnä, valitaan eri päivämäärä).  
- **Toteutus**: Usein mukana "Planner"-agentti, joka luo rakenteellisen suunnitelman (esim. JSON), jota muut agentit sitten toteuttavat.

## 4. Suunnitteluperiaatteet

Agentteja suunniteltaessa on otettava huomioon kolme ulottuvuutta:  
- **Tila**: Agenttien tulee yhdistää ihmiset ja tieto, olla saavutettavissa mutta huomaamattomia.  
- **Aika**: Agentit oppivat *menneestä*, tarjoavat merkityksellisiä vihjeitä *nyt* ja sopeutuvat *tulevaan*.  
- **Ydin**: Epävarmuus hyväksytään, mutta luottamus rakennetaan läpinäkyvyydellä ja käyttäjän kontrollilla.

## 5. Avainopetusten yhteenveto

- **Luento 1**: Agentit ovat järjestelmiä, eivät pelkkiä malleja. Ne havaitsevat, päättävät ja toimivat.  
- **Luento 2**: Microsoft Agent Framework abstrahoi työkalukutsujen ja tilanhallinnan monimutkaisuutta.  
- **Luento 3**: Suunnittele läpinäkyvyys ja käyttäjän kontrolli mielessä.  
- **Luento 4**: Työkalut ovat agentin "kädet". Skeeman määrittely on ratkaisevaa, jotta LLM ymmärtää niiden käytön.  
- **Luento 7**: Suunnittelu on agentin "toimeenpaneva toiminto", joka mahdollistaa monimutkaisten työnkulkujen hallinnan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty tekoälypohjaisen käännöspalvelun [Co-op Translator](https://github.com/Azure/co-op-translator) avulla. Pyrimme tarkkuuteen, mutta automatisoiduissa käännöksissä voi olla virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen omalla kielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä aiheutuvista väärinkäsityksistä tai virhetulkinnasta.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->