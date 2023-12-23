class Player:
    __slots__ = ['team', 'id', 'x', 'y']
    def __init__(self, player_list):
        self.team = Team(player_list[0])
        self.id = player_list[1]
        self.x = player_list[2]
        self.y = player_list[3]

class Ball:
    __slots__ = ['x', 'y', 'r']
    def __init__(self, ball_list):
        self.x = ball_list[2]
        self.y = ball_list[3]
        self.r = ball_list[4]

class Team:
    __slots__ = ['id']

    def __init__(self, id):
        self.id = id

class Moment:
    __slots__ = ['quarter', 'game_clock', 'shot_clock', 'ball', 'players']
    def __init__(self, moment_list):
        self.quarter = moment_list[0]
        self.game_clock = moment_list[2]
        self.shot_clock = moment_list[3]
        self.ball = Ball(moment_list[5][0])
        self.players = [Player(player) for player in moment_list[5][1:]]

class Event:
    def __init__(self, event):
        moments = event['moments']
        self.moments = [Moment(moment) for moment in moments]
        home_players = event['home']['players']
        guest_players = event['visitor']['players']
        players = home_players + guest_players
        player_ids = [player['playerid'] for player in players]
        player_names = [" ".join([player['firstname'],
                        player['lastname']]) for player in players]
        player_jerseys = [player['jersey'] for player in players]
        values = list(zip(player_names, player_jerseys))

        self.player_ids_dict = dict(zip(player_ids, values))

class Game:
    __slots__ = ['gameid', 'gamedate', 'events']
    def __init__(self, tracking_data):
        self.gameid = tracking_data.iloc[0]['gameid']
        self.gamedate = tracking_data.iloc[0]['gamedate']
        self.events = [Event(event) for event in tracking_data['events']]