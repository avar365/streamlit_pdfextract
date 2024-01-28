# pdf_app/microservices/PdfProcessor.py
import pdfplumber
import re
from typing import Union

def clean_text(text: str) -> Union[str, str]:
    """
    Cleans the extracted text by removing control characters and line breaks.

    Parameters:
    - text (str): The text to be cleaned.

    Returns:
    - Union[str, str]: A tuple containing the cleaned text as a string
                      and a message indicating success or failure.
    """
    try:
        cleaned_text = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f-\x9f]', '', text)
        cleaned_text = cleaned_text.replace('\n', ' ').replace('\r', '')
        return cleaned_text.strip(), "Success: Text cleaned successfully."
    except Exception as e:
        return "", f"Error: An unexpected error occurred during text cleaning - {str(e)}."

def read_pdf(file_path: str) -> Union[str, str]:
    """
    Reads the content of a PDF file and returns the extracted text.

    Parameters:
    - file_path (str): The path to the PDF file.

    Returns:
    - Union[str, str]: A tuple containing the extracted text as a string
                      and a message indicating success or failure.
    """
    try:
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()

        cleaned_text, cleaning_message = clean_text(text)
        return cleaned_text, cleaning_message
    except FileNotFoundError:
        return "", "Error: File not found. Please provide a valid file path."
    except pdfplumber.PDFSyntaxError:
        return "", "Error: Invalid PDF file. Unable to extract text."
    except Exception as e:
        return "", f"Error: An unexpected error occurred - {str(e)}."
