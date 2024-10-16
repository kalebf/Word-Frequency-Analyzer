import string

def open_file():
    while True:
        filename = input("Enter the name of the file to open ")
        try:
            with open(filename, 'r') as file:
                words = []
                for line in file:
                    words.extend(line.split())  # Split each line into words and add them to the list
                return words
        except FileNotFoundError:
            print(f'Could not open file {filename}\nPlease try again\n')

def clean_words(words):
    cleaned_words = []
    for word in words:
        word = word.strip(string.punctuation)  # Remove leading and trailing punctuation
        word = word.strip()  # Remove leading and trailing whitespace
        word = word.lower() # makes all words lowercase
        if len(word) > 3:
            cleaned_words.append(word)
    return cleaned_words

def get_word_counts(words): # word count for entire CSV
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def output_top_ten(word_counts): #based on repetition
    counter = 0 
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    print()
    print("Most frequently used words")
    print(f"{'#': >2}{'Word': >15}{'Freq.': >20}")
    print('=' * 37)
    for i in range(min(10, len(sorted_word_counts))):
        counter += 1
        print(f"{counter: >2}{sorted_word_counts[i][0]: >15} {sorted_word_counts[i][1]: >20}")
    return ''

def output_uniques(word_counts): #for all csv
    unique_count = sum(1 for count in word_counts.values() if count == 1)
    print(f"There are {unique_count} words that occur only once")
    print(f"There are {len(word_counts)} unique words in the document")


def main():
        file = open_file()
        words = clean_words(file)
        word_counts = get_word_counts(words)
        top_ten = output_top_ten(word_counts)
        print(top_ten)
        output_uniques(word_counts)
if __name__ == "__main__":
    main()
