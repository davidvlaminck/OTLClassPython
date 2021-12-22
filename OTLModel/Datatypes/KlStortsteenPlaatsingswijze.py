from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlStortsteenPlaatsingswijze(Keuzelijst):
    """De manier waarop de stenen worden geplaatst."""

    def __init__(self):
        super().__init__(naam="KlStortsteenPlaatsingswijze",
                         label="Plaatsingswijze",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStortsteenPlaatsingswijze",
                         definition="De manier waarop de stenen worden geplaatst.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStortsteenPlaatsingswijze")

        self.add_option("gewone-bestorting-zonder-fixatie-collo�daal-beton", "gewone bestorting zonder fixatie collo�daal beton", "gewone bestorting zonder fixatie collo�daal beton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/gewone-bestorting-zonder-fixatie-collo�daal-beton")
        self.add_option("stroomkuilenprofiel-zonder-fixatie-collo�daal-beton", "stroomkuilenprofiel zonder fixatie collo�daal beton", "stroomkuilenprofiel zonder fixatie collo�daal beton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/stroomkuilenprofiel-zonder-fixatie-collo�daal-beton")
        self.add_option("gewone-bestorting-met-fixatie-collo�daal-beton", "gewone bestorting met fixatie collo�daal beton", "gewone bestorting met fixatie collo�daal beton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/gewone-bestorting-met-fixatie-collo�daal-beton")
        self.add_option("stroomkuilenprofiel-met-fixatie-collo�daal-beton", "stroomkuilenprofiel met fixatie collo�daal beton", "stroomkuilenprofiel met fixatie collo�daal beton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/stroomkuilenprofiel-met-fixatie-collo�daal-beton")
        self.add_option("gestapeld", "gestapeld", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/gestapeld")
