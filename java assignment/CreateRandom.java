import java.util.*;
public class CreateRandom{
	public static void main(String [] args){

		Scanner collect = new Scanner(System.in);
		Random rand = new Random();

		int randomNumber = rand.nextInt(1001);
		
		int tooHigh = 0;
		int tooLow = 0;

		System.out.println("Lets play a game \"Yes or No\"");
		String playTheGame = collect.next();

		while (!playTheGame.equalsIgnoreCase("no")){

			System.out.println("Guess my number between \"1 and 1000\" with the fewest guesses: ");
			int letsAskTheUser = collect.nextInt();


			while (letsAskTheUser != randomNumber){

				if (letsAskTheUser <  randomNumber){
					tooLow += 1;

					System.out.println("Too low");	
				}

				else if(letsAskTheUser > randomNumber){
					tooHigh += 1;

					System.out.println("Too high");
				}

				else{
					System.out.println("Congratulations. you guessed the number!!");
				}
				System.out.println("Guess my number between \"1 and 1000\" with the fewest guesses: ");
				letsAskTheUser = collect.nextInt();
			}

			if (tooLow > 10){
				System.out.printf("The number of your lower guesses is %d\nThe number of your highest guesses is %d\nYour performance is too low\nTRY AGAIN!! :(", tooLow, tooHigh );
			}

			else if (tooHigh > 10){
				System.out.printf("The number of your lower guesses is %d\nThe number of your higher guesses is %d\nYour performance is too low\nTRY AGAIN!! :(",tooLow, tooHigh );
			}

			else{
				System.out.printf("The number of your lower guesses is %d\nThe number of your higher guesses is %d\nGOOD JOB!! :)", tooLow, tooHigh );
			}

			System.out.println("Will you love to continue my game \"Yes or No\"");
			playTheGame = collect.next();
		}

	System.out.println("Good bye, hope to see you soon");
	}
}