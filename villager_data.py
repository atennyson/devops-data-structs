"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a list of species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[str]: a list of strings
    """

    species = []

    with open("villagers.csv") as file:
        reader = file.read().splitlines()
        for row in reader:
            row = row.split("|")
            species.append(row[1])

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    with open("villagers.csv") as file:
        reader = file.read().splitlines()
        for row in reader:
            row = row.split("|")
            if row[1] == search_string:
                villagers.append(row[0])
            else:
                villagers.append(row[0])

    villagers.sort()

    return villagers


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    with open("villagers.csv") as file:
        reader = file.read().splitlines()
        for row in reader:
            row = row.split("|")
            if row[3] == "Fitness":
                fitness.append(row[0])
            elif row[3] == "Nature":
                nature.append(row[0])
            elif row[3] == "Education":
                education.append(row[0])
            elif row[3] == "Music":
                music.append(row[0])
            elif row[3] == "Fashion":
                fashion.append(row[0])
            elif row[3] == "Play":
                play.append(row[0])

    return [sorted(fitness), sorted(nature), sorted(education), sorted(music), sorted(fashion), sorted(play)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    with open(filename) as file:
        reader = file.read().splitlines()
        for row in reader:
            row = row.split("|")
            all_data.append((row[0], row[1], row[2], row[3], row[4]))

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    with open(filename) as file:
        reader = file.read().splitlines()
        for row in reader:
            row = row.split("|")
            if row[0] == villager_name:
                return row[4]

    return None


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - list[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        ['Bella', ..., 'Carmen']
    """

    # TODO: replace this with your code
