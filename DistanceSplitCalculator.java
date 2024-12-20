import java.util.Scanner;
public class DistanceSplitCalculation {
    private int marathonTimeSeconds = 0;
    private int marathonPaceSeconds = 0;
    private int paceMinutes = 0;
    private int paceSeconds = 0;
    private double marathonDistance = 42.195;

    public static void secondsToHms(int seconds) {
        int hours = seconds / 3600; // Anzahl der Stunden
        int minutes = (seconds % 3600) / 60; // Anzahl der Minuten
        int remainingSeconds = seconds % 60; // Verbleibende Sekunden

        System.out.printf("%d:%02d:%02dh%n", hours, minutes, remainingSeconds);
    }

    public void calculateMarathonTime() {
        this.marathonTimeSeconds = (int) this.marathonDistance * this.marathonPaceSeconds;
        System.out.println("Marathon Time: ");
        secondsToHms(this.marathonTimeSeconds);
        System.out.println("Halbmarathon Split Time: ");
        secondsToHms(this.marathonTimeSeconds / 2);
    }
    public void inputPace() {
        Scanner scan = new Scanner(System.in);
        System.out.println("----------------------------------------");
        System.out.print("Minuten: ");
        int minuten = scan.nextInt();
        System.out.print("\nSekunden: ");
        int sekunden = scan.nextInt();
        System.out.println("----------------------------------------");
        this.paceMinutes = minuten;
        this.paceSeconds = sekunden;
        this.marathonPaceSeconds = minuten * 60 + sekunden;
        this.calculateMarathonTime();

    }

    public static void main(String[]args){
        DistanceSplitCalculation calculator = new DistanceSplitCalculation();
        calculator.inputPace();
    }
}
