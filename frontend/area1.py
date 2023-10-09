import dash
from dash import html
import dash_bootstrap_components as dbc


area1 = dbc.Stack(
    children=[
        html.H1("COLEGIOS Y CRECIDAS", className="font-weight-bold"),
        html.H4("Alertas de Inundaciones en Zonas Educativas", className= "font-weight-bold")
    ],
    direction="column",
    className="align-items-center flex-wrap py-4 mb-4 text-white",
    style={"background-color": "#64B5F6"}
    
)
