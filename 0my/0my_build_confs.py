# -*- coding: utf-8 -*-

import re


def getRulesStringFromFile(path, kind):
    path = '../factory/' + path
    file = open(path, 'r', encoding='utf-8')
    contents = file.readlines()
    ret = ''

    for content in contents:
        content = content.strip('\r\n')
        if not len(content):
            continue

        if content.startswith('#'):
            ret += content + '\n'
        else:
            prefix = 'DOMAIN-SUFFIX'
            if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', content):
                prefix = 'IP-CIDR'
                if '/' not in content:
                    content += '/32'
            elif '.' not in content:
                prefix = 'DOMAIN-KEYWORD'

            ret += prefix + ',%s,%s\n' % (content, kind)

    return ret


# get head and foot
str_head = open('../factory/' + 'template/sr_head.txt', 'r', encoding='utf-8').read()
str_foot = open('../factory/' + 'template/sr_foot.txt', 'r', encoding='utf-8').read()


# make values
values = {}

values['build_time'] = '9999-99-99'

values['top500_proxy']  = getRulesStringFromFile('resultant/top500_proxy.list', 'Proxy')
values['top500_direct'] = getRulesStringFromFile('resultant/top500_direct.list', 'Direct')

values['ad'] = getRulesStringFromFile('resultant/ad.list', 'Reject')

values['manual_direct'] = getRulesStringFromFile('manual_direct.txt', 'Direct')
values['manual_proxy']  = getRulesStringFromFile('manual_proxy.txt', 'Proxy')
values['manual_reject'] = getRulesStringFromFile('manual_reject.txt', 'Reject')
values['0my_manual_reject'] = getRulesStringFromFile('../0my/0my_manual_reject.txt', 'Reject')

values['gfwlist'] = getRulesStringFromFile('resultant/gfw.list', 'Proxy') \
                  + getRulesStringFromFile('manual_gfwlist.txt', 'Proxy')


# make confs
conf_name = '0my_template_rules'
file_template = open(conf_name + '.txt', 'r', encoding='utf-8')
template = file_template.read()
template = str_head + template + str_foot
file_output = open(conf_name+'.conf', 'w', encoding='utf-8')
marks = re.findall(r'{{(.+)}}', template)
for mark in marks:
    template = template.replace('{{'+mark+'}}', values[mark])
file_output.write(template)