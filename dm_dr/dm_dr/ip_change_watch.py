import socket
import signal
import sys
from datetime import datetime
import time


def resolve_dns(host):
    time = datetime.time(datetime.now())
    print("{0}: {1} resolves to {2} ".format(time.isoformat(),
                                             host,
                                             socket.gethostbyname(host))) # your os sends out a dns query

print ("Press CTRL+C to end")

try:
    while True:
        resolve_dns("www.docmagic.com")
        resolve_dns("www.loan-magic.com")
        resolve_dns("smartclose.docmagic.com")
        resolve_dns("download.docmagic.com")
        resolve_dns("www.documentexpressinc.com")
        print("")
        time.sleep(15)  # Delay for 1 minute (5 seconds)
except KeyboardInterrupt:
    # Catch a CTRL+C to end this loop
    # https://stackoverflow.com/questions/13180941/how-to-kill-a-while-loop-with-a-keystroke
    pass
