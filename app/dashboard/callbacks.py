from dash.dependencies import Input, Output, State
import dash
from ..model_manager import ModelManager
import time

model_manager = ModelManager()

responses = ['', '', '']  # To store full responses for typing effect
current_indices = [0, 0, 0]  # To keep track of the current word index for each response
start_times = [0, 0, 0]  # To record the start time of each model's response
end_times = [0, 0, 0]  # To record the end time of each model's response

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
         Output('response-time-1', 'children'),
         Output('response-time-2', 'children'),
         Output('response-time-3', 'children')],
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
        global responses, current_indices, start_times, end_times
        ctx = dash.callback_context

        if not ctx.triggered:
            return dash.no_update, dash.no_update, dash.no_update, True, True, True, 'Time taken by Model 1: Not started', 'Time taken by Model 2: Not started', 'Time taken by Model 3: Not started'

        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        # Start processing the first model's response
        if button_id == 'submit-button' and n_clicks > 0:
            start_times[0] = time.time()
            responses[0] = model_manager.get_response(input_value, model=model1)
            end_times[0] = time.time()
            current_indices[0] = 0
            if 'enabled' in typing_effect:
                return '', dash.no_update, dash.no_update, False, True, True, f'Time taken by Model 1: {end_times[0] - start_times[0]:.2f} seconds', dash.no_update, dash.no_update
            else:
                # Immediately proceed to the next model if typing effect is disabled
                start_times[1] = time.time()
                responses[1] = model_manager.get_response(input_value, model=model2)
                end_times[1] = time.time()
                start_times[2] = time.time()
                responses[2] = model_manager.get_response(input_value, model=model3)
                end_times[2] = time.time()
                return responses[0], responses[1], responses[2], True, True, True, f'Time taken by Model 1: {end_times[0] - start_times[0]:.2f} seconds', f'Time taken by Model 2: {end_times[1] - start_times[1]:.2f} seconds', f'Time taken by Model 3: {end_times[2] - start_times[2]:.2f} seconds'

        # Process the typing effect for the first model
        if button_id == 'interval-typing-1' and current_indices[0] < len(get_words(responses[0])):
            words = get_words(responses[0])
            new_text_1 = ' '.join(words[:current_indices[0] + 1])
            current_indices[0] += 1
            if current_indices[0] >= len(words):
                start_times[1] = time.time()
                responses[1] = model_manager.get_response(input_value, model=model2)
                end_times[1] = time.time()
                current_indices[1] = 0
                if 'enabled' in typing_effect:
                    return new_text_1, dash.no_update, dash.no_update, True, False, True, f'Time taken by Model 1: {end_times[0] - start_times[0]:.2f} seconds', dash.no_update, dash.no_update
                else:
                    return new_text_1, responses[1], dash.no_update, True, True, True, f'Time taken by Model 1: {end_times[0] - start_times[0]:.2f} seconds', f'Time taken by Model 2: {end_times[1] - start_times[1]:.2f} seconds', dash.no_update
            return new_text_1, dash.no_update, dash.no_update, False, True, True, dash.no_update, dash.no_update, dash.no_update

        # Process the typing effect for the second model
        if button_id == 'interval-typing-2' and current_indices[1] < len(get_words(responses[1])):
            words = get_words(responses[1])
            new_text_2 = ' '.join(words[:current_indices[1] + 1])
            current_indices[1] += 1
            if current_indices[1] >= len(words):
                start_times[2] = time.time()
                responses[2] = model_manager.get_response(input_value, model=model3)
                end_times[2] = time.time()
                current_indices[2] = 0
                if 'enabled' in typing_effect:
                    return dash.no_update, new_text_2, dash.no_update, True, True, False, dash.no_update, f'Time taken by Model 2: {end_times[1] - start_times[1]:.2f} seconds', dash.no_update
                else:
                    return dash.no_update, new_text_2, responses[2], True, True, True, dash.no_update, f'Time taken by Model 2: {end_times[1] - start_times[1]:.2f} seconds', f'Time taken by Model 3: {end_times[2] - start_times[2]:.2f} seconds'
            return dash.no_update, new_text_2, dash.no_update, True, False, True, dash.no_update, dash.no_update, dash.no_update

        # Process the typing effect for the third model
        if button_id == 'interval-typing-3' and current_indices[2] < len(get_words(responses[2])):
            words = get_words(responses[2])
            new_text_3 = ' '.join(words[:current_indices[2] + 1])
            current_indices[2] += 1
            if current_indices[2] >= len(words):
                return dash.no_update, dash.no_update, new_text_3, True, True, True, dash.no_update, dash.no_update, f'Time taken by Model 3: {end_times[2] - start_times[2]:.2f} seconds'
            return dash.no_update, dash.no_update, new_text_3, True, True, False, dash.no_update, dash.no_update, dash.no_update

        return dash.no_update, dash.no_update, dash.no_update, True, True, True, dash.no_update, dash.no_update, dash.no_update
