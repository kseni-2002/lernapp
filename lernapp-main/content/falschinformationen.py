import streamlit as st

from quiz.quiz_falschinformationen import (
    show_quiz_falschinformationen,
    show_deepfake_uebungen,
)


def mark_modul_done(modulname: str, key_name: str):
    if key_name in st.session_state:
        st.session_state[key_name][modulname] = True


def show_falschinformationen(selected_modul):
    st.header("Falschinformationen bei der Nutzung von KI")

    if selected_modul == "Falschinformationen bei der Nutzung der KI":
        st.write("""
Beim Nutzen von KI-Tools ist es wichtig zu wissen, dass nicht jede Antwort automatisch richtig ist.
KI kann sehr überzeugend klingen, obwohl Informationen ungenau, unvollständig oder sogar falsch sein können.
Deshalb solltest du Antworten von KI immer kritisch prüfen.
""")

        st.subheader("Warum können KI-Tools falsche Informationen geben?")

        st.write("""
Wenn du einer KI eine Frage stellst, führt sie verschiedene Informationen zusammen
und gibt sie in neuer Form aus.

Die Antworten basieren auf Mustern aus großen Mengen an Trainingsdaten.
Dabei überprüft die KI nicht automatisch, ob eine Aussage tatsächlich richtig ist.
Sie greift auf viele unterschiedliche Quellen zurück, unter anderem aus dem Internet.

Das Problem dabei ist, dass Informationen im Internet – besonders auf Social Media –
häufig nicht überprüft sind. Dadurch können dort falsche Inhalte oder subjektive Meinungen enthalten sein.

Die KI kann solche Inhalte übernehmen, ohne zwischen guten und schlechten Quellen zu unterscheiden.

Dadurch kann es passieren, dass Informationen:
- erfunden werden  
- miteinander vermischt werden  
- falsch dargestellt werden  
""")

        st.info("""
💡 Wichtig:
KI klingt oft sehr überzeugend – auch wenn die Antwort falsch ist.
""")

        st.subheader("Woran erkennst du mögliche Falschinformationen?")

        st.write("""
Achte auf diese Warnzeichen:
- Es werden keine Quellen genannt  
- Aussagen sind sehr allgemein oder ungenau  
- Fakten, Daten oder Namen widersprechen sich  
- Die Antwort klingt sehr sicher, obwohl das Thema schwierig ist  
- Beispiele passen nicht richtig zur Frage  
""")

        st.subheader("So gehst du richtig mit KI-Antworten um")

        st.write("""
Um Falschinformationen zu vermeiden, solltest du KI-Antworten nie einfach übernehmen.
""")

        st.write("""
- Frag die KI nach Quellen  
- Prüfe die Quelle: Ist sie seriös? Wer hat sie veröffentlicht?  
- Vergleiche die KI-Antwort mit der ursprünglichen Quelle  
- Nutze andere Quellen, z. B. Schulbücher oder Lehrkräfte  
- Überlege, ob es um Fakten oder Meinungen geht  
- Frag nach Hilfe, wenn du unsicher bist  
""")

        st.info("""
✅ Merke:
KI kann beim Lernen helfen, aber sie ersetzt keine kritische Prüfung von Informationen.
""")

        st.header("Quiz")
        show_quiz_falschinformationen()

        st.markdown("---")
        if st.button("✅ Untermodul abschließen", key="finish_falschinfo"):
            mark_modul_done(
                "Falschinformationen bei der Nutzung der KI",
                "falschinformationen_progress"
            )
            st.success("Untermodul abgeschlossen!")
            st.rerun()

    elif selected_modul == "Deepfakes":
        st.write("""
Ein besonderes Problem im Zusammenhang mit Falschinformationen sind sogenannte Deepfakes.
Dabei handelt es sich um mithilfe von KI erstellte oder veränderte Bilder, Videos oder Audios,
die echt wirken, obwohl sie manipuliert sind.
""")

        st.write("""
Zum Beispiel können Personen Dinge sagen oder tun, die sie in Wirklichkeit nie gesagt oder gemacht haben.
Deepfakes sind oft schwer zu erkennen und können gezielt eingesetzt werden,
um Menschen zu täuschen oder falsche Informationen zu verbreiten.
""")

        st.info("""
💡 Deshalb ist es wichtig, auch bei Bildern und Videos kritisch zu bleiben
und ihre Herkunft zu überprüfen.
""")

        st.write("Übung: Deepfakes")
        show_deepfake_uebungen()

        st.markdown("---")
        if st.button("✅ Untermodul abschließen", key="finish_deepfakes"):
            mark_modul_done(
                "Deepfakes",
                "falschinformationen_progress"
            )
            st.success("Untermodul abgeschlossen!")
            st.rerun()