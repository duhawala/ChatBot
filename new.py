#section fo rall my imported modules
from random import randrange
from datetime import *

#code for first greeting along the way, will continue to edit
greetings = ["Hello, I am the **name** chatbot and I'd like to provide you with all information Tottenham related. What can I help you with today?","Let me be your fortune teller, I can predict what is on your mind and I can bet you it's Tottenham related. So tell me what it is then?"]
b = len(greetings)
c = randrange(0,b)
a = greetings[c]
d = input(a).lower()

#code to extract date from first input incase asked about yesterday, tomorrow or today's match, date1 is date in mm/dd/yy format

def getmedate(val):
  try:
    date = datetime.strptime(val,'%m/%d/%Y')
    date2 = date.strftime('%m/%d/%Y')
    return date2
  except ValueError:
    if "no" not in val:
      d = input("So sorry but I only understand dates in the 'mm/dd/yy' format. So can we try this again?")
      return getmedate(d)

if "today" in d:
  date = datetime.today()
  date1 = date.strftime('%m/%d/%Y')
  if "match" or "game" in d:
    #could either ask for matches already played or now to be played
    #could also ask for match timelines or best place to find match highlights
elif "yesterday" in d:
  date = datetime.today() - timedelta(days=1)
  date1 = date.strftime('%m/%d/%Y')
  #could either ask about yesterday's Tottenham highlights or timelines
  #could also ask what matches were played yesterday
elif "tomorrow" in d:
  date = datetime.today() + timedelta(days=1)
  date1 = date.strftime('%m/%d/%Y')
  #could ask what matches would be played and what are our predictions
elif "match" or "game" in d:
  date1 = getmedate(d)