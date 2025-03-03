"""Main entry point of app"""
from dash import Dash

import config
from app.layout import get_layout

app = Dash(__name__, external_scripts=config.EXTERNAL_SCRIPTS)

server = app.server

app.layout = get_layout()

if __name__ == "__main__":
    app.run_server(
        debug=config.DEBUG,
        host=config.HOST,
        port=config.PORT
    )
