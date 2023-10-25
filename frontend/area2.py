import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import geopandas as gpd
import folium

departamentos = gpd.read_file('Departamentos.zip') 
departamentos_ordenados = sorted([depto for depto in departamentos['DeNombre'].unique() if depto != "Area en Litigio Cauca - Huila" 
                                  and depto != 'San Andrés Providencia y Santa Catalina'])
opciones_dropdown = [{'label': depto, 'value': depto} for depto in departamentos_ordenados]


area2 = dbc.Container([
        dbc.Card([
            dbc.CardBody([
                html.H5("Registro de afectaciones"),
                dcc.Dropdown(
                    options=opciones_dropdown,
                    value='Cundinamarca',
                    id='departamento_consultado'
                ),
            ]),
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id="mapa",
                    style={
                        'width': '100%', 
                        "height": "600px"
                    },
                )
            ], width=12),
        ])
    ],
    className="justify-content-start",
)
