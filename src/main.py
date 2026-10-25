from src.recommender import load_songs, recommend_songs

def print_recommendations(profile_name, user_prefs, songs, k=3):
    print(f"\n--- {profile_name} ---")
    print(f"Target: Genre={user_prefs.get('favorite_genre', 'None')}, Mood={user_prefs.get('favorite_mood', 'None')}, Energy={user_prefs['target_energy']}")
    
    recommendations = recommend_songs(user_prefs, songs, k=k)
    for rank, item in enumerate(recommendations, start=1):
        song = item['song']
        score = item['score']
        reasons = ", ".join(item['reasons'])
        print(f"{rank}. {song['title']} (Score: {score:.2f}) - {reasons}")

def main():
    songs = load_songs('data/songs.csv')
    print(f"Loaded songs: {len(songs)}")

    # Profile 1: High-Energy Pop
    pop_profile = {"favorite_genre": "pop", "favorite_mood": "happy", "target_energy": 0.85}

    # Profile 2: Deep Intense Rock
    rock_profile = {"favorite_genre": "rock", "favorite_mood": "intense", "target_energy": 0.95}

    # Profile 3: Adversarial (Conflicting) - Wants sad metal, but low energy
    adversarial_profile = {"favorite_genre": "metal", "favorite_mood": "sad", "target_energy": 0.20}

    # Run and print for each
    print_recommendations("High-Energy Pop Fan", pop_profile, songs)
    print_recommendations("Deep Intense Rock Fan", rock_profile, songs)
    print_recommendations("Adversarial Profile (Sad Metal)", adversarial_profile, songs)

if __name__ == "__main__":
    main()