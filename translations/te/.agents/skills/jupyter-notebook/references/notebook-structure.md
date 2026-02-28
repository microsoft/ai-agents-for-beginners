# నోట్‌బుక్ నిర్మాణం

Jupyter నోట్‌బుక్లు JSON డాక్యుమెంట్లుగా ఉంటాయి, ఇవి ఈ భారీ స్థాయి ఆకారాన్ని కలిగి ఉంటాయి:

- `nbformat` మరియు `nbformat_minor`
- `metadata`
- `cells` (markdown మరియు code సెల్‌ల జాబితా)

When editing `.ipynb` files programmatically:

- టెంప్లేట్ నుండి `nbformat` మరియు `nbformat_minor` ను పరిరక్షించండి.
- `cells` ను క్రమబద్ధమైన జాబితాగా ఉంచండి; ఉద్దేశపూర్వకంగా కాకపోతే దాన్ని పునఃక్రమీకరించవద్దు.
- కోడ్ సెల్‌ల కోసం, తెలియని సందర్భాల్లో `execution_count` ను `null` గా సెట్ చేయండి.
- కోడ్ సెల్‌ల కోసం, scaffolding సమయంలో `outputs` ను ఖాళీ జాబితాగా సెట్ చేయండి.
- markdown సెల్‌ల కోసం, `cell_type="markdown"` మరియు `metadata={}` ను ఉంచండి.

బ్యాండ్ చేయబడిన టెంప్లేట్స్ లేదా `new_notebook.py` (ఉదాహరణకు, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) నుండి scaffolding చేయడాన్ని, raw notebook JSON ను చేతితో రాయడం కంటే ప్రాధాన్యం ఇవ్వండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
బాధ్యత నిరాకరణ:
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ అయిన [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమెటెడ్ అనువాదాల్లో తప్పులు లేదా లోపాలు ఉండవచ్చును. అసలైన పత్రాన్ని దాని మూల భాషలో అధికారిక మూలంగా పరిగణించాలి. కీలకమైన సమాచారానికి వృత్తిపరమైన మానవ అనువాదం చేయించుకోవాలని సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడిన కారణంగా ఏర్పడే ఏవైనా అవగాహనా లోపాలు లేదా తప్పుదారితీసే అర్థాలకై మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->