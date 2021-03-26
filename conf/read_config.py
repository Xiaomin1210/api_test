# -*- coding:utf-8 _*-
import configparser
from tools.project_path import ProjectPath

class ReadConfig:
    @staticmethod
    def get_config(filepath, section, option):
        cf = configparser.ConfigParser()
        cf.read(filepath)
        return cf[section][option]

if __name__ == '__main__':
    data = ReadConfig.get_config(ProjectPath.test_conf_path, 'MODE', 'mode')
    print(data)