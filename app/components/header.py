"""Header component for layout"""
from dash import html


def get_header():
    """
    Returns the header component for the dashboard.
    """
    return html.Header(
        children=[
            html.H1(
                "Acombet Analytics Dashboard",
                style={
                    "textAlign": "center",
                    "padding": "20px",
                    "margin": 0
                }
            )
        ],
        style={
            "backgroundColor": "#f8f9fa",
            "borderBottom": "1px solid #eaeaea"
        }
    )
