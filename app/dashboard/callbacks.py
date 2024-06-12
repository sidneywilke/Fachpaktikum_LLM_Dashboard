from dash.dependencies import Input, Output, State
import dash
from ..model_manager import ModelManager
import time

model_manager = ModelManager()

responses = ['', '', '']  # To store full responses for typing effect
current_indices = [0, 0, 0]  # To keep track of the current word index for each response
start_times = [0, 0, 0]  # To record the start time of each model's response
end_times = [0, 0, 0]  # To record the end time of each model's response
time_1 = 0

def get_words(text):
    return text.split()

def register_callbacks(dash_app):
    @dash_app.callback(
        [Output('output-container-1', 'children'),
         Output('output-container-2', 'children'),
         Output('output-container-3', 'children'),
         Output('interval-typing-1', 'disabled'),
         Output('interval-typing-2', 'disabled'),
         Output('interval-typing-3', 'disabled'),
         Output('response-time-1', 'value'),
         Output('response-time-2', 'value'),
         Output('response-time-3', 'value'),
         Output('like-button-1', 'style'),
         Output('dislike-button-1', 'style'),
         Output('like-button-2', 'style'),
         Output('dislike-button-2', 'style'),
         Output('like-button-3', 'style'),
         Output('dislike-button-3', 'style')],
        [Input('submit-button', 'n_clicks'),
         Input('interval-typing-1', 'n_intervals'),
         Input('interval-typing-2', 'n_intervals'),
         Input('interval-typing-3', 'n_intervals')],
        [State('input-text', 'value'),
         State('model-dropdown-1', 'value'),
         State('model-dropdown-2', 'value'),
         State('model-dropdown-3', 'value')]
    )
    def update_output(n_clicks, n_intervals_1, n_intervals_2, n_intervals_3, input_value, model1, model2, model3, ):
        global responses, current_indices, start_times, end_times
        ctx = dash.callback_context

        if not ctx.triggered:
            return dash.no_update, dash.no_update, dash.no_update, True, True, True, 0, 0, 0, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}

        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        # Start processing the first model's response
        if button_id == 'submit-button' and n_clicks > 0:
            start_times[0] = time.time()
            responses[0] = model_manager.get_response(input_value, model=model1)
            end_times[0] = time.time()
            current_indices[0] = 0
            # Immediately proceed to the next model if typing effect is disabled
            start_times[1] = time.time()
            responses[1] = model_manager.get_response(input_value, model=model2)
            end_times[1] = time.time()
            start_times[2] = time.time()
            responses[2] = model_manager.get_response(input_value, model=model3)
            end_times[2] = time.time()
            print(round(end_times[0] - start_times[0]))
            return responses[0], responses[1], responses[2], True, True, True, round(end_times[0] - start_times[0]), end_times[1] - start_times[1], end_times[2] - start_times[2],  {'display': 'block'}, {'display': 'block'}, {'display': 'block'}, {'display': 'block'}, {'display': 'block'}, {'display': 'block'}

