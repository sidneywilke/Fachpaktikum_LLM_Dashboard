
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash import dash_table

def init_dashboard(server, columns, data):
    dash_app = Dash(server=server, routes_pathname_prefix='/', assets_folder='assets', assets_url_path='/assets/', external_stylesheets=[dbc.themes.BOOTSTRAP])

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
                            {'label': 'Phi3     4,7/5★', 'value': 'phi3'},
                            {'label': 'Mistral      4,2/5★', 'value': 'mistral'},
                            {'label': 'Gemma        3.8/5★', 'value': 'gemma'}
                        ],
                        value='phi3',
                        style={'display': 'inline-block', 'width':'100%'}
                    ), width=4, style={'display': 'flex', 'align-items': 'center', 'marginTop': '5px'}),
                dbc.Col(
                    dcc.Dropdown(
                        id='model-dropdown-2',
                        options=[
                            {'label': 'Phi3     4,7/5★', 'value': 'phi3'},
                            {'label': 'Mistral      4,2/5★', 'value': 'mistral'},
                            {'label': 'Gemma        3.8/5★', 'value': 'gemma'}
                        ],
                        value='mistral',
                        style={'display': 'inline-block', 'width':'100%' }
                    ), width=4, style={'display': 'flex', 'align-items': 'center', 'marginTop': '5px'}),
                dbc.Col(
                    dcc.Dropdown(
                        id='model-dropdown-3',
                        options=[
                            {'label': 'Phi3     4,7/5★', 'value': 'phi3'},
                            {'label': 'Mistral      4,2/5★', 'value': 'mistral'},
                            {'label': 'Gemma        3.8/5★', 'value': 'gemma'}
                        ],
                        value='gemma',
                        style={'display': 'inline-block', 'width':'100%',}
                ), width=4, style={'display': 'flex', 'align-items': 'center', 'marginTop': '5px'}),
            ], className='w-100'), width=5, className='d-flex text-center'),
            dbc.Col([
                html.Button('Submit', id='submit-button', n_clicks=0, className="btn btn-primary ml-2")
            ], width=1, className='d-flex justify-content-end px-0'),
        ], className="w-100 mt-2 gx-0", style={'height':'50px', 'marginRight': '0px'}),
        dbc.Row([
            dbc.Col([
                dcc.Markdown(id='output-container-1', children='Response from Model 1 will appear here.'),
                dcc.Interval(id='interval-typing-1', interval=50, n_intervals=0, disabled=True),
                dbc.Col([
                    html.Button('\U0001F642', id='like-button-1', className="btn btn-success mx-2", style={'display': 'none'}),
                    html.Button('\U0001F610', id='neutral-button-1', className="btn btn-secondary mx-2",
                               style={'display': 'none'}),
                    html.Button('\U0001F641', id='dislike-button-1', className="btn btn-danger mx-2", style={'display': 'none'})
                ], className='mx-auto p-3 d-flex justify-content-evenly', style={'width': '180px'})
            ], width=9, className='p-3', style={'align-items': 'center','boxShadow': 'rgb(178 178 178 / 30%) 0px 0px 16px 2px', 'borderRadius': '4px'}),
            dbc.Col([
                daq.Gauge(
                    id='response-time-1',
                    showCurrentValue=True,
                    value=0,
                    label='Response Time Model 1',
                    max=20,
                    min=0,
                    style={'height': '250px'}
                ),
            ], width='auto', className='p-3 mx-2',
                style={'boxShadow': 'rgb(178 178 178 / 30%) 0px 0px 16px 2px', 'borderRadius': '4px', 'width':'450px'}),

        ], className='mx-1 my-2'),
        dbc.Row([
            dbc.Col([
                dcc.Markdown(id='output-container-2', children='Response from Model 2 will appear here.'),
                dcc.Interval(id='interval-typing-2', interval=50, n_intervals=0, disabled=True),
                dbc.Col([
                    html.Button('\U0001F642', id='like-button-2', className="btn btn-success mx-2",
                                style={'display': 'none'}),
                    html.Button('\U0001F610', id='neutral-button-2', className="btn btn-secondary  mx-2",
                                style={'display': 'none'}),
                    html.Button('\U0001F641', id='dislike-button-2', className="btn btn-danger mx-2",
                                style={'display': 'none'})
                ], className='mx-auto p-3 d-flex justify-content-evenly', style={'width': '180px'})
            ], width=9, className='p-3', style={'boxShadow': 'rgb(178 178 178 / 30%) 0px 0px 16px 2px', 'borderRadius': '4px'}),
            dbc.Col([
                daq.Gauge(
                    id='response-time-2',
                    showCurrentValue=True,
                    value=0,
                    label='Response Time Model 2',
                    max=20,
                    min=0,
                    style={'height': '250px'}
                ),
            ], width='auto', className='p-3 mx-2',
                style={'boxShadow': 'rgb(178 178 178 / 30%) 0px 0px 16px 2px', 'borderRadius': '4px',
                       'width': '450px'}),

        ], className='mx-1 my-2'),
        dbc.Row([
            dbc.Col([
                dcc.Markdown(id='output-container-3', children='Response from Model 3 will appear here.'),
                dcc.Interval(id='interval-typing-3', interval=50, n_intervals=0, disabled=True),
                dbc.Col([
                    html.Button('\U0001F642', id='like-button-3', className="btn btn-success mx-2",
                                style={'display': 'none'}),
                    html.Button('\U0001F610', id='neutral-button-3', className="btn btn-secondary  mx-2",
                                style={'display': 'none'}),
                    html.Button('\U0001F641', id='dislike-button-3', className="btn btn-danger mx-2",
                                style={'display': 'none'})
                ], className='mx-auto p-3 d-flex justify-content-evenly', style={'width': '180px'})
            ], width=9, className='p-3', style={'boxShadow': 'rgb(178 178 178 / 30%) 0px 0px 16px 2px', 'borderRadius': '4px'}),
            dbc.Col([
                daq.Gauge(
                    id='response-time-3',
                    showCurrentValue=True,
                    value=0,
                    label='Response Time Model 3',
                    max=20,
                    min=0,
                    style={'height': '250px'}
                ),

            ], width='auto', className='p-3 mx-2',
                style={'boxShadow': 'rgb(178 178 178 / 30%) 0px 0px 16px 2px', 'borderRadius': '4px',
                       'width': '450px'}),

        ], className='mx-1 my-2'),
        dbc.Row([
            dbc.Col([
                dash_table.DataTable(
                    id='model-comparison-table',
                    editable=True,
                    filter_action="native",
                    sort_action="native",
                    columns=columns,
                    data=data,
                    style_cell={
                        'textAlign': 'left',
                        'padding': '5px',
                        'font-family': 'var(--bs-body-font-family)'
                    },
                    style_header={
                        'fontWeight': 'bold',
                        'font-family': 'var(--bs-body-font-family)'
                    },
                    style_table={
                        'width': '100%',
                        'font-family': 'var(--bs-body-font-family)',
                    },
                    style_data_conditional=[
                        {
                            'if': {'column_id': col_id},
                            'backgroundColor': '#FFFFE0'
                        } for col_id in ["ttft", "tpok", "tgt", "tps", "quality"]
                    ] + [
                        {
                            'if': {'column_id': col_id},
                            'backgroundColor': '#E0F7FF'  # Blue
                        } for col_id in ["privacy", "ethics", "bias", "non-toxicity"]
                    ],
                    css = [{
                        'selector': '.dash-spreadsheet-container',
                        'rule': 'box-shadow: rgb(178 178 178 / 30%) 0px 0px 16px 2px; overflow: hidden;'
                    }],
                )
            ], className='mx-3 my-3 gx-0 w-100')
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                    id='column-selector',
                    options=[{'label': col['name'], 'value': col['id']} for col in columns if col['id'] != 'model'],
                    value='quality',
                    clearable=False,
                    className="dbc w-50 mx-auto"
                ),
                dcc.Graph(id='bar-chart', className="mx-auto", style={'width': '30%'})
            ], width=12)
        ], className='mx-1 my-2')
    ], fluid=True, )


    return dash_app
