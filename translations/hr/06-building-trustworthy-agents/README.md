[![Pouzdani AI agenti](../../../translated_images/hr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknite sliku iznad za prikaz videa ove lekcije)_

# Izrada pouzdanih AI agenata

## Uvod

Ova lekcija će pokriti:

- Kako izgraditi i implementirati sigurne i učinkovite AI agente
- Važne sigurnosne aspekte kod razvoja AI agenata.
- Kako održavati privatnost podataka i korisnika prilikom razvoja AI agenata.

## Ciljevi učenja

Nakon dovršetka ove lekcije, znat ćete kako:

- Prepoznati i ublažiti rizike pri stvaranju AI agenata.
- Provesti sigurnosne mjere kako bi se osiguralo pravilno upravljanje podacima i pristupom.
- Kreirati AI agente koji održavaju privatnost podataka i pružaju kvalitetno korisničko iskustvo.

## Sigurnost

Prvo pogledajmo kako izgraditi sigurne agentne aplikacije. Sigurnost znači da AI agent radi onako kako je dizajniran. Kao kreatori agentnih aplikacija, imamo metode i alate za maksimiziranje sigurnosti:

### Izrada okvira za sistemske poruke

Ako ste ikad izrađivali AI aplikaciju koristeći velike jezične modele (LLM), znate koliko je važno dizajnirati robusni sistemski prompt ili sistemsku poruku. Ti promptovi uspostavljaju meta pravila, upute i smjernice kako će LLM komunicirati s korisnikom i podacima.

Za AI agente, sistemski prompt je još važniji jer će AI agenti trebati vrlo specifične upute da završe zadatke koje smo im dizajnirali.

Za stvaranje skalabilnih sistemskih promptova, možemo koristiti okvir za sistemske poruke za izgradnju jednog ili više agenata u našoj aplikaciji:

![Izrada okvira za sistemske poruke](../../../translated_images/hr/system-message-framework.3a97368c92d11d68.webp)

#### Korak 1: Izradite meta sistemsku poruku

Meta prompt će koristiti LLM za generiranje sistemskih promptova za agente koje stvaramo. Dizajniramo ga kao predložak kako bismo mogli učinkovito kreirati više agenata po potrebi.

Evo primjera meta sistemske poruke koju bismo dali LLM-u:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Korak 2: Izradite osnovni prompt

Sljedeći korak je kreirati osnovni prompt za opis AI agenta. Trebali biste uključiti ulogu agenta, zadatke koje agent obavlja i druge odgovornosti agenta.

Evo primjera:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Korak 3: Dostavite osnovnu sistemsku poruku LLM-u

Sada možemo optimizirati ovu sistemsku poruku tako da damo meta sistemsku poruku kao sistemsku poruku i našu osnovnu sistemsku poruku.

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

#### Korak 4: Iterirajte i poboljšavajte

Vrijednost ovog okvira za sistemske poruke je u tome što možemo lakše skalirati kreiranje sistemskih poruka za više agenata, kao i poboljšavati sistemske poruke tijekom vremena. Rijetko ćete imati sistemsku poruku koja savršeno radi prvi put za vaš kompletan slučaj upotrebe. Mogućnost malih izmjena i poboljšanja mijenjanjem osnovne sistemske poruke i njenim ponovnim pokretanjem kroz sistem omogućit će vam usporedbu i evaluaciju rezultata.

## Razumijevanje prijetnji

Da bismo izgradili pouzdane AI agente, važno je razumjeti i ublažiti rizike i prijetnje prema vašem AI agentu. Pogledajmo samo neke od različitih prijetnji AI agentima i kako se na njih bolje pripremiti i planirati.

![Razumijevanje prijetnji](../../../translated_images/hr/understanding-threats.89edeada8a97fc0f.webp)

### Zadatak i uputa

**Opis:** Napadači pokušavaju promijeniti upute ili ciljeve AI agenta kroz promptanje ili manipulaciju unosima.

**Ublažavanje:** Provedite provjere validacije i filtre unosa kako biste otkrili potencijalno opasne promptove prije nego ih AI agent obradi. Budući da ti napadi obično zahtijevaju čestu interakciju s agentom, ograničavanje broja okreta u razgovoru je još jedan način sprječavanja ovakvih napada.

### Pristup kritičnim sustavima

**Opis:** Ako AI agent ima pristup sustavima i uslugama koje pohranjuju osjetljive podatke, napadači mogu kompromitirati komunikaciju između agenta i tih usluga. To mogu biti direktni napadi ili indirektne pokušaje da se preko agenta dođe do informacija o tim sustavima.

**Ublažavanje:** AI agenti trebaju imati pristup sustavima samo prema potrebi kako bi se spriječili takvi napadi. Komunikacija između agenta i sustava također treba biti sigurna. Implementacija autentifikacije i kontrole pristupa je još jedan način za zaštitu ovih informacija.

### Preopterećenje resursa i usluga

**Opis:** AI agenti mogu pristupati različitim alatima i uslugama za izvršenje zadataka. Napadači mogu iskoristiti tu mogućnost da napadnu te usluge slanjem velikog broja zahtjeva preko AI agenta, što može uzrokovati pad sustava ili visoke troškove.

**Ublažavanje:** Provedite politike za ograničavanje broja zahtjeva koje AI agent može poslati nekoj usluzi. Ograničavanje broja okreta razgovora i zahtjeva prema vašem AI agentu je još jedan način zaštite od ovakvih napada.

### Trovanje baze znanja

**Opis:** Ova vrsta napada nije usmjerena direktno na AI agenta, već na bazu znanja i druge usluge koje AI agent koristi. To može uključivati korumpiranje podataka ili informacija koje AI agent koristi za izvršenje zadatka, što može dovesti do pristranih ili neželjenih odgovora korisniku.

**Ublažavanje:** Redovito provjeravajte podatke koje AI agent koristi u svojim radnim procesima. Osigurajte da je pristup tim podacima siguran i mijenjaju ih samo pouzdane osobe kako biste izbjegli ovu vrstu napada.

### Kaskadni pogreške

**Opis:** AI agenti pristupaju raznim alatima i uslugama radi izvršenja zadataka. Pogreške koje izazivaju napadači mogu dovesti do kvara drugih sustava na koje je AI agent povezan, uzrokujući da napad postane rašireniji i teže za otkloniti.

**Ublažavanje:** Jedna metoda za izbjegavanje toga je rad AI agenta u ograničenom okruženju, poput izvršavanja zadataka u Docker kontejneru, kako bi se spriječili direktni napadi na sistem. Izrada mehanizama za rezervni rad i logike ponovnog pokušaja kad neki sustav odgovori s greškom također pomaže u sprječavanju većih kvarova sustava.

## Čovjek u petlji

Još jedan učinkovit način za izgradnju pouzdanih sustava AI agenata je korištenje čovjeka u petlji (Human-in-the-loop). To stvara tijek u kojem korisnici mogu davati povratne informacije agentima tijekom rada. Korisnici u biti djeluju kao agenti u multi-agentnom sustavu pružajući odobrenje ili prekid procesa.

![Čovjek u petlji](../../../translated_images/hr/human-in-the-loop.5f0068a678f62f4f.webp)

Evo primjera koda koji koristi Microsoft Agent Framework da pokaže kako se ovaj koncept implementira:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Kreirajte davatelja s odobrenjem čovjeka u petlji
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Kreirajte agenta s korakom ljudskog odobrenja
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

Izrada pouzdanih AI agenata zahtijeva pažljiv dizajn, robusne sigurnosne mjere i kontinuiranu iteraciju. Implementacijom strukturiranih meta prompt sustava, razumijevanjem potencijalnih prijetnji i primjenom strategija ublažavanja, programeri mogu stvoriti AI agente koji su istovremeno sigurni i učinkoviti. Također, uključivanje čovjeka u petlji osigurava da AI agenti ostanu usklađeni s potrebama korisnika uz minimaliziranje rizika. Kako se AI nastavlja razvijati, održavanje proaktivnog pristupa sigurnosti, privatnosti i etičkim razmatranjima bit će ključno za izgradnju povjerenja i pouzdanosti u sustavima vođenim AI-em.

## Primjeri koda

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Demonstracija korak-po-korak meta-prompt okvira za sistemske poruke.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Blokade odobrenja prije akcije, razvrstavanje rizičnih razina i zapisivanje za reviziju za pouzdane agente.

### Imate li dodatnih pitanja o izradi pouzdanih AI agenata?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) da upoznate druge učenike, sudjelujete u radnim satima i dobijete odgovore na vaša pitanja o AI agentima.

## Dodatni resursi

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Pregled odgovornog korištenja AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluacija generativnih AI modela i AI aplikacija</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Sigurnosne sistemske poruke</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Predložak procjene rizika</a>

## Prethodna lekcija

[Agentic RAG](../05-agentic-rag/README.md)

## Sljedeća lekcija

[Obrazac planiranja dizajna](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->