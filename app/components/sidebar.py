"""Sidebar component for layout"""
from dash import dcc, html


def get_sidebar():
    """
    Returns the sidebar component with navigation links.
    """
    return html.Div(
        children=[
            html.H2("Navigation", className="""mb-[20px]"""),
            html.Hr(),
            dcc.Link("Overview", href="/overview", className="""pt-[20px]"""),
            dcc.Link("User Analytics", href="/user-analytics",
                     className="""pt-[10px]"""),
            dcc.Link("Revenue", href="/revenue", className="""pt-[10px]"""),
        ],
        className="w-[250px] bg-[#f0f0f0]/10 p-5 shadow-sm flex flex-col gap-5 text-white border-[#0b9799]"
    )
