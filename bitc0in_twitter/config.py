from pathlib import Path
import toml


class Configuration:
    def __init__(self, config_path):
        assert isinstance(config_path, Path), "must be a Path type."
        self.config_path = config_path
        self.general = dict()
        self.bullish = dict()
        self.bearish = dict()

    @property
    def config_file_path(self):
        return self.config_path / "config.toml"

    def load_config(self):
        if not self.config_file_path.exists():
            print(f"{self.config_file_path} not found.")
            self.config_file_path.touch()
            self.create_new_config()

        with open(str(self.config_file_path), "r") as f:
            data = toml.loads(f.read())

        try:
            self.general = data["GENERAL"]
            self.bullish = data["BULLISH"]
            self.bearish = data["BEARISH"]

        except KeyError:
            self.create_new_config()

    def create_new_config(self):
        general = dict()
        bullish = dict()
        bearish = dict()
        general["twitter_name"] = ""
        general["update_interval"] = "1H"

        bullish["twitter_name_bullish_suffix"] = "[PUMPIT]"
        bullish["twitter_bullish_description"] = "To the moon!!!!"
        bullish["twitter_bullish_profile_color"] = "#00AA00"

        bearish["twitter_name_bearish_suffix"] = "[DUMPIT]"
        bearish["twitter_bearish_description"] = "Should have sold. :("
        bearish["twitter_bearish_profile_color"] = "#AA0000"

        data = dict()
        data["GENERAL"] = general
        data["BULLISH"] = bullish
        data["BEARISH"] = bearish

        with open(str(self.config_file_path), "w") as f:
            f.write(toml.dumps(data))


c = Path("")
config = Configuration(c)
config.load_config()
# config.create_new_config()
