# Spam-or-Ham Classifier

## 📌 About
This is a **Spam or Ham Classifier** built using **Flask** and **Machine Learning**. It predicts whether an email is spam or not based on its content. The web application is designed with a cyberpunk-inspired UI using HTML, CSS, and Flask.

## 💡 Features
✔️ **Email Classification** – Enter an email text, and the model predicts if it's spam or ham.  
✔️ **Naïve Bayes Model** – Trained using scikit-learn for accurate spam detection.  
✔️ **Flask Web App** – Lightweight and easy-to-use interface.  
✔️ **Deployment Ready** – Hosted live on Vercel for easy access.  

## 📂 Project Structure
```
📁 Spam-or-ham-classifier-main  
│-- 📁 templates/          # HTML templates (index.html, show.html)  
│-- 📁 venv/               # Virtual environment files  
│-- 📄 Email_Spam_with_pipeline.ipynb  # Jupyter Notebook for model training  
│-- 📄 emails.csv          # Dataset used for training/testing  
│-- 📄 main.py             # Flask application script  
│-- 📄 Naive_model.pkl     # Trained Naïve Bayes model  
│-- 📄 requirements.txt    # Dependencies for the project  
│-- 📄 README.md           # Project documentation  
``` 

## ⚙️ Installation & Usage
### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/Spam-or-ham-classifier-main.git
cd Spam-or-ham-classifier-main
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask app
```bash
python main.py
```

### 4️⃣ Open in Browser
Visit `http://127.0.0.1:5000/` in your web browser.  

## 🛠️ Technologies Used
- **Python, Flask** (Backend)  
- **Scikit-learn** (Machine Learning)  
- **HTML, CSS** (Frontend)   

---
This project is open-source and contributions are welcome! 🎉
