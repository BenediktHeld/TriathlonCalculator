
class PaceCalculator:
    def __init__(self):
        self.Zone1Faktor = 1.35
        self.Zone2Faktor = 1.22
        self.Zone3Faktor = 1.09
        self.Zone4Faktor = 1.02
        self.Zone5Faktor = 0.95

    def pace_zonen(self,minuten,sekunden):

        gesamt_sekunden = minuten * 60 + sekunden

        # Berechnung der Pace-Zonen in Sekunden pro Kilometer
        zonen = {
            "Zone 1 (Erholung)": gesamt_sekunden * self.Zone1Faktor,
            "Zone 2 (Grundlagenausdauer)": gesamt_sekunden * self.Zone2Faktor,
            "Zone 3 (Tempo)": gesamt_sekunden * self.Zone3Faktor,
            "Zone 4 (Laktat-Akkumulation)": gesamt_sekunden * self.Zone4Faktor,
            "Zone 5 (VO2max)": gesamt_sekunden * self.Zone5Faktor
        }

        # Ausgabe der Zonen in Minuten:Sekunden Format
        for zone, pace in zonen.items():
            minuten = int(pace // 60)
            sekunden = int(pace % 60)
            print(f"{zone}: {minuten}:{sekunden:02d}/km")

    def inputPace(self):
        print("---------------------------------")
        minuten = int(input("Minuten: "))
        sekunden = int(input("Sekunden: "))
        print("---------------------------------")
        self.pace_zonen(minuten,sekunden)



calculator = PaceCalculator()
calculator.inputPace()
