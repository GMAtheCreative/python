import java.util.Scanner;
public class MilesPerGallon{
	public static void main(String [] args){

		Scanner collect = new Scanner(System.in);
		
		int milespergallon = 0;
		int totalmilespergallon = 1;
		
		System.out.println("Enter miles driven : ");
		int milesdriven = collect.nextInt();

		System.out.println("Enter gallons useds (-1 to end): ");
		int gallons = collect.nextInt();

		while (gallons != -1){

			milespergallon = milesdriven / gallons;
	
			System.out.printf("The amount of miles per gallon is %d\n", milespergallon);
	
			System.out.println("Enter miles driven : ");
			milesdriven = collect.nextInt();

			System.out.println("Enter gallons useds (-1 to end): ");
			gallons = collect.nextInt();
		}
		
		totalmilespergallon *= milespergallon;

		System.out.printf("The overall average mile/gallon is ", totalmilespergallon);


	}
}