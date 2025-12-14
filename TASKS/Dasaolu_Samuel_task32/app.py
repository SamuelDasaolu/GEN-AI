import streamlit as st
import os
import tempfile
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# --- Page Config ---
st.set_page_config(page_title="Interactive Biography RAG", page_icon="👤")

st.title("👤 Interactive Biography")
st.markdown("Upload a biography (text file) and ask questions to chat with it.")

# --- Sidebar: Configuration ---
with st.sidebar:
    st.header("1. Setup")
    api_key = st.text_input("Google API Key", type="password")
    st.markdown("[Get a Google API Key](https://aistudio.google.com/app/apikey)")
    
    st.divider()
    
    st.header("2. Knowledge Base")
    uploaded_file = st.file_uploader("Upload Biography (.txt)", type="txt")
    
    # Use default biography.txt if no file uploaded
    if not uploaded_file and os.path.exists("biography.txt"):
        st.info("Using default 'biography.txt'. Upload a new file to override.")

# --- RAG Functions ---

@st.cache_resource(ttl="1h")
def build_vector_store(file_path, _api_key):
    """
    Builds the FAISS vector store from a text file.
    Cached to prevent rebuilding on every interaction.
    """
    try:
        # 1. Load the document
        loader = TextLoader(file_path)
        docs = loader.load()

        # 2. Split text into chunks
        # Biographies often have dense paragraphs, so we use a reasonable chunk size
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)

        # 3. Create Embeddings
        # We explicitly pass the API key here to ensure it works even if env var isn't set globally
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001", 
            google_api_key=_api_key
        )

        # 4. Build FAISS Index
        vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)
        return vectorstore

    except Exception as e:
        st.error(f"Error processing document: {e}")
        return None

def get_rag_chain(vectorstore, _api_key):
    """
    Creates the retrieval chain.
    """
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", 
        temperature=0.3,
        google_api_key=_api_key
    )

    system_prompt = (
        "You are an AI assistant representing the person described in the context. "
        "Answer questions as if you are that person, or an expert biographer. "
        "Use the following pieces of retrieved context to answer the question. "
        "If the answer is not in the context, clearly state that the biography does not contain that information. "
        "Keep answers concise and relevant."
        "\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    retriever = vectorstore.as_retriever()
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    return rag_chain

# --- Main Logic ---

if not api_key:
    st.warning("Please enter your Google API Key in the sidebar to start.")
    st.stop()

# Handle File Loading
file_path = "biography.txt" # Default
temp_file = None

if uploaded_file:
    # Save uploaded file to a temporary path
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
        tmp.write(uploaded_file.getvalue())
        file_path = tmp.name
        temp_file = file_path # Mark for cleanup

# Check if file exists
if not os.path.exists(file_path):
    st.error("No biography file found. Please upload a .txt file or create 'biography.txt'.")
    st.stop()

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Build Vector Store
with st.spinner("Processing biography..."):
    vectorstore = build_vector_store(file_path, api_key)

if vectorstore:
    rag_chain = get_rag_chain(vectorstore, api_key)

    # Display Chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User Input
    if prompt := st.chat_input("Ask about the biography..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = rag_chain.invoke({"input": prompt})
                answer = response['answer']
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})

# Cleanup temp file if used
if temp_file and os.path.exists(temp_file):
    try:
        os.remove(temp_file)
    except:
        pass