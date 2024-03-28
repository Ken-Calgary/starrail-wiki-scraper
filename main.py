import web_scraper
import csv

if __name__== '__main__':
    try:
        page = web_scraper.get_page("https://honkai-star-rail.fandom.com/wiki/Character/List")
    except:
        print("Unable to access the webpage")
        exit()

    playable_characters, number_of_characters = web_scraper.get_character_info(page)

    # Write data into csv
    with open("StarRailCharactersData.csv", 'w') as file:
        csvwriter = csv.writer(file)
        file.write("Name, Icon, Rarity, Rarity Icon, Path, Path Icon, Element, Element Icon\n")

        for index in range(0, number_of_characters):
            for key in playable_characters:
                file.write(f"{playable_characters[key][index]},")
            file.write(f"\n")


        

