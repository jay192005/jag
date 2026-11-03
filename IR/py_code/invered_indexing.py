
# IR Practical No. 2
# Title: Document Retrieval Using Inverted Index

# Step 1: Import required libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Step 2: Download required NLTK datasets
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Step 3: Create documents
documents = {
    "Doc1": "The quick brown fox jumped over the lazy dog.",
    "Doc2": "The lazy dog slept in the sun.",
    "Doc3": "The fox is playing in the garden."
}

# Step 4: Initialize stop words and stemmer
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

# Step 5: Create an empty inverted index
inverted_index = {}

# Step 6: Process each document
for doc_id, text in documents.items():

    # Convert text into lowercase
    text = text.lower()

    # Tokenization
    words = word_tokenize(text)

    # Remove stop words and punctuation, then apply stemming
    for word in words:

        if word.isalpha() and word not in stop_words:

            stemmed_word = ps.stem(word)

            # Add word and document ID to inverted index
            if stemmed_word not in inverted_index:
                inverted_index[stemmed_word] = []

            if doc_id not in inverted_index[stemmed_word]:
                inverted_index[stemmed_word].append(doc_id)

# Step 7: Display inverted index
print("\nINVERTED INDEX")
print("-----------------------------")

for word, doc_ids in inverted_index.items():
    print(word, ":", doc_ids)

# Step 8: Search for a word
query = input("\nEnter a word to search: ")

# Convert query into lowercase and stem it
query = query.lower()
query = ps.stem(query)

# Step 9: Retrieve matching documents
print("\nSEARCH RESULTS")
print("-----------------------------")

if query in inverted_index:

    for doc_id in inverted_index[query]:
        print(doc_id, ":", documents[doc_id])

else:
    print("No matching documents found.")
