
import pickle

with open("sentiment_model.pkl", "rb") as file:
    model = pickle.load(file)

print("==============================")
print("   SENTIMENT ANALYZER - ML")
print("==============================")

negative_phrases = [
    "not good", "not great", "not excellent",
    "do not like", "don't like", "not happy",
    "not worth", "poor quality", "very bad",
    "terrible", "worst", "hate",
    "disappointed", "awful", "stopped working",
    "bad service", "do not recommend"
]

positive_phrases = [
    "good", "great", "excellent", "amazing",
    "wonderful", "love", "fantastic",
    "perfect", "happy", "recommend"
]

neutral_phrases = [
    "will arrive", "arrived yesterday",
    "arrived today", "received the order",
    "package contains", "available in",
    "contains a user manual", "has three buttons",
    "weighs two kilograms", "delivered at",
    "has a serial number", "made of cardboard"
]

while True:
    review = input("\nEnter a review (or type 'exit' to stop): ")

    if review.strip().lower() == "exit":
        print("Thank you for using Sentiment Analyzer!")
        break

    text = review.lower().strip()

    # Check negative phrases first
    if any(phrase in text for phrase in negative_phrases):
        prediction = "negative"

    # Then check neutral phrases
    elif any(phrase in text for phrase in neutral_phrases):
        prediction = "neutral"

    # Then check positive phrases
    elif any(phrase in text for phrase in positive_phrases):
        prediction = "positive"

    # Use ML model for other reviews
    else:
        prediction = model.predict([review])[0]

    print("Predicted Sentiment:", prediction.upper())
