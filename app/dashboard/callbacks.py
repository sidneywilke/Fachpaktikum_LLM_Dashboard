
from dash.dependencies import Input, Output, State

from ..model_manager import ModelManager

model_manager = ModelManager()

def register_callbacks(dash_app):
    @dash_app.callback(
        Output('interval-component', 'disabled'),
        Input('submit-button', 'n_clicks'),
        State('input-text', 'value')
    )
    def trigger_streaming(n_clicks, input_value):
        global stream_generator
        if n_clicks > 0:
            stream_generator = model_manager.get_response(input_value)  # Starten des Generators
            return False  # Aktiviert das Interval
        return True

    @dash_app.callback(
        Output('output-container', 'children'),
        Input('interval-component', 'n_intervals'),
        State('output-container', 'children')
    )
    def update_output_div(n, existing_text):
        try:
            new_text = next(stream_generator)  # Holt das nächste Wort
            return existing_text + new_text if existing_text else new_text
        except StopIteration:
            return existing_text  # Stoppt die Aktualisierung, wenn alle Worte abgerufen wurden


from dash.dependencies import Input, Output, State
import requests

stream_generator_1 = None
stream_generator_2 = None

def register_callbacks(dash_app):
    @dash_app.callback(
        [Output('interval-component-1', 'disabled'), Output('interval-component-2', 'disabled')],
        Input('submit-button', 'n_clicks'),
        [State('input-text', 'value'), State('model-dropdown-1', 'value'), State('model-dropdown-2', 'value')]
    )
    def trigger_streaming(n_clicks, input_value, model1, model2):
        global stream_generator_1, stream_generator_2
        if n_clicks > 0:
            stream_generator_1 = model_manager.get_response(input_value, model1)
            stream_generator_2 = model_manager.get_response(input_value, model2)  # Starten des Generators
            return False, False  # Aktiviert beide Intervals
        return True, True

    @dash_app.callback(
        [Output('output-container-1', 'children'), Output('output-container-2', 'children')],
        [Input('interval-component-1', 'n_intervals'), Input('interval-component-2', 'n_intervals')],
        [State('output-container-1', 'children'), State('output-container-2', 'children')]
    )
    def update_output_div(n1, n2, existing_text_1, existing_text_2):
        global stream_generator_1, stream_generator_2
        new_text_1, new_text_2 = existing_text_1, existing_text_2
        if n1 is not None:
            try:
                new_text_1 += next(stream_generator_1)
            except StopIteration:
                pass
        if n2 is not None:
            try:
                new_text_2 += next(stream_generator_2)
            except StopIteration:
                pass
        return new_text_1, new_text_2
