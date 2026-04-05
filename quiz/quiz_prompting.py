import streamlit as st


def show_quiz_prompting():
    st.write("""
Lies die Situation genau und wähle alle Informationen aus,
die sinnvoll in einen Prompt gehören.
""")

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0
    if "total_answered" not in st.session_state:
        st.session_state.total_answered = 0

    if "prompting_quiz_done" not in st.session_state:
        st.session_state.prompting_quiz_done = False
    if "prompting_quiz_show_results" not in st.session_state:
        st.session_state.prompting_quiz_show_results = False
    if "prompting_score" not in st.session_state:
        st.session_state.prompting_score = 0
    if "prompting_feedback" not in st.session_state:
        st.session_state.prompting_feedback = []

    # -------------------------
    # Frage 1
    # -------------------------
    st.write("### 1. Situation:")
    st.write("""
Du möchtest dir den **Satz des Pythagoras** erklären lassen,
weil du ihn für eine Klassenarbeit lernen musst.
""")

    q1 = st.multiselect(
        "Welche Informationen gehören in deinen Prompt?",
        [
            "Hallo Chat",
            "Ich bin in der 8. Klasse",
            "Ich gehe auf ein Gymnasium",
            "Erkläre es mir Schritt für Schritt",
            "Meine Login-Daten sind xyz",
            "Gib mir ein Beispiel mit Zahlen",
            "Danke für deine Hilfe"
        ],
        key="prompt_q1"
    )

    richtige_q1 = {
        "Ich bin in der 8. Klasse",
        "Ich gehe auf ein Gymnasium",
        "Erkläre es mir Schritt für Schritt",
        "Gib mir ein Beispiel mit Zahlen"
    }

    # -------------------------
    # Frage 2
    # -------------------------
    st.markdown("---")
    st.write("### 2. Situation:")
    st.write("""
Du sollst einen Aufsatz in Deutsch zum Thema Mein Stadtteil schreiben und möchtest Feedback zu deinem Text bekommen.
""")

    q2 = st.multiselect(
        "Welche Informationen gehören in deinen Prompt?",
        [
            "Hier ist mein Text: [...]",
            "Achte auf Grammatik und Ausdruck",
            "Bewerte nach typischen Schulkriterien",
            "Mein Lehrer heißt Herr Müller",
            "Ich wohne in der Goethestraße 17",
            "Ich bin in der 9. Klasse",
            "Danke dir :)"
        ],
        key="prompt_q2"
    )

    richtige_q2 = {
        "Hier ist mein Text: [...]",
        "Achte auf Grammatik und Ausdruck",
        "Bewerte nach typischen Schulkriterien",
        "Ich bin in der 9. Klasse"
    }

    # -------------------------
    # Frage 3
    # -------------------------
    st.markdown("---")
    st.write("### 3. Situation:")
    st.write("""
Du möchtest für eine **Geschichtsprüfung lernen** und dich von der KI abfragen lassen.
""")

    q3 = st.multiselect(
        "Welche Informationen gehören in deinen Prompt?",
        [
            "Frage mich einzeln ab",
            "Gib mir Feedback nach jeder Antwort",
            "Ich bin in der 10. Klasse",
            "Thema: Französische Revolution",
            "Meine Adresse ist ...",
            "Mein Passwort ist ...",
            "Danke dir :)"
        ],
        key="prompt_q3"
    )

    richtige_q3 = {
        "Frage mich einzeln ab",
        "Gib mir Feedback nach jeder Antwort",
        "Ich bin in der 10. Klasse",
        "Thema: Französische Revolution"
    }

    # -------------------------
    # Auswertung
    # -------------------------
    if st.button("Quiz abschließen", key="prompting_quiz_abschliessen"):
        score = 0
        feedback = []

        if set(q1) == richtige_q1:
            score += 1
            feedback.append({
                "status": "correct",
                "frage": 1,
                "hinweis": "",
                "text": """💡 Wichtig:
Relevante Infos sind Niveau, Aufgabe und gewünschte Erklärung.
Unnötig sind persönliche Daten oder Höflichkeitsfloskeln.
"""
            })
        else:
            feedback.append({
                "status": "wrong",
                "frage": 1,
                "hinweis": "Schau dir noch mal den Abschnitt „4. Kontext geben (inkl. Quellen)“ und „3. Schrittweise arbeiten“ an.",
                "text": """💡 Wichtig:
Relevante Infos sind Niveau, Aufgabe und gewünschte Erklärung.
Unnötig sind persönliche Daten oder Höflichkeitsfloskeln.
"""
            })

        if set(q2) == richtige_q2:
            score += 1
            feedback.append({
                "status": "correct",
                "frage": 2,
                "hinweis": "",
                "text": """💡 Wichtig:
Gib der KI deinen Text, klare Kriterien und dein Niveau.
Private Daten oder Namen sind nicht relevant.
"""
            })
        else:
            feedback.append({
                "status": "wrong",
                "frage": 2,
                "hinweis": "Schau dir noch mal den Abschnitt „4. Kontext geben (inkl. Quellen)“ und „6. Format festlegen“ an.",
                "text": """💡 Wichtig:
Gib der KI deinen Text, klare Kriterien und dein Niveau.
Private Daten oder Namen sind nicht relevant.
"""
            })

        if set(q3) == richtige_q3:
            score += 1
            feedback.append({
                "status": "correct",
                "frage": 3,
                "hinweis": "",
                "text": """💡 Wichtig:
Ein guter Prompt enthält:
- Thema  
- Niveau  
- klare Arbeitsweise
"""
            })
        else:
            feedback.append({
                "status": "wrong",
                "frage": 3,
                "hinweis": "Schau dir noch mal den Abschnitt „1. Ziel klar formulieren“, „4. Kontext geben (inkl. Quellen)“ und „7. Rückfragen erlauben“ an.",
                "text": """💡 Wichtig:
Ein guter Prompt enthält:
- Thema  
- Niveau  
- klare Arbeitsweise
"""
            })

        st.session_state.prompting_score = score
        st.session_state.prompting_feedback = feedback
        st.session_state.prompting_quiz_show_results = True

        if not st.session_state.prompting_quiz_done:
            st.session_state.total_score += score
            st.session_state.total_answered += 3
            st.session_state.prompting_quiz_done = True

        st.rerun()

    if st.session_state.prompting_quiz_show_results:
        st.markdown("---")
        st.subheader("Ergebnisse")

        for item in st.session_state.prompting_feedback:
            if item["status"] == "correct":
                st.success(f"Frage {item['frage']}: Richtig ✅")
                st.write(item["text"])
            else:
                st.error(f"Frage {item['frage']}: Falsch ❌")
                st.info(item["hinweis"])
                st.write(item["text"])

        st.markdown("---")
        st.write(f"### Deine Punktzahl: {st.session_state.prompting_score} / 3")

        if st.session_state.prompting_score == 3:
            st.balloons()
            st.success("Perfekt! Du kannst sehr gut prompten 👏")
        elif st.session_state.prompting_score == 2:
            st.success("Gut! Du hast ein solides Verständnis.")
        elif st.session_state.prompting_score == 1:
            st.warning("Teilweise richtig – schau dir die Regeln nochmal an.")
        else:
            st.warning("Schau dir das Kapitel nochmal genauer an.")