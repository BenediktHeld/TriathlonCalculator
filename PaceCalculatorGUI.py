from tkinter import *

class PaceCalculator:
    def __init__(self):
        # Zonen Faktoren
        self.Zone1Faktor = 1.35
        self.Zone2Faktor = 1.22
        self.Zone3Faktor = 1.09
        self.Zone4Faktor = 1.02
        self.Zone5Faktor = 0.95

        # Zone Pace set auf 0 am Anfang
        self.Zone1Pace = 0
        self.Zone2Pace = 0
        self.Zone3Pace = 0
        self.Zone4Pace = 0
        self.Zone5Pace = 0

    def pace_zonen(self, minuten, sekunden):
        gesamt_sekunden = minuten * 60 + sekunden
        self.Zone1Pace = gesamt_sekunden * self.Zone1Faktor
        self.Zone2Pace = gesamt_sekunden * self.Zone2Faktor
        self.Zone3Pace = gesamt_sekunden * self.Zone3Faktor
        self.Zone4Pace = gesamt_sekunden * self.Zone4Faktor
        self.Zone5Pace = gesamt_sekunden * self.Zone5Faktor

        self.printPace()

    def printPace(self):
        output = (
            f"Zone 1 (Erholung): {int((self.Zone1Pace)/60)}:{int((self.Zone1Pace%60))}/km\n"
            f"Zone 2 (Grundlagenausdauer):  {int((self.Zone2Pace)/60)}:{int((self.Zone2Pace%60))}/km\n"
            f"Zone 3 (Tempo):  {int((self.Zone3Pace)/60)}:{int((self.Zone3Pace%60))}/km\n"
            f"Zone 4 (Laktat-Akkumulation):  {int((self.Zone4Pace)/60)}:{int((self.Zone4Pace%60))}/km\n"
            f"Zone 5 (VO2max):  {int((self.Zone5Pace)/60)}:{int((self.Zone5Pace%60))}/km"
        )
        return output

    def inputPace(self):
        # Erstelle das Hauptfenster
        window = Tk()
        # Setze den Titel des Fensters
        window.title("Pace Calculator")
        # Setze die minimale Größe des Fensters
        window.minsize(width=500, height=400)

        # Erstelle ein Label (Textfeld)
        my_label = Label(text="Gib deine Pace ein:", font=("Arial", 24, "bold"))
        my_label.pack(side="top")

        # Textfeld für die Ausgabe
        self.output_text = Text(window, height=10, width=50)
        self.output_text.pack()

        # Erstelle ein Frame für die Eingabefelder und Labels
        input_frame = Frame(window)
        input_frame.pack(pady=10)

        # Label und Eingabefeld für Minuten
        Label(input_frame, text="Minuten:").grid(row=0, column=0)
        InputMinuten = Entry(input_frame)
        InputMinuten.grid(row=0, column=1)

        # Label und Eingabefeld für Sekunden
        Label(input_frame, text="Sekunden:").grid(row=1, column=0)
        InputSekunden = Entry(input_frame)
        InputSekunden.grid(row=1, column=1)

        # Funktion, die aufgerufen wird, wenn der Button geklickt wird
        def button_clicked():
            Text1 = int(InputMinuten.get())  # Hole den Text aus dem Eingabefeld
            Text2 = int(InputSekunden.get())
            self.pace_zonen(Text1, Text2)
            # Ausgabe in das Textfeld
            self.output_text.delete(1.0, END)  # Lösche vorherige Ausgaben
            self.output_text.insert(END, self.printPace())  # Füge die neuen Ausgaben hinzu

        # Erstelle einen Button
        button = Button(text="Berechne Pace", command=button_clicked)
        button.pack()

        # Starte die Hauptschleife des Fensters
        window.mainloop()

calculator = PaceCalculator()
calculator.inputPace()
