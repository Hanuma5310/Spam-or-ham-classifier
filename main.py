from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
pipe = pickle.load(open("C:/Users/hanum/OneDrive/Desktop/Projects/Spam-or-ham-classifier-main/Naive_model.pkl", "rb"))

@app.route('/', methods=["GET", "POST"])
def main_function():
    if request.method == "POST":
        text = request.form
        emails = text['email']
        print("Received Email Text:", emails)
        
        list_email = [emails]
        output = pipe.predict(list_email)[0]  # Get model prediction
        print("Model Output:", output)
        
        # Convert numeric output to meaningful labels
        label = "Spam" if output == 1 else "Ham"
        
        return render_template("show.html", prediction=label)
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
