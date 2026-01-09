# core_forecast/views.py
from django.shortcuts import render
import plotly.graph_objects as go
from plotly.offline import plot
import numpy as np
# Create your views here.
def dashboard_estatico(request):
    # --- SIMULACIÓN DE DATOS (Esto vendrá de tu modelo Bi-LSTM luego) ---
    # Pasado: 60 minutos (t-60 a t0)
    time_pasado = np.arange(-60, 1)
    s4_pasado = np.random.uniform(0.1, 0.4, size=61)
    
    # Futuro (Pronóstico): 10 minutos (t1 a t10)
    time_futuro = np.arange(1, 11)
    s4_futuro = np.random.uniform(0.4, 0.8, size=10) # Simulamos un incremento de centelleo

    # --- CREACIÓN DEL GRÁFICO CON PLOTLY ---
    fig = go.Figure()

    # Línea de datos pasados
    fig.add_trace(go.Scatter(
        x=time_pasado, y=s4_pasado,
        mode='lines+markers',
        name='Pasado (Lookback 60 min)',
        line=dict(color='#4682b4', width=2)
    ))

    # Línea de pronóstico
    fig.add_trace(go.Scatter(
        x=time_futuro, y=s4_futuro,
        mode='lines+markers',
        name='Pronóstico (Horizonte 10 min)',
        line=dict(color='#dc143c', width=3, dash='dash'),
        marker=dict(size=8)
    ))

    # Configuración de diseño (Layout)
    fig.update_layout(
        title='Monitor de Centelleo Ionosférico - DeepS4Cast',
        xaxis_title='Tiempo (minutos respecto al presente)',
        yaxis_title='Índice S4',
        template='plotly_white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=60, b=20)
    )

    # Convertir el gráfico a un div de HTML
    plot_div = plot(fig, output_type='div', include_plotlyjs=True)

    return render(request, 'core_forecast/dashboard.html', {'plot_div': plot_div})