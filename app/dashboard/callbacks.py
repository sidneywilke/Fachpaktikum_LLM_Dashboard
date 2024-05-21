from dash.dependencies import Input, Output, State
from ..model_manager import ModelManager

model_manager = ModelManager()

def register_callbacks(dash_app):
    @dash_app.callback(
        [Output('output-container-1', 'children'),
         Output('output-container-2', 'children'),
         Output('output-container-3', 'children')],
        Input('submit-button', 'n_clicks'),
        [State('input-text', 'value'),
         State('model-dropdown-1', 'value'),
         State('model-dropdown-2', 'value'),
         State('model-dropdown-3', 'value')]
    )
    def update_output(n_clicks, input_value, model1, model2, model3):
        if n_clicks > 0:
            response_1 = model_manager.get_response(input_value, model=model1)
            response_2 = model_manager.get_response(input_value, model=model2)
            response_3 = model_manager.get_response(input_value, model=model3)
            return response_1, response_2, response_3
        return '', '', ''
