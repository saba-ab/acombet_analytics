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
                className="""text-center text-white p-[10px] m-0"""
            )
        ],
        className=""" bg-black bt-[1px] bt-[#eaeaea] mt-auto min-h-[5vh]"""
    )
