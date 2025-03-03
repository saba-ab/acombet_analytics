import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


class Database:
    """Class for database connection"""

    def __init__(self, db_url: str = None) -> None:
        """Initialize the database object by creating a SQLAlchemy engine"""

        if db_url is None:
            db_url = os.getenv("DATABASE_URL")
        if not db_url:
            raise ValueError(
                "Database URL is not set in environment variables")

        self.db_url = db_url
        self.engine = create_engine(self.db_url)

    def fetch_data(self, query: str) -> pd.DataFrame:
        """Execute query on database and return dataframe object"""

        with self.engine.connect() as connection:
            df = pd.read_sql(query, connection)
        return df
