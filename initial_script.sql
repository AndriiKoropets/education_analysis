CREATE TABLE Media_Comments (
	id SERIAL PRIMARY KEY,
	media VARCHAR(150) ,
	article_name VARCHAR (500),
	username VARCHAR (150),
	sentiment VARCHAR (100),
	body_of_comment text
);

-- drop table media_comments;
--
select * from media_comments;

select * from media_comments where media = 'Die Welt';
select * from media_comments where username = 'vonDü';
select * from media_comments where sentiment = 'biased';



-- insert into media_comments (media, article_name, username, sentiment, body_of_comment)
-- values ('Die Zeit', 'Nord Stream 2: Wolfgang Schäuble kritisiert Ostsee-Pipeline',
-- 'vonDü', 'biased', 'Die USA und einige europäische Staaten kritisieren den Bau, unter anderem weil sie eine zu große Abhängigkeit von russischem Gas befürchten."Blödsinn wird nicht zur Wahrheit, nur weil man ihn ständig wiederholt.Der Verlauf der Gasleitung ändert die Abhängigkeit nämlich nicht, erhöht allerdings die Versorgungssicherheit Deutschlands, weil die Gaslieferungen dem Zugriff von Transitländern entzogen werden. Transitländer,
-- 	denen man nicht wirklich trauen kann, dass sie diese Gegebenheiten nicht irgendwann als Hebel zur Durchsetzung eigener Interessen benutzen.');
--
--
-- insert into media_comments (media, article_name, username, sentiment, body_of_comment)
-- values ('Die Welt', 'Schäuble übt Kritik an Nord Stream 2', 'Sigrun W', 'neutral', 'Gibt es für diesen Menschen eigentlich noch ein Leben
-- nach der Politik? Demnächst 77 Jahre alt, seit fast 20 Jahren querschnittsgelähmt.
-- Denkt Schäuble eigentlich einmal an seine Frau, an seine Angehörigen? Oder glaubt er gar ohne IHN geht es nicht? Schäuble kann einem leid tun.'
-- );