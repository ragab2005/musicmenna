from AnonXMusic.core.bot import Zelzaly
from AnonXMusic.core.dir import dirr
from AnonXMusic.core.git import git
from AnonXMusic.core.userbot import Userbot
from AnonXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Zelzaly()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
