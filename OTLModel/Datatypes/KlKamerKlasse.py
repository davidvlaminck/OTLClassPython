from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlKamerKlasse(Keuzelijst):
    """De stabiliteitsklasse van de kamer."""

    def __init__(self):
        super().__init__(naam="KlKamerKlasse",
                         label="Kamer klasse",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKamerKlasse",
                         definition="De stabiliteitsklasse van de kamer.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKamerKlasse")

        self.add_option("klasse-1", "klasse 1", "klasse 1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKamerKlasse/klasse-1")
        self.add_option("klasse-2", "klasse 2", "klasse 2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKamerKlasse/klasse-2")