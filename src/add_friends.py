
import os
from login import pwd,login
from instabot import Bot
import glob
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])


class just_someone:
    """
        A simple bot instagram
    """
    def __init__(self,Username,Password):
        #login to the count
        self.bot=Bot()
        self.bot.login(username=Username,password=Password)

    def add_following(self,name):
        self.bot.follow_users(name)


if __name__ == '__main__':
    bot=just_someone(login,pwd)
    bot.add_following("_koala_noir_")