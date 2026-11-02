import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass

GENRE_MATCH_POINTS = 3.0
MOOD_MATCH_POINTS = 2.0
ENERGY_MAX_POINTS = 2.0
ACOUSTIC_MATCH_POINTS = 1.0


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        ranked_songs = sorted(
            self.songs,
            key=lambda song: score_song(user_prefs, song.__dict__)[0],
            reverse=True,
        )
        return ranked_songs[:max(k, 0)]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        _, reasons = score_song(user_prefs, song.__dict__)
        if not reasons:
            return "No preference matches were found."
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""

    numeric_fields = {
        "energy",
        "tempo_bpm",
        "valence",
        "danceability",
        "acousticness",
    }
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            row["id"] = int(row["id"])
            for field in numeric_fields:
                row[field] = float(row[field])
            songs.append(row)
    return songs


def _score_preferences(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    score = 0.0
    reasons = []

    for preference, feature, points, label in (
        ("genre", "genre", GENRE_MATCH_POINTS, "Genre"),
        ("mood", "mood", MOOD_MATCH_POINTS, "Mood"),
    ):
        preferred_value = user_prefs.get(preference)
        song_value = song.get(feature)
        if (
            preferred_value is not None
            and song_value is not None
            and str(preferred_value).strip().casefold()
            == str(song_value).strip().casefold()
        ):
            score += points
            reasons.append(f"{label} match (+{points:g} points)")

    target_energy = user_prefs.get("energy")
    song_energy = song.get("energy")
    if target_energy is not None and song_energy is not None:
        energy_points = max(
            0.0,
            ENERGY_MAX_POINTS * (1.0 - abs(float(target_energy) - float(song_energy))),
        )
        score += energy_points
        if energy_points > 0:
            reasons.append(f"Energy close (+{energy_points:.2f} points)")

    likes_acoustic = user_prefs.get("likes_acoustic")
    acousticness = song.get("acousticness")
    if likes_acoustic is not None and acousticness is not None:
        acoustic_match = float(acousticness) >= 0.5
        if bool(likes_acoustic) == acoustic_match:
            score += ACOUSTIC_MATCH_POINTS
            reasons.append(f"Acoustic preference match (+{ACOUSTIC_MATCH_POINTS:g} point)")

    return score, reasons


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a song's preference score and matching reasons."""

    return _score_preferences(user_prefs, song)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs ranked by score with explanations."""

    scored_songs = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]
    ranked_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return [
        (song, score, "; ".join(reasons) or "No preference matches were found.")
        for song, score, reasons in ranked_songs[:max(k, 0)]
    ]
