﻿import json
from unittest import TestCase

from AllCasesTestClass import AllCasesTestClass
from OTLMOW.Facility.DotnotatieHelper import DotnotatieHelper
from OTLMOW.Facility.SettingsManager import SettingsManager
from OTLMOW.OTLModel.Classes.BestratingVanKassei import BestratingVanKassei


class JsonLdTestData:
    simple = '{ "a": "value a", "b": "value b" }'
    dict_in_dict = '{ "a": "value a", "b": { "c": "value c", "d": "value d" } }'
    list = '{ "a": [1,2] }'
    listdict_in_dict = '{ "a": "value a", "b": [{ "c": "value c", "d": "value d" }, { "e": "value e", "f": "value f" }]}'

class DotnotatieHelperTests(TestCase):
    def test_flatten_dict_simple(self):
        input_dict = json.loads(JsonLdTestData.simple)

        output = DotnotatieHelper().flatten_dict(input_dict=input_dict)
        expected = {"a": "value a", "b": "value b"}
        self.assertDictEqual(expected, output)

    def test_flatten_dict_dict_in_dict(self):
        input_dict = json.loads(JsonLdTestData.dict_in_dict)

        output = DotnotatieHelper().flatten_dict(input_dict)
        expected = {"a": "value a", "b.c": "value c", "b.d": "value d"}
        self.assertDictEqual(expected, output)

    def test_flatten_dict_list(self):
        input_dict = json.loads(JsonLdTestData.list)

        output = DotnotatieHelper().flatten_dict(input_dict=input_dict)
        expected = {"a[0]": 1, "a[1]": 2}
        self.assertDictEqual(expected, output)

    def test_flatten_dict_listdict_in_dict(self):
        input_dict = json.loads(JsonLdTestData.listdict_in_dict)

        output = DotnotatieHelper().flatten_dict(input_dict=input_dict)
        expected = {"a": "value a", "b[0].c": "value c", "b[0].d": "value d", "b[1].e": "value e", "b[1].f": "value f"}
        self.assertDictEqual(expected, output)

    def test_set_attribute_by_dotnotatie_decimal_value(self):
        b = BestratingVanKassei()

        with self.subTest("correctly typed and convert=True"):
            DotnotatieHelper.set_attribute_by_dotnotatie(b, 'afmetingVanBestratingselementBxl.breedte.waarde', 9.0, convert=True)
            self.assertEqual(9.0, b.afmetingVanBestratingselementBxl.breedte.waarde)

        with self.subTest("correctly typed and convert=False"):
            DotnotatieHelper.set_attribute_by_dotnotatie(b, 'afmetingVanBestratingselementBxl.breedte.waarde', 8.0, convert=False)
            self.assertEqual(8.0, b.afmetingVanBestratingselementBxl.breedte.waarde)

        with self.subTest("incorrectly typed and convert=True"):
            DotnotatieHelper.set_attribute_by_dotnotatie(b, 'afmetingVanBestratingselementBxl.breedte.waarde', "7.0", convert=True)
            self.assertEqual(7.0, b.afmetingVanBestratingselementBxl.breedte.waarde)

        with self.subTest("incorrectly typed and convert=False (converted by set_waarde method on attribute itself)"):
            DotnotatieHelper.set_attribute_by_dotnotatie(b, 'afmetingVanBestratingselementBxl.breedte.waarde', "6.0", convert=False)
            self.assertEqual(6.0, b.afmetingVanBestratingselementBxl.breedte.waarde)

    def test_get_attributes_by_dotnotatie_default_values(self):
        instance = AllCasesTestClass()

        with self.subTest("attribute 1 level deep"):
            result_attribute = DotnotatieHelper.get_attributes_by_dotnotatie(instance, 'testDecimalNumberField')
            expected_attribute = instance._testDecimalNumberField
            self.assertEqual(expected_attribute, result_attribute)

        with self.subTest("attribute 1 level deep with cardinality > 1"):
            result_attribute = DotnotatieHelper.get_attributes_by_dotnotatie(instance, 'testStringFieldMetKard[]')
            expected_attribute = instance._testStringFieldMetKard
            self.assertEqual(expected_attribute, result_attribute)

        with self.subTest("attribute 2 levels deep with waarde shortcut disabled"):
            result_attribute = DotnotatieHelper.get_attributes_by_dotnotatie(instance, 'testKwantWrd.waarde')
            expected_attribute = instance.testKwantWrd._waarde
            self.assertEqual(expected_attribute, result_attribute)

        with self.subTest("attribute 2 levels deep"):
            result_attribute = DotnotatieHelper.get_attributes_by_dotnotatie(instance, 'testComplexType.testStringField')
            expected_attribute = instance.testComplexType._testStringField
            self.assertEqual(expected_attribute, result_attribute)

        with self.subTest("attribute 2 levels deep with cardinality > 1"):
            result_attribute = DotnotatieHelper.get_attributes_by_dotnotatie(instance,
                                                                            'testComplexTypeMetKard[].testStringFieldMetKard[]')
            expected_attributes = list(map(lambda c: c._testStringFieldMetKard, instance.testComplexTypeMetKard))
            self.assertEqual(expected_attributes, result_attribute)

        with self.subTest("attribute 3 levels deep"):
            result_attribute = DotnotatieHelper.get_attributes_by_dotnotatie(instance, 'testComplexType.testComplexType2.testStringField')
            expected_attribute = instance.testComplexType.testComplexType2._testStringField
            self.assertEqual(expected_attribute, result_attribute)

        with self.subTest("attribute 3 levels deep with cardinality > 1"):
            result_attribute = DotnotatieHelper.get_attributes_by_dotnotatie(instance,
                                                                            'testComplexTypeMetKard[].testComplexType2MetKard[].testStringFieldMetKard[]')
            expected_testComplexType2MetKard = list(map(lambda c: c._testComplexType2MetKard.waarde, instance.testComplexTypeMetKard))
            expected_attributes = [list(map(lambda c: c[0]._testStringFieldMetKard, expected_testComplexType2MetKard))]
            self.assertEqual(expected_attributes, result_attribute)

        with self.subTest("attribute 4 levels deep with waarde shortcut disabled"):
            result_attribute = DotnotatieHelper.get_attributes_by_dotnotatie(instance,
                                                                            'testComplexType.testComplexType2.testKwantWrd.waarde')
            expected_attribute = instance.testComplexType.testComplexType2.testKwantWrd._waarde
            self.assertEqual(expected_attribute, result_attribute)

    def test_get_attributes_by_dotnotatie_waarde_shortcut(self):
        settingsmanager = SettingsManager(settings_path='')
        settingsmanager.settings['file_formats'] = [
            {'name': 'OTLMOW',
             'dotnotatie': {
                 'separator': '.',
                 'cardinality separator': '|',
                 'cardinality indicator': '[]',
                 'waarde_shortcut_applicable': True}
             }]
        settingsmanager.load_settings_in_app()

        instance = AllCasesTestClass()
        with self.subTest("attribute 2 levels deep with waarde shortcut enabled"):
            result_attribute = DotnotatieHelper.get_attributes_by_dotnotatie(instance, 'testKwantWrd')
            expected_attribute = instance.testKwantWrd._waarde
            self.assertEqual(expected_attribute, result_attribute)

        with self.subTest("attribute 2 levels deep with waarde shortcut enabled and cardinality > 1"):
            result_attribute = DotnotatieHelper.get_attributes_by_dotnotatie(instance, 'testKwantWrdMetKard[]')
            expected_attribute = [instance.testKwantWrdMetKard[0]._waarde]
            self.assertEqual(expected_attribute, result_attribute)

        with self.subTest("attribute 4 levels deep with waarde shortcut disabled"):
            result_attribute = DotnotatieHelper.get_attributes_by_dotnotatie(instance,
                                                                             'testComplexType.testComplexType2.testKwantWrd')
            expected_attribute = instance.testComplexType.testComplexType2.testKwantWrd._waarde
            self.assertEqual(expected_attribute, result_attribute)

        # restore original settings
        settingsmanager.settings['file_formats'] = [
            {'name': 'OTLMOW',
             'dotnotatie': {
                 'separator': '.',
                 'cardinality separator': '|',
                 'cardinality indicator': '[]',
                 'waarde_shortcut_applicable': False}
             }]
        settingsmanager.load_settings_in_app()




