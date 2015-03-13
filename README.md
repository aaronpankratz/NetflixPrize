# Introduction & Specifications #

Here is the wiki page for a project I did in college to solve the Netflix challenge.

<h2>Specifications </h2>
Write a program to win the Netflix Prize.
More info and comments about the Netflix challenge can be found here. http://www.netflixprize.com/


# Details #

<h2>Problem</h2>
The Netflix challenge is to write an algorithm that predicts user ratings for films, based on previous ratings.
<br>
Given an input of movie ids and customer ids, we have to predict what each customer will rate the movies they are listed under.<br>
<br>
To check our predicts we will take the Relative Mean Squared Error of our predictions and the actual rating.<br>
<br>
To find the RMSE we have to take the differences of each prediction and actual rating, then square that value, then sum them all up divide by number of ratings and take the square root.<br>
<br>
By taking the square then summing before we find the average, we give more weight to larger differences.<br>
<br>
This is because we want our predictions to be as accurate as possible.<br>
<br>
It has been claimed that even an improvement of 1% RMSE results in a significant difference in the ranking of the "top-10" most recommended movies for a user.<br>
<br><br>
<h3>Input </h3>
We were given the following data sets to create caches from.  I then used the caches I created to help me make my predictions quickly.<br>
<br>
TRAINING DATASET<br>
MOVIES FILE<br>
THE PROBE DATASET FILE<br>

The training dataset is a directory containing 17770 files, one<br>
per movie.  The first line of each file contains the movie id followed by a<br>
colon.  Each subsequent line in the file corresponds to a rating from a customer<br>
and its date in the following format:<br>
<br>
CustomerID,Rating,Date<br>
<br>
- MovieIDs range from 1 to 17770 sequentially.<br>
- CustomerIDs range from 1 to 2649429, with gaps. There are 480189 users.<br>
- Ratings are on a five star (integral) scale from 1 to 5.<br>
- Dates have the format YYYY-MM-DD.<br>

The Movies file contains movie information in the following format:<br>
<br>
MovieID,Year_of_Release,Title<br>
<br>
- MovieID do not correspond to actual Netflix movie ids or IMDB movie ids.<br>
- Year_of_Release can range from 1890 to 2005 and may correspond to the release of corresponding DVD, not necessarily its theaterical release.<br>
- Title is the Netflix movie title and may not correspond to titles used on other sites.  Titles are in English.<br>

Finally we were provided a probe dataset.<br>
This text file contains lines indicating a movie id, followed by a colon, and<br>
then customer ids, one per line for that movie id.<br>
<br>
MovieID1:<br>
CustomerID11<br>
CustomerID12<br>
...<br>
MovieID2:<br>
CustomerID21<br>
CustomerID22<br>

We were not given the actual ratings for each customer, which I needed to calculate my RMSE, however a classmate posted to the public repository a file containing this information.<br>
<br>
<h3>Output </h3>
The format of the submitted prediction file follows the format of the probe dataset.  However, your predicted rating takes the<br>
place of the corresponding customer id, one per line.<br>
<br>
For example, if the qualifying dataset looked like:<br>
111:<br>
3245<br>
5666<br>
6789<br>
225:<br>
1234<br>
3456<br>

then a prediction file should look something like:<br>
111:<br>
3.0<br>
3.4<br>
4.0<br>
225:<br>
1.0<br>
2.0<br>

which means i predict customer 3245 to rate move 111 with 3.0 stars, and customer 5666 will rate movie 111 slightly higher at 3.4 stars<br>
<br><br>
<h1>The Plan </h1>
So for my initial plan, i just found the overall average rating from all customers for each movie. I then cached these values.  Then for the prediction outputs i just returned the same cached average value for each movie to every customer. So for example if the overall average rating for movie 1 was 3.5, then given the following probe file:<br>
1:<br>
1<br>
2<br>
3<br>
4<br>
5<br>

i would just return:<br>
1:<br>
3.5<br>
3.5<br>
3.5<br>
3.5<br>
3.5<br>

i new that this wouldn't get me under 1.0 RMSE but it was actually in the ballpark at 1.05.<br>
<br>
next i decided to calculate what each customers average rating was, in other words i took all the movies that one customer had rated and found the overall average rating for a particular customer.<br>
<br>
One of the article resources provided by the professor tells us the overall average rating is 3.7,  now i know what a particular customers "sensitivity" is, which is just the difference between their average rating and the average rating of all customers.<br>
<br>
now to calculate my prediction i just add the average rating for a movie to the customer sensitivity.<br>
<br>
using this prediction method i was able to get a RMSE of .973. Success!<br>
<br>
<br><br>
<h3>Optimizations</h3>
I made some optimizations to the cache, because there were many cache files i wanted them to be as small as possible, so i rounded all floats to 2 precision and only stored the rating value and represented the customer or movie with the name of the cache file.<br>
<br>
Turns out having a single text file for each value is a bad idea because querying these files is slow disk access causing my program to run unacceptably slow.  So i changed the caches to be single files containing dictionaries of the average ratings. I can then load these dictionaries into my program and query them in fast constant time.
