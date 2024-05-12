from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


def init_dashboard(server):
    dash_app = Dash(server=server, routes_pathname_prefix='/', external_stylesheets=[dbc.themes.BOOTSTRAP])

    dash_app.layout = dbc.Container([
        dbc.Row(
            dbc.Col(html.H1("LLM Comparative Response Dashboard", className="text-center"), width=12)
        ),
        dbc.Row([
            dbc.Col([
                dcc.Input(
                    id='input-text',
                    type='text',
                    placeholder='Enter your prompt here...',
                    style={'width': '70%', 'display': 'inline-block'}
                ),
                dcc.Dropdown(
                    id='model-dropdown-1',
                    options=[
                        {'label': 'Phi3', 'value': 'phi3'},
                        {'label': 'Mistral', 'value': 'mistral'},
                        {'label': 'Gemma', 'value': 'gemma'}
                    ],
                    value='phi3',
                    style={'width': '25%', 'display': 'inline-block', 'margin-left': '5px'}
                ),
                dcc.Dropdown(
                    id='model-dropdown-2',
                    options=[
                        {'label': 'Phi3', 'value': 'phi3'},
                        {'label': 'Mistral', 'value': 'mistral'},
                        {'label': 'Gemma', 'value': 'gemma'}
                    ],
                    value='mistral',
                    style={'width': '25%', 'display': 'inline-block', 'margin-left': '5px'}
                ),
                html.Button('Submit', id='submit-button', n_clicks=0, className="btn btn-primary ml-2")
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                html.Div(id='output-container-1', children='Response from Model 1 will appear here.'),
                dcc.Interval(id='interval-component-1', interval=1000, n_intervals=0, disabled=True)
            ], width=6),
            dbc.Col([
                html.Div(id='output-container-2', children='Response from Model 2 will appear here.'),
                dcc.Interval(id='interval-component-2', interval=1000, n_intervals=0, disabled=True)
            ], width=6)
        ])
    ], fluid=True)

    return dash_app
