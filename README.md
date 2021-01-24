# Flexi Lunch Recommender Model

Imagine you are an office worker. You’ve been thinking of getting a burger for lunch for the whole morning.  You arrive at Five Guys at 12:30pm, just to discover the queue is very long. You really want a burger (no McDonald’s please…). What will you do?

Try out this “Flexi-Lunch” recommendation model!

The dataset is web-scraped from [Openrice HK’s reviews page](https://www.openrice.com/en/hongkong/restaurant/review/index.htm?tc=bc). It contains 2,600+ reviews on users' lunch experience of 900+ restaurants in HK's prime business districts from 2009 to 2019.  

This project has four main steps:

### Web scraping

* Reviews scrapping (2,600 rows): Captures info including restaurant name, district, cuisine, rating, cost, wait time, review, and restaurant link
* Include only reviews for lunch and with meal spending data
* Since Openrice displays max 17 pages of search result, I broke down the searches to 5 popular cuisines (i.e. Japanese, Chinese, Thai, Italian, American) for all 4 districts

### Text Analysis

* Summarization: Use `CountVectorizer` to identify the sentence in each review that contains the most frequently-appeared words.  Make this sentence a one-line comment highlight.  Add it to the data frame’s new column, “summary”.
* Word Cloud: Quickly find out key words that customers like about the top 10 restaurants !

### Sentiment predictor

* Train a model that classifies the sentiment (positive or negative) of the review.  
* Retain only reviews that have ratings.  Define rating >= 3 as “Good” sentiment.  
* Three models are tested — 1) Multinomial Naive Bayes Classifier (Accuracy: 0.79); 2) Random Forest (0.77); 3) Gradient Boosting (0.83)
* Use Gradient Boosting Classifier to predict the sentiment of a new comment

### Recommendation model

* Transform the original review-based data frame (2,600 rows) into restaurant-based (900 rows). Reviews of the same restaurant are merged into one.  Ratings, wait time, and meal cost are averaged.
* Use `CountVectorizer` to break down reviews to words and count frequencies
* Find the most similar restaurants base on cosine similarity
* Generate 10 most similar restaurants with useful information (e.g, wait time, cost)

Now, you can find nearby burger places that are good alternatives to Five Guys! You can make a wise decision base on the average wait time, cost, and rating from Openrice reviews.
