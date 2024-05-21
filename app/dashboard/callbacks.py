from dash.dependencies import Input, Output, State
import dash
from ..model_manager import ModelManager

model_manager = ModelManager()

stream_generator_1 = None
stream_generator_2 = None
stream_generator_3 = None

buffer_1 = []
buffer_2 = []
buffer_3 = []

generator_lock_1 = False
generator_lock_2 = False
generator_lock_3 = False


def register_callbacks(dash_app):
    @dash_app.callback(
        [Output('output-container-1', 'children'),
         Output('output-container-2', 'children'),
         Output('output-container-3', 'children'),
         Output('interval-component-1', 'disabled'),
         Output('interval-component-2', 'disabled'),
         Output('interval-component-3', 'disabled')],
        [Input('submit-button', 'n_clicks'),
         Input('interval-component-1', 'n_intervals'),
         Input('interval-component-2', 'n_intervals'),
         Input('interval-component-3', 'n_intervals')],
        [State('input-text', 'value'),
         State('model-dropdown-1', 'value'),
         State('model-dropdown-2', 'value'),
         State('model-dropdown-3', 'value'),
         State('output-container-1', 'children'),
         State('output-container-2', 'children'),
         State('output-container-3', 'children')]
    )
    def update_output(n_clicks, n1, n2, n3, input_value, model1, model2, model3, existing_text_1, existing_text_2,
                      existing_text_3):
        global stream_generator_1, stream_generator_2, stream_generator_3
        global buffer_1, buffer_2, buffer_3
        global generator_lock_1, generator_lock_2, generator_lock_3
        ctx = dash.callback_context

        if not ctx.triggered:
            return existing_text_1, existing_text_2, existing_text_3, True, True, True

        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'submit-button':
            if n_clicks > 0:
                stream_generator_1 = model_manager.get_response(input_value, model=model1)
                stream_generator_2 = model_manager.get_response(input_value, model=model2)
                stream_generator_3 = model_manager.get_response(input_value, model=model3)
                buffer_1, buffer_2, buffer_3 = [], [], []  # Clear buffers on new submission
                return '', '', '', False, False, False

        new_text_1 = existing_text_1 if existing_text_1 else ''
        new_text_2 = existing_text_2 if existing_text_2 else ''
        new_text_3 = existing_text_3 if existing_text_3 else ''
        disabled_1, disabled_2, disabled_3 = False, False, False

        if button_id == 'interval-component-1' and n1 is not None and not generator_lock_1:
            generator_lock_1 = True
            try:
                while len(buffer_1) < 5:  # Adjust buffer size if needed
                    next_chunk = next(stream_generator_1)
                    buffer_1.append(next_chunk)
                    print(f"Buffered chunk for container 1: {next_chunk}")
            except StopIteration:
                disabled_1 = True
            finally:
                if buffer_1:
                    new_text_1 += buffer_1.pop(0)
                generator_lock_1 = False

        if button_id == 'interval-component-2' and n2 is not None and not generator_lock_2:
            generator_lock_2 = True
            try:
                while len(buffer_2) < 5:  # Adjust buffer size if needed
                    next_chunk = next(stream_generator_2)
                    buffer_2.append(next_chunk)
                    print(f"Buffered chunk for container 2: {next_chunk}")
            except StopIteration:
                disabled_2 = True
            finally:
                if buffer_2:
                    new_text_2 += buffer_2.pop(0)
                generator_lock_2 = False

        if button_id == 'interval-component-3' and n3 is not None and not generator_lock_3:
            generator_lock_3 = True
            try:
                while len(buffer_3) < 5:  # Adjust buffer size if needed
                    next_chunk = next(stream_generator_3)
                    buffer_3.append(next_chunk)
                    print(f"Buffered chunk for container 3: {next_chunk}")
            except StopIteration:
                disabled_3 = True
            finally:
                if buffer_3:
                    new_text_3 += buffer_3.pop(0)
                generator_lock_3 = False

        print(
            f"Final return values: {new_text_1}, {new_text_2}, {new_text_3}, {disabled_1}, {disabled_2}, {disabled_3}")  # Final debug print statement
        return new_text_1, new_text_2, new_text_3, disabled_1, disabled_2, disabled_3
