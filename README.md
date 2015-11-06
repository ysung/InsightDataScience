Insight Data Engineering - Coding Challenge
===========================================================


## Challenge Summary

This challenge is to implement two features:

1. Clean and extract the text from the raw JSON tweets that come from the Twitter Streaming API, and track the number of tweets that contain unicode.
2. Calculate the average degree of a vertex in a Twitter hashtag graph for the last 60 seconds, and update this each time a new tweet appears.

Here, we have to define a few concepts (though there will be examples below to clarify):

- A tweet's text is considered "clean" once all of the escape characters (e.g. \n, \", \/ ) are replaced and unicode have been removed.
- A Twitter hashtag graph is a graph connecting all the hashtags that have been mentioned together in a single tweet.


## Enviroment

I used Python 2.7.10 to complete the challenge