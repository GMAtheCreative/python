import java.util.Scanner;
public class IfElseStatement{
	public static void main(String [] args){

		Scanner collect = new Scanner(System.in);

		System.out.println("Enter two numbers and i will tell you the the relationships they satisfy");

		System.out.println("Enter first number: ");
		int number1 = collect.nextInt();
	
		System.out.println("Enter second number: ");
		int number2 = collect.nextInt();

		if (number1 == number2){
			System.out.println(number1 + " is equals " + number2);
		}
		else{
			System.out.println(number1 + " is not equals " + number2);
		}

		if (number1 < number2){
			System.out.println(number1 + " is less than " + number2);
		}
		else{
			System.out.println(number1 + " is greater than " + number2);
		}

		if (number1 <= number2){
			System.out.println(number1 + " is less than or equals " + number2);
		}
		else{
			System.out.println(number1 + " is greater than or equals " + number2);
		}



		
	}
}