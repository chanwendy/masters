class GameStats():
    def __init__(self, m_setting):
        self.m_setting = m_setting
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.m_setting.ship_limit
