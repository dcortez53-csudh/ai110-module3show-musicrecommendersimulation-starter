import csv

def load_songs(filepath):
    """Loads songs from a CSV file and converts numerical values to floats/ints."""
    songs = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert the number strings into actual numbers so we can do math
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = int(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    return songs

def score_song(user_prefs, song):
    """Calculates a relevance score and a list of reasons for a single song."""
    score = 0.0
    reasons = []

    # 1. Genre Match (+2.0)
    if song['genre'].lower() == user_prefs['favorite_genre'].lower():
        score += 2.0
        reasons.append("Genre match (+2.0)")

    # 2. Mood Match (+1.0)
    if song['mood'].lower() == user_prefs['favorite_mood'].lower():
        score += 1.0
        reasons.append("Mood match (+1.0)")

    # 3. Energy Similarity (Max +1.0)
    # We calculate the absolute difference (gap) between the song and user's target.
    energy_gap = abs(song['energy'] - user_prefs['target_energy'])
    energy_score = 1.0 - energy_gap
    score += energy_score
    reasons.append(f"Energy similarity (+{energy_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs, songs, k=5):
    """Ranks all songs by score and returns the top K recommendations."""
    scored_songs = []
    
    for song in songs:
        # Get the score and reasons for this specific song
        score, reasons = score_song(user_prefs, song)
        # Save the song data along with its score and reasons
        scored_songs.append({
            'song': song,
            'score': score,
            'reasons': reasons
        })
        
    # Sort the list of dictionaries by score, in descending order (highest first)
    ranked_songs = sorted(scored_songs, key=lambda x: x['score'], reverse=True)
    
    # Return only the top K results
    return ranked_songs[:k]