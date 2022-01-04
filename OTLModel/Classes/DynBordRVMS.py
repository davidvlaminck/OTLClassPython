from OTLModel.Classes.LEDBord import LEDBord
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDynBordRVMSMerk import KlDynBordRVMSMerk
from OTLModel.Datatypes.KlDynBordRVMSModelnaam import KlDynBordRVMSModelnaam


# Generated with OTLClassCreator
class DynBordRVMS(LEDBord):
    """Dynamisch verkeersbord dat dynamische verkeerstekens  en teksten kan afbeelden. RVMS staat voor Road-side Variable Message Signs."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRVMS"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlDynBordRVMSMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRVMS.merk",
                                    definition="Merk van het dynamische bord.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merk van het dynamische bord."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlDynBordRVMSModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRVMS.modelnaam",
                                         definition="Modelnaam van het RVMS-bord.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Modelnaam van het RVMS-bord."""