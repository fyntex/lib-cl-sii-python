import enum
from typing import FrozenSet

from cl_sii.dte.constants import DTE_MONTO_TOTAL_FIELD_MAX_VALUE, TipoDteEnum


# The collection of "tipo DTE" for which it is possible to "ceder" a "DTE".
#   They are defined in a document and also an XML schema.
#   - Document "Formato Archivo Electrónico de Cesión (AEC)"
#     (http://www.sii.cl/factura_electronica/cesion.pdf) are:
#     > Sólo códigos 33, 34, 46 y 43
#   - XML element 'CesionDefType/DocumentoCesion/IdDTE/TipoDTE'
#     - description: "Tipo de DTE"
#     - XML type: 'SiiDte:DTEFacturasType'
#     - source:
#       https://github.com/fyntex/lib-cl-sii-python/blob/7e1c4b52/cl_sii/data/ref/factura_electronica/schemas-xml/Cesion_v10.xsd#L38-L42
#   - XML type 'SiiDte:DTEFacturasType' in official schema 'SiiTypes_v10.xsd'
#     - source:
#       https://github.com/fyntex/lib-cl-sii-python/blob/7e1c4b52/cl_sii/data/ref/factura_electronica/schemas-xml/SiiTypes_v10.xsd#L100-L126
TIPO_DTE_CEDIBLES: FrozenSet[TipoDteEnum] = frozenset({
    TipoDteEnum.FACTURA_ELECTRONICA,
    TipoDteEnum.FACTURA_NO_AFECTA_O_EXENTA_ELECTRONICA,
    TipoDteEnum.FACTURA_COMPRA_ELECTRONICA,
    TipoDteEnum.LIQUIDACION_FACTURA_ELECTRONICA,
})


###############################################################################
# Cesion Fields / "Monto Cedido"
###############################################################################

# Ref:
#   - https://github.com/fyntex/lib-cl-sii-api-python/blob/v0.4.4/cl_sii_api/rtc/data_models.py#L231
#   - Formato Archivo Electrónico de Cesión (AEC) 2013-02-11 (retrieved on 2019-08-12) - SII Chile
CESION_MONTO_CEDIDO_FIELD_MIN_VALUE: int = 0
CESION_MONTO_CEDIDO_FIELD_MAX_VALUE: int = DTE_MONTO_TOTAL_FIELD_MAX_VALUE


###############################################################################
# Cesion Fields / "Secuencia"
###############################################################################

# Ref:
#   - Formato Archivo Electrónico de Cesión (AEC) 2013-02-11 (retrieved on 2019-08-12) - SII Chile
CESION_SEQUENCE_NUMBER_MIN_VALUE: int = 1
CESION_SEQUENCE_NUMBER_MAX_VALUE: int = 40


###############################################################################
# Other
###############################################################################

@enum.unique
class RolContribuyenteEnCesion(enum.Enum):

    """
    "Rol" of "contribuyente" in a "cesion".
    """

    CEDENTE = 'CEDENTE'
    """Cesiones en las que el contribuyente ha sido cedente i.e. ha cedido"""

    CESIONARIO = 'CESIONARIO'
    """Cesiones en las que el contribuyente ha sido cesionario i.e. le han cedido"""

    DEUDOR = 'DEUDOR'
    """Cesiones de DTEs en que el contribuyente es el deudor."""
