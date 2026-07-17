[![Kako oblikovati dobre AI agente](../../../translated_images/sl/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Kliknite na zgornjo sliko za ogled videa te lekcije)_
# Načela oblikovanja AI agentov

## Uvod

Obstaja veliko načinov razmišljanja o ustvarjanju AI agentskih sistemov. Glede na to, da je dvoumnost v zasnovi Generativne AI funkcija in ne napaka, je včasih inženirjem težko ugotoviti, kje sploh začeti. Ustvarili smo niz humanocentričnih načel za oblikovanje uporabniške izkušnje, da omogočimo razvijalcem gradnjo strankam prijaznih agentskih sistemov za reševanje njihovih poslovnih potreb. Ta načela oblikovanja niso predpisana arhitektura, temveč izhodišče za ekipe, ki opredeljujejo in razvijajo agentske izkušnje.

Na splošno naj bi agenti:

- Razširili in povečali človeške zmogljivosti (možganska nevihta, reševanje težav, avtomatizacija itd.)
- Zapolnili vrzeli v znanju (prikazali mi najnovejše informacije o področjih znanja, prevajanje itd.)
- Olajšali in podpirali sodelovanje na načine, kot posamezniki radi delamo z drugimi
- Naredili nas boljše različice samih sebe (npr. življenjski trener/naloga mojster, pomagati nam pri učenju čustvenega uravnavanja in veščin čuječnosti, gradnja odpornosti itd.)

## Ta lekcija bo obravnavala

- Kaj so načela agentskega oblikovanja
- Kakšna so nekatera pravila, ki jih je treba upoštevati pri izvajanju teh načel oblikovanja
- Nekaj primerov uporabe teh načel

## Cilji učenja

Po zaključku te lekcije boste lahko:

1. Razložili, kaj so načela agentskega oblikovanja
2. Razložili pravila za uporabo načel agentskega oblikovanja
3. Razumeli, kako zgraditi agenta z uporabo načel agentskega oblikovanja

## Načela agentskega oblikovanja

![Načela agentskega oblikovanja](../../../translated_images/sl/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (Prostor)

To je okolje, v katerem agent deluje. Ta načela nam pomagajo pri oblikovanju agentov za sodelovanje v fizičnih in digitalnih svetovih.

- **Povezovanje, ne zlivanje** – pomagajte povezati ljudi z drugimi ljudmi, dogodki in uporabnim znanjem za omogočanje sodelovanja in povezovanja.
- Agenti pomagajo povezati dogodke, znanje in ljudi.
- Agenti prinašajo ljudi bližje skupaj. Niso zasnovani za zamenjavo ali manjvrednost ljudi.
- **Enostavno dostopen, vendar občasno neviden** – agent večinoma deluje v ozadju in nas zbudi le, kadar je to relevantno in primerno.
  - Agent je enostavno najti in dostopen pooblaščenim uporabnikom na kateri koli napravi ali platformi.
  - Agent podpira multimodalne vhode in izhode (zvok, glas, besedilo itd.).
  - Agent lahko brez težav prehaja med sprednjim in ozadnim delom; med proaktivnim in reaktivnim, odvisno od zaznavanja potreb uporabnika.
  - Agent lahko deluje v nevidni obliki, vendar je njegova pot ozadnega procesa ter sodelovanje z drugimi Agenti pregledno in nadzorovano s strani uporabnika.

### Agent (Čas)

Tako agent deluje skozi čas. Ta načela nam pomagajo oblikovati agente, ki sodelujejo preko preteklosti, sedanjosti in prihodnosti.

- **Preteklost**: Razmišljanje o zgodovini, ki vključuje tako stanje kot kontekst.
  - Agent nudi bolj relevantne rezultate na podlagi analize bogatejših zgodovinskih podatkov, ne zgolj dogodka, ljudi ali stanj.
  - Agent ustvarja povezave iz preteklih dogodkov in aktivno razmišlja o spominu za boljše vključevanje v trenutne situacije.
- **Zdaj**: Spodbujanje bolj kot obveščanje.
  - Agent utelesi celovit pristop k interakciji z ljudmi. Ko se dogodek zgodi, agent presega statično obveščanje ali druge statične formalnosti. Agent lahko poenostavi procese ali dinamično ustvari opozorila za usmerjanje pozornosti uporabnika ob pravem trenutku.
  - Agent posreduje informacije na podlagi kontekstualnega okolja, družbenih in kulturnih sprememb ter glede na namen uporabnika.
  - Interakcija z agentom se lahko postopoma razvija/raste v kompleksnosti, da dolgoročno opolnomoči uporabnike.
- **Prihodnost**: Prilagajanje in razvoj.
  - Agent se prilagaja različnim napravam, platformam in modalitetam.
  - Agent se prilagaja uporabnikovemu vedenju, potrebam dostopnosti in je prosto prilagodljiv.
  - Agent je oblikovan in se razvija skozi kontinuirano uporabniško interakcijo.

### Agent (Jedro)

To so ključni elementi v jedru zasnove agenta.

- **Sprejmimo negotovost, a vzpostavimo zaupanje**.
  - Pričakuje se določena stopnja negotovosti agenta. Negotovost je ključni element oblikovanja agenta.
  - Zaupanje in transparentnost sta temeljna sloja oblikovanja agenta.
  - Ljudje nadzorujejo, kdaj je agent vklopljen/izklopljen in status agenta je vedno jasno viden.

## Smernice za izvedbo teh načel

Ko uporabljate zgornja načela oblikovanja, upoštevajte naslednje smernice:

1. **Preglednost**: Obvestite uporabnika, da je vključen AI, kako deluje (vključno s preteklimi dejanji) ter kako dati povratne informacije in prilagoditi sistem.
2. **Nadzor**: Omogočite uporabniku prilagajanje, določitev prednosti in personalizacijo ter nadzor nad sistemom in njegovimi atributi (vključno z možnostjo pozabe).
3. **Doslednost**: Prizadevajte si za dosledne, multimodalne izkušnje na napravah in končnih točkah. Uporabljajte znane UI/UX elemente, kjer je mogoče (npr. ikona mikrofona za glasovno interakcijo) in čim bolj zmanjšajte kognitivno obremenitev stranke (npr. ciljni kratki odgovori, vizualna pomoč in vsebine »Izvedi več«).

## Kako oblikovati potovalnega agenta z uporabo teh načel in smernic

Predstavljajte si, da oblikujete potovalnega agenta, takole lahko razmišljate o uporabi načel oblikovanja in smernic:

1. **Preglednost** – Naj uporabnik ve, da je Potovalni agent omogočen z AI. Zagotovite osnovna navodila, kako začeti (npr. sporočilo »Pozdravljeni«, vzorčni pozivi). To jasno zabeležite na strani izdelka. Prikažite seznam pozivov, ki jih je uporabnik predhodno vprašal. Jasno povejte, kako dati povratne informacije (palec gor/dol, gumb Pošlji povratne informacije itd.). Jasno izrazite, če ima agent omejitve glede uporabe ali tem.
2. **Nadzor** – Poskrbite, da je jasno, kako lahko uporabnik spremeni agenta po njegovi ustvaritvi z nastavitvami, kot je Sistemski poziv. Omogočite uporabniku izbiro, kako obširen je agent, njegov slog pisanja in kakršne koli omejitve o tem, o čem agent ne sme govoriti. Dovolite uporabniku ogled in brisanje povezanih datotek, podatkov, pozivov in preteklih pogovorov.
3. **Doslednost** – Poskrbite, da so ikone za Deljenje poziva, dodajanje datoteke ali fotografije in označevanje nečesa ali nekoga standardne in prepoznavne. Uporabite ikono s papirnatim sponko za nakazovanje nalaganja/deljenja datotek z agentom in ikono slike za nakazovanje nalaganja grafike.

## Primeri kode

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Imate več vprašanj o vzorcih oblikovanja AI agentov?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da se srečate z drugimi učenci, sodelujete na urah svetovanja in dobite odgovore na vprašanja o AI agentih.

## Dodatni viri

- <a href="https://openai.com" target="_blank">Prakse za upravljanje agentskih AI sistemov | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Projekt HAX Toolkit - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Orodjarna za odgovorni AI</a>

## Prejšnja lekcija

[Raziščite agentske okvirje](../02-explore-agentic-frameworks/README.md)

## Naslednja lekcija

[Vzorci uporabe orodij](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->