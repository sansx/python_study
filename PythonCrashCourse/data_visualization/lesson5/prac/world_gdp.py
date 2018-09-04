from country_codes import get_country_code
import json
import pygal

filename = "./gdp_json.json"

with open(filename) as f:
    res = json.load(f)
    
resbox = {}
for item in res:
    if item["Year"] == 2016:
        value = int(float(item["Value"])/100000000)
        code = get_country_code(item["Country Name"])
        if code and value>0:
            resbox[code] = value


wm = pygal.maps.world.World()
wm.title = 'World GDP in 2016, by Country'

wm.add("World gdp(Billion)",resbox)

wm.render_to_file("./world_gdp.svg")