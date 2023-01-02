# --- OPTIMIZED GRADIENT BOOSTING ALGORITHM --- 

# Importing libraries
import os
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import mode
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, cross_val_score

# Arrays of result and similar diseases
gerd = {"similarDiseases": ["Bacterial Pneumonia", "Influenza", "Peptic Ulcer"], 
"treatment": "Treatment for heartburn and GERD usually begins with over-the-counter antacids and medications to help reduce stomach acid. You also may want to avoid the foods and drinks that make your symptoms worse. If these treatments don't relieve symptoms, you may need prescription medications, surgery, or other procedures.",
"description": "GERD/Heartburn happens when stomach acid backs up into your esophagus, irritating the lining of the esophagus. To diagnose heartburn or GERD, the doctor will take a medical history and do a physical exam. You may also need to have X-rays, an endoscopy, or other tests."} 

pepticUlcer = {"similarDiseases": ["Gastroenteritis", "Gastritis", "Heartburn/GERD"], 
"treatment": "Antibiotics, Acid-suppressing medicationds, antacids, good diet, and avoiding caffeine, alcohol and tobbaco are among the necessary treatments for Peptic Ulcer.",
"description": "Peptic ulcers are sores or holes in the lining of the stomach or upper intestine (duodenum). Most commonly, H. pylori bacteria and stomach acids have eaten through the stomach lining. A medical history and physical exam can help diagnose an ulcer. The doctor may do a blood or breath test for H. pylori bacteria, a series of X-rays of the stomach called an upper GI, or an endoscopy."}

gastroenteritis = {"similarDiseases": ["Food Poisoning", "Gastritis", "Influenza"], 
"treatment": "Treatment for gastroenteritis may include: Drinking clear fluids, Anti-nausea and anti-diarrhea medications, Taking acetaminophen (Tylenol) as needed to ease muscle aches and lower fever, and IV fluids if severely dehydrated.",
"description": "Gastroenteritis is inflammation of the stomach and intestines caused by viruses. Doctor can diagnose gastroenteritis by taking the medical history and doing a physical exam. The doctor may also do stool tests."}

bronchialAsthma = {"similarDiseases": ["Bacterial Pneumonia", "Influenza", "Bronchitis"], 
"treatment": "Treatment for asthma includes an asthma action plan that has in writing when to take certain medications based on the symptoms. Quick-relief or rescue medications include short-acting bronchodilators and oral corticosteroids.",
"description": "Asthma is a lung condition that causes airways to swell and become inflamed. Asthma makes it hard to breathe. Doctor can diagnose asthma by taking your medical history and doing a physical exam. Other tests include lung function tests, allergy testing, and X-rays."}

migraine = {"similarDiseases": ["Meningitis", "Motion Sickness", "Vitamin B12 Deficiency"],
"treatment": "Some migraines can be treated at home with over-the-counter pain relievers. Severe sudden or chronic migraines are usually treated with prescription medicines. Pain-relieving, over-the-counter medications usually work best when taken at the first sign of a migraine.",
"description": "Migraines are a common type of headache that can cause severe pain. To diagnose migraine, your doctor will take a medical history and do a physical exam. You may also need a CT scan, MRI, or other tests to rule out other problems."}

typhoidFever = {"similarDiseases": ["Influenza", "Viral Gastroenteritis", "Irritable Bowel Syndrome"], 
"treatment": "Typhoid fever is treated with antibiotics which kill the Salmonella bacteria. With appropriate antibiotic therapy, there is usually improvement within one to two days and recovery within seven to 10 days.",
"description": "Typhoid fever is an acute illness associated with fever caused by the Salmonella enterica serotype Typhi bacteria. If a test result isn't clear, blood or urine samples will be taken to make a diagnosis."}

commonCold = {"similarDiseases": ["Coronavirus", "Influenza", "Bacterial Pneumonia"],
"treatment": "Colds usually get better on their own in a few days. Antihistamines, decongestants, pain relievers, drinking plenty of fluids, and breathing in steam may help ease symptoms.",
"description": "The common cold is a short-lived viral infection of the upper respiratory tract, which includes the nose and sinuses, mouth, and throat. The doctor can diagnose a cold by taking your medical history and doing a physical exam. He or she may want to do a throat culture or blood tests to rule out infections."}

pneumonia = {"similarDiseases": ["Coronavirus", "Influenza", "Bronchial Asthma"], 
"treatment": "The doctor may prescribe antibiotics. It’s very important that a patient finish all of these. Otherwise the bacteria may not all be killed and the patient could get sick all over again. The doctor might also suggest medication for pain and fever.",
"description": "Bacterial pneumonia is an infection of your lungs caused by certain bacteria, while Viral pneumonia is a lung infection caused by viruses. The doctor can diagnose pneumonia by taking your medical history and doing a physical exam. Other tests may include blood tests, chest X-ray, and sputum testing."}

UTI = {"similarDiseases": ["Kidney Infection", "Pelvic Inflammatory Disease", "Cervicitis"],
"treatment": "Antibiotics, drinking lots of water, and Phenazopyridine, a medication used to dull the pain in the urethra.",
"description": "Urinary tract infections are common, especially among women. UTIs occur when bacteria in the digestive tract and around the anus get into the urethra, the tube that carries urine from the bladder. The doctor will do a physical exam and order a urine test to diagnose a UTI. The doctor may order further tests for a severe UTI or kidney infection."}

hypertension = {"similarDiseases": ["Migraine", "Acute Sinusitis", "Generalized Anxiety Disorder"],
"treatment": "To prevent high blood pressure, everyone should be encouraged to make lifestyle modifications, such as eating a healthier diet, quitting smoking, and getting more exercise. Moreover, the most important element in the management of high blood pressure is follow-up care as recommended by the doctor.",
"description": "High blood pressure is usually diagnosed using the familiar blood pressure test that involves a cuff wrapped around the upper arm. The cuff is inflated and then sensors measure the pressure of blood beating against the arteries. High blood pressure used to be diagnosed at a measurement of 140/90 millimeters of mercury (mm Hg) or higher. Now these authorities state that if your blood pressure is 130/80 mm Hg or higher, you have hypertension. A normal blood pressure measurement is the same as it was before: less than 120/80 mm Hg."}

# Remove warnings from terminal
import warnings
warnings.filterwarnings('ignore')

BASE_DIR = Path(__file__).resolve().parent.parent

# Reading the train data by removing the last column since it's an empty column
DATA_PATH = os.path.join(BASE_DIR, 'dataset/Train.csv')
data = pd.read_csv(DATA_PATH).dropna(axis = 1)

# Checking whether the dataset is balanced or not
disease_counts = data["prognosis"].value_counts()
temp_df = pd.DataFrame({
    "Disease": disease_counts.index,
    "Counts": disease_counts.values
})

# Encoding the target value into numerical value using LabelEncoder
encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])

# Splitting the data set into train and test 
X = data.iloc[:,:-1]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test =train_test_split(
X, y, test_size = 0.2, random_state = 24)

# --- K-FOLD CROSS VALIDATION ---
def cv_scoring(estimator, X, y):
    return accuracy_score(y, estimator.predict(X))

# Initializing Models
models = {
    "Logistic Regression":LogisticRegression(),
    "Random Forest":RandomForestClassifier(random_state=18),
    "Gradient Boost":GradientBoostingClassifier(learning_rate=0.1,max_depth=9,n_estimators=383,subsample=0.59)
}
 
# Producing cross validation score for the combined model
for model_name in models:
    model = models[model_name]
    scores = cross_val_score(model, X, y, cv = 10,
                             n_jobs = -1,
                             scoring = cv_scoring)

# --- TRAINING AND VALIDATING THE DATA ---
lr_model = LogisticRegression()
rf_model = RandomForestClassifier(random_state=18)
gb_model = GradientBoostingClassifier(learning_rate=0.1,max_depth=9,n_estimators=383,subsample=0.59)

lr_model.fit(X_train, y_train)
rf_model.fit(X_train, y_train)
gb_model.fit(X_train, y_train)

preds = lr_model.predict(X_test)
preds = rf_model.predict(X_test)
preds = gb_model.predict(X_test)

# --- TESTING THE DATA ---
final_lr_model = LogisticRegression()
final_rf_model = RandomForestClassifier(random_state=18)
final_gb_model = GradientBoostingClassifier(learning_rate=0.1,max_depth=9,n_estimators=383,subsample=0.59)

final_lr_model.fit(X, y)
final_rf_model.fit(X, y)
final_gb_model.fit(X, y)
 
# Reading the test data
datafile = os.path.join(BASE_DIR, 'dataset/Test.csv')
test_data = pd.read_csv(datafile).dropna(axis=1)
test_X = test_data.iloc[:, :-1]
test_Y = encoder.transform(test_data.iloc[:, -1])

# Making prediction by take mode of predictions
lr_model = final_lr_model.predict(test_X)
rf_model = final_rf_model.predict(test_X)
gb_model = final_gb_model.predict(test_X)
 
final_preds = [mode([i,j,k])[0][0] for i,j,
               k in zip(lr_model, rf_model, gb_model)]

# --- DISEASE PREDICTION FEATURE ---
symptoms = X.columns.values

# Creating a symptom index dictionary to encode the input symptoms into numerical form
symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index

data_dict = {
    "symptom_index":symptom_index,
    "predictions_classes":encoder.classes_
}

# Defining the Function
def predictDisease(symptoms):
    symptoms = symptoms.split(",")
     
    # creating input data for the models
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1
         
    # reshaping the input data and converting it
    input_data = np.array(input_data).reshape(1,-1)
     
    # generating individual outputs
    lr_prediction = data_dict["predictions_classes"][final_lr_model.predict(input_data)[0]]
    rf_prediction = data_dict["predictions_classes"][final_rf_model.predict(input_data)[0]]
    gb_prediction = data_dict["predictions_classes"][final_gb_model.predict(input_data)[0]]
     
    # making final prediction by taking mode of all predictions
    final_prediction = mode([lr_prediction, rf_prediction, gb_prediction])[0][0]
    if (final_prediction == "GERD"):
        predictions = {
        "lr_model_prediction": lr_prediction,
		"rf_prediction": rf_prediction,
		"gb_prediction": gb_prediction,
		"final_prediction":final_prediction,
        "description": gerd["description"],
        "similarDiseases": gerd["similarDiseases"],
        "treatment": gerd["treatment"]
        }
        return predictions, gerd
    elif (final_prediction == "Peptic ulcer disease"):
        predictions = {
        "lr_model_prediction": lr_prediction,
		"rf_prediction": rf_prediction,
		"gb_prediction": gb_prediction,
		"final_prediction":final_prediction,
        "description": pepticUlcer["description"],
        "similarDiseases": pepticUlcer["similarDiseases"],
        "treatment": pepticUlcer["treatment"]
        }
        return predictions, pepticUlcer 
    elif (final_prediction == "Gastroenteritis"):
        predictions = {
        "lr_model_prediction": lr_prediction,
		"rf_prediction": rf_prediction,
		"gb_prediction": gb_prediction,
		"final_prediction":final_prediction,
        "description": gastroenteritis["description"],
        "similarDiseases": gastroenteritis["similarDiseases"],
        "treatment": gastroenteritis["treatment"]
        }
        return predictions, gastroenteritis
    elif (final_prediction == "Bronchial Asthma"):
        predictions = {
        "lr_model_prediction": lr_prediction,
		"rf_prediction": rf_prediction,
		"gb_prediction": gb_prediction,
		"final_prediction":final_prediction,
        "description": bronchialAsthma["description"],
        "similarDiseases": bronchialAsthma["similarDiseases"],
        "treatment": bronchialAsthma["treatment"]
        }
        return predictions, bronchialAsthma
    elif (final_prediction == "Migraine"):
        predictions = {
        "lr_model_prediction": lr_prediction,
		"rf_prediction": rf_prediction,
		"gb_prediction": gb_prediction,
		"final_prediction":final_prediction,
        "description": migraine["description"],
        "similarDiseases": migraine["similarDiseases"],
        "treatment": migraine["treatment"]
        }
        return predictions, migraine
    elif (predictions == "Typhoid"):
        predictions = {
        "lr_model_prediction": lr_prediction,
		"rf_prediction": rf_prediction,
		"gb_prediction": gb_prediction,
		"final_prediction":final_prediction,
        "description": typhoidFever["description"],
        "similarDiseases": typhoidFever["similarDiseases"],
        "treatment": typhoidFever["treatment"]
        }
        return predictions, typhoidFever
    elif (predictions == "Common Cold"):
        predictions = {
        "lr_model_prediction": lr_prediction,
		"rf_prediction": rf_prediction,
		"gb_prediction": gb_prediction,
		"final_prediction":final_prediction,
        "description": commonCold["description"],
        "similarDiseases": commonCold["similarDiseases"],
        "treatment": commonCold["treatment"]
        }
        return predictions, commonCold
    elif (predictions == "Pneumonia"):
        predictions = {
        "lr_model_prediction": lr_prediction,
		"rf_prediction": rf_prediction,
		"gb_prediction": gb_prediction,
		"final_prediction":final_prediction,
        "description": pneumonia["description"],
        "similarDiseases": pneumonia["similarDiseases"],
        "treatment": pneumonia["treatment"]
        }
        return predictions, pneumonia
    elif (predictions == "Urinary tract infection"):
        predictions = {
        "lr_model_prediction": lr_prediction,
		"rf_prediction": rf_prediction,
		"gb_prediction": gb_prediction,
		"final_prediction":final_prediction,
        "description": UTI["description"],
        "similarDiseases": UTI["similarDiseases"],
        "treatment": UTI["treatment"]
        }
        return predictions, UTI
    elif (predictions == "Hypertension"):
        predictions = {
            "lr_model_prediction": lr_prediction,
            "rf_prediction": rf_prediction,
		    "gb_prediction": gb_prediction,
		    "final_prediction":final_prediction,
        "description": hypertension["description"],
        "similarDiseases": hypertension["similarDiseases"],
        "treatment": hypertension["treatment"]
        }
        return predictions, hypertension
    else:
        predictions = {
        "lr_model_prediction": lr_prediction,
		"rf_prediction": rf_prediction,
		"gb_prediction": gb_prediction,
		"final_prediction":final_prediction
        }
        return predictions
    