import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


from backend.calculoInundacion import consultarDepartamento
from frontend.area1 import area1
from frontend.area2 import area2
from frontend.area3 import area3, render_news_tab, render_empresa_tab, render_conocenos_tab


# Crea la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

@app.callback(
    Output("mapa", "figure"),
    Input("departamento_consultado", "value")
)

def update_map(departamento_consultado):
    return consultarDepartamento(departamento_consultado)

# Contenido del area
@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab"), Input("store", "data")],
)

def render_tab_content(active_tab, data):
    if active_tab == "noticias":
        return render_news_tab()

    elif active_tab == "empresa": 
        return  render_empresa_tab()
    
    elif active_tab == "conocenos":
        return render_conocenos_tab()
    
    return "No tab selected"

# Define el layout de la aplicación
app.layout = dbc.Container(
    [
    dbc.Row([
        dbc.Col(area1, md = 12, style = {'background-color':'white'}), # md es el ancho de la casilla 
        dbc.Col(area2, md = 6, style = {'background-color':'white'}),
        dbc.Col(area3, md = 6, style = {'background-color':'white'})
        ])  
    ],
    fluid=True
)


if __name__ == '__main__':
    app.run_server(debug=True)
