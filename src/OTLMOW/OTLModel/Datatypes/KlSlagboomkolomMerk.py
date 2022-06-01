# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlagboomkolomMerk(KeuzelijstField):
    """Het merk van de slagboomkolom."""
    naam = 'KlSlagboomkolomMerk'
    label = 'Slagboomkolom merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlagboomkolomMerk'
    definition = 'Het merk van de slagboomkolom.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlagboomkolomMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSlagboomkolomMerk.get_dummy_data()

