# Gemini LLM Application

This is a Streamlit application that interacts with the Gemini LLM (Large Language Model) using the Google Generative AI API. The application allows users to ask questions and receive responses generated by the Gemini model.

## Setup

### Prerequisites

Make sure you have the following installed:

- Python
- [Streamlit](https://streamlit.io/) (`pip install streamlit`)
- [Google Generative AI](https://pypi.org/project/google-generativeai/) (`pip install google-generativeai`)
- [Pillow](https://pillow.readthedocs.io/en/stable/) (`pip install Pillow`)

### Configuration

1. Create a `.env` file in the project root.
2. Add your Google API key to the `.env` file:

   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```
   Make sure to replace your_api_key_here with your actual Google API key.

## Usage

### Running the Application
To run the streamlit application,use the following command:
```bash
streamlit run app.py //for chat model
streamlit run vision.py //for image and chat model
streamlit run chat_app.py //for Q&A chat bot 
```
Access the application in your web browser at the provided URL (usually http://localhost:8501).


### Asking Questions

1. Enter your question in the "Input" text box.
2. Click the "Ask a Question" button to get a response.

### Image Demo

1. Enter an input prompt in the "Input Prompt" text box.
2. Upload an image by clicking the "Choose an image..." button.
3. Click the "Tell me about the image" button to receive a response.

### Chat App Demo

1. Enter a message in the "Input" text box.
2. Click the "Ask Question" button to send your question to the Gemini Pro model.
3. View the AI's response in the main section of the app.
4. The chat history is displayed in the sidebar.


## Additional Information

- **Gemini LLM Model:**
  The application leverages the Gemini LLM model for generating responses to user queries. This powerful language model is provided by Google Generative AI.

- **Image Queries:**
  For image-related queries, the application intelligently combines textual input and uploaded images to enrich the context of the user's question. This enhances the overall user experience and allows for more nuanced responses.

- **Technologies Used:**
  This project is built upon the Google Generative AI API, which provides advanced language models, and Streamlit, a user-friendly framework for creating interactive web applications. The integration of these technologies ensures a seamless and responsive web interface.

Feel free to explore, customize, and extend the application based on your needs!


   
