from keras.models import load_model
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense


loaded_model = load_model('ANN_MODEL_CO2.h5')

data = pd.read_csv('MY2023 Fuel Consumption Ratings.csv')

label_encoders = []
for column in ['Make', 'Model', 'Vehicle class',  'Transmission', 'Fuel type']:
    label_encoder = LabelEncoder()
    data[column] = label_encoder.fit_transform(data[column])
    label_encoders.append(label_encoder)

X = data.drop('CO2 rating', axis=1)
y = data['CO2 rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def custom_accuracy(y_true, y_pred, threshold):
    correct = np.sum(np.abs(y_true - y_pred) <= threshold)
    total = len(y_true)
    return correct / total

def predict_input(n1, n2, n3, n4,n5, n6, n7,n8, n9, n10,n11,n12,n13, n14):
    input_data = []
    data_input = [n1,n2,	n3, n4,n5   ,n6, n7,n8,n9,n10,n11,n12,n13,n14]
    for i in range(14):
        if i in [1,2,3,6,7]:  # String columns
            j=i
            if(j==6):j=4
            if(j==7):j=5
            label_encoder = label_encoders[j-1]
            value = data_input[i]
            input_data.append(label_encoder.transform([value])[0])
        else:  # Float columns
            value = float(data_input[i])
            input_data.append(value)
    input_data = pd.DataFrame([input_data], columns=X.columns)
    prediction = loaded_model.predict(input_data)
    if prediction >4.5 : prediction+=random.randint(0, 4)
    scaled_prediction = np.clip(prediction, 0, 10)
    print("Predicted output:", scaled_prediction[0][0])
    return scaled_prediction[0][0]

# Make predictions based on manual input
predict_input(2014, 'Volvo', 'XC90 AWD', 'Sport utility vehicle: Standard',3.2   ,6, 'AS6','X',13.3,8.6,11.2,25,258,6)
