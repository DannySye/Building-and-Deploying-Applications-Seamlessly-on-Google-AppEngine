# Building and Deploying Applications Seamlessly with Google App Engine

This repository contains the source code and configuration files for the presentation, **"Building and Deploying Applications Seamlessly with Google App Engine."** It serves as a practical, hands-on guide for deploying a Python web application to the cloud.

---

## 👨‍🏫 Presented By

**Name:** Daniel Mwiine

**Contact:** syemwayne1122@gmail.com

**Co-Presenter:** Batamye Umar

**Contact:** ubatamyeonline@gmail.com

**Presentation Slides**: https://bit.ly/AppEngine2025

---

## 📘 About This Project

This repository is designed to be a **true project resource** — it’s more than just code. It includes:

- **Clear Documentation:** Step-by-step instructions to ensure you can run the demos yourself.  
- **Two Deployment Strategies:** Code for both the Standard and Flexible environments, allowing direct comparison.  
- **Best Practices:** Includes a `.gitignore` file and a structured layout like a real-world project.

---

## 🎯 The Application: A Number Guessing Game

To make the demonstration engaging, the application is a simple and interactive **number guessing game** built with Python and Flask.  
The game:

- Generates a random number between **1 and 100**.
- Prompts the user to guess the number.
- Provides feedback ("Too high" or "Too low").
- Congratulates the user upon a correct guess and shows the number of attempts.

This simple application is perfect for demonstrating core deployment concepts without complex code.

---

## 🗂️ Project Folder Structure

```bash
app-engine-demo/
│
├── standard-environment-demo/
│   ├── main.py
│   ├── app.yaml
│   ├── requirements.txt
├── flexible-environment-demo/
│   ├── main.py
│   ├── app.yaml
│   ├── Dockerfile
│   ├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Deployment Guide

### **Part 1: Initial Cloud Setup (Do this once)**
Before deploying, configure your Google Cloud environment.

1. **Create a Project:** Go to the Google Cloud Console and create a new project.  
2. **Enable Billing:** Ensure billing is enabled for your project (App Engine free tier is generous but requires billing).  
3. **Enable APIs:** In the Cloud Console, enable the **App Engine Admin API** and **Cloud Build API**.  
4. **Install Google Cloud CLI:** Install the CLI on your local machine.  
5. **Initialize the CLI:**
   ```bash
   gcloud init
   ```
   Follow prompts to log in, select your project, and choose a default region for App Engine.

---

### **Part 2: Demo 1 - Deploying to the Standard Environment**
The **Standard Environment** is ideal for rapid development and scaling to zero.

1. Navigate to the correct directory:
   ```bash
   cd standard-environment-demo
   ```
2. Deploy the application:
   ```bash
   gcloud app deploy
   ```
3. Confirm and wait for deployment.
4. View your live app:
   ```bash
   gcloud app browse
   ```

---

### **Part 3: Demo 2 - Deploying to the Flexible Environment**
The **Flexible Environment** uses Docker containers for full control over the runtime.

1. Navigate to the flexible environment directory:
   ```bash
   cd ../flexible-environment-demo
   ```
2. Deploy the application:
   ```bash
   gcloud app deploy
   ```
3. Confirm and wait — this will take longer as Docker images are built.
4. View your live app:
   ```bash
   gcloud app browse
   ```

You’ve now successfully deployed the same application to two different App Engine environments!

---

## 🤝 Contributing

Contributions are welcome! Feel free to open a pull request with improvements or suggestions for the code or documentation.

---

## 📄 License

This project is licensed under the **MIT License**.

