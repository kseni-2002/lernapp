import streamlit as st

QUESTIONS = [
    {
        "question": "Warum können KI-Antworten manchmal falsch sein?",
        "options": [
            "Weil KI aus Marketinggründen absichtlich falsche Antworten gibt",
            "Weil KI Informationen aus vielen Quellen kombiniert und nicht automatisch überprüft",
            "Weil KI nur mit alten Büchern arbeitet"
        ],
        "answer_index": 1,
        "explanation": "KI kombiniert Informationen aus vielen Quellen und überprüft nicht automatisch, ob alles stimmt."
    },
    {
        "question": "Woran erkennst du mögliche Falschinformationen?",
        "options": [
            "Die Antwort ist sehr lang",
            "Die Antwort ist sehr kurz",
            "Die Antwort enthält viele Emojis",
            "Es können keine Quellen genannt werden"
        ],
        "answer_index": 3,
        "explanation": "Fehlende Quellen und unklare Aussagen sind typische Warnzeichen für Falschinformationen."
    },
    {
        "question": "Wie solltest du mit KI-Antworten umgehen?",
        "options": [
            "Übernehmen, wenn sie sich vernünftig anhört",
            "Nur glauben, wenn sie lang ist",
            "Mit anderen Quellen überprüfen"
        ],
        "answer_index": 2,
        "explanation": "Du solltest Informationen immer überprüfen und mit anderen Quellen vergleichen."
    }
]


def show_quiz_falschinformationen():
    if "total_score" not in st.session_state:
        st.session_state.total_score = 0
    if "total_answered" not in st.session_state:
        st.session_state.total_answered = 0

    if "falschinfo_quiz_done" not in st.session_state:
        st.session_state.falschinfo_quiz_done = False
    if "falschinfo_quiz_show_results" not in st.session_state:
        st.session_state.falschinfo_quiz_show_results = False
    if "falschinfo_quiz_score" not in st.session_state:
        st.session_state.falschinfo_quiz_score = 0
    if "falschinfo_quiz_feedback" not in st.session_state:
        st.session_state.falschinfo_quiz_feedback = []

    antworten = []

    for i, q in enumerate(QUESTIONS):
        st.write(f"**Frage {i + 1}: {q['question']}**")

        selected = st.radio(
            "Wähle eine Antwort:",
            q["options"],
            index=None,
            key=f"falschinfo_q_{i}"
        )
        antworten.append(selected)

    if st.button("Quiz auswerten", key="falschinfo_quiz_auswerten"):
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
                    hinweis = "Warum können KI-Tools falsche Informationen geben?"
                elif i == 1:
                    hinweis = "Woran erkennst du mögliche Falschinformationen?"
                else:
                    hinweis = "So gehst du richtig mit KI-Antworten um"

                feedback.append({
                    "status": "wrong",
                    "frage": i + 1,
                    "richtige_antwort": richtige_antwort,
                    "hinweis": hinweis,
                    "explanation": q["explanation"]
                })

        st.session_state.falschinfo_quiz_score = punktzahl
        st.session_state.falschinfo_quiz_feedback = feedback
        st.session_state.falschinfo_quiz_show_results = True

        if not st.session_state.falschinfo_quiz_done:
            st.session_state.total_score += punktzahl
            st.session_state.total_answered += len(QUESTIONS)
            st.session_state.falschinfo_quiz_done = True

        st.rerun()

    if st.session_state.falschinfo_quiz_show_results:
        st.markdown("---")
        st.subheader("Ergebnisse")

        for item in st.session_state.falschinfo_quiz_feedback:
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
        st.write(f"### Deine Punktzahl: {st.session_state.falschinfo_quiz_score} / {len(QUESTIONS)}")

        if st.session_state.falschinfo_quiz_score == len(QUESTIONS):
            st.balloons()
            st.success("Super! Du hast alle Fragen richtig beantwortet. 🎉")
        elif st.session_state.falschinfo_quiz_score >= 2:
            st.success("Gut gemacht! Du hast die meisten Fragen richtig beantwortet.")
        else:
            st.warning("💡Schau dir das Kapitel nochmal an und versuche es erneut.")


def show_deepfake_uebungen():
    if "total_score" not in st.session_state:
        st.session_state.total_score = 0
    if "total_answered" not in st.session_state:
        st.session_state.total_answered = 0

    if "df1_scored" not in st.session_state:
        st.session_state.df1_scored = False
    if "df1_feedback_shown" not in st.session_state:
        st.session_state.df1_feedback_shown = False
    if "df1_points" not in st.session_state:
        st.session_state.df1_points = 0

    if "df3_scored" not in st.session_state:
        st.session_state.df3_scored = False
    if "df3_feedback_shown" not in st.session_state:
        st.session_state.df3_feedback_shown = False
    if "df3_points" not in st.session_state:
        st.session_state.df3_points = 0

    # -------------------------
    # Deepfake-Übung 1
    # -------------------------
    st.subheader("Übung 1")

    st.write("""
Unten siehst du 6 Bilder. 3 davon sind echt und 3 sind KI-generiert.
Kannst du erkennen, welche Bilder fake sind?
""")

    st.image("quiz/images/Download.png", use_container_width=True)

    antwort = st.multiselect(
        "Welche 3 Bilder sind KI-generiert?",
        [
            "1. Bild",
            "2. Bild",
            "3. Bild",
            "4. Bild",
            "5. Bild",
            "6. Bild"
        ],
        key="deepfake_aufgabe_1"
    )

    if st.button("Antwort überprüfen", key="check_deepfake_1"):
        richtige_antworten = {"2. Bild", "3. Bild", "5. Bild"}

        if len(antwort) != 3:
            st.warning("Bitte wähle genau 3 Bilder aus.")
        else:
            richtige_getroffen = set(antwort) & richtige_antworten
            punkte = len(richtige_getroffen)

            if not st.session_state.df1_scored:
                st.session_state.total_score += punkte
                st.session_state.total_answered += 3
                st.session_state.df1_scored = True

            st.session_state.df1_points = punkte
            st.session_state.df1_feedback_shown = True
            st.rerun()

    if st.session_state.df1_feedback_shown:
        if st.session_state.df1_points == 3:
            st.success("✅ Perfekt! Alle drei Bilder richtig erkannt.")
        elif st.session_state.df1_points > 0:
            st.warning(f"Teilweise richtig 👍 Du hast {st.session_state.df1_points} von 3 KI-Bildern richtig erkannt.")
        else:
            st.error("❌ Leider kein KI-Bild richtig erkannt.")

        st.info("""
KI-generierte Bilder sind: **2. Bild, 3. Bild, 5. Bild**

Es war schwierig, zu erkennen, welche echt sind, oder?

In diesem Beispiel sind es harmlose Bilder, die niemandem schaden.
Mit dieser Übung wollten wir dir allerdings zeigen, wie realistisch Deepfakes mittlerweile aussehen können.
Oft sind sie auf den ersten Blick kaum von echten Bildern zu unterscheiden.
""")

        st.write("""
**Quellen:**  
1. Bild: https://www.br.de/ (BBC NHU/BR/NDR/Paul Williams 2017)  
2. Bild: https://cdn.pixabay.com/ (Nutzer: geralt)  
3. Bild: https://cdn.pixabay.com/ (Nutzer: geralt)  
4. Bild: https://www.tierwelt-live.de/  
5. Bild: https://pixabay.com/ (Nutzer: SimonN90)  
6. Bild: https://www.tierwelt-live.de/  
""")

    st.markdown("---")

    # -------------------------
    # Deepfake-Übung 2
    # -------------------------
    st.subheader("Übung 2")

    st.write("""
Schau dir das Bild genau an.

Das Bild ist **KI-generiert**. Überlege kurz, woran du erkennen könntest,
dass es nicht echt ist, und schreibe deine Beobachtungen auf.
""")

    st.image(
        "quiz/images/papst_designermantel_Balenciaga_ai_ki_fake.webp",
        width=300
    )

    beobachtung = st.text_area(
        "Woran könnte man erkennen, dass das Bild nicht echt ist?",
        height=150,
        key="deepfake_aufgabe_2_text"
    )

    if st.button("Auflösung anzeigen", key="check_deepfake_2"):
        if not beobachtung.strip():
            st.warning("Schreibe zuerst kurz deine Beobachtungen auf.")
        else:
            st.info("""
Das Bild von Papst Franziskus ist KI-generiert.

Ein möglicher Hinweis ist die rechte **Hand**, die unnatürlich wirkt.
Gerade Hände und Finger sind bei KI-Bildern oft fehlerhaft dargestellt.

Außerdem hilft hier auch **logisches Nachdenken**:
Es ist eher unrealistisch, den Papst in so einer auffälligen Designerjacke zu sehen.
Deshalb sollte man nicht sofort glauben, dass das Bild echt ist, sondern zuerst prüfen,
ob vertrauenswürdige Quellen darüber berichten.

Dieses Beispiel zeigt, dass auch von politisch und gesellschaftlich sehr wichtigen Personen
Deepfakes erstellt werden können. Das kann potenziell gefährlich sein, weil solche Bilder
Menschen täuschen und Falschinformationen verbreiten können.

Quelle Bild: https://x.com/
""")

    st.markdown("---")

    # -------------------------
    # Deepfake-Übung 3
    # -------------------------
    st.subheader("Übung 3")

    st.write("""
Unten siehst du zwei Bilder von brennenden Gebäuden.

Eines der Bilder ist **KI-generiert**, das andere ist echt.
Welches Bild sieht für dich fake aus?
""")

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "quiz/images/botschaft_fake.jpg",
            caption="Bild 1",
            use_container_width=True
        )

    with col2:
        st.image(
            "quiz/images/haus_brand_echt.jpg",
            caption="Bild 2",
            use_container_width=True
        )

    antwort_3 = st.radio(
        "Welches Bild ist KI-generiert?",
        ["Bild 1", "Bild 2"],
        index=None,
        key="deepfake_aufgabe_3"
    )

    if st.button("Antwort überprüfen", key="check_deepfake_3"):
        if antwort_3 is None:
            st.warning("Bitte wähle ein Bild aus.")
        else:
            punkte = 1 if antwort_3 == "Bild 1" else 0

            if not st.session_state.df3_scored:
                st.session_state.total_score += punkte
                st.session_state.total_answered += 1
                st.session_state.df3_scored = True

            st.session_state.df3_points = punkte
            st.session_state.df3_feedback_shown = True
            st.rerun()

    if st.session_state.df3_feedback_shown:
        if st.session_state.df3_points == 1:
            st.success("Richtig! ✅")
        else:
            st.error("Nicht ganz richtig ❌")

        st.info("""
Das **erste Bild ist KI-generiert**. Es wurde als angebliches Bild einer brennenden
US-Botschaft in Saudi-Arabien verbreitet, war aber nicht echt.

Gerade solche Bilder sind politisch besonders relevant und gefährlich.
Wenn Menschen glauben, dass ein solches Ereignis wirklich passiert ist,
kann das Angst, Wut oder politische Spannungen auslösen.

Dieses Beispiel zeigt, dass Deepfakes nicht nur zur Unterhaltung erstellt werden,
sondern auch genutzt werden können, um Falschinformationen zu verbreiten
und Meinungen gezielt zu beeinflussen.

Deshalb ist es wichtig, Bilder immer kritisch zu hinterfragen und zu prüfen,
ob vertrauenswürdige Quellen darüber berichten.

**Das zweite Bild ist echt** und wurde vom MDR veröffentlicht, der als seriöse
und vertrauenswürdige Quelle eingestuft werden kann.

**Quellen:**  
Bild 1: https://faktencheck.afp.com/  
Bild 2: https://www.mdr.de/
""")

    st.markdown("---")

    # -------------------------
    # Deepfake-Übung 4
    # -------------------------
    st.subheader("Übung 4")

    st.write("""
Schau dir das Bild genau an.

Das Bild ist **KI-generiert**. Überlege kurz, woran du erkennen könntest,
dass es nicht echt ist, und schreibe deine Beobachtungen auf.
""")

    st.image(
        "quiz/images/staatschefs.jpg",
        width=400
    )

    beobachtung_4 = st.text_area(
        "Woran könnte man erkennen, dass das Bild nicht echt ist?",
        height=150,
        key="deepfake_aufgabe_4_text"
    )

    if st.button("Auflösung anzeigen", key="check_deepfake_4"):
        if not beobachtung_4.strip():
            st.warning("Schreibe zuerst kurz deine Beobachtungen auf.")
        else:
            st.info("""
Dieses Bild ist KI-generiert.

Es soll angeblich ein Treffen zeigen, bei dem europäische Staats- und Regierungschefs
vor dem Oval Office warten, während Gespräche zum Ukrainekrieg stattfinden.
Ein Vergleich mit echten Aufnahmen zeigt jedoch, dass die Szene so nicht stattgefunden hat.

Bei genauer Betrachtung fallen mehrere Fehler auf:
Es sind mehrere **Beine und Schuhe** sichtbar, die keiner Person gehören.
Das **Teppichmuster** wirkt unlogisch und unregelmäßig.

Außerdem wirkt die gesamte Szene **unnatürlich gleichmäßig und gestellt**.

Das Bild wurde in einem X-Beitrag veröffentlicht und wurde unter Anderem auf Facebook, Telegram und auf dem staatlich unterstützten russischen Medium "Pravda" verbreitet. Vertrauenswürdige Quellen zeigen jedoch, dass es unecht ist.

Quelle Informationen: AFP-Faktencheck  (https://faktencheck.afp.com/doc.afp.com.69XG2NQ)

Quelle Bild: https://x.com/
""")