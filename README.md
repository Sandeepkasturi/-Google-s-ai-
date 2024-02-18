# SKAV TECH Flask and Streamlit Application

This project combines Flask and Streamlit to create a web application that serves HTML content and integrates an AI chatbot, HTML extraction, and other functionalities.

### Prerequisites

- Python 3.x
- Flask
- Streamlit
- Google Generative AI library

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sandeepkasturi/google-s-ai.git
    cd google-s-ai
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Start the Flask server:

    ```bash
    python flask_app.py
    ```

2. Open a web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the SKAV TECH application.

3. Enter a URL to extract HTML code or ask the SKAV AI chatbot a question.

### Explanation of Files

- `skav_tech.py`: Main Python script containing Flask and Streamlit application logic.
- `requirements.txt`: List of Python dependencies required for the project.

### Key Functionality

- **Flask Integration**:
    - Handles the main web application and serves HTML content.
    - Starts a Streamlit application after a delay.

- **Streamlit Application**:
    - Provides features for extracting HTML code from a given URL.
    - Integrates the SKAV AI chatbot for answering user questions.
    - Offers options to open URLs and save generated content to Notepad.

- **Google Generative AI**:
    - Utilizes the Generative AI library for generating AI responses.

### Configuration

- Replace `'YOUR_API_KEY_HERE'` in the code with your actual Google Generative AI API key.

### Troubleshooting

- If the application prompts for a PIN after conversion to an executable, consider checking for:
    - Elevated permissions required by the application.
    - User Account Control (UAC) settings on Windows.
    - Interference from antivirus or security software.
    - Code signing options for the executable.

### Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any improvements or bug fixes.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
