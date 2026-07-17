[![Pouzdani AI agenti](../../../translated_images/hr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknite na gornju sliku za pregled video lekcije)_

# Izgradnja pouzdanih AI agenata

## Uvod

Ova lekcija će obuhvatiti:

- Kako izgraditi i implementirati sigurne i učinkovite AI agente
- Važne sigurnosne aspekte prilikom razvoja AI agenata.
- Kako održavati privatnost podataka i korisnika tijekom razvoja AI agenata.

## Ciljevi učenja

Nakon završetka ove lekcije, znat ćete kako:

- Identificirati i ublažiti rizike pri kreiranju AI agenata.
- Implementirati sigurnosne mjere za pravilan menadžment podataka i pristupa.
- Kreirati AI agente koji održavaju privatnost podataka i pružaju kvalitetno korisničko iskustvo.

## Sigurnost

Prvo pogledajmo kako graditi sigurne agentske aplikacije. Sigurnost znači da AI agent djeluje kako je zamišljeno. Kao kreatori agentskih aplikacija imamo metode i alate za maksimiziranje sigurnosti:

### Izgradnja okvira sustavne poruke

Ako ste ikada izrađivali AI aplikaciju koristeći velike jezične modele (LLM), znate koliko je važno dizajnirati robustan sustavni prompt ili sustavnu poruku. Ti prompti postavljaju meta pravila, upute i smjernice za način na koji će LLM komunicirati s korisnikom i podacima.

Za AI agente, sustavni prompt je još važniji jer će AI agenti trebati vrlo specifične upute za dovršetak zadataka koje smo im dizajnirali.

Za stvaranje skalabilnih sustavnih promptova možemo koristiti okvir sustavnih poruka za izgradnju jednog ili više agenata u našoj aplikaciji:

![Izgradnja okvira sustavne poruke](../../../translated_images/hr/system-message-framework.3a97368c92d11d68.webp)

#### Korak 1: Izradite meta sustavnu poruku 

Meta prompt će koristiti LLM za generiranje sustavnih poruka za agente koje kreiramo. Dizajniramo ga kao predložak tako da možemo efikasno kreirati više agenata po potrebi.

Evo primjera meta sustavne poruke koju bismo dali LLM-u:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Korak 2: Izradite osnovni prompt

Sljedeći korak je izraditi osnovni prompt koji opisuje AI agenta. Trebali biste uključiti ulogu agenta, zadatke koje agent treba izvršiti i ostale odgovornosti agenta.

Evo primjera:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Korak 3: Dostavite osnovnu sustavnu poruku LLM-u

Sada možemo optimizirati ovu sustavnu poruku dajući meta sustavnu poruku kao osnovu i našu osnovnu sustavnu poruku.

To će proizvesti sustavnu poruku bolje osmišljenu za vođenje naših AI agenata:

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

#### Korak 4: Iterirajte i poboljšajte

Vrijednost ovog okvira sustavnih poruka je u mogućnosti skalabilnog stvaranja poruka za više agenata te poboljšanje vaših sustavnih poruka tijekom vremena. Rijetko kad će vaša sustavna poruka raditi savršeno prvi put za vaš kompletan slučaj upotrebe. Mogućnost izvršavanja malih prilagodbi i poboljšanja mijenjanjem osnovne sustavne poruke i pokretanjem kroz sustav omogućuje usporedbu i evaluaciju rezultata.

## Razumijevanje prijetnji

Da biste izgradili pouzdane AI agente, važno je razumjeti i ublažiti rizike i prijetnje vašem AI agentu. Pogledajmo samo neke različite prijetnje AI agentima i kako se bolje planirati i pripremiti za njih.

![Razumijevanje prijetnji](../../../translated_images/hr/understanding-threats.89edeada8a97fc0f.webp)

### Zadatak i upute

**Opis:** Napadači pokušavaju promijeniti upute ili ciljeve AI agenta putem promptova ili manipuliranja ulazima.

**Ublažavanje**: Izvedite provjere valjanosti i filtre ulaza kako biste otkrili potencijalno opasne promptove prije nego što ih AI agent procesuira. Budući da ovi napadi obično zahtijevaju čestu interakciju s agentom, ograničavanje broja okretaja u razgovoru još je jedan način za sprječavanje ovakvih napada.

### Pristup kritičnim sustavima

**Opis**: Ako AI agent ima pristup sustavima i servisima koji pohranjuju osjetljive podatke, napadači mogu kompromitirati komunikaciju između agenta i tih servisa. To mogu biti direktni napadi ili indirektni pokušaji dobivanja informacija o tim sustavima putem agenta.

**Ublažavanje**: AI agenati trebaju imati pristup sustavima samo prema potrebi kako bi se spriječili ovakvi napadi. Komunikacija između agenta i sustava također treba biti sigurna. Implementacija autentifikacije i kontrole pristupa dodatno štiti ove informacije.

### Preopterećenje resursa i servisa

**Opis:** AI agenti mogu pristupiti različitim alatima i servisima za izvršenje zadataka. Napadači mogu iskoristiti ovu mogućnost da napadnu te servise slanjem velikog broja zahtjeva preko AI agenta, što može rezultirati kvarovima sustava ili visokim troškovima.

**Ublažavanje:** Implementirajte politike koje ograničavaju broj zahtjeva koje AI agent može poslati servisu. Ograničavanje broja okretaja razgovora i zahtjeva prema vašem AI agentu dodatno sprječava takve napade.

### Trovanje baze znanja

**Opis:** Ova vrsta napada ne cilja izravno AI agenta, već bazu znanja i druge servise koje AI agent koristi. To može uključivati korupciju podataka ili informacija koje AI agent koristi za izvršenje zadataka, što vodi do pristranih ili neželjenih odgovora korisniku.

**Ublažavanje:** Redovito provjeravajte podatke koje AI agent koristi u svojim radnim tokovima. Osigurajte da pristup tim podacima bude siguran i da ih mijenjaju samo pouzdane osobe kako biste izbjegli takav napad.

### Kaskadni pogreške

**Opis:** AI agenti koriste različite alate i servise za izvršavanje zadataka. Pogreške uzrokovane napadačima mogu dovesti do kvarova drugih sustava s kojima je AI agent povezan, što proširuje napad i otežava otklanjanje problema.

**Ublažavanje**: Jedan način da se to izbjegne jest da AI agent djeluje u ograničenom okruženju, poput izvršavanja zadataka unutar Docker kontejnera, kako bi se spriječili izravni napadi na sustav. Kreiranje rezervnih mehanizama i logike ponovnog pokušaja kada sustavi odgovore pogreškom dodatno sprječava veće kvarove.

## Čovjek u petlji

Još jedan učinkovit način za izgradnju pouzdanih sustava AI agenata je korištenje koncepta čovjeka u petlji. To stvara tok u kojem korisnici mogu davati povratne informacije agentima tijekom izvođenja. Korisnici u biti djeluju kao agenti u sustavu s više agenata pružajući odobrenje ili zaustavljanje procesa.

![Čovjek u petlji](../../../translated_images/hr/human-in-the-loop.5f0068a678f62f4f.webp)

Evo isječak koda korištenjem Microsoft Agent Frameworka koji pokazuje kako se ovaj koncept implementira:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Kreirajte pružatelja usluge s odobrenjem čovjeka u petlji
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
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

Izgradnja pouzdanih AI agenata zahtijeva pažljivo planiranje, robusne sigurnosne mjere i kontinuirano poboljšavanje. Implementacijom strukturiranih meta prompt sistema, razumijevanjem potencijalnih prijetnji i primjenom strategija ublažavanja, razvijatelji mogu stvoriti AI agente koji su sigurni i učinkoviti. Nadalje, uključivanje čovjeka u petlju osigurava da AI agenti ostanu usklađeni s potrebama korisnika uz minimiziranje rizika. Kako AI nastavlja evoluirati, održavanje proaktivnog pristupa sigurnosti, privatnosti i etičkim pitanjima bit će ključno za izgradnju povjerenja i pouzdanosti u AI-pokretanih sustavima.

## Primjeri koda

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Demonstracija sustava meta prompta - okvira sustavne poruke, korak po korak.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Provjere odobrenja prije akcije, kategorizacija rizika i zapisivanje revizije za pouzdane agente.

### Imate više pitanja o izgradnji pouzdanih AI agenata?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) da biste se upoznali s drugim polaznicima, sudjelovali u radnim satima i dobili odgovore na pitanja o AI agentima.

## Dodatni resursi

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Pregled odgovornog korištenja AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluacija generativnih AI modela i AI aplikacija</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Sigurnosne sustavne poruke</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Predložak procjene rizika</a>

## Prethodna lekcija

[Agentic RAG](../05-agentic-rag/README.md)

## Sljedeća lekcija

[Dizajn obrazaca planiranja](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->