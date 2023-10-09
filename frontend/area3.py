import dash
from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc
from dash import html

area3 = dbc.Container([
    dcc.Store(id="store"),
    dbc.Row([        
        dbc.Tabs(
            [
                dbc.Tab(label="NOTICIAS", tab_id="noticias"),
                dbc.Tab(label="EMPRESA", tab_id="empresa"),
                dbc.Tab(label="CONOCENOS", tab_id="conocenos"),
            ],
            id="tabs",
            active_tab="noticias",
        ),
        html.Div(id="tab-content", className="p-4"),
    ])
])

articulos = [
    {
        'titulo': "Impacto de lluvias deja a más de 1.600.000 estudiantes sin clase por daños en colegios",
        'ubicacion': '📍 PIE DE CUESTA - SANTANDER',
        'url': 'https://www.bluradio.com/nacion/impacto-de-lluvias-deja-a-mas-de-1-600-000-estudiantes-sin-clases-por-danos-en-colegios-rg10',
        'imagen': 'https://caracoltv.brightspotcdn.com/dims4/default/ce72944/2147483647/strip/true/crop/720x542+0+0/resize/720x542!/format/webp/quality/90/?url=http%3A%2F%2Fcaracol-brightspot.s3.amazonaws.com%2F35%2Fbc%2F5ce64d5a42a5b784987750874597%2Fwhatsapp-image-2022-09-05-at-7.06.02%20AM%20%281%29.jpeg'
    },
    {
        'titulo': "Colegios públicos en estado critico tras inundaciones por fuertes lluvias",
        'ubicacion': '📍 CARTAGENA - BOLIVAR',
        'url': 'https://www.eluniversal.com.co/cartagena/colegios-publicos-en-estado-critico-tras-inundaciones-por-fuertes-lluvias-EH8845314',
        'imagen': 'https://www.eluniversal.com.co/binrepository/1000x563/0c0/0d0/none/13704/FYVN/colegio-clemente-manuel-zabala-flor-del-campo_8318919_20230822124017.jpg'
    },
    {
        'titulo': "Por fuertes lluvias quedó inundado el colegio que fue inaugurado por Shakira en Barranquilla",
        'ubicacion': '📍 CARTAGENA - BOLIVAR',
        'url': 'https://www.elcolombiano.com/colombia/por-fuertes-lluvias-quedoinundado-colegio-que-fue-inaugurado-por-shakira-en-barranquilla-CG22601553',
        'imagen': 'https://estaticos.elcolombiano.com/binrepository/848x565/0c0/780d565/none/11101/OEOU/foto-colprensa-y-captura-de-video-f_43452825_20231006202422.jpg'
    },
]

def render_news_tab():
    """Compnente de renderización para la pestaña noticias

    Returns:
        html.Div: component.
    """
    return [
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Img(
                            src=articulo['imagen'],
                            style={'width': '35%'},  # Tamaño de la imagen
                            className=''
                        ), 
                        dbc.Stack(
                            children=[
                                html.H5(articulo['titulo']),
                                html.Span(articulo['ubicacion'], className="text-uppercase"),
                                dcc.Link('Leer más', href=articulo['url'], target='_blank')  
                            ],
                            direction="column",
                            className="gap-2"
                        )
                    ],
                    className="d-flex flex-row gap-2 mb-2"
                )
            ]
        ) for articulo in articulos
    ]

def render_empresa_tab():
    """Componente de renderización para la pestaña empresa
    Returns:
        html.Div: component.
    """
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

def render_conocenos_tab():
    """Componente de renderización para la pestaña conocenos
    Returns:
        html.Div: component.
    """
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
