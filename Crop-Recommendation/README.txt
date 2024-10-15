# Crop-Recommendation

Dataset is taken from Kaggle. Link : https://www.kaggle.com/atharvaingle/crop-recommendation-dataset

## Variable Details:
Dataset consists of 8 variables where 7 variables are considered for predicting output variable. The details of Variable is given Below
1. N (Nitrogen) : Nitrogen content in the soil. Nitrogen is really important for plant growth (structure), plant food processing (metabolism), and the creation of chlorophyll. Without enough nitrogen in the plant, the plant cannot grow taller, or produce enough food (usually yellow).
2. P (Phosphorus) : Phosphorus content  in the soil. Phosphorus primary role in a plant is to store and transfer energy produced by photosynthesis for use in growth and reproductive processes. Soil P cycles in a variety forms in the soil 
3. K (Potassium) : Potassium content in the soil. Potassium is an essential nutrient for plant growth.
4. Temperature : Temperature in degree censius. High temperatures affect plant growth in numerous ways. The most obvious are the effects of heat on photosynthesis, in which plants use carbon dioxide to produce oxygen, and respiration, an opposite process in which plants use oxygen to produce carbon dioxide.
5. Humidity : Relative humidity in %. When conditions are too humid, it may promote the growth of mold and bacteria that cause plants to die and crops to fail, as well as conditions like root or crown rot. Humid conditions also invite the presence of pests, such as fungus gnats, whose larva feed on plant roots and thrive in moist soil.
6. PH : ph value of the soil. Plant nutrients leach from the soil much faster at pH values below 5.5 than from soils within the 5.5 to 7.0 range. In some mineral soils aluminum can be dissolved at pH levels below 5.0 becoming toxic to plant growth. Soil pH may also affect the availability of plant nutrients.
7. Rain fall : Rainfall in mm. Plants use the moisture in the soil to replenish the water lost through transpiration. If there is no water in the soil, the leaves will wilt. As more water is lost, the plant will fail and eventually die. Rainwater builds up the moisture levels in the soil and assures a healthy plant.
Finally,
8. Label : This is the output variable which contains 22 unique values i.e., 22 different crops and they are ['Apple','Banana','blackgram','chickpea','coconut','coffee','cotton','grapes','jute','kidney beans','lentil','maize','mango','moth beans','mung bean','muskmelon','orange','papaya','pigeonpeas','pomegranate','Rice','Watermelon']\
Exploratory data analysis carried out to fetch insights from the data.

## Algorithm :
Only three algorithms are used to predict the output. They are *Logistic Regression*, *XGBoost* and *Random Forest*.\
1. Accuracy of the model using Logistic Regression is 95%.
2. Accuracy of the model using Random Forest Classifier is 99%.
3. Accuracy of the model using XGBoost Classifier is 99%.\
*Random Forest Classifier* is used for development of model.


