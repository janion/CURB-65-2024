from shiny import ui

def curb65_ui():
    return ui.page_fluid(
        ui.panel_title("CURB-65 Calculator"),
        ui.row(
            ui.p(
                "CURB-65 is a simple six point score based on confusion, urea, respiratory rate, blood pressure, and age",
                "which can be used to stratify patients with community acquired pneumonia (CAP) into different management groups."
            ),
            ui.p("The score is caluclated using the following metrics:"),
            ui.tags.ul(
                ui.tags.li("Confusion of new onset (defined as an AMTS of 8 or less)"),
                ui.tags.li("Blood Urea nitrogen greater than 7 mmol/L (19 mg/dL)"),
                ui.tags.li("Respiratory rate of 30 breaths per minute or greater"),
                ui.tags.li("Blood pressure less than 90 mmHg systolic or diastolic blood pressure 60 mmHg or less"),
                ui.tags.li("Age 65 or older")
            )
        ),
        ui.tags.hr(),
        ui.row(
            ui.column(
                4,
                ui.input_text(id='pid', label='Patient ID'),
                ui.input_date(id='dob', label='Patient Date of Birth'),
                ui.input_date(id='doc', label='Date of Consultation')
            ),
            ui.column(
                4,
                ui.input_checkbox(id='confusion', label='Confusion'),
                ui.input_numeric(id='urea', label='Urea (mg/dL)', value=19),
                ui.input_numeric(id='resp', label='Respiratory Rate (breath/min)', value=30)
            ),
            ui.column(
                4,
                ui.h3('Blood Pressure'),
                ui.input_numeric(id='bps', label='Systolic (mmHg)', value=90),
                ui.input_numeric(id='bpd', label='Diastolic (mmHg)', value=60)
            )
        ),
        ui.input_action_button(id='calc_btn', label='Calculate'),
        ui.div(
            ui.output_text(id='error_msg'),
            style="color: red;"
        ),
        ui.div(
            ui.h3('CURB-65 Score:'),
            style='display: inline-block;'
        ),
        ui.div(
            ui.output_ui(id='score'),
            style='display: inline-block;'
        )
    )