# ML_Pipeline_Project
This project focuses on developing a machine-learning pipeline to streamline data processing, model training, and evaluation. The pipeline is designed to handle various stages of a typical machine-learning workflow, ensuring modularity and scalability.

---

<p align="center"> <img src="https://miro.medium.com/v2/resize:fit:750/format:webp/1*wtvPen4_SIS6HfmxCs2amw.gif" width="600"></p>

---

# Features
  1. Data Ingestion: Loading and preprocessing data from various sources.
  2. Feature Engineering: Applying transformations to enhance model performance.
  3. Model Training: Train machine learning models using the processed data.
  4. Model Evaluation: Assessing model performance using appropriate metrics.

---

# Installation
  1. Clone the repository:
       - bash:
          -> **git clone <Url from GitHub repository>**
 
 2. Navigate to the project directory:
       - bash:
          -> **cd ML_Pipeline_Project**

 3. Set up a virtual environment:
       - bash:
          -> **python -m venv envo source envo/bin/activate**
       - On Windows:
          -> **.\envo\Scripts\activate**

---

# Project Structure

     ML_Pipeline_Project/
        ├── .vscode/
        ├── artifacts/
        |    └── data_ingestion
        |    └── data_transformation
        |    └── model_trainer
        ├── envo/
        ├── logs/
        ├── notebook/
        |    └── data/
        |        └── income_cleandata.csv
        ├── src/
        |    └── __pycache__
        |    └── components
        |    └── pipeline
        |    └── __init__.py
        |    └── exception.py
        |    └── logger.py
        |    └── utils.py
        ├── templates/
        |    └── home.html
        |    └── results.html
        ├── .gitignore
        ├── ML_Pipeline_project.ipynb
        ├── README.md
        ├── app.py
        ├── requirements.txt
        └── setup.py
        
 1. .vscode/: Configuration files for Visual Studio Code.
 2. artifacts/: Directory to store intermediate and final outputs.
 3. envo/: Virtual environment directory.
 4. logs/: Logs generated during pipeline execution.
 5. notebook/: Jupyter notebooks for experimentation.
 6. src/: Source code for the pipeline components.
 7. templates/: Template files for configuration or documentation.
 8. .gitignore: Specifies files and directories to be ignored by Git.
 9. ML_Pipeline_project.ipynb: Main Jupyter notebook for the project.
 10. README.md: This README file.
 11. app.py: Main application script to run the pipeline.
 12. requirements.txt: List of Python dependencies.
 13. setup.py: Setup script for packaging.
