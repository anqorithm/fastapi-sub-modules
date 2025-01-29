# FastAPI Modular App with Git Submodules (POC)

A proof of concept demonstrating how to build a modular FastAPI application using Git submodules as packages.

## Key Concepts
- **Git Submodules**: Used as independent packages, allowing for modular development.
- **Shared Dependencies**: Ensures that all modules can share common dependencies, reducing redundancy.
- **Centralized FastAPI App Integration**: Combines all modules into a single FastAPI application.
- **Poetry**: Utilized for managing dependencies and virtual environments.

## Quick Start
1. **Clone the Repository with Submodules**:
   Use the following command to clone the repository along with its submodules:
   ```bash
   git clone --recurse-submodules https://github.com/anqorithm/fastapi-sub-modules.git
   ```

2. **Install Dependencies**:
   Navigate to the project directory and install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. **Activate the Virtual Environment**:
   Activate the virtual environment created by Poetry:
   ```bash
   poetry shell
   ```

4. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   poetry run uvicorn src.main:app --reload
   ```

5. **Explore the API**:
   Open your browser and navigate to `http://localhost:8000/docs` to explore the API documentation provided by FastAPI's interactive Swagger UI.

This setup is particularly useful for projects that require a modular architecture, allowing different teams to work on separate modules independently while still integrating them into a single application. The use of Git submodules helps in managing these modules as separate repositories, which can be beneficial for version control and collaboration.
