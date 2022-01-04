from abc import abstractmethod
from OTLModel.Classes.PTRegelaarModule import PTRegelaarModule
from OTLModel.Classes.FirmwareObject import FirmwareObject


# Generated with OTLClassCreator
class PTModuleMetFirmware(PTRegelaarModule, FirmwareObject):
    """Abstracte voor de modules met firmware van het personentransportbe�nvloedingssysteem van een verkeersregelaar."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PTModuleMetFirmware"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        PTRegelaarModule.__init__(self)
        FirmwareObject.__init__(self)