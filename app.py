# pdf_app/App.py
import streamlit as st
from microservices.PdfProcessor import read_pdf

def login():
    # Überprüfen, ob der Benutzer bereits angemeldet ist
    if 'logged_in' in st.session_state and st.session_state.logged_in:
        return True
    
    username = st.text_input("Benutzername:")
    password = st.text_input("Passwort:", type="password")

    if st.button("Anmelden"):
        if username == "admin" and password == "admin":
            st.success("Erfolgreich angemeldet!")            
            st.session_state.logged_in = True
            return True
        else:
            st.error("Falscher Benutzername oder falsches Passwort.")
            return False

def main():
    st.title("PDF-Inhalt extrahieren")    
    
    if login():
        # File Uploader
        uploaded_file = st.file_uploader("PDF-Datei hochladen", type=["pdf"])

        # Anzeigen des Inhalts und Nachricht, wenn eine Datei hochgeladen wurde
        if uploaded_file is not None:        
            pdf_text, message = read_pdf(uploaded_file)
        
            # Anzeige der Erfolg- oder Fehlermeldung        
            if "Success" in message:
                st.success(message)
            else:
                st.error(message)        
        
            # Text anzeigen        
            st.subheader("Inhalt der PDF-Datei")
            st.write(pdf_text)     

        # Abmelden-Button hinzufügen
        if st.button("Abmelden"):
            st.session_state.logged_in = False
            st.rerun()            

if __name__ == "__main__":
    main()
