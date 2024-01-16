from re import search


def validate_inputs(pid, dob, doc, confusion, urea, resp_rate, bps, bpd):
    if pid is None or search('P[0-9]{6}', pid) is None:
        return 'Patient ID must be of the form: P******'
    elif dob is None:
        return 'Date of Birth must be specified'
    elif doc is None:
        return 'Date of Consultation must be specified'
    elif confusion is None:
        return 'Confusion must be True or False'
    elif urea is None or urea < 0:
        return 'Urea level must be a positive number or zero'
    elif resp_rate is None or resp_rate <= 0:
        return 'Respiration rate must be a positive number'
    elif bps is None or bps <= 0:
        return 'Systolic blood pressure must be a positive number'
    elif bpd is None or bpd <= 0:
        return 'Diastolic blood pressure must be a positive number'
    else:
        return ''

def calculate_curb_score(dob, doc, confusion, urea, resp_rate, bps, bpd):
    diff = doc - dob
    age = int(diff.days / 365)

    score = 0
    if confusion:
        score += 1
    if urea > 19:
        score += 1
    if resp_rate >= 30:
        score += 1
    if bps< 90 or bpd <= 60:
        score += 1
    if age >= 65:
        score += 1

    return  score