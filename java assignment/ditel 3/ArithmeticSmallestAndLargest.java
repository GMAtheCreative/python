import java.util.Scanner;
public class ArithmeticSmallestAndLargest{
	public static void main(String... args){
		Scanner collect = new Scanner(System.in);

		int sum = 0;
		int average = 0;
		int product = 1;
		int smallest = 0;
		int largest = 0;

		for(int counter = 0; counter <= 4; counter++){
			System.out.println("Enter number: ");
			int number = collect.nextInt();
	
			product *= number;

			sum += number;

			if(smallest == 0 || number < smallest){
	
		 		smallest = number;
			}

			if(largest == 0 || number > largest){
				largest = number;
			}
		}

		average = sum / 2;

		System.out.printf("The sum is %d\nThe average is %d\nThe product of all the numbers is %d\nThe smallest is, %d\nThe largest is %d", sum, average, product, smallest, largest );

	
	}
}