# DS 230 - Final Project - Submission Script
# Please put all your SQL queries in this python script
# Copy and Paste them directly from BigQuery
#From Andy Zheng

def problem_1():
    my_SQL_command = """
    SELECT C.venue_name, C.venue_capacity,
  FROM `bigquery-public-data.ncaa_basketball.mbb_teams_games_sr` C 
  WHERE C.venue_state="IA" and C.venue_city="Iowa City"
  Limit 1
    """
    return my_SQL_command 



def problem_2():
    my_SQL_command = """
    SELECT COUNT(C.game_id) num_of_games
    FROM `bigquery-public-data.ncaa_basketball.mbb_teams_games_sr` C
    WHERE C.venue_name="Carver-Hawkeye Arena" and C.season=2017 and C.opp_name="Hawkeyes"
    """
    return my_SQL_command 



def problem_3():
    my_SQL_command = """
       SELECT Count(C.game_id) Number_of_Games, ROUND(AVG(C.points),1) Iowa_Points, ROUND(AVG(C.opp_points),1) Away_Points
       FROM `bigquery-public-data.ncaa_basketball.mbb_teams_games_sr` C
       WHERE C.season between 2013 and 2017 and C.win=true and C.venue_name="Carver-Hawkeye Arena"
       GROUP BY C.venue_name

    """
    return my_SQL_command 



def problem_4():
    my_SQL_command = """
       SELECT Name,Opp_name, W, L, W-L Margin
FROM (
    SELECT C.win_name Name, C.lose_name Opp_name,C.win_pts W, C.lose_pts L
    FROM `bigquery-public-data.ncaa_basketball.mbb_historical_tournament_games` C
)
order by Margin desc
Limit 1
    """
    return my_SQL_command 



def problem_5():
    my_SQL_command = """
       SELECT COUNT(DISTINCT P.player_id)
FROM `bigquery-public-data.ncaa_basketball.mbb_teams` T,`bigquery-public-data.ncaa_basketball.mbb_players_games_sr` P
WHERE  T.id = P.team_id and P.birthplace_city = T.venue_city and P.birthplace_state = T.venue_state 
    """
    return my_SQL_command 



def problem_6():
    my_SQL_command = """
       SELECT round((
    SELECT COUNT(HT.win_name) 
    FROM `bigquery-public-data.ncaa_basketball.mbb_historical_tournament_games` HT
    WHERE HT.win_seed > HT.lose_seed
) /
    (
    SELECT Count(*)
    FROM `bigquery-public-data.ncaa_basketball.mbb_historical_tournament_games` FKME 
),3)*100
    """
    return my_SQL_command 



def problem_7():
    my_SQL_command = """
SELECT Tn1, Tn2, C1, T1
FROM 
  (
  SELECT C.color C1 ,T.venue_state T1, T.name Tn1
  FROM `bigquery-public-data.ncaa_basketball.team_colors` C, `bigquery-public-data.ncaa_basketball.mbb_teams` T
  WHERE C.id = T.id
  ) first_person, 
  (
  SELECT C.color c2 ,T.venue_state T2, T.name Tn2
  FROM `bigquery-public-data.ncaa_basketball.team_colors` C, `bigquery-public-data.ncaa_basketball.mbb_teams` T
  WHERE C.id = T.id
  ) second_person
WHERE first_person.C1 = second_person.C2 AND first_person.T1 = second_person.T2 AND first_person.Tn1 < second_person.Tn2
ORDER BY C1, Tn1, Tn2, T1

    """
    return my_SQL_command 



def problem_8():
    my_SQL_command = """
SELECT birthplace_city, birthplace_state, birthplace_country, sum(points) totalpts,
FROM `bigquery-public-data.ncaa_basketball.mbb_players_games_sr` 
WHERE team_name="Hawkeyes" and season>=2013
GROUP BY birthplace_city, birthplace_state, birthplace_country
ORDER BY totalpts DESC
Limit 5

    """
    return my_SQL_command 



def problem_9():
    my_SQL_command = """
SELECT PG.team_market TM, Count(distinct PG.full_name) U_P 
FROM `bigquery-public-data.ncaa_basketball.mbb_players_games_sr` PG
WHERE PG.season>=2013 and PG.starter=true and PG.minutes_int64 <=24 and PG.points>=15
GROUP BY PG.team_id, PG.team_market
ORDER BY U_P DESC, TM DESC
    """
    return my_SQL_command 
