import java.util.Scanner;

public class BankAccount{
	public static void main(String... args){
		Scanner collect = new Scanner(System.in);
		

		String actions = """
				a. Deposit
				b. withdraw
				c. check your account balance
				or Exit""";

		System.out.println("Hello \nWelcome to Ace Bank");

		System.out.println("What will you love to do today:\n" + actions);
		String prompt = collect.next();

		int totalbalance = 0;
		while (!prompt.equalsIgnoreCase("exit")){

			switch (prompt){
				
	
				case "a":
					System.out.println("How much do you want to deposit: ");
					long deposit = collect.nextLong();
					totalbalance += deposit;
					
					if(deposit <= 0){
						System.out.println("invalid input");
					}

					else{
					System.out.println("keep it up :)");
					}
					break;

				case "b":
					System.out.println("How much do you want to withdraw: ");
					int withdraw = collect.nextInt();
					
					if (withdraw > totalbalance){
						totalbalance = totalbalance - withdraw;
						System.out.println("Insufficient fund :( \nplease make some deposit");
					}
					else if(withdraw <= 0){
						System.out.println("invalid input");
					}
					else{
						System.out.println("Successful>>>>>>>>>>>>>>>>....");
					}
					break;

				case "c":
					System.out.println("your acount balance is " + totalbalance);
					break;

				default:
					System.out.println("invalid input");
			}

		System.out.println("will you love to continue transaction:\n" + actions);
		prompt = collect.next();
		}

		
	}
}