import json
import random
import streamlit as st

def tira_statistica():
    dadi = [random.randint(1, 6) for _ in range(4)]
    return sum(sorted(dadi)[1:])

def modificatore(statistica):
    mod = (statistica - 10) // 2
    return f"+{mod}" if mod >= 0 else str(mod)

@st.cache_data
def carica_dati():
    with open("tratti.json") as f:
        tratti = json.load(f)
    with open("nomi.json") as f:
        nomi = json.load(f)
    with open("cognomi.json") as f:
        cognomi = json.load(f)
    return tratti, nomi, cognomi

st.title("Generatore di NPC")

tratti, nomi, cognomi = carica_dati()

if st.button("Genera NPC"):
    razza = random.choice(tratti["razza"])
    nome = random.choice(nomi[razza])
    cognome = random.choice(cognomi[razza])
    personalita = random.choice(tratti["personalita"])
    colore_occhi = random.choice(tratti["colori_occhi"])
    colore_capelli = random.choice(tratti["colori_capelli"])
    corporatura = random.choice(tratti["corporatura"])

    FOR = tira_statistica()
    DES = tira_statistica()
    COST = tira_statistica()
    INT = tira_statistica()
    SAG = tira_statistica()
    CAR = tira_statistica()

    st.subheader(f"{nome} {cognome}")
    st.write(f"**Razza:** {razza}")

    st.divider()
    st.write("### Aspetto")
    col1, col2, col3 = st.columns(3)
    col1.metric("Occhi", colore_occhi)
    col2.metric("Capelli", colore_capelli)
    col3.metric("Corporatura", corporatura)

    st.divider()
    st.write("### Personalità")
    st.info(personalita)

    st.divider()
    st.write("### Statistiche")
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("FOR", FOR, modificatore(FOR))
    c2.metric("DES", DES, modificatore(DES))
    c3.metric("COS", COST, modificatore(COST))
    c4.metric("INT", INT, modificatore(INT))
    c5.metric("SAG", SAG, modificatore(SAG))
    c6.metric("CAR", CAR, modificatore(CAR))