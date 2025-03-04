"""Overview page"""
import pandas as pd
import plotly.express as px
from dash import dcc, html

from app.utils.data_processing import fetch_overview_data


def get_overview_layout() -> html.Div:
    """Layout for overview page"""

    overview_data = fetch_overview_data()

    df_metrics = pd.DataFrame({
        "Metric": ["Total Users", "Total Users", "Total games", "Total Providers",],
        "Type": ["Active", "Deactivated", "Total", "Total"],
        "Count": [overview_data.active_users, overview_data.deactivated_users, overview_data.games, overview_data.providers]
    })

    fig = px.bar(
        df_metrics,
        x="Metric",
        y="Count",
        title="Overview Metrics",
        color="Type",
        text="Count",
        barmode="stack",
    )

    fig.update_traces(texttemplate='%{text}', textposition='outside')
    fig.update_layout(uniformtext_minsize=6, uniformtext_mode='hide')
    fig.update_yaxes(range=[0, df_metrics["Count"].max() * 1.2])

    layout = html.Div(
        children=[
            html.H2(
                "Overview", className="text-center text-2xl font-bold p-4 text-white"),
            dcc.Graph(id='overview-chart', figure=fig, className="h-full")
        ],
        className="p-4 w-full h-full"
    )
    return layout
