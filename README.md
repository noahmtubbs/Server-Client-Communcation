# 🔗 Server-Client Communication (Python Sockets)

**Author**: Noah Tubbs

A simple Python-based socket communication project that enables basic messaging between a macOS server and a Windows client. This setup demonstrates how to establish a cross-platform connection using Python's built-in `socket` library.

---

## 🧰 Project Overview

This project consists of two scripts:

- `user1_server.py`: Acts as the server, running on a macOS machine.
- `user2_client.py`: Acts as the client, running on a Windows machine.

The server listens for incoming connections and messages from the client, facilitating a basic chat-like interaction between the two systems.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on both macOS and Windows machines.
- Both machines connected to the same network.

### Setup Instructions

1. **On the macOS machine (Server):**
   - Open Terminal.
   - Navigate to the directory containing `user1_server.py`.
   - Run the server script:
     ```bash
     python3 user1_server.py
     ```

2. **On the Windows machine (Client):**
   - Open Command Prompt.
   - Navigate to the directory containing `user2_client.py`.
   - Run the client script:
     ```bash
     python user2_client.py
     ```

3. **Interaction:**
   - Once both scripts are running, you can send messages from the client to the server.
   - The server will display received messages and can be modified to send responses.

---

## 🔍 Features

- Establishes a TCP connection between two machines.
- Facilitates message sending from client to server.
- Demonstrates basic socket programming concepts in Python.
- Cross-platform compatibility between macOS and Windows.

---

## 📂 File Structure

```
Server-Client-Communcation/
├── user1_server.py   # Server script for macOS
└── user2_client.py   # Client script for Windows
```

---

## 📝 Notes

- This project is intended for educational purposes to demonstrate basic socket communication.
- For real-world applications, consider implementing additional features such as:
  - Error handling and reconnection logic.
  - Secure communication using SSL/TLS.
  - Message formatting protocols (e.g., JSON).
  - GUI interfaces for user-friendly interaction.

---

## 📬 Contact

For questions or suggestions, feel free to reach out:

- GitHub: [noahmtubbs](https://github.com/noahmtubbs)
