# from dotenv import load_dotenv

# load_dotenv()
# import base64
# import streamlit as st
# import os
# import io
# from PIL import Image 
# import pdf2image
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_response(input,pdf_cotent,prompt):
#     model=genai.GenerativeModel('gemini-1.5-flash')
#     response=model.generate_content([input,pdf_content[0],prompt])
#     return response.text

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         ## Convert the PDF to image
#         images=pdf2image.convert_from_bytes(uploaded_file.read())

#         first_page=images[0]

#         # Convert to bytes
#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [
#             {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")

# ## Streamlit App

# st.set_page_config(page_title="ATS Resume EXpert")
# st.header("Resume Roaster 🔥🔥")
# input_text=st.text_area("Job Description: ",key="input")
# uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


# if uploaded_file is not None:
#     st.write("PDF Uploaded Successfully")


# submit1 = st.button("Tell Me About the Resume")

# #submit2 = st.button("How Can I Improvise my Skills")

# submit3 = st.button("Percentage match")

# input_prompt1 = """
# You are tasked with analyzing a resume and providing a roast-style critique. 
# Your goal is to identify the good and bad aspects of the resume, suggest improvements, 
# and if a job description is provided, analyze the resume in the context of the job requirements. Follow these instructions carefully:

# 1. First, carefully read the resume provided within the <resume> tags:
# The below text is extracted from a PDF, don't worry about the formatting or length. 
# OCR might have introduced some errors, but let's roll with it.




# 3. Analyze the resume, focusing on the following aspects:
#    a. Identify and list the good elements of the resume.
#    b. Identify and list the bad elements or weaknesses of the resume.
#    c. Suggest specific improvements for the resume.

# 4. If a job description was provided, compare the resume to the job requirements. Analyze how well the candidate's qualifications match the job requirements.

# 5. Prepare your response in Markdown format. Use appropriate headings, bullet points, and formatting to structure your analysis.

# 6. Your response should include the following sections:
#    - Introduction (brief overview of the resume)
#    - The Good (positive aspects of the resume)
#    - The Bad (weaknesses or areas needing improvement)
#    - How to Improve (specific suggestions for enhancement)
#    - Job Fit Analysis (only if a job description was provided)

# 7. Maintain a roast-style tone throughout your critique. 
#   Be humorous and slightly exaggerated in your criticism, but ensure your analysis remains constructive and helpful. 
#   Use witty language, puns, or pop culture references if appropriate.

# 8. Begin your response with the phrase "Alright, let's roast this dumpster fire of a resume!" to set the tone.

# 9. Conclude your analysis with a brief, humorous summary statement about the overall quality of the resume.

# 10. Use Emojis and slangs for fun.

# 11. Make sure you rate the sections out of 10. like lit/10, fire/10, absolute trash/10, etc.

# Remember, while the tone should be humorous and roast-like, the ultimate goal is to provide valuable feedback that can help improve the resume. 
# Balance your criticism with constructive advice.
# """

# input_prompt3 = """
# You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
# your task is to evaluate the resume against the provided job description, and then roast the hell out of the resume. Then give me the percentage of match if the resume matches
# the job description. First the output should come as percentage and then keywords missing and last final thoughts.
# """

# if submit1:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt1,pdf_content,input_text)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")

# elif submit3:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt3,pdf_content,input_text)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")



   




from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to analyze resume
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

# Function to process uploaded PDF
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Set Streamlit page config
st.set_page_config(page_title="ATS Resume Expert", page_icon="🔥", layout="centered")

# 🌙 Dark Mode - Custom Styling
st.markdown(
    """
    <style>
    /* Background & Text */
    body, .stApp {
        background-color: #121212;
        color: #E0E0E0;
    }

    /* Centering content */
    .stApp {
        max-width: 850px;
        margin: auto;
        padding: 20px;
    }

    /* Title Styling */
    .stMarkdown h1 {
        font-size: 2.8rem;
        font-weight: bold;
        text-align: center;
        color: #BB86FC;
        text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.2);
    }

    /* Subheaders */
    .stMarkdown h2 {
        font-size: 1.8rem;
        font-weight: bold;
        color: #BB86FC;
    }

    /* Text Areas & Inputs */
    .stTextArea textarea, .stTextInput input {
        background-color: #1E1E1E !important;
        color: #E0E0E0 !important;
        border-radius: 10px !important;
        padding: 12px !important;
        border: 1px solid #BB86FC !important;
    }

    /* File Upload */
    .stFileUploader {
        background-color: #1E1E1E !important;
        border: 2px dashed #BB86FC !important;
        padding: 20px !important;
        border-radius: 12px !important;
        text-align: center;
        color: #E0E0E0 !important;
    }

    /* Buttons */
    .stButton > button {
        background-color: #BB86FC !important;
        color: white !important;
        font-size: 1rem;
        font-weight: bold;
        padding: 12px 24px !important;
        border-radius: 8px !important;
        border: none !important;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 10px rgba(187, 134, 252, 0.4);
    }

    .stButton > button:hover {
        background-color: #9B69E1 !important;
        transform: scale(1.05);
        box-shadow: 0 6px 15px rgba(187, 134, 252, 0.6);
    }

    /* Success Message */
    .stAlert {
        background-color: #2E2E2E !important;
        color: #BB86FC !important;
        font-weight: bold;
        border-radius: 10px !important;
        padding: 15px !important;
    }

    /* Container Backgrounds */
    .stContainer {
        background-color: #1E1E1E !important;
        padding: 20px !important;
        border-radius: 12px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# 📝 UI Elements
st.title("🔥 Resume Roaster - ATS Expert")

# Job Description Input
st.subheader("📌 Enter Job Description")
input_text = st.text_area("Paste the job description here:", key="input")

# Resume Upload Section
st.subheader("📂 Upload Your Resume")
uploaded_file = st.file_uploader("Drag & drop or click to upload (PDF only)", type=["pdf"])

if uploaded_file:
    st.success("✅ Resume uploaded successfully!")

# Buttons Section (Centered)
col1, col2 = st.columns(2)
with col1:
    submit1 = st.button("🔥 Roast My Resume")
with col2:
    submit3 = st.button("📊 Percentage Match")

input_prompt1 = """
You are tasked with analyzing a resume and providing a roast-style critique. 
Your goal is to identify the good and bad aspects of the resume, suggest improvements, 
and if a job description is provided, analyze the resume in the context of the job requirements. Follow these instructions carefully:

1. First, carefully read the resume provided within the <resume> tags:
The below text is extracted from a PDF, don't worry about the formatting or length. 
OCR might have introduced some errors, but let's roll with it.




3. Analyze the resume, focusing on the following aspects:
   a. Identify and list the good elements of the resume.
   b. Identify and list the bad elements or weaknesses of the resume.
   c. Suggest specific improvements for the resume.

4. If a job description was provided, compare the resume to the job requirements. Analyze how well the candidate's qualifications match the job requirements.

5. Prepare your response in Markdown format. Use appropriate headings, bullet points, and formatting to structure your analysis.

6. Your response should include the following sections:
   - Introduction (brief overview of the resume)
   - The Good (positive aspects of the resume)
   - The Bad (weaknesses or areas needing improvement)
   - How to Improve (specific suggestions for enhancement)
   - Job Fit Analysis (only if a job description was provided)

7. Maintain a roast-style tone throughout your critique. 
  Be humorous and slightly exaggerated in your criticism, but ensure your analysis remains constructive and helpful. 
  Use witty language, puns, or pop culture references if appropriate.

8. Begin your response with the phrase "Alright, let's roast this dumpster fire of a resume!" to set the tone.

9. Conclude your analysis with a brief, humorous summary statement about the overall quality of the resume.

10. Use Emojis and slangs for fun.

11. Make sure you rate the sections out of 10. like lit/10, fire/10, absolute trash/10, etc.

Remember, while the tone should be humorous and roast-like, the ultimate goal is to provide valuable feedback that can help improve the resume. 
Balance your criticism with constructive advice.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description, and then roast the hell out of the resume. Then give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("🔍 Resume Analysis:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume.")

elif submit3:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("📊 Percentage Match Result:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume.")
   




