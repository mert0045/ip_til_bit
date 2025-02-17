import tkinter as tk
from tkinter import messagebox

def ip_til_binær(ip):
    """Konverterer en IP-adresse til binær."""
    if not valider_ip(ip):
        return "Ugyldig IP"
    return '.'.join(f"{int(oktant):08b}" for oktant in ip.split("."))

def valider_ip(ip):
    """Tjekker om en given IP-adresse er gyldig."""
    oktanter = ip.split(".")
    return len(oktanter) == 4 and all(oktant.isdigit() and 0 <= int(oktant) <= 255 for oktant in oktanter)

def tæl_1_ere_i_subnetmaske(subnetmaske):
    """Tæller antallet af 1'ere i en subnetmaske."""
    return ip_til_binær(subnetmaske).replace('.', '').count('1')

def anvend_subnetmaske(ip, subnetmaske):
    """Finder netværksadressen ved at udføre en bitwise ANDing metoden mellem IP og subnetmaske."""
    bin_ip = ''.join(f"{int(oktant):08b}" for oktant in ip.split("."))
    bin_subnet = ''.join(f"{int(oktant):08b}" for oktant in subnetmaske.split("."))
    net_adresse = ''.join('1' if bin_ip[i] == '1' and bin_subnet[i] == '1' else '0' for i in range(32))
    return '.'.join(str(int(net_adresse[i:i+8], 2)) for i in range(0, 32, 8))

def er_samme_netværk(ip1, ip2, subnetmaske):
    """Tjekker om to IP-adresser er på samme netværk."""
    return anvend_subnetmaske(ip1, subnetmaske) == anvend_subnetmaske(ip2, subnetmaske)

def check_network():
    """Tjekker om IP-adresserne er på samme netværk og viser en besked."""
    ip1 = entry_ip1.get()
    ip2 = entry_ip2.get()
    subnet = entry_subnet.get()
    
    if not (valider_ip(ip1) and valider_ip(ip2) and valider_ip(subnet)):
        messagebox.showerror("Fejl", "Indtast gyldige IP-adresser og subnetmaske.")
        return

    same_network = er_samme_netværk(ip1, ip2, subnet)
    bits = tæl_1_ere_i_subnetmaske(subnet)
    msg = f"IP-adresserne er {'på samme netværk' if same_network else 'ikke på samme netværk (kræver gateway)'}.\nAntal bits i subnetmasken: {bits}"
    messagebox.showinfo("Resultat", msg)

def update_labels(*args):
    """Opdaterer labels med binære værdier, når input ændres."""
    ip1 = entry_ip1.get()
    ip2 = entry_ip2.get()
    subnet = entry_subnet.get()
    
    if valider_ip(ip1):
        label_ip1_bin.config(text=ip_til_binær(ip1))
    if valider_ip(ip2):
        label_ip2_bin.config(text=ip_til_binær(ip2))
    if valider_ip(subnet):
        label_subnet_bin.config(text=ip_til_binær(subnet))

# Opret GUI-vinduet
root = tk.Tk() # Opret vindue
root.title("Netværkskontrol") # Titel
root.geometry("425x300") # Størrelse
root.configure(bg="#2E2E2E") # Baggrundsfarve

# Farver
label_fg = "#FFFFFF" # Tekstfarve
entry_bg = "#3C3C3C" # Inputbaggrund
entry_fg = "#FFFFFF" # Inputtekstfarve
button_bg = "#555555" # Knapbaggrund
button_fg = "#FFFFFF" # Knaptekstfarve

# Subnetmaske
tk.Label(root, text="Subnetmaske:", font=("Arial", 12), bg="#2E2E2E", fg=label_fg).grid(row=0, column=0, padx=10, pady=5)
entry_subnet = tk.Entry(root, font=("Arial", 12), bg=entry_bg, fg=entry_fg) # Inputfelt
entry_subnet.grid(row=0, column=1, padx=10, pady=5) # Placering af inputfelt
label_subnet_bin = tk.Label(root, text="00000000.00000000.00000000.00000000", font=("Arial", 10), bg="#2E2E2E", fg=label_fg) # Label til binær værdi
label_subnet_bin.grid(row=1, column=1) # Placering af label

# IP 1
tk.Label(root, text="IP-adresse 1:", font=("Arial", 12), bg="#2E2E2E", fg=label_fg).grid(row=2, column=0, padx=10, pady=5)
entry_ip1 = tk.Entry(root, font=("Arial", 12), bg=entry_bg, fg=entry_fg)
entry_ip1.grid(row=2, column=1, padx=10, pady=5)
label_ip1_bin = tk.Label(root, text="00000000.00000000.00000000.00000000", font=("Arial", 10), bg="#2E2E2E", fg=label_fg)
label_ip1_bin.grid(row=3, column=1)

# IP 2
tk.Label(root, text="IP-adresse 2:", font=("Arial", 12), bg="#2E2E2E", fg=label_fg).grid(row=4, column=0, padx=10, pady=5)
entry_ip2 = tk.Entry(root, font=("Arial", 12), bg=entry_bg, fg=entry_fg)
entry_ip2.grid(row=4, column=1, padx=10, pady=5)
label_ip2_bin = tk.Label(root, text="00000000.00000000.00000000.00000000", font=("Arial", 10), bg="#2E2E2E", fg=label_fg)
label_ip2_bin.grid(row=5, column=1)

# Knap
tk.Button(root, text="Kontroller netværk", command=check_network, font=("Arial", 12, "bold"), bg=button_bg, fg=button_fg).grid(row=6, columnspan=2, pady=10)

# Smiley
label_smiley = tk.Label(root, text="😊", font=("Arial", 20), bg="#2E2E2E", fg=label_fg)
label_smiley.grid(row=7, columnspan=2, pady=10)

# Bind inputfelter til opdateringsfunktionen
entry_ip1.bind("<KeyRelease>", update_labels)
entry_ip2.bind("<KeyRelease>", update_labels)
entry_subnet.bind("<KeyRelease>", update_labels)

# Start GUI
root.mainloop()