# AI-Auto-Publisher
This is a semi Bot I built using Python. The aim was to build an autonomous Bot which collects keywords from a search engine (Google for example) and then generate an article based on a cluster of related keywords using AI and publish the articles through the REST API on Wordpress.

The Bot uses some NLP Libraries such as SpaCy and Pyrank for the purpose of entity recognition and clustering. Openai's embeddings were also used to categorize the references from which the Bot pulls facts in order to write a factual base article.

Text generation was done through Openai's API using Davinci-003 model at the start and then switched to ChatGPT 3.5.
