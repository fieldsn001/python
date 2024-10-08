class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = int(Television.MIN_VOLUME)
        self.__channel = int(Television.MIN_CHANNEL)

    def power(self): # turn tv on an off by changing value of status variable
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self): # mute, unmute the tv when it's on by changing the value of the muted variable
        if self.__status: # check to see if tv is on
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self): # use to increase the tv channel value when the tv is on...
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self): # use to decrease the tv channel value when the tv is on...
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self): # volume should stay at min or max (not cycle through like channels)
        if self.__status:
            self.__muted = False # if muted, first unmute then adjust volume status
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self): # volume should stay at min or max (not cycle through like channels)
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        if self.__muted: # if muted, display min volume, otherwise display current volume
            return f' Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f' Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


