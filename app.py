from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_cotent,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

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

## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("Resume Roaster 🔥🔥")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

#submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")

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
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")



   




