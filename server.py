#serv

import socket

def main():
    client_ip = input("Enter client IP to connect: ")
    PORT = 26574

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((client_ip, PORT))
    print(f"[+] Connected to {client_ip}:{PORT}")

    try:
        while True:
            cmd = input("Command> ")
            if not cmd.strip():
                continue

            client.sendall(cmd.encode())

            if cmd.strip().lower() == 'exit':
                print("[+] Exiting.")
                break

            data = client.recv(4096)
            print(data.decode('utf-8', errors='replace'))
    finally:
        client.close()

if __name__ == "__main__":
    main()
