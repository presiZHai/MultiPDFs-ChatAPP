import streamlit as st 


def main():
    st.set_page_config(page_title="Chat with PDF Docs", page_icon=":books:")
    st.header("Chat with PDFs App :books:")
    st.text_input("Ask questions about the uploaded documents")
    
    with st.sidebar:
        st.subheader("Choose a PDF Document")
        pdf_file = st.file_uploader("Upload a PDF document", type=["pdf"])
        
        if pdf_file is not None:
            st.text("You have uploaded a PDF document.")
            st.text(f"Filename: {pdf_file.name}")
            st.text(f"Filesize: {pdf_file.size} bytes")
            st.text("Processing...")

if __name__ == "__main__":
    main()
