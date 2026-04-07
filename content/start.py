import streamlit as st

def show_start():
    
    st.markdown("""
<h1 style='font-size: 40px; text-align: center;'>
Willkommen zur interaktiven Lernumgebung<br>
zu künstlicher Intelligenz!
</h1>
""", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,4,1])
    with col2:
        st.image("quiz/images/start.png", use_container_width=True)
        
    st.markdown("""---""")

    st.write("""
Diese App hilft dir dabei, **Künstliche Intelligenz (KI)** besser zu verstehen.

Du lernst:
- was KI ist und wie sie funktioniert
- wo du KI im Alltag findest
- welche Chancen und Risiken es gibt
- wie du KI sinnvoll nutzen kannst
""")
    

    st.info("""
Wähle links im Menü ein Modul aus und starte den Lernprozess! Bitte arbeite dich von oben nach unten durch.
""")

    st.success("""
💡 Ziel: Du sollst KI nicht nur nutzen, sondern auch verstehen und kritisch hinterfragen.
""")
    
    st.markdown("---")
    st.write("Viel Spaß beim Lernen!")

    total_score = st.session_state.get("total_score", 0)
    total_answered = st.session_state.get("total_answered", 0)

    st.subheader("Dein Fortschritt")
    st.write(f"Gesamtpunkte: **{total_score}**")
    st.write(f"Gelöste Aufgaben: **{total_answered}**")
