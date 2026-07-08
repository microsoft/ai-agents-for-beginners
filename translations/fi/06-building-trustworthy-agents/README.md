[![Luotettavat tekoälyagentit](../../../translated_images/fi/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Napsauta yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Luotettavien tekoälyagenttien rakentaminen

## Johdanto

Tämä oppitunti kattaa:

- Kuinka rakentaa ja ottaa käyttöön turvallisia ja tehokkaita tekoälyagentteja
- Tärkeitä turvallisuuteen liittyviä seikkoja tekoälyagenttien kehittämisessä.
- Kuinka ylläpitää tietojen ja käyttäjien yksityisyyttä tekoälyagentteja kehitettäessä.

## Oppimistavoitteet

Tämän oppitunnin suorittamisen jälkeen osaat:

- Tunnistaa ja lieventää riskejä tekoälyagentteja luotaessa.
- Toteuttaa turvallisuustoimenpiteitä varmistaaksesi, että tiedot ja käyttöoikeudet ovat asianmukaisesti hallinnassa.
- Luoda tekoälyagentteja, jotka ylläpitävät tietosuojaa ja tarjoavat laadukkaan käyttäjäkokemuksen.

## Turvallisuus

Katsotaan ensin, kuinka rakennetaan turvallisia agenttisovelluksia. Turvallisuus tarkoittaa, että tekoälyagentti toimii suunnitellusti. Agenttisovellusten rakentajina meillä on menetelmiä ja työkaluja turvallisuuden maksimoimiseksi:

### Järjestelmäviestikehyksen rakentaminen

Jos olet koskaan rakentanut tekoälysovellusta suuren kielimallin (LLM) avulla, tiedät, kuinka tärkeää on suunnitella vahva järjestelmän kehotus tai järjestelmäviesti. Nämä kehotukset määrittelevät meta-säännöt, ohjeet ja toimintaperiaatteet, joiden mukaan LLM vuorovaikuttaa käyttäjän ja datan kanssa.

Tekoälyagenttien kohdalla järjestelmäkehote on vielä tärkeämpi, sillä tekoälyagentit tarvitsevat erittäin tarkat ohjeet suorittaakseen niille määritellyt tehtävät.

Skaalautuvien järjestelmäkehoteiden luomiseksi voimme käyttää järjestelmäviestikehystä rakentaessamme yhtä tai useampaa agenttia sovellukseemme:

![Järjestelmäviestikehyksen rakentaminen](../../../translated_images/fi/system-message-framework.3a97368c92d11d68.webp)

#### Vaihe 1: Luo meta-järjestelmäviesti

Meta-kehotusta käyttää LLM luodakseen järjestelmäviestit agenteille, joita luomme. Suunnittelemme sen malliksi, jotta voimme tehokkaasti luoda useita agenteja tarvittaessa.

Tässä on esimerkki meta-järjestelmäviestistä, jonka antaisimme LLM:lle:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Vaihe 2: Luo peruskehotus

Seuraava vaihe on luoda peruskehotus kuvaamaan tekoälyagenttia. Sinun tulisi sisällyttää agentin rooli, agentin suorittamat tehtävät ja muut agentin vastuut.

Tässä on esimerkki:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Vaihe 3: Anna perusjärjestelmäviesti LLM:lle

Nyt voimme optimoida tämän järjestelmäviestin antamalla meta-järjestelmäviestin järjestelmäviestinä ja perusjärjestelmäviestimme.

Tämä tuottaa järjestelmäviestin, joka on paremmin suunniteltu ohjaamaan tekoälyagenttejämme:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### Vaihe 4: Toista ja paranna

Tämän järjestelmäviestikehyksen arvo on siinä, että järjestelmäviestien luominen useilta agenteilta skaalautuu helpommin ja että järjestelmäviestejä voi parantaa ajan myötä. On harvinaista, että sinulla olisi järjestelmäviesti, joka toimii täydellisesti heti ensimmäisellä kerralla käyttötarkoitukseesi. Pienten säätöjen ja parannusten tekeminen muuttamalla perusjärjestelmäviestiä ja ajamalla se järjestelmän läpi antaa mahdollisuuden vertailla ja arvioida tuloksia.

## Uhkien ymmärtäminen

Rakentaaksesi luotettavia tekoälyagentteja on tärkeää ymmärtää ja lieventää riskejä ja uhkia tekoälyagentillesi. Katsotaan joitain erilaisia tekoälyagentteihin kohdistuvia uhkia ja sitä, miten voit paremmin suunnitella ja varautua niihin.

![Uhkien ymmärtäminen](../../../translated_images/fi/understanding-threats.89edeada8a97fc0f.webp)

### Tehtävä ja ohjeistus

**Kuvaus:** Hyökkääjät yrittävät muuttaa tekoälyagentin ohjeita tai tavoitteita ohjeistuksen tai syötteiden manipuloinnin kautta.

**Lievitys**: Suorita validointitarkistuksia ja syötteiden suodatusta havaitaaksesi mahdollisesti vaaralliset kehotukset ennen kuin tekoälyagentti käsittelee ne. Koska nämä hyökkäykset vaativat tyypillisesti toistuvaa vuorovaikutusta agentin kanssa, keskustelukierrosten rajoittaminen on toinen tapa estää tämän tyyppiset hyökkäykset.

### Pääsy kriittisiin järjestelmiin

**Kuvaus:** Jos tekoälyagentilla on pääsy järjestelmiin ja palveluihin, jotka tallentavat arkaluontoisia tietoja, hyökkääjät voivat vaarantaa viestinnän agentin ja näiden palveluiden välillä. Nämä voivat olla suoria hyökkäyksiä tai epäsuoria yrityksiä saada tietoa näistä järjestelmistä agentin kautta.

**Lievitys:** Tekoälyagenttien tulisi saada järjestelmiin pääsy vain tarpeen mukaan tämän tyyppisten hyökkäysten estämiseksi. Viestinnän agentin ja järjestelmän välillä tulisi myös olla turvallista. Todennuksen ja pääsynhallinnan käyttöönotto on toinen tapa suojella tätä tietoa.

### Resurssien ja palveluiden ylikuormitus

**Kuvaus:** Tekoälyagentit voivat käyttää erilaisia työkaluja ja palveluita suorittaakseen tehtäviä. Hyökkääjät voivat käyttää tätä kykyä hyökkäyksiin lähettämällä suuria määriä pyyntöjä tekoälyagentin kautta, mikä saattaa aiheuttaa järjestelmävirheitä tai suuria kustannuksia.

**Lievitys:** Ota käyttöön käytännöt, jotka rajoittavat tekoälyagentin tekemien pyyntöjen määrää palveluun. Keskustelukierrosten ja tekoälyagentille tehtyjen pyyntöjen rajoittaminen on toinen tapa ehkäistä tämän tyyppisiä hyökkäyksiä.

### Tietopohjan myrkyttäminen

**Kuvaus:** Tämä hyökkäystyyppi ei kohdistu suoraan tekoälyagenttiin vaan tietopohjaan ja muihin palveluihin, joita agentti käyttää. Se voi sisältää datan tai tiedon korruptoimisen, jota tekoälyagentti käyttää tehtävien suorittamiseen, mikä johtaa puolueellisiin tai tahattomiin vastauksiin käyttäjälle.

**Lievitys:** Suorita säännöllinen datan tarkastus, jota tekoälyagentti käyttää työnkuluissaan. Varmista, että tämän datan käyttö on turvallista ja että dataa muuttavat vain luotettavat henkilöt tämän tyyppisen hyökkäyksen välttämiseksi.

### Virheiden ketjuttuminen

**Kuvaus:** Tekoälyagentit käyttävät eri työkaluja ja palveluita tehtävien suorittamiseen. Hyökkääjien aiheuttamat virheet voivat johtaa muiden agenttiin liitettyjen järjestelmien vikaantumiseen, jolloin hyökkäys leviää laajemmaksi ja vianmääritys vaikeutuu.

**Lievitys:** Yksi tapa välttää tätä on saada tekoälyagentti toimimaan rajoitetussa ympäristössä, kuten suorittamaan tehtäviä Docker-kontissa, estämään suorat järjestelmähyökkäykset. Varajärjestelmien ja uudelleenyrittämisen logiikan luominen, kun jotkin järjestelmät vastaavat virheellä, on toinen tapa estää suurempia järjestelmävirheitä.

## Ihminen silmukassa

Toinen tehokas tapa rakentaa luotettavia tekoälyagenttijärjestelmiä on ihmisen osallistaminen (Human-in-the-loop). Tämä luo prosessin, jossa käyttäjät voivat antaa palautetta agenteille suorituksen aikana. Käyttäjät toimivat ikään kuin agenteina moniagenttisessa järjestelmässä, antaen hyväksynnän tai keskeytyksen käynnissä olevalle prosessille.

![Ihminen silmukassa](../../../translated_images/fi/human-in-the-loop.5f0068a678f62f4f.webp)

Tässä on koodiesimerkki Microsoft Agent Frameworkin avulla, joka näyttää kuinka tämä konsepti toteutetaan:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Luo palveluntarjoaja, jossa on ihmisen hyväksyntä
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Luo agentti, jossa on ihmisen hyväksymisvaihe
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Käyttäjä voi tarkistaa ja hyväksyä vastauksen
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Yhteenveto

Luotettavien tekoälyagenttien rakentaminen vaatii huolellista suunnittelua, vahvoja turvallisuustoimenpiteitä ja jatkuvaa kehitystä. Rakentamalla strukturoituja meta-kehotusjärjestelmiä, ymmärtämällä potentiaaliset uhat ja soveltamalla lieventämisstrategioita kehittäjät voivat luoda turvallisia ja tehokkaita tekoälyagentteja. Lisäksi ihmisen osallistaminen prosessiin varmistaa, että tekoälyagentit pysyvät käyttäjän tarpeiden mukaisina ja riskit minimoidaan. Tekoälyn kehittyessä turvallisuuden, yksityisyyden ja eettisten näkökohtien ennakoiva hallinta on avain luottamuksen ja luotettavuuden edistämiseen tekoälypohjaisissa järjestelmissä.

## Koodiesimerkit

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Askeltainen demonstrointi meta-kehotusjärjestelmäviestikehyksestä.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Toimenpiteitä edeltävät hyväksyntäportit, riskiluokitus ja tarkastuslokitus luotettaville agenteille.

### Onko sinulla lisää kysymyksiä luotettavien tekoälyagenttien rakentamisesta?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua vastaanottoaikoihin ja saada vastauksia tekoälyagenttikysymyksiisi.

## Lisäresurssit

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Vastuullisen tekoälyn yleiskatsaus</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatiivisten tekoälymallien ja tekoälysovellusten arviointi</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Turvallisuusjärjestelmäviestit</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Riskinarviointimalli</a>

## Edellinen oppitunti

[Agenttinen RAG](../05-agentic-rag/README.md)

## Seuraava oppitunti

[Suunnittelumalli](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->