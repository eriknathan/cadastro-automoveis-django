import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


# Carregar os dados do arquivo CSV
data = pd.read_csv('/home/eriknathan/Estudos/Projetos/cadastro-automoveis-django/app/scripts/winequality-red.csv')

# Separar os dados de entrada (X) e os rótulos (y)
X = data.drop('quality', axis=1)
y = data['quality']

# Criar o classificador Random Forest
rf = RandomForestClassifier()
rf.fit(X, y)

# Salvar o modelo treinado em um arquivo h5
joblib.dump(rf, 'random_forest.h5')      
    