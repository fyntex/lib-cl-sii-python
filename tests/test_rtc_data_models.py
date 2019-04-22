from __future__ import annotations

import unittest
from datetime import datetime

from cl_sii.dte.data_models import DteNaturalKey
from cl_sii.dte.constants import TipoDteEnum
from cl_sii.libs import tz_utils
from cl_sii.rtc.data_models import (
    CesionNaturalKey,
    CesionAltNaturalKey,
    CesionL0,
    CesionL1,
    CesionL2,
)
from cl_sii.rut import Rut


class CesionNaturalKeyTest(unittest.TestCase):
    def _set_obj_1(self) -> None:
        obj_dte_natural_key = DteNaturalKey(
            emisor_rut=Rut('76354771-K'),
            tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
            folio=170,
        )

        obj = CesionNaturalKey(
            dte_key=obj_dte_natural_key,
            seq=32,
        )
        self.assertIsInstance(obj, CesionNaturalKey)

        self.obj_1 = obj

    def test_create_new_empty_instance(self) -> None:
        with self.assertRaises(TypeError):
            CesionNaturalKey()

    def test_str_and_repr(self) -> None:
        self._set_obj_1()

        obj = self.obj_1
        expected_output = (
            "CesionNaturalKey("
            "dte_key=DteNaturalKey("
            "emisor_rut=Rut('76354771-K'),"
            " tipo_dte=<TipoDteEnum.FACTURA_ELECTRONICA: 33>,"
            " folio=170"
            "),"
            " seq=32"
            ")"
        )
        self.assertEqual(str(obj), expected_output)
        self.assertEqual(repr(obj), expected_output)

    def test_as_dict(self) -> None:
        self._set_obj_1()

        obj = self.obj_1
        expected_output = dict(
            dte_key=dict(
                emisor_rut=Rut('76354771-K'),
                tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
                folio=170,
            ),
            seq=32,
        )
        self.assertEqual(obj.as_dict(), expected_output)

    def test_slug(self) -> None:
        self._set_obj_1()

        obj = self.obj_1
        expected_output = '76354771-K--33--170--32'
        self.assertEqual(obj.slug, expected_output)


class CesionAltNaturalKeyTest(unittest.TestCase):
    def _set_obj_1(self) -> None:
        obj_dte_natural_key = DteNaturalKey(
            emisor_rut=Rut('76354771-K'),
            tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
            folio=170,
        )

        obj = CesionAltNaturalKey(
            dte_key=obj_dte_natural_key,
            cedente_rut=Rut('76389992-6'),
            cesionario_rut=Rut('76598556-0'),
            fecha_cesion_dt=tz_utils.convert_naive_dt_to_tz_aware(
                dt=datetime(2019, 4, 5, 12, 57, 32),
                tz=CesionAltNaturalKey.DATETIME_FIELDS_TZ,
            ),
        )
        self.assertIsInstance(obj, CesionAltNaturalKey)

        self.obj_1 = obj

    def test_create_new_empty_instance(self) -> None:
        with self.assertRaises(TypeError):
            CesionAltNaturalKey()

    def test_str_and_repr(self) -> None:
        self._set_obj_1()

        obj = self.obj_1
        expected_output = (
            "CesionAltNaturalKey("
            "dte_key=DteNaturalKey("
            "emisor_rut=Rut('76354771-K'),"
            " tipo_dte=<TipoDteEnum.FACTURA_ELECTRONICA: 33>,"
            " folio=170"
            "),"
            " cedente_rut=Rut('76389992-6'),"
            " cesionario_rut=Rut('76598556-0'),"
            " fecha_cesion_dt=datetime.datetime("
            "2019, 4, 5, 12, 57, 32,"
            " tzinfo=<DstTzInfo 'America/Santiago' -03-1 day, 21:00:00 DST>"
            ")"
            ")"
        )
        self.assertEqual(str(obj), expected_output)
        self.assertEqual(repr(obj), expected_output)

    def test_as_dict(self) -> None:
        self._set_obj_1()

        obj = self.obj_1
        expected_output = dict(
            dte_key=dict(
                emisor_rut=Rut('76354771-K'),
                tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
                folio=170,
            ),
            cedente_rut=Rut('76389992-6'),
            cesionario_rut=Rut('76598556-0'),
            fecha_cesion_dt=datetime.fromisoformat('2019-04-05T15:57:32+00:00'),
        )
        self.assertEqual(obj.as_dict(), expected_output)

    def test_slug(self) -> None:
        self._set_obj_1()

        obj = self.obj_1
        expected_output = '76354771-K--33--170--76389992-6--76598556-0--2019-04-05T12:57:32-03:00'
        self.assertEqual(obj.slug, expected_output)


class CesionL0Test(unittest.TestCase):
    def test_create_new_empty_instance(self) -> None:
        with self.assertRaises(TypeError):
            CesionL0()


class CesionL1Test(unittest.TestCase):
    def test_create_new_empty_instance(self) -> None:
        with self.assertRaises(TypeError):
            CesionL1()


class CesionL2Test(unittest.TestCase):
    def test_create_new_empty_instance(self) -> None:
        with self.assertRaises(TypeError):
            CesionL2()
