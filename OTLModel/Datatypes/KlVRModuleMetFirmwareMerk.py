from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlVRModuleMetFirmwareMerk(Keuzelijst):
    """Lijst met merken van VR-modules met firmware."""

    def __init__(self):
        super().__init__(naam="KlVRModuleMetFirmwareMerk",
                         label="VR-module met firmware merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVRModuleMetFirmwareMerk",
                         definition="Lijst met merken van VR-modules met firmware.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVRModuleMetFirmwareMerk")
