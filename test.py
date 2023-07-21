import pint

def convert_units_to_symbols(unit_string):
    # Mapping of unit names to symbols
    unit_map = {
        '[length]': 'l',
        '[mass]': 'm',
        '[luminosity]': 'l',
        '[current]': 'i',
        '[time]': 't',
        '[substance]': 't',

    }

    # Mapping of numbers to their superscript versions
    superscript_map = {
        '0': '⁰',
        '1': '¹',
        '2': '²',
        '3': '³',
        '4': '⁴',
        '5': '⁵',
        '6': '⁶',
        '7': '⁷',
        '8': '⁸',
        '9': '⁹',
        '.': '⋅',  # Dot for decimals
    }

    # Iterate over the mapping and replace units with symbols
    for unit, symbol in unit_map.items():
        unit_string = unit_string.replace(unit, symbol)

    # Replace ** with superscript notation
    parts = unit_string.split(" ")
    for i, part in enumerate(parts):
        if part == "**":
            num = parts[i + 1]
            superscript_num = ''.join([superscript_map[digit] for digit in num])
            parts[i] = superscript_num
            parts[i + 1] = ''  # Empty the next part which is the number
    unit_string = ''.join(parts).replace(' ', '')

    return unit_string


ureg = pint.UnitRegistry()

# Getting a list of all units
all_units = list(ureg._units.keys())

# Getting categories (dimensionality) for each unit
unit_categories = {}
for unit in all_units:
    try:
        category = str(ureg[unit].dimensionality)
        if category not in unit_categories:
            unit_categories[category] = [unit]
        else:
            unit_categories[category].append(unit)
    except:
        pass

for key in unit_categories:
    for units in unit_categories[key]:
        if ' ' in key:
            converted_string = convert_units_to_symbols(key)
            print ('''{unit: '%s', group:'%s'},'''%(units, converted_string))




# Test the function
s = "[length] ** 1.5 * [mass] ** 0.5 / [time]"
converted_string = convert_units_to_symbols(s)
converted_string

# # add new unit
# import pint
# ureg = pint.UnitRegistry()
#
# ureg.define('USD = currency')
#
# kg = ureg.kg
# USD = ureg.USD
#
# weight = 2.3 * kg
# price = 1.49 * USD / kg
# cost = weight * price
# print(f"{cost:~.2f}")  # prints '3.43 USD'