from unittest import TestCase

from AllCasesTestClass import AllCasesTestClass
from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


class NonStringableObject(object):
    def __str__(self):
        pass


class KeuzelijstFieldTests(TestCase):
    def test_full_test_on_testclass_kard_1(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNone(instance.testKeuzelijst)

        with self.subTest('assign values to Keuzelijst with kard 1'):
            instance.testKeuzelijst = 'waarde-1'
            self.assertEqual('waarde-1', instance.testKeuzelijst)
            instance.testKeuzelijst = 'waarde-2'
            self.assertEqual('waarde-2', instance.testKeuzelijst)

    def test_full_test_on_testclass_kard_more(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNone(instance.testKeuzelijstMetKard)
            self.assertFalse(instance._testKeuzelijstMetKard.field.waarde_shortcut_applicable)

        with self.subTest('assign value directly to KeuzelijstMetKard with kard *'):
            instance.testKeuzelijstMetKard = ['waarde-1']
            self.assertEqual('waarde-1', instance.testKeuzelijstMetKard[0])

        with self.subTest('assign value to KeuzelijstMetKard with kard * by using add_value method'):
            instance._testKeuzelijstMetKard.add_value('waarde-2')
            self.assertEqual('waarde-1', instance.testKeuzelijstMetKard[0])
            self.assertEqual('waarde-2', instance.testKeuzelijstMetKard[1])

        with self.subTest('assign bad value to KeuzelijstMetKard with kard *'):
            with self.assertRaises(ValueError):
                instance.testKeuzelijstMetKard = ['waarde-1', 'a']
