# YOLOv11-Based Triatoma infestans Detection
## Project Description
This project implements a deep learning model based on YOLOv11 for the detection and classification of _Triatoma infestans_. It includes data segmentation, model training, and evaluation. The goal is to develop a robust and accurate AI solution for identifying this species in real-world scenarios.

## Problem Statement
The manual identification of _Triatoma infestans_ is a time-consuming process prone to errors. Our model provides an automated and precise solution, reducing false positives and improving detection accuracy across different environments.

## How the System Works
- The model is trained using YOLOv11 with images of Triatoma infestans and other species to minimize false positives.
- An inference system allows real-time image analysis for detection.
-The model is evaluated using key metrics such as accuracy, sensitivity, and false positive rate.

## Repository Structure
- project/dataset - Dataset used for model training.
- project/models/experimental_models - Experimental versions of the model.
- project/models/production_model - Optimized final model.
- project/models/production_models/inference_script.py - Script for running inference.
- notebooks/experimental_notebooks - Jupyter Notebooks with experimental model versions.
- notebooks/production_notebook - Final inference notebook.
- requirements.txt - List of required dependencies.
- README.md - This file.
- LICENSE - Project license.

## Installation and Usage

1. Clone the repository:
```bash
git clone https://github.com/your-repo.git
cd your-repo
```

2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Navegate to folder
```bash
cd project/models/production_model/
```

4. Run inference:
```bash
python inference_script.py
```

## Demostration Video 
Watch the demonstration video of our model at the following link: [Demo](demo/demo.mp4)



# Check-In
- Title of your submission: **[YOLOv11-Based Triatoma infestans Detection]**
- Team Members: [Brian A. Cumi-Guzman](mailto:brian.azael02@gmail.com), [Alejandro D. Espinosa-Chim](mailto:danyespinosachim@gmail.com), [Alfonso Barragan-Romero](mailto:alfonso.barragan0304@gmail.com)
- [x] All team members agree to abide by the [Hackathon Rules](https://aaai.org/conference/aaai/aaai-25/hackathon/)
- [x] This AAAI 2025 hackathon entry was created by the team during the period of the hackathon, February 17 – February 24, 2025
- [x] The entry includes a 2-minute maximum length demo video here: [Link](https://your-link.com)
- [x] The entry clearly identifies the selected theme in the README and the video.