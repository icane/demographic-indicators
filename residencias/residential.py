"""Modulo residential.py. Hereda de etl."""

import logging

from residencias.etl import Etl


class Residential(Etl):
    """Proceso de banco de datos mensual del IPI."""

    def __init__(self, config, config_meta):
        """Devuelve una instancia de la clase IndDestEcon con datos cargados.

        Args:
            config (Baseconfig): parámetros de configuración.
            config_meta (Baseconfig): parámetros de configuración
                                      para actualizar los metadatos.
        """
        self.logger = logging.getLogger(__name__)

        self.config_dict = {}

        self.json_vars = []

        # Estructura de cada configuración individual.
        self.single_dict = self.cfg.single_dict

        super().__init__(config, config_meta)

    def transform_vars(self):
        """Normaliza el excel de datos."""
        self.var_list = []

        variables = self.data.iloc[:, 15:]

        var_labels = variables.keys()

        loop_length = int(len(var_labels)/2)

        for value in range(0, loop_length):
            self.var_list.append(
                var_labels[value] +
                '|' +
                var_labels[loop_length+value]
                )

    def listLabels(self):
        """Divide la columna en category y label.

        Si la suma de nulos es total - 1 es una category
        Si no es una label y guarda ambas en una lista
        separadas por el símbolo |.
        """
        self.categories = []
        self.labels = []

        val_cat = None

        # Obtengo la cantidad de nulos por cada fila
        dicNull = self.df.isnull().sum(axis=1).tolist()
        # Cantidad de columnas del dataframe
        df_length = len(self.df.columns) - 1

        # Borra las primeras dos filas que son cabeceras
        self.df = self.df.iloc[2:]

        for row, col in self.df.iterrows():
            if dicNull[row] == df_length:
                self.categories.append(col[self.cfg.config_col_name])
                val_cat = col[self.cfg.config_col_name]
            else:
                # Añadimos la category + la label juntas
                # Ejemplo:
                # Índice de Cobertura (nº de plazas/población>=65)*100.|Total
                self.labels.append(val_cat+'|'+col[self.cfg.config_col_name])

    def name_json(self):
        """Modifica el nombre de variable y añade .json-stat para exportar."""

        lista = []

        for val in self.var_list:
            val1, val2 = val.split('|', 2)
            val1 = val1.rpartition('_Cantabria')[0]
            val1 = val1.casefold()
            for regla in self.cfg.reglas:
                val1 = val1.replace(regla, self.cfg.reglas[regla])

            lista.append(val1)

        for val in lista:
            for regla in self.cfg.reglasEspecificas:
                val = val.replace(regla, self.cfg.reglasEspecificas[regla])
            self.json_vars.append(val)

    def create_config(self):
        """Divide la variable val y actualiza la configuración.

        Recorre todas las keys del diccionario de configuracion
        básico y va actualizando los valores y tras terminar
        inserta el diccionario actualizado en una key del
        diccionario de configuracion final.
        """
        # Puede ser una lista, es para dar nombre a cada configuración.
        x = 0
        for val in range(0, len(self.labels)):
            category, label = self.labels[val].split('|', 2)
            var_can, var_esp = self.var_list[val].split('|', 2)

            for keys in self.single_dict.keys():
                if keys == 'category':
                    self.single_dict['category'] = category
                if keys == 'label':
                    self.single_dict['label'] = label
                if keys == 'rate_vars':
                    self.single_dict['rate_vars'] = [var_can, var_esp]
                if keys == 'json':
                    self.single_dict['json'] = self.json_vars[x]

            self.config_dict[x] = self.single_dict.copy()
            x += 1

    def _load(self):
        super()._load()

    def start(self):
        """Proceso ETL completo."""
        self.listLabels()
        self.transform_vars()
        self.name_json()
        self.create_config()
        super().start()
