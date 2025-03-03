"""Main layout for acombet analytics"""

from dash import html
from app.components import header, sidebar, footer


def get_layout():
    """
    Returns the base layout for app

    Layout includes:
        - Header on top.
        - Sidebar for navigation are.
        - Footer at the bottom.
    """

    return html.Div(
        children=[
            header.get_header(),
            html.Div(
                children=[
                    sidebar.get_sidebar(),
                    html.Div(
                        id="page-content",
                        children=[
                            html.H2("Welcome to Acombet Analytics Dashboard"),
                            html.P(
                                "Select an option from sidebar to view detailed insights.")
                        ],
                        style={
                            "flex": 1,
                            "padding": "20px"
                        }
                    )
                ],
                style={
                    "display": "flex",
                    "minHeight": "80vh"
                }
            ),
            footer.get_footer()
        ],
        style={
            "display": "flex",
            "flexDirection": "column",
            "minHeight": "100vh"
        }
    )
