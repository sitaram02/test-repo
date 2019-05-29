FROM python:3
MAINTAINER ram32.chowdary@gmail.com
RUN  easy_install pip && pip install requests
COPY . /src
EXPOSE 90
CMD ["python","/src/search_movie_rating.py"]
