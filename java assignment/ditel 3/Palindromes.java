import java.util.Scanner;
public class Palindromes{
	public static void main(String [] args){

		Scanner collect = new Scanner(System.in);

		System.out.println("Enter a 5digit number: ");
		int number = collect.nextInt();

		int originalNumber = number;
		int reverse = 0;

		while(number != 0){
			int newNumber = number % 10;
			reverse = reverse * 10 + newNumber;
			number /= 10;
		}
		 if(originalNumber == reverse){
			System.out.println("its palindrome");
		}
	
	}
}