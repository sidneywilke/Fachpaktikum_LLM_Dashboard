
from dash.dependencies import Input, Output, State

from ..model_manager import ModelManager

model_manager = ModelManager()

from dash.dependencies import Input, Output, State
import requests

stream_generator_1 = None
stream_generator_2 = None
stream_generator_3 = None

def register_callbacks(dash_app):
    @dash_app.callback(
        [Output('interval-component-1', 'disabled'), Output('interval-component-2', 'disabled'), Output('interval-component-3', 'disabled')],
        Input('submit-button', 'n_clicks'),
        [State('input-text', 'value'), State('model-dropdown-1', 'value'), State('model-dropdown-2', 'value'), State('model-dropdown-3', 'value')]
    )
    def trigger_streaming(n_clicks, input_value, model1, model2, model3):
        global stream_generator_1, stream_generator_2, stream_generator_3
        if n_clicks > 0:
            stream_generator_1 = model_manager.get_response(input_value, model1)
            stream_generator_2 = model_manager.get_response(input_value, model2)
            stream_generator_3 = model_manager.get_response(input_value, model3) # Starten des Generators
            return False, False, False  # Aktiviert beide Intervals
        return True, True, True

    @dash_app.callback(
        [Output('output-container-1', 'children'), Output('output-container-2', 'children'), Output('output-container-3', 'children')],
        [Input('interval-component-1', 'n_intervals'), Input('interval-component-2', 'n_intervals'), Input('interval-component-3', 'n_intervals')],
        [State('output-container-1', 'children'), State('output-container-2', 'children'), State('output-container-3', 'children')]
    )
    def update_output_div(n1, n2, n3, existing_text_1, existing_text_2, existing_text_3):
        global stream_generator_1, stream_generator_2, stream_generator_3
        new_text_1, new_text_2, new_text_3 = existing_text_1, existing_text_2, existing_text_3
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
        if n3 is not None:
            try:
                new_text_3 += next(stream_generator_3)
            except StopIteration:
                pass
        return new_text_1, new_text_2, new_text_3
