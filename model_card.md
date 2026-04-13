# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch 1.0**  

---

## 2. Intended Use  

This recommender is designed to suggest songs based on a user’s preferences such as genre, mood, and energy. It assumes that users have clear taste preferences that can be represented using a few features.

This system is built for classroom exploration to understand how basic recommendation systems work, not for real-world deployment.

---

## 3. How the Model Works  

The model uses features like genre, mood, energy, valence, danceability, and acousticness to represent each song. The user provides preferences for these features, such as preferred genre and target energy level.

The system assigns a score to each song by giving higher points for matching genre and mood, and by calculating similarity scores for numerical features like energy and valence. Songs that are closer to the user’s preferences receive higher scores.

Finally, all songs are ranked based on their scores, and the top results are recommended.

---

## 4. Data  

The dataset contains around 20 songs with different genres such as pop, lofi, rock, jazz, EDM, and more. It includes features like mood, energy, valence, danceability, and acousticness.

I expanded the dataset by adding more songs to increase diversity. However, the dataset is still small and does not include all types of music or deeper features like lyrics or user behavior.

---

## 5. Strengths  

The system works well for users with clear and consistent preferences, such as high-energy or chill music listeners. It correctly captures patterns like high-energy songs for energetic profiles and low-energy songs for relaxed profiles.

In many cases, the recommendations matched my intuition, especially for profiles like Chill Lofi and Intense Rock.

---

## 6. Limitations and Bias 

This recommender system has a few limitations due to its simple scoring logic and small dataset. First, it tends to over-prioritize certain features like genre or energy depending on the assigned weights, which can create a “filter bubble” where similar types of songs are repeatedly recommended.

Second, the system relies only on a limited set of features (genre, mood, and numerical attributes) and does not consider deeper aspects like lyrics, context, or user listening history. This can lead to less personalized or sometimes misleading recommendations.

Finally, because the dataset is small and not fully diverse, the system may favor certain genres more often and fail to provide a wide variety of suggestions. 

---

## 7. Evaluation  

I tested the recommender using three different user profiles: High-Energy Pop, Chill Lofi, and Intense Rock. For each profile, I checked whether the top recommended songs matched the expected vibe based on genre, mood, and energy.

The results mostly matched my expectations. For example, High-Energy Pop recommended upbeat and energetic songs, while Chill Lofi showed slower and more acoustic tracks. Intense Rock prioritized high-energy and intense songs.

One surprising observation was that some songs ranked high even without matching the genre because their numerical features (like energy and valence) were very close to the user’s preferences. This shows that the system relies heavily on similarity scores.

I also ran a small experiment by increasing the weight of energy and reducing genre importance. This caused songs with closer energy levels to rank higher, even if they did not match the genre, making the recommendations more diverse but sometimes less accurate.

---

## 8. Future Work  

Add more songs and genres to improve diversity
Include user listening history for better personalization
Improve scoring by dynamically adjusting weights
Add advanced features like lyrics sentiment or artist similarity

---

## 9. Personal Reflection  

Through this project, I learned how simple scoring rules can simulate recommendation systems. It was interesting to see how small changes in weights can significantly affect the results.

One surprising aspect was that even a simple system can produce recommendations that feel realistic. This helped me better understand how apps suggest music and how bias can be introduced through feature weighting. 
