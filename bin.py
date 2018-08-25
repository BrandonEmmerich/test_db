import psycopg2 as pg2, psycopg2.extras as pg2_extras
import web

conn = pg2.connect(host="localhost", port=5432, dbname="test_db", user="b")
cur = conn.cursor(cursor_factory=pg2_extras.DictCursor)

stories = web.get_eastmoney_stories()
web.write_to_db_china_news(stories, cur, conn)

cur.close()
conn.close()
