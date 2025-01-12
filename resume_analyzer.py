import os
import fitz
from openai import OpenAI

# Set your OpenAI API key
client = OpenAI(
    api_key = ""  # Add your API key here
)

# Paths
RESUME_FOLDER = "./resume"
OUTPUT_FOLDER = "./output"
ANALYSIS_OUTPUT = os.path.join(OUTPUT_FOLDER, "resume_analysis.txt")

def extract_text_from_pdf(file_path):
    """Extract text from your PDF file"""
    try:
        with fitz.open(file_path) as pdf:
            text = ""
            for page in pdf:
                text += page.get_text("text")
        return text
    except Exception as e:
        raise ValueError(f"Error extracting text from PDF: {e}")

def analyze_resume(resume_text):
    """Send the PDF text to the OpenAI API"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a professional resume analyzer."},
                {"role": "user", "content": f"Analyze this resume and suggest improvements:\n\n{resume_text}"}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"Error analyzing document: {e}")

def main():
    """Main script"""
    # Ensure folders exist
    if not os.path.exists(RESUME_FOLDER):
        os.makedirs(RESUME_FOLDER)
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Check the number of PDF files in the resume folder
    pdf_files = [f for f in os.listdir(RESUME_FOLDER) if f.endswith(".pdf")]

    if len(pdf_files) == 0:
        print("No PDF files found in the resume folder. Please add a resume and try again.")
        return
    elif len(pdf_files) > 1:
        print("Multiple PDF files found. Ensure there is only one PDF in the resume folder.")
        return

    # Extract the text from the PDF
    pdf_path = os.path.join(RESUME_FOLDER, pdf_files[0])
    print(f"Processing resume: {pdf_files[0]}")
    try:
        resume_text = extract_text_from_pdf(pdf_path)
    except ValueError as e:
        print(e)
        return

    # Analyze the resume using OpenAI API
    try:
        analysis = analyze_resume(resume_text)
    except RuntimeError as e:
        print(e)
        return

    # Save the analysis to a file
    with open(ANALYSIS_OUTPUT, "w") as output_file:
        output_file.write(analysis)

    print(f"Resume analysis complete. Results saved to: {ANALYSIS_OUTPUT}")

if __name__ == "__main__":
    main()