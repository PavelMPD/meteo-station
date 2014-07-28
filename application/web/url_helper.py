from application.web.config import API_VERSION

VIEW = 'view'
ADD = 'add'
EDIT = 'edit'
DELETE = 'delete'

DAY_SAMPLE_URL = '/{0}/day_samples'.format(API_VERSION)


class UrlHelper():
    def __init__(self, base_url):
        self.base_url = base_url

    def view(self):
        return self.base_url + '/{0}'.format(VIEW)

    def add(self):
        return self.base_url + '/{0}'.format(ADD)

    def edit(self):
        return self.base_url + '/{0}'.format(EDIT)

    def delete(self):
        return self.base_url + '/{0}'.format(DELETE)