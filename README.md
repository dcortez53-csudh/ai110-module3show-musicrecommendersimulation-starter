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
The system uses a weighted scoring algorithm to judge every song in the catalog:
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
