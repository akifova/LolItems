from src import Service

characters = Service.get_input()
found_champions = Service.search(characters)

if found_champions:
    champion = Service.make_selection(found_champions)
    Service.display_output(champion)
