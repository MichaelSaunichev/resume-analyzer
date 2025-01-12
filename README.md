# Resume Analyzer

This project extracts text from a PDF resume and analyzes it using OpenAI's API to provide suggestions for improvements.

## Instructions:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
Replace <repository-url> with the URL of the repository (e.g., https://github.com/MichaelSaunichev/resume-analyzer).

2. **Delete placeholder .gitkeep files from the resume and output directories**

3. **Install the required Python packages**:
   ```bash
   pip install -r requirements.txt

4. **Add your OpenAI API key**:
Edit `resume_analyzer.py` and add your OpenAI API key to the `api_key` field inside `client = OpenAI(api_key="")`.

5. **Add your resume (in PDF format) to the resume folder**

6. **Run the script**:
   ```bash
   python resume_analyzer.py
