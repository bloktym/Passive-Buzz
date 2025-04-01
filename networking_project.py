import socket 

host = "255.255.255.255"
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creating the UDP socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.settimeout(0.1)
s.bind(('',port)) #binds to listen on specified port 


def main():

   
    print("Buzzer Activation System\n" +  "Choose: EMERGENCY, EXIT")

    
    try:
        while True:
            try:
                data,addr = s.recvfrom(1024) #receiving  the incoming UDP messages
                print(f"Emergency received from {addr} : {data.decode()} ")
            except socket.timeout:
                pass #this ignores timeout errors

            cmd = input("-> ").strip().upper()

            if cmd == "EMERGENCY":
                s.sendto(cmd.encode(), (host, port))
                print(f"sent {cmd} alert")
            elif cmd == "EXIT":
                print("Exiting...")
                break
            else:
                print("Invalid. Try 'EMERGENCY' or 'EXIT'")

    except KeyboardInterrupt:
        print("Exiting due to user interruption..")
            
    s.close() #closing the socket


if __name__ == "__main__":
    main()



    