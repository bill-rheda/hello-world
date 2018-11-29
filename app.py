import socket
import sys
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
output1 = "OK, CONNECTION SUCCEEDED"
output2 ="NOT OK, CONNECTION FAILED"

def check_tcp_connection(IP):
    port = 8443
    try:
        client.connect(('IP', port))
        return output1 
    except socket.error:
        return output2 
check_tcp_connection('0.0.0.0')


def test_case(IP):
    if (check_tcp_connection(IP) == output1):
        print ("Checking the connectivity......................................OK! CONNECTION SUCCEEDED")
    else:
        print("Checking the connectivity......................................NOT OK! CONNECTION FAILED")
test_case('0.0.0.0')


def send_sms(IP):
    message ="Hey! How are you doing? From FRIEDASMS Ltd"
    try:
        client.sendall(message)
    except:
        print ("ERROR IN SENDING MESSAGE")
send_sms('0.0.0.0')




    

   




    

