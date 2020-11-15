from datetime import datetime

from helper import create_jinja_env
from parser import parse_events, parse_all_events

today = datetime.now()
all_events = parse_all_events()
events = parse_events('data/2021_events_db.csv', today)

env = create_jinja_env()
template = env.get_template('index.html')
result = template.render(
    upcoming=events['upcoming'],
    has_upcoming=events['has_upcoming'],
    prev=events['prev'],
    has_prev=events['has_prev'],
    all_events=all_events,
    year='2021',
    other_year='2020',
    other_year_link='2020'
)

with open('build/2021/index.html', 'a') as f:
    f.write(result)
