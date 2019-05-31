"""Pull authors from database."""
from os import environ
from sqlalchemy import create_engine, MetaData, text
import simplejson as json


class Database:
    """Maanage DB connection, pull records."""

    def __init__(self):
        self.uri = environ.get('SQLALCHEMY_DATABASE_URI')
        self.db_schema = environ.get('SQLALCHEMY_DB_SCHEMA')
        self.db_query = environ.get('SQLALCHEMY_AUTHOR_QUERY')
        self.meta = MetaData(schema=self.db_schema)
        self.engine = create_engine(self.uri,
                                    connect_args={'sslmode': 'require'},
                                    echo=True)

    def database_get_records(self, authorName):
        """Fetch records for backlog issues."""
        query = self.db_query % (authorName)
        sql = text(query)  # SQL Query
        rows = self.engine.execute(sql)  # Get Rows
        rows = [dict(row) for row in rows]  # Render as dict
        return rows[0]

    def create_json_response(self, authorName):
        """Create JSON response of records."""
        response = self.database_get_records(authorName)
        return json.dumps(response)
