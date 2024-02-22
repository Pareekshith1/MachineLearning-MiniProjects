def feed_the_model(colors, textures, weights, taste, seeds):
    import pandas as pd
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.compose import ColumnTransformer

    dataset = pd.read_excel('Fruit_dataset.xlsx')

    dataset['Seed/Seed_less'] = dataset['Seed/Seed_less'].replace({'yes': 1, 'no': 0})

    X = dataset.drop(columns=['Fruit_name'])
    y = dataset['Fruit_name']

    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0, 1, 3])], remainder='passthrough')
    X_encoded = ct.fit_transform(X)

    le_seed = LabelEncoder()
    y_encoded = le_seed.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_encoded, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    input_data = [[colors, textures, weights, taste, seeds]]
    input_df = pd.DataFrame(input_data, columns=X.columns)
    input_df['Seed/Seed_less'] = input_df['Seed/Seed_less'].replace({'yes': 1, 'no': 0})

    input_encoded = ct.transform(input_df)

    prediction = model.predict(input_encoded)
    predicted_fruit = le_seed.inverse_transform(prediction)

    return predicted_fruit[0]
