from abc import abstractmethod

from ModelGenerator.BaseClasses.OTLAsset import OTLAsset
from ModelGenerator.BaseClasses.StringField import StringField
from ModelGenerator.BaseClasses.URIField import AnyURIField
from OTLClasses.Verification.AIMDBStatus import AIMDBStatus
from OTLClasses.Verification.AIMToestand import AIMToestand
from ModelGenerator.BaseClasses.RelatieInteractor import RelatieInteractor


class AIMObject(AIMDBStatus, AIMToestand, OTLAsset, RelatieInteractor):
    """Abstracte als de basisklasse voor alle uniek geïdentificeerde OTL objecten met de basiseigenschappen die elk OTL object minstens heeft."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMDBStatus.__init__(self)
        AIMToestand.__init__(self)
        OTLAsset.__init__(self)
        RelatieInteractor.__init__(self)
        self.notitie = StringField(naam="notitie", label="notitie", uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.notitie", definition="Extra notitie voor het object.", constraints="",
                          usagenote="", deprecated_version="")
        """Extra notitie voor het object."""

    # TODO: incomplete: missing attributes
