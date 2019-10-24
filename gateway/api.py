import requests
import asyncio
import r6sapi as api


class Api:
    def __init__(self, game, player, platform):
        self.game = game
        self.player = player
        self.platform = platform
        self.headers = {'TRN-Api-Key': '4fbe2f49-1452-4167-8bd1-65ab373dcdb5'}

    def _build_request(self):
        if self.game == 'overwatch':
            return Overwatch
        elif self.game == 'fortnite':
            return Fortnite
        elif self.game == 'pubg':
            return Pubg
        else:
            raise Exception('')

    def get_data(self):
        game_api = self._build_request()
        game = game_api(self.player, self.platform)
        game.call(self.headers)
        self.request = game.request
        
    def _validate_request(self):
        if self.request.status_code >= 200 and self.request.status_code < 400:
            return True
        else:
            return False




class R6:
    def __init__(self):
        self.fake = None

    def a(self):
        async def run():
            auth = api.Auth("chris.lewis831@gmail.com", "e2Z2#RRfL@pYPx.")
            
            player = await auth.get_player("billy_yoyo", api.Platforms.UPLAY)
            operator = await player.get_operator("sledge")
            print(operator.kills)

            await auth.close()
            
        asyncio.get_event_loop().run_until_complete(run())
        


class Overwatch:
    def __init__(self, player, platform):
        self.player = player
        self.platform = platform

    def _format_params(self):
        platform_choices = ['battlenet', 'psn', 'xbl']

    def call(self, headers):
        self.request = requests.get(f'https://public-api.tracker.gg/v2/overwatch/standard/profile/{self.platform}/{self.player}', headers)


class Fortnite:
    def __init__(self, player, platform):
        self.player = player
        self.platform = platform

    def _format_params(self):
        platform_choices = ['pc', 'xbl', 'psn']

    def call(self):
        # Likely needs to be switched over to use http.client because tracker api redirect drops the auth in the header.
        #self.request = requests.get(f'https://api.fortnitetracker.com/v1/profile/{self.platform}/{self.player}', self.headers)
        pass


class Pubg:
    def __init__(self, player, platform):
        self.player = player
        self.platform = platform
        self.api_key = """eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.
        eyJqdGkiOiJkZTFjMjBkMC1hMDU5LTAxMzctOTg3Zi00N2ZiNGVlMjNhYjEiLCJpc3MiOiJ
        nYW1lbG9ja2VyIiwiaWF0IjoxNTY1NzQzMTU1LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIj
        oicHViZyIsImFwcCI6ImNocmlzLWxld2lzODMxIn0.rAoJb52ml7d-ORY8Mp5MFwy_yABkW
        Rbx67FjtMr1ex0
        """

        self.headers = {
        'Authorization': f'Bearer {self.api_key}',
        'Accept': 'application/vnd.api+json'}

    def _format_params(self):
        platform_choices = ['steam', 'kakao', 'psn', 'tournament', 'xbox']

    def call(self):
        self.request = requests.get(f"https://api.pubg.com/shards/{self.platform}/players?filter[playerNames]={self.player_id}", headers=self.headers)


class R6:
    def __init__(self):
        pass