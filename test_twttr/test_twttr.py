from twttr import shorten

def test_str():
    assert shorten("rauShAn") == "rShn"
def test_mixed():
    assert shorten("RaUsHAN1234, ';@#$% !?") == "RsHN1234, ';@#$% !?"
# 18002021234 samsung pickup 