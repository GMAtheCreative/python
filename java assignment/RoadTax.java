import java.util.Scanner;
public class RoadTax{
	public static void main(String [] args){

		Scanner collect = new Scanner(System.in);

		System.out.println("How much did you buy your car? : ");
		int amountOfCar = collect.nextInt();

		
		if(amountOfCar <= 1_000_000){
			int rate1 = amountOfCar * 10 / 100;

			System.out.printf("your tax in dollars is $%d", rate1); 
		}

		else if(amountOfCar > 1_000_000 && amountOfCar <= 3_000_000){
			int rate2 = amountOfCar * 15 / 100;

			System.out.printf("Your tax in Dollars is $%d",rate2 );
		}

		else if(amountOfCar > 3_000_000 && amountOfCar <= 5_000_000){
			int rate3 = amountOfCar * 20 / 100;

			System.out.printf("Your tax in Dollars is $%d",rate3 );
		}

		else if(amountOfCar > 5_000_000){
			int rate4 = amountOfCar * 25 / 100;

			System.out.printf("Your tax in Dollars is $%d",rate4 );
		}

		else{
			System.out.println("is that the price of your car");
		}
	}
}