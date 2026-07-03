[![Kako oblikovati dobre AI agente](../../../translated_images/sl/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Kliknite zgornjo sliko za ogled videa te lekcije)_
# Principi AI agentnega oblikovanja

## Uvod

Obstaja veliko načinov razmišljanja o gradnji AI agentnih sistemov. Glede na to, da je nesigurnost značilnost in ne napaka v zasnovi generativne AI, je inženirjem včasih težko ugotoviti, kje sploh začeti. Ustvarili smo nabor uporabniško usmerjenih principov UX oblikovanja, da razvijalcem omogočimo gradnjo strankam osredotočenih agentnih sistemov za reševanje njihovih poslovnih potreb. Ti principi oblikovanja niso predpisana arhitektura, ampak izhodišče za ekipe, ki opredeljujejo in razvijajo agentne izkušnje.

Na splošno bi agenti morali:

- Razširjati in povečevati človeške sposobnosti (zamisliti ideje, reševanje problemov, avtomatizacija itd.)
- Zapolnjevati vrzeli v znanju (hitro me seznaniti z določenimi področji znanja, prevajanje itd.)
- Omogočiti in podpirati sodelovanje na načine, ki jih kot posamezniki raje uporabljamo pri sodelovanju z drugimi
- Narediti nas boljše različice samih sebe (npr. življenjski trener/obvladovalec nalog, pomoč pri učenju čustvene regulacije in pozornosti, grajenje odpornosti itd.)

## Ta lekcija bo pokrivala

- Kaj so agentni principi oblikovanja
- Nekaj smernic, ki jih je treba upoštevati pri izvajanju teh principov oblikovanja
- Nekaj primerov uporabe principov oblikovanja

## Cilji učenja

Po končani lekciji boste lahko:

1. Pojasnili, kaj so agentni principi oblikovanja
2. Pojasnili smernice za uporabo agentnih principov oblikovanja
3. Razumeli, kako zgraditi agenta z uporabo agentnih principov oblikovanja

## Agentni principi oblikovanja

![Agentni principi oblikovanja](../../../translated_images/sl/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (prostor)

To je okolje, v katerem agent deluje. Ti principi informirajo, kako oblikujemo agente za delovanje v fizičnih in digitalnih svetovih.

- **Povezovanje, ne zruševanje** – pomagati povezati ljudi z drugimi ljudmi, dogodki in uporabnim znanjem, da omogočimo sodelovanje in povezovanje.
- Agenti pomagajo povezovati dogodke, znanje in ljudi.
- Agenti ljudi približajo skupaj. Niso zasnovani, da bi nadomestili ali manjvrednotili ljudi.
- **Enostavno dostopni, a občasno nevidni** – agent pretežno deluje v ozadju in nas opomni le, ko je to relevantno in primerno.
  - Agent je enostavno odkritljiv in dostopen pooblaščenim uporabnikom na kateri koli napravi ali platformi.
  - Agent podpira večmodalne vnose in izhode (zvok, glas, besedilo itd.).
  - Agent lahko brez težav prehaja med sprednjim in ozadnim načinom; med proaktivnim in reaktivnim, glede na zaznavanje uporabniških potreb.
  - Agent lahko deluje v nevidni obliki, a je njegova ozadna procesna pot in sodelovanje z drugimi agenti uporabniku pregledno in obvladljivo.

### Agent (čas)

Tako agent deluje skozi čas. Ti principi informirajo, kako oblikujemo agente, ki delujejo skozi preteklost, sedanjost in prihodnost.

- **Preteklost**: Razmišljanje o zgodovini, ki vključuje tako stanje kot kontekst.
  - Agent zagotavlja bolj relevantne rezultate na podlagi analize bogatejših zgodovinskih podatkov, ki presegajo le dogodek, ljudi ali stanja.
  - Agent ustvarja povezave iz preteklih dogodkov in aktivno reflektira spomin za ukvarjanje s trenutnimi situacijami.
- **Zdaj**: Spodbujanje bolj kot obveščanje.
  - Agent predstavlja celosten pristop k interakciji z ljudmi. Ko se dogodek zgodi, agent presega statično obvestilo ali drugo statično formalnost. Agent lahko poenostavi procese ali dinamično ustvarja namige za usmerjanje pozornosti uporabnika ob pravem trenutku.
  - Agent posreduje informacije glede na kontekst okolja, družbene in kulturne spremembe ter prilagojeno uporabniškemu namenu.
  - Interakcija z agentom je lahko postopna, razvijajoča se/rastoča v kompleksnosti, da dolgoročno opolnomoči uporabnike.
- **Prihodnost**: Prilagajanje in razvoj.
  - Agent se prilagaja različnim napravam, platformam in modalitetam.
  - Agent se prilagaja uporabniškemu vedenju, potrebam dostopnosti in je poljubno prilagodljiv.
  - Agent oblikuje in razvija skozi neprekinjeno interakcijo z uporabnikom.

### Agent (jedro)

To so ključni elementi v jedru oblikovanja agenta.

- **Sprejmi negotovost, a vzpostavi zaupanje**.
  - Pričakuje se določena stopnja negotovosti agenta. Negotovost je ključen element agentnega oblikovanja.
  - Zaupanje in preglednost sta temeljni plasti agentnega oblikovanja.
  - Ljudje nadzorujejo, kdaj je agent vklopljen/izklopljen in status agenta je ves čas jasno viden.

## Smernice za izvajanje teh principov

Ko uporabljate prejšnje principe oblikovanja, uporabite naslednje smernice:

1. **Preglednost**: Obvestite uporabnika, da je vključen AI, kako deluje (vključno s preteklimi dejanji) in kako dati povratne informacije ter spremeniti sistem.
2. **Nadzor**: Omogočite uporabniku, da prilagodi, določi preference in personalizira ter ima nadzor nad sistemom in njegovimi značilnostmi (vključno z možnostjo pozabe).
3. **Doslednost**: Ciljajte na dosledne, večmodalne izkušnje na napravah in končnih točkah. Uporabite znane UI/UX elemente, kjer je mogoče (npr. ikona mikrofona za glasovno interakcijo) in zmanjšajte kognitivno obremenitev kupca čim bolj (npr. ciljajte na jedrnate odgovore, vizualna pomagala in vsebino "Več o tem").

## Kako oblikovati potovalnega agenta z uporabo teh principov in smernic

Predstavljajte si, da oblikujete potovalnega agenta, tukaj je, kako bi lahko razmišljali o uporabi principov oblikovanja in smernic:

1. **Preglednost** – Dajte uporabniku vedeti, da je potovalni agent AI-omogočen agent. Zagotovite nekaj osnovnih navodil, kako začeti (npr. pozdravno sporočilo, vzorčni pozivi). To jasno dokumentirajte na strani izdelka. Prikažite seznam pozivov, ki jih je uporabnik v preteklosti uporabil. Jasno razložite, kako dati povratne informacije (palec gor/dol, gumb Pošlji povratne informacije itd.). Jasno navedite, če ima agent omejitve glede uporabe ali tem.
2. **Nadzor** – Poskrbite, da je jasno, kako lahko uporabnik spremeni agenta po njegovi ustvaritvi z orodji, kot je sistemski poziv. Omogočite uporabniku, da izbere, kako obširen je agent, njegov slog pisanja, in morebitne opozorilne okoliščine o tem, o čem agent naj ne bi govoril. Dovolite uporabniku, da si ogleda in izbriše povezane datoteke ali podatke, pozive in pretekle pogovore.
3. **Doslednost** – Poskrbite, da so ikone za deljenje poziva, dodajanje datoteke ali fotografije ter označevanje nekoga ali nečesa standardne in prepoznavne. Uporabite ikono sponke za nalaganje/deljenje datotek z agentom in ikono slike za nalaganje grafike.

## Primeri kode

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Imate več vprašanj o vzorcih AI agentnega oblikovanja?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kjer se lahko srečate z drugimi učenci, udeležite ur svetovanja in dobite odgovore na vaša vprašanja o AI agentih.

## Dodatni viri

- <a href="https://openai.com" target="_blank">Prakse za upravljanje agentnih AI sistemov | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Projekt HAX Toolkit - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Orodjarna za odgovorno AI</a>

## Prejšnja lekcija

[Raziskovanje agentnih okvirjev](../02-explore-agentic-frameworks/README.md)

## Naslednja lekcija

[Vzorec uporabe orodja](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->