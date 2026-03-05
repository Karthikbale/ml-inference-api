**Prerequires**
Python

DockerDesktop

VScode

**🚀 PROJECT: Containerized ML Inference API**
✅ STEP 0 — Create Project Folder
1️⃣ Open Command Prompt
2️⃣ Go to Desktop
cd Desktop
3️⃣ Create Project Folder
mkdir ml-inference-api
cd ml-inference-api

dir


✅ STEP 1 — Create Virtual Environment (Very Important)

This keeps dependencies clean.

python -m venv venv

Activate it:

venv\Scripts\activate

You should now see:

(venv) C:\Users\...\ml-inference-api>

If you see (venv) → good.

✅ STEP 2 — Install Required Libraries

We need:

fastapi

uvicorn

scikit-learn

joblib

pandas

Run:

Wait  until installation completes.

✅ STEP 3 — Create Training Script

Inside this folder, create a file named:

train.py

Open folder in VS Code:

code .

If code doesn’t work, open VS Code manually and open this folder.

✍️ Inside train.py — Paste This
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained and saved as model.pkl")

Save the file.

✅ STEP 4 — Run Training Script

In terminal (inside project folder, venv active):

python train.py

You should see:

Model trained and saved as model.pkl

Now run:

dir

You must see:

model.pkl
pip install fastapi uvicorn scikit-learn joblib pandas

Wait until installation completes.
