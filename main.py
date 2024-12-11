import subprocess

nw = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'])
decoded_nw = nw.decode('ascii')
print(decoded_nw)

# netsh wlan show all - detailed info on available networks