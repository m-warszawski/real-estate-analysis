import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

def train_linear_model(data):
    X = data[['powierzchnia', 'liczba_pokoi', 'lokalizacja']]
    y = data['cena']
    X = pd.get_dummies(X, columns=['lokalizacja'], drop_first=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f'MSE: {mse}')
    return model

def train_random_forest_model(data):
    X = data[['powierzchnia', 'liczba_pokoi', 'lokalizacja']]
    y = data['cena']
    X = pd.get_dummies(X, columns=['lokalizacja'], drop_first=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f'Random Forest Regressor MSE: {mse}')
    return model

def train_property_classifier(data):
    le = LabelEncoder()
    data['typ'] = le.fit_transform(data['typ'])
    X = data[['powierzchnia', 'liczba_pokoi', 'lokalizacja']]
    y = data['typ']
    X = pd.get_dummies(X, columns=['lokalizacja'], drop_first=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    classifier = RandomForestClassifier()
    classifier.fit(X_train, y_train)
    accuracy = classifier.score(X_test, y_test)
    print(f'Accuracy: {accuracy}')
    return classifier

def perform_association_rule_analysis(data):
    from mlxtend.frequent_patterns import apriori, association_rules
    data_bin = pd.get_dummies(data[['powierzchnia', 'liczba_pokoi', 'lokalizacja', 'typ']], drop_first=True)
    data_bin['powierzchnia'] = data['powierzchnia'].apply(lambda x: 1 if x > data['powierzchnia'].median() else 0)
    data_bin['liczba_pokoi'] = data['liczba_pokoi'].apply(lambda x: 1 if x > data['liczba_pokoi'].median() else 0)
    frequent_itemsets = apriori(data_bin, min_support=0.1, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
    return rules
