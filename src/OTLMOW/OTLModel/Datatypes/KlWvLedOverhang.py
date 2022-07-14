# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedOverhang(KeuzelijstField):
    """Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan."""
    naam = 'KlWvLedOverhang'
    label = 'WV LED overhang'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedOverhang'
    definition = 'Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedOverhang'
    options = {
        '0': KeuzelijstWaarde(invulwaarde='0',
                              label='+0',
                              status='ingebruik',
                              definitie='+0',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/0'),
        '0-5': KeuzelijstWaarde(invulwaarde='0-5',
                                label='+0.5',
                                status='ingebruik',
                                definitie='+0,5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/0-5'),
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='-1',
                              status='ingebruik',
                              definitie='-1',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/1'),
        '1-5': KeuzelijstWaarde(invulwaarde='1-5',
                                label='+1.5',
                                status='ingebruik',
                                definitie='+1,5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/1-5'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='-2',
                              status='ingebruik',
                              definitie='-2',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/2'),
        '2-5': KeuzelijstWaarde(invulwaarde='2-5',
                                label='+2.5',
                                status='ingebruik',
                                definitie='+2,5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/2-5'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='-3',
                              status='ingebruik',
                              definitie='-3',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/3'),
        '3-5': KeuzelijstWaarde(invulwaarde='3-5',
                                label='+3.5',
                                status='ingebruik',
                                definitie='+3,5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/3-5'),
        '4': KeuzelijstWaarde(invulwaarde='4',
                              label='-4',
                              status='ingebruik',
                              definitie='-4',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/4'),
        '4-5': KeuzelijstWaarde(invulwaarde='4-5',
                                label='+4.5',
                                status='ingebruik',
                                definitie='+4,5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/4-5'),
        '5': KeuzelijstWaarde(invulwaarde='5',
                              label='-5',
                              status='ingebruik',
                              definitie='-5',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/5'),
        'o+0': KeuzelijstWaarde(invulwaarde='o+0',
                                label='o+0',
                                status='uitgebruik',
                                definitie='o+0',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+0'),
        'o+0.5': KeuzelijstWaarde(invulwaarde='o+0.5',
                                  label='o+0.5',
                                  status='uitgebruik',
                                  definitie='o+0,5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+0.5'),
        'o+1.5': KeuzelijstWaarde(invulwaarde='o+1.5',
                                  label='o+1.5',
                                  status='uitgebruik',
                                  definitie='o+1,5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+1.5'),
        'o+2.5': KeuzelijstWaarde(invulwaarde='o+2.5',
                                  label='o+2.5',
                                  status='uitgebruik',
                                  definitie='o+2,5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+2.5'),
        'o+3.5': KeuzelijstWaarde(invulwaarde='o+3.5',
                                  label='o+3.5',
                                  status='uitgebruik',
                                  definitie='o+3,5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+3.5'),
        'o+4.5': KeuzelijstWaarde(invulwaarde='o+4.5',
                                  label='o+4.5',
                                  status='uitgebruik',
                                  definitie='o+4,5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+4.5'),
        'o-1': KeuzelijstWaarde(invulwaarde='o-1',
                                label='o-1',
                                status='uitgebruik',
                                definitie='o-1',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-1'),
        'o-2': KeuzelijstWaarde(invulwaarde='o-2',
                                label='o-2',
                                status='uitgebruik',
                                definitie='o-2',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-2'),
        'o-3': KeuzelijstWaarde(invulwaarde='o-3',
                                label='o-3',
                                status='uitgebruik',
                                definitie='o-3',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-3'),
        'o-4': KeuzelijstWaarde(invulwaarde='o-4',
                                label='o-4',
                                status='uitgebruik',
                                definitie='o-4',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-4'),
        'o-5': KeuzelijstWaarde(invulwaarde='o-5',
                                label='o-5',
                                status='uitgebruik',
                                definitie='o-5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-5')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlWvLedOverhang.get_dummy_data()

