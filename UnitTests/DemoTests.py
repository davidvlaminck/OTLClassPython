﻿import unittest
from unittest import TestCase

from Facility.OTLFacility import OTLFacility
from Loggers.NoneLogger import NoneLogger
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.Stroomkring import Stroomkring


class DemoTests(TestCase):
    #@unittest.skip('not an actual unit test')
    def test_demo(self):
        fac = OTLFacility(NoneLogger())
        kring = fac.asset_factory.dynamic_create_instance_from_name('Stroomkring')
        kring.typeURI  # print uri to verify type
        self.assertTrue(isinstance(kring, Stroomkring))  # other way in python to verify

        kring = Stroomkring()  # alternative to create Stroomkring
        self.assertTrue(isinstance(kring, AIMObject))  # true inheritance
        kring.toestand = 'in-gebruik'


        print(kring.info())
        print(kring.attr_info(''))

        print(kring.attr_info('assetId'))
        print(kring.attr_type_info('assetId'))

        kring.assetId.identificator = 'eigen_id'
        kring.assetId.toegekendDoor = 'Python'
        print(kring.assetId)  # print assetId

        kring.theoretischeLevensduur.waarde = 120

        # show some value validation

        # show relaties:
        # print(kring._showGeldigeRelaties())

        #fac.davieExporter.export_objects_to_json_file(kring, 'kring.json')

        #fac.visualiser.show([kring])








