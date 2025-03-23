import pandas as pd
from sodapy import Socrata

def limpiar_datos ( data ):
    """
    Funcion para limpiar los datos obtenidos de la API
    """
    # 1. Convertir la columna 'Edad' a tipo numérico
    data [ 'Edad' ] = pd.to_numeric ( data [ 'Edad'], errors = 'coerce') # 'coerce' convierte los valores no numericos en Nan

    # 2. Manejar valores nulos en la columna 'Edad' ( imputar con la mediana )
    mediana_edad = data [ 'Edad']. median ()
    data [ 'Edad']. fillna ( mediana_edad, inplace= True )

    #3. Eliminar filas donde el 'Estado' sea nulo
    data.dropna ( subset= [ 'Estado' ], inplace= True )

    #4. Normalizar la columna 'Tipo' ( convertir a mayúsculas )
    data [ 'Tipo' ]= data [ 'Tipo' ].str.upper ()

    #5. Eliminar duplicados ( si las hay )
    data.drop_duplicates ( inplace= True )

    return data

def obtener_datos ( departamento, limite ):
    client = Socrata ( "www.datos.gov.co", None )
    results = client.get ( "gt2j-8ykr",
                         departamento_nom=departamento.upper(),
                         limit=limite,
                         select= "ciudad_municipio_nom , departamento_nom , edad , fuente_tipo_contagio , estado , pais_viajo_1_nom")
    results_df = pd.DataFrame.from_records ( results )
    column_mapping = {'ciudad_municipio_nom': 'Ciudad de ubicacion',
                      'departamento_nom': 'Departamento',
                      'edad': 'Edad',
                      'fuente_tipo_contagio': 'Tipo',
                      'estado': 'Estado',
                      'pais_viajo_1_nom': 'País de procedencia'}
    results_df.rename ( columns=column_mapping, inplace=True )

    #Limpiar los antes antes de devolverlos 
    results_df =limpiar_datos ( results_df )
    return results_df
