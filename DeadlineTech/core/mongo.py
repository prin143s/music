

# ==========================================================
# 🎧 Public Open-Source VC Player Music Bot (Cookies Based)
# 🛠️ Maintained by Team DeadlineTech | Lead Developer: @Its_damiann
# 🔓 Licensed for Public Use — All Rights Reserved © Team DeadlineTech
#
# This file is part of a publicly available and open-source Telegram music bot
# developed by Team DeadlineTech. It offers high-quality streaming in Telegram voice
# chats using YouTube as a source, supported by session-based assistant accounts and
# YouTube cookie integration for improved access and performance.
#
# 💡 This source code is released for educational and community purposes. You're free
# to study, modify, and deploy it under fair and respectful usage. However, any misuse,
# removal of credits, or false ownership claims will be considered a violation of our
# community standards and may lead to denial of support or blacklisting.
#
# 🔗 Looking for powerful performance with stable APIs? Get access to the official
# premium API service: https://DeadlineTech.site
#
# ❤️ Openly built for the community, but proudly protected by the passion of its creators.
# ==========================================================




from motor.motor_asyncio import AsyncIOMotorClient
from ..logging import LOGGER

MONGO_DB_URI = "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority"

LOGGER(__name__).info("⏳ Establishing a secure link to your MongoDB database...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.deadline
    LOGGER(__name__).info("✅ Successfully connected to MongoDB. All systems are ready!")
except:
    LOGGER(__name__).error("❌ MongoDB connection failed!")
    exit()
