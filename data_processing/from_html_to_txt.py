#Fonction faites grâce à Chat GPT disponible sur VSCode
#Prompt :
# "Extracts the text content from an HTML file based on the specified tag names in form of list and writes it to a .txt file."
from bs4 import BeautifulSoup
import re

def extract_content_from_html(html_file, tag_names, output_txt_file):
    """
    Extracts the text content from an HTML file based on the specified tag names and writes it to a .txt file.
    
    Args:
        html_file (str): The path to the HTML file.
        tag_names (list): A list of tag names to extract text content from (e.g., ['p', 'h1']).
        output_txt_file (str): The path to the output .txt file.
    """
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract the text content of the specified tags
    content = []
    for tag_name in tag_names:
        tags = soup.find_all(tag_name)
        content.extend(tag.get_text() for tag in tags)
    
    # Write the content to a .txt file
    with open(output_txt_file, 'w', encoding='utf-8') as file:
        text='\n'.join(content)
        file.write(clean_text(text))

def clean_text(text):
    """
    Cleans the input text by removing extra spaces and special characters.
    
    Args:
        text (str): The input text to be cleaned.
    
    Returns:
        str: The cleaned text.
    """
    # Remove special characters (keeping only alphanumeric and spaces)
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Strip leading and trailing spaces
    text = text.strip()
    return text