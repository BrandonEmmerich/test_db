from sqlalchemy import Column, create_engine, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import web

engine = create_engine('postgresql://b:@localhost/test_db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class china_news_2(Base):
    __tablename__ = 'china_news_2'
    newsid = Column(String, primary_key=True)
    url_w = Column(String)
    simtitle = Column(String)
    simdigest = Column(String)
    showtime = Column(String)
    art_media_name = Column(String)
    run_id = Column(String)

stories = web.get_eastmoney_stories()

for story in stories:
    row = china_news_2(**story)
    session.merge(row)

session.commit()
