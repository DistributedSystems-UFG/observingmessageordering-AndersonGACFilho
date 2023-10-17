#To Do: Replace all this with a naming service

# With local addresses (within the same cloud region)
#PEERS = ['172.31.78.41','172.31.65.227','172.31.74.212','172.31.75.17','172.31.72.48','172.31.75.162']

# With public addresses (in the same region of the cloud)
# The last one is not fixed and must be changed each time the lab is restarted.
PEERS_SAME_REGION = ['3.219.23.96','34.226.166.158','44.198.151.245','44.219.197.47','44.220.0.53','18.204.3.6']

# With public addresses (in two separate regions - last two servers in Oregon)
PEERS_TWO_REGIONS = ['3.219.23.96','34.226.166.158','44.198.151.245','44.219.197.47','44.239.194.163','52.88.79.71']


PEER_UDP_PORT = 4567
PEER_TCP_PORT = 5679
N = 6   # Number of peers
SERVER_ADDR ='3.219.23.96'
SERVER_PORT = 5678

