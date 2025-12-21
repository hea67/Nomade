# ============================================================
# Group Manager Bot
# Author: LearningBotsOfficial (https://github.com/LearningBotsOfficial) 
# Support: https://t.me/LearningBotsCommunity
# Channel: https://t.me/learning_bots
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================

from .start import register_handlers
from .group_commands import register_group_commands

def register_all_handlers(app):
    register_handlers(app)
    register_group_commands(app)
    print("✅ Group commands registered!")
from handlers.id import register_id_handler

def register_all_handlers(app):
    register_id_handler(app)
from handlers.owner import register_owner_handler
register_owner_handler(app)
from handlers.forcejoin import register_forcejoin_handler
register_forcejoin_handler(app)
