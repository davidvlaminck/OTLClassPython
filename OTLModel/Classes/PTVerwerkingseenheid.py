from OTLModel.Classes.PTModuleMetFirmware import PTModuleMetFirmware


# Generated with OTLClassCreator
class PTVerwerkingseenheid(PTModuleMetFirmware):
    """Ook LS-kaart of Local Stationkaart genoemd, de centrale verwerkingseenheid die in verbinding staat met ��n of meerdere demodulatoren."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTVerwerkingseenheid"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
