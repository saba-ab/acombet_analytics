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
                className="text-center p-4 m-0"
            )
        ],
        className="bg-[#f8f9fa] border border-b-[#eaeaea]"
    )
