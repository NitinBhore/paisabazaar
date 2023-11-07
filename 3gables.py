import pandas as pd
import re


# Function to count words in a file
def count_words(filename):
    word_counts = {}

    try:
        with open(filename, 'r') as file:
            # Read the content of the file
            text = file.read()

            # Tokenize the text into words
            words = re.findall(r'\b\w+\b', text.lower())

            # Count the frequency of each word
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

    return word_counts


# Replace '3gables.txt' with the path to your file
file_path = '3gables.txt'
word_counts = count_words(file_path)

# 1. Generate counts of words
print("Word Counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

# 2. Print a list of Top 5 and Bottom 5 words
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
print("\nTop 5 Words:")
for word, count in sorted_word_counts[:5]:
    print(f"{word}: {count}")

print("\nBottom 5 Words:")
for word, count in sorted_word_counts[-5:]:
    print(f"{word}: {count}")

# 3. Create a pandas data frame with words and their counts
df = pd.DataFrame(sorted_word_counts, columns=['Word', 'Count'])

# 4. Remove words with count less than 5
df = df[df['Count'] >= 5]

# 5. Create a new column with a conditional
df['MoreThan5Length_And_MoreThan10Count'] = (df['Word'].apply(len) > 5) & (df['Count'] > 10)

# Display the pandas data frame
print("\nDataFrame:")
print(df)