import java.util.Scanner;
public class Factorial {
	public static void main(String [] args){

		Scanner collect = new Scanner(System.in);

		System.out.println("enter a number to get the factorial: ");
		int number = collect.nextInt();

		int factorial = 1;
		for (int counter = 1; counter <= number; counter++){
			factorial *= counter;
			System.out.println(factorial);
	
		}
		System.out.println(factorial);
		
	}
}
