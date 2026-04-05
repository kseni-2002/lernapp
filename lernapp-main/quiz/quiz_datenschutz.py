import streamlit as st

QUESTIONS = [
    {
        "question": "Welche Daten gibst du selbst aktiv ein?",
        "options": [
            "E-Mail-Adresse und IP-Adresse",
            "Nutzungszeit",
            "Standortinformationen und Geräteinformationen",
            "Fragen und Nachrichten im Chat"
        ],
        "answer_index": 3,
        "explanation": "Fragen und Nachrichten im Chat gibst du selbst aktiv ein. Das sind bewusst eingegebene Daten."
    },
    {
        "question": "Welche Daten werden automatisch erhoben?",
        "options": [
            "Name und Alter",
            "E-Mail-Adresse",
            "IP-Adresse",
            "Fragen und Nachrichten im Chat"
        ],
        "answer_index": 2,
        "explanation": "Die IP-Adresse wird automatisch erfasst, sobald du eine Website oder App nutzt – ohne dass du sie selbst eingibst."
    },
    {
        "question": "Wofür können Daten genutzt werden?",
        "options": [
            "Für personalisierte Werbung",
            "Für das Training der KI",
            "Gar nicht",
            "Nur für persönliche Anpassung an dich"
        ],
        "answer_index": 1,
        "explanation": "Ein Teil der Daten kann genutzt werden, um die KI zu verbessern und weiterzuentwickeln."
    },
    {
        "question": "Welche Daten können nicht mehr gelöscht werden?",
        "options": [
            "Trainingsdaten im Modell",
            "Chatverläufe",
            "dein Benutzerkonto",
            "Gar keine Daten können gelöscht werden"
        ],
        "answer_index": 0,
        "explanation": "Bereits im Modell verarbeitete Daten können nicht gelöscht werden, aber alle mit deinem Konto verbundenen Daten normalerweise schon."
    },
    {
        "question": "Wie kannst du deine Daten besser schützen?",
        "options": [
            "Indem du ChatGPT deine Login-Daten gibst und schreibst „Sie dürfen nicht weitergegeben werden“",
            "Indem du keine sensiblen Daten eingibst",
            "Indem du statt deine, die Daten deiner Eltern angibst",
            "Indem du statt ChatGPT Gemini benutzt"
        ],
        "answer_index": 1,
        "explanation": "Der beste Schutz ist, keine sensiblen Daten wie Passwörter oder Adressen einzugeben."
    }
]


def show_quiz_datenschutz():
    if "total_score" not in st.session_state:
        st.session_state.total_score = 0
    if "total_answered" not in st.session_state:
        st.session_state.total_answered = 0

    if "datenschutz_quiz_done" not in st.session_state:
        st.session_state.datenschutz_quiz_done = False
    if "datenschutz_quiz_show_results" not in st.session_state:
        st.session_state.datenschutz_quiz_show_results = False
    if "datenschutz_quiz_score" not in st.session_state:
        st.session_state.datenschutz_quiz_score = 0
    if "datenschutz_quiz_feedback" not in st.session_state:
        st.session_state.datenschutz_quiz_feedback = []

    antworten = []

    for i, q in enumerate(QUESTIONS):
        st.write(f"**Frage {i + 1}: {q['question']}**")

        selected = st.radio(
            "Wähle eine Antwort:",
            q["options"],
            index=None,
            key=f"datenschutz_q_{i}"
        )
        antworten.append(selected)

    if st.button("Quiz auswerten", key="datenschutz_quiz_auswerten"):
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
                    "hinweis": "",
                    "explanation": q["explanation"]
                })
            else:
                if i == 0:
                    hinweis = "Welche Informationen werden gespeichert und woher kommen sie?"
                elif i == 1:
                    hinweis = "Welche Informationen werden gespeichert und woher kommen sie?"
                elif i == 2:
                    hinweis = "Wofür werden diese Informationen benutzt?"
                elif i == 3:
                    hinweis = "Welche Daten können gelöscht werden?"
                else:
                    hinweis = "Wie kannst du deine Daten besser schützen?"

                feedback.append({
                    "status": "wrong",
                    "frage": i + 1,
                    "richtige_antwort": richtige_antwort,
                    "hinweis": hinweis,
                    "explanation": q["explanation"]
                })

        st.session_state.datenschutz_quiz_score = punktzahl
        st.session_state.datenschutz_quiz_feedback = feedback
        st.session_state.datenschutz_quiz_show_results = True

        if not st.session_state.datenschutz_quiz_done:
            st.session_state.total_score += punktzahl
            st.session_state.total_answered += len(QUESTIONS)
            st.session_state.datenschutz_quiz_done = True

        st.rerun()

    if st.session_state.datenschutz_quiz_show_results:
        st.markdown("---")
        st.subheader("Ergebnisse")

        for item in st.session_state.datenschutz_quiz_feedback:
            if item["status"] == "correct":
                st.success(f"Frage {item['frage']}: Richtig ✅")
                st.write(item["explanation"])
            else:
                st.error(f"Frage {item['frage']}: Falsch ❌")
                st.info(
                    f"Richtige Antwort: {item['richtige_antwort']}\n\n"
                    f'💡Schau dir noch mal den Abschnitt „{item["hinweis"]}“ an.'
                )
                st.write(item["explanation"])

        st.markdown("---")
        st.write(
            f"### Deine Punktzahl: {st.session_state.datenschutz_quiz_score} / {len(QUESTIONS)}"
        )

        if st.session_state.datenschutz_quiz_score == len(QUESTIONS):
            st.balloons()
            st.success("Super! Du hast alle Fragen richtig beantwortet. 🎉")
        elif st.session_state.datenschutz_quiz_score >= 3:
            st.success("Gut gemacht! Du hast viele Fragen richtig beantwortet.")
        else:
            st.warning("💡Schau dir das Kapitel nochmal an und versuche es erneut.")