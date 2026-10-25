# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
VibeFinder 1.0  

---

## 2. Intended Use  

This recommender is designed for classroom exploration to demonstrate how content-based filtering works. It generates a list of top 5 songs based on a single user's explicity preferences (genre, mood, energy). It assumes the user has a static, well-defined taste profile and is meant for educational simulation, not real-world production.

---

## 3. How the Model Works  

The model looks at three features of each song: genre, mood, and energy. It compares these to the user's preferences. It gives +2.0 points if the genre mathces, +1.0 point if the mood matches, and up to +1.0 point based on how close the song's energy level is to the user's target energy. The model then ranks all the songs by their total score to find the top recommendations. I changed the starter logic by implementing a mathematical gap calculation for energy instead of just a binary high/low check.

---

## 4. Data  

The catalog has 16 songs. It includes a mix of pop, lofi, rock, electronic, metal, country, and classical. I added 6 new songs to the original 10 to include more genres and moods like "sad", "energetic", and "focused". Musical taste elements like lyrics, cultural context, or artist popularity are missing from this dataset.  

---

## 5. Strengths  

The system works very well for users whose tastes perfectly align with an established genre in the dataset. For example, the "High-Energy Pop" profile correctly surfaced "Gym Hero" because it matched all three criteria. The scoring captures the intuition that if you want chill lofi, you want low energy and a matching mood.  

---

## 6. Limitations and Bias 

The system heavily over-prioritizes exact genre matches because it is worth the most points (+2.0). This creates a "filter bubble": if a user's favorite genre is "pop," the system will almost exclusively recommend pop songs, completely ignoring incredible rock or electronic songs that perfectly match the user's mood and energy. Additionally, the "Energy Similarity" math rewards songs that are close to the target, but if a user has contradictory preferences (e.g., they want "sad" music but high "energy"), the system struggles to find a balance and will just default to whichever song gets the most math points.  

---

## 7. Evaluation  

I tested the system with three distinct profiles: a High-Energy Pop fan, a Deep Intense Rock fan, and an Adversarial profile (someone who wants "Sad Metal" with very low energy).

Comparing the Pop and Rock profiles, the outputs shifted drastically. The Pop profile recommended "Gym Hero" (high energy, happy pop), while the Rock profile recommended "Storm Runner" and "Heavy Metal Thunder." This makes sense because the genre and energy weights correctly aligned with those tastes.

However, the Adversarial profile produced a surprising result. Because there are no "sad metal" songs in the dataset, the system abandoned the metal genre entirely and recommended "Symphony of Sorrow" (classical/sad) and "Whiskey Tears" (country/sad). It prioritized the mood and energy preferences over the genre preference because the math for the mood (+1.0) and energy (+1.0) outweighed the missing genre points (0+).

During a data experiment, I temporarily removed the "Mood Match" logic. The recommendation for the Pop profile changed significantly; songs with the correct energy but completely wrong moods (like "Night Drive Loop" by Neon Echo) started appearing in the top results. This proved that the mood weight is critical for keeping the recommendations emotionally relevant to the user.

---

## 8. Future Work  

I would add more features like "valence" and "danceabilitiy" to the scoring logic. I would improve diversity by penalizing songs if the same artist appears multiple times in the top results. I would also handle complex user tastes by allowing multiple favorite genres.

---

## 9. Personal Reflection  

I learned that simple math can actually feel like a real recommendation system. It was interesting to see how changing just one weight (like  removing the mood check) completely changed the output. It changed how I thnk about Spotify; even simple algorithms can create a filter bubble if they weight one feature too heavily.
