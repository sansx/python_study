def initcity(city,country,population=""):
    city = city.title().strip()
    country = country.title().strip()
    if population:
        return city + ", " + country + " - population " +  str(population)  
    else:
        return city + ", " + country