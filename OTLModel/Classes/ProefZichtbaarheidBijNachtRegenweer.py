from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLClassCreator
class ProefZichtbaarheidBijNachtRegenweer(Proef):
    """Bepaling van het retroreflecterend vermogen van een markering bij nacht bij nat weer (tijdens regenbui)."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNachtRegenweer"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.retrotreflectieco�ffici�nt = DecimalFloatField(naam="retrotreflectieco�ffici�nt",
                                                            label="retrotreflectieco�ffici�nt",
                                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNachtRegenweer.retrotreflectieco�ffici�nt",
                                                            definition="De maat voor het retroreflecterend vermogen van een markering bij nacht bij nat weer (tijdens regenbui).",
                                                            constraints="",
                                                            usagenote="uitgedrukt in mcd. m-2.lux-1",
                                                            deprecated_version="")
        """De maat voor het retroreflecterend vermogen van een markering bij nacht bij nat weer (tijdens regenbui)."""
