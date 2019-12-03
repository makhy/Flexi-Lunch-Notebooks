# Flexi-Lunch-Recommender

Imagine you are an office worker in Wan Chai.  You’ve been thinking of getting a delicious burger for lunch for the whole morning.  You arrive at Five Guys at 12:30pm, just to discover the queue at the cashier is over half an hour long, and almost every table has a person standing at the side waiting to be seated.  You really want a burger (no McDonald’s please…), but there isn’t much time left for the lunch hour.  What will you do?

Try out this “Flexi-Lunch” recommendation tool! 

![](Flexi-lunch-webapp-1.png =50x20)

This tool is built on a dataset web-scraped from Openrice HK’s reviews page.  It contains 2,600+ reviews on users' lunch experience of 900+ restaurants in the prime business districts of Central, Admiralty, Causeway Bay and Wan Chai from 2009 to 2019.  

This project contains four main parts:

## 1. Web-scraping: 

* Reviews-based (2,600 rows): Captures info of restaurant name, district, cuisine, rating, cost, wait time, review, and restaurant link
* Include only reviews for lunch and with valid meal cost data
* Since Openrice displays max 17 pages of search result, I broke down the searches to 5 popular cuisines (i.e. Japanese, Chinese, Thai, Italian, American) for all 4 districts

## 2. Text Analysis - NLP:

* Summarization: Use `< CountVectorizer>` to identify the sentence in each review that contains the most frequently-appeared words.  Make this sentence a one-line comment highlight.  Add it to the data frame’s new column, “summary”.
* Word Cloud: Quickly find out key words that customers like about the top 10 restaurants !

## 3. Sentiment predictor - NLP:

* Train a model that classifies the sentiment (positive or negative) of the review.  
* Retain only reviews that having ratings.  Define rating >= 3 as “Good” sentiment.  
* Three models are tested — 1) Multinomial Naive Bayes Classifier (Accuracy: 0.79); 2) Random Forest (0.77); 3) Gradient Boosting (0.83)
* Use Gradient Boosting to predict the sentiment of a new comment

![](Sentiment-predict-1.png =30x20)

## 4, Recommendation Tool - NLP:

* Transform the original review-based data frame (2,600 rows) into restaurant-based (900 rows). Reviews of the same restaurant are merged into one.  Ratings, wait time, and meal cost are averaged. 
* Use `< CountVectorizer>` to break down reviews to words and count frequencies
* Find the most similar restaurants base on cosine similarity 
* Generate 10 most similar restaurants with useful information (e.g, wait time, cost)

![](Flexi-lunch-webapp-1.png =50x20)

By using this recommendation tool, you can find the nearby burger places that are good alternatives to Five Guys! You can make a wise decision base on the average wait time, cost, rating, etc. from prior reviews. 

This tool will help save your time from reading lots of comments.  You can refer to the one-line highlight that likely captures the most important features in all reviews.  Also, you’ll find out whether the comment is positive or negative by inputing it to the sentiment predictor.

Hope this tool will improve your lunch experience!
