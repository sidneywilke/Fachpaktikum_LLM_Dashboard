import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/',
        external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
    )

    # Create Dash Layout
    dash_app.layout = html.Div([
        html.H1('LLM Performance Dashboard'),
        dcc.Graph(id='example-graph'),
        html.Div([
            dcc.Input(
                id='input-field',
                type='text',
                value='Input data here'
            ),
            html.Button('Submit', id='submit-button', n_clicks=0),
        ]),
        html.Div(id='output-div')
    ])

    return dash_app
