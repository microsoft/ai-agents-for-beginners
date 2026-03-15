[![Pouzdani AI agenti](../../../translated_images/hr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknite sliku iznad da pogledate video ove lekcije)_

# Izgradnja pouzdanih AI agenata

## Uvod

Ova lekcija obuhvaća:

- Kako izgraditi i implementirati sigurne i učinkovite AI agente
- Važne sigurnosne aspekte pri razvoju AI agenata.
- Kako održavati privatnost podataka i korisnika pri razvoju AI agenata.

## Ciljevi učenja

Nakon završetka ove lekcije, znat ćete kako:

- Prepoznati i ublažiti rizike pri stvaranju AI agenata.
- Provoditi sigurnosne mjere kako bi se osiguralo pravilno upravljanje podacima i pristupom.
- Stvoriti AI agente koji održavaju privatnost podataka i pružaju kvalitetno korisničko iskustvo.

## Sigurnost

Prvo pogledajmo kako graditi sigurne aplikacije temeljene na agentima. Sigurnost znači da AI agent radi kako je zamišljeno. Kao tvorci aplikacija s agentima, imamo metode i alate za maksimalno povećanje sigurnosti:

### Izgradnja okvira za sistemske poruke

Ako ste ikada izgradili AI aplikaciju koristeći Large Language Models (LLMs), znate koliko je važno dizajnirati robusni sistemski prompt ili sistemsku poruku. Ti promptovi uspostavljaju metapravila, upute i smjernice za način na koji će LLM komunicirati s korisnikom i podacima.

Za AI agente, sistemski prompt je još važniji jer će AI agenti trebati vrlo specifične upute kako bi dovršili zadatke koje smo im zadali.

Za stvaranje skalabilnih sistemskih promptova, možemo koristiti okvir za sistemske poruke pri izgradnji jednog ili više agenata u našoj aplikaciji:

![Izgradnja okvira za sistemske poruke](../../../translated_images/hr/system-message-framework.3a97368c92d11d68.webp)

#### Korak 1: Stvorite meta sistemsku poruku 

Meta prompt će koristiti LLM za generiranje sistemskih promptova za agente koje stvorimo. Dizajniramo ga kao predložak kako bismo mogli učinkovito stvoriti više agenata ako je potrebno.

Evo primjera meta sistemske poruke koju bismo dali LLM-u:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Korak 2: Stvorite osnovni prompt

Sljedeći korak je izraditi osnovni prompt koji opisuje AI agenta. Trebali biste uključiti ulogu agenta, zadatke koje će agent izvršavati i sve druge odgovornosti agenta.

Evo primjera:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Korak 3: Dostavite osnovnu sistemsku poruku LLM-u

Sada možemo optimizirati ovu sistemsku poruku pružajući meta sistemsku poruku kao sistemsku poruku zajedno s našom osnovnom sistemskom porukom.

To će proizvesti sistemsku poruku bolje dizajniranu za usmjeravanje naših AI agenata:

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

Vrijednost ovog okvira za sistemske poruke je u mogućnosti lakšeg skaliranja stvaranja sistemskih poruka za više agenata, kao i u poboljšavanju vaših sistemskih poruka tijekom vremena. Rijetko se događa da imate sistemsku poruku koja radi iz prve za vaš cjelokupni slučaj upotrebe. Mogućnost izvođenja malih prilagodbi i poboljšanja promjenom osnovne sistemske poruke i pokretanjem kroz sustav omogućit će vam usporedbu i procjenu rezultata.

## Razumijevanje prijetnji

Za izgradnju pouzdanih AI agenata važno je razumjeti i ublažiti rizike i prijetnje prema vašem AI agentu. Pogledajmo neke od različitih prijetnji AI agentima i kako se na njih bolje planirati i pripremiti.

![Razumijevanje prijetnji](../../../translated_images/hr/understanding-threats.89edeada8a97fc0f.webp)

### Zadaci i upute

**Opis:** Napadači pokušavaju promijeniti upute ili ciljeve AI agenta putem promptanja ili manipulacije ulazima.

**Ublažavanje**: Izvršite provjere valjanosti i filtre ulaza kako biste otkrili potencijalno opasne promtove prije nego što ih AI agent obradi. Budući da ti napadi obično zahtijevaju čestu interakciju s agentom, ograničavanje broja okretaja u razgovoru još je jedan način sprječavanja ovakvih napada.

### Pristup kritičnim sustavima

**Opis**: Ako AI agent ima pristup sustavima i servisima koji pohranjuju osjetljive podatke, napadači mogu kompromitirati komunikaciju između agenta i tih servisa. To mogu biti izravni napadi ili neizravni pokušaji dobivanja informacija o tim sustavima preko agenta.

**Ublažavanje**: AI agenti trebaju imati pristup sustavima samo po principu nužnosti kako bi se spriječile ovakve vrste napada. Komunikacija između agenta i sustava također treba biti sigurna. Implementacija autentikacije i kontrole pristupa još je jedan način zaštite ovih podataka.

### Preopterećenje resursa i servisa

**Opis:** AI agenti mogu pristupati različitim alatima i servisima kako bi dovršili zadatke. Napadači mogu iskoristiti ovu sposobnost za napad na te servise slanjem velike količine zahtjeva preko AI agenta, što može rezultirati kvarovima sustava ili visokim troškovima.

**Ublažavanje:** Provedite politike za ograničavanje broja zahtjeva koje AI agent može poslati servisu. Ograničavanje broja okretaja u razgovoru i zahtjeva vašem AI agentu još je jedan način sprječavanja ovakvih napada.

### Trovanje baze znanja

**Opis:** Ova vrsta napada ne cilja izravno AI agenta nego bazu znanja i druge servise koje će AI agent koristiti. To može uključivati korumpiranje podataka ili informacija koje će AI agent koristiti za izvršavanje zadatka, što dovodi do pristranih ili nenamjernih odgovora korisniku.

**Ublažavanje:** Redovito provjeravajte podatke koje će AI agent koristiti u svojim radnim tokovima. Osigurajte da je pristup tim podacima siguran i da ih mijenjaju samo pouzdane osobe kako biste izbjegli ovu vrstu napada.

### Kaskadne pogreške

**Opis:** AI agenti pristupaju raznim alatima i servisima kako bi dovršili zadatke. Pogreške uzrokovane od strane napadača mogu dovesti do otkaza drugih sustava s kojima je AI agent povezan, uzrokujući da napad postane razorniji i teže za otkloniti.

**Ublažavanje**: Jedan način da se to izbjegne je da AI agent radi u ograničenom okruženju, poput izvršavanja zadataka u Docker kontejneru, kako bi se spriječili izravni napadi na sustav. Izrada rezervnih mehanizama i logike ponovnog pokušaja kada se neki sustavi jave s pogreškom još je jedan način sprječavanja većih kvarova sustava.

## Čovjek u petlji

Još jedan učinkovit način izgradnje pouzdanih sustava AI agenata je upotreba čovjeka u petlji. To stvara tok u kojem korisnici mogu pružiti povratne informacije agentima tijekom rada. Korisnici u suštini djeluju kao agenti u sustavu s više agenata i daju odobrenje ili prekidaju proces koji se izvodi.

![Čovjek u petlji](../../../translated_images/hr/human-in-the-loop.5f0068a678f62f4f.webp)

Ovdje je isječak koda koji koristi Microsoft Agent Framework kako bi prikazao kako je ovaj koncept implementiran:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Kreiraj providera s ljudskim odobravanjem
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Kreiraj agenta s korakom ljudskog odobrenja
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

Izgradnja pouzdanih AI agenata zahtijeva pažljiv dizajn, robusne sigurnosne mjere i kontinuirano iteriranje. Implementacijom strukturiranih meta-prompting sustava, razumijevanjem potencijalnih prijetnji i primjenom strategija ublažavanja, programeri mogu stvoriti AI agente koji su i sigurni i učinkoviti. Dodatno, uključivanje pristupa čovjeka u petlji osigurava da AI agenti ostanu usklađeni s potrebama korisnika uz minimiziranje rizika. Kako se AI nastavlja razvijati, održavanje proaktivnog pristupa sigurnosti, privatnosti i etičkim razmatranjima bit će ključno za poticanje povjerenja i pouzdanosti u sustavima pokretanim AI-jem.

### Imate li dodatna pitanja o izgradnji pouzdanih AI agenata?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) kako biste se susreli s drugim polaznicima, prisustvovali radnim satima i dobili odgovore na pitanja o vašim AI agentima.

## Dodatni resursi

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Pregled odgovornog korištenja AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Procjena generativnih AI modela i AI aplikacija</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Sigurnosne sistemske poruke</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Predložak procjene rizika</a>

## Prethodna lekcija

[Agentic RAG](../05-agentic-rag/README.md)

## Sljedeća lekcija

[Uzorak dizajna planiranja](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Odricanje odgovornosti:
Ovaj dokument preveden je pomoću AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->