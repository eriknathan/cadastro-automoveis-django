import sqlite3


def database():
    # Exemplo de valores das características para fazer a predição
    conn = sqlite3.connect('db.sqlite3')  # substitua pelo caminho correto para o seu banco de dados
    cursor = conn.cursor()

    # Executando uma consulta para obter os valores dos campos
    consulta = "SELECT acidez_fixa, acidez_volátil, acido_cítrico, acucar_residual, cloretos, dióxido_de_enxofre_livre, dióxido_de_enxofre_total, densidade, pH, sulfatos, álcool FROM app_vinhos ORDER BY id DESC LIMIT 1"  # substitua "registro" pelo nome da sua tabela e "id" pelo critério de seleção adequado
    cursor.execute(consulta)

    resultado = cursor.fetchone()

    # Fechando a conexão com o banco de dados
    conn.close()
    
    print(resultado[0])

    return {
        "acidez_fixa": resultado[0],
        "acidez_volatil": resultado[1],
        "acido_citrico": resultado[2],
        "acucar_residual": resultado[3],
        "cloretos": resultado[4],
        "enxofre_livre": resultado[5],
        "enxofre_total": resultado[6],
        "densidade": resultado[7],
        "ph": resultado[8],
        "sulfatos": resultado[9],
        "alcool": resultado[10],
}


database()
