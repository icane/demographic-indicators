"""Módulo etl.

Este módulo contiene la superclase Etl, que implementa operaciones
ETL comunes, como la lectura de ficheros fuente, procesamiento de dataframes
y carga en bases de datos.
"""

# import logging

from abc import ABC

from etlstat.extractor import extractor


class Etl(ABC):
    """Superclase de la que hereda del siguiente módulo.

    -residential.

    Implementa un flujo ETL general en tres pasos:

        - Extracción, implementado en el constructor.
        - Remapeo de columnas en el método remap().
        - Asignación de valores nulos en el método _fillna().
        - Transformación, implementado en el método _transform().
        - Carga en BD, implementado en el método _load().
        - Actualización de metadatos en el método _metadata().

    El método público start() ejecuta el proceso completo.

    .. automethod:: __init__
    """

    def __init__(self, config, config_meta=None):
        """Devuelve un objeto Etl listo para procesar datos.

        El objeto es inicializado con objetos Baseconfig, que contienen
        un diccionario de variables de configuración, como cedenciales de
        base de datos, rutas de ficheros, codificaciones, etc.

        Argumentos:
            config (Baseconfig): almacena los parámetros de configuración
                                 en una estructura jerárquica. Proporciona
                                 acceso a los parámetros como claves de
                                 diccionario o como atributos del objeto.
            config_meta: almacena los parámetros de configuración para
                         realizar la actualizacion de los metadatos.

        Ejemplo:
        from ipietl.etl_micro import EtlMicro

        class xxx(EtlMicro):
            super().__init__(config)

            # sobrecargar con código específico de la subclase

        """
        frame = extractor.xls(
            dir_path=self.cfg.path.input,
            data_extension=self.cfg.data_extension)
        self.df = frame[self.cfg.excel_name][self.cfg.df_name]

        frame = extractor.xls(
            dir_path=self.cfg.path.input,
            data_extension=self.cfg.data_extension)
        self.data = frame[self.cfg.excel_data][self.cfg.sheet_data]

    def _load(self):
        """Actualiza los metadatos del cubo."""

    def _metadata(self):
        """Actualiza los metadatos del cubo."""

    def start(self):
        """Proceso ETL completo."""
