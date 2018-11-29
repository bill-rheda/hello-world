#This is a client script meant to check the TCP connection with its server and return a result
import socket
import sys
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
output1 = "OK, CONNECTION SUCCEEDED"
output2 ="NOT OK, CONNECTION FAILED"

def check_tcp_connection(IP):#This defines the function that connects the client to the server.The function has as parameter the IP of the server
    port = 8443
    try:
        client.connect(('IP', port))
        return output1 
    except socket.error:
        return output2 
check_tcp_connection('0.0.0.0')#This function only test the connection and returns either output one or two but does not print out the result


def test_case(IP):#This is a test for the function above.It has as parameter the IP of server and prints out the result from the test
    if (check_tcp_connection(IP) == output1):#if your client is connected to your server, then this would be printed on your screen
        print ("Checking the connectivity......................................OK! CONNECTION SUCCEEDED")
    else:#if not, it indicates that your I is not connected to the server and would have this printed on your screen
        print("Checking the connectivity......................................NOT OK! CONNECTION FAILED")
test_case('0.0.0.0')


def send_sms(IP):#This function sends mesages to the IP of the server given that the connection has been established
    message ="Hey! How are you doing? From FRIEDASMS Ltd"
    try:
        client.sendall(message)#If a connection is established, then the message above would be sent to your server
    except:
        print ("ERROR IN SENDING MESSAGE")#If no connection exist, then the mesage would not be sent and "ERROR IN SENDING MESSAGE" would be displayed on your screen
send_sms('0.0.0.0')




    

   




    

