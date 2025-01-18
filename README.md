# Serverless Student Entry Using AWS Amplify

This project demonstrates the use of **AWS Amplify** to build a serverless web application for student entry management. The application integrates with **GitHub**, **Lambda**, **DynamoDB**, and **API Gateway** to provide a seamless experience for deployment, data storage, and security features.
![Screenshot_1](https://github.com/user-attachments/assets/3653b162-63d8-4e78-966a-211d84ac6d43)


## Overview

The application is built using **AWS Amplify** to deploy the frontend and backend resources automatically, whenever code is pushed to GitHub. It includes:
- **Lambda Functions** for server-side processing (GET/POST data from DynamoDB).
- **DynamoDB** for persistent storage.
- **API Gateway** to expose the Lambda functions as HTTP endpoints.
- **Amplify Hosting** for frontend hosting and progressive deployment notifications.
- **Amplify Authentication** for secure access control.

---

## Setup and Configuration

### 1. **Amplify Project Integration with GitHub**

The Amplify project has been successfully integrated with GitHub to automate deployments. Every time you push code to the repository, Amplify automatically handles the build and deployment process.

#### Screenshots:
- Amplify project created and integrated with GitHub:
  ![Amplify Integration](https://github.com/user-attachments/assets/ed56c03e-eca3-4b5b-ab2b-aa88c796ffe6)

- Amplify Build notification feature enabled:
  ![Build Notification](https://github.com/user-attachments/assets/bbe05adf-bbdf-492c-81f1-c84937116688)

- Build notification email confirmation:
  ![Build Notification Email](https://github.com/user-attachments/assets/d3f81c00-97aa-443f-91a8-2aed1df24ca7)

---

### 2. **Lambda Function Creation**

A **Python Lambda function** is created to handle the business logic for the application. This function handles both `GET` and `POST` requests to/from **DynamoDB**.

#### Screenshot:
- Lambda function for GET/POST data:
  ![Lambda Function](https://github.com/user-attachments/assets/d116bfa9-bc3b-431f-a17e-c01f3dc9dd1b)

---

### 3. **Lambda Permissions for DynamoDB Access**

We ensure that the Lambda function has the necessary permissions to interact with **DynamoDB** by attaching the appropriate role.

#### Screenshot:
- Lambda role with DynamoDB access:
  ![Lambda Role](https://github.com/user-attachments/assets/1d232526-52e9-46df-857f-f0fab8ae908c)

---

### 4. **DynamoDB Table Creation**

The **DynamoDB table** is created to store student data. It is designed to handle both `GET` and `POST` requests efficiently.

#### Screenshot:
- DynamoDB table creation:
  ![DynamoDB Table](https://github.com/user-attachments/assets/05e7602b-e369-4557-af6e-9bc6f1093cc3)

---

### 5. **API Gateway Integration**

The **API Gateway** is configured to expose the Lambda function endpoints. This allows the frontend to interact with the backend securely.

#### Screenshot:
- API Gateway and Lambda integration:
  ![API Gateway](https://github.com/user-attachments/assets/a1a9d7af-cb7d-46bf-9caa-898cbb23eab1)

---

## Testing

### 1. **Automatic Deployments via GitHub Integration**

Whenever code is pushed to the GitHub repository, Amplify automatically deploys it and sends an email notification to confirm the deployment.

#### Screenshots:
- Successful code deployment:
  ![Amplify Deployment](https://github.com/user-attachments/assets/e2b8f03c-ace6-4d70-a3d6-b6d6bbc53fd8)

- Build notification confirmation:
  ![Build Notification](https://github.com/user-attachments/assets/a6954021-0c9d-4c4d-9a93-54ca2deceb44)

---

### 2. **Security Features and Authentication**

For added security, Amplify Authentication is enabled. The website prompts users to enter credentials before accessing the application, ensuring controlled access to the app.

#### Screenshots:
- Secure authentication prompt:
  ![Authentication Prompt](https://github.com/user-attachments/assets/1a032487-0ce2-4745-b42e-5cae30484bf7)

- Login page:
  ![Login Page](https://github.com/user-attachments/assets/ad2288b5-e030-4bf7-aacf-58242a2db42c)

---

### 3. **Viewing Student Records**

The application allows users to view the stored student records in DynamoDB. Data can be managed via the API endpoints exposed through API Gateway.

#### Screenshot:
- Viewing student records:
  ![Student Records](https://github.com/user-attachments/assets/89fa33ba-0df5-4238-8266-a23b33782463)

