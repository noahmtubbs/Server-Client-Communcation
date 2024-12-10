# user1_server.py
import socket

def server_program():
    host = '********'  # Put Mac's IP
    port = 5075  # Port to listen on

# create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server started on {host}:{port}. Waiting for a connection...")

    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    while True:
        # Receive data from user2
        data = conn.recv(1024).decode().strip("#")  # Remove hash delimiter
        if not data or data.lower() == "exit":
            print("User2 has ended the chat.")
            conn.send("Exit".encode())
            break
        print(f"User2: {data}")

        # Allow user1 to respond
        response = input("You: ").strip()
        conn.send((response + "#").encode())  # Add hash as delimiter
        if response.lower() == "exit":
            break

    conn.close()
    print("Connection closed.")

if __name__ == "__main__":
    server_program()
