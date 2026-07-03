import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        RecommendationEngine engine = new RecommendationEngine();

        System.out.println("==================================");
        System.out.println("      Movie Recommendation");
        System.out.println("==================================");

        System.out.println("\nAvailable Genres:");
        System.out.println("1. Action");
        System.out.println("2. Horror");
        System.out.println("3. Comedy");
        System.out.println("4. Sci-Fi");

        System.out.print("\nEnter your favorite genre: ");
        String genre = scanner.nextLine();

        engine.recommend(genre);

        scanner.close();
    }
}