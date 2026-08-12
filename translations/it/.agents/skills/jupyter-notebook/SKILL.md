---
name: jupyter-notebook
description: Usa quando l'utente chiede di creare, strutturare o modificare notebook
  Jupyter (`.ipynb`) per esperimenti, esplorazioni o tutorial; privilegia i modelli
  inclusi ed esegui lo script di supporto `new_notebook.py` per generare un notebook
  di partenza pulito.
---
# Competenze Jupyter Notebook

Crea notebook Jupyter puliti e riproducibili per due modalità principali:

- Esperimenti e analisi esplorativa
- Tutorial e percorsi didattici

Preferisci i template inclusi e lo script di supporto per una struttura coerente e meno errori nel JSON.

## Quando usare
- Crea un nuovo notebook `.ipynb` da zero.
- Converti appunti grezzi o script in un notebook strutturato.
- Refattorizza un notebook esistente per renderlo più riproducibile e facile da scorrere.
- Crea esperimenti o tutorial che saranno letti o rieseguiti da altre persone.

## Albero decisionale
- Se la richiesta è esplorativa, analitica o guidata da ipotesi, scegli `experiment`.
- Se la richiesta è istruttiva, passo-passo o specifica per un pubblico, scegli `tutorial`.
- Se stai modificando un notebook esistente, trattalo come una refattorizzazione: preserva l'intento e migliora la struttura.

## Percorso di competenza (impostalo una volta)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

Le skill a livello utente si installano sotto `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Flusso di lavoro
1. Definisci l'intento.
Identifica il tipo di notebook: `experiment` o `tutorial`.
Registra l'obiettivo, il pubblico e cosa significa 'fatto'.

2. Crea la struttura a partire dal template.
Usa lo script di supporto per evitare di scrivere manualmente il JSON grezzo del notebook.

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind experiment \
  --title "Compare prompt variants" \
  --out output/jupyter-notebook/compare-prompt-variants.ipynb
```

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind tutorial \
  --title "Intro to embeddings" \
  --out output/jupyter-notebook/intro-to-embeddings.ipynb
```

3. Riempi il notebook con piccoli passi eseguibili.
Mantieni ogni cella di codice focalizzata su un solo passo.
Aggiungi brevi celle markdown che spieghino lo scopo e il risultato atteso.
Evita output grandi e rumorosi quando basta un breve riepilogo.

4. Applica il pattern giusto.
Per gli esperimenti, segui `references/experiment-patterns.md`.
Per i tutorial, segui `references/tutorial-patterns.md`.

5. Modifica in modo sicuro quando lavori con notebook esistenti.
Preserva la struttura del notebook; evita di riordinare le celle a meno che ciò non migliori la narrazione dall'alto verso il basso.
Preferisci modifiche mirate rispetto a riscritture complete.
Se devi modificare il JSON grezzo, rivedi prima `references/notebook-structure.md`.

6. Valida il risultato.
Esegui il notebook dall'alto verso il basso quando l'ambiente lo permette.
Se l'esecuzione non è possibile, dichiaralo esplicitamente e indica come validarlo localmente.
Usa la checklist dell'ultimo passaggio in `references/quality-checklist.md`.

## Template e script di supporto
- I template risiedono in `assets/experiment-template.ipynb` e `assets/tutorial-template.ipynb`.
- Lo script di supporto carica un template, aggiorna la cella del titolo e scrive un notebook.

Percorso dello script:
- `$JUPYTER_NOTEBOOK_CLI` (installato di default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Convenzioni per file temporanei e output
- Usa `tmp/jupyter-notebook/` per i file intermedi; elimina quando hai finito.
- Scrivi gli artefatti finali in `output/jupyter-notebook/` quando lavori in questo repo.
- Usa nomi di file stabili e descrittivi (per esempio, `ablation-temperature.ipynb`).

## Dipendenze (installa solo quando necessario)
Preferisci `uv` per la gestione delle dipendenze.

Pacchetti Python opzionali per l'esecuzione locale dei notebook:

```bash
uv pip install jupyterlab ipykernel
```

Lo script di scaffolding incluso utilizza solo la libreria standard di Python e non richiede dipendenze aggiuntive.

## Ambiente
Nessuna variabile d'ambiente richiesta.

## Mappa di riferimento
- `references/experiment-patterns.md`: struttura degli esperimenti e euristiche.
- `references/tutorial-patterns.md`: struttura dei tutorial e flusso didattico.
- `references/notebook-structure.md`: forma del JSON del notebook e regole per modifiche sicure.
- `references/quality-checklist.md`: checklist finale di validazione.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Dichiarazione di non responsabilità:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur facendo del nostro meglio per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->