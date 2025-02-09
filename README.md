## Taste Bud Review

**Project Overview**
  Taste Bud Review is a web-based application that allows users to enter a restaurant review and receive sentiment analysis results (positive or negative). Based on the sentiment, the application displays a corresponding video within the review box.

**Features**:
  - Users can input their restaurant review in a text area.
  - The review is analyzed using a Multinomial Naive Bayes sentiment analysis model.  
  - If the sentiment is positive, a positive-themed video is displayed.
  - If the sentiment is negative, a negative-themed video is displayed.
  - The review box seamlessly transitions to a video display while maintaining the same dimensions.
  - A back button allows users to return to the review input box.

**Technologies Used**

Frontend: HTML, CSS, JavaScript
Backend: Flask (Python)
Machine Learning Model: Multinomial Naive Bayes for sentiment classification
Dataset: Restaurant review dataset for training the model

**Project Structure**
      Taste-Bud-Review/
      │── templates/
      │   ├── index.html (Frontend UI)
      │   ├── food-bg.jpg (Background image)
      │   ├── positive.mp4 (Positive sentiment video)
      │   ├── negative.mp4 (Negative sentiment video)
      │── app.py (Flask Backend)
      │── model.pkl (Trained sentiment analysis model)
      │── README.md (Project Documentation)

**API Endpoints**
  **POST /predict**
    Request: { "review": "The food was amazing!" }
    Response: { "sentiment": "Positive" }

**Future Enhancements**
  - Improve UI with animations and additional styling.
  - Enhance model accuracy with deep learning techniques.
  - Add support for multi-class sentiment analysis.

**Credits**
  Developed by R.K.Apoorva 
  Special thanks to OpenAI for guidance.

**License**:
  This project is open-source and available under the MIT License.

