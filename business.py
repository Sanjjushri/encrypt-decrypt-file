import streamlit as st
from cryptography.fernet import Fernet


keyss=Fernet.generate_key()
print(keyss)

keys="_2W26CqmfuNpxIN0nE1Hb-1PIbXGBCIpo_h2_pGVP-c="
key = bytes(keys, 'utf-8')

st.title("Encrypt and Decrypt your  File ")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    
    fernet=Fernet(key)

    with open('key.key','wb')as filekey:
        filekey.write(key)

    with open('key.key','rb')as filekey:
        key = filekey.read()
        
    # with open(uploaded_file,'rb')as file:

    originalaudio = uploaded_file.read()
        
    encrypted = fernet.encrypt(originalaudio)

    with open('voice encryption.mp3','wb')as encrypted_file:
        encrypted_file.write(encrypted)

    fernet = Fernet(key)

    with open('voice encryption.mp3','rb') as enc_file:
        encrypted = enc_file.read()
        
    decrypted = fernet.decrypt(encrypted)

    with open('voice decryption.mp3','wb')as dec_file:
        dec_file.write(decrypted)

    with open('voice encryption.mp3') as f:
        st.download_button('Download Encrypted File', f)

    # with open('voice decryption.mp3') as f:
    #     st.download_button('Download decry mp3', f)

    # audio_file = open("audio-sample.mp3", "rb")

    # st.audio(audio_file.read())

    if st.button('Show Decrypted file'):
        audio_file = open("voice decryption.mp3", "rb")
        st.audio(audio_file.read())

   