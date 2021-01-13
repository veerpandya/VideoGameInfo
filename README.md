# VideoGameInfo

### Overview

This is an app used to quickly find general information about video games by searching using a name. The app uses the queried keyword(s) and then scrapes game information from popular sites like [Metacritic](https://www.metacritic.com/), [HowLongToBeat](https://howlongtobeat.com/), [Wikipedia](https://en.wikipedia.org/wiki/Main_Page), and [Google](https://www.google.com/). The information is then organized and listed in an easy to read format.

### Heroku Deployment

This app is deployed here:
https://videogameinfo.herokuapp.com/

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
