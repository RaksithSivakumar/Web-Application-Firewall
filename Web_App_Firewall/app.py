import streamlit as st
import os
from waf import check_request_for_attacks
from blockchain import Blockchain

# Initialize the blockchain
blockchain = Blockchain()

# Streamlit app title
st.title("Web Application Firewall (WAF) with Blockchain Logging")

# Option for text input or file upload
option = st.radio("Choose input type:", ("Text", "File"))

# Handle text input
if option == "Text":
    user_input = st.text_area("Enter input to check for vulnerabilities:")

    if st.button("Submit Text"):
        # Check the text for attacks
        attack_type = check_request_for_attacks(user_input)

        if attack_type:
            st.error(f"Blocked due to {attack_type} attack!")
            # Log attack in blockchain
            blockchain.add_new_transaction({"attack": attack_type, "input": user_input})
            blockchain.mine()
        else:
            st.success("Input is safe!")

# Handle file upload
elif option == "File":
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        # Save file to uploads directory
        if not os.path.exists("uploads"):
            os.mkdir("uploads")

        file_path = os.path.join("uploads", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Read and process file content
        with open(file_path, "r") as f:
            file_content = f.read()

        st.text(f"File content:\n{file_content}")
        
        if st.button("Submit File"):
            # Check file content for attacks
            attack_type = check_request_for_attacks(file_content)

            if attack_type:
                st.error(f"Blocked due to {attack_type} attack!")
                # Log attack in blockchain
                blockchain.add_new_transaction({"attack": attack_type, "input": file_content})
                blockchain.mine()
            else:
                st.success("File content is safe!")

# Display the blockchain
st.write("Blockchain Log of Attacks:")
for block in blockchain.chain:
    st.write(f"Block {block['index']}: {block['transactions']}")
