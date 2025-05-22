# AI Resume Evaluater

An AI-powered resume analysis tool that leverages Streamlit and the Grok API to evaluate PDF resumes.  
It extracts key information, assesses content quality, and provides actionable feedback to help users enhance their resumes.

## 🔍 Features

- **PDF Resume Upload**: Easily upload your resume in PDF format for analysis.
- **Text Extraction**: Utilizes the Grok API to extract text from uploaded resumes.
- **Content Evaluation**: Analyzes resume content to identify strengths and areas for improvement.
- **Actionable Feedback**: Provides suggestions to enhance resume quality and effectiveness.
- **User-Friendly Interface**: Built with Streamlit for an intuitive and interactive user experience.

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/siddhivdash/AI-Resume-Evaluater.git
   cd AI-Resume-Evaluater
2. Create a Virtual Environment (Optional but recommended):
    ```bash
    python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
    
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt

4.Set Up Environment Variables:
  ```bash
GROK_API_KEY=your_grok_api_key_here

5. Run the Application:
streamlit run app.py

📁 Project Structure
AI-Resume-Evaluater/
├── app.py               # Main Streamlit application
├── utils.py             # Utility functions for processing
├── sample.py            # Sample script for testing
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not included in version control)
├── tech_role_resumes-*.pdf  # Sample resumes for testing
└── README.md            # Project documentation
🤝 Contributing
Contributions are welcome! If you'd like to improve this project, please fork the repository and submit a pull request. For major changes, open an issue first to discuss your ideas.

📬 Contact
For questions or feedback, please contact Siddhivdash.






   
