import sqlite3

import joblib
import numpy as np


def using_model():
    # Carregar o modelo treinado a partir do arquivo h5
    loaded_model = joblib.load('random_forest.h5')

    # Exemplo de valores das características para fazer a predição
    conn = sqlite3.connect('db.sqlite3')  # substitua pelo caminho correto para o seu banco de dados
    cursor = conn.cursor()

    # Executando uma consulta para obter os valores dos campos
    consulta = "SELECT acidez_fixa, acidez_volátil, acido_cítrico, acucar_residual, cloretos, dióxido_de_enxofre_livre, dióxido_de_enxofre_total, densidade, pH, sulfatos, álcool " \
               "FROM app_vinhos ORDER BY id DESC LIMIT 1"  # substitua "registro" pelo nome da sua tabela e "id" pelo critério de seleção adequado
    cursor.execute(consulta)

    resultado = cursor.fetchone()

    # Fechando a conexão com o banco de dados
    conn.close()

    acidez_fixa = resultado[0]
    acidez_volatil = resultado[1]
    acido_citrico = resultado[2]
    acucar_residual = resultado[3]
    cloretos = resultado[4]
    enxofre_livre = resultado[5]
    enxofre_total = resultado[6]
    densidade = resultado[7]
    ph = resultado[8]
    sulfatos = resultado[9]
    alcool = resultado[10]

    exemplo_caracteristicas = np.array([[acidez_fixa, acidez_volatil, acido_citrico, acucar_residual, cloretos, enxofre_livre, enxofre_total, densidade, ph, sulfatos, alcool]])
    # exemplo_caracteristicas = np.array([[7.3,0.65,0,1.2,0.065,15,21,0.9946,3.39,0.47,10]])

    # Fazer a predição utilizando o modelo carregado
    predicao = loaded_model.predict(exemplo_caracteristicas)

    # Exibir a predição
    print(f"Predição: {predicao[0]}")

    return predicao[0]

using_model()
