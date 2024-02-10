# ES built-in to Read and Run All Queries

# Required Imports
from index import index_name, es
from parser import parser, stop_words
import string

# Path to the directory containing the query file
query_path = '/Users/reelataher/hw1-Reela-Taher/IR_data/AP_DATA/query_desc.51-100.short.txt'

# Function to read and return queries from txt file
def read_query(filename):
    
    # Initializes a list variable for all queries
    queries = []
    
    # Read query file line by line
    with open(filename, 'r') as file:
        
        for line in file:

            # Skip any blank lines
            if not line.strip(): 
                continue
            
            # Split each line on a period to separate the number and text
            attributes = line.split('.', 1)
            
            # Appends stored attributes of each query within list of queries
            query_number = attributes[0].strip()
            query = attributes[1].strip()

            queries.append((query_number, query))
    
    return queries

# Function to preprocess queries
def process_queries(queries):
    
    processed_queries = []
    
    for query in queries:
        
        # Lowercase + remove punctuation
        query = query.lower()
        query = query.translate(str.maketrans('', '', string.punctuation))
        
        # Stem each query
        words = query.split() 
        stemmed_words = [parser.stem(word) for word in words]
        filtered_words = [word for word in stemmed_words if word not in stop_words]
        
        # Join back into a string
        processed_query = ' '.join(filtered_words)
        processed_queries.append(processed_query)
        
    return processed_queries

# Search Elasticsearch index using match query 
def es_search(query):
    
    # Send match query to Elasticsearch
    result = es.search(index=index_name, body={'query': {'match': {'content': query}}})
    
    # Get the hits from the returned result 
    hits = result['hits']['hits']
    
    # Return the hits
    return hits


# Process results from ES with specified format
def process_results(query_number, query):
  
  # Get hits from search function
  hits = es_search(query)
  
  output = []

  # Iterate through the hits 
  for hit in hits:

    # Define values for attributes within output line
    rank = 1
    docno = hit['_source']['DOCNO']
    score = hit['_score']
    
    # Create output line with appropriate inputs variables above
    output_line = f"{query_number} Q0 {docno} {rank + 1} {score} Exp\n"
    output.append(output_line)

    # Runs until there are 1000 results for each query
    if rank > 1000:
        break
  
  # Return complete output with all formatted lines
  return output

# Defines directory to add new file
output_path = '/Users/reelataher/hw1-Reela-Taher/Deliverables'

# Takes output string from search and writes it to a text file in the specified output directory
def output_txt(filename, results):
    with open(output_path + '/'+ filename + '.txt', 'w') as file:
        for line in results:  
            file.write(line)

# TESTING
queries = read_query(query_path)
print(queries)
  
#   hits = es_search(query)

#   query_results = process_results(query_number, query)

#   results.extend(query_results)

# # Output results
# output_file = "query_ES_builtin"#
# output_txt(output_file, results)

# print('Output Completed')
