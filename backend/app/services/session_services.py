analysis_context = {}


def reset_context():

    global analysis_context

    analysis_context = {}

def update_context(key, value):

    analysis_context[key] = value

def get_context():

    return analysis_context