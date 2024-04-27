from dash.dependencies import Input, Output, State

def register_callbacks(dash_app):
    @dash_app.callback(
        Output('example-graph', 'figure'),
        [Input('submit-button', 'n_clicks')],
        [State('input-field', 'value')]
    )
    def update_graph(n_clicks, input_value):
        # Hier würde normalerweise die Logik stehen, um Daten zu verarbeiten und den Graphen zu aktualisieren
        # Einfaches Beispiel:
        x = ['A', 'B', 'C']
        y = [n_clicks, n_clicks * 2, n_clicks * 3]
        return {
            'data': [{'x': x, 'y': y, 'type': 'bar'}],
            'layout': {
                'title': f'Graph Updated {n_clicks} times, Input: {input_value}'
            }
        }
