from OTLModel.Classes.AfschermendeConstructie import AfschermendeConstructie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACTypeEindstuk import KlLEACTypeEindstuk


# Generated with OTLClassCreator
class Eindstuk(AfschermendeConstructie):
    """Een niet-gecertificeerd einde aan een geleideconstructie, aan de stroomafwaartse zijde ten opzichte van de meest nabij gelegen rijstrook."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Eindstuk"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlLEACTypeEindstuk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Eindstuk.type",
                                    definition="De vorm van het eindstuk.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De vorm van het eindstuk."""
