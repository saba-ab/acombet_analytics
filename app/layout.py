"""Main layout for acombet analytics"""

from dash import dcc, html

from app.components import footer, header, sidebar


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
            dcc.Location(id="url", refresh=False),
            header.get_header(),
            html.Div(
                children=[
                    sidebar.get_sidebar(),
                    html.Div(
                        id="page-content",
                        children=[
                            html.H2("Welcome to Acombet Analytics Dashboard",
                                    className="text-white"
                                    ),
                            html.P(
                                "Select an option from sidebar to view detailed insights.",
                                className="text-white"
                            )
                        ],
                        className="flex flex-col gap-4 w-full h-full min-h-[80vh]"
                    )
                ],
                className="flex min-h-[80vh]"
            ),
            footer.get_footer()
        ],
        className="flex flex-col min-h-[100vh]"
    )
