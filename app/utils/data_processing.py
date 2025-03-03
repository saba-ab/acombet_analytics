"""Module for processing data"""

import pandas as pd

from app.utils.db_access import Database


def fetch_overview_data():
    """Fetches total counts of users, games and providers"""

    db = Database()

    user_df = db.fetch_data("SELECT COUNT(*) as total_users FROM users;")
    game_df = db.fetch_data("SELECT COUNT(*) as total_games FROM games;")
    provider_df = db.fetch_data(
        "SELECT COUNT(*) as total_providers FROM providers;")

    total_users = int(
        user_df.iloc[0]['total_users']
    ) if not user_df.empty else 0
    total_games = int(
        game_df.iloc[0]['total_games']
    ) if not user_df.empty else 0
    total_providers = int(
        provider_df.iloc[0]['total_providers']
    ) if not user_df.empty else 0

    return {
        "total_users": total_users,
        "total_games": total_games,
        "total_providers": total_providers
    }
