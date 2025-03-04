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
                className="text-center p-4 m-0 text-white"
            )
        ],
        className="transparent border border-[#0b9799] shadow-xl p-4 min-h-[10vh]"
    )
