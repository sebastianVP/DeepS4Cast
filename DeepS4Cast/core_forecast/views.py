# core_forecast/views.py
from django.shortcuts import render
import plotly.graph_objects as go
from plotly.offline import plot
import numpy as np

def dashboard_estatico(request):
    # 1. Obtener estación (por defecto Jicamarca)
    estacion_sel = request.GET.get('estacion', 'Jicamarca')

    # 2. Diccionario de coordenadas para el punto rojo en el mapa (ajustar según tu imagen)
    estaciones_coords = {
        'Jicamarca': {'top': 56, 'left': 44},
        'Huancayo':  {'top': 60, 'left': 53},
        'Piura':     {'top': 25, 'left': 32},
        'Cuzco':     {'top': 72, 'left': 66},
        'Pucallpa':  {'top': 46, 'left': 62},
        'Ayacucho':  {'top': 66, 'left': 56},
        'Tacna':     {'top': 91, 'left': 85},
        'Iquitos':   {'top': 18, 'left': 70},
    }
    coord = estaciones_coords.get(estacion_sel)

    # 3. Simulación de datos según estación (Usamos seed para que el gráfico cambie algo)
    np.random.seed(hash(estacion_sel) % 100)
    time_pasado = np.arange(-60, 1)
    s4_pasado = np.random.uniform(0.05, 0.3, size=61)
    
    time_futuro = np.arange(1, 11)
    # Si es Jicamarca, simulamos un evento de centelleo más alto para la demo
    nivel = 0.5 if estacion_sel == 'Jicamarca' else 0.2
    s4_futuro = np.random.uniform(nivel, nivel + 0.3, size=10)

    # 4. Crear Gráfico Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time_pasado, y=s4_pasado, mode='lines+markers', name='Datos Reales (t-60)', line=dict(color='#4682b4')))
    fig.add_trace(go.Scatter(x=time_futuro, y=s4_futuro, mode='lines+markers', name='Predicción Bi-LSTM', line=dict(color='#dc143c', dash='dash')))

    fig.update_layout(
        title=f'Análisis de Centelleo Ionosférico: Estación {estacion_sel}',
        xaxis_title='Tiempo (minutos)',
        yaxis_title='Índice S4',
        template='plotly_white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    plot_div = plot(fig, output_type='div', include_plotlyjs=True)

    # 5. Contexto para el HTML
    context = {
        'plot_div': plot_div,
        'estacion_sel': estacion_sel,
        'coord': coord
    }
    return render(request, 'core_forecast/dashboard.html', context)