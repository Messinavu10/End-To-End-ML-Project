from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import os 
import numpy as np
import pandas as pd
from src.datascience.pipeline.prediction import PredictionPipeline
import threading
import time

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

# Global variable to track training status
training_status = {"is_training": False, "status": "Not started", "message": ""}

@app.route('/',methods=['GET'])
def homePage():
    return render_template("index.html", training_status=training_status)

@app.route('/train',methods=['GET', 'POST'])
def training():
    global training_status
    
    if request.method == 'POST':
        if training_status["is_training"]:
            return jsonify({"status": "error", "message": "Training already in progress"})
        
        # Start training in a separate thread
        training_status = {"is_training": True, "status": "Training started", "message": "Initializing..."}
        
        def train_model():
            global training_status
            try:
                training_status["message"] = "Running data ingestion..."
                time.sleep(1)
                
                training_status["message"] = "Running data validation..."
                time.sleep(1)
                
                training_status["message"] = "Running data transformation..."
                time.sleep(1)
                
                training_status["message"] = "Training model..."
                time.sleep(2)
                
                # Run the actual training
                os.system("python main.py")
                
                training_status = {"is_training": False, "status": "Completed", "message": "Training completed successfully!"}
            except Exception as e:
                training_status = {"is_training": False, "status": "Failed", "message": f"Training failed: {str(e)}"}
        
        thread = threading.Thread(target=train_model)
        thread.start()
        
        return jsonify({"status": "success", "message": "Training started"})
    
    return render_template("training.html", training_status=training_status)

@app.route('/training-status')
def training_status_route():
    return jsonify(training_status)

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        try:
            # Check if model exists
            model_path = "artifacts/model_trainer/model.joblib"
            if not os.path.exists(model_path):
                flash("Model not found. Please train the model first.", "error")
                return redirect(url_for('homePage'))
            
            #user inputs
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])
       
            data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, 
                   free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)
            
            # Determine wine quality category
            quality_score = float(predict[0])
            if quality_score >= 7:
                quality_category = "Excellent"
                quality_color = "success"
            elif quality_score >= 6:
                quality_category = "Good"
                quality_color = "info"
            elif quality_score >= 5:
                quality_category = "Average"
                quality_color = "warning"
            else:
                quality_category = "Poor"
                quality_color = "danger"

            return render_template('results.html', 
                                prediction=quality_score, 
                                quality_category=quality_category,
                                quality_color=quality_color,
                                input_data=data[0])

        except ValueError:
            flash("Please enter valid numeric values for all fields.", "error")
            return redirect(url_for('homePage'))
        except Exception as e:
            flash(f"Prediction failed: {str(e)}", "error")
            return redirect(url_for('homePage'))

    else:
        return redirect(url_for('homePage'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
