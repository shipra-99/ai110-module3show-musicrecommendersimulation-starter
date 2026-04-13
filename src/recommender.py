from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    """
    songs = []

    with open(csv_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Compute score and reasons for a song based on user preferences."""
    score = 0.0
    reasons = []

    # Genre match
    if song["genre"] == user_prefs["genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match
    if song["mood"] == user_prefs["mood"]:
        score += 1.5
        reasons.append("mood match (+1.5)")

    # Energy similarity
    energy_diff = abs(song["energy"] - user_prefs["energy"])
    energy_score = 1 - energy_diff
    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    # Valence similarity
    valence_diff = abs(song["valence"] - user_prefs.get("valence", 0.5))
    valence_score = 1 - valence_diff
    score += valence_score
    reasons.append(f"valence similarity (+{valence_score:.2f})")

    # Danceability similarity
    dance_diff = abs(song["danceability"] - user_prefs.get("danceability", 0.5))
    dance_score = 1 - dance_diff
    score += dance_score
    reasons.append(f"danceability similarity (+{dance_score:.2f})")

    # Acousticness similarity
    acoustic_diff = abs(song["acousticness"] - user_prefs.get("acousticness", 0.5))
    acoustic_score = 1 - acoustic_diff
    score += acoustic_score
    reasons.append(f"acousticness similarity (+{acoustic_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    # Sort by score (highest first)
    scored_songs.sort(key=lambda x: x[1], reverse=True)

    return scored_songs[:k]
