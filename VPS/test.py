import os

try:
    USER_ID_H_02 = os.environ['USER_ID_H_02']
except:
    # 本地调试用
    USER_ID_H_02 = ''
    
try:
    PASS_WD_H_02 = os.environ['PASS_WD_H_03']
except:
    # 本地调试用
    PASS_WD_H_02 = ''
  
print('This is :'+USER_ID_H_02)
