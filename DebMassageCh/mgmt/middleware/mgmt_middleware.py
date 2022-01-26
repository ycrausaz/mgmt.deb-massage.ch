from django.http import HttpResponse, HttpResponseBadRequest
from django.db import IntegrityError


class MgmtMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization on start-up

    def __call__(self, request):
        # Logic executed on a request before the view (and other middleware) is called.
        # get_response call triggers next phase
        response = self.get_response(request)
        # Logic executed on response after the view is called.
        # Return response to finish middleware sequence
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        return None

    def process_exception(self, request, exception):
        ErrorMessage = '<!DOCTYPE html>'
        ErrorMessage += '<html lang="en">'
        ErrorMessage += '<head>'
        ErrorMessage += '<meta charset="utf-8">'
        ErrorMessage += '<title>deb-massage</title>'
        ErrorMessage += '</head>'
        ErrorMessage += '<body>'
        ErrorMessage += '<H1><b>Attention !</b></h1>'
        ErrorMessage += 'Le client en cours d\'effacement est lié à une prestation. La suppression n\'est donc par autorisée.<br>'
        ErrorMessage += '<button onclick="history.back()">Back</button>'
        ErrorMessage += '</body>'
        ErrorMessage += '</html>'
        return HttpResponse(ErrorMessage)

    def process_template_response(self, request, response):
        return response