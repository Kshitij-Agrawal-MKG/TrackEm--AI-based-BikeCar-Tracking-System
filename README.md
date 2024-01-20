# TrackEm - AI-based Bike/Car Tracking System

TrackEm is an advanced vehicle tracking system that utilizes YOLO v8 and OpenCV for real-time vehicle detection, precise OCR for license plates, and robust criminal database cross-referencing. It also provides automated alerts via Gmail API and Telegram API.

## Features

- Real-time vehicle detection using YOLO v8 and OpenCV
- Precise OCR for license plate recognition
- Integration with criminal databases for cross-referencing
- Automated alerts via Gmail API and Telegram API

## Getting Started

### Prerequisites

Make sure you have the following prerequisites installed:

- Python (version 3.x)
- YOLO v8 (from Ultralytics)
- OpenCV
- EasyOCR
- SSL
- smtplib
- csv
- email (from requests)
- requests
- string

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/TrackEm-AI-Based-Tracking.git
    ```

2. Navigate to the project directory:

    ```bash
    cd TrackEm-AI-Based-Tracking
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up Gmail API credentials:

    - Follow the [Gmail API Python Quickstart](https://developers.google.com/gmail/api/quickstart) to obtain the credentials file.
    - Save the credentials in message.py file in the project directory.

5. Set up Telegram API credentials:

    - Create a Telegram bot using the [BotFather](https://core.telegram.org/bots#botfather).
    - Save the credentials in message.py file in the project directory.

6. Configure other project settings:

    - Edit the configuration files or set environment variables as needed.

7. Start the application:

    ```bash
    python trackem.py
    ```

## Usage

To use TrackEm, follow these steps:

1. Run the application using the provided command.
2. The system will start real-time vehicle detection and license plate recognition.
3. Alerts will be sent via Gmail and Telegram in case of suspicious vehicles.

## Acknowledgments

- YOLO v8 Contributors
- OpenCV Contributors
- EasyOCR Contributors
- Gmail API Developers
- Telegram API Developers
- Requests Developers
