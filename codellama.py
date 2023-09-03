"""
A library for interacting with the powerful AI model CodeLlama V2 locally.
"""

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="Phind/Phind-CodeLlama-34B-v2")


def translate_code(language_one, language_two, code):
    """
    Translates a given code from one programming language to another.

    Args:
        language_one (str): The source programming language.
        language_two (str): The target programming language.
        code (str): The code to be translated.

    Returns:
        str: The translated code.
    """
    preprompt = f"translate {code} from {language_one} to {language_two}"
    return pipe(preprompt)[0]["generated_text"]

def explain_code(code):
    """
    Explains a given code in natural language.
    
    Args:
        code (str): The code to be explained.

    Returns:
        str: The explanation.
    """
    preprompt = f"explain {code} in natural language"
    return pipe(preprompt)[0]["generated_text"]
