[Topic Modeling in Python: Latent Dirichlet Allocation (LDA)](https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0)
(How to get started with topic modeling using LDA in Python)




<u></u>
## Topic Modeling
Topic Model are a type of <u>statistical language models</u> used for uncovering hidden structure in a collection of texts. It can be used in:

1. **Dimensionality Reduction**
   representing a text _T_ in a topic space as <u>{Topic_i: Weight(Topic_i, T) for Topic_i in Topics}</u>, rather than <u>{Word_i: count(Word_i, T) for Word_i in Vocabulary}</u>

2. **Unsupervised Learning**
   Different from clustering. In the case of clustering, the number of topics, like the number of clusters, is an output parameter.
   But by doing topic modeling, we build <u>clusters of words</u> rather than <u>clusters of texts</u>. A text is thus a mixture of all the topics, each having a specific weight

3. **Tagging**
   abstract “topics” that occur in a collection of documents that best represents the information in them.



#### Several methods to perform the topic modeling
- Latent Semantic Analysis (LSA/LSI)
- Probabilistic Latent Semantic Analysis (pLSA)
- Latent Dirichlet Allocation (LDA)


## LDA
LDA is a <u>generative probabilistic model</u> that **assumes 
	1. each topic is a mixture over an underlying set of words
	2. each document is a mixture of over a set of topic probabilities.**
![](https://raw.githubusercontent.com/HenryVarro666/images/master/images/202205011542264.png)


###  Generative process
 given the _M_ number of documents, _N_ number of words, and prior _K_ number of topics, the model trains to output:
 - _psi_, the distribution of words for each topic _K_
 - _phi_, the distribution of topics for each document _i_

### Parameters of LDA
**Alpha parameter** is Dirichlet prior concentration parameter that represents document-topic density — with _a higher alpha, documents are assumed to be made up of more topics and result in more specific topic distribution per document._

**Beta parameter** is the same prior concentration parameter that represents topic-word density — _with high beta, topics are assumed to made of up most of the words and result in a more specific word distribution per topic._

 
### LDA Implementation
#### Loading data 
#### Data cleaning 
- Focus only on the text data from each paper, and drop other metadata columns
- Remove punctuation/lower casing

#### Exploratory analysis    
   To verify whether the preprocessing, we’ll make a word cloud using the wordcloud package to get a visual representation of most common words. It is key to understanding the data and ensuring we are on the right track, and if any more preprocessing is necessary before training the model.

#### Preparing data for LDA analysis 
   Transform the textual data in a format that will serve as an input for training LDA model.
	1. Tokenize the text
	2. Removing stopwords
	3. Convert the tokenized object into a corpus and dictionary

#### LDA model training 
To keep things simple, we’ll keep all the parameters to default except for inputting the number of topics. For this tutorial, we will build a model with 10 topics where each topic is a combination of keywords, and each keyword contributes a certain weightage to the topic.

#### Analyzing LDA model results
Now that we have a trained model let’s visualize the topics for interpretability. To do so, we’ll use a popular visualization package, <u>pyLDAvis</u> which is designed to help interactively with:
   1. Better understanding and interpreting individual topics
    manually select each topic to view its top most frequent and/or “relevant” terms, using different values of the λ parameter. This can help when you’re trying to assign a human interpretable name or “meaning” to each topic
   2. Better understanding the relationships between the topics.
	exploring the _Intertopic Distance Plot_ can help you learn about how topics relate to each other, including potential higher-level structure between groups of topics.


### Reference
https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0

[https://en.wikipedia.org/wiki/Topic_model](https://en.wikipedia.org/wiki/Topic_model)

