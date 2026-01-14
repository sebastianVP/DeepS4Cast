# core_forecast/views.py
from django.shortcuts import render
import plotly.graph_objects as go
from plotly.offline import plot
import numpy as np

from core_forecast.utils.s4_parser import parse_s4_array


def dashboard_estatico(request):
    # =========================
    # 1. ESTACIÓN SELECCIONADA
    # =========================
    estacion_sel = request.GET.get('estacion', 'Jicamarca')

    estaciones_coords = {
        'Jicamarca': {'top': 63, 'left': 37},
        'Huancayo':  {'top': 63, 'left': 49},
        'Piura':     {'top': 31, 'left': 13},
        'Cuzco':     {'top': 70, 'left': 70},
        'Pucallpa':  {'top': 56, 'left': 62},
        'Ayacucho':  {'top': 76, 'left': 56},
        'Tacna':     {'top': 91, 'left': 83},
        'Iquitos':   {'top': 30, 'left': 50},
    }

    estaciones = [
    "Jicamarca",
    "Huancayo",
    "Piura",
    "Cuzco",
    "Pucallpa",
    "Ayacucho",
    "Tacna",
    "Iquitos"
    ]
    coord = estaciones_coords.get(estacion_sel)

    # =========================
    # VARIABLES DE CONTROL
    # =========================
    s4_pasado = None
    alerta_observada = False
    alerta_pronostico = False
    error_msg = None

    # =========================
    # 2. INPUT DEL USUARIO
    # =========================
    if request.method == "POST":
        try:
            if request.FILES.get("s4_file"):
                file = request.FILES["s4_file"]
                text = file.read().decode("utf-8")
                s4_pasado = parse_s4_array(text)

            elif request.POST.get("s4_text"):
                s4_pasado = parse_s4_array(request.POST["s4_text"])

            if s4_pasado is not None:
                alerta_observada = np.max(s4_pasado) >= 0.6

        except ValueError as e:
            error_msg = str(e)

    # =========================
    # 3. DATOS SIMULADOS
    # =========================
    if s4_pasado is None:
        np.random.seed(hash(estacion_sel) % 100)
        s4_pasado = np.random.uniform(0.05, 0.3, size=60)

    time_pasado = np.arange(-59, 1)
    time_futuro = np.arange(1, 11)

    nivel = 0.5 if estacion_sel == 'Jicamarca' else 0.2
    s4_futuro = np.random.uniform(nivel, nivel + 0.3, size=10)

    alerta_pronostico = np.max(s4_futuro) >= 0.6

    # =========================
    # 4. COLORES SEGÚN ALERTA
    # =========================
    color_pasado = '#dc143c' if alerta_observada else '#4682b4'   # rojo / azul
    color_futuro = '#dc143c' if alerta_pronostico else '#2e8b57' # rojo / verde

    # =========================
    # 5. GRÁFICO PLOTLY
    # =========================
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=time_pasado,
        y=s4_pasado,
        mode='lines+markers',
        name='Datos Observados (60 min)',
        line=dict(color=color_pasado),
        marker=dict(color=color_pasado)
    ))

    fig.add_trace(go.Scatter(
        x=time_futuro,
        y=s4_futuro,
        mode='lines+markers',
        name='Predicción (10 min)',
        line=dict(color=color_futuro, dash='dash'),
        marker=dict(color=color_futuro)
    ))

    fig.update_layout(
        title=f'Análisis de Centelleo Ionosférico – Estación {estacion_sel}',
        xaxis_title='Tiempo (minutos)',
        yaxis_title='Índice S4',
        template='plotly_white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    plot_div = plot(fig, output_type='div', include_plotlyjs=True)

    # =========================
    # 6. CONTEXTO PARA EL TEMPLATE
    # =========================
    context = {
        'plot_div': plot_div,
        'estacion_sel': estacion_sel,
        'coord': coord,
        'estaciones':estaciones,
        # alertas
        'alerta_observada': alerta_observada,
        'alerta_pronostico': alerta_pronostico,

        'error_msg': error_msg
    }

    return render(request, 'core_forecast/dashboard.html', context)
