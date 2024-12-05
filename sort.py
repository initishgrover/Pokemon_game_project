# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Nitish Grover 101324174 Carson winnik 101299194 Naveen thottan 101307261 Danyel Soreefan 101302982"

# Update "" with your team (e.g. T102)
__team__ = "T-77"

#==========================================#
# Place your sort_characters_agility_bubble function after this line


def sort_characters_agility_bubble(characters, order):
    """
    Sorts a list of character dictionaries by the "Agility" attribute.
    >>> sort_characters_agility_bubble([{'Occupation': 'EB', 'Agility': 13}, {'Occupation':
    'H', 'Agility': 11}], "A")
    [{'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB', 'Agility': 13}]
    >>> sort_characters_agility_bubble([{'Occupation':'EB'}, {'Occupation': 'M'}], "A")
    "Agility" key is not present.
    [{'Occupation': 'EB'},{'Occupation': 'M'}]
    """
    for i in range(len(characters)):
        for j in range(len(characters) - 1 - i):
            if 'Agility' not in characters[j] or 'Agility' not in characters[j + 1] or characters[j]['Agility'] is None or characters[j + 1]['Agility'] is None:
                print('"Agility" key is not present.')
                return characters
            if (order == "A" and characters[j]['Agility'] > characters[j + 1]['Agility']) or (order == "D" and characters[j]['Agility'] < characters[j + 1]['Agility']):
                characters[j], characters[j
                                          + 1] = characters[j + 1], characters[j]
    return characters
#==========================================#
# Place your sort_characters_intelligence_selection function after this line


def sort_characters_intelligence_selection(char_list: list[dict], asc_dsc: str) -> list[dict]:
    """
    return a list of tuples in either ascending or descending order of intelligence
    using selection sort method
    If the intelligence key is not present in the list, the original list is returned
    with an error message
    Precondition : List of dictionaries have valid keys and values associated with them
    Examples:

    >>>sort_characters_intelligence_selection([{'Occupation': 'AT','Intelligence': 30}, {'Occupation': 'H','Intelligence': 12}], "A")
    [{'Occupation': 'H', 'Intelligence': 12}, {'Occupation': 'AT', 'Intelligence': 30}]

    >>>sort_characters_intelligence_selection([{'Occupation': 'H', 'Strength': 19, 'Agility': 9}], 'D')
    "Intelligence" key is not present
    [{'Occupation': 'H', 'Strength': 19, 'Agility': 9}]

    >>>sort_characters_intelligence_selection([{'Occupation': 'AT','Intelligence': 9}, {'Occupation': 'H','Intelligence': 10},{'Intelligence':5}], "D")
    [{'Occupation': 'H', 'Intelligence': 10}, {'Occupation': 'AT', 'Intelligence': 9}, {'Intelligence': 5}]
    """

    char_num = len(char_list)

    if char_num == 0 or char_list[0].get("Intelligence") == None:
        print('"Intelligence" key is not present')
        return char_list
    if asc_dsc == "A":
        for i in range(char_num):
            min_index = i

            for j in range((i + 1), char_num):
                if char_list[j]["Intelligence"] < char_list[min_index]["Intelligence"]:
                    min_index = j

            char_list[i], char_list[min_index] = char_list[min_index], char_list[i]

        return char_list

    if asc_dsc == "D":
        for i in range(char_num):
            min_index = i

            for j in range((i + 1), char_num):
                if char_list[j]["Intelligence"] > char_list[min_index]["Intelligence"]:
                    min_index = j

            char_list[i], char_list[min_index] = char_list[min_index], char_list[i]

        return char_list

#==========================================#
# Place your sort_characters_health_insertion function after this line


def sort_characters_health_insertion(list_of_dict: [dict], sorting_order: str) -> None:
    """
    """
    if list_of_dict == [] or list_of_dict[0].get("Health") == None:
        print("Health key is not present")
        return list_of_dict

    # list_of_dict[0].get("Health")
    if sorting_order == "A":
        for i in range(1, len(list_of_dict)):
            j = i
            while list_of_dict[j - 1].get("Health") > list_of_dict[j].get("Health") and j > 0:
                list_of_dict[j
                             - 1], list_of_dict[j] = list_of_dict[j], list_of_dict[j - 1]
                j -= 1

        return list_of_dict
    elif sorting_order == "D":
        for i in range(1, len(list_of_dict)):
            j = i
            while list_of_dict[j - 1].get("Health") < list_of_dict[j].get("Health") and j > 0:
                list_of_dict[j
                             - 1], list_of_dict[j] = list_of_dict[j], list_of_dict[j - 1]
                j -= 1

        return list_of_dict


# Do NOT include a main script in your submission

#==========================================#
# Place your sort_characters_armor_bubble function after this line
def sort_characters_armor_bubble(arr: list[dict], order: str) -> list[dict]:
    """
    Return bubble sorted list of dictionaries by Armor value.

    Preconditions: Data must contain proper keys and integers for Armor values

    >>>sort_characters_armor_bubble([{'Occupation': 'AT', 'Strength': 13,
    'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8,
    'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}], 'A')

    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon':
    'Staff'}]

    >>>sort_characters_armor_bubble([{'Occupation': 'AT', 'Strength': 13,
    'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8,
    'Luck': 0.67, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 12,
    'Agility': 3, 'Stamina': 7, 'Personality': 13, 'Intelligence': 11,
    'Luck': 0.33, 'Weapon': 'Staff'}],'D')

    "Armor is not present."
    [{'Occupation': 'AT', 'Strength': 13,
    'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8,
    'Luck': 0.67, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 12,
    'Agility': 3, 'Stamina': 7, 'Personality': 13, 'Intelligence': 11,
    'Luck': 0.33, 'Weapon': 'Staff'}]

    >>>sort_characters_armor_bubble([{'Occupation': 'EB',
    'Armor': 11}, {'Occupation': 'H', 'Armor': 10}], 'D')

    [{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}]

    """
    if all("Armor" in armor for armor in arr):
        swap = True
        while swap:
            swap = False
            for i in range(len(arr) - 1):
                if order == "A":
                    if arr[i]["Armor"] > arr[i + 1]["Armor"]:
                        aux = arr[i]
                        arr[i] = arr[i + 1]
                        arr[i + 1] = aux
                        swap = True

                elif order == "D":
                    if arr[i]["Armor"] < arr[i + 1]["Armor"]:
                        aux = arr[i]
                        arr[i] = arr[i + 1]
                        arr[i + 1] = aux
                        swap = True

                else:
                    print('Incorrect order option')
                    return arr

        return arr
    else:
        print('"Armor" is not present.')
        return arr

# Do NOT include a main script in your submission

#==========================================#
# Place your sort function after this line


def sort(list_of_dictionary: [dict], sorting_order: str, sorting_var: str) -> None:
    """
    """
    if sorting_var == 'Health':
        resulting_list = sort_characters_health_insertion(
            list_of_dictionary, sorting_order)
        return resulting_list
    elif sorting_var == 'Intelligence':
        resulting_list = sort_characters_intelligence_selection(
            list_of_dictionary, sorting_order)
        return resulting_list
    elif sorting_var == 'Agility':
        resulting_list = sort_characters_agility_bubble(
            list_of_dictionary, sorting_order)
        return resulting_list
    elif sorting_var == 'Armor':
        resulting_list = sort_characters_armor_bubble(
            list_of_dictionary, sorting_order)
        return resulting_list
    else:
        print('cannot be sorted by', sorting_var)
        return list_of_dictionary


# Do NOT include a main script in your submission


