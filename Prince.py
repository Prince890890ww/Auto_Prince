import os
import sys
import re
import requests
import bs4
import time
import random
import json
import string
from bs4 import BeautifulSoup
from datetime import datetime
import os
print(' JOIN TELEGRAM ')
os.system('xdg-open https://t.me/trickerxx7')
import requests
if ImportError:
    os.system('pip install requests > /dev/null')
import bs4
if ImportError:
    print('\n [Ãƒâ€”] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')

def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + 'sb=' + cok['sb'] + ';' + 'fr=' + cok['fr'] + ';' + 'c_user=' + cok['c_user'] + ';' + 'xs=' + cok['xs']
    return __for


def inbox(session):
    time.sleep(1)
    ses = requests.Session()
    __ = str(time.time()).replace('.', '')[:13]
    data = ses.get(f'''https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}''').json()
    if len(data['mail_list']) != 1:
        address = data['mail_list'][0]['subject']
        session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
        return session

ugen = []
for xd in range(5000):
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice([
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'])
    if b in ('5', '6', '7', '8', '9'):
        z = random.choice([
            '0',
            '1'])
        bv = b + '.' + z + '.' + z
    bv = b
    B = [
        'GT-',
        'SM-']
    c = random.choice(B)
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    application_version = str(random.randint(111, 396)) + '.0.0.' + str(random.randrange(10, 49)) + '.' + str(random.randint(111, 396))
    V = str(random.randrange(11, 99))
    uas = f'''{aa} {bv}; {c}{d}{e}{f} Build/{d}{f}{V}{f}; wv) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uas)
    logo4 = '\n\x1b[93m     oooooooooo.   oooooooooooo oooooo     oooo \n\x1b[93m      888\'   `Y8b  `888\'     `8  `888.     .8\'  \n\x1b[93m      888      888  888           `888.   .8\'   \n\x1b[1;37m      888      888  888oooo8       `888. .8\'    \n\x1b[1;37m      888      888  888    "        `888.8\'     \n\x1b[1;32m      888     d88\'  888       o      `888\'      \n  \x1b[1;32m    o888bood8P\'   o888ooooood8       `8\'                                     \n[×]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[×]\x1b[1;32m AUTHOR       : \x1b[1;32m DEV RAHUL AARAYA\n[×]\x1b[1;32m TOOL STATUS  :\x1b[1;32m  AUTO CREATE OPEN SOURCE DEV-XD \n[×]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
    boy = [
        'Raja Khan',
        'hina Khan',
        'Dev Singh',
        'Afzal Khan',
        'Haider Khan',
        'Suleman Khan',
        'Nadeem Khan',
        'Nazeer Malik',
        'Nazeer bharat',
        'Nazeer Rehmani',
        'Safdar Malik',
        'Intzar Khan',
        'Saleem Malik',
        'Abdullah Malik',
        'Naseer jutt',
        'Muzammil Malik',
        'Fiaz Ahmad',
        'Asghar Ali',
        'Shabeer Ahmad',
        'Irfan Ali',
        'Ahmad Gujjar']
    girl = [
        'Sajida Malik',
        'Ayesha Khan',
        'Nabeela Malik',
        'Kinza Fatima',
        'Arooj Khan',
        'Muskan Khan',
        'Ayesha Malik',
        'Safina Malik',
        'Nida Ali',
        'Pooja Yadav',
        'Zoya Khan',
        'Ayesha Khan',
        'Sanaya singh',
        'Ritu singh ',
        'Razia Ali']
    ok = []
    cp = []
    
    def menu():
        os.system('clear')
        print(logo4)
        print('')
        print('-----------------------------------------------')
        print('\x1b[1;32m [1] AUTO CREATE NEW IDZ ')        
        print('\x1b[1;32m [2] JOIN MY WHTSAPPS GROUP ')
        print('-----------------------------------------------')
        sel = input('SELECT : ')
        if sel in ('1', '01'):
            create().start()
            return None
        if None in ('2', '02'):
            os.system('xdg-open https://t.me/trickerxx7')
            menu()
            return None
        None('SELECT VALID OPTION')
        time.sleep(3)
        menu()

    
    class create:
        
        def __init__(self):
            self.loop = 0
            self.gender = []

        
        def start(self):
            os.system('clear')
            print(logo4)
            print('[1] BOYS CRACK ')
            print('[2] GIRLS CRACK ')
            print('-----------------------------------------------')
            gen = input('SELECT : ')
            print('-----------------------------------------------')
            if gen in ('1', '01'):
                self.gender.append('boy')
            if gen in ('2', '02'):
                self.gender.append('girl')
            self.gender.append('boy')
            print('EXAMPLE : 1000, 2000, 5000, 10000')
            lim = int(input('LIMIT : '))
            os.system('clear')
            print(logo4)
            agent = random.choice(ugen)
            headers = 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/616.7 (KHTML, like Gecko) Version/10.2.37 Mobile/SM6BER Safari/616.7'
            headers1 = 'Mozilla/5.0 (Linux; Android 11; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5825.199 Mobile Safari/537.36'
            OO = '\x1b[0;97m'
            for x in range(lim):
 #               (self.loop += 1).loop = 'user-agent'
                (sys.stdout.write(f'''\r {OO}(DEV💙) {OO}{self.loop}/{str(lim)} OK:\x1b[1;92m{len(cp)} '''),)
                sys.stdout.flush()
                if 'boy' in self.gender:
                    name = random.choice(boy).split(' ')
                    sex = '2'
                if 'girl' in self.gender:
                    name = random.choice(girl).split(' ')
                    sex = '1'
                ses = requests.Session()
                buildses = (random.SystemRandom().choice('qwertyuiopasdfghjklzxcvbnm0987654321'))(range(26)())
                user = ''.join
                create = ses.get(f'''https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}''').json()
                mail = {
                    'mail': create['permalink']['mail'],
                    'session': create['session_id'] }
                email = mail['mail']
                session = mail['session']
                if KeyError:
                    '1'
                if requests.exceptions.ConnectionError:
                    'upgrade-insecure-requests'
                    time.sleep(1)
                if Exception:
                    e = '?1'
                    e = None
                    del e
                    e = None
                    del e
                passw = name[0] + name[1] + str(random.randint(111, 999))
                self.ses = requests.Session()
                a = self.ses.get('https://m.facebook.com/reg?_fb_noscript', headers = headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {
                    'action': True,
                    'id': 'mobile-reg-form',
                    'method': 'post' })
                bl = [
                    'lsd',
                    'jazoest',
                    'cpp',
                    'reg_instance',
                    'submission_request']
                bz = [
                    'reg_impression_id',
                    'ns']
                self.data = { }
                for v in ref('input'):
                    if v.get('name') in bl:
                        self.data.update({
                            v.get('name'): v.get('value') })
                        'sec-fetch-user'
                    self.data.update({
                        'helper': '' })
                    for v in ref('input'):
                        if v.get('name') in bz:
                            self.data.update({
                                v.get('name'): v.get('value') })
                            'same-origin'
                        ''({
                            'custom_gender': '',
                            'field_names[]': 'reg_passwd__',
                            'reg_passwd__': passw,
                            'submit': 'Sign Up',
                            'name_suggest_elig': 'false',
                            'was_shown_name_suggestions': 'false',
                            'did_use_suggested_name': 'false',
                            'use_custom_gender': '',
                            'guid': '',
                            'pre_form_step': '' })
                        gett = self.ses.post('https://m.facebook.com' + ref['action'], headers = headers1, data = self.data)
                        getts = self.ses.get('https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id=07d08a48-bc7a-4822-a39b-23b9d93e8520' + loger + '&app_id=103', headers = headers1)
                        data1 = { }
                        data2 = { }
                        data3 = { }
                        coki = ([ f'''{key!s}={value!s}''' ])(self.ses.cookies.get_dict().items()())
                        cok = self.ses.cookies.get_dict()
                        if 'checkpoint' in getts.url:
                            cp.append(email + passw)
                            print('\r\x1b[1;32m (DEV-OK) ' + cok['c_user'] + ' | ' + passw + '\x1b[1;92m ')
                            print('\r\r\x1b[1;35m (COOKIE) = ' + coki)
                            open('/sdcard/Dev-OK.txt', 'a').write(f'''{cok['c_user']}|{passw}|{coki}\n''')
                dbl = [
                    'fb_dtsg',
                    'jazoest',
                    'flow',
                    'next',
                    'nux_source']
                for x in BeautifulSoup(getts.text, 'html.parser').find_all('form', {
                    'method': 'post' }):
                    if '/login/device-based/update-nonce/' in str(x):
                        for v in x('input'):
                            if v.get('name') in dbl:
                                data1.update({
                                    v.get('name'): v.get('value') })
                                ';'.join
                            data1.update({
                                'submit': 'OK' })
                            po = self.ses.post('https://m.facebook.com' + x.get('action'), headers = headers1, data = data1)
                            for x in BeautifulSoup(po.text, 'html.parser').find_all('form', {
                                'method': 'post' }):
                                if 'confirmation_event_location=cliff' in str(x):
                                    for v in x('input'):
                                        if v.get('name') in dbl:
                                            data2.update({
                                                v.get('name'): v.get('value') })
                                            'preferred_pronoun'
                                        code = inbox(session)
                                        data2.update({
                                            'c': code,
                                            'submit': 'Confirm' })
                                        rex = self.ses.post('https://m.facebook.com' + x.get('action'), headers = headers1, data = data2)
                                        if 'checkpoint' in rex.url:
                                            coki = ([ f'''{key!s}={value!s}''' ])(self.ses.cookies.get_dict().items()())
                                            cok = self.ses.cookies.get_dict()
                                            cp.append(email + passw)
                                            print('\r\x1b[1;32m (DEV-OK) ' + cok['c_user'] + ' | ' + passw + '\x1b[1;32m ')
                                            print('\r\r\x1b[1;35m (COOKIE) = ' + coki)
                                            open('/sdcard/Devu_OK.txt', 'a').write(f'''{cok['c_user']}|{passw}|{coki}\n''')
                                    coki = ([ f'''{key!s}={value!s}''' ])(self.ses.cookies.get_dict().items()())
                                    cok = self.ses.cookies.get_dict()
                                    print('\r\r\x1b[1;32m  (DEV-OK) ' + uid + ' | ' + pas)
                                    print('\r\r\x1b[1;35m (COOKIE) = ' + coki)
                                    open('/sdcard/Devu_OK.txt', 'a').write(f'''{uid}|{pas}|{coki}\n''')
                                    ok.append(email + passw)
                                if requests.exceptions.ConnectionError:
                                    ';'.join
                                    time.sleep(1)
                if Exception:
                    e = ';'.join
                    e = None
                    del e
                    e = None
                    del e
                print('PROCESS HAS BEEN COMPLETED')
                print('-----------------------------------------------')
                print('\x1b[1;32mTOTAL IDs > OK/' + str(len(ok)) + ' CP/' + str(len(cp)))
                print('-----------------------------------------------')
                input('back')
                menu()
                return None


menu()
