import socket

host = input("Please enter the host IP address: ")
port= int(input("Please enter port number: "))

def send_command(command):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        try:
            s.settimeout(5.0)

            s.connect((host, port))
            print(f"Connected to {host}:{port}")

            s.sendall(command.encode()) #converts to bytes
            print(f"Sent {command}")
            response = s.recv(1024).decode() #receives the data
            print(f"Response from Server: {response}")

       
        except ConnectionRefusedError:
            print("Error occurred: Server not running or connection refused")

        except Exception as e:
            print(f"Unexpected error: {e}")  #general error

def main():
    print("Buzzer Activation System")
    print("Choose: ACTIVATE, DEACTIVATE, EXIT\n")

    while True:

        cmd = input("-> ").strip().upper()

        if cmd == "EXIT":
            print("Exiting..")
            break
        elif cmd in ("ACTIVATE", "DEACTIVATE"):
            send_command(cmd)
        else:
            print("Invalid command. Try using 'ACTIVATE', 'DEACTIVATE', or 'EXIT' ")

if __name__ == "__main__":
    main()
