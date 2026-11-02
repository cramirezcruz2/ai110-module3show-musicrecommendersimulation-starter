# 🎵 Music Recommender Simulation

## Project Summary

This project is a music recommendation system that suggests songs based on a user's music preferences. It compares song features with a user's taste profile, calculates a score for each song, and recommends the songs with the highest scores.

---

## How The System Works

My music recommender uses content-based filtering to recommend songs based on a user's preferences. Each Song stores information such as its genre, mood, energy, and tempo. The UserProfile stores the user's preferred genres, moods, and energy levels. The Recommender compares each song's features with the user's preferences and calculates a score based on how closely they match. Songs that match the user's preferred genre and mood receive more points. The system also gives points based on how close a song's energy is to the user's preferred energy level. Finally, the system sorts the songs by score from highest to lowest and recommends the highest-scoring songs first.


### User Profile

One example user profile stores these music preferences:
- Favorite genre: pop
- Favorite mood: happy
- Target energy: 0.8

### Algorithm Recipe

- Genre match: +3 points.
- Mood match: +2 points.
- Energy similarity: Up to +2 points based on how close the song's energy is to the user's preferred energy level.
- Acoustic preference match: +1 point when the song matches the user's acoustic preference.
- Songs are sorted from highest to lowest score, and the top 5 are recommended.

### Potential Biases

The system gives genre more points than mood or energy, which may cause it to favor songs from the user's preferred genre. It also does not consider listening history or artist variety. This could cause the system to overlook songs that match the user's mood but belong to a different genre.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the tests with:

```bash
python -m pytest

5 passed in 0.05s

---


## Sample Recommendation Output


The following examples show the results from running the recommender with three different user profiles.

### High-Energy Pop Profile

```text
PROFILE: High-Energy Pop
User preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 0.9}
Sunrise City - Score: 6.84
Gym Hero - Score: 4.94
Rooftop Lights - Score: 3.72
Storm Runner - Score: 1.98
Flashing Lights - Score: 1.82
```

### Moody Hip-Hop Profile

```text
PROFILE: Moody Hip-Hop
User preferences: {'genre': 'hip-hop', 'mood': 'moody', 'energy': 0.4}
Day 'n' Nite - Score: 6.42
Heartless - Score: 4.28
Flashing Lights - Score: 4.18
Nights - Score: 3.36
Night Drive Loop - Score: 3.30
```

### Conflicting Preferences Profile

```text
PROFILE: Conflicting Preferences
User preferences: {'genre': 'hip-hop', 'mood': 'sad', 'energy': 0.9}
Heartless - Score: 6.72
Flashing Lights - Score: 4.82
Day 'n' Nite - Score: 4.58
Storm Runner - Score: 1.98
Gym Hero - Score: 1.94
```
---

## Experiments You Tried

I tested the recommender using three different user profiles: High-Energy Pop, Moody Hip-Hop, and Conflicting Preferences. Each profile received different song recommendations based on its preferences.

I also changed the scoring weights to see how they affected the results. I lowered genre points from 3 to 1.5 and increased the maximum energy points from 2 to 4. The top recommended song stayed the same for all three profiles, but some other songs changed positions in the rankings. This showed me that changing the scoring weights can affect recommendations.

---

## Limitations and Risks

One limitation of my recommender is that it only has 15 songs, which limits the variety of recommendations. Some genres also have fewer songs than others. Another limitation is that songs can receive high scores based on energy even when they do not match the user's preferred genre or mood. The system also does not use listening history, artist preferences, tempo, or danceability when calculating scores.

---

## Reflection

I learned that recommendation systems use information about songs and user preferences to calculate scores and suggest music. I also learned that changing the scoring weights can change which songs are recommended. This helped me understand how music apps use data to make recommendations feel more personal.

I also learned that bias can happen when a system gives more importance to certain features than others. For example, my system gives genre more points, which can cause it to favor songs from one genre. Having a small dataset can also limit the variety of recommendations. This showed me why it is important to test recommendation systems and understand their limitations.


