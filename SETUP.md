# VHOTIEX AI Quick Start & Local Setup Guide

This guide covers the local setup for the Android app and Python backend, plus the common development workflows, API usage, debugging, and troubleshooting for the project.

## 1. Project overview

VHOTIEX AI is an Android-first AI assistant with a holographic interface, multi-agent orchestration, voice-first interaction, and dark premium UI styling.

The repository contains two main application layers:

- Android app: Kotlin + Jetpack Compose in `app/`
- Backend API: FastAPI in `backend/`

## 2. Prerequisites

Install the following before starting development:

- Android Studio (latest stable)
- JDK 17
- Python 3.10 or newer
- pip
- Git
- Android emulator or a physical Android device
- Optional: Postman, curl, or a browser-based API client

Recommended versions:

- Android Studio: Hedgehog or newer
- JDK: 17
- Python: 3.10 or 3.11

## 3. Repository structure

```text
sturdy-funicular/
├── .github/
├── app/
│   ├── build.gradle.kts
│   └── src/
│       └── main/
│           ├── AndroidManifest.xml
│           └── java/com/vhotiex/
│               ├── app/
│               ├── model/
│               ├── navigation/
│               └── ui/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── agents.py
│   │       └── chat.py
│   └── services/
│       ├── __init__.py
│       ├── agent_orchestrator.py
│       ├── memory_service.py
│       ├── model_router.py
│       └── tool_executor.py
├── ARCHITECTURE.md
├── APP_FLOW.md
├── BACKEND_SCHEMA.md
├── DESIGN.md
├── IMPLEMENTATION_PLAN.md
├── README.md
├── SETUP.md
├── build.gradle.kts
├── gradle.properties
├── settings.gradle.kts
├── LICENSE
└── ...
```

Key files:

- `app/build.gradle.kts`: Android app-level Gradle configuration
- `build.gradle.kts`: top-level Gradle settings and plugin versions
- `backend/main.py`: FastAPI app entrypoint
- `backend/api/routes/chat.py`: chat endpoint definitions
- `backend/api/routes/agents.py`: agent API definitions
- `backend/services/agent_orchestrator.py`: agent selection and orchestration logic
- `backend/services/model_router.py`: model map for agent routing

## 4. Backend local setup

### 4.1 Create a virtual environment

From the project root:

```bash
cd sturdy-funicular
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
cd sturdy-funicular
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4.2 Install backend dependencies

The project currently uses FastAPI and Uvicorn. Install them with:

```bash
pip install fastapi uvicorn
```

If a future `requirements.txt` file is added, use:

```bash
pip install -r requirements.txt
```

### 4.3 Run the backend

From the project root:

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

Verify it starts successfully:

- App root: `http://localhost:8000/`
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 5. Android app local setup

### 5.1 Open in Android Studio

1. Open Android Studio
2. Choose `Open an existing project`
3. Select the repository root folder
4. Let Gradle sync finish

### 5.2 Confirm Android project configuration

The app is configured with:

- Kotlin
- Jetpack Compose
- JDK 17
- Android namespace: `com.vhotiex.app`
- `compileSdk = 34`
- `targetSdk = 34`

### 5.3 Run the app

From Android Studio:

1. Select an emulator or connected device
2. Choose the `app` run configuration
3. Click Run

From terminal:

```bash
./gradlew assembleDebug
```

On Windows:

```powershell
gradlew.bat assembleDebug
```

## 6. How to run the app and backend together

For a full local workflow:

1. Start the backend on `localhost:8000`
2. Launch Android Studio and run the app on an emulator/device
3. Use the correct backend URL from the device/client environment

Important networking notes:

- For Android Emulator, use `10.0.2.2` instead of `localhost`
- For a physical device, use the computer's local IP address
- Example emulator URL: `http://10.0.2.2:8000`
- Example physical device URL: `http://192.168.1.25:8000`

Current repo status:

- Backend is runnable as a FastAPI app
- Android app shell is present and launchable
- App-to-backend integration may still require additional client-side networking code depending on the feature phase

## 7. Environment variables and API key setup

At the moment, the repository does not contain a required `.env` file or explicit secret loader. The backend is currently minimal and does not require mandatory environment variables to start.

But for future integrations and production usage, common variables may include:

```env
APP_ENV=development
MODEL_PROVIDER=openai
OPENAI_API_KEY=your_key_here
API_BASE_URL=http://localhost:8000
```

Best practices:

- Keep secrets outside the repo
- Use `.env` locally only
- Add `.env.example` for collaborators
- Never commit real credentials to GitHub

## 8. API usage examples

The backend currently provides router endpoints under `backend/api/routes/`.

### 8.1 Root endpoint

```bash
curl http://localhost:8000/
```

Example response:

```json
{
  "name": "VHOTIEX AI",
  "status": "running",
  "version": "0.1.0"
}
```

### 8.2 List available agents

```bash
curl http://localhost:8000/agents/
```

Example response:

```json
{
  "agents": [
    {
      "name": "Astra",
      "role": "Coordinator",
      "specialties": ["planning", "alignment", "handoff"]
    },
    {
      "name": "Nova",
      "role": "Researcher",
      "specialties": ["research", "analysis", "fact-checking"]
    }
  ],
  "recommended_default": "Astra"
}
```

### 8.3 Get a single agent profile

```bash
curl http://localhost:8000/agents/Astra
```

### 8.4 Send a chat request

```bash
curl -X POST http://localhost:8000/chat/ \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Plan a roadmap for my AI app launch",
    "agent": "Astra"
  }'
```

Example response:

```json
{
  "status": "accepted",
  "message": "Plan a roadmap for my AI app launch",
  "agent": "Astra",
  "model": "gpt-orchestrator",
  "role": "Coordinator",
  "response": "Astra here. I am handling this in coordinator mode...",
  "personality": {
    "name": "Astra",
    "role": "Coordinator"
  }
}
```

## 9. Testing and debugging guide

### 9.1 Backend testing

Use curl or Postman to call the endpoints directly:

```bash
curl http://localhost:8000/agents/
curl http://localhost:8000/chat/ -H "Content-Type: application/json" -d '{"message":"hello","agent":"Astra"}'
```

Check the server logs in the terminal running Uvicorn.

### 9.2 Android testing

Use Android Studio:

- Logcat for runtime logs
- Emulator/device selection for validation
- Gradle sync output for build issues

### 9.3 Recommended smoke tests

1. Run backend and confirm `/` responds
2. Call `/agents/`
3. Call `/chat/` with a simple message
4. Start Android app and check it launches
5. Verify app build completes without Gradle errors

## 10. Troubleshooting

### 10.1 Python import errors

Symptom: `ModuleNotFoundError` or package errors.

Fix:

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn
```

### 10.2 Backend not reachable

Symptom: browser or curl cannot connect to the API.

Fix:

- Confirm the backend is running
- Check the port is free
- Try `http://localhost:8000/`
- For Android emulator, use `10.0.2.2:8000`
- For physical device, use the local IP of the development machine

### 10.3 Gradle sync issues

Symptom: Android Studio cannot sync the project.

Fix:

- Ensure JDK 17 is selected
- Go to `File -> Project Structure -> SDK Location`
- Invalidate cache and restart Android Studio if needed
- Open the repo root, not a child folder

### 10.4 App crashes on startup

Symptom: app builds but crashes in the emulator/device.

Fix:

- Check `AndroidManifest.xml`
- Verify `MainActivity` exists and is declared
- Inspect Logcat output for runtime exceptions
- Confirm the emulator satisfies the app's Android requirements

### 10.5 API response is wrong or empty

Symptom: incorrect payload or no response.

Fix:

- Ensure JSON body contains `message`
- Verify correct route path and HTTP method
- Check backend logs for exceptions
- Test with a simple payload first

## 11. Recommended next steps

1. Add a real `requirements.txt` for backend dependencies
2. Add `.env.example` for environment configuration
3. Connect the Android app to the backend API layer
4. Add unit tests for routes and agent selection
5. Add a clear setup section to the main README

## 12. Summary

This repo already contains strong architecture and product planning documents, but it lacked an actionable developer onboarding guide. This document fills that gap with local setup steps, backend instructions, Android run steps, API examples, and troubleshooting guidance.

For more product context, also review:

- `README.md`
- `ARCHITECTURE.md`
- `APP_FLOW.md`
- `BACKEND_SCHEMA.md`
- `DESIGN.md`
- `IMPLEMENTATION_PLAN.md`
