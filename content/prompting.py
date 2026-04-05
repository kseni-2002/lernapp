import streamlit as st
from quiz.quiz_nutzung import show_quiz_nutzung
from quiz.quiz_prompting import show_quiz_prompting


def mark_modul_done(modulname: str, key_name: str):
    if key_name in st.session_state:
        st.session_state[key_name][modulname] = True


def show_prompting(selected_modul):
    if selected_modul == "Einsatzmöglichkeiten von KI beim Lernen":
        st.header("Einsatzmöglichkeiten von KI beim Lernen")
        st.write("""
KI kann dich beim Lernen auf viele verschiedene Arten unterstützen.
Wichtig ist aber, dass du sie **richtig nutzt**!
""")

        st.subheader("✅ So nutzt du KI richtig")

        st.write("""
KI kann dein Lernen **individueller und effektiver** gestalten, wenn du sie wie einen persönlichen Lerncoach nutzt.

Du kannst KI zum Beispiel verwenden, um:
- dein Lernverhalten besser zu verstehen und passende Übungen zu bekommen  
- dir schwierige Themen einfach erklären zu lassen  
- Unterstützung beim Schreiben von Texten zu erhalten  
- Feedback zu Aufgaben oder Texten zu bekommen  
- Sprachen zu lernen oder zu üben  
- Hilfe beim Programmieren oder kreativen Arbeiten zu bekommen  
""")

        st.write("""
Viele KI-Tools funktionieren wie ein persönlicher Tutor:
Du kannst jederzeit Fragen stellen, Inhalte erklären lassen und so lange nachfragen, bis du es verstanden hast.

Außerdem kann KI:
- deinen aktuellen Wissensstand einschätzen  
- dir zeigen, wo du noch üben solltest  
- dir einen Lernplan erstellen  
""")

        st.info("""
💡 Wichtig:
KI ist am hilfreichsten, wenn du sie als Unterstützung nutzt – nicht als Ersatz für dein eigenes Denken.
""")

        st.subheader("⚠️ Häufige Fehler")

        st.write("""
- Antworten einfach übernehmen  
- zu ungenaue Fragen stellen  
- KI als Ersatz für eigenes Denken nutzen  
""")

        st.header("Quiz: Nutzung von KI beim Lernen")
        show_quiz_nutzung()

        st.markdown("---")
        if st.button("✅ Untermodul abschließen", key="finish_nutzung_ki"):
            mark_modul_done(
                "Einsatzmöglichkeiten von KI beim Lernen",
                "nutzung_ki_progress"
            )
            st.success("Untermodul abgeschlossen!")
            st.rerun()

    elif selected_modul == "Richtiges Prompting für effiziente Nutzung":
        st.header("Richtiges Prompting für effiziente Nutzung")

        st.write("""
Gutes Prompting ist eine wichtige Fähigkeit.
Damit kannst du deinen Lernprozess aktiv steuern und KI sinnvoll nutzen.
""")

        st.subheader("Was ist Prompting?")

        st.write("""
Ein **Prompt** ist die Eingabe, die du an eine KI stellst.

Je besser dein Prompt ist, desto besser ist auch die Antwort.
""")

        st.header("Übung: richtiges Prompting")
        show_quiz_prompting()

        st.markdown("---")
        if st.button("✅ Untermodul abschließen", key="finish_prompting"):
            mark_modul_done(
                "Richtiges Prompting für effiziente Nutzung",
                "nutzung_ki_progress"
            )
            st.success("Untermodul abgeschlossen!")
            st.rerun()