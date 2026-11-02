"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # User music preferences
    user_prefs = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.8
    }

    # Get the top 5 song recommendations
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")

    for rec in recommendations:
        song, score, explanation = rec

        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()