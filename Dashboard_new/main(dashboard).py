from quart import Quart, redirect, url_for
from quart_discord import DiscordOAuth2Session, requires_authorization, Unauthorized

app = Quart(__name__)

app.secret_key = b"random bytes representing quart secret key"

app.config["DISCORD_CLIENT_ID"] = 844813316505075712    # Discord client ID.
# Discord client secret.
app.config["DISCORD_CLIENT_SECRET"] = "_2M5Jp4VYn8gb0HetsrNW_rfdTruwSG2"
# URL to your callback endpoint.
app.config["DISCORD_REDIRECT_URI"] = "http://127.0.0.1:5000/callback"
# Required to access BOT resources.
app.config["DISCORD_BOT_TOKEN"] = "ODQ0ODEzMzE2NTA1MDc1NzEy.YKX3tg.AGjRaxwtYgBiOeHWfPEupR-FypU"

discord = DiscordOAuth2Session(app)


@app.route("/login/")
async def login():
    return await discord.create_session()


@app.route("/callback/")
async def callback():
    await discord.callback()
    return redirect(url_for(".me"))


@app.errorhandler(Unauthorized)
async def redirect_unauthorized(e):
    return redirect(url_for("login"))


@app.route("/me/")
@requires_authorization
async def me():
    user = await discord.fetch_user()
    return f"""
    <html>
        <head>
            <title>{user.name}</title>
        </head>
        <body>
            <img src='{user.avatar_url}' />
        </body>
    </html>"""


if __name__ == "__main__":
    app.run(debug=True)
