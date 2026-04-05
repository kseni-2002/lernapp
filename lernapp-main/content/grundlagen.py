import streamlit as st
from quiz.quiz_grundlagen import (
    show_grundlagen_aufgabe_1,
    show_grundlagen_aufgabe_2_1,
    show_grundlagen_aufgabe_2_2,
    show_grundlagen_aufgabe_3_1,
    show_grundlagen_aufgabe_3_2,
    show_grundlagen_aufgabe_3_3,
    show_grundlagen_aufgabe_3_4,
    show_grundlagen_aufgabe_4,
    show_quiz_grundlagen,
)


def mark_modul_done(modulname: str):
    if "grundlagen_progress" in st.session_state:
        st.session_state.grundlagen_progress[modulname] = True


def show_abschliessen_button(modulname: str, button_key: str):
    st.markdown("---")
    if st.button("✅ Untermodul abschließen", key=button_key):
        mark_modul_done(modulname)
        st.success(f"'{modulname}' wurde als abgeschlossen markiert.")
        st.rerun()


def show_was_ist_ki():
    st.subheader("Was ist überhaupt KI?")

    st.write("""In diesem Modul lernst du um was es sich handelt, wenn von **KI** gesprochen wird.""")

    st.write("""
Künstliche Intelligenz ist der Oberbegriff für Systeme,
die Aufgaben lösen können, für die üblicherweise menschliches Denken nötig ist.
""")

    st.write("""
KI kann zum Beispiel:
- Sprache verstehen
- Texte aus verschiedenen Sprachen übersetzen
- Texte schreiben
- Bilder erkennen
- Bilder erstellen
""")

    st.write("""
Es gibt nicht **DIE EINE** Definition von KI.
Im Grunde ist es eine Art Sammelbegriff für Technologien, durch die Maschinen Informationen verarbeiten
und Probleme lösen können. Hier sollst du eine Idee dafür bekommen, wie das funktionieren kann.
""")

    st.info("""
💡 Wichtig:
KI ist nicht „magisch“ und auch nicht allwissend.
Sie arbeitet mit einer großen Anzahl an Daten, erkennt Muster und berechnet Wahrscheinlichkeiten.
""")

    st.write("""
Viele heutige KI-Systeme sind für bestimmte Aufgaben erstellt.
Eine KI, die Bilder erkennt, kann zum Beispiel nicht automatisch auch gute Texte schreiben.
""")

    show_grundlagen_aufgabe_1()
    show_abschliessen_button("Was ist KI?", "finish_was_ist_ki")


def show_maschinelles_lernen():
    st.header("Maschinelles Lernen")

    st.write("""
Ein sehr wichtiger Teilbereich von KI ist das **Maschinelle Lernen**.
Das bedeutet, dass KI-Systeme aus ganz vielen Daten lernen anstelle von festgelegten Regeln.

""")

    st.write("""
KI-Systeme bekommen im sogenannten **Training** ganz viele Beispiele.
Das Ziel ist, aus diesen Beispielen Muster zu erkennen.
Wenn die Systeme diese Muster erkennen können, dann können sie daraus Vorhersagen treffen.
Dadurch kann das System später neue Aufgaben lösen.
Je mehr Beispiele die KI bekommen hat, desto genauer können zukünftige Vorhersagen getroffen werden.
""")

    st.subheader("Beispiel: Bilderkennung")
    st.write("""
Die KI soll erkennen, ob auf einem Bild ein Hund 🐶 oder eine Katze 🐱 zu sehen ist.
Ohne Maschinelles Lernen wäre das nicht möglich.
Beim Maschinellen Lernen bekommt die KI ganz viele Beispiele von Bildern mit Hunden und es wird ihr gesagt, dass es sich um einen Hund handelt.
Genau das gleiche auch mit Katzen. 
Diese Beispiele bezeichnet man als **Trainingsdaten**. 
Die KI kann dann Muster erkennen, wie typische Ohrenformen, Größenverhältnisse oder Gesichtsformen.
""")

    
    st.info("""💡 Wichtig:
Die KI versteht nicht wirklich was ein Hund oder eine Katze ist. **ABER** sie erkennt Muster, die typisch für Hunde oder Katzen sind. Dadurch kann Sie Vorhersagen treffen.""")

    st.subheader("Beispiel: Mustererkennung")
    st.write("""Die KI erkennt also Muster in den Trainingsdaten, also sich wiederholende Strukturen. Das funktioniert zum Beispiel bei Texten und Bildern.""")

   


    show_grundlagen_aufgabe_2_1()
    show_grundlagen_aufgabe_2_2()
    show_abschliessen_button("Maschinelles Lernen", "finish_ml")


def show_sprachmodelle():
    st.subheader("Sprachmodelle")

    st.write("""
Einige KI-Systeme beschäftigen sich mit der Verarbeitung von Sprache.
Dazu gehören zum Beispiel Chatbots wie Chatgpt.
""")

    st.write("""
Sie wurden mit sehr vielen verschiedenen Texten trainiert wie zum Beispiel mit Büchern und Websiten.
Dabei lernen sie, wie Sprache aufgebaut ist und welche Wörter oft aufeinander folgen.
Das heißt, sie erkennen Muster in der Sprache.
Diese KI-Systeme können zum Beispiel Texte schreiben, Texte übersetzen, Texte zusammenfassen, Fragen beantworten und Gespräche führen.
""")

    st.success("""
Wenn du einem Chatbot eine Frage stellst, berechnet er,
welche Antwort gut passen würde. KI versteht also nicht sonden sagt vorher, welche Antwort passt.
""")

    show_grundlagen_aufgabe_3_1()
    show_grundlagen_aufgabe_3_2()
   
        

    st.info("""
💡 Chatbots können sehr überzeugend klingen.
Sie sind aber nicht allwissend! Mehr dazu lernst du in den nächsten Modulen!
""")

    show_abschliessen_button("Sprachmodelle", "finish_llm")


def show_deep_learning():
    st.subheader("Deep Learning")

    st.write("""
**Deep Learning** ist ein Teilbereich des Maschinellen Lernens.
Die KI-Systeme, die auf Deep Learning basieren, bestehen aus ganz vielen verschiedenen Schichten.
""")

    st.write("""
Informationen werden in jeder Schicht verarbeitet,
wodurch auch sehr komplexe Muster erkannt werden können.
""")

    st.write("""
Bei der Bilderkennung kann das zum Beispiel so aussehen:
- eine Schicht erkennt Linien,
- eine weitere Schicht erkennt Formen,
- spätere Schichten erkennen ganze Objekte.
""")

    st.write("""
Deep Learning ist besonders wichtig für moderne Anwendungen wie:
- Sprachassistenten
- Bilderkennung
- automatische Übersetzungen
- Chatbots
""")

    st.warning("""
⚠️ Deep Learning klingt kompliziert, aber die Grundidee ist:
Die KI verarbeitet Informationen in vielen aufeinander aufbauenden Schritten.
""")

    show_grundlagen_aufgabe_3_3()

 

    show_abschliessen_button("Deep Learning", "finish_dl")


def show_ki_umwelt():
    st.subheader("Auswirkungen von KI auf die Umwelt")

    st.info("""KI-Systeme benötigen sehr große Rechenzentren. Diese benötigen viel Wasser, um die Server zu kühlen, damit sie nicht überhiten. """)

    st.write("""Im Vergleich zu einer Google Suche wird zum Beispiel weniger Strom und Wasser verbraucht. Das liegt daran, dass bei einer Suchmaschine bestehende Inhalte durchsucht werden. Eine KI generiert komplett neue Ausgaben. 
             Dafür werden wie du in den vorherigen Modulen gelernt hast, viele Berechnungen durchgeführt. Damit steigt der Rechenaufwand. Bei höherem Rechenaufwand brauchen die Rechenzentren Strom und Wasser zur Kühlung!.""")
    st.warning(""" KI ist sehr praktisch und kann uns bei vielen Aufgaben unterstützen. **Aber** die Nutzung führt auch zu einer Belastung der Umwelt. 
               Nutze KI also nicht unnötig und überlege dir, ob du für deine Frage wirklich KI brauchst!""")

    st.write("""Es ist also wichtig zu wissen, dass auch simple Gespräche mit Chatgpt Ressourcen verbrauchen. Je mehr Menschen KI für Fragen oder Gespräche nutzen, für die keine KI benötigt wird, desto mehr Strom und Wasser werden verbraucht. Das kann zu einer Belastung der Umwelt führen. 
             Diesen Verbrauch kannst du reduzieren, indem du bewusst mit KI umgehst.
             Das heißt nicht, dass du KI nicht benutzen solltest, sondern dass du dir vorher gut überlegst, ob du für deine Frage wirklich KI brauchst oder ob du die Antwort auch über einen anderen Weg herausfinden kannst.""")

    show_grundlagen_aufgabe_3_4()

    show_abschliessen_button("Auswirkungen von KI auf die Umwelt", "finish_umwelt")

def show_ki_im_alltag():
    st.write("""
KI begegnet uns heute ganz oft im Alltag. Manchmal ohne dass wir merken, dass KI dahintersteckt!
""")

    st.write("""
Zum Beispiel in:
- Suchmaschinen
- Sozialen Medien
- Navigations-Apps
- Streaming-Plattformen
- Übersetzungsprogrammen
- Sprachassistenten
- Lernhilfen und Chatbots
""")

    st.write("""
Wenn dir auf TikTok, YouTube oder Netflix Inhalte vorgeschlagen werden,
steckt oft KI dahinter. Sie analysiert, was du vorher einmal angeklickt hast und macht
dir darauf basierend Vorschläge. 
""")

    show_grundlagen_aufgabe_4()

    st.write("""
Gerade weil KI im Alltag so verbreitet ist,
ist es wichtig zu verstehen, wie sie funktioniert.
""")

   
    



    show_quiz_grundlagen()
    show_abschliessen_button("KI im Alltag", "finish_alltag")

    


def show_grundlagen(selected_modul):
    st.header("Grundlagen der Künstlichen Intelligenz")

    if selected_modul == "Was ist KI?":
        show_was_ist_ki()

    elif selected_modul == "Maschinelles Lernen":
        show_maschinelles_lernen()

    elif selected_modul == "Sprachmodelle":
        show_sprachmodelle()

    elif selected_modul == "Deep Learning":
        show_deep_learning()

    elif selected_modul == "Auswirkungen von KI auf die Umwelt":
        show_ki_umwelt()

    elif selected_modul == "KI im Alltag":
        show_ki_im_alltag()



    else:
        st.info("Bitte wähle links ein Untermodul aus.")