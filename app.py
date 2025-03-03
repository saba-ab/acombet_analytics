"""Main entry point of app"""
from dash import Dash, Input, Output, html

import config
from app.layout import get_layout
from app.pages.overview import get_overview_layout

app = Dash(__name__, external_scripts=config.EXTERNAL_SCRIPTS)

server = app.server

app.layout = get_layout()

# Callback to handle URL routing and update the "page-content"


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    """Routing"""
    if pathname in ["/", "/overview"]:
        return get_overview_layout()
    # Uncomment and implement these if you have additional pages:
    # elif pathname == "/user-analytics":
    #     return get_user_analytics_layout()
    # elif pathname == "/revenue":
    #     return get_revenue_layout()
    else:
        # Return a 404 message if the pathname doesn't match any known routes
        return html.Div(
            "404: Page not found",
            className="p-4 text-center text-xl"
        )


if __name__ == "__main__":
    app.run_server(
        debug=config.DEBUG,
        host=config.HOST,
        port=config.PORT
    )
