### **Insightify- Turn PDFs into instant insights💁**

---

#### **Overview**

This project is a Streamlit-based web application that allows users to upload PDF files and interact with their content using natural language questions. The app leverages Google Generative AI (Gemini) for embeddings and conversational AI and FAISS (Facebook AI Similarity Search) for vector storage and retrieval.

---

### **Features**

- Upload multiple PDF files and process their content.
- Automatically split PDF text into manageable chunks for better processing.
- Create vector embeddings for efficient similarity-based text retrieval.
- Ask questions related to the uploaded PDF content and receive detailed responses.
- Intuitive web interface with a sidebar menu for easy navigation.

---

### **Technologies Used**

- **Python Libraries:**
  - [Streamlit](https://streamlit.io/) for building the web application.
  - [PyPDF2](https://pypi.org/project/PyPDF2/) for extracting text from PDF files.
  - [LangChain](https://github.com/hwchase17/langchain) for handling embeddings, text splitting, and conversational AI.
  - [FAISS](https://github.com/facebookresearch/faiss) for vector similarity search.
  - [Google Generative AI](https://cloud.google.com/ai/) for embeddings and conversational modeling.
  - [dotenv](https://pypi.org/project/python-dotenv/) for environment variable management.

- **Vector Database:** FAISS
- **Embeddings and AI Models:** Google Generative AI (Gemini)

---

### **Setup and Installation**

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-repo/chat-pdf-gemini.git
   cd chat-pdf-gemini
   ```

2. **Install Dependencies**  
   Create a virtual environment and install the required libraries:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set Up Google API Key**  
   - Obtain an API key from [Google Cloud](https://console.cloud.google.com/).
   - Create a `.env` file in the project directory and add the API key:
     ```env
     GOOGLE_API_KEY=your_api_key_here
     ```

4. **Run the Application**  
   Start the Streamlit server:
   ```bash
   streamlit run main.py
   ```

---

### **Usage Instructions**

1. Open the application in your browser (the terminal will display the URL, usually `http://localhost:8501`).
2. Use the **sidebar menu** to upload one or more PDF files.
3. Click the **Submit & Process** button to extract and process the content.
4. Once processing is complete, enter a question related to the uploaded PDF content in the input field.
5. View the generated response in real time.

---

### **Code Structure**

- **`main.py`**: The main script containing all the logic for the application.
- **Functions**:
  - `get_pdf_text(pdfs)`: Extracts text from the uploaded PDF files.
  - `make_chunks(text)`: Splits the text into smaller chunks for processing.
  - `vector_space(text_chunks)`: Creates a vector store from the text chunks.
  - `get_conversational_chain()`: Sets up the conversational chain using Gemini.
  - `user_input(user_question)`: Handles the user's question and generates a response.

---

### **Key Notes**

- Ensure the Google API key is valid and has appropriate permissions for using Generative AI models.
- For safety, the `allow_dangerous_deserialization` flag is explicitly set to `True`. Only use with trusted data sources.
- FAISS stores the vector database locally in the `faiss_index` directory.

---

### **Future Improvements**

- Add support for other file formats like Word and plain text.
- Enhance the conversational model to include multi-turn interactions.
- Deploy the app to a cloud platform for public access.

---

### **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.  

---

### **Contributors**

- **Your Name**  
  [GitHub](https://github.com/your-username) | [LinkedIn](https://linkedin.com/in/your-profile)  

---
