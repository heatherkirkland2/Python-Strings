# Product Review Analysis
# Task 1: Keyword Highlighter

# Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
#     reviews = [
#        "This product is really good. I'm impressed with its quality.",
#        "The performance of this product is excellent. Highly recommended!",
#        "I had a bad experience with this product. It didn't meet my expectations.",
#        "Poor quality product. Wouldn't recommend it to anyone.",
#        "The product was average. Nothing extraordinary about it."
#    ]
# So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

# Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.
#    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
#    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
# Task 3: Review Summary

# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

# Example: "This product is really good. I'm...",

# Task 1: Keyword Highlighter
def highlight_keywords(reviews):
    keywords = ["good", "excellent", "bad", "poor", "average"]
    highlighted_reviews = []
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        highlighted_reviews.append(review)
    return highlighted_reviews

# Task 2: Sentiment Tally
def sentiment_tally(reviews, positive_words, negative_words):
    tally = []
    for review in reviews:
        pos_count = sum(review.lower().count(word) for word in positive_words)
        neg_count = sum(review.lower().count(word) for word in negative_words)
        tally.append((pos_count, neg_count))
    return tally

# Task 3: Review Summary
def create_summary(reviews):
    summaries = []
    for review in reviews:
        words = review[:30].split()
        if len(words[-1]) + len(' '.join(words[:-1])) > 30:
            summary = ' '.join(words[:-1])
        else:
            summary = ' '.join(words)
        summaries.append(summary + "...")
    return summaries

# Sample data
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Execute tasks
highlighted_reviews = highlight_keywords(reviews)
sentiment_counts = sentiment_tally(reviews, positive_words, negative_words)
review_summaries = create_summary(reviews)

# Print results
print("Highlighted Reviews:")
for review in highlighted_reviews:
    print(review)

print("\nSentiment Tally (Positive, Negative):")
for count in sentiment_counts:
    print(count)

print("\nReview Summaries:")
for summary in review_summaries:
    print(summary)
