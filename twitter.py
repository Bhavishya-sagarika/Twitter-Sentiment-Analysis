import pandas as pd
from textblob import TextBlob
import re

# Clean tweet text
def clean_tweet(text):
    text = re.sub(r'RT[\s]+', '', text)
    text = re.sub(r'https?:\/\/\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'[^A-Za-z ]+', '', text)
    return text.lower().strip()

# Sentiment using TextBlob
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Sample tweets (you can add your own)
tweets = [
    "I love the new AI tools!",
    "This update is so bad!",
    "I am not sure how to feel about this.",
    "What a wonderful day!",
    "This service is terrible."
]

data = []

for t in tweets:
    cleaned = clean_tweet(t)
    sentiment = get_sentiment(cleaned)
    data.append([t, cleaned, sentiment])

df = pd.DataFrame(data, columns=["Original Tweet", "Cleaned Tweet", "Sentiment"])

print(df)

df.to_csv("sentiment_output.csv", index=False)
print("\n✔ Saved to sentiment_output.csv")

