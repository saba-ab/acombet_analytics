"""Module for processing data"""

from dataclasses import dataclass

import pandas as pd

from app.utils.db_access import Database


@dataclass
class OverviewDTO:
    """Data transfer object for """
    users: int
    games: int
    providers: int
    deactivated_users: int
    active_users: int


def extract_count(df: pd.DataFrame, df_column: str) -> int:
    """Extracts count from DataFrame"""
    return int(df.iloc[0][df_column]) if not df.empty else 0


def fetch_overview_data() -> OverviewDTO:
    """Fetches total counts of users, games and providers"""

    db = Database()

    user_count_query = "SELECT COUNT(*) as users FROM users;"
    deactivated_user_count_query = "SELECT COUNT(*) as deactivated_users FROM deactivated_users;"
    game_count_query = "SELECT COUNT(*) as games FROM games;"
    provider_count_query = "SELECT COUNT(*) as providers FROM providers;"

    user_df = db.fetch_data(user_count_query)
    deactivated_user_df = db.fetch_data(deactivated_user_count_query)
    game_df = db.fetch_data(game_count_query)
    provider_df = db.fetch_data(provider_count_query)

    users = extract_count(user_df, "users")
    games = extract_count(game_df, "games")
    providers = extract_count(provider_df, "providers")
    deactivated_users = extract_count(
        deactivated_user_df, "deactivated_users")

    active_users = users - deactivated_users

    return OverviewDTO(
        users=users,
        games=games,
        providers=providers,
        deactivated_users=deactivated_users,
        active_users=active_users
    )
