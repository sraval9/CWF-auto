import subprocess

CWAG_fields = '-e frame.time -e ip.src -e ip.dst -e frame.protocols -e radius.code -e radius.Acct_Status_Type -e dhcp.option.dhcp'
read_CWAG1_pcap = 'CWAG_small.pcapng'
output_CWAG1_text_filename = 'sandbox_parse.txt'
CWAG1_tshark_command = 'tshark -r ' + read_CWAG1_pcap + ' -T fields -E separator=";" -E occurrence=a ' + CWAG_fields + ' > ' + output_CWAG1_text_filename
p1 = subprocess.run(CWAG1_tshark_command, shell = True)
