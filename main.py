from riotwatcher import LolWatcher, ApiError
import pandas as pd
import datetime

# golbal variables
api_key = 'RGAPI-1868ffd1-4ab5-4413-a0a8-072717c51e11'
watcher = LolWatcher(api_key)
my_region = 'na1'
skillzy_puuid = "n_B7vyMzM4Ni_srzS_NYfvDMLUJ86-eWJ9vObGIHBYKCy3wLAShLGpY0XWElUSrnWDMXg1lzcNASdQ"

#match = watcher.match.by_id(my_region, skillzy_history[0])
def pull_matchlist(summoner):
    """
    pulls a matchlist object from a given summoners puuid and returns it.
    """
    return watcher.match.matchlist_by_puuid(my_region, summoner)

def pull_matches(match_history):
    """
    when given a match history in the form of a matchlist. goes through each match and pulls the data for those matches. spits out a list of the matches.
    """
    matches = []
    for match in match_history:
        matches.append(watcher.match.by_id(my_region, match))
    return matches

def grab_data(match): 
    """
    when given a match, grabs relevant data and returns a dictionary.
    """
    dict = {}
    game_start = match['info']['gameStartTimestamp']
    game_end = match['info']['gameEndTimestamp']
    game_duration = match['info']['gameDuration']
    game_id = match['info']['gameId']
    dict["game id"] = game_id
    dict["game start"] = game_start_time = datetime.datetime.fromtimestamp(game_start/1000)
    dict["game end"] = game_end_time = datetime.datetime.fromtimestamp(game_end/1000)
    dict["game duration"] = secs_to_mins(game_duration)
    
    return dict

def secs_to_mins(time):
    secs = time%60
    mins = (time/60.0)
    mins = int(mins)
    return str(mins) + ":" + str(secs)

if __name__ == "__main__":
    matchlist = pull_matchlist(skillzy_puuid)
    matches = pull_matches(matchlist)
    data = {}
    i = 1
    for match in matches:
        match_data = grab_data(match)
        data[i] = match_data
        i += 1
    print(data)

    """
    dict = {}
    dict['game start time'] = game_start_time
    dict['game end time'] = game_end_time
    df = pd.DataFrame(data=dict,index=0)
    df  

    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    print(df)
    """