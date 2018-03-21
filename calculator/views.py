from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import BaseListView


class CalculatorView(BaseListView):
    template_name = 'calculator.html'
    all_symbol = '0123456789.+-/*#C='
    operations = '.+-/*#C='
    status = ''
    error = '/calculator/E/'
    primary = '/calculator/'

    def calc(self, request, **kargs):
        button_name = request.GET.get('command')
        if button_name:
            if button_name in self.all_symbol:
                if button_name == 'C':
                    self.status = ''
                    return HttpResponseRedirect(self.primary)
                if button_name == '=':
                    if self.status == '' or self.valid_value() is False:
                        return HttpResponseRedirect(self.error)
                    self.status = self.status.replace('#', '*-1')
                    result = int(eval(self.status))
                    self.status = ''
                    return HttpResponseRedirect(
                        '/calculator/{}/'.format(result)
                    )
                self.status += button_name
            else:
                return HttpResponseRedirect(self.error)
        return render(request, self.template_name)

    def valid_value(self):
        """
        :return: False if the string begins with an action, or contains
        a division by 0
        """
        if self.status[0] in '=/#*+-.' or self.status[-1] == '0' and \
                        self.status[-2] == '/':
            return False
        else:
            return True
