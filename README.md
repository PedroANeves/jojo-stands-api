# Jojo Stands API


Written in [Python](https://www.python.org/)/[Django](https://www.djangoproject.com/) using the [Django REST framework](https://www.django-rest-framework.org/) and deployed on [heroku](https://heroku.com/) at: https://jojo-stand-stats.herokuapp.com/

By default, the project uses the [Browsable API](https://www.django-rest-framework.org/topics/browsable-api/) when open with a web browser, you can use [?format=json](https://jojo-stand-stats.herokuapp.com/?format=json) to view the raw json.

The api that returns stands names, power, speed, range, stamina, precision and development potential

## example

running:
```
curl -H "Content-Type: application/javascript" https://jojo-stand-stats.herokuapp.com/api/1/
```

returns:
```
{
    "id": 1,
    "url": "http://127.0.0.1:8000/jojo/1/",
    "STAND": "Anubis",
    "PART": 3,
    "atributes": {
        "PWR": "B",
        "SPD": "B",
        "RNG": "E",
        "STA": "A",
        "PRC": "E",
        "DEV": "C"
}
```

## fields names

JSON field | meaning
---|---
STAND | stand name
PART | stand first appearance
PWR | power
SPD | speed
RNG | range
STA | stamina
PRC | precision
DEV | development potential

## fields values

JSON field | meaning
---|---
A | Very Good
B | Good
C | Average
D | Poor
E | Very Poor
∅ | None
∞ | Infinite
? | Unknown

## part values

JSON field | meaning
---|---
0 | No part
1 | Real Life Stand
2 | Purple Haze Feedback Light Novel
3 | Part 3, Stardust Crusaders.
4 | Part 4, Diamond Is Unbreakable.
5 | Part 5, Golden Wind.
6 | Part 6, Stone Ocean.
7 | Part 7, Steel Ball Run.
8 | Part 8, JoJolion.
