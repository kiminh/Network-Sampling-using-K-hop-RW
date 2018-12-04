## CODS COMAD 2019  

Network Sampling refers to the methodologies defined for preserving structural properties of the given network. In recent past


Further, 
Network Sampling is an important pre-requisite for Unsupervised Network Embedding methods. 


The datasets used for experimentation are:
* **DBLP**
* **ACM**

You can download the datasets from this [link](https://drive.google.com/file/d/1wC1A_P3Gpe9GMXiN3akHqLTTwSCpQNVC/view?usp=sharing).

- DATASET = acm/dblp
- GRAPHTYPE = star/clique
- CLASSIFICATION_METHOD = lr/nb/rf/dt

## Preparing Mapped file from unmapped [unmapped_to_mapped.py]
```
python unmapped_to_mapped.py -d ${DATASET} 	
```
## Preparing Train Dataset [create_train.py]
1. Read 'Title', 'Venue' , 'Year' & 'Author' columns for each row from the csv.
2. Checked for year prior to 2014 and 2016 for acm and dblp respectively
3. Star-based: added all title-author pairs and title-venue pairs.
   Clique-based: added all title-author pairs, author-venue pairs, and the corresponding title-venue pairs.

```
python create_train.py -d ${DATASET} -g ${GRAPHTYPE}
```

## Preparing Test Dataset [crate_test.py]
1. Read 'Title', 'Venue', 'Year' & 'Author' columns for each row from the csv.
2. For rows where year > 2013, cretaed a dictionary indexed by venue containing all the authors for that venue, a dictionary indexed by title containing all the authors for that title. Also stored a list of authors for year > 2013.
3. For rows where  year <= 2013, created a list of authors.
4. Iterated on all possible unique author-author pairs from year > 2013 (the list created in step 2) and checked following conditions: 
   a. If these two authors are connected directly to same venue
   b. If these two authors are connected directly to same title
   c. If any of the two authors are not present in train dataset (author list for year <= 2013, created in step 3)
   If none of the above three conditions are satisfied, add it to the list of test edges, otherwise not.

- For positive test edges
```
python create_test.py -d ${DATASET} 
```

- For negative test edges

```
python create_random.py -d ${DATASET} 
```

## CORPUS GENERATION and RW-k SAMPLING
```
python corpus_generate.py -d ${DATASET} --samples_length ${SAMPLES_LENGTH} --num_samples ${NUM_SAMPLES} --graphtype ${GRAPHTYPE} -k 1
```

##  EMBEDDING GENERATION
### WORD2VEC

```
python embedding_word2vec.py -f ${DATASET}/${DATASET}_sampling_1_${GRAPHTYPE}.csv
```

Here, you can generate also other embeddings like Node2Vec, Metapath2Vec and Verse for baseline comparisions.

### HADAMARD PRODUCT GENERATION FOR TEST EDGE (compute_hadamard.py)
Compute hadamard similarites of authors in test data.
```
python compute_hadamard_new.py -d ${DATASET} -m khop -k 1 -g ${GRAPHTYPE}
```

### EVALUATION OF CLASSIFICATION TASK
Evaluation:
```
python eval.py -d ${DATASET} -m ${CLASSIFICATION_METHOD} -model khop -k 1 -g ${GRAPHTYPE}
```
