﻿from unittest import TestCase

from Facility.AssetFactory import AssetFactory
from OTLModel.Classes.Aftakking import Aftakking
from OTLModel.Classes.Agent import Agent
from OTLModel.Classes.ProefStroefheid import ProefStroefheid
from OTLModel.Classes.Stroomkring import Stroomkring


class AssetFactoryTests(TestCase):
    def test_dynamic_create_instance_from_uri_using_valid_uri(self):
        factory = AssetFactory()
        uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking'
        asset_created = factory.dynamic_create_instance_from_uri(uri)
        self.assertEqual(uri, asset_created.typeURI)

    def test_dynamic_create_instance_from_uri_using_invalid_uri(self):
        factory = AssetFactory()
        uri = 'https://bad.uri.com'
        with self.assertRaises(ValueError):
            factory.dynamic_create_instance_from_uri(uri)

    def test_get_public_fieldlist_from_object_None(self):
        factory = AssetFactory()
        with self.assertRaises(ValueError):
            factory.get_public_fieldlist_from_object(None)

    def test_get_public_fieldlist_from_object_Aftakking(self):
        factory = AssetFactory()
        fields = factory.get_public_fieldlist_from_object(Aftakking())
        expected_fields = ['assetId', 'bestekPostNummer', 'datumOprichtingObject', 'geometry', 'isActief', 'naam', 'notitie',
                           'standaardBestekPostNummer', 'theoretischeLevensduur', 'toestand', 'typeURI']
        self.assertListEqual(expected_fields, fields)

    def test_create_aimObject_using_other_aimObject_as_template_empty_typeURI(self):
        factory = AssetFactory()
        aftakking = Aftakking()
        created_asset = factory.create_aimObject_using_other_aimObject_as_template(aftakking)
        self.assertEqual(aftakking.typeURI, created_asset.typeURI)

    def test_create_aimObject_using_other_aimObject_as_template_same_typeURI(self):
        factory = AssetFactory()
        aftakking = Aftakking()
        created_asset = factory.create_aimObject_using_other_aimObject_as_template(aftakking, typeURI=aftakking.typeURI)
        self.assertEqual(aftakking.typeURI, created_asset.typeURI)

    def test_create_aimObject_using_other_aimObject_as_template_other_typeURI(self):
        factory = AssetFactory()
        aftakking = Aftakking()
        stroomkringURI = Stroomkring.typeURI
        with self.assertRaises(ValueError) as exc_different_type_uri_empty_fieldList:
            created_asset = factory.create_aimObject_using_other_aimObject_as_template(aftakking, typeURI=stroomkringURI)
        self.assertEqual(str(exc_different_type_uri_empty_fieldList.exception), "parameter typeURI is different from orig_aimObject. parameter fieldsToCopy cannot be empty")

    def test_create_aimObject_using_other_aimObject_as_template_other_typeURI_with_oneField(self):
        factory = AssetFactory()
        aftakking = Aftakking()
        aftakking.naam.waarde = 'aftakking naam'
        aftakking.isActief.waarde = True
        stroomkringURI = Stroomkring.typeURI
        created_asset = factory.create_aimObject_using_other_aimObject_as_template(aftakking, typeURI=stroomkringURI, fieldsToCopy=['naam'])

        self.assertEqual(True, aftakking.isActief.waarde)
        self.assertEqual('aftakking naam', aftakking.naam.waarde)

        self.assertTrue(isinstance(created_asset, Stroomkring))
        self.assertEqual('aftakking naam', created_asset.naam.waarde)
        self.assertIsNone(created_asset.isActief.waarde)


    def test_create_aimObject_using_other_aimObject_as_template_not_OTLAsset(self):
        factory = AssetFactory()
        geen_asset = Agent()
        with self.assertRaises(ValueError):
            factory.create_aimObject_using_other_aimObject_as_template(geen_asset)

    def test_create_aimObject_using_other_aimObject_as_template_StringField_KwantWrd(self):
        factory = AssetFactory()
        orig_aftakking = Aftakking()
        orig_aftakking.theoretischeLevensduur.waarde = 120
        orig_aftakking.naam = 'aftakking originele naam'
        nieuwe_aftakking = factory.create_aimObject_using_other_aimObject_as_template(orig_aftakking)
        self.assertEqual(120, orig_aftakking.theoretischeLevensduur.waarde)
        self.assertEqual('aftakking originele naam', orig_aftakking.naam)
        orig_aftakking.theoretischeLevensduur.waarde = 240
        orig_aftakking.naam = 'aftakking nieuwe naam'

        self.assertEqual(240, orig_aftakking.theoretischeLevensduur.waarde)
        self.assertEqual('aftakking nieuwe naam', orig_aftakking.naam)
        self.assertTrue(isinstance(nieuwe_aftakking, Aftakking))
        self.assertEqual(120, nieuwe_aftakking.theoretischeLevensduur.waarde)
        self.assertEqual('aftakking originele naam', nieuwe_aftakking.naam)

    def test_copy_fields_from_object_to_new_object_invalid_orig_asset(self):
        factory = AssetFactory()
        with self.assertRaises(ValueError) as ex_invalid_orig_asset:
            factory.copy_fields_from_object_to_new_object(None, Aftakking(), ['naam'])
        self.assertEqual(str(ex_invalid_orig_asset.exception), "parameter orig_object is None")

    def test_copy_fields_from_object_to_new_object_invalid_new_asset(self):
        factory = AssetFactory()
        with self.assertRaises(ValueError) as ex_invalid_new_asset:
            factory.copy_fields_from_object_to_new_object(Aftakking(), None, ['naam'])
        self.assertEqual(str(ex_invalid_new_asset.exception), "parameter new_object is None")

    def test_copy_fields_from_object_to_new_object_invalid_field_list(self):
        factory = AssetFactory()
        with self.assertRaises(ValueError) as ex_invalid_field_list:
            factory.copy_fields_from_object_to_new_object(Aftakking(), Aftakking(), [])
        self.assertEqual(str(ex_invalid_field_list.exception), "parameter fieldList is empty or None")
        with self.assertRaises(ValueError) as ex_invalid_field_list:
            factory.copy_fields_from_object_to_new_object(Aftakking(), Aftakking(), None)
        self.assertEqual(str(ex_invalid_field_list.exception), "parameter fieldList is empty or None")

    def test_copy_fields_from_object_to_new_object_StringField(self):
        factory = AssetFactory()
        orig_aftakking = Aftakking()
        nieuwe_aftakking = factory.dynamic_create_instance_from_uri(Aftakking.typeURI)
        orig_aftakking.naam.waarde = 'originele naam'

        factory.copy_fields_from_object_to_new_object(orig_aftakking, nieuwe_aftakking, ['naam'])
        orig_aftakking.naam.waarde = 'nieuwe naam'

        self.assertEqual('nieuwe naam', orig_aftakking.naam.waarde)
        self.assertEqual('originele naam', nieuwe_aftakking.naam.waarde)

    def test_copy_fields_from_object_to_new_object_ComplexField(self):
        factory = AssetFactory()
        orig_aftakking = Aftakking()
        nieuwe_aftakking = factory.dynamic_create_instance_from_uri(Aftakking.typeURI)
        orig_aftakking.assetId.identificator.waarde = 'originele id'

        factory.copy_fields_from_object_to_new_object(orig_aftakking, nieuwe_aftakking, ['assetId'])
        orig_aftakking.assetId.identificator.waarde = 'nieuwe id'

        self.assertEqual('nieuwe id', orig_aftakking.assetId.identificator.waarde)
        self.assertEqual('originele id', nieuwe_aftakking.assetId.identificator.waarde)

    def test_copy_fields_from_object_to_new_object_DotNotatie(self):
        self.assertTrue(False)