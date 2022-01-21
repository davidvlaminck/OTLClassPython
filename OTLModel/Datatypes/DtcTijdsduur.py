# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInMinuut import KwantWrdInMinuut
from OTLModel.Datatypes.KwantWrdInSeconde import KwantWrdInSeconde
from OTLModel.Datatypes.KwantWrdInUur import KwantWrdInUur


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTijdsduurWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._minuten = OTLAttribuut(field=KwantWrdInMinuut,
                                     naam='minuten',
                                     label='minuten',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTijdsduur.minuten',
                                     definition='Het aantal minuten.')

        self._seconden = OTLAttribuut(field=KwantWrdInSeconde,
                                      naam='seconden',
                                      label='seconden',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTijdsduur.seconden',
                                      definition='Het aantal seconden.')

        self._uren = OTLAttribuut(field=KwantWrdInUur,
                                  naam='uren',
                                  label='uren',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTijdsduur.uren',
                                  definition='Het aantal uren.')

    @property
    def minuten(self):
        """Het aantal minuten."""
        return self._minuten.waarde

    @minuten.setter
    def minuten(self, value):
        self._minuten.set_waarde(value, owner=self._parent)

    @property
    def seconden(self):
        """Het aantal seconden."""
        return self._seconden.waarde

    @seconden.setter
    def seconden(self, value):
        self._seconden.set_waarde(value, owner=self._parent)

    @property
    def uren(self):
        """Het aantal uren."""
        return self._uren.waarde

    @uren.setter
    def uren(self, value):
        self._uren.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTijdsduur(ComplexField, AttributeInfo):
    """Complex datatype voor de instelling van een tijdsbepaling."""
    naam = 'DtcTijdsduur'
    label = 'Tijdsduur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTijdsduur'
    definition = 'Complex datatype voor de instelling van een tijdsbepaling.'
    waardeObject = DtcTijdsduurWaarden

    def __str__(self):
        return ComplexField.__str__(self)

