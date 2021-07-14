# VideoGameInfo

![Website](https://img.shields.io/website?up_message=running&url=http%3A%2F%2Fvideogameinfo.dev.vpandya.xyz%2F)

![VideoGameInfo](https://github.com/Kou-kun42/VideoGameInfo/blob/main/videogameinfo.png?raw=true)

### Overview

This is an app used to quickly find general information about video games by searching using a name. The app uses the queried keyword(s) and then scrapes game information from popular sites like [Metacritic](https://www.metacritic.com/), [HowLongToBeat](https://howlongtobeat.com/), [Wikipedia](https://en.wikipedia.org/wiki/Main_Page), and [Google](https://www.google.com/). The information is then organized and listed in an easy to read format.

### Deployment

This app is deployed here:
http://videogameinfo.dev.vpandya.xyz/

The heroku deployment works now that I've added multiprocessing and set a limit of 10 games for a search.

### Local Deployment

To launch this app on your local environment, clone this repository:

```
git clone https://github.com/Kou-kun42/VideoGameInfo.git
```

Then, set up a python virtual environment using:

```
python3 -m venv env
```

and then activate it:

```
source env/bin/activate
```

Next, install all the required packages:

```
pip3 install -r requirements.txt
```

Finally, launch the app:

```
python3 app.py
```


### Docker Build

To build the docker image:

```
docker build -t videogameinfo-image .
```

Build and run the container:

```
docker run -p 5000:5000 --rm --name videogameinfo-container videogameinfo-image
```
