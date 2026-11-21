from television import Television
def test_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert tv._muted == True
    tv.mute()
    assert tv._muted == False
    tv = Television()
    tv.power()
    tv.mute()
    tv.power()
    assert tv._muted == True
    tv.mute()
    assert tv._muted == True
    tv = Television()
    tv.power()
    tv.power()
    assert tv._muted == False
    tv.mute()
    assert tv._muted == False