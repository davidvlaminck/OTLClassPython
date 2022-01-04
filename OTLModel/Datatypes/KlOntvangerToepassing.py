from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlOntvangerToepassing(Keuzelijst):
    """Keuzelijst met modelnamen voor OntvangerToepassing."""

    def __init__(self):
        super().__init__(naam="KlOntvangerToepassing",
                         label="Ontvanger toepassing",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOntvangerToepassing",
                         definition="Keuzelijst met modelnamen voor OntvangerToepassing.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOntvangerToepassing")

        self.add_option("WIFI", "WIFI", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOntvangerToepassing/WIFI")
        self.add_option("KAR", "KAR", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOntvangerToepassing/KAR")
        self.add_option("GPRS", "GPRS", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOntvangerToepassing/GPRS")
        self.add_option("GSM", "GSM", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOntvangerToepassing/GSM")