import streamlit as st
import tweepy as tw
import pandas as pd
import cohere 
from cohere.classify import Example 


api_key = 'Hnrleh9HSfnm26bF9oGzpVbos'
api_key_secret = 'QEMggpHriC5yMU0BNc9wGmH3qtf3O28C6o3t0Hzw1iSdnJhakC'
access_token= '785508615230631936-GVXzqXUBNJM7YJv25CnQa4wHF7P33pg'
access_token_secret = 'CkG6hIlp7kKN11suc313lDhfM8ulYP89dcWniuwGf7j68'

auth = tw.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

st.image("Stock-Market.jpeg")
st.title('StockTalk')

date_since = "2022-09-16"
keyword = st.text_input("Enter a company:", "Company Name")
limit = 150
tweets = tw.Cursor(api.search_tweets, q = keyword, lang = "en", tweet_mode = "extended").items(limit)

tweet_list = [tweet.full_text for tweet in list(tweets)]

co = cohere.Client('dWlGexUAj18f43U8aaWLyvhJF7qQpX41LlvRLltz') 

if (keyword == "Company Name"):
    pass
else:
    response = co.classify( 
    model='large', 
    inputs=tweet_list, 
    examples=[Example("My model X saved my family and our vacation from a crazy driver merging right into us last night. The X surged to the left and braked hard. Car missed us by inches.  The other car must have been going a 100 mph. Thank you Tesla!!!", "Positive"), Example("Nacho fries are back!!! I repeat. NACHO. FRIES. ARE. BACK!  #TacoBell", "Positive"), Example("Tequila Anyone? Yes I bought this beauty at #Costco", "Positive"), Example("So good I had to share! Check out all the items I\'m loving on @Poshmarkapp from @SavyT_ @SafiyahSissoko #poshmark #fashion #style #shopmycloset #clarks #oldnavy #gianibernini: https://posh.mk/MxAIyLVFFob", "Positive"), Example("Good on you #Chevrolet.  This is a massive improvement over the OG Trax.", "Positive"), Example("@ChipotleTweets  your app is terrible and keeps removing ingredients when adding to to cart -was  deliver tacos with only meat and lettuce..  second time this has happened in weeks.. what is happening there.. #chipotle", "Negative"), Example("#BoycottShein This is modern day slavery and more. #fastfashion", "Negative"), Example("I wonder if Facebook will fact check its own boss???\n#Facebook #FactCheck #Zuckerberg", "Negative"), Example("My brand new model 3 stopped abruptly in the middle of the highway. \n\nI had 140 miles in range left, but my @Tesla service center insists this horrifying incident is MY fault and I “ran out of change”. Why the lies?", "Negative"), Example("Taco Bell - Linden, Michigan - Ate 4 5 layer burritos last night and woke up with all the symptoms.,  Something in the 5 layer burritos My daughter also ate here hours after I did so if s... Food Poisoning https://iwaspoisoned.com/i/zqQjpoz #tacobell #taco #burrito", "Negative")]) 

    predictions = [i.prediction for i in response.classifications]
    p = 0
    n = 0
    outcome = False
    for i in predictions:
        if i == 'Positive':
            p += 1
        else:
            n += 1
    if p > n:
        outcome = True

    if outcome:
        st.subheader("Invest in this company")
    else:
        st.subheader("Don't invest in this company")
