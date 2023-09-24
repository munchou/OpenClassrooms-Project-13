import subprocess
from getpass import getpass

while True:
    username = input("username: ")
    password = getpass("password: ")

    connection = subprocess.run(f"docker login -u {username} -p {password}")

    if connection.returncode == 1:
        print("\nProblem while connecting, please try again.")
        continue
    elif connection.returncode == 0:
        break

print(f"\nYou are now connect as {username}")
print("Would you like to download the Docker image?")
dl_img = input('Type "y" to download, anything else to exit: ')

while True:
    if dl_img.casefold() == "y":
        subprocess.run("docker pull munchou/munchou_oc_p13:latest")
        break
    break

print("\nDisconnecting...\n")
subprocess.run("docker logout")
