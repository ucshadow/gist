__author__ = 'SHADOW'

import praw
import time
import json
import datetime


r = praw.Reddit(user_agent='agent')
r.login('username', 'password')


with open('dict_storage.json') as dict_storage:
    idol_list = json.loads(dict_storage.read())

with open('op_karma.json') as kar:
    op_karma = json.loads(kar.read())



while True:
    subreddit = r.get_subreddit('kpics')
    for submission in subreddit.get_new(limit=75):
        suv = int(submission.ups)
        with open("ids.txt", "r") as sub_id:
            ids = sub_id.read().split(' ')
        if submission.id not in ids:
            for idol in idol_list:
                slss = submission.title.lower()
                sign_check = list(slss)
                new_sls = []
                for sign in sign_check:
                    if sign not in "!,:;?+-":
                        if sign == "'":
                            sign = " "
                        new_sls.append(sign)
                sls = ''.join(new_sls).split()
                if idol in sls:

                    if idol in ('choa', 'hyuna', 'sojin', 'boa', 'soyeon',
                                'jiae', 'hyorin', 'gummi', 'hyerin'):
                        if idol == 'choa':
                            if 'crayon' in sls or 'pop' in sls:
                                idol_list['choa_cp'][0] += 1
                            else:
                                idol_list['choa'][0] += 1
                        elif idol == 'hyuna':
                            if '9m' in sls or 'muses' in sls or '9muses' in sls:
                                idol_list['hyuna_9m'][0] += 1
                            else:
                                idol_list['hyuna'][0] += 1
                        elif idol == 'sojin':
                            if '9m' in sls or 'muses' in sls or '9muses' in sls:
                                idol_list['sojin_9m'][0] += 1
                            else:
                                idol_list['sojin'][0] += 1
                        elif idol == 'boa':
                            if 'spica' in sls:
                                idol_list['boa_s'][0] += 1
                            else:
                                idol_list['boa'][0] += 1
                        elif idol == 'soyeon':
                            if 'laboum' in sls:
                                idol_list['soyeon_l'][0] += 1
                            else:
                                idol_list['soyeon'][0] += 1
                        elif idol == 'jiae':
                            if 'wassap' in sls:
                                idol_list['jiae_w'][0] += 1
                            else:
                                idol_list['jiae'][0] += 1
                        elif idol == 'gummi':
                            idol_list['geummi'][0] += 1
                        elif idol == 'hyerin':
                            idol_list['hyelin'][0] += 1
                        elif idol == 'hyorin':
                            idol_list['hyolin'][0] += 1
                    else:
                         idol_list[idol][0] += 1
                    print('hey I found -- ', idol, ' -- in ', submission.title,
                          'posted by ', submission.author.name)
                    with open("OP's.txt", 'a') as o:
                        op = submission.author
                        o.write(op.name + ' ')
            with open("ids.txt", "a") as f:
                f.write(submission.id + ' ')

        if submission.created_utc + 86400 < (time.mktime(datetime.datetime.now().timetuple())):
            with open('karma_id.txt', 'r') as kar:
                karma_id = kar.read().split(' ')
            if submission.id not in karma_id:
                a_name = submission.author.name
                if a_name not in op_karma:
                    op_karma[a_name] = [0, 0]
                    print('i added op ', a_name)
                op_karma[a_name][0] += suv
                op_karma[a_name][1] += 1

                for idol in idol_list:
                    slss = submission.title.lower()
                    sign_check = list(slss)
                    new_sls = []
                    for sign in sign_check:
                        if sign not in "!,:;?+-":
                            if sign == "'":
                                sign = " "
                            new_sls.append(sign)
                    sls = ''.join(new_sls).split()
                    if idol in sls:

                        if idol in ('choa', 'hyuna', 'sojin', 'boa', 'soyeon',
                                    'jiae', 'hyorin', 'gummi', 'hyerin'):
                            if idol == 'choa':
                                if 'crayon' in sls or 'pop' in sls:
                                    idol_list['choa_cp'][1] += suv
                                    idol_list['choa_cp'][2] += 1
                                else:
                                    idol_list['choa'][1] += suv
                                    idol_list['choa'][2] += 1
                            elif idol == 'hyuna':
                                if '9m' in sls or 'muses' in sls or '9muses' in sls:
                                    idol_list['hyuna_9m'][1] += suv
                                    idol_list['hyuna_9m'][2] += 1
                                else:
                                    idol_list['hyuna'][1] += suv
                                    idol_list['hyuna'][2] += 1
                            elif idol == 'sojin':
                                if '9m' in sls or 'muses' in sls or '9muses' in sls:
                                    idol_list['sojin_9m'][1] += suv
                                    idol_list['sojin_9m'][2] += 1
                                else:
                                    idol_list['sojin'][1] += suv
                                    idol_list['sojin'][2] += 1
                            elif idol == 'boa':
                                if 'spica' in sls:
                                    idol_list['boa_s'][1] += suv
                                    idol_list['boa_s'][2] += 1
                                else:
                                    idol_list['boa'][1] += suv
                                    idol_list['boa'][2] += 1
                            elif idol == 'soyeon':
                                if 'laboum' in sls:
                                    idol_list['soyeon_l'][1] += suv
                                    idol_list['soyeon_l'][2] += 1
                                else:
                                    idol_list['soyeon'][1] += suv
                                    idol_list['soyeon'][2] += 1
                            elif idol == 'jiae':
                                if 'wassap' in sls:
                                    idol_list['jiae_w'][1] += suv
                                    idol_list['jiae_w'][2] += 1
                                else:
                                    idol_list['jiae'][1] += suv
                                    idol_list['jiae'][2] += 1
                            elif idol == 'gummi':
                                idol_list['geummi'][1] += suv
                                idol_list['geummi'][2] += 1
                            elif idol == 'hyerin':
                                idol_list['hyelin'][1] += suv
                                idol_list['hyelin'][2] += 1
                            elif idol == 'hyorin':
                                idol_list['hyolin'][1] += suv
                                idol_list['hyolin'][2] += 1
                        else:
                            idol_list[idol][1] += suv
                            idol_list[idol][2] += 1
                            print('new post, new karma for :--', idol)
                with open('karma_id.txt', 'a') as add_karma_id:
                    add_karma_id.write(submission.id + ' ')

    with open('dict_storage.json', 'w') as dic:
        json.dump(idol_list, dic)
    with open('op_karma.json', 'w') as karm:
        json.dump(op_karma, karm)
    print('sleeping for 1200')
    time.sleep(1200)


