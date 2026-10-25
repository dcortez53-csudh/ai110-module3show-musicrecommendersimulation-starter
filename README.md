# 🎵 Music Recommender Simulation

## Project Summary

This project is a content-based music recommender simulation. It reads a catalog of songs from a CSV file, compares their attributes (genre, mood, and energy) against a user's specific "taste profile," and calculates a numerical score for every song. The system then ranks the songs from highest to lowest score to generate a personalized top-5 recommendation list.

---

## How The System Works

Explain your design in plain language.

**Features Used:**
* **Song:** 'genre', 'mood', 'energy' (ranging from 0.0 to 1.0).
* **UserProfile:** 'favorite_genre', 'favorite_mood', 'target_energy'.

**How the Recommender Computes a Score:**
The system uses a weighted scoring algorithm to judge every son in the catalog:
1. **Genre Match:** +2.0 points if the song's genre matches the user's favorite.
2. **Mood Match:** +1.0 point if the song's mood matches the user's favorite.
3. **Energy Similarity:** Up to +1.0 point. It calculates the mathematical difference between the song's energy and the user's target energy. A perfect match gives +1.0, while a massive gap gives a much lower score.

**How Songs are Chosen:**
Every song is scored, and then the list is sorted in descending order. The top 5 songs with the highest overall scores are returned to the user.

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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Top 5 Recommendations for a 'lofi' fan:
------------------------------------------------------------
1. Midnight Coding by LoRoom
   Final Score: 3.98
   Reasons: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.98)

2. Library Rain by Paper Lanterns
   Final Score: 3.95
   Reasons: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.95)

3. Focus Flow by LoRoom
   Final Score: 3.00
   Reasons: Genre match (+2.0), Energy similarity (+1.00)

4. Spacewalk Thoughts by Orbit Bloom
   Final Score: 1.88
   Reasons: Mood match (+1.0), Energy similarity (+0.88)

5. Coffee Shop Stories by Slow Stereo
   Final Score: 0.97
   Reasons: Energy similarity (+0.97)
```

---

## Experiments You Tried

I ran an experiment testing an "Adversarial Profile" (a user who wanted "sad" music but with very high "energy"). Beacuse there are no sad/high-energy songs in the dataset, the system abandoned the user's genre entirely and recommended classical and country songs because it prioritized the mood and energy preferences over the game preference.

I also ran a data experiment where I temporarily removed the "Mood Match" logic from the code. The recommendation for a Pop profile changed significantly; songs with the correct energy but completely wrong moods started appearing the top results. This proved that the mood weight is critical for keeping recommendations emotionally relevant.
---

## Limitations and Risks

The system heavily over-prioritizes exact genre matches because it is worth the most points (+2.0). This creates a "filter bubble": if a user's favorite genre is "pop,' the system will almost exclusively recommend pop songs, completely ignoring incredible rock or electronic songs that perfectly match the user's mood and energy. Additionally, the catalog is very small (16 songs), so niche tastes are not well represented.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

My biggest learning moment was seeing how just three simple math rules (genre, mood, energy) could actually "feel" like a real recommendation system. It surprised me how much a simple algorithm can mimic a personalized experience by turning raw data into predicitons. 

This project also changed how I view apps like Spotify. Even simple algorithms can create a filter bubble if they weight one feature too heavily. If a real system over-priotizes one genre or mood, users could get trapped listening to the exact saame type of music forever, missing out on diverse new artists.

