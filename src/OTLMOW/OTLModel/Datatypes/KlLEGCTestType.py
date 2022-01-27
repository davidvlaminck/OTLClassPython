# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCTestType(KeuzelijstField):
    """Het test type van het geluidswerend scherm."""
    naam = 'KlLEGCTestType'
    label = 'Test type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCTestType'
    definition = 'Het test type van het geluidswerend scherm.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCTestType'
    options = {
        'geluidsabsorptie': KeuzelijstWaarde(invulwaarde='geluidsabsorptie',
                                             label='geluidsabsorptie',
                                             definitie='Proef : De ééngetalsaanduiding als waarde voor de geluidsabsorptie',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCTestType/geluidsabsorptie'),
        'luchtgeluidsisolatie': KeuzelijstWaarde(invulwaarde='luchtgeluidsisolatie',
                                                 label='luchtgeluidsisolatie',
                                                 definitie='Proef : De ééngetalsaanduiding voor luchtgeluidsisolatie',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCTestType/luchtgeluidsisolatie')
    }
