**Prerequires**

Python

DockerDesktop

VScode

**🚀 PROJECT: Containerized ML Inference API**
✅ STEP 0 — Create Project Folder
1️⃣ Open Command Prompt

2️⃣ Go to Desktop

**cd Desktop**

3️⃣ Create Project Folder

**mkdir ml-inference-api**

**cd ml-inference-api**

**dir**


✅ STEP 1 — Create Virtual Environment (Very Important)

This keeps dependencies clean.

**python -m venv venv**

Activate it:

**venv\Scripts\activate**

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

**pip install fastapi uvicorn scikit-learn joblib pandas** 

Wait  until installation completes.

✅ STEP 3 — Create Training Script

Inside this folder, create a file named:

**train.py**

Open folder in VS Code:

**code .**

If code doesn’t work, open VS Code manually and open this folder.

**✍️ Inside train.py** — Paste code


✅ STEP 4 — Run Training Script

In terminal (inside project folder, venv active):

  **python train.py**

You should see:

  Model trained and saved as model.pkl

Now run:

  **dir**

You must see:

  model.pkl

✅ STEP 5 — Build FastAPI Inference API

This will turn your ML model into a real backend service.

🧱 What We Are Building

You will create:

/ → Health check

/predict → Send input → Get prediction

Using:

👉 FastAPI

✅ Step 5.1 — Create app.py

Inside:

C:\Users\Admin\Desktop\ml-inference-api

Create a new file:

**app.py**
✍️ Paste This Inside app.py    //paste the code 

✅ Step 5.2 — Run FastAPI Server

Make sure:

You are inside ml-inference-api

Virtual environment is activated (venv)

Now run:

**uvicorn app:app --reload**

You should see something like:

Uvicorn running on http://127.0.0.1:8000

✅ Step 5.3 — Test in Browser

Open browser and go to:

http://127.0.0.1:8000

You should see:

{"message":"ML Inference API is running"}

✅ Step 5.4 — Test Prediction Endpoint

Go to:

http://127.0.0.1:8000/docs

This opens Swagger UI automatically (FastAPI feature).

Click /predict

Click "Try it out"

Enter this:

{

  "sepal_length": 5.1,
  
  "sepal_width": 3.5,
  
  "petal_length": 1.4,
  
  "petal_width": 0.2

}

Click Execute

You should get something like:

{

  "prediction": 0

}

🎉  ML model is now serving predictions via API.

Means:

✅ FastAPI is running
✅ Model loaded correctly
✅ JSON validation working
✅ Inference working
✅ API responding properly

 first ML inference API successfully 🎉

 🚀 Now We Move to DEVOPS MODE

Next step:

✅ STEP 6 — Dockerize the Application

Now we convert this into a container using:

**Docker**

Step 6.1 — Stop Server

In terminal press:

**CTRL + C**

To stop uvicorn.

**Step 6.2 — Create requirements.txt**

Inside  project folder create file:

**requirements.txt**

Paste this inside:

**fastapi
uvicorn
scikit-learn
joblib
numpy
pandas**

Save it.

Step 6.3 — Create Dockerfile

Create a new file named:

**Dockerfile**

paste all the docker code in this file 

Step 6.4 — Build Docker Image

Inside project folder run:

**docker build -t ml-inference-api .**

When build finishes, you should see:

Successfully tagged ml-inference-api:latest

✅ STEP 7 — Run the Container

Inside your project folder run:

**docker run -p 8000:8000 ml-inference-api**

Explanation:

-p 8000:8000 → maps container port to your system

ml-inference-api → image name

After running, you should see something like:

Uvicorn running on http://0.0.0.0:8000

✅ STEP 8 — Test From Browser

Open browser and go to:

http://127.0.0.1:8000

You should see:

{"message":"ML Inference API is running"}

✅ STEP 9 — Test Prediction

Open:

http://127.0.0.1:8000/docs

Test /predict like before.

If prediction works → 🎉
