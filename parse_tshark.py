# tshark -r /Users/sraval/20190801120501.pcap -T fields -E separator=';' -E occurrence=a -e frame.time -e ip.src -e ip.dst -e sctp.chunk_type > /Users/sraval/parse_tshark.txt


#Script to parse captured pcap using tshark - running as a cron on MME

#import os,re
import datetime, subprocess
#import sftp_logs


#######################################################################################
# MAIN
#######################################################################################
datedir = datetime.date.today().isoformat()
datedir = datedir.replace('-','')
timedir = datetime.datetime.now().time().isoformat(timespec = 'minutes')
timedir = timedir.replace(':','')

if timedir.endswith('01'):
    #Go to prev hour
    if timedir == '0001':
        prev_timeslot = '2345'
    prev_timeslot = str(int(timedir) - 56)
else:
    prev_timeslot = str(int(timedir) - 16)

if len(prev_timeslot) == 3:
    prev_timeslot = '0' + prev_timeslot
elif len(prev_timeslot) == 2:
    prev_timeslot = '00' + prev_timeslot
elif len(prev_timeslot) == 1:
    prev_timeslot = '000' + prev_timeslot

print(prev_timeslot)

#read_file = '/Users⁩/⁨sraval⁩/⁨Documents⁩/⁨Old docs⁩/⁨FB_SFE⁩/' + datedir + '/' + prev_timeslot
#CWAG2
read_CWAG1_pcap = '/home/octeam/Logs/CWAG1/' + datedir + '_' + prev_timeslot + '.pcap'
read_CWAG2_pcap = '/home/octeam/Logs/CWAG2/' + datedir + '_' + prev_timeslot + '.pcap'
read_FeG1_pcap = '/home/octeam/Logs/FeG1/' + datedir + '_' + prev_timeslot + '.pcap'
read_FeG2_pcap = '/home/octeam/Logs/FeG2/' + datedir + '_' + prev_timeslot + '.pcap'

#read_file = '/Users/sraval/Downloads/20200218_113001_2.pcap'
output_CWAG1_text_filename = read_CWAG1_pcap.replace('pcap', 'txt')
output_CWAG2_text_filename = read_CWAG2_pcap.replace('pcap', 'txt')
output_FeG1_text_filename = read_FeG1_pcap.replace('pcap', 'txt')
output_FeG2_text_filename = read_FeG2_pcap.replace('pcap', 'txt')

'''
datedir = datetime.date.today().isoformat()
datedir = datedir.replace('-','')
timedir = datetime.datetime.now().time().isoformat(timespec = 'seconds')
timedir = timedir.replace(':','')

output_filename = datedir + timedir
'''

CWAG_fields = '-e frame.time -e ip.src -e ip.dst -e frame.protocols -e radius.code -e radius.Acct_Status_Type' # -e dhcp.option.dhcp'

CWAG1_tshark_command = 'tshark -r ' + read_CWAG1_pcap + ' -T fields -E separator=";" -E occurrence=a ' + CWAG_fields + ' > ' + output_CWAG1_text_filename
CWAG2_tshark_command = 'tshark -r ' + read_CWAG2_pcap + ' -T fields -E separator=";" -E occurrence=a ' + CWAG_fields + ' > ' + output_CWAG2_text_filename
FeG1_tshark_command = 'tshark -r ' + read_FeG1_pcap + ' -T fields -E separator=";" -E occurrence=a -e frame.time -e ip.src -e ip.dst -e frame.protocols -e diameter.cmd.code -e diameter.flags.request > '+ output_FeG1_text_filename
FeG2_tshark_command = 'tshark -r ' + read_FeG2_pcap + ' -T fields -E separator=";" -E occurrence=a -e frame.time -e ip.src -e ip.dst -e frame.protocols -e diameter.cmd.code -e diameter.flags.request > '+ output_FeG2_text_filename

#print(tshark_command)
p1 = subprocess.run(CWAG1_tshark_command, shell = True)
p2 = subprocess.run(CWAG2_tshark_command, shell = True)
p3 = subprocess.run(FeG1_tshark_command, shell = True)
p4 = subprocess.run(FeG2_tshark_command, shell = True)

symlink1 = 'ln -s ' + output_CWAG1_text_filename + ' /var/www/html/Logs/CWAG1/'
symlink2 = 'ln -s ' + output_CWAG2_text_filename + ' /var/www/html/Logs/CWAG2/'
symlink3 = 'ln -s ' + output_FeG1_text_filename + ' /var/www/html/Logs/FeG1/'
symlink4 = 'ln -s ' + output_FeG2_text_filename + ' /var/www/html/Logs/FeG2/'
q1 = subprocess.run(symlink1, shell = True)
q2 = subprocess.run(symlink2, shell = True)
q3 = subprocess.run(symlink3, shell = True)
q4 = subprocess.run(symlink4, shell = True)


