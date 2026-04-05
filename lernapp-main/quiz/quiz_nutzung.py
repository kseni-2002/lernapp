import streamlit as st

QUESTIONS = [
    {
        "question": "Welche Nutzung von KI fördert nachhaltiges Lernen am stärksten?",
        "options": [
            "KI gibt direkt die fertige Lösung einer Aufgabe aus",
            "KI erstellt automatisch komplette Hausaufgaben",
            "KI stellt Rückfragen, gibt Hinweise und lässt dich selbst denken",
            "KI fasst alle Inhalte so kurz wie möglich zusammen"
        ],
        "answer_index": 2,
        "explanation": "Nachhaltiges Lernen wird besonders dann gefördert, wenn die KI Rückfragen stellt, Hinweise gibt und dich zum eigenen Denken anregt."
    },
    {
        "question": "Warum kann die Nutzung von KI als Lernbegleiter effektiver sein als klassische Lösungen?",
        "options": [
            "Weil KI immer richtige Antworten liefert",
            "Weil KI sich an dein individuelles Lernniveau anpassen kann",
            "Weil KI schneller arbeitet als Lehrkräfte",
            "Weil KI alle Aufgaben automatisch erledigt"
        ],
        "answer_index": 1,
        "explanation": "Ein Vorteil von KI ist, dass sie sich an dein Lernniveau anpassen und dadurch gezielter beim Lernen helfen kann."
    },
    {
        "question": "Welche Situation zeigt eine sinnvolle Nutzung von KI beim Lernen?",
        "options": [
            "Ein Schüler lässt sich eine komplette Analyse schreiben und übernimmt sie unverändert",
            "Eine Schülerin nutzt KI, um Fehler in ihrem eigenen Text zu erkennen und zu verbessern",
            "Ein Schüler nutzt KI nur, um möglichst schnell Ergebnisse zu bekommen",
            "Eine Schülerin kopiert Lösungen ohne sie zu verstehen"
        ],
        "answer_index": 1,
        "explanation": "Sinnvoll ist KI dann, wenn sie das eigene Lernen unterstützt, zum Beispiel durch Feedback und Verbesserungsvorschläge zum selbst geschriebenen Text."
    }
]


def show_quiz_nutzung():
    st.write("Wähle die beste Antwort aus. Die Fragen sind bewusst anspruchsvoll.")

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0
    if "total_answered" not in st.session_state:
        st.session_state.total_answered = 0

    if "nutzung_ki_quiz_done" not in st.session_state:
        st.session_state.nutzung_ki_quiz_done = False
    if "nutzung_ki_quiz_show_results" not in st.session_state:
        st.session_state.nutzung_ki_quiz_show_results = False
    if "nutzung_ki_quiz_score" not in st.session_state:
        st.session_state.nutzung_ki_quiz_score = 0
    if "nutzung_ki_quiz_feedback" not in st.session_state:
        st.session_state.nutzung_ki_quiz_feedback = []

    antworten = []

    for i, q in enumerate(QUESTIONS):
        st.write(f"**Frage {i + 1}: {q['question']}**")

        selected = st.radio(
            "Wähle die beste Antwort:",
            q["options"],
            index=None,
            key=f"nutzung_q_{i}"
        )
        antworten.append(selected)

    if st.button("Quiz auswerten", key="nutzung_quiz_auswerten"):
        punktzahl = 0
        feedback = []

        for i, q in enumerate(QUESTIONS):
            richtige_antwort = q["options"][q["answer_index"]]
            auswahl = antworten[i]

            if auswahl == richtige_antwort:
                punktzahl += 1
                feedback.append({
                    "status": "correct",
                    "frage": i + 1,
                    "richtige_antwort": richtige_antwort,
                    "explanation": q["explanation"]
                })
            else:
                feedback.append({
                    "status": "wrong",
                    "frage": i + 1,
                    "richtige_antwort": richtige_antwort,
                    "explanation": q["explanation"]
                })

        st.session_state.nutzung_ki_quiz_score = punktzahl
        st.session_state.nutzung_ki_quiz_feedback = feedback
        st.session_state.nutzung_ki_quiz_show_results = True

        if not st.session_state.nutzung_ki_quiz_done:
            st.session_state.total_score += punktzahl
            st.session_state.total_answered += len(QUESTIONS)
            st.session_state.nutzung_ki_quiz_done = True

        st.rerun()

    if st.session_state.nutzung_ki_quiz_show_results:
        st.markdown("---")
        st.subheader("Ergebnisse")

        for item in st.session_state.nutzung_ki_quiz_feedback:
            if item["status"] == "correct":
                st.success(f"Frage {item['frage']}: ✅Richtig")
                st.write(item["explanation"])
            else:
                st.error(f"Frage {item['frage']}: ❌Falsch")
                st.info(f"Richtige Antwort: {item['richtige_antwort']}")
                st.write(item["explanation"])

        st.markdown("---")
        st.write(f"### Deine Punktzahl: {st.session_state.nutzung_ki_quiz_score} / {len(QUESTIONS)}")

        if st.session_state.nutzung_ki_quiz_score == len(QUESTIONS):
            st.balloons()
            st.success("Sehr gut! Du hast die Nutzung von KI wirklich verstanden.")
        elif st.session_state.nutzung_ki_quiz_score == 2:
            st.success("Gut! Du hast ein solides Verständnis.")
        elif st.session_state.nutzung_ki_quiz_score == 1:
            st.warning("Teilweise richtig – lies dir das Kapitel nochmal genau durch.")
        else:
            st.warning("💡Schau dir das Kapitel nochmal genauer an.")