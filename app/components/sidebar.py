"""Sidebar component for layout"""
from dash import html, dcc


def get_sidebar():
    """
    Returns the sidebar component with navigation links.
    """
    return html.Div(
        children=[
            html.H2("Navigation", style={
                    "padding": "10px", "marginBottom": "0px"}),
            html.Hr(),
            dcc.Link("Overview", href="/overview",
                     style={"display": "block", "padding": "10px 0"}),
            dcc.Link("User Analytics", href="/user-analytics",
                     style={"display": "block", "padding": "10px 0"}),
            dcc.Link("Revenue", href="/revenue",
                     style={"display": "block", "padding": "10px 0"}),
        ],
        style={
            "width": "250px",
            "backgroundColor": "#f0f0f0",
            "padding": "20px",
            "boxShadow": "2px 0px 5px rgba(0,0,0,0.1)"
        }
    )
