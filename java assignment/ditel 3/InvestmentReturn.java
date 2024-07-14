import java.util.Scanner;
public class InvestmentReturn{
	public static void main(String [] args){

		Scanner collect = new Scanner(System.in);
	
		System.out.println("Enter the Amount you want to invest: ");
		int amounttoinvest = collect.nextInt();

		double investmentaftertenyears = 0;
		double investmentaftertwentyyears = 0;
		double investmentafterthirtyyears = 0;

		for (int counter = 0; counter <= 30; counter++){

			if (counter == 10){
				investmentaftertenyears = amounttoinvest * Math.pow(1 + 0.07, counter);
			}

			if (counter == 20){
		investmentaftertwentyyears = amounttoinvest * Math.pow(1 + 0.07, counter);
			}

			if (counter == 30){ 
		investmentafterthirtyyears = amounttoinvest * Math.pow (1 + 0.07, counter);
			}

		}
	System.out.printf("Your investment in 10yrs is %.2f \nYour investment in 20yrs is %.2f \nYour investment in 30yrs is %.2f ", investmentaftertenyears, investmentaftertwentyyears, investmentafterthirtyyears);

		
	}
}