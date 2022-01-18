# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKubiekeMeterPerSecondeEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeMeterPerSeconde.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in kubieke meter per seconde.',
                                              constraints='',
                                              usagenote='"m3/s"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKubiekeMeterPerSeconde(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInKubiekeMeterPerSeconde'
    label = 'Kwantitatieve waarde in kubieke meter per seconde'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeMeterPerSeconde'
    definition = 'Een kwantitatieve waarde die een getal in kubieke meter per seconde uitdrukt.'
    eenheid = KwantWrdInKubiekeMeterPerSecondeEenheid()
