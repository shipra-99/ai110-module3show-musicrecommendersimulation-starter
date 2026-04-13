# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

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

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
