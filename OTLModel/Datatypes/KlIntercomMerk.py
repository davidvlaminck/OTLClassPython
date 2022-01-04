from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlIntercomMerk(Keuzelijst):
    """Het merk van het intercomtoestel."""

    def __init__(self):
        super().__init__(naam="KlIntercomMerk",
                         label="Intercomtoestel merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIntercomMerk",
                         definition="Het merk van het intercomtoestel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIntercomMerk")
