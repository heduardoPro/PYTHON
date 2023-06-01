class Log:

    def _log(self, msg):
        raise NotImplementedError('Implemente o metdo log')
    
    def log_error(self, msg):

        return self._log(f'Error:  {msg=}')
   
    def log_success(self, msg):

        return self._log(f'Success:  {msg=}')

class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'\n{msg} {self.__class__.__name__}')



if __name__ == '__main__':
    i = LogPrintMixin()
    i.log_error('Hello World')
    i.log_success('Qualquer coisa')