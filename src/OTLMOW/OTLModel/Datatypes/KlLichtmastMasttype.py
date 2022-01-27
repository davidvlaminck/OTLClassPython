# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLichtmastMasttype(KeuzelijstField):
    """Lijst van mogelijke types voor lichtmasten."""
    naam = 'KlLichtmastMasttype'
    label = 'lichtmast type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastMasttype'
    definition = 'Lijst van mogelijke types voor lichtmasten.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLichtmastMasttype'
    options = {
        'B': KeuzelijstWaarde(invulwaarde='B',
                              label='B',
                              definitie='Betonnen paal',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/B'),
        'BS': KeuzelijstWaarde(invulwaarde='BS',
                               label='BS',
                               definitie='Betonnen paal op voet',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/BS'),
        'K': KeuzelijstWaarde(invulwaarde='K',
                              label='K',
                              definitie='Kreukelpaal met arm',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/K'),
        'KS': KeuzelijstWaarde(invulwaarde='KS',
                               label='KS',
                               definitie='Kreukelpaal met arm op voet',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/KS'),
        'M': KeuzelijstWaarde(invulwaarde='M',
                              label='M',
                              definitie='Metalen paal met arm',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/M'),
        'MS': KeuzelijstWaarde(invulwaarde='MS',
                               label='MS',
                               definitie='Metalen paal met arm en voet',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/MS'),
        'RK': KeuzelijstWaarde(invulwaarde='RK',
                               label='RK',
                               definitie='Kreukelpaal',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/RK'),
        'RKS': KeuzelijstWaarde(invulwaarde='RKS',
                                label='RKS',
                                definitie='Kreukelpaal op voet',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/RKS'),
        'RM': KeuzelijstWaarde(invulwaarde='RM',
                               label='RM',
                               definitie='Rechte metalen paal',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/RM'),
        'RMS': KeuzelijstWaarde(invulwaarde='RMS',
                                label='RMS',
                                definitie='Rechte metalen paal op voet',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/RMS')
    }
