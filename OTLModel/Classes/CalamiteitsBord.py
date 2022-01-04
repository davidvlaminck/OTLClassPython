from OTLModel.Classes.RetroreflecterendVerkeersbord import RetroreflecterendVerkeersbord
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlCalamiteitsbordType import KlCalamiteitsbordType
from OTLModel.Datatypes.KlCalamiteitsbordVorm import KlCalamiteitsbordVorm


# Generated with OTLClassCreator
class CalamiteitsBord(RetroreflecterendVerkeersbord):
    """De aanwijzingsborden ter plaatse van een startpunt, een aantakpunt, een wissel- of koppelpunt van een
omleggingsroute bij calamiteiten zijn ge�ntegreerd in een ��n-bordsysteem met een scharnierende
plaat."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CalamiteitsBord"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.calamiteitsbordType = KeuzelijstField(naam="calamiteitsbordType",
                                                   label="calamiteitsbord type",
                                                   lijst=KlCalamiteitsbordType(),
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CalamiteitsBord.calamiteitsbordType",
                                                   definition="Het type van calamiteitsbord (bv. draaiend of dragend).",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        """Het type van calamiteitsbord (bv. draaiend of dragend)."""

        self.vorm = KeuzelijstField(naam="vorm",
                                    label="vorm",
                                    lijst=KlCalamiteitsbordVorm(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CalamiteitsBord.vorm",
                                    definition="De vorm van het calamiteitsbord.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De vorm van het calamiteitsbord."""