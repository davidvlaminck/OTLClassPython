# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Proef import Proef
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVlakheid(Proef):
    """Controle van de effenheid van het oppervlak met behulp van een 3 meter lange rei volgens NBN EN 13036-7."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVlakheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._vlakheid = OTLAttribuut(field=DtcDocument,
                                      naam='vlakheid',
                                      label='vlakheid',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVlakheid.vlakheid',
                                      definition='Proefresultaten van de vlakheid.')

    @property
    def vlakheid(self):
        """Proefresultaten van de vlakheid."""
        return self._vlakheid.waarde

    @vlakheid.setter
    def vlakheid(self, value):
        self._vlakheid.set_waarde(value, owner=self)