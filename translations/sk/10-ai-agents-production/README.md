<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ad5de6a6388d02c145a92dd04358bab",
  "translation_date": "2025-07-12T13:41:49+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "sk"
}
-->
[![AI Agents In Production](../../../translated_images/lesson-10-thumbnail.2b79a30773db093e0b4fb47aaa618069e0afb4745fad4836526cf51df87f9ac9.sk.png)](https://youtu.be/l4TP6IyJxmQ?si=IvCW3cbw0NJ2mUMV)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_
# AI Agenti v produkcii

## Úvod

V tejto lekcii sa dozviete:

- Ako efektívne naplánovať nasadenie vášho AI Agenta do produkcie.
- Bežné chyby a problémy, s ktorými sa môžete stretnúť pri nasadzovaní AI Agenta do produkcie.
- Ako riadiť náklady a zároveň udržať výkon vášho AI Agenta.

## Ciele učenia

Po dokončení tejto lekcie budete vedieť/rozumieť:

- Techniky na zlepšenie výkonu, nákladov a efektívnosti produkčného systému AI Agenta.
- Čo a ako hodnotiť u vašich AI Agentov.
- Ako kontrolovať náklady pri nasadzovaní AI Agentov do produkcie.

Je dôležité nasadzovať AI Agentov, ktorým možno dôverovať. Pozrite si tiež lekciu „Building Trustworthy AI Agents“.

## Hodnotenie AI Agentov

Pred, počas a po nasadení AI Agentov je nevyhnutné mať správny systém na ich hodnotenie. To zabezpečí, že váš systém bude v súlade s vašimi a používateľskými cieľmi.

Na hodnotenie AI Agenta je dôležité vedieť vyhodnotiť nielen výstup agenta, ale aj celý systém, v ktorom AI Agent funguje. To zahŕňa, ale nie je obmedzené na:

- Počiatočnú požiadavku modelu.
- Schopnosť agenta identifikovať zámer používateľa.
- Schopnosť agenta vybrať správny nástroj na vykonanie úlohy.
- Odozvu nástroja na požiadavku agenta.
- Schopnosť agenta interpretovať odpoveď nástroja.
- Spätnú väzbu používateľa na odpoveď agenta.

Týmto spôsobom môžete identifikovať oblasti na zlepšenie modulárnejšie. Následne môžete efektívnejšie sledovať vplyv zmien v modeloch, promptoch, nástrojoch a ďalších komponentoch.

## Bežné problémy a možné riešenia s AI Agentmi

| **Problém**                                    | **Možné riešenie**                                                                                                                                                                                                        |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AI Agent nevykonáva úlohy konzistentne         | - Vylepšite prompt, ktorý dávate AI Agentovi; buďte jasní v cieľoch.<br>- Identifikujte, kde môže pomôcť rozdelenie úloh na podúlohy a ich spracovanie viacerými agentmi.                                                  |
| AI Agent sa dostáva do nekonečných slučiek     | - Zabezpečte jasné podmienky ukončenia, aby agent vedel, kedy proces zastaviť.<br>- Pri zložitých úlohách vyžadujúcich uvažovanie a plánovanie použite väčší model špecializovaný na tieto úlohy.                          |
| Volania nástrojov AI Agenta nefungujú dobre    | - Testujte a overujte výstupy nástrojov mimo systému agenta.<br>- Vylepšite definované parametre, prompty a pomenovanie nástrojov.                                                                                        |
| Multi-agentný systém nefunguje konzistentne    | - Vylepšite prompty pre každého agenta, aby boli špecifické a odlišné.<br>- Vytvorte hierarchický systém s „routing“ alebo kontrolným agentom, ktorý určí, ktorý agent je správny.                                        |

## Riadenie nákladov

Tu sú niektoré stratégie na riadenie nákladov pri nasadzovaní AI agentov do produkcie:

- **Ukladanie odpovedí do cache** – Identifikovanie bežných požiadaviek a úloh a poskytovanie odpovedí ešte pred ich spracovaním agentným systémom je dobrý spôsob, ako znížiť počet podobných požiadaviek. Môžete dokonca implementovať tok na určenie podobnosti požiadavky s uloženými odpoveďami pomocou jednoduchších AI modelov.

- **Používanie menších modelov** – Malé jazykové modely (SLM) môžu dobre fungovať pri určitých agentných prípadoch použitia a výrazne znížiť náklady. Ako už bolo spomenuté, najlepším spôsobom, ako pochopiť, ako dobre SLM funguje vo vašom prípade, je vybudovať hodnotiaci systém na porovnanie výkonu s väčšími modelmi.

- **Používanie router modelu** – Podobnou stratégiou je využitie rôznych modelov a veľkostí. Môžete použiť LLM/SLM alebo serverless funkciu na smerovanie požiadaviek podľa ich zložitosti na najvhodnejšie modely. To pomôže znížiť náklady a zároveň zabezpečiť výkon na správnych úlohách.

## Gratulujeme

Toto je momentálne posledná lekcia kurzu „AI Agents for Beginners“.

Plánujeme pokračovať v pridávaní lekcií na základe spätnej väzby a zmien v tomto neustále rastúcom odvetví, takže sa čoskoro opäť zastavte.

Ak chcete pokračovať v učení a tvorbe s AI Agentmi, pridajte sa do <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>.

Organizujeme tam workshopy, komunitné okrúhle stoly a „ask me anything“ relácie.

Máme tiež kolekciu Learn s ďalšími materiálmi, ktoré vám pomôžu začať stavať AI Agentov v produkcii.

## Predchádzajúca lekcia

[Metacognition Design Pattern](../09-metacognition/README.md)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.