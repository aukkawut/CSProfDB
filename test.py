#sanity check
from scholarly import scholarly

print(next(scholarly.search_author('Steven A. Cholewiak')))