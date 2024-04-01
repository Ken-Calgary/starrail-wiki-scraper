import web_scraper
import csv

if __name__== '__main__':
    while(True):
        user_input = input("1. For Character Info\n2. For Relics\n3. For Planars\n4. Quit\nEnter Your Choice: ")

        match user_input:
            case "1":
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

                print("Successfully written Star Rail Character Data into csv file.\n")
                continue

            case "2":
                try:
                    page = web_scraper.get_page("https://honkai-star-rail.fandom.com/wiki/Relic/Sets")
                except:
                    print("Unable to acess the webpage")
                    exit()

                relics, total_relics = web_scraper.get_relics(page)
                
                with open("StarRailRelicsData.csv", 'w') as file:
                    csvwriter = csv.writer(file)
                    file.write("Name, Icon, Helmet Name, Helmet icon, Guantlet Name, Guantlet Icon, Chest Name, Chest Icon, Boots Name, Boots Icon, Bonus Desc\n")

                    for index in range(0, total_relics):
                        for key in relics:
                            file.write(f"{relics[key][index]},")
                        file.write(f"\n")

                print("Successfully written Star Rail Relics Data into csv file.\n")
                continue

            case "3":
                print("case3")

            case "4":
                print("Exiting...")
                quit()
            
        print("Invalid input, please try again.\n")


    
