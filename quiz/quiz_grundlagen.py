import streamlit as st
from quiz.quiz_utils import init_global_score


QUESTIONS = [
    {
        "question": "Welche Aussage beschreibt Künstliche Intelligenz am besten?",
        "options": [
            "KI ist ein Roboter, der wie ein Mensch denken kann",
            "KI ist ein Oberbegriff für Systeme, die Aufgaben lösen, für die sonst menschliches Denken nötig ist",
            "KI ist nur ein anderes Wort für Computerprogramme",
            "KI funktioniert immer selbstständig und fehlerfrei"
        ],
        "answer_index": 1,
        "explanation": "KI ist ein Oberbegriff für Systeme, die Aufgaben lösen können, für die normalerweise menschliches Denken nötig ist."
    },
    {
        "question": "Was ist der wichtigste Unterschied zwischen klassischer Programmierung und maschinellem Lernen?",
        "options": [
            "Beim maschinellen Lernen lernt das System aus Daten statt nur festen Regeln zu folgen",
            "Beim maschinellen Lernen braucht man keine Daten",
            "Bei klassischer Programmierung können Computer keine Ergebnisse berechnen",
            "Maschinelles Lernen funktioniert nur bei Robotern"
        ],
        "answer_index": 0,
        "explanation": "Beim maschinellen Lernen werden nicht nur feste Regeln vorgegeben. Das System lernt Muster aus Daten."
    },
    {
        "question": "Warum kann eine KI nach dem Training Hund und Katze auf neuen Bildern unterscheiden?",
        "options": [
            "Weil sie Tiere wirklich so sieht wie ein Mensch",
            "Weil sie die Bilder auswendig gespeichert hat und nie etwas Neues berechnet",
            "Weil sie Muster und typische Merkmale in den Trainingsdaten erkannt hat",
            "Weil Menschen ihr bei jedem neuen Bild die Antwort eingeben"
        ],
        "answer_index": 2,
        "explanation": "Die KI erkennt in Trainingsdaten typische Merkmale und Muster. So kann sie neue Bilder einordnen."
    },
    {
        "question": "Was trifft auf ein Sprachmodell wie ChatGPT am ehesten zu?",
        "options": [
            "Es kennt immer die eine richtige Wahrheit",
            "Es berechnet, welche Wörter oder Sätze wahrscheinlich gut zusammenpassen",
            "Es sucht nur fertige Antworten aus dem Internet heraus",
            "Es funktioniert ganz ohne Training mit Texten"
        ],
        "answer_index": 1,
        "explanation": "Sprachmodelle arbeiten vor allem mit Wahrscheinlichkeiten und sagen voraus, welches Wort oder welcher Satz gut passt."
    },
    {
        "question": "Warum wirken Antworten von Sprachmodellen oft menschlich?",
        "options": [
            "Weil die KI Gefühle und Absichten wie ein Mensch besitzt",
            "Weil das Modell Sprache, Satzbau und typische Wortfolgen aus vielen Texten gelernt hat",
            "Weil hinter jeder Antwort heimlich ein Mensch sitzt",
            "Weil Sprachmodelle nur sehr kurze Standardsätze benutzen"
        ],
        "answer_index": 1,
        "explanation": "Das Modell wurde mit sehr vielen Texten trainiert und hat dadurch Muster von Sprache gelernt."
    },
    {
        "question": "Welche Aussage grenzt Deep Learning am besten von allgemeinem maschinellen Lernen ab?",
        "options": [
            "Deep Learning ist eine Form des maschinellen Lernens mit vielen Verarbeitungsschichten",
            "Deep Learning ist kein Teil von KI",
            "Deep Learning bedeutet nur, dass besonders lange Texte gelesen werden",
            "Deep Learning braucht keine Daten"
        ],
        "answer_index": 0,
        "explanation": "Deep Learning ist ein Teilbereich des maschinellen Lernens und arbeitet mit vielen aufeinander aufbauenden Schichten."
    },
    {
        "question": "Welche Anwendung passt am besten zu Sprachverarbeitung?",
        "options": [
            "Ein Chatbot beantwortet Fragen in natürlicher Sprache",
            "Eine Lampe geht an, wenn man auf einen Schalter drückt",
            "Ein Taschenrechner addiert zwei Zahlen",
            "Ein Drucker druckt ein Bild aus"
        ],
        "answer_index": 0,
        "explanation": "Sprachverarbeitung beschäftigt sich mit menschlicher Sprache, zum Beispiel bei Chatbots oder Übersetzungsprogrammen."
    },
    {
        "question": "Welche Aussage über KI im Alltag ist richtig?",
        "options": [
            "KI steckt heute fast nur in Robotern",
            "KI wird unter anderem in Navigations-Apps, Streaming-Plattformen und Sprachassistenten genutzt",
            "KI kommt nur in der Forschung vor",
            "KI wird nur für das Schreiben von Texten genutzt"
        ],
        "answer_index": 1,
        "explanation": "KI begegnet uns heute in vielen Alltagsanwendungen, zum Beispiel bei Empfehlungen, Navigation oder Sprachassistenten."
    }
]


def show_grundlagen_aufgabe_1():
    st.markdown("### Mini-Aufgabe")
    init_global_score()

    if "g_task0_checked" not in st.session_state:
        st.session_state.g_task0_checked = False
    if "g_task0_scored" not in st.session_state:
        st.session_state.g_task0_scored = False
    if "g_task0_correct" not in st.session_state:
        st.session_state.g_task0_correct = False

    choice = st.radio(
        "Welches Beispiel zeigt am besten den Einsatz von KI?",
        [
            "Ein Taschenrechner addiert zwei Zahlen",
            "Chatgpt beantwortet deine Frage über Hausaufgaben",
            "Eine Lampe wird mit einem Schalter eingeschaltet",
            "Ein Drucker druckt ein Dokument aus"
        ],
        key="g_task0_choice"
    )

    if not st.session_state.g_task0_checked:
        if st.button("Antwort prüfen", key="g_task0_button"):
            st.session_state.g_task0_checked = True

            if choice == "Chatgpt beantwortet deine Frage über Hausaufgaben":
                st.session_state.g_task0_correct = True
                if not st.session_state.g_task0_scored:
                    st.session_state.total_score += 1
                    st.session_state.total_answered += 1
                    st.session_state.g_task0_scored = True
            else:
                st.session_state.g_task0_correct = False
                if not st.session_state.g_task0_scored:
                    st.session_state.total_answered += 1
                    st.session_state.g_task0_scored = True

            st.rerun()

    else:
        if st.session_state.g_task0_correct:
            st.success("✅ Richtig! Chatgpt ist ein sehr bekanntes KI-Tool.")
        else:
            st.error("❌ Nicht ganz.")

        st.info("Wie KI funktioniert lernst du in den nächsten Modulen! ")

        if st.button("Nochmal versuchen", key="g_task0_retry"):
            st.session_state.g_task0_checked = False
            st.session_state.g_task0_correct = False
            st.rerun()


def show_grundlagen_aufgabe_2_1():
    st.markdown("### Muster erkennen")
    st.write("Schau dir diese Reihe an:")

    st.markdown("2, 4, 8, 16, 32, ❓")
    init_global_score()

    if "ml_pattern_checked" not in st.session_state:
        st.session_state.ml_pattern_checked = False
    if "ml_pattern_scored" not in st.session_state:
        st.session_state.ml_pattern_scored = False
    if "ml_pattern_correct" not in st.session_state:
        st.session_state.ml_pattern_correct = False

    choice = st.radio(
        "Was kommt als Nächstes?",
        ["34", "48", "64", "60"],
        key="ml_pattern_task"
    )

    if not st.session_state.ml_pattern_checked:
        if st.button("Muster prüfen", key="ml_pattern_check"):
            st.session_state.ml_pattern_checked = True

            if choice == "64":
                st.session_state.ml_pattern_correct = True
                if not st.session_state.ml_pattern_scored:
                    st.session_state.total_score += 1
                    st.session_state.total_answered += 1
                    st.session_state.ml_pattern_scored = True
            else:
                st.session_state.ml_pattern_correct = False
                if not st.session_state.ml_pattern_scored:
                    st.session_state.total_answered += 1
                    st.session_state.ml_pattern_scored = True

            st.rerun()

    else:
        if st.session_state.ml_pattern_correct:
            st.success("✅ Richtig! Du hast das Muster erkannt. Die Zahlen werden immer verdoppelt.")
            st.info("Genauso sucht auch KI nach Mustern – nur mit viel mehr Daten.")
        else:
            st.error("❌ Nicht ganz. Schau dir die Reihe nochmal genau an.")

        st.write("""
Maschinelles Lernen bedeutet also:
Die KI lernt aus Beispielen und kann dadurch Vorhersagen oder Einordnungen treffen.
""")

        if st.button("Nochmal versuchen", key="ml_pattern_retry"):
            st.session_state.ml_pattern_checked = False
            st.session_state.ml_pattern_correct = False
            st.rerun()


def show_grundlagen_aufgabe_2_2():
    st.markdown("### Mini-Aufgabe")
    init_global_score()

    if "g_task1_checked" not in st.session_state:
        st.session_state.g_task1_checked = False
    if "g_task1_scored" not in st.session_state:
        st.session_state.g_task1_scored = False
    if "g_task1_correct" not in st.session_state:
        st.session_state.g_task1_correct = False

    choice = st.radio(
        "Welches Beispiel beschreibt maschinelles Lernen am besten?",
        [
            "Ein Computer führt immer genau die gleichen festen Regeln aus",
            "Ein System erkennt in vielen Beispielen Muster und nutzt sie für neue Aufgaben",
            "Ein Programm wird jeden Tag von Hand neu geschrieben",
            "Ein Gerät funktioniert nur mit dem Internet"
        ],
        key="g_task1_choice"
    )

    if not st.session_state.g_task1_checked:
        if st.button("Antwort prüfen", key="g_task1_button"):
            st.session_state.g_task1_checked = True

            if choice == "Ein System erkennt in vielen Beispielen Muster und nutzt sie für neue Aufgaben":
                st.session_state.g_task1_correct = True
                if not st.session_state.g_task1_scored:
                    st.session_state.total_score += 1
                    st.session_state.total_answered += 1
                    st.session_state.g_task1_scored = True
            else:
                st.session_state.g_task1_correct = False
                if not st.session_state.g_task1_scored:
                    st.session_state.total_answered += 1
                    st.session_state.g_task1_scored = True

            st.rerun()

    else:
        if st.session_state.g_task1_correct:
            st.success("✅ Richtig! Genau das ist die Grundidee des maschinellen Lernens.")
        else:
            st.error("❌ Nicht ganz.")

        st.info("Maschinelles Lernen bedeutet, dass ein System aus Daten Muster erkennt und dieses Wissen später auf neue Beispiele anwendet.")

        if st.button("Nochmal versuchen", key="g_task1_retry"):
            st.session_state.g_task1_checked = False
            st.session_state.g_task1_correct = False
            st.rerun()


def show_grundlagen_aufgabe_3_1():
    st.markdown("### Wortvorhersage")
    st.write("Wie könnte der Satz sinnvoll weitergehen?")
    init_global_score()

    if "llm_checked" not in st.session_state:
        st.session_state.llm_checked = False
    if "llm_scored" not in st.session_state:
        st.session_state.llm_scored = False
    if "llm_correct" not in st.session_state:
        st.session_state.llm_correct = False

    choice = st.radio(
        "Wähle eine Antwort:",
        [
            "Im Winter ist es oft ... heiß",
            "Im Winter ist es oft ... kalt",
            "Im Winter ist es oft ... laut"
        ],
        key="llm_prediction"
    )

    if not st.session_state.llm_checked:
        if st.button("Antwort prüfen", key="llm_check"):
            st.session_state.llm_checked = True

            if "kalt" in choice:
                st.session_state.llm_correct = True
                if not st.session_state.llm_scored:
                    st.session_state.total_score += 1
                    st.session_state.total_answered += 1
                    st.session_state.llm_scored = True
            else:
                st.session_state.llm_correct = False
                if not st.session_state.llm_scored:
                    st.session_state.total_answered += 1
                    st.session_state.llm_scored = True

            st.rerun()

    else:
        if st.session_state.llm_correct:
            st.success("✅ Genau! Das ist hier das wahrscheinlichste Wort.")
        else:
            st.error("❌ Eher nicht. Überlege nochmal, welches Wort am besten passt.")

        st.info("So ähnlich funktioniert ein Sprachmodell: Es berechnet, welches Wort wahrscheinlich gut passt.")

        if st.button("Nochmal versuchen", key="llm_retry"):
            st.session_state.llm_checked = False
            st.session_state.llm_correct = False
            st.rerun()


def show_grundlagen_aufgabe_3_2():
    st.markdown("### Mini-Aufgabe")
    init_global_score()

    if "g_task2_checked" not in st.session_state:
        st.session_state.g_task2_checked = False
    if "g_task2_scored" not in st.session_state:
        st.session_state.g_task2_scored = False
    if "g_task2_correct" not in st.session_state:
        st.session_state.g_task2_correct = False

    choice = st.radio(
        "Was macht ein Sprachmodell wie ChatGPT hauptsächlich?",
        [
            "Es sucht nur fertige Sätze aus einem Buch heraus",
            "Es berechnet, welche Wörter oder Sätze wahrscheinlich gut zusammenpassen",
            "Es versteht Sprache genauso wie ein Mensch",
            "Es übersetzt jedes Wort einzeln ohne Zusammenhang"
        ],
        key="g_task2_choice"
    )

    if not st.session_state.g_task2_checked:
        if st.button("Antwort prüfen", key="g_task2_button"):
            st.session_state.g_task2_checked = True

            if choice == "Es berechnet, welche Wörter oder Sätze wahrscheinlich gut zusammenpassen":
                st.session_state.g_task2_correct = True
                if not st.session_state.g_task2_scored:
                    st.session_state.total_score += 1
                    st.session_state.total_answered += 1
                    st.session_state.g_task2_scored = True
            else:
                st.session_state.g_task2_correct = False
                if not st.session_state.g_task2_scored:
                    st.session_state.total_answered += 1
                    st.session_state.g_task2_scored = True

            st.rerun()

    else:
        if st.session_state.g_task2_correct:
            st.success("✅ Richtig! Sprachmodelle arbeiten vor allem mit Wahrscheinlichkeiten.")
        else:
            st.error("❌ Nicht ganz.")

        st.info("Sprachmodelle berechnen, welche Wörter oder Sätze sprachlich und inhaltlich wahrscheinlich gut passen.")

        if st.button("Nochmal versuchen", key="g_task2_retry"):
            st.session_state.g_task2_checked = False
            st.session_state.g_task2_correct = False
            st.rerun()


def show_grundlagen_aufgabe_3_3():
    st.markdown("### Mini-Aufgabe")
    init_global_score()

    if "g_task3_checked" not in st.session_state:
        st.session_state.g_task3_checked = False
    if "g_task3_scored" not in st.session_state:
        st.session_state.g_task3_scored = False
    if "g_task3_correct" not in st.session_state:
        st.session_state.g_task3_correct = False

    choice = st.radio(
        "Was beschreibt Deep Learning am besten?",
        [
            "Eine besondere Form des maschinellen Lernens mit vielen Verarbeitungsschichten",
            "Ein Computer liest besonders lange Texte",
            "Ein Programm arbeitet komplett ohne Daten",
            "Eine Methode, bei der Menschen jede Antwort direkt vorgeben"
        ],
        key="g_task3_choice"
    )

    if not st.session_state.g_task3_checked:
        if st.button("Antwort prüfen", key="g_task3_button"):
            st.session_state.g_task3_checked = True

            if choice == "Eine besondere Form des maschinellen Lernens mit vielen Verarbeitungsschichten":
                st.session_state.g_task3_correct = True
                if not st.session_state.g_task3_scored:
                    st.session_state.total_score += 1
                    st.session_state.total_answered += 1
                    st.session_state.g_task3_scored = True
            else:
                st.session_state.g_task3_correct = False
                if not st.session_state.g_task3_scored:
                    st.session_state.total_answered += 1
                    st.session_state.g_task3_scored = True

            st.rerun()

    else:
        if st.session_state.g_task3_correct:
            st.success("✅ Richtig! Deep Learning ist ein Teilbereich des maschinellen Lernens.")
        else:
            st.error("❌ Nicht ganz.")

        st.info("Deep Learning nutzt viele aufeinander aufbauende Verarbeitungsschichten, um komplexe Muster zu erkennen.")

        if st.button("Nochmal versuchen", key="g_task3_retry"):
            st.session_state.g_task3_checked = False
            st.session_state.g_task3_correct = False
            st.rerun()
        
def show_grundlagen_aufgabe_3_4():
    st.markdown("### Mini-Aufgabe")
    init_global_score()

    if "g_task_umwelt_checked" not in st.session_state:
        st.session_state.g_task_umwelt_checked = False
    if "g_task_umwelt_scored" not in st.session_state:
        st.session_state.g_task_umwelt_scored = False
    if "g_task_umwelt_correct" not in st.session_state:
        st.session_state.g_task_umwelt_correct = False

    choice = st.radio(
        "Wann ist der Einsatz von KI im Hinblick auf die Umwelt am sinnvollsten?",
        [
            "Wenn ich eine sehr einfache Information suche, zum Beispiel die Uhrzeit",
            "Wenn ich für eine komplexe Aufgabe eine ausführliche Erklärung oder Hilfe brauche",
            "Wenn ich statt einer Suchmaschine immer direkt KI benutze",
            "Wenn ich KI für jede kleine Alltagsfrage verwende"
        ],
        key="g_task_umwelt_choice"
    )

    if not st.session_state.g_task_umwelt_checked:
        if st.button("Antwort prüfen", key="g_task_umwelt_button"):
            st.session_state.g_task_umwelt_checked = True

            if choice == "Wenn ich für eine komplexe Aufgabe eine ausführliche Erklärung oder Hilfe brauche":
                st.session_state.g_task_umwelt_correct = True
                if not st.session_state.g_task_umwelt_scored:
                    st.session_state.total_score += 1
                    st.session_state.total_answered += 1
                    st.session_state.g_task_umwelt_scored = True
            else:
                st.session_state.g_task_umwelt_correct = False
                if not st.session_state.g_task_umwelt_scored:
                    st.session_state.total_answered += 1
                    st.session_state.g_task_umwelt_scored = True

            st.rerun()

    else:
        if st.session_state.g_task_umwelt_correct:
            st.success("✅ Richtig! KI sollte vor allem dann genutzt werden, wenn sie bei komplexeren Aufgaben wirklich hilfreich ist.")
        else:
            st.error("❌ Nicht ganz.")

        st.info("KI verbraucht für Berechnungen viel Energie und Wasser. Deshalb ist es sinnvoll, sie bewusst einzusetzen und für einfache Fragen eher andere Wege zu nutzen.")

        if st.button("Nochmal versuchen", key="g_task_umwelt_retry"):
            st.session_state.g_task_umwelt_checked = False
            st.session_state.g_task_umwelt_correct = False
            st.rerun()


def show_grundlagen_aufgabe_4():
    st.markdown("### KI im Alltag")
    init_global_score()

    if "g_task5_checked" not in st.session_state:
        st.session_state.g_task5_checked = False
    if "g_task5_scored" not in st.session_state:
        st.session_state.g_task5_scored = False
    if "g_task5_correct" not in st.session_state:
        st.session_state.g_task5_correct = False

    alltag_optionen = st.multiselect(
        "Welche Anwendungen nutzen häufig KI, um Daten auszuwerten und passende Ergebnisse vorzuschlagen?",
        [
            "Navigations-Apps",
            "Streaming-Plattformen",
            "Sprachassistenten",
            "Ein einfacher Lichtschalter",
            "Übersetzungsprogramme"
        ],
        key="alltag_multiselect"
    )

    richtige = {
        "Navigations-Apps",
        "Streaming-Plattformen",
        "Sprachassistenten",
        "Übersetzungsprogramme"
    }

    if not st.session_state.g_task5_checked:
        if st.button("Auswahl prüfen", key="alltag_check"):
            st.session_state.g_task5_checked = True

            if set(alltag_optionen) == richtige:
                st.session_state.g_task5_correct = True
                if not st.session_state.g_task5_scored:
                    st.session_state.total_score += 1
                    st.session_state.total_answered += 1
                    st.session_state.g_task5_scored = True
            else:
                st.session_state.g_task5_correct = False
                if not st.session_state.g_task5_scored:
                    st.session_state.total_answered += 1
                    st.session_state.g_task5_scored = True

            st.rerun()

    else:
        if st.session_state.g_task5_correct:
            st.success("✅ Genau! Diese Anwendungen nutzen häufig KI.")
        else:
            st.error("❌ Nicht ganz.")

        st.info("KI wird oft dort eingesetzt, wo viele Daten ausgewertet werden und daraus Vorschläge, Einordnungen oder Antworten entstehen.")

        if st.button("Nochmal versuchen", key="g_task5_retry"):
            st.session_state.g_task5_checked = False
            st.session_state.g_task5_correct = False
            st.rerun()


def show_quiz_grundlagen():
    st.subheader("Quiz: Grundlagen")
    init_global_score()

    if "grundlagen_quiz_done" not in st.session_state:
        st.session_state.grundlagen_quiz_done = False

    antworten = []

    for i, q in enumerate(QUESTIONS):
        st.write(f"**Frage {i + 1}: {q['question']}**")

        selected = st.radio(
            "Wähle eine Antwort:",
            q["options"],
            index=None,
            key=f"grundlagen_q_{i}"
        )
        antworten.append(selected)

    if st.button("Quiz auswerten", key="grundlagen_quiz_auswerten"):
        punktzahl = 0

        st.markdown("---")
        st.subheader("Ergebnisse")

        for i, q in enumerate(QUESTIONS):
            richtige_antwort = q["options"][q["answer_index"]]
            auswahl = antworten[i]

            if auswahl == richtige_antwort:
                punktzahl += 1
                st.success(f"Frage {i + 1}: Richtig ✅")
                st.write(q["explanation"])
            else:
                st.error(f"Frage {i + 1}: Falsch ❌")

                if i == 0:
                    hinweis = "Was ist KI?"
                elif i == 1 or i == 2:
                    hinweis = "Maschinelles Lernen"
                elif i == 3 or i == 4 or i == 6:
                    hinweis = "Sprachmodelle"
                elif i == 5:
                    hinweis = "Deep Learning"
                else:
                    hinweis = "KI im Alltag"

                st.info(
                    f"Richtige Antwort: {richtige_antwort}\n\n"
                    f'💡 Schau dir noch mal den Abschnitt „{hinweis}“ an.'
                )
                st.write(q["explanation"])

        if not st.session_state.grundlagen_quiz_done:
            st.session_state.total_score += punktzahl
            st.session_state.total_answered += len(QUESTIONS)
            st.session_state.grundlagen_quiz_done = True

        st.markdown("---")
        st.write(f"### Deine Punktzahl: {punktzahl} / {len(QUESTIONS)}")

        if punktzahl == len(QUESTIONS):
            st.balloons()
            st.success("Super! Du hast alle Fragen richtig beantwortet. 🎉")
        elif punktzahl >= 6:
            st.success("Gut gemacht! Du hast viele Fragen richtig beantwortet.")
        else:
            st.warning("💡 Schau dir das Kapitel nochmal an und versuche es erneut.")