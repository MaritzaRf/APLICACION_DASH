import dash
import geopandas as gpd
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import folium

from backend.calculoInundacion import consultarDepartamento
from frontend.area1 import *
from frontend.area2 import *
from frontend.area3 import *



# Crea la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

@app.callback(
    Output("mapa", "figure"),
    Input("departamento_consultado", "value")
)

def update_map(departamento_consultado):
    return consultarDepartamento(departamento_consultado)

@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab"), Input("store", "data")],
)

def render_tab_content(active_tab, data):
    if active_tab == "noticias":
        return html.Div([
            html.Div([
                html.H4("Impacto de lluvias deja a más de 1.600.000 estudiantes sin clase por daños en colegios",
                        style={'color': '#15868e', 'font-weight': 'bold'}),
                html.H6("(PIE DE CUESTA - SANTANDER) 📍",
                        style={'color': '#007BFF', 'font-weight': 'bold', 'font-style': 'italic'}),
                html.A('Leer más', href='https://www.bluradio.com/nacion/impacto-de-lluvias-deja-a-mas-de-1-600-000-estudiantes-sin-clases-por-danos-en-colegios-rg10',
                       target='_blank', style={'color': '#007BFF', 'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '20px'},  # Enlace a tu noticia
                       ),  # Estilo para mostrar en línea y margen izquierdo
                #html.Br(),
                html.Img(
                    src='https://caracoltv.brightspotcdn.com/dims4/default/ce72944/2147483647/strip/true/crop/720x542+0+0/resize/720x542!/format/webp/quality/90/?url=http%3A%2F%2Fcaracol-brightspot.s3.amazonaws.com%2F35%2Fbc%2F5ce64d5a42a5b784987750874597%2Fwhatsapp-image-2022-09-05-at-7.06.02%20AM%20%281%29.jpeg',
                    style={'width': '60%'},  # Tamaño de la imagen
                    className='mx-auto d-block'),
                html.Br()
            ]),  # Estilo para mostrar en línea

            html.Div([
                html.H4("Colegios públicos en estado critico tras inundaciones por fuertes lluvias",
                        style={'color': '#15868e', 'font-weight': 'bold'}),
                html.H6("(CARTAGENA - BOLIVAR)📍",
                        style={'color': '#007BFF', 'font-weight': 'bold', 'font-style': 'italic'}),
                html.A('Leer más', href='https://www.eluniversal.com.co/cartagena/colegios-publicos-en-estado-critico-tras-inundaciones-por-fuertes-lluvias-EH8845314',
                       target='_blank', style={'color': '#007BFF'})  # Enlace a tu noticia
            ], style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '20px'}),  # Estilo para mostrar en línea y margen izquierdo
            html.Div([
                html.Br(),
                html.Img(
                    src='https://www.eluniversal.com.co/binrepository/1000x563/0c0/0d0/none/13704/FYVN/colegio-clemente-manuel-zabala-flor-del-campo_8318919_20230822124017.jpg',
                    style={'width': '60%'},  # Tamaño de la imagen
                    className='mx-auto d-block'),
                html.Br()
            ])  # Estilo para mostrar en línea
        ])

    elif active_tab == "empresa":
        return html.Div([
            html.H3("MISIÓN", style={'color': '#007BFF', 'font-weight': 'bold'}),
            html.P("Garantizar la seguridad de los colegios en Colombia a través de un "
                   "seguimiento constante y alertas tempranas de inundaciones, proporcionando soluciones "
                   "tecnológicas y servicios de prevención de alta calidad."),
            html.H3("VISIÓN", style={'color': '#007BFF', 'font-weight': 'bold'}),
            html.P("Ser líderes en la protección de la comunidad escolar en Colombia, utilizando la "
                   "tecnología más avanzada para prevenir inundaciones y brindar tranquilidad a las "
                   "instituciones educativas y sus familias."),
            html.H3("OBJETIVOS", style={'color': '#007BFF', 'font-weight': 'bold'}),       
            html.Ul([
                html.Li("Desarrollar sistemas de monitoreo avanzados para detectar inundaciones en tiempo real."),
                html.Li("Establecer alianzas estratégicas con colegios y autoridades locales."),
                html.Li("Capacitar a nuestros equipos en la gestión de riesgos y respuestas ante emergencias."),
                html.Li("Ampliar nuestra cobertura en todo el territorio colombiano."),
                html.Li("Promover la conciencia sobre la importancia de la seguridad escolar.")
            ]),
        ])
    elif active_tab == "conocenos":
        return html.Div([
            html.H4("Contacto", style={'color': '#007BFF', 'font-weight': 'bold'}),
            html.Br(),
            html.Strong("Nombre de la Empresa:"),
            " Alerta Escolar Colombia S.A.",
            html.Br(),
            html.Strong("Dirección de la Oficina Principal:"),
            " Calle 123 #45-67, Bogotá, Colombia",
            html.Br(),
            html.Strong("Teléfono Principal:"),
            " +57 301 234 5678",
            html.Br(),
            html.Strong("Correo Electrónico de Atención al Cliente:"),
            " contacto@alertaescolarcolombia.com",
            html.H4("Redes Sociales", style={'color': '#007BFF', 'font-weight': 'bold'}),
            html.Ul([
                html.Li('Facebook: facebook.com/AlertaEscolarCol'),
                html.Li('Twitter: twitter.com/AlertaEscolarCol'),
                html.Li('LinkedIn: linkedin.com/company/AlertaEscolarCol'),
                html.Li('Instagram: instagram.com/Alerta_EscolarCol')
              ]),
            html.H4("Horario de Atención al Cliente:", style={'color': '#007BFF', 'font-weight': 'bold'}),
            html.P("Lunes a Viernes: 8:00 AM - 5:00 PM"),
            html.P("Sábados: 9:00 AM - 1:00 PM"),
            html.H4("Contacto de Emergencia 24/7:", style={'color': '#007BFF', 'font-weight': 'bold'}),
            html.P("Teléfono de Emergencia: +57 3 333 3333")
        ])
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
