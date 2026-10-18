-- your code goes here
select player_name,score from players where player_name in (select winner from matches) order by score desc ;