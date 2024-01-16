from shiny import Inputs, Outputs, Session, reactive, render, ui

from curb65.calculator import validate_inputs, calculate_curb_score
from curb65.database import Database


def curb65_server(input: Inputs, output: Outputs, session: Session):
    database = Database()

    curb_score = reactive.Value()
    error_message = reactive.Value('')

    @reactive.Effect
    @reactive.event(input.calc_btn)
    def _calculate_score():
        curb_score.set(None)

        error_message.set(
            validate_inputs(
                input.pid(),
                input.dob(),
                input.doc(),
                input.confusion(),
                input.urea(),
                input.resp(),
                input.bps(),
                input.bpd()
            )
        )

        if error_message() != '':
            return

        score =            calculate_curb_score(
                input.dob(),
                input.doc(),
                input.confusion(),
                input.urea(),
                input.resp(),
                input.bps(),
                input.bpd()
            )

        curb_score.set(score        )
        database.add_score(
                input.pid(),
                str(input.dob()),
                str(input.doc()),
                1 if input.confusion() else 0,
                input.urea(),
                input.resp(),
                input.bps(),
                input.bpd(),
            score
        )

    @render.text
    def error_msg():
        return error_message()

    @render.ui
    def score():
        if curb_score() is None:
            return None

        bg_colour = 'Yellow'
        text_colour = 'black'
        severity = 'Medium'
        if curb_score() < 2:
            bg_colour = 'green'
            text_colour = 'white'
            severity = 'Low'
        elif curb_score() > 2:
            bg_colour = 'red'
            text_colour = 'white'
            severity = 'High'

        return ui.div(
            ui.h3(f'{curb_score()} - {severity} Severity'),
                style=f'background-color: {bg_colour}; color: {text_colour}'
        )
