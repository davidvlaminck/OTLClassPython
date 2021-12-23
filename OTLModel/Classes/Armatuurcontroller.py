from OTLModel.Classes.Communicatieapparatuur import Communicatieapparatuur
from OTLModel.Classes.FirmwareObject import FirmwareObject
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator
class Armatuurcontroller(Communicatieapparatuur, FirmwareObject):
    """Controller die op het verlichtingstoestel wordt gemonteerd en die ��n verlichtingstoestel aanstuurt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Communicatieapparatuur.__init__(self)
        FirmwareObject.__init__(self)
        self.merk = StringField(naam="merk",
                                label="merk",
                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.merk",
                                definition="Merk van de armatuurcontroller.",
                                constraints="",
                                usagenote="",
                                deprecated_version="")
        """Merk van de armatuurcontroller."""

        self.modelnaam = StringField(naam="modelnaam",
                                     label="modelnaam",
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.modelnaam",
                                     definition="Modelnaam van de armatuurcontroller.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """Modelnaam van de armatuurcontroller."""

        self.serienummer = StringField(naam="serienummer",
                                       label="serienummer",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.serienummer",
                                       definition="Het unieke nummer waarmee het toestel door de fabrikant ge�dentificeerd is.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Het unieke nummer waarmee het toestel door de fabrikant ge�dentificeerd is."""
