from textblob import TextBlob

def analyze_sentiment(text: str) -> str:
    """
    Analyze the sentiment of the given text.
    
    Args:
        text (str): The text to analyze.

    Returns:
        str: Sentiment category (Positive, Negative, or Neutral).
    """
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    print("Welcome to the Sentiment Analysis Program!")
    while True:
        user_input = input("\nEnter a sentence to analyze (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        sentiment = analyze_sentiment(user_input)
        print(f"The sentiment of your sentence is: {sentiment}")

if __name__ == "__main__":
    main()
