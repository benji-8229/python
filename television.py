class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

        self._prev_volume = self._volume

    def power(self):
        if self._status:
            self._status = False
        else:
            self._status = True

    def mute(self):
        if not self._status:
            return

        if self._muted:
            self._muted = False
            self._volume = self._prev_volume
        else:
            self._prev_volume = self._volume
            self._volume = 0
            self._muted = True

    def channel_up(self):
        if not self._status:
            return

        self._channel += 1
        if self._channel > Television.MAX_CHANNEL:
            self._channel = Television.MIN_CHANNEL

    def channel_down(self):
        if not self._status:
            return

        self._channel -= 1
        if self._channel < Television.MIN_CHANNEL:
            self._channel = Television.MAX_CHANNEL

    def volume_up(self):
        if not self._status:
            return

        if self._muted:
            self.mute()

        if self._volume == Television.MAX_VOLUME:
            return

        self._volume += 1

    def volume_down(self):
        if not self._status:
            return

        if self._muted:
            self.mute()

        if self._volume == Television.MIN_VOLUME:
            return

        self._volume -= 1


    def __str__(self):
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"
