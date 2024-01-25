import socket

def whois_lookup(domain):
    
    tld = domain.split('.')[-1]
    whois_server = 'whois.iana.org'

    
    with socket.create_connection((whois_server, 43)) as sock:
       
        sock.sendall(f'{tld}\r\n'.encode('utf-8'))

        
        response = b''
        while True:
            data = sock.recv(1024)
            if not data:
                break
            response += data

    
    response_lines = response.decode('utf-8').split('\n')
    
    if len(response_lines) > 0 and ': ' in response_lines[0]:
        whois_server_info = response_lines[0].split(': ')[1].strip()
        print(f'Whois Server: {whois_server_info}\n')

    
    print(response.decode('utf-8'))


domain_name = input("Enter a domain name: ")
whois_lookup(domain_name)
