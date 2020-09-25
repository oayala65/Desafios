runners={'osval':13,'Lis':5,'Pit':9}

def find_winner_name(dictionary):
  #print(min(dictionary.values()))
  winner_score = min(dictionary.values())
  for key, value in dictionary.items():
    print(key)
    print(value)
    if value == winner_score:
      return key  

winnerName = find_winner_name(runners)
print(winnerName)