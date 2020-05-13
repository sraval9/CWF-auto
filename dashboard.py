import datetime, subprocess

def writeKPI(date1,time1, kpi_CWAG1, kpi_CWAG2):
    #base_path = '/Users/sraval/Documents/Old_docs/FB_SFE/'
    #base = '/home/octeam/Logs/'
    #CWAG2_html_file = base + 'CWAG2/' + date1 + '_dashboard_test.html'
    #symlink_CWAG2_html = 'ln -s ' + CWAG2_html_file + ' /var/www/html/Logs/dashboard.html'
    #q_CWAG2_html = subprocess.run(symlink_CWAG2_html, shell = True)
    CWAG2_html_file = '/var/www/html/Logs/dashboard.html'

    html_template = '''
    <!DOCTYPE html>
    <html>
    <body>

        <table style='width:100%', border = '1'>
            <col width='10%'>
            <col width='90%'>

            <tr>
                <th>Timeslot</th>
                <th></th>
            </tr>

            <tr>
                <td>{0}</td>
                <td>
                    <table border = '1', style='width:100%'>
                        <tr>
                            <th colspan='6'>CWAG1</th>
                        </tr>
                        <tr>
                            <td>Access Req</td>
                            <td>Access Ch</td>
                            <td>Access Acpt</td>
                            <td>Access Rej</td>
                            <td>Acnt Req</td>
                            <td>Acnt Resp</td>
                        </tr>
                        <tr>
                            <td>{1}</td>
                            <td>{2}</td>
                            <td>{3}</td>
                            <td>{4}</td>
                            <td>{5}</td>
                            <td>{6}</td>
                        </tr>

                        <tr>
                            <th colspan='6'>CWAG2</th>
                        </tr>
                        <tr>
                            <td>Access Req</td>
                            <td>Access Ch</td>
                            <td>Access Acpt</td>
                            <td>Access Rej</td>
                            <td>Acnt Req</td>
                            <td>Acnt Resp</td>
                        </tr>
                        <tr>
                            <td>{7}</td>
                            <td>{8}</td>
                            <td>{9}</td>
                            <td>{10}</td>
                            <td>{11}</td>
                            <td>{12}</td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>

    </body>
    </html>
    '''

    date_time = date1 + '_' + time1
    html_string = html_template.format(date_time, kpi_table_CWAG1['Access Request'], kpi_table_CWAG1['Access Challange'], kpi_table_CWAG1['Access Accept'], kpi_table_CWAG1['Access Reject'], kpi_table_CWAG1['Accounting Request'], kpi_table_CWAG1['Accounting Response'], kpi_table_CWAG2['Access Request'], kpi_table_CWAG2['Access Challange'], kpi_table_CWAG2['Access Accept'], kpi_table_CWAG2['Access Reject'], kpi_table_CWAG2['Accounting Request'], kpi_table_CWAG2['Accounting Response'])

    with open(CWAG2_html_file, 'r+') as file2:
        old = file2.read() # read everything in the file
        file2.seek(0) # rewind
        file2.write(html_string + old)


#######################################
# MAIN
#######################################

kpi_table_CWAG1 = {'Access Request':0,
'Access Challange':0,
'Access Accept':0,
'Access Reject':0,
'Accounting Request':0,
'Accounting Response':0
}

kpi_table_CWAG2 = {'Access Request':0,
'Access Challange':0,
'Access Accept':0,
'Access Reject':0,
'Accounting Request':0,
'Accounting Response':0
}

datedir = datetime.date.today().isoformat()
datedir = datedir.replace('-','')
timedir = datetime.datetime.now().time().isoformat(timespec = 'minutes')
timedir = timedir.replace(':','')

if timedir.endswith('05'):
    #Go to prev hour
    if timedir == '0001':
        prev_timeslot = '2345'
    prev_timeslot = str(int(timedir) - 60)
else:
    prev_timeslot = str(int(timedir) - 20)

if len(prev_timeslot) == 3:
    prev_timeslot = '0' + prev_timeslot
elif len(prev_timeslot) == 2:
    prev_timeslot = '00' + prev_timeslot
elif len(prev_timeslot) == 1:
    prev_timeslot = '000' + prev_timeslot

#print(prev_timeslot)

read_CWAG1_txt= '/home/octeam/Logs/CWAG1/' + datedir + '_' + prev_timeslot + '.txt'
read_CWAG2_txt= '/home/octeam/Logs/CWAG2/' + datedir + '_' + prev_timeslot + '.txt'
read_FeG1_txt= '/home/octeam/Logs/FeG1/' + datedir + '_' + prev_timeslot + '.txt'
read_FeG2_txt= '/home/octeam/Logs/FeG2/' + datedir + '_' + prev_timeslot + '.txt'

radiusCodeArr = ['0','Access Request','Access Accept','3','Accounting Request','Accounting Response', '6', '7', '8', '9', '10', 'Access Challange']
#radiusAccountStatusTypeArr = ['0', 'Start', 'Stop', 'Interim Update']
fileArr1 = []
fileArr2 = []
fileArr3 = []
fileArr4 = []
#input_parsed_text = '/Users/sraval/Documents/Old_docs/FB_SFE/AP_Roaming_CWAG_small.txt'
with open(read_CWAG1_txt, 'r') as file1, open(read_CWAG2_txt, 'r') as file5, open(read_FeG1_txt, 'r') as file3, open(read_FeG2_txt, 'r') as file4:
    CWAG1_data = file1.readlines()
    CWAG2_data = file5.readlines()
    FeG1_data = file3.readlines()
    FeG2_data = file4.readlines()

    for line1 in CWAG1_data:
        lineArr1 = line1.split(';') # Each line split into different elements of array. Each element is one word from line.
            # Aug  6, 2019 15:59:41.915427771 PDT;10.253.1.219;10.253.1.63;(sctp);s1ap.proc;emmtype;esmtype
            ## Aug  6, 2019 15:59:41.915427771 PDT;10.253.1.219;10.253.1.63;3s1ap.proc;4emmtype;5esmtype;6contextreleasecmd;7realeasecomplete;8cntxtsetupresponse
        # Feb 18, 2020 11:30:18.934041000 PST;10.22.3.50;10.22.22.49;sll:ethertype:ip:udp:radius:eap;1
        #lineArr[3] = lineArr[3].rstrip()
        #lineArr[4] = lineArr[4].rstrip()

        if 'radius' in lineArr1[3]:
            # print(lineArr[3])
            lineArr1[3] = 'Radius-'
            #print(lineArr[4])
            lineArr1[4] = radiusCodeArr[int(lineArr1[4])]
            # lineArr1[5] = radiusCodeArr[int(lineArr1[5])]
            #print(lineArr1[4])
            fileArr1.append(lineArr1)
            #print(lineArr)

            kpi_table_CWAG1[lineArr1[4]] += 1

    for line2 in CWAG2_data:
        lineArr2 = line2.split(';') # Each line split into different elements of array. Each elemen$
            # Aug  6, 2019 15:59:41.915427771 PDT;10.253.1.219;10.253.1.63;(sctp);s1ap.proc;emmty$
            ## Aug  6, 2019 15:59:41.915427771 PDT;10.253.1.219;10.253.1.63;3s1ap.proc;4emmtype;5$
        # Feb 18, 2020 11:30:18.934041000 PST;10.22.3.50;10.22.22.49;sll:ethertype:ip:udp:radius:$
        #lineArr[3] = lineArr[3].rstrip()
        #lineArr[4] = lineArr[4].rstrip()

        if 'radius' in lineArr2[3]:
            # print(lineArr[3])
            lineArr2[3] = 'Radius-'
            #print(lineArr[4])
            lineArr2[4] = radiusCodeArr[int(lineArr2[4])]
            # lineArr[5] = radiusCodeArr[int(lineArr[5])]
            #print(lineArr[4])
            fileArr2.append(lineArr2)
            #print(lineArr)

            kpi_table_CWAG2[lineArr2[4]] += 1

print(kpi_table_CWAG1)
print(kpi_table_CWAG2)
writeKPI(datedir, prev_timeslot, kpi_table_CWAG1, kpi_table_CWAG2)
