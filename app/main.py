from pydantic import BaseSettings
from pymongo import MongoClient


class Settings(BaseSettings):
    mongodb_uri: str
    mongodb_name: str

    class Config:
        env_file = ".env.dev"


if __name__ == "__main__":
    settings = Settings()
    mongo_client = MongoClient()
