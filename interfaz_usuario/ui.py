import pandas as pd
from tabulate import tabulate

def convertir_a_tabla(data):
    df = pd.DataFrame(data)
    tabla = tabulate(df, headers='keys', tablefmt='fancy_grid')
    return tabla