from flask import Flask, request, render_template
#from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np 
# Load the Random Forest CLassifier model
file_name = "model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')
	
@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()    
    if request.method == 'POST':
        Overs = float(request.form['Overs'])
        Runs = int(request.form['Runs'])
        Wickets = int(request.form['Wickets'])
        FiveRuns = float(request.form['5Runs'])
        Fivewkt = float(request.form['5Wkt'])
        
        batting2=request.form['Batting']
        if(batting2=='BT1'):
            temp_array = temp_array + [1,0,0,0,0,0]     
        elif (batting2=='BT2'):
            temp_array = temp_array + [0,1,0,0,0,0] 
        elif (batting2=='BT3'):
            temp_array = temp_array + [0,0,1,0,0,0] 
        elif (batting2=='BT4'):
            temp_array = temp_array + [0,0,0,1,0,0] 
        elif (batting2=='BT5'):
            temp_array = temp_array + [0,0,0,0,1,0] 
        elif (batting2=='BT6'):
            temp_array = temp_array + [0,0,0,0,0,1] 

        bowling2=request.form['Bowling']
        if(bowling2=='BL1'):
            temp_array = temp_array + [1,0,0,0,0,0]     
        elif (bowling2=='BL2'):
            temp_array = temp_array + [0,1,0,0,0,0] 
        elif (bowling2=='BL3'):
            temp_array = temp_array + [0,0,1,0,0,0] 
        elif (bowling2=='BL4'):
            temp_array = temp_array + [0,0,0,1,0,0] 
        elif (bowling2=='BL5'):
            temp_array = temp_array + [0,0,0,0,1,0] 
        elif (bowling2=='BL6'):
            temp_array = temp_array + [0,0,0,0,0,1] 
            
        venue2=request.form['Venue']
        if(venue2=='VU1'):
            temp_array = temp_array + [1,0,0,0,0,0,0]     
        elif (venue2=='VU2'):
            temp_array = temp_array + [0,1,0,0,0,0,0] 
        elif (venue2=='VU3'):
            temp_array = temp_array + [0,0,1,0,0,0,0] 
        elif (venue2=='VU4'):
            temp_array = temp_array + [0,0,0,1,0,0,0] 
        elif (venue2=='VU5'):
            temp_array = temp_array + [0,0,0,0,1,0,0] 
        elif (venue2=='VU6'):
            temp_array = temp_array + [0,0,0,0,0,1,0]
        elif (venue2=='VU7'):
            temp_array = temp_array + [0,0,0,0,0,0,1]  
			
        #temp_array = temp_array + [Minimum_Nights, Availability,Host_Listing, Reviews,Reviews_by_Month ]
        
        temp_array = [Overs, Runs, Wickets, FiveRuns, Fivewkt]+ temp_array 
        
        data = np.array([temp_array])
 
        my_prediction = int((model.predict(data).reshape(1,-1))[0])
        #my_prediction = np.where(my_prediction==1,'likely to Churn.', 'likely to stay with the bank.')
    #    reviews_per_month, calculated_host_listings_count,
    #    availability_365, Bronx, Brooklyn, Manhattan, Queens,
    #    Staten Island, Entire home/apt, Private room, Shared room]])
        return render_template("result2.html", my_prediction=my_prediction ,data = data)#lower_limit = my_prediction-5, upper_limit = my_prediction+5,data=data)
if __name__ == "__main__":
    app.run(debug=True)