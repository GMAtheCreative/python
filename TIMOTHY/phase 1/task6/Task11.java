public class Task11 {

	public static int takesNumberReturnList (int number){
		
		int numberList [];
		int reverse = 0;
		while (number !=0){
			int newNumber = number % 10;
			reverse = reverse * 10 + newNumber;
			number //= 10;
		}
		
		while (reverse !=0){
			int reverse = number % 10;
			numberList[] = numberList[] * 10 + reverse;
			number //= 10;
		}
	}
}