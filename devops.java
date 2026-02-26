import java.util.Scanner;
import java.util.Random;

public class devops {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int secretNumber = random.nextInt(50) + 1; // 1 to 50
        int guess;
        int attempts = 0;

        System.out.println("Guess a number between 1 and 50:");

        do {
            System.out.print("Enter your guess: ");
            guess = scanner.nextInt();
            attempts++;

            if (guess > secretNumber) {
                System.out.println("Too high!");
            } else if (guess < secretNumber) {
                System.out.println("Too low!");
            } else {
                System.out.println("Correct! You guessed it in " + attempts + " attempts.");
            }

        } while (guess != secretNumber);

        scanner.close();
    }
}
