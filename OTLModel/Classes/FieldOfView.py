from OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator
class FieldOfView(AIMNaamObject):
    """2D-polygoon die het gezichtsveld van een gekoppeld camera onderdeel voorstelt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FieldOfView"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()