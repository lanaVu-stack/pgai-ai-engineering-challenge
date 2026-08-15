# pgai-ai-engineering-challenge

An automated AI voice bot for testing patient-facing conversational agents.

## Overview

Hello! This project was created for the Pretty Good AI Engineering Challenge. It uses Python and Retell AI to create a simulated patient that makes outbound phone calls to a healthcare conversational agent.

The goal is to test how the agent handles realistic patient conversations and identify issues with conversation flow, turn-taking, and task completion.

## Test Scenarios

I tested 10 different phone call scenarios, including:

- Appointment scheduling
- Appointment rescheduling
- Changing an appointment date
- Asking for alternative appointment times
- Appointment cancellation
- Prescription change request
- Insurance questions
- Office hours questions
- Medication refill request
- An unclear/ambiguous patient request

Audio recordings of the calls are located in the `recordings/` folder.

Corresponding transcripts are located in the `transcripts/` folder.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/lanaVu-stack/pgai-ai-engineering-challenge.git
cd pgai-ai-engineering-challenge
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

On Windows, activate the virtual environment with:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install retell-sdk python-dotenv
```

### 4. Configure environment variables

Create a `.env` file in the project root.

An `.env.example` file is included in the repository as a template:

```env
RETELL_API_KEY=your_retell_api_key_here
RETELL_FROM_NUMBER=your_retell_phone_number_here
PGAI_TEST_NUMBER=your_test_number_here
```

Replace the placeholder values with your own Retell API key, Retell phone number, and test phone number.

The real `.env` file is excluded from Git and should not be committed because it contains private credentials.

## Running the Bot

After completing the setup and activating the virtual environment, run:

```bash
python main.py
```

The program will:

1. Load the required environment variables.
2. Connect to Retell.
3. Initiate an outbound call from the configured Retell phone number to the test number.
4. Display the resulting call ID in the terminal.

Example output:

```text
Pretty Good AI patient bot starting...
Retell API key loaded successfully!
Connecting to Retell...
Call initiated successfully!
Call ID: call_xxxxxxxxx
```

## Project Structure

```text
pgai-ai-engineering-challenge/
├── main.py
├── README.md
├── ARCHITECTURE.md
├── BUG_REPORT.md
├── .env.example
├── recordings/
│   ├── call-01-scheduling.mp3
│   ├── ...
│   └── call-10-unclear-request.mp3
└── transcripts/
    ├── call-01-scheduling.txt
    ├── ...
    └── call-10-unclear-request.txt
```

## Test Results

Ten outbound phone calls were completed to evaluate the conversational agent across different patient scenarios.

The tests focused on:

- Successful task completion
- Natural conversation flow
- Turn-taking behavior
- Handling interruptions
- Clarifying ambiguous requests
- Handling scheduling and administrative questions

The call recordings and transcripts are included in this repository so the test results can be reviewed directly.

## Findings

During testing, I found that turn-taking at the beginning of calls could be challenging when the receiving system played an automated recording or language-selection message.

I adjusted the simulated patient's behavior to wait for automated opening announcements to finish before beginning the conversation. I also tested different conversation scenarios to see how the receiving agent handled both straightforward and less predictable patient requests.

More information about the issues discovered during testing is available in [`BUG_REPORT.md`](BUG_REPORT.md).

## Architecture

The project uses a small Python application to load configuration values and communicate with the Retell API. Retell provides the simulated patient voice agent and initiates outbound calls to the healthcare conversational agent.

More information about the design is available in [`ARCHITECTURE.md`](ARCHITECTURE.md).

## Security

API credentials and other private configuration values are stored locally in a `.env` file.

The `.env` file is excluded from Git and is not included in this repository. The provided `.env.example` documents the required environment variables without exposing credentials.

## Technologies Used

- Python
- Retell AI
- python-dotenv
- Git and GitHub
