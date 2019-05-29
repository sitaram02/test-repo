# test-repo

i have written code using python

created dockerfile with set of commands and build image from that

ex: docker build -t imagename .

docker build -t myimage . Run the container using dockerimage by passing arguments like

ex: docker run imageName python /src/search_movie_rating.py(file address) "movie name"

docker run myimage python /src/search_movie_rating.py "Aladdin"

Finally we can get the Rotten Tomatoes value

ex: Rotten Tomatoes:45%
