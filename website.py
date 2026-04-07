import streamlit as st

from content.start import show_start
from content.grundlagen import show_grundlagen
from content.datenschutz import show_datenschutz
from content.falschinformationen import show_falschinformationen
from content.prompting import show_prompting
from quiz.quiz_utils import init_global_score

# Grundkonfiguration
st.set_page_config(
    page_title="Interaktive KI Lernumgebung",
    page_icon="🤖",
    layout="centered"
)

grundlagen_module = [
    "Was ist KI?",
    "Maschinelles Lernen",
    "Sprachmodelle",
    "Deep Learning",
    "Auswirkungen von KI auf die Umwelt",
    "KI im Alltag"
]

nutzung_ki_module = [
    "Einsatzmöglichkeiten von KI beim Lernen",
    "Richtiges Prompting für effiziente Nutzung"
]

falschinformationen_module = [
    "Falschinformationen bei der Nutzung der KI",
    "Deepfakes"
]


def init_module_progress():
    if "grundlagen_progress" not in st.session_state:
        st.session_state.grundlagen_progress = {
            modul: False for modul in grundlagen_module
        }

    if "selected_grundlagen_modul" not in st.session_state:
        st.session_state.selected_grundlagen_modul = grundlagen_module[0]

    if "nutzung_ki_progress" not in st.session_state:
        st.session_state.nutzung_ki_progress = {
            modul: False for modul in nutzung_ki_module
        }

    if "selected_nutzung_ki_modul" not in st.session_state:
        st.session_state.selected_nutzung_ki_modul = nutzung_ki_module[0]

    if "falschinformationen_progress" not in st.session_state:
        st.session_state.falschinformationen_progress = {
            modul: False for modul in falschinformationen_module
        }

    if "selected_falschinformationen_modul" not in st.session_state:
        st.session_state.selected_falschinformationen_modul = falschinformationen_module[0]

    if "datenschutz_abgeschlossen" not in st.session_state:
        st.session_state.datenschutz_abgeschlossen = False

    if "current_page" not in st.session_state:
        st.session_state.current_page = "Start"


def grundlagen_abgeschlossen():
    return all(st.session_state.grundlagen_progress.values())


def nutzung_ki_abgeschlossen():
    return all(st.session_state.nutzung_ki_progress.values())


def falschinformationen_abgeschlossen():
    return all(st.session_state.falschinformationen_progress.values())


def datenschutz_abgeschlossen():
    return st.session_state.datenschutz_abgeschlossen


def main():
    init_global_score()
    init_module_progress()

    with st.sidebar:
        st.title("Menü")
        st.write("Wähle ein Modul:")

        if st.button("Start", use_container_width=True):
            st.session_state.current_page = "Start"

        if st.button("Grundlagen", use_container_width=True):
            st.session_state.current_page = "Grundlagen"

        if st.button("Datenschutz", use_container_width=True):
            st.session_state.current_page = "Datenschutz"

        if st.button("Falschinformationen", use_container_width=True):
            st.session_state.current_page = "Falschinformationen"

        if st.button("Richtige Nutzung der KI", use_container_width=True):
            st.session_state.current_page = "Nutzung KI"

     

        if st.session_state.current_page == "Grundlagen":
            st.markdown("### Unterthemen")

            grundlagen_optionen = []
            for modul_name in grundlagen_module:
                label = modul_name
                if st.session_state.grundlagen_progress[modul_name]:
                    label += " ✓"
                grundlagen_optionen.append(label)

            selected_label = st.radio(
                "Grundlagen-Module",
                grundlagen_optionen,
                index=grundlagen_module.index(st.session_state.selected_grundlagen_modul)
            )

            st.session_state.selected_grundlagen_modul = selected_label.replace(" ✓", "")

        elif st.session_state.current_page == "Falschinformationen":
            st.markdown("### Unterthemen")

            falschinformationen_optionen = []
            for modul_name in falschinformationen_module:
                label = modul_name
                if st.session_state.falschinformationen_progress[modul_name]:
                    label += " ✓"
                falschinformationen_optionen.append(label)

            selected_label = st.radio(
                "Falschinformationen-Module",
                falschinformationen_optionen,
                index=falschinformationen_module.index(
                    st.session_state.selected_falschinformationen_modul
                )
            )

            st.session_state.selected_falschinformationen_modul = selected_label.replace(" ✓", "")

        elif st.session_state.current_page == "Nutzung KI":
            st.markdown("### Unterthemen")

            nutzung_ki_optionen = []
            for modul_name in nutzung_ki_module:
                label = modul_name
                if st.session_state.nutzung_ki_progress[modul_name]:
                    label += " ✓"
                nutzung_ki_optionen.append(label)

            selected_label = st.radio(
                "Nutzung-der-KI-Module",
                nutzung_ki_optionen,
                index=nutzung_ki_module.index(
                    st.session_state.selected_nutzung_ki_modul
                )
            )

            st.session_state.selected_nutzung_ki_modul = selected_label.replace(" ✓", "")

       
        st.subheader("⭐ Dein Punktestand")
        st.write(f"Gesamtpunkte: {st.session_state.total_score}")
        st.write(f"Beantwortete Fragen: {st.session_state.total_answered}")

        if st.button("🔄 Alles zurücksetzen", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    page = st.session_state.current_page

    if page == "Start":
        show_start()

    elif page == "Grundlagen":
        show_grundlagen(st.session_state.selected_grundlagen_modul)

    elif page == "Datenschutz":
        show_datenschutz()

    elif page == "Falschinformationen":
        show_falschinformationen(st.session_state.selected_falschinformationen_modul)

    elif page == "Nutzung KI":
        show_prompting(st.session_state.selected_nutzung_ki_modul)


if __name__ == "__main__":
    main()
