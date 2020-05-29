import subprocess

##############
# MAIN
##############

def main():
    all_cmds = ['ssh-keygen -R 10.22.22.47',
    'ssh-keygen -R 10.22.22.48',
    'ssh-keygen -R 10.22.22.49',
    'ssh-keygen -R 10.22.22.121',
    'ssh-keygen -R 10.22.22.122',
    'sshpass -p testuser ssh-copy-id testuser@10.22.22.47',
    'sshpass -p testuser ssh-copy-id testuser@10.22.22.48',
    'sshpass -p testuser ssh-copy-id testuser@10.22.22.49',
    'sshpass -p testuser ssh-copy-id testuser@10.22.22.121',
    'sshpass -p testuser ssh-copy-id testuser@10.22.22.122']

for cmd in all_cmds:
    run_cmd = subprocess.Popen(cmd, shell=True)

if __name__ == "__main__":
    main()

