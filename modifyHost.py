import platform
import os

def add_to_hosts(lines_to_add):
    # Determine the path to the host file based on the operating system
    if platform.system() == "Windows":
        host_path = os.path.join(os.environ["SystemRoot"], "System32", "drivers", "etc", "hosts")
    else:
        host_path = "/etc/hosts"

    # Open the host file and add the given lines to it
    with open(host_path, "a") as file:
        for line in lines_to_add:
            file.write(line + "\n")

lines = [
"127.0.0.1 license.worksheetcrafter.com",
"127.0.0.1 license.getschoolcraft.com"]
add_to_hosts(lines)
#permission error

'''C:\Windows\System32\drivers\etc'''
