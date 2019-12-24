--select count(*) from media_comments;

CREATE TABLE Media_Comments (
	id SERIAL PRIMARY KEY,
	media VARCHAR(150) ,
	article_name VARCHAR (500),
	username VARCHAR (150),
	sentiment VARCHAR (100),
	body_of_comment text
);

select * from  media_comments mc;
select count(*) from  media_comments mc;
select count(*) from  media_comments mc where media = 'Die Zeit';
select count(*) from  media_comments mc where media = 'Die Welt';
select * from media_comments where body_of_comment ilike '%zuverlässig%' and body_of_comment ilike  '%Lieferant%';

select * from media_comments where body_of_comment ilike '%zuverlässig%' and body_of_comment ilike  '%Lieferant%';

select count(username), username from media_comments where body_of_comment ilike '%zuverlässig%'
and body_of_comment ilike  '%Lieferant%' and media = 'zeit' group by username;

select count(username), username from media_comments where body_of_comment ilike '%zuverlässig%'
and body_of_comment ilike  '%Lieferant%' and media = 'zeit' group by username;

--select count(distinct(username)) from media_comments where body_of_comment ilike '%zuverlässig%';
--
--select distinct(username) from media_comments where body_of_comment ilike '%zuverlässig%';

--select pg_database_size('media_comments');
--
--select pg_size_pretty( pg_database_size('media_comments'));
--
