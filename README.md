# Salary Predictor

This is a simple machine learning project that predicts salary based on years of experience.

I made this project to get some hands-on practice with Scikit-learn and Streamlit and understand the complete workflow of an ML project, from training a model to deploying it as a web app.

## Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## How it works

- The dataset is loaded using Pandas.
- A Linear Regression model is trained using Scikit-learn.
- The trained model is saved using pickle.
- Streamlit is used to create a small web interface where users can enter their years of experience and get a predicted salary.

## Running the project

Clone the repository:

```bash
git clone https://github.com/soroshimukherjee/salary-predictor.git
```

Move into the project folder:

```bash
cd salary-predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

## Future improvements

- Use more features instead of only years of experience.
- Try other regression models.
- Improve the UI.

This project was built mainly for learning purposes and to understand the basics of machine learning deployment.