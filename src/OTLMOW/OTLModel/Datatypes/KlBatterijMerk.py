# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBatterijMerk(KeuzelijstField):
    """Het merk van de batterij."""
    naam = 'KlBatterijMerk'
    label = 'Batterij merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBatterijMerk'
    definition = 'Het merk van de batterij.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBatterijMerk'
    options = {
    }
