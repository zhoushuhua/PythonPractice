# -*- coding: cp936 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class IndexPage(webapp.RequestHandler):
    def get(self):
        pass
    def post(self):
        new_birth = birthDB.BirthDetails()

        new_birth.name = self.request.get("name")
        new_birth.date = self.request.get("date_of_birth")
        new_birth.time = self.request.get("time_of_birth")

        # ��������
        new_birth.put()

        # ������ʾ��Ϣ
        html = template.render("templates/header.html", {"title":"Thank you!"})
        html = html + "<p>Thank you for providing your birth details</p>"
        html = html + template.render("templates/footer.html", {"links":"Enter <a href='/'>another birth</a>"})

        # ��Ӧ��ʾ��Ϣ
        self.response.write(html)

app = webapp.WSGIApplication([('/.*', IndexPage)], debug = True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()
