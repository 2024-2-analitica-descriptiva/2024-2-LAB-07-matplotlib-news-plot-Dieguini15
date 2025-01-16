"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
def pregunta_01():
    plt.figure()
    df=pd.read_csv("news.csv",index_col=0)
    for col in df.columns:
        plt.plot(df[col],label=col)
    plt.show()
pregunta_01()
"""
Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
generar el archivo `files/plots/news.png`.

Un ejemplo de la grafica final esta ubicado en la raíz de
este repo.

El gráfico debe salvarse al archivo `files/plots/news.png`.

"""
