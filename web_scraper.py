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