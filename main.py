
print("================================")
print("      SENTIMENT ANALYZER")
print("================================")

review = input("Enter your review: ")
review = review.lower()

negative_phrases = ["not good", "not great", "not excellent", "not love"]

if any(phrase in review for phrase in negative_phrases):
    print("Sentiment: Negative 😞")

elif any(word in review for word in ["good", "great", "excellent", "love"]):
    print("Sentiment: Positive 😊")

elif any(word in review for word in ["bad", "worst", "poor", "hate"]):
    print("Sentiment: Negative 😞")

else:
    print("Sentiment: Neutral 😐")
