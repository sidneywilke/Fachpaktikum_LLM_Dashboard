
from dash.dependencies import Input, Output, State
import requests

from ..model_manager import ModelManager

model_manager = ModelManager()


def register_callbacks(dash_app):
    @dash_app.callback(
        Output('output-container', 'children'),
        [Input('submit-button', 'n_clicks')],
        [State('input-text', 'value'), State('model-dropdown', 'value')]
    )
    def update_output(n_clicks, input_value, selected_mode):
        if n_clicks > 0 and input_value:
            print(input_value)
            response = model_manager.get_response(input_value, selected_mode)['message']['content']

            print(response)
            return response
        return "Enter a prompt and press submit."