import requests
import re
import logging
logging.captureWarnings(True)

########################################
#### User configuration starts here #### 
username_str='r1234567' 
pass_str='password_here'
#### User configuration ends here   #### 
########################################

s=requests.Session()
r_webpage =s.get('https://netlogin.kuleuven.be/cgi-bin/wayf2.pl?inst=kuleuven&lang=en&submit=Ga+verder+%2F+Continue')
pass_regex= '<td><input type="password" size="20" maxlength="50" name="(.+?)" class="formField" autocomplete="off" /></td>'
pass_pattern = re.compile(pass_regex)
pass_name = re.findall(pass_pattern , r_webpage.content)
form_submit={'inst': 'kuleuven', 'lang': 'en', 'uid': username_str, pass_name[0]: pass_str, 'submit': 'Login'}
resp=s.post('https://netlogin.kuleuven.be/cgi-bin/netlogin.pl',form_submit)

usage_regex='<TD width="30%">(.+?) MBytes<br>\((.+?)\%\)'
usage_pattern=re.compile(usage_regex)
usage_data=re.findall(usage_pattern,resp.content)
notice= '\nThe download volume [Mb]:'+usage_data[0][0]+','+usage_data[0][1]+'%\n'+'The upload volume   [Mb]:'+usage_data[1][0]+','+usage_data[1][1]+'%\n'
print(notice)
