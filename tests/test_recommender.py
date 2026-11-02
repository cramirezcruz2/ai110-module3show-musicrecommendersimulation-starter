from src.recommender import (
    Song,
    UserProfile,
    Recommender,
    recommend_songs,
    score_song,
)

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_genre_match_is_worth_three_points_and_mood_two():
    song = {"genre": "pop", "mood": "happy"}

    genre_score, _ = score_song({"genre": "pop"}, song)
    mood_score, _ = score_song({"mood": "happy"}, song)

    assert genre_score == 3
    assert mood_score == 2


def test_energy_points_decrease_with_distance_from_target():
    close_song = {"energy": 0.8}
    distant_song = {"energy": 0.3}

    close_score, _ = score_song({"energy": 0.75}, close_song)
    distant_score, _ = score_song({"energy": 0.75}, distant_song)

    assert close_score == 1.9
    assert distant_score == 1.1


def test_functional_recommendations_are_ranked_and_explained():
    songs = [
        {"title": "Chill Track", "genre": "lofi", "mood": "chill", "energy": 0.4},
        {"title": "Pop Track", "genre": "pop", "mood": "happy", "energy": 0.8},
    ]

    results = recommend_songs(
        {"genre": "pop", "mood": "happy", "energy": 0.8},
        songs,
        k=1,
    )

    assert len(results) == 1
    assert results[0][0]["title"] == "Pop Track"
    assert results[0][1] == 7
    assert "Genre match" in results[0][2]
    assert "Mood match" in results[0][2]
