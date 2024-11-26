from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)

    sentiment = blob.sentiment
    polarity = sentiment.polarity

    if polarity > 0 :
        sentiment_cat = "Positive"
    elif polarity < 0 :
        sentiment_cat = "Negative"
    else:
       sentiment_cat = "Neutral"

    return sentiment_cat

text = input("Enter your text: ")
result = analyze_sentiment(text)
print(f"Sentiment: {result}")