
class PaceCalculator:
    def __init__(self):
        #Zonen Faktoren
        self.Zone1Faktor = 1.35
        self.Zone2Faktor = 1.22
        self.Zone3Faktor = 1.09
        self.Zone4Faktor = 1.02
        self.Zone5Faktor = 0.95

        #Zone Pace set auf 0 am Anfang
        self.Zone1Pace = 0
        self.Zone2Pace = 0
        self.Zone3Pace = 0
        self.Zone4Pace = 0
        self.Zone5Pace = 0

    def pace_zonen(self,minuten,sekunden):

        gesamt_sekunden = minuten * 60 + sekunden

        self.Zone1Pace = gesamt_sekunden * self.Zone1Faktor
        self.Zone2Pace = gesamt_sekunden * self.Zone2Faktor
        self.Zone3Pace = gesamt_sekunden * self.Zone3Faktor
        self.Zone4Pace = gesamt_sekunden * self.Zone4Faktor
        self.Zone5Pace = gesamt_sekunden * self.Zone5Faktor

        self.printPace()

    def printPace(self):
        print(f"Zone 1 (Erholung): {int((self.Zone1Pace)/60)}:{int((self.Zone1Pace%60))}/km")
        print(f"Zone 2 (Grundlagenausdauer):  {int((self.Zone2Pace)/60)}:{int((self.Zone2Pace%60))}/km")
        print(f"Zone 3 (Tempo):  {int((self.Zone3Pace)/60)}:{int((self.Zone3Pace%60))}/km")
        print(f"Zone 4 (Laktat-Akkumulation):  {int((self.Zone4Pace)/60)}:{int((self.Zone4Pace%60))}/km")
        print(f"Zone 5 (VO2max):  {int((self.Zone5Pace)/60)}:{int((self.Zone5Pace%60))}/km")

    def inputPace(self):
        print("---------------------------------")
        minuten = int(input("Minuten: "))
        sekunden = int(input("Sekunden: "))
        print("---------------------------------")
        self.pace_zonen(minuten,sekunden)



calculator = PaceCalculator()
calculator.inputPace()
