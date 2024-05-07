import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output




def init_dashboard(server):
    """Initialize the Dash application on the provided Flask server."""

    # Dash App erstellen
    dash_app = Dash(server=server, routes_pathname_prefix='/', external_stylesheets=[dbc.themes.BOOTSTRAP])

    # Layout der Dash App definieren
    dash_app.layout = dbc.Container([
        dbc.Row(
            dbc.Col(html.H1("LLM Response Dashboard", className="text-center"), width=12)
        ),
        dbc.Row(
            dbc.Col([
                dcc.Input(
                    id='input-text',
                    type='text',
                    placeholder='Enter your prompt here...',
                    style={'width': '100%', 'height': '40px'}
                ),
                dcc.Dropdown(
                    id='model-dropdown',
                    options=[
                        {'label': 'Phi3', 'value': 'phi3'},
                        {'label': 'Mistral', 'value': 'mistral'},
                        {'label': 'Gemma', 'value': 'gemma'}
                    ],
                    value='phi3',  # Standardmodell auswählen
                    style={'width': '25%', 'display': 'inline-block', 'margin-left': '5px'}
                ),
                html.Button('Submit', id='submit-button', n_clicks=0, className="btn btn-primary mt-2")
            ], width=6)
        ),
        dbc.Row(
            dbc.Col([
                html.Div(id='output-container', children='Enter a prompt and press submit.')
            ], width=12)
        )
    ], fluid=True)

    return dash_app

