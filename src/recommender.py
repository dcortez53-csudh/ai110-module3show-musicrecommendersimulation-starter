import csv

class Song:
    def __init__(self, id, title, artist, genre, mood, energy, tempo_bpm, valence, danceability, acousticness):
        self.id = id
        self.title = title
        self.artist = artist
        self.genre = genre
        self.mood = mood
        self.energy = energy
        self.tempo_bpm = tempo_bpm
        self.valence = valence
        self.danceability = danceability
        self.acousticness = acousticness

class UserProfile:
    def __init__(self, favorite_genre, favorite_mood, target_energy, likes_acoustic=False):
        self.favorite_genre = favorite_genre
        self.favorite_mood = favorite_mood
        self.target_energy = target_energy
        self.likes_acoustic = likes_acoustic

class Recommender:
    def __init__(self, songs):
        self.songs = songs

    def score_song(self, user, song):
        score = 0.0
        if song.genre.lower() == user.favorite_genre.lower():
            score += 2.0
        if song.mood.lower() == user.favorite_mood.lower():
            score += 1.0
        energy_gap = abs(song.energy - user.target_energy)
        score += (1.0 - energy_gap)
        return score

    def recommend(self, user, k=5):
        scored_songs = []
        for song in self.songs:
            score = self.score_song(user, song)
            scored_songs.append((score, song))
        
        scored_songs.sort(key=lambda x: x[0], reverse=True)
        return [song for score, song in scored_songs[:k]]

    def explain_recommendation(self, user, song):
        reasons = []
        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append("Genre match (+2.0)")
        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append("Mood match (+1.0)")
        energy_gap = abs(song.energy - user.target_energy)
        reasons.append(f"Energy similarity (+{1.0 - energy_gap:.2f})")
        return ", ".join(reasons)

def load_songs(filepath):
    songs = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            songs.append(Song(
                id=int(row['id']),
                title=row['title'],
                artist=row['artist'],
                genre=row['genre'],
                mood=row['mood'],
                energy=float(row['energy']),
                tempo_bpm=int(row['tempo_bpm']),
                valence=float(row['valence']),
                danceability=float(row['danceability']),
                acousticness=float(row['acousticness'])
            ))
    return songs