from OTLModel.Classes.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator
class IsSWGehostOp(DirectioneleRelatie):
    """Deze relatie legt de link tussen een software en hardware onderdeel."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsSWGehostOp"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()