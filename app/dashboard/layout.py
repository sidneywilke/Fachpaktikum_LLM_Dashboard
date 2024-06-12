from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
from .callbacks import time_1

def init_dashboard(server):
    dash_app = Dash(server=server, routes_pathname_prefix='/', external_stylesheets=[dbc.themes.BOOTSTRAP])

    dash_app.layout = dbc.Container([
        dbc.Row(
            dbc.Col(html.H1("LLM Dashboard", className="bg-primary text-white p-2 my-2 text-center rounded", style={'borderRadius': '4'}),style={'borderRadius': '4'}, width=12)
        ),
        dbc.Row([
            dbc.Col([
                dcc.Input(
                    id='input-text',
                    type='text',
                    className='dbc rounded border',
                    placeholder='Enter your prompt here...',
                    style={'width': '100%'}
                )
            ], width=6, className='d-flex text-center'),
            dbc.Col(dbc.Row([
                dbc.Col(
                    dcc.Dropdown(
                        id='model-dropdown-1',
                        className="dbc w-100 mx-2",
                        options=[
                            {'label': 'Phi3', 'value': 'phi3'},
                            {'label': 'Mistral', 'value': 'mistral'},
                            {'label': 'Gemma', 'value': 'gemma'}
                        ],
                        value='phi3',
                        style={'display': 'inline-block', 'width':'100%'}
                    ), width=4, style={'display': 'flex', 'align-items': 'center', 'marginTop': '5px'}),
                dbc.Col(
                    dcc.Dropdown(
                        id='model-dropdown-2',
                        options=[
                            {'label': 'Phi3', 'value': 'phi3'},
                            {'label': 'Mistral', 'value': 'mistral'},
                            {'label': 'Gemma', 'value': 'gemma'}
                        ],
                        value='mistral',
                        style={'display': 'inline-block', 'width':'100%' }
                    ), width=4, style={'display': 'flex', 'align-items': 'center', 'marginTop': '5px'}),
                dbc.Col(
                    dcc.Dropdown(
                        id='model-dropdown-3',
                        options=[
                            {'label': 'Phi3', 'value': 'phi3'},
                            {'label': 'Mistral', 'value': 'mistral'},
                            {'label': 'Gemma', 'value': 'gemma'}
                        ],
                        value='gemma',
                        style={'display': 'inline-block', 'width':'100%',}
                ), width=4, style={'display': 'flex', 'align-items': 'center', 'marginTop': '5px'}),
            ], className='w-100'), width=5, className='d-flex text-center'),
            dbc.Col([
                html.Button('Submit', id='submit-button', n_clicks=0, className="btn btn-primary ml-2")
            ], width=1, className='d-flex justify-content-end px-0'),
        ], className="w-100 mt-2 gx-0", style={'height':'50px', 'marginRight': '0px'}),
        dbc.Row(dcc.Checklist(
                    id='typing-effect-checkbox',
                    options=[{'label': 'Enable Typing Effect', 'value': 'enabled'}],
                    value=['enabled'],
                    className='mx-2'

                ),className='w-100 mt-2 mb-4 gx-0'),
        dbc.Row([
            dbc.Col([
                dcc.Markdown(id='output-container-1', children='Response from Model 1 will appear here.'),
                dcc.Interval(id='interval-typing-1', interval=50, n_intervals=0, disabled=True)
            ], width=8, className='p-3', style={'align-items': 'center','boxShadow': 'rgb(178 178 178 / 30%) 0px 0px 16px 2px', 'borderRadius': '4px'}),
            dbc.Col([
                daq.Gauge(
                    id='response-time-1',
                    value= 0,
                    label='Default',
                    max=30,
                    min=0,
                ),
            ], width='auto', className='p-3 mx-2',
                style={'boxShadow': 'rgb(178 178 178 / 30%) 0px 0px 16px 2px', 'borderRadius': '4px', 'width':'450px'}),
            dbc.Col([
                html.Button('Like', id='like-button',  className="btn btn-primary mx-2"),
                html.Button('Dislike', id='dislike-button', className="btn btn-primary mx-2")
            ],width='auto', className='p-3 d-flex justify-content-evenly',
                style={'boxShadow': 'rgb(178 178 178 / 30%) 0px 0px 16px 2px', 'borderRadius': '4px', 'width': '180px'})
        ], className='mx-1 my-2'),
        dbc.Row([
            dbc.Col([
                dcc.Markdown(id='output-container-2', children='Response from Model 2 will appear here.'),

                dcc.Interval(id='interval-typing-2', interval=50, n_intervals=0, disabled=True)
            ], width=8, className='p-3 mx-2', style={'boxShadow': 'rgb(178 178 178 / 30%) 0px 0px 16px 2px', 'borderRadius': '4px'}),
            dbc.Col([
                html.Div(id='response-time-2', children='Time taken by Model 2: Not started'),
            ], width=2, className='p-3',
                style={'boxShadow': 'rgb(178 178 178 / 30%) 0px 0px 16px 2px', 'borderRadius': '4px'})
        ], className='mx-1 my-2'),
        dbc.Row([
            dbc.Col([
                dcc.Markdown(id='output-container-3', children='Response from Model 3 will appear here.'),
                dcc.Interval(id='interval-typing-3', interval=50, n_intervals=0, disabled=True)
            ], width=8, className='p-3 mx-2', style={'boxShadow': 'rgb(178 178 178 / 30%) 0px 0px 16px 2px', 'borderRadius': '4px'}),
            dbc.Col([
                daq.Gauge(
                    value=5,
                    label='Default',
                    max=20,
                    min=0,
                ),
                html.Div(id='response-time-3', children='Time taken by Model 3: Not started'),
            ], width=2, className='p-3',
                style={'boxShadow': 'rgb(178 178 178 / 30%) 0px 0px 16px 2px', 'borderRadius': '4px'})
        ], className='mx-1 my-2')
    ], fluid=True)

    return dash_app
