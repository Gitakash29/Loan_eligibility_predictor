from flask import Flask, render_template, request
import pickle



app = Flask(__name__)

file=open('lrm.pkl','rb')
model = pickle.load(file)

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        
        
       
        
        ApplicantIncome = float(request.form['ApplicantIncome'])
        
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        
        LoanAmount = float(request.form['LoanAmount'])
        
        Dependents = float(request.form['Dependents'])
        
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
        
        Credit_History = float(request.form['Credit_History'])
        
        
        
        Gender = request.form['Gender']
        if (Gender == 'Male'):
            Gender=1
            
        else :
            Gender = 0
            
            
            
        Married = request.form['Married']
        if (Married == 'Married'):
            Married=1
            
        else :
            Married = 0
            
            
            
        Self_Employed = request.form['Self_Employed']
        if (Self_Employed == 'Yes'):
            Self_Employed = 1
            
        else :
            Self_Employed = 0
            
            
            
        Education = request.form['Education']
        if (Education == 'Yes'):
             Education = 1
            
        else :
            Education = 0
            
            
            
        Property_Area = request.form['Property_Area']                
        if (Property_Area == 'Urban'):
            Property_Area=1
            
            
        elif (Property_Area == 'Semiurban'):
           Property_Area=2
            
        else:
           Property_Area=0
            
        prediction=model.predict([[ApplicantIncome, CoapplicantIncome, LoanAmount, Dependents, Loan_Amount_Term, Credit_History,Gender, Married, Self_Employed, Education, Property_Area]])
        
        output = prediction

        print(output)

        if output == 0:
            return render_template('index.html',prediction_text="The applicant is Not Eligible for Loan")
        elif output == 1:
            return render_template('index.html',prediction_text="The applicant is Eligible for Loan")
    else:
        return render_template('index.html')
            
        

if __name__=="__main__":
    app.run(debug=False,port=8000)