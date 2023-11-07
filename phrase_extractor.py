def parse_conll(f_path):
    # Read the CONLL file and parse it into a list of (token, label) tuples
    with open(f_path, 'r') as file:
        lines = file.readlines()

    # Initialize lists to store tokens and labels
    tokens = []
    labels = []

    for line in lines:
        if line.strip():  # Skip empty lines
            parts = line.strip().split('\t')
            token, label = parts[0], parts[1]
            tokens.append(token)
            labels.append(label)

    # Combine tokens and labels into (token, label) pairs
    tok_label_list = list(zip(tokens, labels))

    return tok_label_list

def get_phrases(tok_label_list):
    # Extract SECTIONHEADER phrases from the list of (token, label) pairs
    phrases = []
    current_phrase = []

    for token, label in tok_label_list:
        if label == 'B-SectionHeader':
            # Start a new phrase
            current_phrase = [token]
        elif label == 'I-SectionHeader':
            # Continue the current phrase
            current_phrase.append(token)
        else:
            # Check if there is a current phrase
            if current_phrase:
                phrases.append(' '.join(current_phrase))
            current_phrase = []

    # Check if there is a final phrase
    if current_phrase:
        phrases.append(' '.join(current_phrase))

    return phrases

if __name__ == "__main__":
    tok_tags_1 = parse_conll('file_1.conll')
    print("File 1 Section Headers are:")
    print(get_phrases(tok_tags_1))
    # Output: ['History of Present Illness', 'BMI']

    print('')

    tok_tags_2 = parse_conll('file_2.conll')
    print("File 2 Section Headers are:")
    print(get_phrases(tok_tags_2))
    # Output: ['Name', 'Admission Date', 'SECONDARY DIAGNOSES', 'Vital Signs', 'AGE']
