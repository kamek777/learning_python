def country_town(country,town):
    """Prosta funkcja zawierająca informacje o kraju i mieście znajdującym się w nim."""
    return f"{country.title()}, {town.title()}."

print(country_town('polska','warszawa'))