from unittest import TestCase
import qhangups.oauth2_helper

class TestGoogleOauth2Helper(TestCase):
    def test_checkTitle(self):
        successTitles = ["Success code=4/v6xr77ewYqhvHSyW6UJ1w7jKwAzu",
                 "Success code=4/v6xr77ewYqhvHSyW6UJ1w7jKwAzu&abc=zyz",
                 "Success abc=xyz&code=4/v6xr77ewYqhvHSyW6UJ1w7jKwAzu"]
        expectedStatus = "Success"
        expectedVar = "code"
        expectedVal = "4/v6xr77ewYqhvHSyW6UJ1w7jKwAzu"
        for title in successTitles:
            res = qhangups.oauth2_helper.parseOAuth2Title(title)
            self.assertEquals(expectedStatus, res[0])
            self.assertEquals(expectedVal, res[1][expectedVar])
