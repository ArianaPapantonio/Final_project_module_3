
## Consultoria Datos Corporativos
El propósito de este proyecto es la lectura, limpieza, análisis de los datos y la experimentación A/B de gran alcance de la empresa ABC Corporation para potenciar a los empleados. Con el objetivo de reducir la rotación de empleados y mejorar la satisfacción en el trabajo la empresa.

Nuestra misión es identificar factores clave que influyen en la satisfacción en el trabajo y, en última instancia, en la retención de empleados.

En resumen, en este proyecto, presentaremos los resultados de nuestro análisis exploratorio de datos, diseñaremos un experimento A/B para probar hipótesis críticas y analizaremos los resultados para proporcionar a ABC Corporation información valiosa que informe sus decisiones estratégicas.

# Mi Proyecto

## Índice

1. [Descripción](#Descripción)
2. [Archivos](#Archivos)
3. [Metodología](#Metodología)
4. [Autor](#Autor)

## Descripción
El objetivo es reducir la rotación de empleados y mejorar la satisfacción en el trabajo la empresa. Esto se ha podido hacer con las distintas fases:

Fase 1: Análisis Exploratorio de Datos(EDA)

Fase 2: Transformación de los datos

Fase 3: Diseño de BBDD e Insercción de los Datos

Fase 4: Problema de Pruebas A/B

Fase 5: Creación de un ETL

Fase 6: Informe de los resultados

## Archivos

    1. Carpeta Data:

    - categoricos_limpio.csv
    - categoricos.csv
    - data_limpia_1.csv
    - hr_raw_data_final.csv
    - info_personal.csv
    - info_salario_1.csv
    - info_saisfaction_1.csv
    - info_trabajo.csv
    - numericos_limpio_1.csv
    - numericos:csv
    - unidos_limpio_1.csv

    2. Carpeta Fase_1_EDA

    - EDA_categorico.ipynb
    - EDA_general.ipynb
    - EDA_numerico.ipynb

    3. Carpeta Fase_2_transformacion:

    - 1_division_dataframes.ipynb
    - 2_limpieza_categoicos.ipynb
    - 3_limpieza_numericos.ipynb
    - 4_columnas_eliminadas.ipynb
    - 5_data_junta.ipynb

    4. Carpeta Fase_3_diseño_bbdd_insercion
    - Carpeta: Exportacion-importacion
        - estudio_satisfaccion_info_personal.sql
        - estudio_satisfaccion_info_salario.sql
        - estudio_satisfaccion_info_trabajo.sql
        - estudio_satisfaccion_satisfaccion.sql
    - 1_creacion_tablas.ipynb
    - 2_BBDD.sql
    - 3_insercion-datos.ipynb

    5. Carpeta Fase_4_AB_testing

    - AB_testing.ipynb

    6. Carpeta Fase_5_ETL

    - Carpeta src
        - __init__.py
        - soporte_bbdd.py
        - soporte_funciones.py
        - soporte_queries.py
    - main.py

    7. Carpeta_6_reporte_resultados

    - Powerpoint.pdf

- Documentacion.ipynb
- proyecto-3.md
- README.md


## Metodología
Pasos de limpieza de datos: Fase 1 y 2

Técnicas de visualización utilizadas: Gráficos

Herramientas y bibliotecas empleadas: jupyter notebook, pandas, numpy, scipy.stats, warnings, matplotlib, seaborn en Python, mysql.

## Autor

El Análisis de Datos fue realizado por Ana Hernandez, Ariana Papantonio, Mirella Vissetti y Irene Alonso. Somos un equipo de analistas de datos especializados en la exploración y análisis de datos para obtener información útil y acciones significativas.






