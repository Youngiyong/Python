"""
경로 이동은  Path 모듈로 안되어 os 모듈이 필요하다
"""
import os
# print(os.environ["HOMEPATH"])
print(os.path.expanduser('$JAVA_HOME'))
print(os.path.expanduser('$TOMCAT_HOME'))

'''
    shutil 패키지
'''
import shutil
# shutil.rmtree('imsi')

# shutil.copytree('../e_file_class', 'test')