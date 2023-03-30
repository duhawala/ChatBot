# welcome - Murtuza Duhawala
def welcome():
  print("Hello. I see you are interested in football.")
  question = input("How may I help you? ")
  if keywordSearch(question):
    return True
  else:
    print("Okay, thank you. Bye.")

# match status - Rozeta Singh 
def match():
  futureMatch = input("Would you like some more information on upcoming matches? ")
  if futureMatch.lower() == "yes": 
    print("Here are the upcoming 3 matches: Tottenham Vs Everton on 3rd April 2022. Tottenham Vs Brighton on 8th April 2022. Tottenham Vs Bournemouth on 15th April 2022")
    ans = input("Is there anything else I can help you with? ")
    if ans.lower() == "yes": 
      previousMatch = input("Have you seen the last game? ")
      if previousMatch.lower() == "no": 
       lastMatch()
        ans = input("Is there anything else you would like to know about? ")
        welcome()
    else:
      pass

# ranking status - Murtuza Duhawala
def rankings():
  rankings = input("Would you like to know more about the ranks? ")
  if rankings.lower() == "yes":
    print("Tottenham is ranked 4th in the league table")
    moreInfo()
  else:
    pass

# gets the data of the last match including the score, goals - Rozeta Singh 
def lastMatch():
  print("For the last game. Tottenham played against Nottingham Forest on Saturday 11th March. The score was 3-1. ")
  lastGame = input("Would you like to know more information about this game? ")
  if lastGame.lower() == "yes":
    print("Harry Kane scored a goal")
  else:
    previous = input("Would you like to know more about previous matches?")
    if previous.lower() == "yes":
      dateOfMatch = input("Enter the date of the match you would like to know about in the format (DD/MM/YYYY) ")
      print("Tottenham played against Manchester United on", dateOfMatch)

# asking the user if they want to know more information or if they want to exit the chatbot - Murtuza Duhawala
def moreInfo():
  moreInfo = input("Would you like to know any more information? ")
  if moreInfo.lower() == "yes":
    welcome()
  else:
    print("Okay, thank you. Bye.")
    # exit the program
      
# searches for keywords and directs them to a particular function - Rozeta Singh 
def keywordSearch(word):
  listOfKeywords = ["match", "ranking"]
  if word in listOfKeywords:
    if word.lower() == "match": # make it case sensitive 
      match()
    elif word.lower() == "ranking": # make it case sensitive 
      rankings()
    else:
      welcome()
    

welcome()
