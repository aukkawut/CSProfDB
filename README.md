# CSProfDB
This repo is for searching professor in CS based on their work. Probably smart enough to make you find suitable professors for your grad school.

## How this is working (currently)

A user inputs their keywords -> we call the search for papers with that keyword -> filter the last author id out of the search -> search for that author -> if their email contains .edu, that person is probably a professor -> return that professor information

## How to run

```
python run.py
```

## Requirement

Run `pip install -r requirements.txt` to install all required libraries, this might not work on Windows as I have tried.

## Problem

Fetching new observations is quite expensive (the time it takes is quite long). Need some optimization on this. One way I can think of is to have a local database to store the search each time and if it is a generic topic like "machine learning", change the method of search from searching papers to searching the keyword. Moreover, we might want to have a proxy for these things to work as you might get a rate limit or ban.

## TODO

- [x] Get some results
- [ ] Proxy!
- [ ] Database
- [ ] Semantic search on database
- [ ] Optimization

