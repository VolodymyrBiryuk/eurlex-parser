import re
from typing import List

from bs4 import BeautifulSoup
from markdownify import markdownify as md


def detect_language(soup: BeautifulSoup) -> str:
    try:
        language_tag = soup.find('p', class_='oj-hd-lg')
        language = language_tag.text
    except AttributeError:
        try:
            language_tag = soup.find('p', class_='hd-lg')
            language = language_tag.text
        except AttributeError:
            raise ValueError('Unknown or unsupported language')
    return language


def roman_to_int(s: str) -> int:
    """
    Convert a Roman numeral string to an integer.
    Args:
        s (str): The Roman numeral string.

    Returns: The int representing the Roman numeral.
    """
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]
    return total



def html_table_to_markdown(markup: str) -> str:
    """
    Convert a HTML table to a Markdown table.
    Args:
        markup (str): The HTML table to convert.:

    Returns: A markdown representation of the table.

    """
    markdown = md(markup)
    lines = markdown.split('\n')
    # Filter out lines that don't contain any actual content.
    valid_lines = [line for line in lines if re.search(r'[A-Za-z0-9]', line)]
    markdown_cleaned = '\n'.join(valid_lines).strip()
    return markdown_cleaned


def extract_directive_and_regulation_at_beginning(text: str) -> str:
    # General pattern to match directives and regulations    
    pattern = (
        r'(^\s*\(?\d{0,3}\)?\s*Directive \d+/\d+/\s?\w{2,3})|'
        r'(^\s*\(?\d{0,3}\)?\s*Directive \(\w{2,3}\) \d+/\d+)|'
        r'(^\s*\(?\d{0,3}\)?\s*Regulation \(\w{2,3}\) No \d+/\d+)|'
        r'(^\s*\(?\d{0,3}\)?\s*Council Regulation \(\w{2,3}\) No \d+/\d+)|'
        r'(^\s*\(?\d{0,3}\)?\s*Regulation \(\w{2,3}\) \d+/\d+)|'
        r'(^\s*\(?\d{0,3}\)?\s*Decision \d+/\d+/\w{2,3})|'
        r'(^\s*\(?\d{0,3}\)?\s*Commission Recommendation \d+/\d+/\w{2,3})|'
        r'(^\s*\(?\d{0,3}\)?\s*Regulation \d+/\d+)'
    )

    match = re.match(pattern, text, re.IGNORECASE)

    if match:
        directive = match.group(0).strip()
        directive = re.sub(r'^\s*\(?\d{0,3}\)?\s*', '', directive)
        return directive
    return None


def extract_directives_and_regulations(text: str) -> List[str]:
    # General pattern to match directives and regulations
    pattern = (
        r'(Directive \d+/\d+/\s?\w{2,3})|'
        r'(Directive \(\w{2,3}\) \d+/\d+)|'
        r'(Regulation \(\w{2,3}\) No \d+/\d+)|'
        r'(Regulation \(\w{2,3}\) \d+/\d+)|'
        r'(Decision \d+/\d+/\w{2,3})|'
        r'(Commission Recommendation \d+/\d+/\w{2,3})|'
        r'(Regulation \d+/\d+)'
    )

    matches = re.findall(pattern, text, re.IGNORECASE)
    results = [match for group in matches for match in group if match]
    unique_results = list(dict.fromkeys(results))

    # For case like "Directives 2014/24/EU, 2014/25/EU or 2014/23/EU"
    directive_pattern = r'Directives?\s+((?:\d{4}/\d+/\w{2,3}\s*(?:, )?)+)\s*or\s+(\d{4}/\d+/\w{2,3})'
    directive_matches = re.findall(directive_pattern, text, re.IGNORECASE)

    if directive_matches:
        combined_directives = ', '.join(directive_matches[0])
        items = combined_directives.split(', ')
        directives_list = ['Directive ' + item.strip() for item in items if item]
        unique_results.extend(directives_list)
        unique_results = list(dict.fromkeys(unique_results))

    # For case like "Directives 2014/24/EU or 2014/25/EU"
    directive_pattern = r'Directives? (\d{4}/\d+/\w{2,3})(?:, (\d{4}/\d+/\w{2,3}))* (?:and|or) (\d{4}/\d+/\w{2,3})'

    directive_matches = re.findall(directive_pattern, text, re.IGNORECASE)
    directives_list = []
    if directive_matches:
        all_matches = [match for sublist in directive_matches for match in sublist if match]
        directives_list = ['Directive ' + item.strip() for item in all_matches]
        unique_results.extend(directives_list)
        unique_results = list(dict.fromkeys(unique_results))

    # For case like "Regulations (EU) No 2016/679 or (EU) No 2016/680"
    # regulation_pattern = r'Regulations? \(EU\) No (\d{4}/\d+)(?:, \(EU\) No (\d{4}/\d+))* or \(EU\) No (\d{4}/\d+)'
    regulation_pattern = r'Regulations? \(EU\) No (\d{3,4}/\d+)(?:, \(EU\) No (\d{3,4}/\d+))* (?:and|or) \(EU\) No (\d{3,4}/\d+)'
    regulation_matches = re.findall(regulation_pattern, text, re.IGNORECASE)

    if regulation_matches:
        all_matches = [match for sublist in regulation_matches for match in sublist if match]
        regulations_list = ['Regulation (EU) No ' + item.strip() for item in all_matches]
        unique_results.extend(regulations_list)
        unique_results = list(dict.fromkeys(unique_results))

    return unique_results
