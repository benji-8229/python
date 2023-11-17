class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """
        Model of a TV complete with power, mute, volume, and channel switching.
        """

        self._status: bool = False
        self._muted: bool = False
        self._volume: int = Television.MIN_VOLUME
        self._channel: int = Television.MIN_CHANNEL

        # Needed to save the volume to return to after unmuting
        self._prev_volume: int = self._volume

    def power(self) -> None:
        """
        Toggles the power status of the TV.
        :return:
        """

        if self._status:
            self._status = False
        else:
            self._status = True

    def mute(self) -> None:
        """
        Toggle the TV between muted and unmuted. Sets the TV volume to 0
        when muting, sets the TV volume to the value it was before when unmuting.
        :return:
        """

        if not self._status:
            return

        if self._muted:
            # If currently muted we should unmute and set the volume
            # to the value we previously saved
            self._muted = False
            self._volume = self._prev_volume
        else:
            # If not currently muted we mute, save our "true" volume
            # and then set the volume to 0
            self._prev_volume = self._volume
            self._volume = Television.MIN_VOLUME
            self._muted = True

    def channel_up(self) -> None:
        """
        Increases the channel by one. If the channel is already at Television.MAX_CHANNEL
        it will loop back to Television.MIN_CHANNEL.
        :return:
        """

        if not self._status:
            return

        self._channel += 1
        if self._channel > Television.MAX_CHANNEL:
            self._channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decreases the channel by one. If the channel is already at Television.MIN_CHANNEL
        it will loop back to Television.MAX_CHANNEL.
        :return:
        """

        if not self._status:
            return

        self._channel -= 1
        if self._channel < Television.MIN_CHANNEL:
            self._channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases the volume by one. If the volume is already at Television.MAX_VOLUME
        it will loop back to Television.MAX_CHANNEL.
        :return:
        """

        if not self._status:
            return

        if self._muted:
            self.mute()

        if self._volume == Television.MAX_VOLUME:
            return

        self._volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by one. If the volume is already at Television.MIN_VOLUME
        it will loop back to Television.MAX_VOLUME.
        :return:
        """

        if not self._status:
            return

        if self._muted:
            self.mute()

        if self._volume == Television.MIN_VOLUME:
            return

        self._volume -= 1

    def __str__(self) -> str:
        """
        Returns a brief summary of the status of the TV.
        :return: str
        """
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"
