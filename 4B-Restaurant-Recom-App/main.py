from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from flask_table import Table, Col
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)

#Input page Page
@app.route('/')
def home():
    return render_template("index.html")    

# result page
@app.route("/recommendation", methods = ["GET", "POST"])
def recommendation():
    if request.method == "POST":
        #reading the dataset 
        title = request.form["title"]

        df = pd.read_csv("Openrice_Transformed_V2.csv", low_memory = False)

# define vectorizer object, remove stop words like the, a
        tfidf = TfidfVectorizer(stop_words = "english")

# replace nan with empty string
        df["Reviews"] = df["Reviews"].fillna("")

        tfidf_matrix = tfidf.fit_transform(df["Reviews"])

        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

        indices = pd.Series(df.index, index = df["Restaurant_Name"])

        def get_recommendations(title, cosine_sim = cosine_sim):
    
    #get the index of the restuarant that matches the title
            idx = indices[title]
    #pairwise similarity scores of all restaurants
            sim_scores = list(enumerate(cosine_sim[idx]))
    # sort the restaurants based on the similarity scores
    # add second element of list to the function
            sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)
    # get the scores of the 10 most similar restaurants
            sim_scores = sim_scores[1:11]
    # Get the restaurant indices
            rest_indices = [i[0] for i in sim_scores]
    # return the top 10 most similar restaurants
            df_10 = df[["Restaurant_Name","Restaurant_Link","District","Rating_Average","Wait_Average"]].iloc[rest_indices]

            return df_10.to_html(header="true", table_id="table")

        return get_recommendations(title)

if __name__ == "__main__":
    app.run(host='0.0.0.0')