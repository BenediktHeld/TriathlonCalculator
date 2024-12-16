import java.util.Scanner;
public class PaceCalculator {
    //Zeit
    private double gesamt_sekunden = 0;
    private double minuten = 0;
    private double sekunden = 0;

    //Zonen Faktoren
    private double Zone1Faktor = 1.35;
    private double Zone2Faktor = 1.22;
    private double Zone3Faktor = 1.09;
    private double Zone4Faktor = 1.02;
    private double Zone5Faktor = 0.95;

    //Zone Pace set auf 0 am Anfang
    private double Zone1Pace = 0;
    private double Zone2Pace = 0;
    private double Zone3Pace = 0;
    private double Zone4Pace = 0;
    private double Zone5Pace = 0;

    //Konstruktor
    public PaceCalculator(){

    }

    public void pace_zonen(){
        this.gesamt_sekunden = this.minuten * 60 + this.sekunden;

        //Berechung der Pace-Zonen in Sekunden pro Kilometer
        this.Zone1Pace = this.gesamt_sekunden * this.Zone1Faktor;
        this.Zone2Pace = this.gesamt_sekunden * this.Zone2Faktor;
        this.Zone3Pace = this.gesamt_sekunden * this.Zone3Faktor;
        this.Zone4Pace = this.gesamt_sekunden * this.Zone4Faktor;
        this.Zone5Pace = this.gesamt_sekunden * this.Zone5Faktor;

        this.printPace();
    }

    public void printPace() {
        System.out.println("Zone 1 (Erholung): " + (int) this.Zone1Pace/60 +":"+(int) this.Zone1Pace%60);
        System.out.println("Zone 2 (Grundlagenausdauer): " + (int) this.Zone2Pace/60 +":"+(int) this.Zone2Pace%60);
        System.out.println("Zone 3 (Tempo): "+ (int) this.Zone3Pace/60 +":"+(int) this.Zone3Pace%60);
        System.out.println("Zone 4 (Laktat-Akkumulation): "+ (int) this.Zone4Pace/60 +":"+(int) this.Zone4Pace%60);
        System.out.println("Zone 5 (V02Max): "+ (int) this.Zone5Pace/60 +":"+(int) this.Zone5Pace%60);
    }

    public void inputPace(){
        Scanner scan = new Scanner(System.in);
        System.out.println("----------------------------------------");
        System.out.print("Minuten: ");
        this.minuten = scan.nextInt();
        System.out.print("\nSekunden: ");
        this.sekunden = scan.nextInt();
        System.out.println("----------------------------------------");
        this.pace_zonen();
    }
}


public class Main {
    public static void main(String[] args) {
        PaceCalculator p1 = new PaceCalculator();
        p1.inputPace();
    }
}
