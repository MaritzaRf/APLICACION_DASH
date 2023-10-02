import dash
from dash import html
import dash_bootstrap_components as dbc

area1 = dbc.Card(
    [
        dbc.CardHeader(
            html.Strong("COLEGIOS Y CRECIDAS", style={"font-size": "26px", "color": "white"}),
            style={
                "background": "linear-gradient(to right, #15868e, #F0FFFF)",
                "border": "none",
            },
        ),
        dbc.CardBody(
            [
                html.H6("ALERTAS DE INUNDACIONES EN ZONAS EDUCATIVAS", style={"color": "#15868e"}),
            ],
            style={"font-size": "20px", "background-color": "#ffffff", "color": "#333"},
        ),
    ],
    style={"border": "2px solid #15868e", "border-radius": "10px", "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)"},
)
