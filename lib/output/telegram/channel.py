import requests

from lib.output.base.base_output import BaseOutput

CHANNEL_URI = "https://api.telegram.org/bot{}/sendMessage?parse_mode=markdown&chat_id={}&text={}"

class TelegramChannelOutput(BaseOutput):
    def __init__(self, chat_id=None, bot_key=None):
        self._chat_id = chat_id
        self._bot_key = bot_key

        super(TelegramChannelOutput, self).__init__()

    def output(self, content, *args, **kwargs):
        requests.get(CHANNEL_URI.format(self._bot_key, self._chat_id, content))