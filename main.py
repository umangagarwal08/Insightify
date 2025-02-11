import streamlit as st 
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GOOGLE-API-KEY")
genai.configure(api_key=api_key)


def get_pdf_text(pdfs):
    text=""
    for pdf in pdfs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

def make_chunks(text):
    text_split=RecursiveCharacterTextSplitter(chunk_size=10000)
    chunks=text_split.split_text(text)
    return chunks


def vector_space(text_chunks):
    
    embeddings = GoogleGenerativeAIEmbeddings(google_api_key=api_key,model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    
    vector_store.save_local("faiss_index")
    


def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro",api_key=api_key,
                             temperature=0.3)
    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain



def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(google_api_key=api_key,model = "models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index",embeddings, allow_dangerous_deserialization=True)

    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    print(response)
    st.write("Reply: ", response["output_text"])


def main():
    st.set_page_config("Chat PDF")
    st.header("Insightify- Turn PDFs into instant insights💁")

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = make_chunks(raw_text)
                vector_space(text_chunks)
                st.success("Done")



if __name__ == "__main__":
    main()