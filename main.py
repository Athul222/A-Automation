from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5

from forms import InstagramForm, TinderForm, WifiComplaintForm, SpotifyForm, CookieClickerForm, WebsiteScrapingForm

from instagram import InstagramFollowerBot
from tinder import TinderBot
from wifi import InternetSpeedTwitterBot
from spotify import SpotifyAddMusic
from cookie_clicker import CookieClicker
from webscrap import ScrapWebsite

app = Flask(__name__)
app.config["SECRET_KEY"] = "cmoihw083quejxc23729487"
Bootstrap5(app)

@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/doc")
def documentation():
    return render_template("documentation.html")

@app.route("/instagramBot", methods=["GET", "POST"])
def instagram():
    form = InstagramForm()
    if request.method == "POST":
        id = request.form.get("username")
        password = request.form.get("password")
        targetId = request.form.get("target_username")
        
        bot = InstagramFollowerBot(username=id, password=password, similar_account=targetId)
        bot.instagram_login()
        bot.find_followers()
        bot.follow()
        return redirect(url_for("instagram"))
    return render_template("test.html", form=form)

@app.route("/tinderBot", methods=["GET", "POST"])
def tinder():
    form = TinderForm()
    if request.method == "POST":
        id = request.form.get("username")
        password = request.form.get("password")
        
        bot = TinderBot(username=id, password=password)
        bot.run()
        return redirect(url_for("tinder"))
    return render_template("test.html", form=form)

@app.route("/wifiComplaintBot", methods=["GET", "POST"])
def wifi():
    form = WifiComplaintForm()
    if request.method == "POST":
        promised_up = int(request.form.get("promised_up"))
        promised_down = int(request.form.get("promised_down"))
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        
        bot = InternetSpeedTwitterBot(promised_up, promised_down, email, username, password)
        bot.get_internet_speed()
        bot.tweet_at_provider()
        
        return redirect(url_for("wifi"))
    return render_template("test.html", form=form)

@app.route("/spotifyBot", methods=["GET", "POST"])
def spotify_add_music():
    form = SpotifyForm()
    if request.method == "POST":
        client_id = request.form.get("client_id")
        client_secret = request.form.get("client_secret")
        date = request.form.get("date")
        
        bot = SpotifyAddMusic(client_id, client_secret, date)
        bot.run()
        
        return redirect(url_for("spotify_add_music"))
    return render_template("test.html", form=form)        

result = []
@app.route("/webScrapeBot", methods=["GET", "POST"])
def webscrape():
    form = WebsiteScrapingForm()
    if request.method == "POST":
        url = request.form.get("url")
        element = request.form.get("element")
        bot = ScrapWebsite(url, element)
        scrape_result = bot.scrape()
        global result
        result = []
        result = scrape_result
        return render_template("test.html", form=form, data=True)
    return render_template("test.html",form=form, data=False)  

@app.route("/scrapeResult")
def scrape_result():
    return {
        "element" : result
    }

@app.route("/cookieClikerBot", methods=["GET", "POST"])
def cookie_clicker():
    form = CookieClickerForm()
    if request.method == "POST":
        minute = request.form.get("minute")
        bot = CookieClicker(minute=int(minute))
        bot.run()
        return redirect(url_for("cookie_clicker"))
    return render_template("test.html", form=form)  

@app.route("/about")
def about():  
    return render_template("about.html")

@app.route("/contact")
def contact():  
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, threaded=True)