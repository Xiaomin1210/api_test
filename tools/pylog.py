# -*- coding:utf-8 _*-
import logging
class MyLog():
    def my_log(self,msg,level):
        """定义一个日志收集器"""
        my_log = logging.getLogger('py日志')

        """设定级别"""
        my_log.setLevel('DEBUG')

        """创建一个输出渠道"""
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')
        ch.setFormatter(formatter)


        fh = logging.FileHandler('PY11.txt',mode='a',encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)
        """两者对接"""
        my_log.addHandler(ch)
        my_log.addHandler(fh)

        #收集日志
        if level.upper() == 'DEBUG':
            my_log.debug(msg)
        elif level == 'INFO':
            my_log.info(msg)
        elif level == 'ERROR':
            my_log.error(msg)
        elif level == 'WARNING':
            my_log.warning(msg)
        elif level == 'CRITICAL':
            my_log.critical(msg)


        #关闭日志收集器
        my_log.removeHandler(ch)
        my_log.removeHandler(fh)

    def debug(self,msg):
        self.my_log(msg,'DEBUG')

    def info(self,msg):
        self.my_log(msg,'INFO')

    def error(self,msg):
        self.my_log(msg,'ERROR')

    def warning(self,msg):
        self.my_log(msg,'WARNING')

    def critical(self,msg):
        self.my_log(msg,'CRITICAL')


if __name__ == '__main__':
    pass
