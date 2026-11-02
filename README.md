# 🎵 Music Recommender Simulation

## Project Summary

This project is a music recommendation system that suggests songs based on a user's music preferences. It compares song features with a user's taste profile, calculates a score for each song, and recommends the songs with the highest scores.

---

## How The System Works

My music recommender uses content-based filtering to recommend songs based on a user's preferences. Each Song stores information such as its genre, mood, energy, and tempo. The UserProfile stores the user's preferred genres, moods, and energy levels. The Recommender compares each song's features with the user's preferences and calculates a score based on how closely they match. Songs that match the user's preferred genre and mood receive more points, while numerical features like energy and tempo receive higher scores when they are closer to the user's preferences. Finally, the system sorts the songs by score from highest to lowest and recommends the highest-scoring songs first.

### User Profile

My user profile stores the user's music preferences:
- Favorite genre: hip-hop
- Favorite mood: moody
- Target energy: 0.75

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

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Top recommendations:

Day 'n' Nite - Score: 6.88
Because: Genre match (+3 points); Mood match (+2 points); Energy close (+1.88 points)

Heartless - Score: 4.98
Because: Genre match (+3 points); Energy close (+1.98 points)

Flashing Lights - Score: 4.88
Because: Genre match (+3 points); Energy close (+1.88 points)

Night Drive Loop - Score: 4.00
Because: Mood match (+2 points); Energy close (+2.00 points)

Nights - Score: 3.94
Because: Mood match (+2 points); Energy close (+1.94 points)


**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


