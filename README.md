# pgai-ai-engineering-challenge

An automated AI voice bot for testing patient-facing conversational agents.

## Overview

This project was created for the Pretty Good AI Engineering Challenge. It uses Python and Retell AI to create a simulated patient that makes outbound phone calls to a healthcare conversational agent.

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
git clone <repository-url>
cd pgai-ai-engineering-challenge