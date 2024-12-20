class marathonSplitCalculator:
    def __init__(self):
        self.marathonTimeSeconds = 0
        self.marathonPaceSeconds = 0
        self.PaceMinutes = 0
        self.PaceSeconds = 0
        self.marathonDistance = 42.195

    def seconds_to_hms(self,seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        remaining_seconds = int(seconds % 60)

        print(f"{hours}:{minutes:02}:{remaining_seconds:02}h")

    def calculateMarathonTime(self):
        self.marathonTimeSeconds = self.marathonDistance * self.marathonPaceSeconds
        print("Marathon Time:")
        self.seconds_to_hms(self.marathonTimeSeconds)
        print("Halbmarathon Split:")
        self.seconds_to_hms(self.marathonTimeSeconds/2)
    def inputPace(self):
        print("---------------------------------")
        minuten = int(input("Minuten: "))
        sekunden = int(input("Sekunden: "))
        print("---------------------------------")
        self.PaceMinutes = minuten
        self.PaceSeconds = sekunden
        self.marathonPaceSeconds = minuten*60 + sekunden
        self.calculateMarathonTime()

calculator = marathonSplitCalculator()
calculator.inputPace()
