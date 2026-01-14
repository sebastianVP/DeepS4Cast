import numpy as np

def parse_s4_array(text):
    """
    Espera algo como:
    0.12, 0.15, 0.18, ..., 0.22
    """
    try:
        values = [float(v) for v in text.replace('\n', ',').split(',') if v.strip()]
        if len(values) != 60:
            raise ValueError("El arreglo debe contener exactamente 60 valores.")
        return np.array(values)
    except Exception as e:
        raise ValueError(f"Error al procesar los datos: {e}")