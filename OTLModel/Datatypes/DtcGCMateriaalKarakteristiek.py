from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEGCGeluidskarakteristiek import KlLEGCGeluidskarakteristiek
from OTLModel.Datatypes.KlLEGCMateriaal import KlLEGCMateriaal


# Generated with OTLComplexDatatypeCreator
class DtcGCMateriaalKarakteristiek(ComplexField):
    """Complex datatype voor het materiaal en zijn geluidskarakteristiek van de geluidswerende constructie."""

    def __init__(self):
        super().__init__(naam="DtcGCMateriaalKarakteristiek",
                         label="Materiaal karakteristiek",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGCMateriaalKarakteristiek",
                         definition="Complex datatype voor het materiaal en zijn geluidskarakteristiek van de geluidswerende constructie.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.geluidskarakteristiek = KeuzelijstField(naam="geluidskarakteristiek",
                                                            label="geluidskarakteristiek",
                                                            lijst=KlLEGCGeluidskarakteristiek(),
                                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGCMateriaalKarakteristiek.geluidskarakteristiek",
                                                            definition="Het kenmerkend gedrag inzake geluid van de geluidswerende constructie.",
                                                            constraints="",
                                                            usagenote="",
                                                            deprecated_version="")
        self.geluidskarakteristiek = self.waarde.geluidskarakteristiek
        """Het kenmerkend gedrag inzake geluid van de geluidswerende constructie."""

        self.waarde.materiaal = KeuzelijstField(naam="materiaal",
                                                label="materiaal",
                                                lijst=KlLEGCMateriaal(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGCMateriaalKarakteristiek.materiaal",
                                                definition="Het materiaal van de geluidswerende constructie.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        self.materiaal = self.waarde.materiaal
        """Het materiaal van de geluidswerende constructie."""