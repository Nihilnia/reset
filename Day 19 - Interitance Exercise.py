from time import sleep

# Let's create a class

class YoutubeChannels():

    def __init__(self, channelName, about, subscribers):
        self.channelName = channelName
        self.about = about
        self.subscribers = subscribers

    def showChannelInfos(self):
        print("""
        Channel - {}
        About: {}
        Subscribers : {}
        """.format(self.channelName, self.about, self.subscribers))

# Let's create another class for Inheritance exercise

class GamingChannels(YoutubeChannels):
    
    def ChangeSubscribersCount(self, newSubscribersCount):
        self.subscribers = newSubscribersCount

# Now we can use everything from first class "YoutubeChannels"

LifeisGG = GamingChannels(channelName = "Life is GG", about = "Gaming", subscribers = "96000")
LifeisGG.showChannelInfos() #as you can see we can use that function bc of Inheritance

userChoice = input("Do you wanna change subscribers count?: Y / N ")
if userChoice.lower() != "n":
    newCount = int(input("Currently {} New subscribers count: ".format(LifeisGG.subscribers)))
    LifeisGG.ChangeSubscribersCount(newSubscribersCount = newCount)
    print("Changing Subscribers..")
    sleep(2)
    print("Changed succesfuly! New subscribers of {} is {}".format(LifeisGG.channelName, LifeisGG.subscribers))
else:
    pass