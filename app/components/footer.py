"""Footer component for layout"""
from dash import html


def get_footer():
    """
    Returns the footer component for the dashboard.
    """
    return html.Footer(
        children=[
            html.P(
                "© 2025 Acombet Analytics. All rights reserved.",
                style={"textAlign": "center", "padding": "10px", "margin": 0}
            )
        ],
        style={
            "backgroundColor": "#f8f9fa",
            "borderTop": "1px solid #eaeaea",
            "marginTop": "auto"
        }
    )
