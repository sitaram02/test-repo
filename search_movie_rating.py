"""
Script to fetch Rotten Tomatoes rating for a movie.
sript usage:
python search_movie_rating.py "<Movie name>".
Example : python search_movie_rating.py "Aladdin"

"""
import requests
import sys

IMDB_ID = "tt3896198"
IMDB_API_KEY = "4a4aed04"
URL = "http://www.omdbapi.com"
RATING_SOURCE = 'Rotten Tomatoes'


def search_movie_rating(movie_name):
    message = ''
    search_url = URL + '/?i=' + IMDB_ID + '&apikey=' + IMDB_API_KEY + '&t=' + movie_name
    results = requests.get(search_url)
    json_data = results.json()

    ratings = json_data.get('Ratings', '')
    if ratings:
        for r in ratings:
            if r['Source'] == RATING_SOURCE:
                message = r.get('Value')
    return message


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid arguments supplied.")
    else:
        movie_name = sys.argv[1]
        print("Searching Rotten Tomatoes rating for movie : " + movie_name)
        rating = search_movie_rating(movie_name)
        if rating:
            print("Rotten Tomatoes rating for movie %s is %s" % (movie_name, rating))
        else:
            print("Rotten Tomatoes rating not found!!!")
