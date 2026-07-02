[![Pouzdani AI agenti](../../../translated_images/hr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknite na gornju sliku za pregled videa ove lekcije)_

# Izgradnja pouzdanih AI agenata

## Uvod

Ova lekcija će obuhvatiti:

- Kako izgraditi i implementirati sigurne i učinkovite AI agente
- Važne sigurnosne razmatranja pri razvoju AI agenata
- Kako održavati privatnost podataka i korisnika pri razvoju AI agenata

## Ciljevi učenja

Nakon završetka ove lekcije, znat ćete kako:

- Identificirati i ublažiti rizike prilikom stvaranja AI agenata
- Primijeniti sigurnosne mjere kako biste osigurali pravilno upravljanje podacima i pristupom
- Stvoriti AI agente koji održavaju privatnost podataka i pružaju kvalitetno korisničko iskustvo

## Sigurnost

Prvo ćemo pogledati kako izgraditi sigurne agencijske aplikacije. Sigurnost znači da AI agent radi kako je dizajniran. Kao tvorci agencijskih aplikacija, imamo metode i alate za maksimiziranje sigurnosti:

### Izgradnja okvira za sistemsku poruku

Ako ste ikada gradili AI aplikaciju koristeći Velike jezične modele (LLM), znate važnost dizajniranja robusnog sistemskog prompta ili sistemske poruke. Ti promptovi uspostavljaju metaregle, upute i smjernice za to kako će LLM komunicirati s korisnikom i podacima.

Za AI agente, sistemski prompt je još važniji jer će AI agenti trebati vrlo specifične upute za dovršavanje zadataka koje smo im dodijelili.

Za stvaranje skalabilnih sistemskih promptova, možemo koristiti okvir sistemske poruke za izgradnju jednog ili više agenata u našoj aplikaciji:

![Izgradnja okvira sistemske poruke](../../../translated_images/hr/system-message-framework.3a97368c92d11d68.webp)

#### Korak 1: Kreirajte meta sistemsku poruku

Meta prompt će se koristiti od strane LLM-a za generiranje sistemskih promptova za agente koje stvaramo. Dizajniramo ga kao predložak kako bismo mogli učinkovito stvoriti više agenata ako je potrebno.

Evo primjera meta sistemske poruke koju bismo dali LLM-u:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Korak 2: Kreirajte osnovni prompt

Sljedeći korak je izraditi osnovni prompt za opis AI agenta. Trebali biste uključiti ulogu agenta, zadatke koje agent izvršava i sve druge odgovornosti agenta.

Evo primjera:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Korak 3: Dostavite osnovnu sistemsku poruku LLM-u

Sada možemo optimizirati ovu sistemsku poruku pružajući meta sistemsku poruku kao sistemsku poruku i našu osnovnu sistemsku poruku.

To će proizvesti sistemsku poruku koja je bolje dizajnirana za usmjeravanje naših AI agenata:

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

#### Korak 4: Iterirajte i poboljšavajte

Vrijednost ovog okvira sistemske poruke je u mogućnosti lakšeg skaliranja stvaranja sistemskih poruka za više agenata kao i poboljšavanje sistemskih poruka tijekom vremena. Rijetko ćete imati sistemsku poruku koja radi savršeno prvi put za vaš kompletan slučaj upotrebe. Mogućnost pravljenja malih prilagodbi i poboljšanja promjenom osnovne sistemske poruke i njenim ponovnim pokretanjem kroz sistem omogućuje usporedbu i evaluaciju rezultata.

## Razumijevanje prijetnji

Da biste izgradili pouzdane AI agente, važno je razumjeti i ublažiti rizike i prijetnje prema vašem AI agentu. Pogledajmo samo neke od različitih prijetnji AI agentima i kako se bolje možete planirati i pripremiti za njih.

![Razumijevanje prijetnji](../../../translated_images/hr/understanding-threats.89edeada8a97fc0f.webp)

### Zadatak i upute

**Opis:** Napadači pokušavaju promijeniti upute ili ciljeve AI agenta putem promptanja ili manipulacije ulazima.

**Ublažavanje**: Izvedite provjere valjanosti i filtre ulaza kako biste otkrili potencijalno opasne prompty prije nego što ih AI agent obradi. Budući da takvi napadi obično zahtijevaju čestu interakciju s agentom, ograničavanje broja okretaja u razgovoru je još jedan način za sprječavanje ovakvih napada.

### Pristup kritičnim sustavima

**Opis:** Ako AI agent ima pristup sustavima i uslugama koje pohranjuju osjetljive podatke, napadači mogu kompromitirati komunikaciju između agenta i tih usluga. To mogu biti direktni napadi ili indirektni pokušaji dobivanja informacija o tim sustavima putem agenta.

**Ublažavanje:** AI agenti bi trebali imati pristup sustavima samo prema potrebi radi sprječavanja ovakvih napada. Komunikacija između agenta i sustava također treba biti sigurna. Implementacija autentifikacije i kontrole pristupa je još jedan način zaštite ovih informacija.

### Preopterećenje resursa i usluga

**Opis:** AI agenti mogu pristupati različitim alatima i uslugama za dovršavanje zadataka. Napadači mogu iskoristiti ovu sposobnost za napad na te usluge slanjem velikog broja zahtjeva kroz AI agenta, što može rezultirati kvarovima sustava ili visokim troškovima.

**Ublažavanje:** Implementirajte politike za ograničavanje broja zahtjeva koje AI agent može poslati usluzi. Ograničavanje broja okretaja u razgovoru i zahtjeva prema vašem AI agentu još je jedan način za sprječavanje ovih napada.

### Trovanje baze znanja

**Opis:** Ova vrsta napada ne cilja direktno AI agenta, već cilja bazu znanja i druge usluge koje će AI agent koristiti. To može uključivati korumpiranje podataka ili informacija koje AI agent koristi za dovršetak zadatka, što dovodi do pristranih ili neželjenih odgovora korisniku.

**Ublažavanje:** Redovito provjeravajte podatke koje će AI agent koristiti u svojim tokovima rada. Osigurajte da pristup tim podacima bude siguran i da te podatke mijenjaju samo pouzdane osobe kako biste izbjegli ovu vrstu napada.

### Sljedstvene pogreške

**Opis:** AI agenti pristupaju raznim alatima i uslugama za dovršavanje zadataka. Pogreške prouzročene napadačima mogu dovesti do kvarova drugih sustava kojima je AI agent povezan, uzrokujući da napad postane rašireniji i teži za rješavanje.

**Ublažavanje:** Jedna metoda za izbjegavanje ovoga je da AI agent djeluje u ograničenom okruženju, poput izvršavanja zadataka u Docker kontejneru, kako bi se spriječili direktni napadi na sustav. Izrada mehanizama za rezervne opcije i logike ponovnog pokušaja kada određeni sustavi odgovore pogreškom je još jedan način za sprječavanje većih kvarova sustava.

## Čovjek u petlji

Još jedan učinkovit način za izgradnju pouzdanih AI agentskih sustava je korištenje čovjeka u petlji. To stvara tijek u kojem korisnici mogu pružiti povratnu informaciju agentima tijekom rada. Korisnici u suštini djeluju kao agenti u sustavu s više agenata pružajući odobrenje ili zaustavljanje pokrenutog procesa.

![Čovjek u petlji](../../../translated_images/hr/human-in-the-loop.5f0068a678f62f4f.webp)

Evo isječak koda koji koristi Microsoft Agent Framework za prikaz kako je ovaj koncept implementiran:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Kreirajte davatelja usluga s odobrenjem uključivanja čovjeka
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Kreirajte agenta s korakom odobrenja od strane čovjeka
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Korisnik može pregledati i odobriti odgovor
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Zaključak

Izgradnja pouzdanih AI agenata zahtijeva pažljiv dizajn, robusne sigurnosne mjere i kontinuiranu iteraciju. Primjenom strukturiranih meta prompting sustava, razumijevanjem potencijalnih prijetnji i primjenom strategija ublažavanja, programeri mogu stvarati AI agente koji su i sigurni i učinkoviti. Osim toga, uključivanje pristupa čovjeka u petlji osigurava da AI agenti ostanu usklađeni s potrebama korisnika dok se minimiziraju rizici. Kako AI nastavlja evoluirati, održavanje proaktivnog pristupa sigurnosti, privatnosti i etičkim pitanjima bit će ključno za poticanje povjerenja i pouzdanosti u sustavima pokretanima AI-jem.

## Primjeri koda

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Korak-po-korak demonstracija meta-prompting okvira sistemske poruke.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Prethodne kontrole odobrenja, razvrstavanje rizika i auditiranje za pouzdane agente.

### Imate li dodatna pitanja o izgradnji pouzdanih AI agenata?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) zajednici za susret s drugim učenicima, sudjelovanje u radnim satima i dobivanje odgovora na svoja pitanja o AI agentima.

## Dodatni resursi

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Pregled odgovorne uporabe AI-a</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluacija generativnih AI modela i AI aplikacija</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Sistemske poruke za sigurnost</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Predložak procjene rizika</a>

## Prethodna lekcija

[Agentni RAG](../05-agentic-rag/README.md)

## Sljedeća lekcija

[Obrazac dizajna planiranja](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->