# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from OTLMOW.OTLModel.Datatypes.DtcProductidentificatiecode import DtcProductidentificatiecode


# Generated with OTLClassCreator. To modify: extend, do not edit
class LaagProductidentificatiecode(ABC):
    """Abstracte waarmee aan een laag de eigenschap productidentificatiecode wordt toegekend."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagProductidentificatiecode'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._productidentificatiecode = OTLAttribuut(field=DtcProductidentificatiecode,
                                                      naam='productidentificatiecode',
                                                      label='productidentificatiecode',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagProductidentificatiecode.productidentificatiecode',
                                                      definition='De productidentificatiecode van het gebruikte product (bv. COPRO code of Benor code).',
                                                      owner=self)

    @property
    def productidentificatiecode(self):
        """De productidentificatiecode van het gebruikte product (bv. COPRO code of Benor code)."""
        return self._productidentificatiecode.waarde

    @productidentificatiecode.setter
    def productidentificatiecode(self, value):
        self._productidentificatiecode.set_waarde(value, owner=self)
