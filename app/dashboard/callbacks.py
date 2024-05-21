from dash.dependencies import Input, Output, State
from ..model_manager import ModelManager
import dash
model_manager = ModelManager()

stream_generator_1 = None
stream_generator_2 = None
stream_generator_3 = None


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
        ctx = dash.callback_context

        if not ctx.triggered:
            return existing_text_1, existing_text_2, existing_text_3, True, True, True

        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'submit-button':
            if n_clicks > 0:
                stream_generator_1 = model_manager.get_response(input_value, model=model1)
                stream_generator_2 = model_manager.get_response(input_value, model=model2)
                stream_generator_3 = model_manager.get_response(input_value, model=model3)
                return '', '', '', False, False, False

        new_text_1, new_text_2, new_text_3 = existing_text_1, existing_text_2, existing_text_3
        disabled_1, disabled_2, disabled_3 = False, False, False

        if button_id == 'interval-component-1' and n1 is not None:
            try:
                new_text_1 += next(stream_generator_1)
            except StopIteration:
                disabled_1 = True

        if button_id == 'interval-component-2' and n2 is not None:
            try:
                new_text_2 += next(stream_generator_2)
            except StopIteration:
                disabled_2 = True

        if button_id == 'interval-component-3' and n3 is not None:
            try:
                new_text_3 += next(stream_generator_3)
            except StopIteration:
                disabled_3 = True

        return new_text_1, new_text_2, new_text_3, disabled_1, disabled_2, disabled_3
