# Bug Report

## 1. Conversation context unexpectedly resets during appointment scheduling

**Severity:** Medium

**Call:** Call 01 — Routine Appointment Scheduling

**Details:**  
During the appointment-scheduling conversation, the receptionist stated that it would check available appointment times. Instead of returning availability, it unexpectedly stated that a patient profile had been created, supplied an incorrect demo date of birth, and asked "How can I help you today?" again.

The simulated patient corrected the date of birth and repeated the appointment request, after which the conversation recovered successfully.

**Why this matters:**  
The response appears to lose the current conversational state and partially restart the workflow. A real patient could interpret this as the system forgetting information already discussed or linking the conversation to incorrect patient information.

**Expected behavior:**  
After saying that appointment availability is being checked, the agent should continue the scheduling workflow and present available times without resetting the conversation or introducing unrelated patient-profile information.

---

## 2. Early turn-taking issue during automated opening message

**Severity:** Low

**Calls:** Early scheduling/rescheduling calls

**Details:**  
During early test calls, the simulated patient began speaking while the medical practice's automated recording and language-selection announcement were still playing.

**Iteration:**  
I lowered response eagerness and interruption sensitivity, changed the welcome behavior so the remote side speaks first, and added explicit prompt instructions to wait until automated announcements finish.

Later calls showed clean turn-taking at the beginning of the conversation.

## Summary

Across the 10 test calls, the conversational agent generally completed the requested tasks successfully. The most significant issue observed was an unexpected loss of conversational context during appointment scheduling.

An early turn-taking issue was also identified in the simulated patient configuration. After adjusting speech settings and prompting behavior, later calls demonstrated cleaner turn-taking during automated opening messages.

Reviewing both transcripts and call recordings was important because transcript segmentation did not always perfectly represent the timing heard in the actual audio.
