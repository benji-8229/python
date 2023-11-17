import pytest
from television import Television


def convert_details(details: Television) -> dict:
    details = str(details)
    list_details = [x.strip().split(" ")[2] for x in details.split(",")]
    return {"power": list_details[0], "channel": int(list_details[1]), "volume": int(list_details[2])}


class TestTelevision:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test___init__(self):
        self.tv.__init__()
        assert self.tv.__str__() == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"

    def test_power(self):
        self.tv.__init__()
        assert convert_details(self.tv)["power"] == "False"
        self.tv.power()
        assert convert_details(self.tv)["power"] == "True"

    def test_mute(self):
        self.tv.__init__()
        self.tv.power()

        start_volume = convert_details(self.tv)["volume"]

        # On, volume up, mute
        self.tv.volume_up()
        self.tv.mute()
        assert convert_details(self.tv)["volume"] == Television.MIN_VOLUME

        # Unmute
        self.tv.mute()
        assert convert_details(self.tv)["volume"] == start_volume + 1

        # Off, mute
        self.tv.power()
        self.tv.mute()
        assert convert_details(self.tv)["volume"] == start_volume + 1

        # Off, unmute
        self.tv.mute()
        assert convert_details(self.tv)["volume"] == start_volume + 1

    def test_channel_up(self):
        self.tv.__init__()
        start_channel = convert_details(self.tv)["channel"]

        # Off, channel increase
        self.tv.channel_up()
        assert convert_details(self.tv)["channel"] == start_channel

        # On, channel increase
        self.tv.power()
        self.tv.channel_up()
        assert convert_details(self.tv)["channel"] == start_channel + 1

        # increase channel until we loop back
        for i in range(0, Television.MAX_CHANNEL - start_channel):
            self.tv.channel_up()
        assert convert_details(self.tv)["channel"] == Television.MIN_CHANNEL

    def test_channel_down(self):
        self.tv.__init__()
        # Television.MIN_CHANNEL
        start_channel = convert_details(self.tv)["channel"]

        # Off, channel decrease past minimum
        self.tv.channel_down()
        assert convert_details(self.tv)["channel"] == start_channel

        # On, channel decrease past minimum
        self.tv.power()
        self.tv.channel_down()
        assert convert_details(self.tv)["channel"] == Television.MAX_CHANNEL

    def test_volume_up(self):
        self.tv.__init__()
        # Television.MIN_VOLUME
        start_vol = convert_details(self.tv)["volume"]

        # Off, volume up
        self.tv.volume_up()
        assert convert_details(self.tv)["volume"] == start_vol

        # On, volume up
        self.tv.power()
        self.tv.volume_up()
        assert convert_details(self.tv)["volume"] == start_vol + 1

        # On, mute, volume up
        self.tv.mute()
        self.tv.volume_up()
        assert convert_details(self.tv)["volume"] == start_vol + 2

        # Increase volume past max
        for i in range(0, Television.MAX_VOLUME + 1):
            self.tv.volume_up()
        assert convert_details(self.tv)["volume"] == Television.MAX_VOLUME

    def test_volume_down(self):
        self.tv.__init__()

        start_vol = convert_details(self.tv)["volume"]

        # Off, volume down
        self.tv.volume_down()
        assert convert_details(self.tv)["volume"] == Television.MIN_VOLUME

        # On, volume high, and decreased
        self.tv.power()
        for i in range(0, Television.MAX_VOLUME):
            self.tv.volume_up()
        self.tv.volume_down()
        assert convert_details(self.tv)["volume"] == Television.MAX_VOLUME - 1

        # On, muted, decreased
        self.tv.mute()
        self.tv.volume_down()
        assert convert_details(self.tv)["volume"] == Television.MAX_VOLUME - 2

        # On, decreased past min
        for i in range(0, Television.MAX_VOLUME+1):
            self.tv.volume_down()
        assert convert_details(self.tv)["volume"] == Television.MIN_VOLUME
