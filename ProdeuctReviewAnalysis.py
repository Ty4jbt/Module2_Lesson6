# Task 1
# A list of reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

# Keywords to capitalize
keywords = ["good", "excellent", "bad", "poor", "average"]

# Function to capitalize keywords
def capitalized_keywords(reviews, keywords):

    # List to store modified reviews
    capitalized_reviews = []

    # Capitalize keywords in reviews
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        capitalized_reviews.append(review)
    return capitalized_reviews

# Variable to hold the output of the capitalized_keywords function
modified_reviews = capitalized_keywords(reviews, keywords)

# Prints each instance of the modified reviews
for review in modified_reviews:
    print(review)

# Task 2
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentiment_tally(reviews, positive_words, negative_words):
    # Initialize counters for positive and negative reviews
    positive_count = 0
    negative_count = 0

    # Check each review for positive and negative words
    for review in reviews:
        # Formats the keywords
        words = [word.lower() for word in review.split()]
        
        # Check for positive words
        positive_count += sum(word in positive_words for word in words)

        # Check for negative words
        negative_count += sum(word in negative_words for word in words)

    return positive_count, negative_count

# Call the sentiment_tally function and print the results
positive_count, negative_count = sentiment_tally(reviews, positive_words, negative_words)

print("The sentiment tally is...")
print(f"Positive words: {positive_count}")
print(f"Negative words: {negative_count}")

# Task 3
# Function to summarize reviews
def review_summary(review):

    # Remove leading and trailing whitespaces
    review = review.strip()

    # If the review is already short, return it as is
    if len(review) <= 30:
        return review

    # If the review is longer than 30 characters, shorten it
    short_review = review[:30]

    # Check if the last character is a space
    if short_review[-1] != " ":

        # Find the last space in the shortened review
        last_space_index = short_review.rfind(" ")

        # If a space is found, shorten the review to the last space
        if last_space_index != -1:
            short_review = short_review[:last_space_index]

    # Return the shortened review with an ellipsis and if the last character is a period, remove it
    return short_review.rstrip('.') + "..."

# Print the summary of each review
for review in reviews:
    print(review_summary(review))