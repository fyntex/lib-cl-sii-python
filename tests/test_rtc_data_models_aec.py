from __future__ import annotations

import unittest
from datetime import date, datetime

from cl_sii.dte.constants import TipoDteEnum
from cl_sii.dte.data_models import DteDataL1, DteNaturalKey, DteXmlData
from cl_sii.libs import encoding_utils
from cl_sii.libs import tz_utils
from cl_sii.rtc.data_models import CesionL2, CesionNaturalKey, CesionAltNaturalKey
from cl_sii.rtc.data_models_aec import CesionAecXml, AecXml
from cl_sii.rut import Rut

from .utils import read_test_file_bytes


class CesionAecXmlTest(unittest.TestCase):
    """
    Tests for :class:`CesionAecXml`.
    """

    def _set_obj_1(self) -> None:
        obj = CesionAecXml(
            dte=DteDataL1(
                emisor_rut=Rut('76354771-K'),
                tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
                folio=170,
                fecha_emision_date=date(2019, 4, 1),
                receptor_rut=Rut('96790240-3'),
                monto_total=2996301,
            ),
            seq=1,
            cedente_rut=Rut('76354771-K'),
            cesionario_rut=Rut('76389992-6'),
            monto_cesion=2996301,
            fecha_cesion_dt=tz_utils.convert_naive_dt_to_tz_aware(
                dt=datetime(2019, 4, 1, 10, 22, 2),
                tz=CesionAecXml.DATETIME_FIELDS_TZ,
            ),
            fecha_ultimo_vencimiento=date(2019, 5, 1),
            cedente_razon_social='SERVICIOS BONILLA Y LOPEZ Y COMPAÑIA LIMITADA',
            cedente_direccion='MERCED 753  16 ARBOLEDA DE QUIILOTA',
            cedente_email='enaconltda@gmail.com',
            cesionario_razon_social='ST CAPITAL S.A.',
            cesionario_direccion='Isidora Goyenechea 2939 Oficina 602',
            cesionario_email='fynpal-app-notif-st-capital@fynpal.com',
            dte_deudor_email=None,
            cedente_declaracion_jurada=(
                'Se declara bajo juramento que SERVICIOS BONILLA Y LOPEZ Y COMPAÑIA '
                'LIMITADA, RUT 76354771-K ha puesto a disposición del cesionario ST '
                'CAPITAL S.A., RUT 76389992-6, el o los documentos donde constan los '
                'recibos de las mercaderías entregadas o servicios prestados, entregados '
                'por parte del deudor de la factura MINERA LOS PELAMBRES, RUT 96790240-3, '
                'deacuerdo a lo establecido en la Ley N°19.983.'
            ),
        )
        self.assertIsInstance(obj, CesionAecXml)

        self.obj_1 = obj

    def _set_obj_2(self) -> None:
        obj = CesionAecXml(
            dte=DteDataL1(
                emisor_rut=Rut('76354771-K'),
                tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
                folio=170,
                fecha_emision_date=date(2019, 4, 1),
                receptor_rut=Rut('96790240-3'),
                monto_total=2996301,
            ),
            seq=2,
            cedente_rut=Rut('76389992-6'),
            cesionario_rut=Rut('76598556-0'),
            monto_cesion=2996301,
            fecha_cesion_dt=tz_utils.convert_naive_dt_to_tz_aware(
                dt=datetime(2019, 4, 5, 12, 57, 32),
                tz=CesionAecXml.DATETIME_FIELDS_TZ,
            ),
            fecha_ultimo_vencimiento=date(2019, 5, 1),
            cedente_razon_social='ST CAPITAL S.A.',
            cedente_direccion='Isidora Goyenechea 2939 Oficina 602',
            cedente_email='APrat@Financiaenlinea.com',
            cesionario_razon_social='Fondo de Inversión Privado Deuda y Facturas',
            cesionario_direccion='Arrayan 2750 Oficina 703 Providencia',
            cesionario_email='solicitudes@stcapital.cl',
            dte_deudor_email=None,
            cedente_declaracion_jurada=(
                'Se declara bajo juramento que ST CAPITAL S.A., RUT 76389992-6 ha puesto '
                'a disposicion del cesionario Fondo de Inversión Privado Deuda y Facturas, '
                'RUT 76598556-0, el documento validamente emitido al deudor MINERA LOS '
                'PELAMBRES, RUT 96790240-3.'
            ),
        )
        self.assertIsInstance(obj, CesionAecXml)

        self.obj_2 = obj

    def test_create_new_empty_instance(self) -> None:
        with self.assertRaises(TypeError):
            CesionAecXml()

    def test_natural_key(self) -> None:
        self._set_obj_1()
        self._set_obj_2()

        obj = self.obj_1
        expected_output = CesionNaturalKey(
            dte_key=DteNaturalKey(
                emisor_rut=Rut('76354771-K'),
                tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
                folio=170,
            ),
            seq=1,
        )
        self.assertEqual(obj.natural_key, expected_output)

        obj = self.obj_2
        expected_output = CesionNaturalKey(
            dte_key=DteNaturalKey(
                emisor_rut=Rut('76354771-K'),
                tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
                folio=170,
            ),
            seq=2,
        )
        self.assertEqual(obj.natural_key, expected_output)

    def test_alt_natural_key(self) -> None:
        self._set_obj_1()
        self._set_obj_2()

        obj = self.obj_1
        expected_output = CesionAltNaturalKey(
            dte_key=DteNaturalKey(
                emisor_rut=Rut('76354771-K'),
                tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
                folio=170,
            ),
            cedente_rut=Rut('76354771-K'),
            cesionario_rut=Rut('76389992-6'),
            fecha_cesion_dt=tz_utils.convert_naive_dt_to_tz_aware(
                dt=datetime(2019, 4, 1, 10, 22),
                tz=CesionAltNaturalKey.DATETIME_FIELDS_TZ,
            ),
        )
        self.assertEqual(obj.alt_natural_key, expected_output)

        obj = self.obj_2
        expected_output = CesionAltNaturalKey(
            dte_key=DteNaturalKey(
                emisor_rut=Rut('76354771-K'),
                tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
                folio=170,
            ),
            cedente_rut=Rut('76389992-6'),
            cesionario_rut=Rut('76598556-0'),
            fecha_cesion_dt=tz_utils.convert_naive_dt_to_tz_aware(
                dt=datetime(2019, 4, 5, 12, 57),
                tz=CesionAltNaturalKey.DATETIME_FIELDS_TZ,
            ),
        )
        self.assertEqual(obj.alt_natural_key, expected_output)


class AecXmlTest(unittest.TestCase):
    """
    Tests for :class:`AecXml`.
    """

    def _set_obj_1(self) -> None:
        obj_dte_signature_value = encoding_utils.decode_base64_strict(
            read_test_file_bytes(
                'test_data/sii-crypto/DTE--76354771-K--33--170-signature-value-base64.txt',
            ),
        )
        obj_dte_signature_x509_cert_der = read_test_file_bytes(
            'test_data/sii-crypto/DTE--76354771-K--33--170-cert.der',
        )
        obj_dte = DteXmlData(
            emisor_rut=Rut('76354771-K'),
            tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
            folio=170,
            fecha_emision_date=date(2019, 4, 1),
            receptor_rut=Rut('96790240-3'),
            monto_total=2996301,
            emisor_razon_social='INGENIERIA ENACON SPA',
            receptor_razon_social='MINERA LOS PELAMBRES',
            fecha_vencimiento_date=None,
            firma_documento_dt=tz_utils.convert_naive_dt_to_tz_aware(
                dt=datetime(2019, 4, 1, 1, 36, 40),
                tz=DteXmlData.DATETIME_FIELDS_TZ,
            ),
            signature_value=obj_dte_signature_value,
            signature_x509_cert_der=obj_dte_signature_x509_cert_der,
            emisor_giro='Ingenieria y Construccion',
            emisor_email='ENACONLTDA@GMAIL.COM',
            receptor_email=None,
        )

        obj_cesion_1 = CesionAecXml(
            dte=DteDataL1(
                emisor_rut=Rut('76354771-K'),
                tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
                folio=170,
                fecha_emision_date=date(2019, 4, 1),
                receptor_rut=Rut('96790240-3'),
                monto_total=2996301,
            ),
            seq=1,
            cedente_rut=Rut('76354771-K'),
            cesionario_rut=Rut('76389992-6'),
            monto_cesion=2996301,
            fecha_cesion_dt=tz_utils.convert_naive_dt_to_tz_aware(
                dt=datetime(2019, 4, 1, 10, 22, 2),
                tz=CesionAecXml.DATETIME_FIELDS_TZ,
            ),
            fecha_ultimo_vencimiento=date(2019, 5, 1),
            cedente_razon_social='SERVICIOS BONILLA Y LOPEZ Y COMPAÑIA LIMITADA',
            cedente_direccion='MERCED 753  16 ARBOLEDA DE QUIILOTA',
            cedente_email='enaconltda@gmail.com',
            cesionario_razon_social='ST CAPITAL S.A.',
            cesionario_direccion='Isidora Goyenechea 2939 Oficina 602',
            cesionario_email='fynpal-app-notif-st-capital@fynpal.com',
            dte_deudor_email=None,
            cedente_declaracion_jurada=(
                'Se declara bajo juramento que SERVICIOS BONILLA Y LOPEZ Y COMPAÑIA '
                'LIMITADA, RUT 76354771-K ha puesto a disposición del cesionario ST '
                'CAPITAL S.A., RUT 76389992-6, el o los documentos donde constan los '
                'recibos de las mercaderías entregadas o servicios prestados, entregados '
                'por parte del deudor de la factura MINERA LOS PELAMBRES, RUT 96790240-3, '
                'deacuerdo a lo establecido en la Ley N°19.983.'
            ),
        )

        obj_cesion_2 = CesionAecXml(
            dte=DteDataL1(
                emisor_rut=Rut('76354771-K'),
                tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
                folio=170,
                fecha_emision_date=date(2019, 4, 1),
                receptor_rut=Rut('96790240-3'),
                monto_total=2996301,
            ),
            seq=2,
            cedente_rut=Rut('76389992-6'),
            cesionario_rut=Rut('76598556-0'),
            monto_cesion=2996301,
            fecha_cesion_dt=tz_utils.convert_naive_dt_to_tz_aware(
                dt=datetime(2019, 4, 5, 12, 57, 32),
                tz=CesionAecXml.DATETIME_FIELDS_TZ,
            ),
            fecha_ultimo_vencimiento=date(2019, 5, 1),
            cedente_razon_social='ST CAPITAL S.A.',
            cedente_direccion='Isidora Goyenechea 2939 Oficina 602',
            cedente_email='APrat@Financiaenlinea.com',
            cesionario_razon_social='Fondo de Inversión Privado Deuda y Facturas',
            cesionario_direccion='Arrayan 2750 Oficina 703 Providencia',
            cesionario_email='solicitudes@stcapital.cl',
            dte_deudor_email=None,
            cedente_declaracion_jurada=(
                'Se declara bajo juramento que ST CAPITAL S.A., RUT 76389992-6 ha puesto '
                'a disposicion del cesionario Fondo de Inversión Privado Deuda y Facturas, '
                'RUT 76598556-0, el documento validamente emitido al deudor MINERA LOS '
                'PELAMBRES, RUT 96790240-3.'
            ),
        )

        obj = AecXml(
            dte=obj_dte,
            cedente_rut=Rut('76389992-6'),
            cesionario_rut=Rut('76598556-0'),
            fecha_firma_dt=tz_utils.convert_naive_dt_to_tz_aware(
                dt=datetime(2019, 4, 5, 12, 57, 32),
                tz=AecXml.DATETIME_FIELDS_TZ,
            ),
            signature_value=None,  # TODO
            signature_x509_cert_der=None,  # TODO
            cesiones=[
                obj_cesion_1,
                obj_cesion_2,
            ],
            contacto_nombre='ST Capital Servicios Financieros',
            contacto_telefono=None,
            contacto_email='APrat@Financiaenlinea.com',
        )
        self.assertIsInstance(obj, AecXml)

        self.obj_1 = obj
        self.obj_1_dte = obj_dte
        self.obj_1_cesion_1 = obj_cesion_1
        self.obj_1_cesion_2 = obj_cesion_2

    def test_create_new_empty_instance(self) -> None:
        with self.assertRaises(TypeError):
            AecXml()

    def test_natural_key(self) -> None:
        self._set_obj_1()

        obj = self.obj_1
        expected_output = CesionNaturalKey(
            dte_key=DteNaturalKey(
                emisor_rut=Rut('76354771-K'),
                tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
                folio=170,
            ),
            seq=2,
        )
        self.assertEqual(obj.natural_key, expected_output)

    def test_alt_natural_key(self) -> None:
        self._set_obj_1()

        obj = self.obj_1
        expected_output = CesionAltNaturalKey(
            dte_key=DteNaturalKey(
                emisor_rut=Rut('76354771-K'),
                tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
                folio=170,
            ),
            cedente_rut=Rut('76389992-6'),
            cesionario_rut=Rut('76598556-0'),
            fecha_cesion_dt=tz_utils.convert_naive_dt_to_tz_aware(
                dt=datetime(2019, 4, 5, 12, 57),
                tz=CesionAltNaturalKey.DATETIME_FIELDS_TZ,
            ),
        )
        self.assertEqual(obj.alt_natural_key, expected_output)

    def test_slug(self) -> None:
        self._set_obj_1()

        obj = self.obj_1
        expected_output = '76354771-K--33--170--2'
        self.assertEqual(obj.slug, expected_output)

    def test_last_cesion(self) -> None:
        self._set_obj_1()

        obj = self.obj_1
        obj_cesion_2 = self.obj_1_cesion_2
        self.assertEqual(obj.cesiones[-1], obj_cesion_2)
        self.assertEqual(obj._last_cesion, obj.cesiones[-1])

    def test_as_cesion_l2(self) -> None:
        self._set_obj_1()

        obj = self.obj_1
        expected_output = CesionL2(
            dte_key=DteNaturalKey(
                emisor_rut=Rut('76354771-K'),
                tipo_dte=TipoDteEnum.FACTURA_ELECTRONICA,
                folio=170,
            ),
            seq=2,
            cedente_rut=Rut('76389992-6'),
            cesionario_rut=Rut('76598556-0'),
            fecha_cesion_dt=tz_utils.convert_naive_dt_to_tz_aware(
                dt=datetime(2019, 4, 5, 12, 57, 32),
                tz=CesionL2.DATETIME_FIELDS_TZ,
            ),
            monto_cedido=2996301,
            fecha_firma_dt=tz_utils.convert_naive_dt_to_tz_aware(
                dt=datetime(2019, 4, 5, 12, 57, 32),
                tz=CesionL2.DATETIME_FIELDS_TZ,
            ),
            dte_receptor_rut=Rut('96790240-3'),
            dte_fecha_emision=date(2019, 4, 1),
            dte_monto_total=2996301,
            fecha_ultimo_vencimiento=date(2019, 5, 1),
            cedente_razon_social='ST CAPITAL S.A.',
            cedente_email='APrat@Financiaenlinea.com',
            cesionario_razon_social='Fondo de Inversión Privado Deuda y Facturas',
            cesionario_email='solicitudes@stcapital.cl',
            dte_emisor_razon_social='INGENIERIA ENACON SPA',
            dte_receptor_razon_social='MINERA LOS PELAMBRES',
            dte_deudor_email=None,
            cedente_declaracion_jurada=(
                'Se declara bajo juramento que ST CAPITAL S.A., RUT 76389992-6 ha puesto '
                'a disposicion del cesionario Fondo de Inversión Privado Deuda y Facturas, '
                'RUT 76598556-0, el documento validamente emitido al deudor MINERA LOS '
                'PELAMBRES, RUT 96790240-3.'
            ),
            dte_fecha_vencimiento=None,
            contacto_nombre='ST Capital Servicios Financieros',
            contacto_telefono=None,
            contacto_email='APrat@Financiaenlinea.com',
        )
        obj_cesion_l2 = obj.as_cesion_l2()
        self.assertEqual(obj_cesion_l2, expected_output)
        self.assertEqual(obj_cesion_l2.natural_key, obj.natural_key)
        self.assertEqual(obj_cesion_l2.alt_natural_key, obj.alt_natural_key)
        self.assertEqual(obj_cesion_l2.dte_key, obj.dte.natural_key)
