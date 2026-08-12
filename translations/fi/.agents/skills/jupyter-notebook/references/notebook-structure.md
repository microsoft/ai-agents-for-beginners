# Muistikirjan rakenne

Jupyter-muistikirjat ovat JSON-dokumentteja, joilla on seuraava yleinen rakenne:

- `nbformat` ja `nbformat_minor`
- `metadata`
- `cells` (lista markdown- ja koodisoluista)

Kun muokkaat `.ipynb`-tiedostoja ohjelmallisesti:

- Säilytä mallin `nbformat` ja `nbformat_minor`.
- Pidä `cells` järjestettynä listana; älä muuta järjestystä, ellei se ole tarkoituksellista.
- Koodisoluille aseta `execution_count` arvoksi `null`, jos se on tuntematon.
- Koodisoluille aseta `outputs` tyhjäksi listaksi, kun luot alustavaa rakennetta.
- Markdown-soluissa pidä `cell_type="markdown"` ja `metadata={}`.

Suosi rungon luontia mukana tulevista malleista tai `new_notebook.py` (esimerkiksi `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) sen sijaan, että kirjoittaisit raakaa muistikirja-JSONia käsin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastuuvapauslauseke:
Tämä asiakirja on käännetty käyttäen tekoälypohjaista käännöspalvelua Co-op Translator (https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomaathan, että automatisoiduissa käännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä on pidettävä ensisijaisena lähteenä. Kriittisissä asioissa suosittelemme ammattimaisen kääntäjän tekemää käännöstä. Emme ole vastuussa tästä käännöksestä mahdollisesti aiheutuvista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->