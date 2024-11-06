import os
from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from prettytable import PrettyTable

app = Flask(__name__)

# Настройка PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'postgresql://postgres:postgres@db:5432/pg')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# model
class Counter(db.Model):
    __tablename__ = 'counter'
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime(timezone=True), default=datetime.now(ZoneInfo("Europe/Moscow")))
    client_info = db.Column(db.String(512))

    def __init__(self, client_info):
        self.client_info = client_info


# create table if not exists
with app.app_context():
    db.create_all()


@app.route('/')
def hello():
    client_info = request.headers.get('User-Agent', 'Unknown')
    new_entry = Counter(client_info=client_info)
    db.session.add(new_entry)
    db.session.commit()

    # кол-во записей
    total_hits = Counter.query.count()

    # все записи
    all_entries = Counter.query.all()

    table = PrettyTable()
    table.field_names = ["ID", "Datetime", "Client Info"]
    for entry in all_entries:
        formatted_datetime = entry.datetime.strftime("%d/%b/%Y %H:%M:%S")
        table.add_row([entry.id, formatted_datetime, entry.client_info])

    table_html = table.get_html_string(attributes={"class": "table table-striped"})

    # Возврат текста с количеством кликов и таблицей
    return f"""
        <div>
            <h1>Кол-во кликов: {total_hits}</h1>
            {table_html}
        </div>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
