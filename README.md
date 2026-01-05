# Eczema and Scabies Classifier

A deep learning-based classification system for automated diagnosis of eczema and scabies from skin lesion images.

## Overview

This system analyzes skin lesion images and classifies them as either eczema or scabies using a fine-tuned EfficientNet model. The model was trained on a comprehensive dataset curated from multiple medical sources to ensure robust performance.

## Features

- **Binary Classification**: Accurately classifies skin conditions as eczema or scabies
- **Fine-tuned EfficientNet**: Leverages transfer learning for high accuracy
- **Multi-source Dataset**: Trained on diverse data from three reputable medical sources
- **Full-stack Application**: Backend API with FastAPI and frontend interface with Streamlit

## Model

This system uses a **fine-tuned EfficientNet** classification model trained on a curated dataset from three different sources:

- **DermNet Europe**
- **DermaCon/IN**
- **Passion MICCAI Africa**

The combination of these datasets ensures diverse representation and robust model performance across different populations and imaging conditions.

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd EczemaAndScabiesClassifier
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The application consists of a FastAPI backend and a Streamlit frontend that need to be run simultaneously.

### Step 1: Start the Backend Server

Open a terminal and navigate to the backend directory:

```bash
cd backend
uvicorn main:app --reload
```

The API server will start on `http://localhost:8000`

### Step 2: Start the Frontend Interface

Open a **new terminal** and navigate to the frontend directory:

```bash
cd frontend
streamlit run streamlit.py
```

The Streamlit interface will open in your default web browser.

## How It Works

1. Upload a skin lesion image through the Streamlit interface
2. The image is sent to the FastAPI backend for processing
3. The fine-tuned EfficientNet model analyzes the image
4. Classification result (eczema or scabies) is returned and displayed

## Dataset Sources

The model was trained on a curated dataset combining images from:

- **DermNet Europe**: Comprehensive dermatology image database
- **DermaCon/IN**: Indian dermatology consultation platform
- **Passion MICCAI Africa**: African skin disease dataset from MICCAI challenge

## Limitations

- **Single Condition Classification**: The model classifies the entire image as one condition. If an image contains both eczema and scabies, it will classify the whole image as one or the other, not both.
- **Limited to Two Classes**: Images containing other skin conditions not in the training dataset (only eczema and scabies) will be misclassified as one of these two conditions.
- **No Localization**: The current system does not identify or segment the affected areas within the image.

## Future Work

- **Segmentation Module**: Implementing segmentation to localize affected areas and handle images with multiple conditions
- **Multi-class Classification**: Extending to additional skin conditions beyond eczema and scabies
- **Dataset Expansion**: Continuously increasing dataset size and diversity for improved performance

## Requirements

See `requirements.txt` for a complete list of dependencies.

## Contact

*(Add your contact information here)*
