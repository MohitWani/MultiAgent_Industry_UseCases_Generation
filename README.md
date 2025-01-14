# MultiAgent_Industry_UseCases_Generation

This project is designed to use a Multi-Agent Architecture get information quickly without wasting time to read research paper. It implement Arxiv AGENT, Tools and Advance Retrieval Augmented Generation to get relevant information about any research papers.

---

### Key Features.

- Feature 1: Utilize a CrewAI Multi-Agents and serperdev Tool for getting accurate information about Industry.
- Feature 2: Created a Advanced Retrieval Augmented Generation Pipeline for documents Not in Arxiv Library.

---

### Technology used.

- **Language/Frameworks** : Python, CrewAI, Streamlit.

---

## Installation

Follow these steps to install and run the project locally:

### Prerequisites

Ensure that the following are installed on your system:

#### For Local Setup:

- **Python 3.11.6**: You can download it from [Python's official website](https://www.python.org/downloads/).
- **pip**: Python package installer (comes with Python).
- **git**: For cloning the repository.
- **API keys**: Check .env.example file to add your own api tokens.


### Local Setup

1. **Clone the Repository**

   First, clone the repository from GitHub to your local machine:

   ```bash
   git clone https://github.com/MohitWani/MultiAgent_Industry_UseCases_Generation.git
   ```

2. **Navigate to the Project Directory**

    ```bash
    cd MultiAgent_Industry_UseCases_Generation
    ```
 
3. **Create a Virtual Environment**

    ```bash
    python -m venv env
    env\Scripts\activate
    ```

4. **Install the Required Dependencies**

    install all required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

5. **Setup API TOKENS**

    Create .env file:

    //add your own API tokens use .env.example file for reference.
    ```bash
    touch .env


6. **Run the Application**

    Finally, run the application:

- For a Streamlit app:

    ```bash
    streamlit run app.py
    ```

---

#### Agent Input and UI
![Project Screenshot](./assets/Input_UI.png)
---
![Project Screenshot](./assets/output_UI.png)


