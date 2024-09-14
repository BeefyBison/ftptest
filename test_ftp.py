import os
import ssl
import ftplib
import sys

host = "192.168.56.101"
target_path = "/ftpfiles"
user_name = "ftpuser"
password = "password"
filename = "test.txt"

def main():

    try:
        connect = ftplib.FTP(host, user_name, password)
        connect.encoding = "utf-8"
        connect.dir()

        with open(filename, "rb") as f:
            connect.storbinary(f"STOR {filename}", f)
        connect.dir()
    except ConnectionError as ce:
        print(f"Connection failed: {ce}")
    except FileNotFoundError as fe:
        print(f"File not found: {fe}")
    except ftplib.error_perm as pe:
        print(f"Permanent error found: {pe}")
    except ftplib.error_temp as te:
        print(f"Temporary error found: {te}")
    except ftplib.all_errors as alle:
        print(f"Unknown ftp related error: {alle}")
    except ftplib.error_reply as er:
        print(f"An error has occurred in the reply: {er}")
    except:
        print(f"An unexpected error has occurred")

    finally:
        connect.quit()

if __name__ == "__main__":
    main()
