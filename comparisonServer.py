from socket import *
import pickle
from constMP import *
import time
import sys

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('0.0.0.0', SERVER_PORT))
serverSock.listen(6)

def mainLoop():
	cont = 1
	while 1:
		(mode,nMsgs) = promptUser()
		peerList = PEERS_SAME_REGION if mode == 'l' else PEERS_TWO_REGIONS
		startPeers(peerList,mode,nMsgs)
		if nMsgs == 0:
			break
		print('Now, wait for the message logs from the communicating peers...')
		waitForLogsAndCompare(nMsgs)
	serverSock.close()

def promptUser():
	mode =''
	while (mode != 'l' and mode != 'r' and mode != '0'):
		mode = input('Enter mode: l=local region -or- r=remote region => ')
	nMsgs = int(input('Enter the number of messages for each peer to send (0 to terminate)=> '))
	return (mode,nMsgs)

def startPeers(peerList,mode,nMsgs):
	# Connect to each of the peers and send the 'initiate' signal:
	peerNumber = 0
	for peer in peerList:
		clientSock = socket(AF_INET, SOCK_STREAM)
		clientSock.connect((peerList[peerNumber], PEER_TCP_PORT))
		msg = (peerNumber,mode,nMsgs)
		msgPack = pickle.dumps(msg)
		clientSock.send(msgPack)
		msgPack = clientSock.recv(512)
		print(pickle.loads(msgPack))
		clientSock.close()
		peerNumber = peerNumber + 1

def waitForLogsAndCompare(N_MSGS):
	# Loop to wait for the message logs for comparison:
	numPeers = 0
	msgs = [] # each msg is a list of tuples (with the original messages received by the peer processes)

	# Receive the logs of messages from the peer processes
	while numPeers < N:
		(conn, addr) = serverSock.accept()
		msgPack = conn.recv(32768)
		conn.close()
		msgs.append(pickle.loads(msgPack))
		numPeers = numPeers + 1

	unordered = 0

	# Compare the lists of messages
	for j in range(0,N_MSGS-1):
		firstMsg = msgs[0][j]
		for i in range(1,N-1):
			if firstMsg != msgs[i][j]:
				unordered = unordered + 1
				break
	
	print ('Found ' + str(unordered) + ' unordered message rounds')


# Initiate server:
mainLoop()