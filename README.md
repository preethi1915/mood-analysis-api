# Mood Analysis API

## Overview
The **Mood Analysis API** is a web application built with **FastAPI** to analyze moods expressed in text using **TextBlob**. It can classify moods as `Positive`, `Negative`, or `Neutral` based on the sentiment of the input text. This project demonstrates how to integrate a basic sentiment analysis tool with a RESTful API.

---

## Features
- **RESTful API**: Exposes endpoints to analyze mood-based text.
- **TextBlob Sentiment Analysis**: Uses polarity and subjectivity to classify moods.
- **Customizable**: Easily extendable with additional sentiment libraries.
- **Fast and Scalable**: Built using FastAPI for high performance.

---

## How It Works
1. **Input**: The user sends a text-based mood description via a POST request.
2. **Processing**: The API analyzes the sentiment using TextBlob.
3. **Output**: Returns the mood classification as:
   - `Positive`
   - `Negative`
   - `Neutral`

---

## Example Use Case
- A social media analysis tool to classify user posts.
- A chatbot to detect user emotions and respond accordingly.
- Integrating mood analysis into mental health or journaling apps.

---

## Prerequisites
- **Python 3.10+**
- Basic knowledge of Python and RESTful APIs.

---

## Installation and Setup
### 1. Clone the Repository
```bash
git clone https://github.com/preethi1915/mood-analysis-api.git
cd mood-analysis-api
