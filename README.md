# 🏢 Final Project Module 3 – Employee Satisfaction and Retention Analysis

**Final project for Module 3 of the Adalab Data Analytics Bootcamp**  
*Technologies used: Python · Pandas · MySQL · Seaborn · Matplotlib · ETL · A/B Testing*

This project was developed by **Ana Hernández**, **Ariana Papantonio**, **Mirella Vissetti**, and **Irene Alonso**.  
It focuses on reducing employee turnover and improving job satisfaction within a fictional company, ABC Corporation.

---

## 🎯 Project Goal

The aim of this project is to analyze internal employee data to identify key factors that influence job satisfaction and retention.  
We applied data cleaning, exploratory analysis, relational database design, and A/B testing to generate actionable insights.  
The outcome helps support strategic decisions for boosting engagement and reducing churn.

---

## 🧠 Project Phases

The work was structured into six main phases:

1. **Exploratory Data Analysis (EDA)**  
   Initial examination of numerical and categorical variables.

2. **Data Transformation**  
   Cleaning and restructuring the datasets.

3. **Database Design & Insertion**  
   Structuring data into relational models and loading into **MySQL**.

4. **A/B Testing Design**  
   Formulating and running controlled experiments to test critical hypotheses.

5. **ETL Pipeline Development**  
   Automating data movement from source files into the SQL database using custom Python scripts.

6. **Results Reporting**  
   Presenting conclusions and strategic recommendations based on the analysis.

---

## 📁 Project Structure

```
├── Data/
│   ├── hr_raw_data_final.csv
│   ├── info_personal.csv
│   ├── info_salario_1.csv
│   ├── info_satisfaccion_1.csv
│   ├── info_trabajo.csv
│   ├── categoricos.csv
│   ├── numericos.csv
│   ├── unidos_limpio_1.csv
│   └── cleaned datasets (various)
│
├── Fase_1_EDA/
│   ├── EDA_categorico.ipynb
│   ├── EDA_numerico.ipynb
│   └── EDA_general.ipynb
│
├── Fase_2_transformacion/
│   ├── 1_division_dataframes.ipynb
│   ├── 2_limpieza_categoricos.ipynb
│   ├── 3_limpieza_numericos.ipynb
│   └── 5_data_junta.ipynb
│
├── Fase_3_diseño_bbdd_insercion/
│   ├── 1_creacion_tablas.ipynb
│   ├── 2_BBDD.sql
│   ├── 3_insercion_datos.ipynb
│   └── Exportacion-importacion/
│       ├── estudio_satisfaccion_info_personal.sql
│       ├── estudio_satisfaccion_info_salario.sql
│       └── estudio_satisfaccion_info_trabajo.sql
│
├── Fase_4_AB_testing/
│   └── AB_testing.ipynb
│
├── Fase_5_ETL/
│   ├── main.py
│   └── src/
│       ├── __init__.py
│       ├── soporte_bbdd.py
│       ├── soporte_funciones.py
│       └── soporte_queries.py
│
├── Fase_6_reporte_resultados/
│   └── Powerpoint.pptx
│
├── Documentacion.ipynb
├── proyecto-3.md
└── README.md
```

---

## 📊 Tools & Technologies

- **Python**: data cleaning, analysis, and scripting  
- **MySQL**: relational database storage and queries  
- **Pandas**, **NumPy**, **SciPy**: data manipulation and statistical testing  
- **Matplotlib**, **Seaborn**: visualizations  
- **Jupyter Notebook**: development and presentation  
- **A/B Testing**: statistical experiment design  
- **ETL Pipeline**: automated data loading via Python scripts

---

# ✅ Thanks for exploring our project!
