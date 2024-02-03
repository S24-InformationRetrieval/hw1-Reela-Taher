from elasticsearch import Elasticsearch 
from parser import parse_docs, stop_words

es = Elasticsearch(['http://localhost:9200/'])

index_name = "ap89"

# Index settings
ap89_index = {
  "settings": { # Reduces resource usage
    "analysis": {
      "filter": {
        "english_stop": {
          "type": "stop",
          "stopwords": stop_words # Custom stop filter using predefined stopwords 
        }
      },
      "analyzer": { 
        "stopped": {
           "type": "custom",
           "tokenizer": "standard",
           "filter": [
             "lowercase",
             "english_stop"
           ]
        }
      }
    }
  },
  "mappings": { # Field data enabled for sorting and aggregations
    "properties": {
      "text": {
        "type": "text",
        "analyzer": "stopped", 
        "index_options": "positions"  
      }
    }
  }
}

# es.indices.create(index=index_name, body=ap89_index)

# Parse documents
docs = parse_docs() 

# Index documents
for doc in docs:
  es.index(index=index_name, body=doc, id=doc['DOCNO'])
  