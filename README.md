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

Darunter sind die Ausgabefenster zu finden. Das obere ist zugehörig zum LLM im linken Dropdown usw. Rechts daneben befindet sich die Ausgabezeit in Form eines Tachometers. Dieses lässt sich nutzen, um die Antwortzeit der einzelnen LLMs miteinander vergleichen zu können.

Im letzten Abschnitt ist die 
