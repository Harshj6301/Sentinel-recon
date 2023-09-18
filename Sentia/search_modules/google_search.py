# Define your search query
from googlesearch import search

def gsearch(term):
  RESULT = []
  result = search(query=term)
  for r,i in enumerate(result):
    RESULT.append(i)
    print(r, i)
  return RESULT