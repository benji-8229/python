class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """
        Model of a TV complete with power, mute, volume, and channel switching.
        """

        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the power status of the TV.
        :return:
        """

        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Toggle the TV between muted and unmuted. Sets the TV volume to 0
        when muting, sets the TV volume to the value it was before when unmuting.
        :return:
        """

        if not self.__status:
            return

        if self.__muted:
            # If currently muted we should unmute and set the volume
            # to the value we previously saved
            self.__muted = False
            if self.prev_volume:
                self.__volume = self.prev_volume
        else:
            # If not currently muted we mute, set vol to 0, and
            # save our previous volume
            self.prev_volume = self.__volume
            self.__volume = Television.MIN_VOLUME
            self.__muted = True

    def channel_up(self) -> None:
        """
        Increases the channel by one. If the channel is already at Television.MAX_CHANNEL
        it will loop back to Television.MIN_CHANNEL.
        :return:
        """

        if not self.__status:
            return

        self.__channel += 1
        if self.__channel > Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decreases the channel by one. If the channel is already at Television.MIN_CHANNEL
        it will loop back to Television.MAX_CHANNEL.
        :return:
        """

        if not self.__status:
            return

        self.__channel -= 1
        if self.__channel < Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases the volume by one. If the volume is already at Television.MAX_VOLUME
        it will loop back to Television.MAX_CHANNEL.
        :return:
        """

        if not self.__status:
            return

        if self.__muted:
            self.mute()

        if self.__volume == Television.MAX_VOLUME:
            return

        self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by one. If the volume is already at Television.MIN_VOLUME
        it will loop back to Television.MAX_VOLUME.
        :return:
        """

        if not self.__status:
            return

        if self.__muted:
            self.mute()

        if self.__volume == Television.MIN_VOLUME:
            return

        self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns a brief summary of the status of the TV.
        :return: str
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
