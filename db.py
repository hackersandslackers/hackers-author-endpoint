"""Pull issues from database."""
from os import environ
from sqlalchemy import create_engine, MetaData, text
import simplejson as json


class Database:
    """Maanage DB connection, pull records."""

    def __init__(self):
        self.uri = environ.get('SQLALCHEMY_DATABASE_URI')
        self.db_schema = environ.get('SQLALCHEMY_DB_SCHEMA')
        self.backlog_query = environ.get('SQLALCHEMY_BACKLOG_QUERY')
        self.todo_query = environ.get('SQLALCHEMY_TODO_QUERY')
        self.inprogress_query = environ.get('SQLALCHEMY_INPROGRESS_QUERY')
        self.done_query = environ.get('SQLALCHEMY_DONE_QUERY')
        self.meta = MetaData(schema=self.db_schema)
        self.engine = create_engine(self.uri,
                                    connect_args={'sslmode': 'require'},
                                    echo=True)

    def database_get_records(self, query):
        """Fetch records for backlog issues."""
        sql = text(query)  # SQL Query
        rows = self.engine.execute(sql)  # Get Rows
        rows = [dict(row) for row in rows]  # Render as dict
        return rows

    def create_response(self):
        """Create JSON response of records."""
        response = {
            'backlog': self.database_get_records(self.backlog_query),
            'todo': self.database_get_records(self.todo_query),
            'inprogress': self.database_get_records(self.inprogress_query),
            'done': self.database_get_records(self.done_query),
        }
        return json.dumps(response)
