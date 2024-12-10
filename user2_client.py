import socket
    # connect to mac's port definition
def start_client():
    print("Starting client...")
    host = '**.*.*.***'  # Put Macbook's ip
    port = 5075  # Server's port


    # connects to mac's ip
    try:
        print(f"Connecting to {host}:{port}...")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        chat_loop(client_socket)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()
        print("Connection closed.")

# chat loop between computers
def chat_loop(client_socket):
    print("Chat loop started.")
    try:
        while True:
            message = input("You: ").strip()
            client_socket.send((message + "#").encode()) # add # to end chat and send to next person
            if message.lower() == "exit":
                print("You ended the chat.")
                break

            data = client_socket.recv(1024).decode().strip("#")
            if not data or data.lower() == "exit":
                print("User1 has ended the chat.")
                break

            print(f"User1: {data}")
    except Exception as e:
        print(f"Chat error: {e}")

if __name__ == "__main__":
    start_client()
