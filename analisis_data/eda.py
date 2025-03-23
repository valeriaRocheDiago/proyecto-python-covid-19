import matplotlib.pyplot as plt
import seaborn as sns

def realizar_eda ( datos ):
    """
    Funcion para realizar el analisis exploratorio de Datos ( EDA )
    """
    print ( "\n=== Analisis Exploratorio de Datos (EDA) ===\n" )

    # 1. Estadisticas descriptivas de la columna 'Edad'
    print ( "\nEstadisticas descriptivas de la columna 'Edad':\n" )
    print ( datos [ 'Edad' ]. describe () )

    # 2. Histograma de la columna 'Edad'
    print ( "\nGenerando histograma de la columna 'Edad'...\n" )
    sns.histplot ( datos [ 'Edad' ], kde=True )
    plt.title ( 'Distribucion de Edades' )
    plt.xlabel ( 'Edad' )
    plt.ylabel ( 'Frecuencia' )
    plt.show ()

    # 3. Gráfico de barras para contar casos por ciudad 
    print ( "\nGenerando gráfico de casos por ciudad..." )
    sns.countplot ( data=datos, x='Ciudad de ubicacion' )
    plt.title ( 'casos por ciudad ' )
    plt.xlabel ( 'Ciudad' )
    plt.ylabel ( 'Número de casos' )
    plt.xticks ( rotation= 90 )
    plt.show ()

    # 4. Gráfico de barras para contar casos por tipo de contagio
    print ( "\nGnerando gráfico de casos por tipo de contagio..." )
    sns.countplot ( data=datos, x= 'Tipo' )
    plt.title ( 'Casos por tipo de contagio' )
    plt.xlabel ( 'Tipo de contagio' )
    plt.ylabel ( 'Número de casos' )
    plt.show ()

    # 5. Gráfico de caja para detectar outliers en 'Edad'
    print ( "\nGenerando gráfico de caja para detectar outliers en 'Edad..." )
    sns.boxplot ( x=datos [ 'Edad' ] )
    plt.title ( 'Boxplot de Edades' )
    plt.xlabel ( 'Edad' )
    plt.show ()