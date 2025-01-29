def ip_til_binær(ip):
    oktanter = ip.split(".")
    binær_ip = '.'.join(f"{int(oktant):08b}" for oktant in oktanter)
    return binær_ip

def tæl_1_ere_i_subnetmaske(subnetmaske):
    binær_subnet = ip_til_binær(subnetmaske)
    return binær_subnet.count('1')

def anvend_subnetmaske(ip, subnetmaske):
    binær_ip = ip_til_binær(ip)
    binær_subnetmaske = ip_til_binær(subnetmaske)
    
    # Anvend bitwise AND mellem IP-adressen og subnetmasken
    netværksadresse = ''.join('1' if binær_ip[i] == '1' and binær_subnetmaske[i] == '1' else '0' 
                              for i in range(32))
    
    return netværksadresse

def er_samme_netværk(ip1, ip2, subnetmaske):
    netværks_ip1 = anvend_subnetmaske(ip1, subnetmaske)
    netværks_ip2 = anvend_subnetmaske(ip2, subnetmaske)
    
    return netværks_ip1 == netværks_ip2

def netværk_tjek():
    # Brugeren indtaster IP-adresser og subnetmaske
    ip1 = input("Indtast den første IP-adresse: ")
    ip2 = input("Indtast den anden IP-adresse: ")
    subnetmaske = input("Indtast subnetmasken: ")

    # Vis binære repræsentationer af IP-adresser og subnetmaske
    binær_ip1 = ip_til_binær(ip1)
    binær_ip2 = ip_til_binær(ip2)
    binær_subnetmaske = ip_til_binær(subnetmaske)
    
    print(f"Binær repræsentation af IP {ip1}: {binær_ip1}")
    print(f"Binær repræsentation af IP {ip2}: {binær_ip2}")
    print(f"Binær repræsentation af subnetmasken {subnetmaske}: {binær_subnetmaske}")
    
    # Tæller antallet af 1'ere i subnetmasken
    antal_1_ere_i_subnetmaske = tæl_1_ere_i_subnetmaske(subnetmaske)
    print(f"Antal 1'ere i subnetmasken: {antal_1_ere_i_subnetmaske}")
    
    # Tjek om IP-adresserne er på samme netværk
    if er_samme_netværk(ip1, ip2, subnetmaske):
        print(f"IP {ip1} og {ip2} er på samme netværk.")
    else:
        print(f"IP {ip1} og {ip2} er på forskellige netværk, sendes via gateway.")

# Kør programmet
netværk_tjek()
