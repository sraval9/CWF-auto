import time,datetime, subprocess

def main():
    datedir = datetime.date.today().isoformat()
    datedir = datedir.replace('-','')
    timedir = datetime.datetime.now().time().isoformat(timespec = 'minutes')
    timedir = timedir.replace(':','')
    capture_filter = 'CWAG'

    output_filename_CWAG_flows = '/home/octeam/Logs/CWAG1/' + datedir + '_' + timedir
    #output_filename_CWAG2 = '/home/octeam/Logs/CWAG2/' + datedir + '_' + timedir
    output_filename_fw_flows = '/home/octeam/Logs/FeG1/' + datedir + '_' + timedir
    #output_filename_FeG2 = '/home/octeam/Logs/FeG2/' + datedir + '_' + timedir

    #CWAG_filter = '\"\'port 1812 or port 67 or port 68 or port 9109\'\"'

    tshark_command_CWAG_flows = 'ssh adminfb@10.22.2.127 sudo tcpdump -i any -G 900 -W 1 -U -w - \'udp and port 2041\' > ' + output_filename_CWAG_flows + '.pcap'
    #tshark_command_CWAG2 = 'ssh testuser@10.22.22.49 sudo tcpdump -i any -G 900 -W 1 -U -w - \'port 1812 or port 1813 or port 67 or port 68 or port 9109 or port 8443 or port 50065\' > ' + output_filename_CWAG2 + '.pcap'
    tshark_command_fw_flows = 'ssh adminfb@10.22.2.126 sudo tcpdump -i any -G 900 -W 1 -U -w - \'udp and port 2042\' > ' + output_filename_fw_flows + '.pcap'
    #tshark_command_FeG2 = 'ssh testuser@10.22.22.122 sudo tcpdump -i any -G 900 -W 1 -U -w - \'port 3868\' > ' + output_filename_FeG2 + '.pcap'
    kill_tcpdump = 'ssh testuser@10.22.22.121 sudo killall tcpdump'
    k1 = subprocess.Popen(kill_tcpdump, shell = True)
    time.sleep(1)
    #FeG_filter = 'port 3868'

    #tshark -i any -w /tmp/new.pcap -f "port 1812 or port 67 or port 68 or port 9109" -t ad -a duration:60
    #tshark_command = 'tshark -i any -w /tmp/' + output_filename + '.pcap -f ' + filter + ' -t ad -a duration:60'
    #tshark_command = 'ssh testuser@10.22.22.109 sudo tshark -i any -t ad -a duration:60 -f ' + filter + ' > /home/octeam/' + output_filename + '.pcap'
    #print(tshark_command)
    p1 = subprocess.Popen(tshark_command_CWAG_flows, shell = True)
    #p2 = subprocess.Popen(tshark_command_CWAG2, shell = True)
    #k1 = subprocess.Popen(kill_tcpdump, shell = True)
    p3 = subprocess.Popen(tshark_command_fw_flows, shell = True)
    #p4 = subprocess.Popen(tshark_command_FeG2, shell = True)

    symlink1 = 'ln -s ' + output_filename_CWAG_flows + '.pcap /var/www/html/Logs/Flows/CWAG'
    #symlink2 = 'ln -s ' + output_filename_CWAG2 + '.pcap /var/www/html/Logs/CWAG2/'
    symlink3 = 'ln -s ' + output_filename_fw_flows + '.pcap /var/www/html/Logs/Flows/FW'
    #symlink4 = 'ln -s ' + output_filename_FeG2 + '.pcap /var/www/html/Logs/FeG2/'
    q1 = subprocess.run(symlink1, shell = True)
    #q2 = subprocess.run(symlink2, shell = True)
    q3 = subprocess.run(symlink3, shell = True)
    #q4 = subprocess.run(symlink4, shell = True)

if __name__ == "__main__":
    main()

