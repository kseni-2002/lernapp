import streamlit as st
import pandas as pd

from quiz.quiz_datenschutz import show_quiz_datenschutz

vergleich_daten = {
    "Aktiv bereitgestellte Informationen": [
        "Name",
        "E-Mail-Adresse",
        "Chatnachrichten",
        "hochgeladene Dateien"
    ],
    "Automatisch erhobene Informationen": [
        "IP-Adresse",
        "Geräteinformationen",
        "Nutzungszeit",
        "Standortinformationen"
    ]
}


def mark_datenschutz_done():
    if "datenschutz_done" in st.session_state:
        st.session_state.datenschutz_done = True


def show_datenschutz():
    if "datenschutz_done" not in st.session_state:
        st.session_state.datenschutz_done = False

    st.title("Datenschutz bei der Nutzung der KI")

    st.write(
        "Künstliche Intelligenz funktioniert, indem sie viele Daten analysiert und verarbeitet. "
        "Damit du sie sicher nutzen kannst und deine persönlichen Informationen geschützt bleiben, "
        "lernst du in diesem Kapitel den richtigen Umgang mit deinen Daten."
    )

    st.header("Welche Informationen werden gespeichert und woher kommen sie?")

    st.write(
        "Informationen über Nutzerinnen und Nutzer entstehen an verschiedenen Stellen. "
        "Daten, die du selbst eingibst sind **aktiv bereitgestellte Daten**. Sie entstehen beispielsweise:"
    )

    st.markdown("""
- bei der Kontoerstellung (z.B. deine Kontoinformationen)
- in Konversationen (z. B. deine Fragen oder Nachrichten im Chat)
- durch hochgeladene Dateien (z. B. Bilder oder Dokumente)
""")

    st.write("""
Andere Daten fallen bei der Nutzung der App oder Webseite **automatisch** an. 
Außerdem können **öffentliche Daten** aus den Inhalten im Internet benutzt werden, wenn das KI-System mit Online-Diensten arbeitet.
    """)

    st.write(
        "In der Tabelle siehst du einige Beispiele an Daten, die erhoben und gespeichert werden."
    )

    df_vergleich = pd.DataFrame(vergleich_daten)
    st.dataframe(df_vergleich, hide_index=True)

    st.header("Wofür werden diese Informationen benutzt?")
    st.write("""
- **Nutzung der Daten für das Training:** Ein Teil der gesammelten Informationen kann genutzt werden, um KI-Systeme weiterzuentwickeln. Dadurch lernen Algorithmen, Muster zu erkennen und in Zukunft bessere Antworten zu geben. Die Daten helfen also dabei, die KI zu verbessern.
- **Nutzung der Daten für die Anpassung an die Nutzerin oder den Nutzer:** Einige Informationen werden genutzt, um Inhalte besser an einzelne Nutzerinnen und Nutzer anzupassen. So können zum Beispiel Einstellungen gespeichert, Vorschläge gemacht oder Antworten persönlicher gestaltet werden.
    """)

    st.header("Welche Daten können gelöscht werden?")

    st.write("""
Für alle Nutzerinnen und Nutzer in der EU gilt das gleiche Recht, das von jedem Anbieter gewährleistet wird. Bei allen personenbezogenen Daten, die von der KI gespeichert wurden, muss im Normalfall die Möglichkeit bestehen, sie **wieder zu löschen**. Dazu gehören:
- Chatverläufe
- hochgeladene Dateien (Bilder, PDF-Dateien etc.)
- Konto und alle damit verbundenen Daten
""")

    st.warning(
        "Hinweis: Deine Daten werden nach der Löschung noch für 30 Tage gespeichert."
    )

    st.write("""
        Manche Informationen werden **nicht mehr gelöscht**:
- **Daten für das Training:** Wenn deine Daten in das Training hineinfließen, können sie aus den Algorithmen nicht wieder entfernt werden. Aber: sie sind dann schon anonymisiert und können nicht mehr mit deinem Konto verknüpft werden.
- **Längere Aufbewahrung in Ausnahmefällen:** Daten werden in Ausnahmefälle länger als 30 Tage aufbewahrt, wenn sie zum Beispiel für die Sicherheit oder zur Betrugsverhinderung gebraucht werden.
""")

    st.warning(
        "Hinweis: In manchen Fällen können Daten auch weitergegeben werden, zum Beispiel an Regierungsbehörden "
        "oder an Eltern beziehungsweise Erziehungsberechtigte von Jugendlichen."
    )

    st.header("Wie kannst du deine Daten besser schützen?")

    st.write(
        "Am Beispiel von ChatGPT erklären wir dir, wie du deine Daten besser schützen kannst. "
        "Eine ähnliche Vorgehensweise gilt auch für viele andere KI-Systeme."
    )

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "1. Keine sensiblen Daten",
        "2. Daten einsehen",
        "3. Training ausschalten",
        "4. Chats löschen",
        "5. Dateien löschen",
        "6. Temporärer Chat"
    ])

    with tab1:
        st.subheader("Teile keine sensiblen Daten")
        st.write(
            "Gib keine persönlichen Informationen ein, die missbraucht werden könnten. "
            "Dazu gehören zum Beispiel:"
        )

        st.markdown("""
- deine Adresse
- deine Telefonnummer
- Passwörter
        """)

    with tab2:
        st.subheader("Daten einsehen (Export)")
        st.write(
            "Du kannst eine Datei mit deinen Kontodaten und Chats anfordern. "
            "So bekommst du einen Überblick darüber, welche Informationen über dich gespeichert wurden."
        )
        st.markdown("""
**So geht's:**
1. Einstellungen öffnen
2. Datenkontrollen auswählen
3. Daten exportieren anklicken
4. Export starten
""")

    with tab3:
        st.subheader("Nutzung deiner Daten für Training ausschalten")
        st.write(
            "Du kannst verhindern, dass deine Daten für das Training der KI genutzt werden."
        )
        st.markdown("""
**So geht's:**
1. Einstellungen öffnen
2. Datenkontrollen auswählen
3. „Das Modell für alle verbessern“ deaktivieren
""")

    with tab4:
        st.subheader("Chats löschen")
        st.write("Du kannst einzelne oder alle Chats löschen.")
        st.markdown("""
**So geht's:**
1. Einstellungen öffnen
2. Datenkontrollen auswählen
3. „Alle Chats löschen“ auswählen
""")

    with tab5:
        st.subheader("Dateien und Links löschen")
        st.write(
            "Auch hochgeladene Dateien und geteilte Links kannst du wieder entfernen."
        )
        st.markdown("""
**So geht's:**
1. Einstellungen öffnen
2. Datenkontrollen auswählen
3. Weitergegebene Links verwalten
""")

    with tab6:
        st.subheader("Temporären Chat nutzen")
        st.write(
            "Du kannst einen temporären Chat verwenden. In diesem Modus werden deine Eingaben "
            "nicht gespeichert."
        )
        st.markdown("""
**So geht's:**
1. Neuen Chat starten
2. Symbol mit der gestrichelten Sprechblase auswählen (oben rechts im Chat)
""")

    st.header("Quiz: Datenschutz")
    show_quiz_datenschutz()

    st.markdown("---")
    if st.button("✅ Kapitel abschließen", key="finish_datenschutz"):
        mark_datenschutz_done()
        st.success("Das Kapitel 'Datenschutz' wurde als abgeschlossen markiert.")
        st.rerun()