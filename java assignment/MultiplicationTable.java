import java.util.Scanner;
public class MultiplicationTable{
	public static void main(String [] args){

		Scanner collect = new Scanner(System.in);
		
		System.out.println("Enter any Number to get the multiplication table: ");
		int number = collect.nextInt(); 

		for(int counter = 1; counter <= 10; counter++){
			multiplication = number * counter;
	
			System.out.printf("%d x %d = %d", number, counter, multiplication);
		}

	}
}