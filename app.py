#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
import joblib
from datetime import date


# In[2]:


model = joblib.load('model.pkl')
model


# In[3]:


app = Flask(__name__)


# In[4]:


year = date.today().year
year


# In[5]:


@app.route("/")
def home():
    return render_template('home.html',current_year=year)


# In[6]:


@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "POST":
        ph = request.form['ph'] #Range: (0.00,14.00)
        hardness = request.form['hardness'] #Range: (117.12,276.39)
        solids = request.form['solids'] #Range: (320.94,44831.86)
        chloramines = request.form['chloramines'] #Range: (3.14,11.09)
        sulfate = request.form['sulfate'] #Range: (267.15,400.32)
        conductivity = request.form['conductivity'] #Range: (191.64,655.87)
        organic_carbon = request.form['organic_carbon'] #Range: (5.32,23.29)
        trihalomethanes = request.form['trihalomethanes'] #Range: (26.61,106.69)
        turbidity = request.form['turbidity'] #Range: (1.84,6.09)
        
        predictions = model.predict([[
            ph,
            hardness,
            solids,
            chloramines,
            sulfate,
            conductivity,
            organic_carbon,
            trihalomethanes,
            turbidity
        ]])
        
        output = int(predictions[0])
        
        if output == 1:
            return render_template('home.html',current_year=year,prediction_text="The water with given details is pure and potable enough to drink and meets the federal standards for domestic consumption.")
        else:
            return render_template('home.html',current_year=year,prediction_text="The water with specified details is impure, contaminated and non-potable. It may not be suitable for domestic consumption.")


# In[ ]:


if __name__ == "__main__":
    app.run(port=8080)

