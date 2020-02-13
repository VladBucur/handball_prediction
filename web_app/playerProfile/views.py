from django.shortcuts import render
import pandas as pd

def profileView(request):
    try:
        playerName = request.POST['player-name']
    except:
        return render(request, 'playerProfile.html', {"playerName": "", "predictionSeasonList": []})

    players_df = pd.read_csv('../inputs/final_processed_data.csv')
    players_raw_df = pd.read_csv('../inputs/raw_data.csv')

    player_data = players_df[players_df['name'] == playerName]
    player_raw_data = players_raw_df[players_raw_df['name'] == playerName]

    player_raw_data['goals_per_match_year3'] = player_raw_data['goals_year3'] / player_raw_data['matches_year3']
    data = player_data.merge(player_raw_data[['goals_per_match_year3', 'prediction_season']],
                             on='goals_per_match_year3', how='left')

    predictionSeasonList = list(data['prediction_season'][~data['prediction_season'].isna()].values)

    return render(request, 'playerProfile.html', {"playerName": playerName, "predictionSeasonList": predictionSeasonList})
