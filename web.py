import requests
import time

def get_eastmoney_stories():
    """This function hits the eastmoney mobile news api to get news stories"""

    run_id = int(time.time())
    url = 'http://newsapi.eastmoney.com/kuaixun/v2/api/yw?limit=10'
    res = requests.get(url)

    list_of_data = []
    _data = res.json()['news']

    for i in range(len(_data)):
        print i

        _dict = {
            'newsid' : _data[i].get('newsid'),
            'url_w' : _data[i].get('url_w'),
            'simtitle' : _data[i].get('simtitle'),
            'simdigest' : _data[i].get('simdigest'),
            'showtime' : _data[i].get('showtime'),
            'Art_Media_Name' : _data[i].get('Art_Media_Name'),
            'run_id': run_id,
            }

        list_of_data.append(_dict)

    return list_of_data

def write_to_db_china_news(stories, cur, conn):
    """This function writes to the China News table"""

    for story in stories:
        newsid = story['newsid'],
        url_w = story['url_w'],
        simtitle = story['simtitle'],
        simdigest = story['simdigest'],
        showtime = story['showtime'],
        art_media_name = story['Art_Media_Name'],
        run_id = story['run_id']

        # executing using cursor
        cur.execute(
            ''' INSERT INTO china_news (newsid, url_w, simtitle, simdigest,showtime, art_media_name,run_id)
                VALUES (%(newsid)s, %(url_w)s, %(simtitle)s, %(simdigest)s, %(showtime)s, %(art_media_name)s, %(run_id)s);
            ''',
            {
                'newsid' : newsid,
                'url_w' : url_w,
                'simtitle' : simtitle,
                'simdigest' : simdigest,
                'showtime' : showtime,
                'art_media_name' : art_media_name,
                'run_id': run_id,
            }
        )

        #  commiting changes to db
        conn.commit()
