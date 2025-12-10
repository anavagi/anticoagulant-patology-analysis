
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score,make_scorer
from sklearn.model_selection import learning_curve
from matplotlib import pyplot as plt
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import validation_curve

def evaluate_model(y_true, y_pred, model_name):
    """Calcula y muestra R2, RMSE, MAE para un modelo."""
    r2 = r2_score(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    
    print(f"--- Evaluación: {model_name} ---")
    print(f"R² (Coeficiente de Determinación): {r2:.4f}")
    print(f"RMSE (Error Cuadrático Medio): {rmse:.4f}")
    print(f"MAE (Error Absoluto Medio): {mae:.4f}")
    return {"R2": r2, "RMSE": rmse, "MAE": mae}


def bestHiperparamethers_randomizedSearchCV(param_grid_rf,estimator,X_train, y_train):
    # Configurar RandomizedSearchCV
    search = RandomizedSearchCV(
        estimator=estimator,
        param_distributions=param_grid_rf,
        n_iter=10, # Número de combinaciones a probar (ajustable)
        scoring='neg_root_mean_squared_error', # Optimizar para minimizar RMSE
        cv=5,
        random_state=23,
        n_jobs=-1
    )

    print(f"Iniciando ajuste de {estimator}...")
    search.fit(X_train, y_train)
    best = search.best_estimator_
    print(f"Mejores parámetros RF: {search.best_params_}")
    return best

def plot_learning_curve(estimator, X, y, scoring='neg_mean_squared_error', cv=5):
    """Genera y grafica las curvas de aprendizaje."""
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, scoring=scoring, 
        train_sizes=np.linspace(0.1, 1.0, 10), n_jobs=-1
    )
    
    # Cálculo de la media y la desviación estándar de los scores
    train_scores_mean = np.mean(-train_scores, axis=1)
    test_scores_mean = np.mean(-test_scores, axis=1)
    
    # 📉 Visualización
    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, train_scores_mean, 'o-', color="blue", 
             label="Error en Entrenamiento")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="red", 
             label="Error en Validación Cruzada")
    
    plt.xlabel("Tamaño del Conjunto de Entrenamiento")
    plt.ylabel("Error Cuadrático Medio (RMSE)")
    plt.title("Curvas de Aprendizaje (Bias-Varianza)")
    plt.legend(loc="best")
    plt.grid()
    plt.show()




def plot_validation_curve(estimator,X, y,param_name,param_range):

    # 3. Generar la Curva de Validación
    train_scores, test_scores = validation_curve(
        estimator=estimator, 
        X=X, # Usamos el set completo de entrenamiento/validación (70%)
        y=y,
        param_name=param_name, # Nombre del parámetro que vamos a variar
        param_range=param_range,
        cv=5, # Validación cruzada (5 folds)
        scoring=make_scorer(mean_squared_error, greater_is_better=False),
        n_jobs=-1
    )

    # 4. Cálculo de la media y la visualización
    train_scores_mean = np.mean(-train_scores, axis=1) # El error en entrenamiento
    test_scores_mean = np.mean(-test_scores, axis=1)   # El error en validación

    plt.figure(figsize=(10, 6))
    plt.plot(param_range, train_scores_mean, label="Error en Entrenamiento", color="blue", marker='o')
    plt.plot(param_range, test_scores_mean, label="Error en Validación", color="red", marker='o')

    plt.title(f"Curva de Validación {param_name}")
    plt.xlabel(f"Valor de {param_name}")
    plt.ylabel("Error Cuadrático Medio (RMSE)")
    plt.legend(loc="best")
    plt.grid()
    plt.show()


def plot_validation_curve_boosting(estimator,X, y,param_name,param_range):

    # 3. Generar la Curva de Validación
    train_scores, test_scores = validation_curve(
        estimator=estimator, 
        X=X, # Usamos el set completo de entrenamiento/validación (70%)
        y=y,
        param_name=param_name, # Nombre del parámetro que vamos a variar
        param_range=param_range,
        cv=5, # Añadir validación cruzada para robustez
        scoring="neg_mean_squared_error", # Usar una métrica de error
        n_jobs=-1
    )

    # 4. Cálculo de la media y la visualización
    train_scores_mean = np.sqrt(np.mean(-train_scores, axis=1)) # RMSE en Entrenamiento
    test_scores_mean = np.sqrt(np.mean(-test_scores, axis=1))   # RMSE en Validación
    
    plt.figure(figsize=(10, 6))
    plt.plot(param_range, train_scores_mean, label="Error en Entrenamiento (RMSE)", color="blue", marker='o')
    plt.plot(param_range, test_scores_mean, label="Error en Validación (RMSE)", color="red", marker='o')

    plt.title(f"Curva de Validación para {param_name}")
    plt.xlabel(f"Valor de {param_name}")
    plt.ylabel("Error Cuadrático Medio (RMSE)")
    
    # Añadir un punto vertical para el valor óptimo (si lo conoces)
    # plt.axvline(x=10, color='gray', linestyle='--', label='Max Depth Óptima (10)')
    
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()