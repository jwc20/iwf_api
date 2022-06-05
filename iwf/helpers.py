# <---------------------------------Validations------------------------------->


def isResult(url):
    """
    Validates event url
    Example: https://iwf.sport/results/results-by-events/?event_id=529
    """
    return True if RESULT_URL in url else False


def isAthleteBio(url):
    """
    Validate athlete url
    Example: https://iwf.sport/weightlifting_/athletes-bios/?athlete=ilyin-ilya-1988-05-24&id=7895
    """
    return True if ATHLETE_BIO_URL in url else False
