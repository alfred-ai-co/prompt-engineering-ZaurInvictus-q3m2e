
# Setup: Preparing Your Development Environment
Before starting with prompt engineering techniques, it’s important to ensure your development environment is set up correctly. This setup includes creating a virtual environment, installing dependencies, and securing your Google API key, ensuring smooth execution of the quiz generator.

Step 1: Create and Activate a Virtual Environment
Create the Environment:
Using Python’s built-in venv module, run the following command to create a virtual environment in your project directory:

bash

python -m venv env        
Alternatively, you can use Conda for managing environments. If you haven't installed Conda yet, follow the installation process detailed at Conda Docs.

Activate the Virtual Environment:
For Linux and macOS, activate the environment with:
bash

source env/bin/activate
For Windows, activate the environment with:
bash

env\Scripts\activate
Once activated, your shell will indicate the active environment, isolating your Python installation from the system-wide environment. To deactivate, simply type deactivate.
Step 2: Install Dependencies
Install Required Libraries:
With the environment activated, run the following command to install dependencies from the requirements.txt file:
bash

pip install -r requirements.txt
Alternatively, you can manually install the key libraries using:
bash

pip install langchain langchain-google-genai pydantic streamlit python-dotenv
Step 3: Secure Your Google API Key
Create a .env File:
At the root of your project, create a .env file to store sensitive information like your GOOGLE_API_KEY. Add the following line to the file:
GOOGLE_API_KEY=your_google_api_key
Prevent the .env File from Being Committed:
Ensure that a .gitignore file exists in your project and that .env is included to prevent it from being accidentally committed to your repository.
Step 4: Check the Project Structure and Run the Application
Review the README.md:
Take a moment to review the project’s README.md file, which contains the project structure and additional setup instructions.
Run the Streamlit Application:
Use the following command to launch the Streamlit application and verify your setup:
bash

streamlit run main.py
The application will inform you if any environment variables, such as GOOGLE_API_KEY, are missing.

