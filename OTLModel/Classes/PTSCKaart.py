from OTLModel.Classes.PTModuleZFirmware import PTModuleZFirmware


# Generated with OTLClassCreator
class PTSCKaart(PTModuleZFirmware):
    """Seri�le controle uitbreidingskaart (optioneel): 4 lussen per kaart, max. 2 bijkomende uitbreidingskaarten per luscontactinterface."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTSCKaart"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
