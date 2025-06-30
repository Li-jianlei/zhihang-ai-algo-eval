import spacy
import re

# Function to extract names from the string using spaCy
def extract_name(string):
    # Convert the string to Unicode
    r1 = unicode(string)  # Consider using str() instead of unicode() in Python 3.x
    nlp = spacy.load('xx_ent_wiki_sm')  # Load the spaCy model for named entity recognition
    doc = nlp(r1)
    for ent in doc.ents:
        if ent.label_ == 'PER':  # Check if the entity is a person's name
            print(ent.text)  # Print the person's name
            break

# Function to extract Phone Numbers from the string using regular expressions
def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    # Clean up the phone numbers and return them as a list
    return [re.sub(r'\D', '', number) for number in phone_numbers]

# Function to extract Email addresses from the string using regular expressions
def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    # Find and return email addresses in the string
    return r.findall(string)
