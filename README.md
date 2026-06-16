Robocar 

Im Rahmen dieses Projekts wurde ein autonomer Linienfolger auf Basis eines Raspberry Pi entwickelt. Ziel war es, einer schwarzen Linie auf hellem Untergrund selbstständig folgen zu können.

Die Software wurde in mehrere Module aufgeteilt, um die einzelnen Aufgabenbereiche übersichtlich voneinander zu trennen.

Die Datei motor.py ist für die Ansteuerung der vier Gleichstrommotoren zuständig. Die Motoren werden über einen PCA9685 PWM-Treiber angesteuert. Neben den grundlegenden Funktionen zur Initialisierung und zum Stoppen aller Motoren enthält das Modul verschiedene Fahrfunktionen wie Vorwärtsfahrt, Rechts- und Linkskurven sowie leichte Korrekturen nach links oder rechts.

In sensor.py werden die drei Infrarot-Liniensensoren ausgelesen. Für jeden Sensor existiert eine Funktion, die zurückgibt, ob die Linie erkannt wurde oder nicht. Zusätzlich werden verschiedene Sensorkombinationen ausgewertet, beispielsweise wenn mehrere Sensoren gleichzeitig die Linie erkennen oder wenn keine Linie erkannt wird.

Die eigentliche Fahrlogik befindet sich in control.py. Dort werden die Sensorwerte kontinuierlich ausgewertet und entsprechende Fahrbefehle an die Motorsteuerung übergeben. Je nach Position der Linie fährt das Fahrzeug geradeaus, lenkt nach links oder rechts oder führt kleinere Kurskorrekturen durch. Außerdem wird die zuletzt erkannte Position der Linie gespeichert, um die Linie nach einem kurzzeitigen Verlust wiederfinden zu können.

Die Datei main.py dient als Einstiegspunkt des Programms. Hier werden die benötigten Module initialisiert und die Steuerung gestartet. Zudem wird sichergestellt, dass beim Beenden des Programms alle Motoren gestoppt werden.

Zur besseren Wartbarkeit wurden verschiedene Parameter in eine config.json ausgelagert. Dazu gehören unter anderem die Fahrgeschwindigkeiten für Geradeausfahrt und Kurven, die PWM-Frequenz des PCA9685 sowie die Zykluszeit der Steuerung. Dadurch können wichtige Einstellungen angepasst werden, ohne Änderungen am eigentlichen Programmcode vornehmen zu müssen.

Das Programm arbeitet in einer Endlosschleife. Die Sensoren werden fortlaufend abgefragt, die Position der Linie bestimmt und anschließend die passende Motoransteuerung ausgeführt. Dadurch kann das Fahrzeug der Linie kontinuierlich folgen.
