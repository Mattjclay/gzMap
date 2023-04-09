# Brents Linode Server - Hack it if you can
testing_ip = "139.144.38.7"

# Add ; python gzmap to the end of the command to run gzmap after the command finishes
nmap_options = {
    "Nmap": "nmap",
    "placeholder2": "placeholder2",
    "placeholder3": "placeholder3",
    "placeholder4": "placeholder4",
    "placeholder5": "placeholder5",
    "placeholder6": "placeholder6",
    "placeholder7": "placeholder7",
    "exit": "placeholder8", 
}

directory_enumeration_options = {
    "List Directories": "ls -lah",
    "placeholder2": "placeholder2",
    "placeholder3": "placeholder3",
    "placeholder4": "placeholder4",
    "placeholder5": "placeholder5",
    "placeholder6": "placeholder6",
    "placeholder7": "placeholder7",
    "exit": "placeholder8", 
}

def get_options(action):
    match action:
        case "Nmap":
            return nmap_options
        case "Directory Enumeration":
            return directory_enumeration_options
        case _:
            return None
    
    

    