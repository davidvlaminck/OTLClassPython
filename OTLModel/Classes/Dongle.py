from OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator
class Dongle(AIMNaamObject):
    """Een hardwaresleutel."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dongle"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()