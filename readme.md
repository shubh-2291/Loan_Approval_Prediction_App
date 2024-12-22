# Loan Prediction Web Application

## Project Overview

The **Loan Prediction Web Application** is designed to automate the loan eligibility verification process for Dream Housing Finance. Using a machine learning model integrated with a Python Flask web application, this project enables users to register, log in, and check their loan eligibility by providing necessary details.

## Key Features

1. **User Authentication**:
   - Registration: Create an account with a username and password.
   - Login: Secure access to the application.
   - Logout: Safely exit the application.

2. **Loan Eligibility Prediction**:
   - Input customer details such as Gender, Marital Status, Income, Loan Amount, and Credit History.
   - Get real-time loan eligibility status using a pre-trained machine learning model.

3. **Database Integration**:
   - MySQL for user credential management and data storage.

4. **Machine Learning**:
   - Classification model trained and saved using Pickle for seamless integration with Flask.

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Database**: MySQL
- **Machine Learning**: Scikit-learn
- **Tools**: PyCharm/Visual Studio Code, Pickle

## Dataset

The dataset contains the following attributes:

- **Features**: Loan ID, Gender, Marital Status, Dependents, Education, Applicant Income, Co-Applicant Income, Loan Amount, Loan Term, Credit History, Property Area
- **Target**: Loan Status (Approved/Not Approved)

**Source**: [Loan Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/ssiddharth408/loan-prediction-dataset)

## Application Workflow

1. **Homepage**:
   - Users are prompted to register or log in.

2. **Registration**:
   - Enter a username and password.
   - Data is stored securely in a MySQL database.

3. **Login**:
   - Authenticated users are redirected to the prediction form.

4. **Prediction Form**:
   - Users enter required details to check loan eligibility.
   - Prediction results are displayed.

5. **Logout**:
   - Users can log out securely.

## Project Structure

```
Loan_Prediction/
├── app.py                  # Main Flask application file
├── templates/
│   ├── home.html           # Homepage for registration and login
│   ├── register.html       # User registration page
│   ├── login.html          # User login page
│   ├── predict.html        # Form for loan eligibility prediction
├── model.pkl               # Pre-trained ML model
├── Loan_Prediction_Model.ipynb  # Jupyter Notebook for model building
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

## Steps to Run the Application

1. **Clone the Repository**:
   ```bash
   git clone <repository_link>
   cd Loan_Prediction
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   - Configure MySQL with a database named `loan_app_db`.
   - Create a table `User` with fields `user_id`, `full_name`, `email`, and `password`.

5. **Run the Flask Application**:
   ```bash
   python app.py
   ```
   Access the application at `http://127.0.0.1:8080`.

## Model Development

1. **Data Preprocessing**:
   - Handled missing values and redundant features.
   - Encoded categorical variables.

2. **Visualization**:
   - Explored target variable distribution across features.

3. **Model Training**:
   - Classification model trained to predict loan eligibility.
   - Model saved using Pickle for deployment.

## Screenshots

1. **Home Page**: Registration and login options.
2. **Register Page**: Create a new user account.
3. **Login Page**: Authenticate registered users.
4. **Prediction Form**: Input details for loan eligibility check.
5. **Result Page**: Displays loan eligibility status.

## Contribution

Contributions to improve the application are welcome. Please submit a pull request or open an issue for discussions.

## Acknowledgements

- [Kaggle](https://www.kaggle.com/) for the dataset.
- Mentors and reviewers for guidance and support.

---

