from OTLModel.Classes.PTModuleZFirmware import PTModuleZFirmware


# Generated with OTLClassCreator
class PTVoedingsmodule(PTModuleZFirmware):
    """Voedingsmodule van de PT regelaar 230VAC/ 24 VDC - 5A."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTVoedingsmodule"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()