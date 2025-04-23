# Function for API call
from . import pdfAWAM
import requests
import io

# Source is the PDF URL
def check_accessibility(source, password='', verbose=False, report=False):
    """
    Returns the accessibility check result in JSON format.
    Accepts a local file path or URL to a PDF.
    """
    if source.startswith('http://') or source.startswith('https://'):
        data = requests.get(source).content
        stream = io.BytesIO(data)
    else:
        stream = open(source, 'rb')

    result = pdfAWAM.extractAWAMIndicators(
        stream,
        password,
        verbose=verbose,
        report=report,
        json_value=True,
        console=False
    )

    return result
