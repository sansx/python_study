from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n


def get_country_code(cy_name):
    for code,name in COUNTRIES.items():
        if name == cy_name:
            return code 

    return None

# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))
