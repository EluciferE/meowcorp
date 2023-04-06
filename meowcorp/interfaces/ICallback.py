from __future__ import annotations
from abc import ABC, abstractmethod
from aiogram import Bot
from meowcorp.status.status import STATUS
from aiogram.types import CallbackQuery
from models import User, Session
from os import getenv


class Callback(ABC):
    """
    :param status: attr from STATUS_CALLBACK
    """
    status: STATUS

    def __init__(self, user: User, db: Session, call: CallbackQuery):
        """
        Interface for worker of Callback
        All work with telegram goes throw self.bot

        :param user: Current user
        :param db: Current DB session for user
        :param call: Current CallbackQuery
        """
        self.bot: Bot = Bot(token=getenv('BOT_TOKEN'))
        self.user: User = user
        self.db: Session = db
        self.call: CallbackQuery = call

    @classmethod
    def from_callback(cls, callback: Callback) -> Callback:
        return cls(
            user=callback.user,
            db=callback.db,
            call=callback.call
        )

    @abstractmethod
    async def work(self, *args, **kwargs):
        """
        Handler of current CallbackQuery

        :return: None
        """
        pass
