import java.util.Scanner;
public class NumberOfStudents{
	public static void main(String [] args){

		Scanner collect = new Scanner(System.in);

		int fails = 0;
		int passes = 0;
		
		for(int counter = 1; counter <=10; counter++){
		
			System.out.printf("Enter grade of student%d: ", counter);
			int scores = collect.nextInt();

			if(scores <= 45)
				fails += 1;

			else
				passes += 1;
		}

		System.out.printf("The number of student that passed is %d, The number of students that failed is %d", passes, fails); 

		
	}
}