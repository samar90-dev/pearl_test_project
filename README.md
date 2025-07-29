# Integration Proxy API

A FastAPI-based automation platform that acts as a proxy to external APIs with mocked third-party integrations.

## Technologies Used

- **Python 3.8+**
- **FastAPI** - Modern, fast web framework for building APIs
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI web server implementation
- **Pytest** - Testing framework
- **HTTPX** - Async HTTP client for testing

## Features

- RESTful API endpoint `/integrate/{provider}` for third-party integrations
- Support for multiple providers (Salesforce, UPS)
- Multiple authentication schemes (password, API key, OAuth)
- Normalized JSON responses with error handling
- Extensible architecture for adding new providers
- Comprehensive unit tests

## Installation and Usage

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**

   ```bash
   cd app
   python main.py
   ```
   
   Or using uvicorn directly:

   ```bash
   uvicorn app.main:app --reload
   ```

3. **Access the API:**
   - API will be available at `http://localhost:8000`
   - Interactive docs at `http://localhost:8000/docs`
   - List providers at `http://localhost:8000/providers`

4. **Run tests:**

   ```bash
   pytest tests/
   ```

## API Usage Examples

### Salesforce Integration

```bash
curl -X POST "http://localhost:8000/integrate/salesforce" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "create_contact",
    "parameters": {
      "firstName": "John",
      "lastName": "Doe",
      "email": "john.doe@example.com"
    }
  }'
```

### UPS Integration

```bash
curl -X POST "http://localhost:8000/integrate/ups" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "track_package",
    "parameters": {
      "tracking_number": "1Z12345E0205271688"
    }
  }'
```

> This is a challenge by Coodesh

## Completion and Submission Instructions

1. Add the link to the repository with your solution to the task on the platform
2. Check if the Readme is good and make the final commit to your repository
3. Submit and wait for further instructions. If the test requires a video presentation, it will be possible to record it on the submission screen after adding the repository link. Good luck and success! =)

## Support

For questions about the process, send a message directly to a specialist in the platform chat.y Template

This is a sample repository for you to start developing the task. Please carefully read the requirements of the task statement on the platform and follow best practices on how to use this repository.

## Repository Readme

- It should contain the project title
- A one-sentence description about the project
- It should include a list of languages, frameworks, and/or technologies used
- How to install and use the project (instructions)
- Don't forget the .gitignore
- If you are using a personal GitHub, mention that it is a challenge by Coodesh:

> This is a challenge by Coodesh

## Completion and Submission Instructions
1. Add the link to the repository with your solution to the task on the platform
2. Check if the Readme is good and make the final commit to your repository
3. Submit and wait for further instructions. If the test requires a video presentation, it will be possible to record it on the submission screen after adding the repository link. Good luck and success! =)

## Support

For questions about the process, send a message directly to a specialist in the platform chat.