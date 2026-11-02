# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeTrack 1.0 

---

## 2. Intended Use  

VibeTrack 1.0 is designed to recommend songs based on a user's music preferences. It uses genre, mood, and energy to calculate scores and rank songs. This project is intended for classroom learning and experimentation rather than a real music streaming service. It assumes users know what types of music they enjoy. 

---

## 3. How the Model Works  

The recommender compares each song's genre, mood, and energy with the user's preferences. Songs receive 3 points for a matching genre, 2 points for a matching mood, and up to 2 points based on how close the song's energy is to the user's target. An additional point can be awarded for an acoustic preference match. The system adds these points together, ranks the songs from highest to lowest, and displays the top five recommendations with explanations.

---

## 4. Data  

The system uses a CSV dataset containing 15 songs. Each song includes information like its title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. I added five more songs to expand the original dataset. The dataset includes different genres and moods, but it is still small and does not represent every type of music.

---

## 5. Strengths  

The recommender works well when users have clear genre, mood, and energy preferences. It produces different recommendations when users change their perferences. An example is, the High Energy Pop profile recommended Sunrise City, meanwhile the Moody Hip-Hop profile recommended Day 'n' Nite. 

---

## 6. Limitations and Bias 

VibeTrack 1.0 has a small dataset of only 15 songs, which limits the variety of recommendations that it can provide. Some genres have only one or two songs, which makess it difficult to provide different recommendations for those preferences. Another weakness is that songs can receive high scores based on energy even when they do not match the user's preferred genre or mood, as it was seen with Storm Runner in my experiments. Another thing is that the system also does not consider listening history, or favorite artists.

---

## 7. Evaluation

### Step 1: Diverse User Profile Testing

I tested VibeTrack 1.0 using three different user profiles: High Energy Pop, Moody Hip Hop, and Conflicting Preferences.
The High-Energy Pop profile recommended Sunrise City first with a score of 6.84 because it matched the user's preferred genre and mood while also having high energy. The Moody Hip-Hop profile recommended Day 'n' Nite first with a score of 6.42 because it matched both hip-hop and moody preferences. The Conflicting Preferences profile recommended Heartless first with a score of 6.72 because it matched hip-hop, sad mood, and had energy close to the user's target.
One interesting result was that Storm Runner appeared in multiple recommendation lists even though it did not match the preferred genre or mood. This happened because its energy score was high. This shows that numerical features can influence recommendations even when other preferences don't match.

### Terminal Results

```text
Loaded songs: 15

=============================================
PROFILE: High-Energy Pop
User preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 0.9}
=============================================
Sunrise City - Score: 6.84
Because: Genre match (+3 points); Mood match (+2 points); Energy close (+1.84 points)

Gym Hero - Score: 4.94
Because: Genre match (+3 points); Energy close (+1.94 points)

Rooftop Lights - Score: 3.72
Because: Mood match (+2 points); Energy close (+1.72 points)

Storm Runner - Score: 1.98
Because: Energy close (+1.98 points)

Flashing Lights - Score: 1.82
Because: Energy close (+1.82 points)


=============================================
PROFILE: Moody Hip-Hop
User preferences: {'genre': 'hip-hop', 'mood': 'moody', 'energy': 0.4}
=============================================
Day 'n' Nite - Score: 6.42
Because: Genre match (+3 points); Mood match (+2 points); Energy close (+1.42 points)

Heartless - Score: 4.28
Because: Genre match (+3 points); Energy close (+1.28 points)

Flashing Lights - Score: 4.18
Because: Genre match (+3 points); Energy close (+1.18 points)

Nights - Score: 3.36
Because: Mood match (+2 points); Energy close (+1.36 points)

Night Drive Loop - Score: 3.30
Because: Mood match (+2 points); Energy close (+1.30 points)


=============================================
PROFILE: Conflicting Preferences
User preferences: {'genre': 'hip-hop', 'mood': 'sad', 'energy': 0.9}
=============================================
Heartless - Score: 6.72
Because: Genre match (+3 points); Mood match (+2 points); Energy close (+1.72 points)

Flashing Lights - Score: 4.82
Because: Genre match (+3 points); Energy close (+1.82 points)

Day 'n' Nite - Score: 4.58
Because: Genre match (+3 points); Energy close (+1.58 points)

Storm Runner - Score: 1.98
Because: Energy close (+1.98 points)

Gym Hero - Score: 1.94
Because: Energy close (+1.94 points)
```

### Step 2: Accuracy and Surprises

Heartless ranked first for the Conflicting Preferences profile because it matched both the genre and mood preferences while also having a close energy match.
The profile preferences were hip-hop, sad, and energy 0.9. Heartless has the hip-hop genre, sad mood, and an energy level of 0.76.
Using the scoring rules in `recommender.py`:

1. Genre: Hip-hop matches, earning 3 points.
2. Mood:Sad matches, earning 2 points.
3. Energy: 2 × (1 − |0.9 − 0.76|) = 1.72 points.
4. Acoustic: No acoustic preference was specified, so it earns 0 points.
Total score: 3 + 2 + 1.72 = 6.72 points.

Heartless ranked above the other songs because no other song matched both hip-hop and sad. Flashing Lights scored 4.82, while Day 'n' Nite scored 4.58. This shows how matching multiple user preferences can give a song a higher recommendation score.

### Step 3: Small Data Experiment

For this experiment, I doubled the importance of energy and cut the importance of genre in half. The original genre weight was 3 points, and it changed to 1.5 points. The original energy weight was 2 points, and it changed to 4 points. I kept the mood and acoustic weights the same.
After running the program , I saw that some song rankings changed. For example, Rooftop Lights moved above Gym Hero in the High-Energy Pop profile, and Nights moved above Heartless in the Moody Hip-Hop profile. However, the first-place song remained the same for all three profiles.
This experiment showed me that changing the scoring weights affects the rankings and makes energy more influential. The recommendations became different.

### Step 4: Comparing User Profiles

**High-Energy Pop vs. Moody Hip-Hop:**

The High-Energy Pop profile recommended Sunrise City, while the Moody Hip-Hop profile recommended Day 'n' Nite. This makes sense because the first profile prefers happy pop music with high energy, while the second prefers moody hip-hop with lower energy.

**High-Energy Pop vs. Conflicting Preferences:**

The High-Energy Pop profile recommended Sunrise City, while the Conflicting Preferences profile recommended Heartless. Both profiles prefer high energy, but their genre and mood preferences are different. This shows that genre and mood help influence which songs are recommended.

**Moody Hip-Hop vs. Conflicting Preferences:**

The Moody Hip-Hop profile recommended Day 'n' Nite, while the Conflicting Preferences profile recommended Heartless. Both profiles prefer hip-hop, but one prefers a moody feeling with lower energy, while the other prefers a sad mood with higher energy. These differences explain why different songs ranked first.
Overall, testing these three profiles showed me that changing a user's music preferences can change the recommendations. It also showed me that the scoring weights influence which songs appear at the top.

---


## 8. Future Work  

In the future, I would like to expand the dataset with more songs and genres to provide better recommendations. I would also like to include listening history and additional song features. Another improvement would be to make the recommendations more diverse so users do not repeatedly get songs from the same genre or the same artist. I could also improve the scoring system to better balance genre, mood, and energy.

---

## 9. Personal Reflection

My biggest learning moment was seeing how changing the scoring points for genre, mood, and energy can change the song recommendations. I learned how a recommendation system uses a user's preferences to choose songs.

AI tools helped me understand my code, fix errors, and find weaknesses in my project. However, I had to double-check the AI's suggestions by looking at my code and running tests to make sure everything worked correctly.

I was surprised that a simple scoring system could recommend different songs based on a person's music preferences. It helped me understand how music apps can suggest songs that users might enjoy.

If I continued this project, I would add more songs, include more music features, and use listening history to improve the recommendations. Overall, this project helped me understand how recommendation systems work and how AI can help with programming.
