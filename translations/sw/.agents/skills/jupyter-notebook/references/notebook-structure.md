# Muundo wa Daftari

Daftari za Jupyter ni nyaraka za JSON zenye muundo wa ngazi ya juu kama ifuatavyo:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (orodha ya seli za markdown na seli za code)

Unapohariri faili za `.ipynb` kwa njia ya programu:

- Preserve `nbformat` and `nbformat_minor` from the template.
- Keep `cells` as an ordered list; do not reorder unless intentional.
- Kwa seli za code, weka `execution_count` kuwa `null` wakati haijulikani.
- Kwa seli za code, weka `outputs` kuwa orodha tupu wakati unapotengeneza muundo wa awali.
- Kwa seli za markdown, giữ `cell_type="markdown"` and `metadata={}`.

Pendelea kutengeneza muundo wa awali kutoka kwenye templeti zilizofungwa au `new_notebook.py` (kwa mfano, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) badala ya kuandika kwa mkono JSON ghafi ya daftari.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Tamko la kutokuwajibika:
Nyaraka hii imetafsiriwa kwa kutumia huduma ya utafsiri wa AI, Co-op Translator (https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au zisizo sahihi. Nyaraka ya asili kwa lugha yake ya asili inapaswa kutambulika kama chanzo rasmi. Kwa taarifa muhimu, tunapendekeza kutumia tafsiri ya kitaalamu iliyofanywa na mtafsiri wa kibinadamu. Hatuwajibiki kwa uelewa mbaya au tafsiri isiyo sahihi zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->