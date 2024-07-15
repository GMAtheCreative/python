import java.util.Scanner;
public class LargestandSecondLargest{
	public static void main(String [] args){

		Scanner collect = new Scanner(System.in);
		
		int largest = 0;
		int secondlargest = 0;

		for (count = 0; count <= 10; count++){
			
			System.out.println("enter number: ");
			int number = collect.nextInt();

			if (number > largest){
				largest = number;
			}

			else if (number < largest && number > secondlargest){
				secondlargest = number;
			}

		}
		System.out.printf("largest number is %d, second largest number is %d",largest, secondlargest);

		
	}
}