# -*- coding: cp936 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms
from google.appengine.api import users
import hfwwgDB

class SightingForm(djangoforms.ModelForm):
    class Meta:
        model = hfwwgDB.Sighting
        exclude = ["which_user"]


class SightingInputPage(webapp.RequestHandler):
    def get(self):
        html = template.render("templates/header.html", {"title" : "Report a Possible Sighting"})
        html = html + template.render("templates/form_start.html", {})
        html = html + str(SightingForm())
        html = html + template.render("templates/form_end.html", {"sub_title" : "Submit Sighting"})
        html = html + template.render("templates/.html", {"links" : ""})
        self.response.out.write(html)

    def post(self):
        new_hfwwg = hfwwgDB.Sighting()

        # 初始化
        new_hfwwg.name = self.request.get("name")
        new_hfwwg.email = self.request.get("email")
        new_hfwwg.date = self.request.get("date")
        new_hfwwg.time = self.request.get("time")
        new_hfwwg.location = self.request.get("location")
        new_hfwwg.fin_type = self.request.get("fin_type")
        new_hfwwg.whale_type = self.request.get("whale_type")
        new_hfwwg.blow_type = self.request.get("blow_type")
        new_hfwwg.wave_type = self.request.get("wave_type")
        new_hfwwg.which_user = users.get_current_user()

        # 保存数据
        new_hfwwg.put()

        # 弹出提示信息
        html = template.render("templates/header.html", {"title":"Thank you!"})
        html = html + "<p>Thank you for providing your sighting data</p>"
        html = html + template.render("templates/footer.html", {"links":"Enter <a href='/'>another birth</a>"})

        # 响应提示信息
        self.response.write(html)


app = webapp.WSGIApplication([("/.*", SightingInputPage)], debug = True)

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
