"""Overview page"""
from dash import html, dcc
import plotly.express as px
import pandas as pd
from app.utils.data_processing import fetch_overview_data


def get_overview_layout() -> html.Div:
    """Layout for overview page"""

    data = fetch_overview_data()

    df_metrics = pd.DataFrame({
        "Metric": ["Total Users", "Total games", "Total Providers"],
        "Count": [data["total_users"], data["total_games"], data["total_providers"]]
    })

    fig = px.bar(
        df_metrics,
        x="Metric",
        y="Count",
        title="Overview Metrics",
        color="Metric",
        text="Count"
    )

    fig.update_traces(texttemplate='%{text}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

    layout = html.Div(
        children=[
            html.H2("Overview", className="text-center text-2xl font-bold p-4"),
            dcc.Graph(id='overview-chart', figure=fig)
        ],
        className="p-4 w-full"
    )
    return layout
