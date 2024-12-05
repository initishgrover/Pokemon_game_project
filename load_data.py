# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Nitish Grover 101324174 Carson Winnik 101299194 Naveen Thottan 101307261 Danyel Soreefan"

# Update "" with your team (e.g. T102)
__team__ = "T-77"


#==========================================#
# Place your character_occupation_list function after this line

def character_occupation_list(file_name: str, occupation: str) -> list[dict]:
    """Return a list with  stats of all characters in file with user specified
    occupation

    Precondition: File to be read is in same directory as Python file

    Examples:
    >>> character_occupation_list('characters-mat.csv', 'AT')
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7,
    'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}]
    >>> character_occupation_list('characters-mat.csv', 'H')
    [{'Strength': 12, 'Agility': 9, 'Stamina': 4. 'Personality': 6,
    'Intelligence': 12, 'Luck': 0.61, 'Armor': 10, 'Weapon': 'Club']}
    """

    in_file = open(file_name)
    first_line = True
    character_list = []
    for line in in_file:
        line = line.strip().split(',')
        if first_line:
            first_line = False
            table_header = line
        elif line[0] == occupation:
            character = {}
            character[table_header[1]] = int(line[1])
            character[table_header[2]] = int(line[2])
            character[table_header[3]] = int(line[3])
            character[table_header[4]] = int(line[4])
            character[table_header[5]] = int(line[5])
            character[table_header[6]] = float(line[6])
            character[table_header[7]] = int(line[7])
            character[table_header[8]] = line[8]
            character_list += [character]
    in_file.close()
    return character_list
#==========================================#
# Place your character_strength_list function after this line


def character_strength_list(file_name: str, min_max: tuple[int, int]) -> list[dict]:
    """
    Return a list of dictionaried whcih contain pokemons with with strength in a
    given parameter from "characters-mat.csv"
    Preconditions: "characters-mat.csv" has following columns: ['Occupation',
    'Strength', 'Agility', 'Stamina','Personality', 'Intelligence','Luck',
    'Armor','Weapon']
    >>>character_strength_list("characters-mat.csv",(15,16)
    [{'Occupation': 'AT', 'Strength': 15, 'Agility': 11, 'Stamina': 10,
    'Personality': 13, 'Intelligence': 9, 'Luck': 0.94, 'Armor': 11,
    'Weapon': 'Club'}, {Next item}, ...]
    """
    in_file = open(file_name, 'r')
    pokemons_list = []
    first_line = True
    for line in in_file:
        line = line.strip().split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            pokemon = {}
            pokemon[table_header[0]] = line[0]
            # pokemon[table_header[1]] = int(line[1])
            pokemon[table_header[2]] = int(line[2])
            pokemon[table_header[3]] = int(line[3])
            pokemon[table_header[4]] = int(line[4])
            pokemon[table_header[5]] = int(line[5])
            pokemon[table_header[6]] = float(line[6])
            pokemon[table_header[7]] = int(line[7])
            pokemon[table_header[8]] = line[8]
            if int(line[1]) >= min_max[0] and int(line[1]) <= min_max[1]:
                pokemons_list += [pokemon]
    in_file.close()
    return pokemons_list

#==========================================#
# Place your character_luck_list function after this line


def character_luck_list(file_name: str, luck: float) -> list[dict]:
    """ return the list of dictionary that have less luck than provided value
    precondition: luck has to float
    >>>print(character_luck_list("characters-mat.csv", 0.20)) =[{'Occupation':
    'VF', 'Strength': 12, 'Agility': 4, 'Stamina': 2, 'Personality': 14,
    'Intelligence': 14, 'Armor': 9, 'Weapon': 'Dagger'}]
    >>>print(character_luck_list("characters-mat.csv", 0.23))= [{'Occupation':
    'VF', 'Strength': 12, 'Agility': 4, 'Stamina': 2, 'Personality': 14,
    'Intelligence': 14, 'Armor': 9, 'Weapon': 'Dagger'}]
    """
    file = open(file_name, 'r')
    pokemons_list = []
    first_line = True
    count = 0
    for line in file:
        line = line.strip()
        line = line.split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            pokemon = {}
            pokemon[table_header[0]] = line[0]
            pokemon[table_header[1]] = int(line[1])
            pokemon[table_header[2]] = int(line[2])
            pokemon[table_header[3]] = int(line[3])
            pokemon[table_header[4]] = int(line[4])
            pokemon[table_header[5]] = int(line[5])
            # pokemon[table_header[6]] = float(line[6])
            pokemon[table_header[7]] = int(line[7])
            pokemon[table_header[8]] = line[8]
            if float(line[6]) < luck:
                pokemons_list += [pokemon]

    file.close()
    return pokemons_list

#==========================================#
# Place your character_weapon_list function after this line


def character_weapon_list(file_name: str, weapon_name: str) -> list[dict]:
    """
    >>> character_weapon_list ('characters-mat.csv', 'Staff')
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8},
    {another element},]
    >>> character_weapon_list ('characters-mat.csv', 'aaa')
    []
    """

    lists = []
    with open(file_name, "r") as infile:
        lines = next(infile).strip()
        keys = lines.split(",")

        if 'Weapon' not in keys:
            return lists

        for line in infile:
            line = line.strip()
            val = line.split(",")
            character = {}

            for i in range(len(val)):
                if keys[i] == 'Luck':
                    character[keys[i]] = float(val[i])
                elif keys[i] in ["Strength", "Agility", "Stamina", "Personality", "Intelligence", "Armor"]:
                    character[keys[i]] = int(val[i])
                else:
                    character[keys[i]] = val[i]

            if character.get('Weapon', "") == weapon_name:
                if 'Weapon' in keys:
                    character['Weapon'] = val[keys.index('Weapon')]
                character.pop('Weapon', None)
                lists.append(character)

    return lists

#==========================================#
# Place your load_data function after this line


def load_data(file_name: str, t: tuple[str, str]) -> list[dict]:
    """ return the list of dictionary that has bunch of characters in it
    precondition: parameter has to be tuple with string values
    >>>print(load_data("characters-mat.csv", ('Luck', '0.20'))) =[{'Occupation':
    'VF', 'Strength': 12, 'Agility': 4, 'Stamina': 2, 'Personality': 14,
    'Intelligence': 14, 'Armor': 9, 'Weapon': 'Dagger'}]
    >>>print(load_data("characters-mat.csv", ('Nitish', '0.21'))) = Invalid 
    Value []
    """

   # t = (x, y)
    if t[0] == 'Luck':
        z = character_luck_list(file_name, t[1])
        return z
    elif t[0] == 'Strength':
        z = character_strength_list(file_name, t[1])
        return z
    elif t[0] == 'Weapon':
        z = character_weapon_list(file_name, t[1])
        return z
    elif t[0] == 'Occupation':
        z = character_occupation_list(file_name, t[1])
        return z
    # elif t[0] == 'All':

    elif t[0] != 'Luck' or 'Strength' or 'Weapon' or 'Occupation' or 'All':
        print("Invalid Value")
        return []


#==========================================#
# Place your calculate_health function after this line

def calculate_health(l: list[dict]) -> list[dict]:
    """
    Return list of of dictionaries with calculated health added onto the
    original dictionary
    Precondition: all elements are assumes to be eys of dictionary
    >>>calculate_health([{'Strength': 11, 'Agility': 4, 'Stamina': 9,
 'Personality': 4, 'Intelligence': 6, 'Luck': 3.5, 'Armor': 8, 'Weapon': 'Staff'}])
 [{'Strength': 11, 'Agility': 4, 'Stamina': 9, 'Personality': 4,
     'Intelligence': 6, 'Luck': 3.5, 'Armor': 8, 'Weapon': 'Staff', 'Health': 258.0}]
    >>>calculate_health([{'Strength': 7, 'Agility': 14, 'Stamina': 5,
 'Personality': 8, 'Intelligence': 9, 'Luck': 9.0, 'Armor': 5, 'Weapon': 'Staff'}])
 [{'Strength': 7, 'Agility': 14, 'Stamina': 5, 'Personality': 8,
     'Intelligence': 9, 'Luck': 9.0, 'Armor': 5, 'Weapon': 'Staff', 'Health': 268.0}]
    >>>Calculate_health([{'Strength': 10, 'Agility': 10, 'Stamina': 5,
 'Personality': 5, 'Intelligence': 4, 'Luck': 6.6, 'Armor': 5, 'Weapon': 'Staff'}])
 [{'Strength': 10, 'Agility': 10, 'Stamina': 5, 'Personality': 5,
     'Intelligence': 4, 'Luck': 6.6, 'Armor': 5, 'Weapon': 'Staff', 'Health': 199.0}]
    """

    if len(l) == 0:  # if list index is 0, return the original list
        health = 0
        return l
    else:
        health = (l[0]['Strength'] + l[0]['Agility'] + l[0]['Stamina'] + l[0]['Personality']
                  + l[0]['Intelligence'] + (l[0]['Armor']**2 * l[0]['Luck']))  # health calculation
        l[0]['Health'] = health  # add health into dictionary
        return l  # return new list
# Do NOT include a main script in your submission
