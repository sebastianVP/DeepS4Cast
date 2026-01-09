# 🛰️ DeepS4Cast: Ionospheric Scintillation Forecasting System

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)

**DeepS4Cast** es una plataforma web desarrollada en Lima, Perú, diseñada para el pronóstico del centelleo ionosférico (índice $S_4$) mediante modelos de Deep Learning. Este sistema permite monitorear y predecir irregularidades atmosféricas que afectan la precisión de las señales GNSS en la región ecuatorial.



## 🌟 Características Principales
- **Arquitectura Bi-LSTM:** Utiliza redes neuronales recurrentes bidireccionales para capturar patrones temporales complejos.
- **Predicción Multi-paso:** Capacidad de pronosticar una ventana de tiempo futura (horizonte de predicción).
- **Interfaz Web Moderna:** Panel de control desarrollado en Django con visualización interactiva de datos.
- **Optimizado para Región Ecuatorial:** Ajustado con datos recolectados en el Hub de baja latitud de Perú.

## 🏗️ Arquitectura del Sistema
El proyecto integra una arquitectura robusta que separa la lógica de negocio web del motor de inferencia de IA:

1. **Frontend:** HTML5, CSS3, JavaScript (Plotly.js para gráficos dinámicos).
2. **Backend:** Django (Framework principal).
3. **ML Engine:** Inferencia optimizada con TensorFlow/Keras y pre-procesamiento con Scikit-learn.



## 🚀 Instalación y Uso

### Requisitos Previos
- Python 3.9 o superior
- Entorno virtual (venv o conda)

### Pasos
1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/DeepS4Cast.git](https://github.com/tu-usuario/DeepS4Cast.git)
   cd DeepS4Cast/DeepS4Cast
   ```
2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar migraciones:**
   ```bash
   python manage.py migrate     
   ```
3. **Iniciar el servidor::**
   ```bash
   python manage.py runserver     
   ```

Visita http://127.0.0.1:8000/ en tu navegador.
---

## 📊 Marco Metodológico: Variables de Investigación

El sistema **DeepS4Cast** basa su capacidad predictiva en un enfoque multivariable, integrando datos de diversas fuentes físicas para capturar la complejidad de la ionósfera ecuatorial.

### 🎯 Variable Dependiente
* **Índice de centelleo ionosférico ($S_4$):** Parámetro que cuantifica las fluctuaciones de amplitud en las señales GNSS debido a las irregularidades ionosféricas.

### ⚙️ Variables Independientes (Predictores)

| Categoría | Variables Incluidas | Impacto en el Modelo |
| :--- | :--- | :--- |
| **Parámetros Solares** | $F_{10.7}$, Viento solar (velocidad/densidad), IMF | Estado de la fuente de ionización. |
| **Parámetros Geomagnéticos** | $K_p$, $AE$, $D_{st}$ | Respuesta de la magnetósfera terrestre. |
| **Parámetros Ionosféricos** | $TEC$, $ROTI$, Gradientes espaciales | Caracterización de la densidad electrónica. |
| **Parámetros GNSS** | $C/N_0$ (Intensidad), Elevación, Geometría | Calidad y trayectoria de la señal. |
| **Variables Temporales** | Hora local, Estacionalidad, Ciclo Solar | Patrones cíclicos y de recurrencia. |



---