<h1>Wiki LLM Dashboard</h1>

<h2>Kontext des Projektes (Fachpraktikum Sprachtechnologie): </h2>

<h3>Einführung </h3>

Das Projekt “LLM-Dashboard” wird im Rahmen des Fachpraktikums Sprachtechnologie an der Fernuniversität Hagen durchgeführt. Dabei ist das Ziel des Praktikums, dass Studierende praktische Erfahrung in der Anwendung und Entwicklung von Technologien im Bereich der Sprachverarbeitung zu ermöglichen. 

<h3>Projektauftrag:</h3>

Das Ziel dieses Projektes ist es, ein Dashboard zur Visualisierung und Vergleich verschiedener Large Language Models (LLMs) im universitären Umfeld zu entwickeln. Dabei sollen Parameter wie Durchsatz, ethische Aspekte, Qualität und Sicherheit unter Berücksichtigung von Datenschutzrichtlinien verglichen werden.

<h2>Hintergrund & Idee</h2>

<h3>Problemstellung </h3>

Mit der zunehmenden Nutzung von LLMs in verschiedenen Bereichen, einschließlich des universitären Umfelds, besteht ein Bedarf an Werkzeugen, die den Vergleich und die Bewertung dieser Modelle erleichtern. Die Herausforderung besteht darin, diese Modelle nicht nur in Bezug auf ihre Leistungsfähigkeit, sondern auch auf ethische und sicherheitstechnische Aspekte zu bewerten. Dabei sollen diese auch auf technischen Geräten welche nicht viel leisten können verfügbar sein.  

<h3>Relevante Forschung & Technologie</h3>

Einführung

Die Entwicklung und Evaluierung von Large Language Models (LLMs) ist ein dynamisches Feld, das sowohl technische Innovationen als auch ethische Überlegungen umfasst. In diesem Abschnitt gehen wir auf relevante Forschung und die technologischen Fortschritte, die für die Entwicklung eines LLM-Dashboards im universitären Umfeld von Bedeutung sind ein.

Leistungsbewertung von LLMs

Die Leistung von LLMs wird anhand verschiedener Parameter bewertet, die für das universitäre Umfeld relevant sind. Diese umfassen Durchsatz, Qualität der Antworten und Sicherheit.

1. Durchsatz: Dieser Parameter misst die Effizienz eines LLMs, indem die Anzahl der pro Zeiteinheit verarbeiteten Anfragen bewertet wird. Verschiedene Betriebsbedingungen, wie unterschiedliche Nutzerzahlen oder parallele Anfragen, werden getestet, um ein realistisches Bild der Leistungsfähigkeit zu erhalten.

2. Qualität der Antworten: Die Qualität wird durch Benchmarks wie standardisierte Tests und spezifische Use-Cases im universitären Kontext bewertet. Die Genauigkeit und Relevanz der Antworten spielen eine zentrale Rolle, wobei verschiedene Techniken wie Few-Shot und Zero-Shot Learning zum Einsatz kommen.

3. Sicherheitsaspekte: Die Sicherheitsbewertung konzentriert sich auf Datenschutz und Datensicherheit. Modelle müssen den Datenschutzrichtlinien der Universität entsprechen und dürfen keine sensiblen Informationen preisgeben.

Bias-Erkennung und -Minderung

Die Erkennung und Minderung von Bias in LLMs ist ein kritischer Aspekt, um faire und objektive Modelle zu gewährleisten. Die folgenden Schritte sind dabei von Bedeutung:

1. Vorbereitung: Identifikation von Stereotypen und demografischen Gruppen. Es wird eine Liste von stereotypischen Aussagen erstellt, die verschiedene demografische Gruppen betreffen, und diese Aussagen werden in unterschiedliche Vorlagen gegossen.

2. Erstellung von Eingabeaufforderungen: Formulierung von Aufforderungen, die das Modell dazu bringen sollen, einer stereotypischen Aussage zuzustimmen oder nicht. Diese Aufforderungen werden in gutartige, ungezielte und gezielte Kategorien unterteilt.

3. Evaluierung: Generierung und Auswertung der Modellantworten. Die Zustimmung des Modells zu stereotypischen Aussagen wird gemessen und in einem Übereinstimmungsindex dargestellt.

4. Aggregation der Ergebnisse: Die Übereinstimmungsindizes werden für verschiedene Stereotyp-Themen und demografische Gruppen berechnet und visualisiert, um ein umfassendes Bild der Bias-Verteilung zu erhalten.

Unterschiedliche Ansätze zur Bias-Detektion

Verschiedene statistische Methoden wie der Chi²-Test und der Agreement Index werden zur Bias-Detektion verwendet:

1. Chi²-Test: Vergleich von erwarteten und beobachteten Häufigkeiten, geeignet für kategoriale Daten. Gut für die Analyse von Zusammenhängen zwischen Variablen und Erkennung systematischer Unterschiede.

2. Agreement Index: Messung der proportionalen Übereinstimmung zwischen zwei Ratern oder Modellvorhersagen. Einfach zu berechnen, liefert jedoch keine statistische Validierung der Ergebnisse.

Toxizitätsbewertung

Die Toxizitätsbewertung eines LLMs erfolgt mithilfe der Perspective API, die toxische Sprache und Hassrede erkennt. Zwei Hauptmetriken werden verwendet:

1. Erwartete maximale Toxizität: Bewertet das Worst-Case-Generierungsszenario, indem der maximale Toxizitätswert aus mehreren Iterationen genommen wird.

2. Toxizitätswahrscheinlichkeit: Schätzt die Wahrscheinlichkeit, dass das Modell toxische Inhalte generiert. Diese Wahrscheinlichkeit wird als Häufigkeit toxischer Antworten in mehreren Iterationen gemessen.

Datensammlung und Vorverarbeitung

Die Datensammlung und Vorverarbeitung sind entscheidend für die Fairness-Berechnung:

1. Erfassung demografischer Merkmale: Sorgfältige Datenaufbereitung, um sicherzustellen, dass die Daten repräsentativ und ausgewogen sind.

2. Statistische Tests: Anwendung von Methoden wie Chi-Quadrat-Tests und Embeddings-Analyse zur Erkennung systematischer Vorurteile.

Fairness-Metriken

Zur Messung der Fairness von LLMs werden verschiedene Metriken eingesetzt:

1. Demographic Parity: Überprüfung der Entscheidungsgleichheit unabhängig von der Gruppenzugehörigkeit.

2. Equalized Odds: Vergleich der Fehlerraten zwischen verschiedenen Gruppen.

3. Equal Opportunity: Sicherstellung der Gleichheit positiver Ergebniskorrekturen für alle Gruppen.

4. Calibration: Überprüfung der Korrektheit der vorhergesagten Wahrscheinlichkeiten unabhängig von der Gruppenzugehörigkeit.

Kontinuierliche Überwachung

Die kontinuierliche Überwachung und Anpassung der Modelle ist notwendig, um langfristig faire und sichere LLMs zu gewährleisten. Regelmäßige Überprüfungen und Feedback-Schleifen helfen, neue oder fortbestehende Vorurteile zu identifizieren und zu adressieren.

Quellen

https://arxiv.org/pdf/2306.11698
https://arxiv.org/pdf/2308.13387v1
https://www.jstor.org/stable/pdf/2288877.pdf?refreqid=fastly-default%3A1a7dbed3dd5d9d2d8b02f2f6557c0923&ab_segments=&origin=&initiator=&acceptTC=1 

<h3>Projektidee</h3>

Die Idee ist es, ein Dashboard zu entwickeln, das es Universitätsmitgliedern ermöglicht, verschiedene LLMs anhand definierter Parameter direkt zu vergleichen. Dies soll die Entscheidungsfindung bezüglich der Nutzung dieser Modelle im akademischen Kontext erleichtern. Besonders hinsichtlich der Generierung von Texten oder Beispielaufgaben. Eine weiterer Anwendungsfall ist die Nutzung des Dashboards zur Übersetzung der Inhalte für Studierende. 

<h2>Details zur Umsetzung</h2>

Lösungsskizze

Definition der zu vergleichenden Parameter

- Durchsatz: Messung der Verarbeitungsgeschwindigkeit der LLMs.

- Ethische Aspekte: Bewertung der Modelle hinsichtlich ihrer Einhaltung ethischer Richtlinien.

- Qualität: Evaluierung der Antwortqualität anhand von Benchmarks.

- Sicherheit: Bewertung der Sicherheitsmerkmale der Modelle unter Berücksichtigung der Datenschutzrichtlinien.


Einrichtung des Dashboards

- Entwicklung eines Dashboards: Erstellung einer Benutzeroberfläche zur Visualisierung und zum Vergleich der LLMs.

- Benutzerfreundlichkeit: Implementierung einer Oberfläche, die den Bedürfnissen und Anforderungen von Universitätsmitgliedern entspricht.


Definition und Anwendung von Benchmarks

- Festlegung von Benchmarks: Definition von objektiven Messkriterien zur Bewertung der Antwortqualität der LLMs.

- Integration der Ergebnisse: Darstellung der Benchmark-Ergebnisse im Dashboard.


Messung des Durchsatzes

- Mechanismen zur Durchsatzmessung: Implementierung von Tools zur kontinuierlichen Messung des Durchsatzes unter verschiedenen Betriebsbedingungen.


Visualisierung der Ergebnisse

- Darstellung im Dashboard: Entwicklung von Visualisierungen für die Vergleichsergebnisse zur sofortigen Analyse.


Möglichkeit zur gleichzeitigen Abfrage verschiedener LLMs

- Integration der Suchfunktion: Implementierung einer Suchzeile zur gleichzeitigen Abfrage mehrerer LLMs.

- Darstellung der Antworten: Vergleich der Antworten der LLMs im Dashboard.


Evaluierung der Sicherheitsaspekte

- Untersuchung der Sicherheitsaspekte: Analyse der Sicherheitsmerkmale jedes LLMs im Kontext der Datenschutzrichtlinien.

- Integration der Sicherheitsbewertungen: Darstellung der Sicherheitsbewertungen im Dashboard.

 

Technischer Aufbau des Dashboards: 

![image](https://github.com/user-attachments/assets/9f625363-7f7d-4eff-b990-47a9f09f6d6f)



<h3>Interessante Designentscheidungen </h3>

Durch die Nutzung von der Ollama API war es möglich sowohl ohne Boilerplate beliebig viele Modelle auswählen zu können und stets State-of-the-Art in einem sich schnell wandelnden Feld zu sein. 

Die Umsetzung in Python Dash ermöglichte eine schlanke Lösung im Browser mit minimalen Ladezeiten und einer Benutzeroberfläche unabhängig

Technische Details 

Das Projekt zur Evaluierung und Verbesserung von Large Language Models (LLMs) wurde auf einer umfassenden technischen Infrastruktur aufgebaut. Diese umfasst sowohl Frontend- als auch Backend-Komponenten und verwendet verschiedene Technologien und Methoden zur Umsetzung. Hier sind die technischen Details:

Frontend

Das Frontend des Dashboards wurde mit Python Dash entwickelt. Dash ist ein Framework für die Erstellung interaktiver Webanwendungen, das besonders gut für Datenvisualisierungen geeignet ist. Die wesentlichen Komponenten des Frontends sind:

- Suchzeile: Ermöglicht Benutzern die Eingabe von Abfragen.

- Dropdown-Menü für LLM-Auswahl: Benutzer können zwischen verschiedenen LLMs wählen.

- Antwortbox: Zeigt die generierten Antworten der LLMs an.

Diese Komponenten wurden entwickelt, um eine benutzerfreundliche und interaktive Oberfläche zu schaffen, die den Zugang zu den verschiedenen Funktionen des Dashboards erleichtert.

Backend

Das Backend wurde mit Python Flask realisiert, einem Mikro-Webframework, das für seine Einfachheit und Flexibilität bekannt ist. Die wichtigsten Funktionen des Backends umfassen:

- Schnittstelle zu den LLMs: Implementiert mit OLLAMA. Diese Schnittstelle leitet Anfragen aus dem Frontend an die lokal heruntergeladenen Modelle weiter und sendet die Antworten zurück.

- Modellverwaltung: Verwaltung und Auswahl verschiedener LLMs, die für die Verarbeitung der Benutzeranfragen verwendet werden.

- Datenverarbeitung: Vorverarbeitung der Eingaben und Nachverarbeitung der Modellantworten, um sicherzustellen, dass die Daten korrekt und konsistent sind.

Benchmarks

Bias-Erkennung:

Die Erkennung von Bias erfolgt durch die Analyse von Modellantworten auf stereotype Aussagen. Hierbei werden verschiedene Metriken verwendet, darunter der Übereinstimmungsindex, der die Häufigkeit misst, mit der das Modell stereotypischen Aussagen zustimmt.

Toxizitätserkennung:

Verwendet wird die Perspective API, um toxische Inhalte zu identifizieren. Wichtige Metriken sind die erwartete maximale Toxizität und die Toxizitätswahrscheinlichkeit.

Fairness-Metriken:

Zur Bewertung der Fairness des Modells werden verschiedene Metriken wie Demographic Parity, Equalized Odds, Equal Opportunity und Calibration angewandt, um sicherzustellen, dass das Modell keine systematischen Vorurteile oder Diskriminierungen aufweist.

Latenz:

1. Time To First Token (TTFT): Dies ist die Zeitspanne, die vergeht, bis der Benutzer nach der Eingabe eines Prompts das erste Token von dem Modell erhält. TTFT ist ein kritischer Faktor für die Benutzererfahrung, da eine niedrige TTFT bedeutet, dass das Modell schnell auf die Eingaben reagiert. Faktoren, die TTFT beeinflussen, umfassen die Modellgröße, Serverkapazität und die Effizienz der Anfrageverarbeitung.

2. Total Generation Time: Diese Metrik umfasst die gesamte Latenz, vom Empfang der Eingabeaufforderung bis zur Bereitstellung der vollständigen Antwort. Sie bietet eine umfassende Bewertung der End-to-End-Leistung des LLMs und ist entscheidend für die Echtzeitanwendung, bei der eine zügige Antwortzeit erforderlich ist.

Durchsatz:

Der Durchsatz eines LLM gibt an, wie viele Anfragen oder Tokens das Modell innerhalb eines bestimmten Zeitraums verarbeiten kann. Es gibt zwei Hauptarten der Durchsatzmessung:

1. Anfragen pro Sekunde: Misst, wie viele Benutzeranfragen das Modell pro Sekunde verarbeiten kann. Ein hoher Wert zeigt an, dass das Modell in der Lage ist, viele Anfragen effizient zu bearbeiten.

<h3>Herausforderungen und Lösungen</h3>

Einer der wichtigen Erfolge war die Fertigstellung und der Upload des Projektplans am 13.05.2024. Dieser Plan bildete die Grundlage für alle weiteren Arbeiten und wurde von allen Teammitgliedern genehmigt und daraufhin auf Moodle hochgeladen. Nach Erhalt des Feedbacks wurde der Projektplan aktualisiert, was ein weiterer Meilenstein war. Dies erforderte gemeinschaftliche Diskussionen und Konsensfindung, um sicherzustellen, dass alle relevanten Punkte berücksichtigt wurden.

Ein weiterer bedeutender Fortschritt war die Entwicklung des Frontends des Dashboards, bei dem wichtige Komponenten wie die Suchzeile, das Dropdown-Menü für die Auswahl der Large Language Models (LLM) und die Antwortbox funktionell integriert wurden. Dies wurde mithilfe von Python Dash realisiert, um eine benutzerfreundliche Oberfläche zu gewährleisten. Parallel dazu wurde das Backend des Dashboards erfolgreich mit Python Flask implementiert. Eine entscheidende Komponente war die Schnittstelle zu den LLMs, die mithilfe von OLLAMA eingerichtet wurde, sodass Anfragen vom Frontend weitergegeben und die Antworten von lokal heruntergeladenen Modellen berechnet und zurückgesendet werden konnten.

Bei den Herausforderungen war das Auftreten von Fehlern in den Antworten der LLMs ein Risiko. Einige Antworten waren unvollständig oder wurden langsam generiert. Dieses Problem konnte durch die sorgfältige Auswahl der Modelle und die Verbesserung der Synchronisation behoben werden, sodass Antworten erst dann an das Frontend gesendet wurden, wenn sie vollständig berechnet waren.

Nach Erhalt des Peer-Feedbacks wurden Pläne zur Überarbeitung des Feedback-Buttons gemacht, eine wichtige Aktivität. Anstatt eines "Like"/"Dislike"-Buttons wird es eine Darstellung durch Smileys (traurig, mittel, glücklich) geben. Eine Feedback-Option soll integriert werden, bei der die Bewertung der LLMs angezeigt wird, inklusive der Anzahl der Bewertungen und des Durchschnitts. Weitere statische Merkmale wie ethische Aspekte (Bias, Fairness und Inklusivität) sollen ebenfalls implementiert und visualisiert werden.

Eine weitere Herausforderung lag in der Berechnung und Implementierung weiterer Benchmarks wie Toxizität, Stereotypen, Privatsphäre und Fairness. Diese ethischen Aspekte wurden anhand von Literatur untersucht und als Mock-Up in das LLM-Dashboard eingebunden. Obwohl die weiterführenden Diskussionen über die Benchmarks ein geringes Risiko darstellten und Zeit in Anspruch nahmen, waren sie notwendig für eine gründliche Analyse. Die Implementation der Berechnung der Parameter erforderte historische Daten für die statistische Auswertung, was ebenfalls als geringes Risiko eingestuft wurde.

<h3>Ergebnisse und Evaluation</h3>

Das Projekt zur Evaluierung und Verbesserung von Large Language Models (LLMs) hat zahlreiche wichtige Ergebnisse hervorgebracht, die in mehreren Phasen erreicht wurden. Die Evaluation erfolgte systematisch durch die Implementierung und Testung verschiedener Metriken sowie die Entwicklung eines Dashboards zur Visualisierung und Analyse der Ergebnisse.

Entwicklung und Implementierung des Dashboards

Ein wesentlicher Erfolg war die Entwicklung eines funktionalen Dashboards, das in Python Dash für das Frontend und Python Flask für das Backend realisiert wurde. Die Schnittstelle zu den LLMs wurde mithilfe von OLLAMA implementiert. Diese ermöglicht es, Anfragen vom Frontend an lokal heruntergeladene Modelle weiterzuleiten und die berechneten Antworten zurückzusenden. Das Dashboard integriert wichtige Komponenten wie Suchzeilen, Dropdown-Menüs für die Modellauswahl und Antwortboxen.

Bias- und Toxizitätserkennung

Die Evaluation der LLMs konzentrierte sich auf die Erkennung und Quantifizierung von Bias und Toxizität. Die Bias-Erkennung erfolgte in mehreren Schritten:

1. Vorbereitung: Auswahl von Stereotypen und demografischen Gruppen, Erstellung von Vorlagen für verschiedene stereotype Aussagen.

2. Erstellung von Eingabeaufforderungen: Formulierung gutartiger, ungezielter und gezielter Aufforderungen, um die Reaktion des Modells auf stereotype Aussagen zu testen.

3. Evaluierung: Generierung und Analyse von Modellantworten, Berechnung des Übereinstimmungsindex zur Quantifizierung der Bias-Tendenzen.

4. Aggregation der Ergebnisse: Durchschnittliche Übereinstimmungsindizes wurden über verschiedene Stereotyp-Themen und demografische Gruppen hinweg berechnet und in Heatmaps visualisiert.

Für die Toxizitätserkennung wurde die Perspective API verwendet. Hierbei wurden folgende Metriken berechnet:

- Erwartete maximale Toxizität: Worst-Case-Szenario basierend auf den höchsten Toxizitätswerten der generierten Inhalte.

- Toxizitätswahrscheinlichkeit: Wahrscheinlichkeit, dass das Modell toxische Antworten produziert, basierend auf der empirischen Häufigkeit solcher Antworten.

Fairness-Metriken

Zur Berechnung der Fairness von LLMs wurden verschiedene Metriken verwendet, darunter:

- Demographic Parity: Überprüfung, ob das Modell unabhängig von der Gruppenzugehörigkeit eine bestimmte Entscheidung trifft.

- Equalized Odds und Equal Opportunity: Vergleich der Fehlerraten und der Wahrscheinlichkeit korrekter Vorhersagen zwischen verschiedenen Gruppen.

- Calibration: Überprüfung, ob die vorhergesagten Wahrscheinlichkeiten die tatsächlichen Chancen korrekt widerspiegeln.

Evaluation und Anpassung

Die Evaluation der Modelle erfolgte kontinuierlich durch die Anwendung der entwickelten Metriken und die Analyse der Ergebnisse im Dashboard. Dabei wurden die folgenden Schritte unternommen:

- Modellbewertung: Einsatz der Bias- und Fairness-Metriken zur Bewertung der Modelle.

- Bias Mitigation: Anwendung von Techniken zur Reduzierung identifizierter Verzerrungen, einschließlich Re-Balancing der Trainingsdaten und Anpassung der Verlustfunktion.

- Feedback-Schleifen: Integration von Nutzerfeedback zur Identifikation und Adressierung neuer oder fortbestehender Vorurteile.



Insgesamt konnte durch das Projekt eine fundierte Methodik zur Evaluation und Verbesserung von LLMs entwickelt und implementiert werden. Die erzielten Ergebnisse tragen wesentlich zur Weiterentwicklung von fairen und zuverlässigen Sprachmodellen bei.


Entwicklung starten:

Step 1: Bei einer IDE neues projekt von VersionControl anlegen und das Github Repository klonen

Step 2: Um die LLMs anzusprechen, muss der Ollama Client im Hintergrund laufen, dieser kann unter https://ollama.com heruntergeladen werden

Step 3: Per Terminal können nun die LLMs zur lokalen Benutzung heruntergeladen werden mit
        ollama pull Modellname

        In unserem Beispiel haben wir die 3 Modelle Mistral, Phi3 und Gemma verwendet
        ollama pull mistral
        ollama pull phi3
        ollama pull gemma 

Step 4: In der IDE sind alle notwendigen Packages zu installieren, im Detail:
        pip install flask, dash, ollama, dash_bootstrap_components, dash_daq, dash-table, dash_html_components

Step 5: run.py ausführen



Benutzerhandbuch

Im oberen Bereich des Dashboards ist links ein gewöhnliches Input zu finden, in das der Prompt eingegeben werden kann. Rechts daneben sind 3 Dropdownmenüs, mit welchen das zu benutzende LLM ausgewählt werden kann. Die Auswahlmöglichkeiten sind im Quellcode anzupassen und funktionieren nur, wenn sie mit Ollama im Voraus heruntergeladen wurden.

Darunter sind die Ausgabefenster zu finden. Das obere ist zugehörig zum LLM im linken Dropdown usw. Die Antwort wird wenn vom Modell in Markdown dargestellt, was die Übersichtlichkeit und optische Aufbereitung der Antwort unterstützt. Ist die Antwort generiert, erscheinen Emojis, mit denen die Qualität der Antwort bewertet werden kann. Dieses dient dazu, ein Gesamtqualitätsscore zu bilden, der in der unteren Tabelle wieder verwendet werden kann. Rechts daneben befindet sich die Ausgabezeit in Form eines Tachometers. Dieses lässt sich nutzen, um die Antwortzeit der einzelnen LLMs miteinander vergleichen zu können.

Der letzte Abschnitt ist die Parametervergleichstabelle. Hier können dynamische (vom Gerät abhängige) Parameter links und statische, eher ethische Parameter rechts der einzelnen LLM miteinander verglichen werden. Dabei unterstützt die darunter liegende dynamische Diagarmmdarstellung, in der einzelne Parameter auch visuell miteinander verglichen werden können.
