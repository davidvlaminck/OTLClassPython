from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlStraatkolkType(Keuzelijst):
    """Types van straatkolk."""

    def __init__(self):
        super().__init__(naam="KlStraatkolkType",
                         label="Straatkolk type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStraatkolkType",
                         definition="Types van straatkolk.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStraatkolkType")

        self.add_option("horizontaal", "horizontaal", "Een gietijzeren rooster met horizontale afvoeropening dat op regelmatige afstand geplaatst wordt langs of in een weg, fietspad of voetpad.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkType/horizontaal")
        self.add_option("verticaal", "verticaal", "Verticale afvoeropening die op regelmatige afstand geplaatst wordt langs of in een boordsteen van de weg, fietspad of voetpad.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkType/verticaal")
        self.add_option("geisoleerd", "geisoleerd", "Een straatkolk die niet in een rij geplaatst werd maar bijvoorbeeld ergens solitair op een plein.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkType/geisoleerd")