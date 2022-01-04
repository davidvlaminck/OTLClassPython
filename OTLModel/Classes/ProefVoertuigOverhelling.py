from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACVoertuigOverhelling import KlLEACVoertuigOverhelling


# Generated with OTLClassCreator
class ProefVoertuigOverhelling(Proef):
    """Proef om de overhelling over de bebakening van het voertuig te bepalen bij impact."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVoertuigOverhelling"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()