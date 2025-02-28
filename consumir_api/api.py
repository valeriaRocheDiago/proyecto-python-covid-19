import pandas as pd
from sodapy import Socrata

def obtener_datos(departamento, limite):
    client = Socrata("www.datos.gov.co", None)
    results = client.get("gt2j-8ykr",
                         departamento_nom=departamento.upper(),
                         limit=limite,
                         select= "ciudad_municipio_nom , departamento_nom , edad , fuente_tipo_contagio , estado , pais_viajo_1_nom")
    results_df = pd.DataFrame.from_records(results)
    column_mapping = {'ciudad_municipio_nom': 'Ciudad de ubicacion',
                      'departamento_nom': 'Departamento',
                      'edad': 'Edad',
                      'fuente_tipo_contagio': 'Tipo',
                      'estado': 'Estado',
                      'pais_viajo_1_nom': 'País de procedencia'}
    results_df.rename(columns=column_mapping, inplace=True)
    return results_df