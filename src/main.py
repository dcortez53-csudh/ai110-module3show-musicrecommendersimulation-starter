from src.recommender import load_songs, UserProfile, Recommender

def print_recommendations(profile_name, user_prefs, rec, k=3):
    print(f"\n--- {profile_name} ---")
    print(f"Target: Genre={user_prefs.favorite_genre}, Mood={user_prefs.favorite_mood}, Energy={user_prefs.target_energy}")

    recommendations = rec.recommend(user_prefs, k=k)
    for rank, song in enumerate(recommendations, start=1):
        score = rec.score_song(user_prefs, song)
        reasons = rec.explain_recommendation(user_prefs, song)
        print(f"{rank}. {song.title} (Score: {score:.2f}) - {reasons}")

def main():
    songs = load_songs('data/songs.csv')
    print(f"Loaded songs: {len(songs)}")
    rec = Recommender(songs)

    pop_profile = UserProfile(favorite_genre="pop", favorite_mood="happy", target_energy=0.85)
    rock_profile = UserProfile(favorite_genre="rock", favorite_mood="intense", target_energy=0.95)
    adversarial_profile = UserProfile(favorite_genre="metal", favorite_mood="sad", target_energy=0.20)

    print_recommendations("High-Energy Pop Fan", pop_profile, rec)
    print_recommendations("Deep Intense Rock Fan", rock_profile, rec)
    print_recommendations("Adversarial Profile (Sad Metal)", adversarial_profile, rec)

if __name__ == "__main__":
    main()