from dash.dependencies import Input, Output, State
import dash
from ..model_manager import ModelManager

model_manager = ModelManager()

responses = ['', '', '']  # To store full responses for typing effect
current_indices = [0, 0, 0]  # To keep track of the current character index for each response

def register_callbacks(dash_app):
    @dash_app.callback(
        [Output('output-container-1', 'children'),
         Output('output-container-2', 'children'),
         Output('output-container-3', 'children'),
         Output('interval-typing-1', 'disabled'),
         Output('interval-typing-2', 'disabled'),
         Output('interval-typing-3', 'disabled')],
        [Input('submit-button', 'n_clicks'),
         Input('interval-typing-1', 'n_intervals'),
         Input('interval-typing-2', 'n_intervals'),
         Input('interval-typing-3', 'n_intervals')],
        [State('input-text', 'value'),
         State('model-dropdown-1', 'value'),
         State('model-dropdown-2', 'value'),
         State('model-dropdown-3', 'value'),
         State('typing-effect-checkbox', 'value')]
    )
    def update_output(n_clicks, n_intervals_1, n_intervals_2, n_intervals_3, input_value, model1, model2, model3, typing_effect):
        global responses, current_indices
        ctx = dash.callback_context

        if not ctx.triggered:
            return dash.no_update, dash.no_update, dash.no_update, True, True, True

        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'submit-button' and n_clicks > 0:
            responses[0] = model_manager.get_response(input_value, model=model1)
            responses[1] = model_manager.get_response(input_value, model=model2)
            responses[2] = model_manager.get_response(input_value, model=model3)
            current_indices = [0, 0, 0]
            if 'enabled' in typing_effect:
                return '', '', '', False, False, False
            else:
                return responses[0], responses[1], responses[2], True, True, True

        new_text_1 = responses[0][:current_indices[0]] if current_indices[0] < len(responses[0]) else responses[0]
        new_text_2 = responses[1][:current_indices[1]] if current_indices[1] < len(responses[1]) else responses[1]
        new_text_3 = responses[2][:current_indices[2]] if current_indices[2] < len(responses[2]) else responses[2]

        disabled_1, disabled_2, disabled_3 = True, True, True

        if button_id == 'interval-typing-1' and current_indices[0] < len(responses[0]):
            current_indices[0] += 1
            disabled_1 = False

        if button_id == 'interval-typing-2' and current_indices[1] < len(responses[1]):
            current_indices[1] += 1
            disabled_2 = False

        if button_id == 'interval-typing-3' and current_indices[2] < len(responses[2]):
            current_indices[2] += 1
            disabled_3 = False

        return new_text_1, new_text_2, new_text_3, disabled_1, disabled_2, disabled_3
