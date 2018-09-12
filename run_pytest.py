import os
import sys


str = sys._getframe().f_code.co_filename
list = str.split('\\')
final_path = ''
for y in range(len(list) - 1):
    if y == 0:
        final_path = list[0]
    else:
        final_path = final_path + '/' + list[y]
p = os.popen('cd %s&&pytest --alluredir allure-report' % final_path)
q = os.popen('cd %s&&allure serve allure-report' % final_path)
x = p.read() + q.read()
print(x)
p.close()
q.close()
