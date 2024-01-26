import os
from nltk.stem import PorterStemmer

# Library to remove the suffixes from an English word and obtain its stem
parser = PorterStemmer()

# Path to the directory containing the files
directory_path = '/Users/reelataher/hw1-Reela-Taher/IR_data/AP_DATA/ap89_collection'

# Loads stop words within provided file
stopword_path = '/Users/reelataher/hw1-Reela-Taher/IR_data/AP_DATA/stoplist.txt'  

with open(stopword_path) as f:
  stop_words = set(f.read().split())
  
# Set stopwords to list
stop_words = list(stop_words)

# Function to parse all documents within directory
def parse_docs():

  # Initialize dictionary to input all extracted documents
  documents = []
  
  # Store all files within a variable using the os module
  for filename in os.listdir(directory_path):
  
    # Construct the full path of the file
    file_path = os.path.join(directory_path, filename)
    
    # Open each file in the ap89_collection directory for reading
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
    
      # Initialize what one document should contain, document ID and body
      single_doc = {'DOCNO': '', 'text': ''}
      texts = []
      inside_text = True
      current_text = ''
      
      # Parsing every individual file
      for line in file:
      
        # Checks if this is the beginning of a document and initializes an empty dictionary
        if line.startswith('<DOC>'):
          single_doc = {'DOCNO': '', 'text': ''} 
          texts = []
          
        # Reads that this is the document ID and stores this in a variable
        elif line.startswith('<DOCNO>'):
          single_doc['DOCNO'] = line[8:].strip()
        
        # Reads that this is the body of the document and appends found text
        elif line.startswith('<TEXT>'):
          inside_text = True
          current_text = ''
        
        # Reads that this is the end of the document and stores the final content
        elif line.startswith('</TEXT>'):
          inside_text = False
          texts.append(current_text.strip())

        elif inside_text:
          current_text += line + ' '
        
        # Reads that this is the end of the document and stems all wards user parser
        elif line.startswith('</DOC>'):
            single_doc['text'] = parser.stem(' '.join(texts)) 
            documents.append(single_doc)

  # Returns dictionary of all parsed documents
  return documents


