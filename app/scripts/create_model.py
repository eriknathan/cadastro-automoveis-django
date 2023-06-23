import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import joblib

# Carregar os dados do arquivo CSV
data = pd.read_csv('/home/eriknathan/Estudos/faculdade/trabalho-ia-vinhos/app/scripts/winequality-red.csv')

# Dividir os dados em recursos (features) e rótulos (labels)
X = data.drop('quality', axis=1)  # Features
y = data['quality']  # Rótulo de qualidade

# Melhores hiperparâmetros encontrados
best_params = {}

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# Definir os hiperparâmetros a serem ajustados
params = {'n_estimators': 85,
            'max_depth': 40,
            'min_samples_split': 4
            }

# Criar o modelo RandomForestClassifier
model = RandomForestClassifier(random_state=67, **params)

# Treinar o modelo
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Calcular a acurácia
current_accuracy = accuracy_score(y_test, y_pred)

joblib.dump(model, 'random_forest.h5')

print("Treinamento concluído!")
print(f"Acurácia alcançada: {current_accuracy * 100}%")
