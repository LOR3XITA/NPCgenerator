# NPCgenerator

Un generatore casuale di personaggi non giocanti per campagne D&D 5e

---

## Requisiti

- Python 3.8 o superiore
- Streamlit

```bash
pip install streamlit
```

## Avvio

```bash
python -m streamlit run NPCgenerator.py
```

Il browser si aprirà automaticamente. Se non si apre, vai su `http://localhost:8501`

## Personalizzazione

Per aggiungere nuovi nomi, tratti e razze si può modificare i JSON

**ESEMPIO: Aggiungere una nuova razza:**
1. Aggiungi il nome della razza alla lista `"razza"` in `tratti.json`
2. Aggiungi una chiave con i relativi nomi in `nomi.json`
3. Aggiungi una chiave con i relativi cognomi in `cognomi.json`

## Funzionamento

Premi il pulsante Genera NPC per creare un personaggio casuale. Il programma:

1. Pesca una razza casuale da `tratti.json`
2. Usa la razza come chiave per scegliere nome e cognome coerenti da `nomi.json` e `cognomi.json`
3. Pesca tratti fisici e personalità dal pool di `tratti.json`
4. Tira le statistiche D&D con il metodo 4d6 drop lowest (tira 4 dadi da 6, scarta il più basso, somma i restanti)
5. Mostra tutto con i relativi modificatori
