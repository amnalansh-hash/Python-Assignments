# Step 1: Preloaded Feedbacks
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Ana', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support,   not happy   ',
        'GREAT experience! will come again.',
        'okay   okay...',
        ' not   BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

print(feedback_data)

# Step 2: Add More Feedbacks
n = int(input("How many more feedbacks do you want to add? "))

for i in range(n):
    print("Feedback", i + 1)
    name = input("Enter name: ")
    text = input("Enter feedback: ")

    rating = int(input("Enter rating (1-5): "))
    while rating < 1 or rating > 5:
        print("Rating must be between 1 and 5.")
        rating = int(input("Enter rating (1-5): "))

    new_sno = len(feedback_data['S_No']) + 1

    feedback_data['S_No'].append(new_sno)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(text)
    feedback_data['Rating'].append(rating)

print(feedback_data)

# Step 3: Text Cleaning
cleaned_feedback = []

for text in feedback_data['Feedback']:
    # Remove punctuation
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('!', '')
    text = text.replace('?', '')

    # Convert to lowercase
    text = text.lower()

    # Remove extra spaces (split() also strips the ends, join() puts back single spaces)
    text = ' '.join(text.split())

    cleaned_feedback.append(text)

feedback_data['Feedback'] = cleaned_feedback

print(feedback_data['Feedback'])

# Step 4: Word Count Insights
def count_word_in_feedbacks(word):
    count = 0
    for text in feedback_data['Feedback']:
        if word.lower() in text.lower().split():
            count = count + 1
    return count

print("Number of feedbacks containing 'good':", count_word_in_feedbacks("good"))
print("Number of feedbacks containing 'poor':", count_word_in_feedbacks("poor"))
print("Number of feedbacks containing 'excellent':", count_word_in_feedbacks("excellent"))

# Step 5: Final Summary & Insights

# 1. Display the final cleaned feedback_data
print("Final Feedback Data:")
for key in feedback_data:
    print(key, ":", feedback_data[key])

# 2. Average rating
average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print("Average Rating:", round(average_rating, 2))

# 3. Feedback with the longest comment (by word count)
longest_index = 0
max_words = 0
for i in range(len(feedback_data['Feedback'])):
    word_count = len(feedback_data['Feedback'][i].split())
    if word_count > max_words:
        max_words = word_count
        longest_index = i

print("Longest feedback:", feedback_data['Feedback'][longest_index])
print("By:", feedback_data['Name'][longest_index], "| Words:", max_words)

# 4. Unique words across all feedbacks
unique_words = set()
for text in feedback_data['Feedback']:
    for word in text.split():
        unique_words.add(word)

print("Unique words:", sorted(unique_words))

# 5. (Optional) Sort feedbacks by rating, highest to lowest
combined = zip(feedback_data['Rating'], feedback_data['Name'], feedback_data['Feedback'])
sorted_feedbacks = sorted(combined, reverse=True)

print("Feedbacks sorted by rating (highest to lowest):")
for rating, name, text in sorted_feedbacks:
    print(rating, "-", name, "-", text)