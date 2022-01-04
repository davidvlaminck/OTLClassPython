from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlContactorType import KlContactorType


# Generated with OTLClassCreator
class Contactor(AIMObject):
    """Toestel dat ter plaatse of op afstand aangestuurd wordt om (grote) vermogensstromen af te schakelen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.type = KeuzelijstField(naam="type",
                                    label="type contactor",
                                    lijst=KlContactorType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor.type",
                                    definition="Geeft aan of het een K of Q contactor betreft.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Geeft aan of het een K of Q contactor betreft."""