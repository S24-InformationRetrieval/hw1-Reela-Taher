Reela Taher
Human Computer Interaction
February 14th, 2024

# Homework 1: Retrieval Models - Final Report

Score of Top Relevant File of a Sample Query for each Retrieval Model

  I am inserting the score of the top relevant file of Query 85 for each Retrieval Model.

# Retrieval Model Performance

| Model | Score |
|-|-|  
| ES (Built-In) | 14.1059885 |
| Okapi TF | 3.072789799482072 |
| TF-IDF | 28.087223197202817 | 
| Okapi BM-25 | 13.952770115593648 |
| Unigram LM with Laplace Smoothing | -42.704173982425765 |
| Unigram LM with Jelinek-Mercer Smoothing | -17.29693882233905 |


# Inference on the Above Results

I made sure that all of the documents and queries were meticulously preprocessed before the analysis to ensure consistency. Notably, I changed abbreviations like "U.S." to their full forms, like "United States", to match how often they appear in the documents. I also separated compound words within my queries that might have been seperated in the documents, which improved the results of the data recovered. Deleting the stopwords given, using a stemmer, and tokenization at white spaces were essential steps toward refining the information. To maintain consistency across models, I determined the term frequencies and document lengths prior to determining scores. This added to the precision and dependability of the relative scores across various models. To streamline the analysis and prevent long response times, I strategically structured all my functions. For example, I created each result text file in separate code blocks to avoid duplicate recalculations. This organizational approach not only optimizes efficiency but also facilitates easy retrieval and management of individual model outputs. Moreover, I implemented a process results function that formats the files to accept the specific scoring model as an input parameter, eliminating redundancy in the code. This deliberate separation of functions enhances the overall clarity and maintainability of the entire process.

# Retrieval Model Performance 

| Model | Average Precision | Precision at 10 | Precision at 30 |
|-|-|-|-|
| ES (Built-In) | **0.3008** | 0.4360 | 0.3800 |  
| Okapi TF | 0.2633 | 0.4860 | 0.3600 |
| TF-IDF | 0.2633 | 0.4880 | 0.3600 |
| Okapi BM-25 | **0.3009** | 0.4440 | 0.3880 |
| Unigram LM with Laplace smoothing | 0.2576 | 0.4160 | 0.3427 |
| Unigram LM with Jelinek-Mercer smoothing | 0.2366 | 0.3680 | 0.3253 |


# Inference on Above Retrieval Model Results 

The ES and Okapi BM25 model achieved the highest average precisions. These models probably performed the best because they incorporate term frequency weighting and length normalization, which helps match relevant documents. Both Okapi TF and TF-IDF weight terms based on their frequency within a document and inverse document frequency across the entire corpus. The main difference is Okapi TF has some minor term frequency normalization that TF-IDF does not. So their weighting and resulting rankings are very alike. This normalization and weighting improves their ranking ability over just TF-IDF alone. The language models with smoothing techniques did not perform as well as other models like ES and BM25. As we discussed in class, the smoothing probably helped with data sparsity, but the model still relies heavily on the statistics to estimate probabilities. Words and combinations might have not appeared enough times for the models to estimate accurate probabilities and relevance, ultimately resulting in lower scores.
