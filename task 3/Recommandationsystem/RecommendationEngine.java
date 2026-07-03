import java.util.ArrayList;
import java.util.List;

public class RecommendationEngine {

    private List<Movie> movies;

    public RecommendationEngine() {

        movies = new ArrayList<>();

        movies.add(new Movie("Avengers: Endgame", "Action", 9.2));
        movies.add(new Movie("John Wick", "Action", 8.9));
        movies.add(new Movie("The Dark Knight", "Action", 9.5));

        movies.add(new Movie("The Conjuring", "Horror", 8.7));
        movies.add(new Movie("Annabelle", "Horror", 8.2));
        movies.add(new Movie("Insidious", "Horror", 8.6));

        movies.add(new Movie("3 Idiots", "Comedy", 9.3));
        movies.add(new Movie("Golmaal", "Comedy", 8.5));
        movies.add(new Movie("Hera Pheri", "Comedy", 9.1));

        movies.add(new Movie("Interstellar", "Sci-Fi", 9.4));
        movies.add(new Movie("Inception", "Sci-Fi", 9.3));
        movies.add(new Movie("The Martian", "Sci-Fi", 8.9));
    }

    public void recommend(String genre) {

        boolean found = false;

        System.out.println("\nRecommended Movies:\n");

        for (Movie movie : movies) {

            if (movie.getGenre().equalsIgnoreCase(genre)) {

                System.out.println(movie.getTitle()
                        + " | Genre: " + movie.getGenre()
                        + " | Rating: " + movie.getRating());

                found = true;
            }
        }

        if (!found) {
            System.out.println("No recommendations found.");
        }
    }
}