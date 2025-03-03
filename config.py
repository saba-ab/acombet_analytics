"""Config module for storing constants"""

import os

# Dash server running mode
DEBUG = os.getenv("DEBUG", "True").lower() in ["true", "1"]

# Host for running server
HOST = os.getenv("HOST", "127.0.0.1")

# Port for running server
PORT = int(os.getenv("PORT", "8050"))

# Database url for creating SQLalchemy engine
DATABASE_URL = os.getenv("DATABASE_URL")
