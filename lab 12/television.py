class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initialize the television."""
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Turn the television on or off."""
        self._status = not self._status

    def mute(self) -> None:
        """Mute or unmute the television when it is on."""
        if self._status:
            self._muted = not self._muted

    def channel_up(self) -> None:
        """Increase the channel when the television is on."""
        if self._status:
            if self._channel == Television.MAX_CHANNEL:
                self._channel = Television.MIN_CHANNEL
            else:
                self._channel += 1

    def channel_down(self) -> None:
        """Decrease the channel when the television is on."""
        if self._status:
            if self._channel == Television.MIN_CHANNEL:
                self._channel = Television.MAX_CHANNEL
            else:
                self._channel -= 1

    def volume_up(self) -> None:
        """Increase volume and unmute if necessary."""
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self) -> None:
        """Decrease volume and unmute if necessary."""
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:
        """Return the television's current settings."""
        return f"Power = [{self._status}], Channel = [{self._channel}], Volume = [{self._volume}]"
