from abc import abstractmethod
from OTLModel.Datatypes.StringField import StringField
from OTLModel.Verification.AIMObject import AIMObject


class AIMNaamObject(AIMObject):
    """Abstracte als de basisklasse voor elk OTL object dat benoemd wordt met een mensleesbare identificator."""
    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMNaamObject"

    naam = StringField(naam="naam", label="naam", uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMNaamObject.naam", definition="De mensleesbare naam van een asset zoals dit bv. ook terug te vinden is op een etiket op het object zelf. De assetbeheerder kent deze naam toe of geeft de opdracht om deze toe te kennen. Indien een object een algemeen gangbare naam heeft zoals bv. bij een waterloop dan wordt deze gebruikt.", constraints="", usagenote="", deprecated_version="")
    """De mensleesbare naam van een asset zoals dit bv. ook terug te vinden is op een etiket op het object zelf. De 
    assetbeheerder kent deze naam toe of geeft de opdracht om deze toe te kennen. Indien een object een algemeen 
    gangbare naam heeft zoals bv. bij een waterloop dan wordt deze gebruikt. """

    @abstractmethod
    def __init__(self):
        super().__init__()