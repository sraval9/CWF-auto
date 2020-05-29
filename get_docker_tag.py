import subprocess

def main():
    cwag2_tag_file = '/home/octeam/cwag2_tag.txt'
    cwag1_tag_file = '/home/octeam/cwag1_tag.txt'
    cwag2_cmd = 'ssh testuser@10.22.22.49 "cd /var/opt/magma/docker && sudo docker ps | grep magmad" > /home/octeam/cwag2_tag.txt'
    cwag1_cmd = 'ssh testuser@10.22.22.48 "cd /var/opt/magma/docker && sudo docker ps | grep magmad" > /home/octeam/cwag1_tag.txt'
    p1 = subprocess.Popen(cwag1_cmd, shell = True)
    p2 = subprocess.Popen(cwag2_cmd, shell = True)
    join_line = ''

    with open(cwag2_tag_file, 'r') as f1:
        lines = f1.readline()
        #print (lines)
        for line in lines:
            #if 'magma' in line:
                #print ('Here')
            #print (line)
            #a = line.split(':')
            #tag = a[1][:8]
            #print (tag)
            join_line = join_line + line
        print (join_line)
        a = join_line.split(':')
        cwag2_tag = a[1][:8]
        print (cwag2_tag)
    with open(cwag1_tag_file, 'r') as f1:
        lines = f1.readline()
        #print (lines)
        for line in lines:
            #if 'magma' in line:
                #print ('Here')
            #print (line)
            #a = line.split(':')
            #tag = a[1][:8]
            #print (tag)
            join_line = join_line + line
        print (join_line)
        a = join_line.split(':')
        cwag1_tag = a[1][:8]
        print (cwag1_tag)
    return cwag1_tag,cwag2_tag


if __name__ == "__main__":
    main()

