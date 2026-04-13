from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    user_profiles = [
        {
            "name": "High-Energy Pop",
            "prefs": {
                "genre": "pop",
                "mood": "happy",
                "energy": 0.9,
                "valence": 0.85,
                "danceability": 0.85,
                "acousticness": 0.2
            }
        },
        {
            "name": "Chill Lofi",
            "prefs": {
                "genre": "lofi",
                "mood": "chill",
                "energy": 0.4,
                "valence": 0.6,
                "danceability": 0.5,
                "acousticness": 0.8
            }
        },
        {
            "name": "Intense Rock",
            "prefs": {
                "genre": "rock",
                "mood": "intense",
                "energy": 0.95,
                "valence": 0.5,
                "danceability": 0.6,
                "acousticness": 0.1
            }
        }
    ]

    for profile in user_profiles:
        print(f"\n=== {profile['name']} ===\n")

        recommendations = recommend_songs(profile["prefs"], songs, k=5)

        for song, score, explanation in recommendations:
            print(f"{song['title']}  |  Score: {score:.2f}")
            print("Reasons:")
            for reason in explanation.split(", "):
                print(f"  - {reason}")
            print("-" * 40)


if __name__ == "__main__":
    main()