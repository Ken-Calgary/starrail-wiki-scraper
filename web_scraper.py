import requests
import re
from bs4 import BeautifulSoup

def get_page(url):
    """
    Returns the HTML content of the page
    
    url -- The url of the website
    """

    html_page = requests.get(url)
    return html_page.content

def get_character_info(page):
    """
    Returns the playable character information alongside the total number of playable characters

    page -- The html page of the website
    """
    soup = BeautifulSoup(page, "html.parser")
    playable_characters = dict(name=[], icon=[], rarity=[], rarity_icon=[], path=[], path_icon=[], element=[], element_icon=[])
    # Gets only the specified html attribute using regex
    pattern_src = r'src="(.*?)"'
    pattern_title = r'title="(.*?)"'

    # Gets total number of playable characters
    num_of_playable_characters = int(str(soup.find_all("b")[2]).replace("<b>", "").replace("</b>", ""))

    all_table_rows = soup.find_all("tr")

    # Goes through each <tr> element for the amount of playable characters available as of now
    for index in range(1, num_of_playable_characters + 1):
        title_elements = re.findall(pattern=pattern_title, string=str(all_table_rows[index]))
        src_elements = re.findall(pattern=pattern_src, string = str(all_table_rows[index]))

        # Gets all necessary information from each HTML element as long as it's not Trailblazer
        if title_elements[0] != 'Trailblazer':
            name, rarity, path, element = title_elements[0], title_elements[2], title_elements[3], title_elements[5]
            character_icon, rarity_icon, path_icon, element_icon = src_elements[0], src_elements[2], src_elements[4], src_elements[6]
        else: 
            name, rarity, path, element = title_elements[0], title_elements[2], "Adaptive", "Adaptive"
            character_icon, rarity, path, element = src_elements[0], src_elements[2], "N/A", "N/A"
        
        character_info = dict(name=name, icon=character_icon, rarity=rarity, rarity_icon=rarity_icon,
                               path=path, path_icon=path_icon, element=element, element_icon=element_icon)

        # Store character information
        for key in playable_characters:
            playable_characters[key].append(character_info[key])
        
    return playable_characters, num_of_playable_characters

def get_relics(page):
    """
    Returns the relics' information alongside the total number of relics

    page -- The html page of the website
    """
    soup = BeautifulSoup(page, "html.parser")
    relics = dict(set_icon=[], set_name=[], pieces_name=[], pieces_icon=[], bonuses=[])

    # Gets only the specified html attribute using regex
    pattern_src = r'src="(.*?)"'
    pattern_title = r'title="(.*?)"'

    # Gets total number of relics
    total_relics = int(str(soup.find_all("b")[2]).replace("<b>", "").replace("</b>", ""))
    
    all_table_rows = soup.find_all("tr")
    bonus_desc_html = soup.find_all(id="mw-customcollapsible-relicsettable")
    
    for index in range(1, total_relics + 1):
        # Pattern to seperate the different tags/attributes
        title_elements = re.findall(pattern=pattern_title, string=str(all_table_rows[index]))
        src_elements = re.findall(pattern=pattern_src, string = str(all_table_rows[index]))

        set_name = title_elements[0]
        pieces_name = []

        # Store all four different set piece names (helmet, gloves, body, shoes)
        for piece_index in range(2, len(title_elements), 2):
            if len(pieces_name) == 4:
                break
            else:
                pieces_name.append(title_elements[piece_index])

        set_icon = src_elements[0]
        pieces_icon = []

        # Store all four different set piece icons (helmet, gloves, body, shoes)
        for piece_index in range(2, len(src_elements), 4):
            pieces_icon.append(src_elements[piece_index])
        
        bonus_desc = _remove_html_attributes(bonus_desc_html[index])
        
        set_info = dict(set_icon=set_icon, set_name=set_name, pieces_name=pieces_name, pieces_icon=pieces_icon, bonuses=bonus_desc)

        for key in relics:
            relics[key].append(set_info[key])

    return relics, total_relics


def get_planars(page):
    """
    Returns the planars' information alongside the total number of planars

    page -- The html page of the website
    """
    soup = BeautifulSoup(page, "html.parser")
    planars = dict(icon=[], set=[], pieces=[], bonuses=[])

def _remove_html_attributes(html):
    """
    A helper function to remove html attributes from a string, and return that string.

    html -- HTML code
    """
    attribute_removal_pattern = r'<.*?>'
    string = re.sub(pattern=attribute_removal_pattern, repl='' ,string=str(html))
    
    return string
