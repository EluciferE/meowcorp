from __future__ import annotations
from abc import ABC, abstractmethod
from aiogram import Bot
from meowcorp.status.status import STATUS
from aiogram.types import Message
from models import User, Session
from os import getenv


class Branch(ABC):
    """
    :param status: attr from STATUS_BRANCH
    """
    status: STATUS

    def __init__(self, user: User, db: Session, message: Message):
        """
        Interface for worker of Branch
        All work with telegram goes throw self.bot

        :param user: Current user
        :param db: Current DB session for user
        :param message: Current message
        """
        self.bot: Bot = Bot(token=getenv('BOT_TOKEN'))
        self.user: User = user
        self.db: Session = db
        self.message: Message = message

    @classmethod
    def from_branch(cls, branch: Branch) -> Branch:
        return cls(
            user=branch.user,
            db=branch.db,
            message=branch.message
        )

    @abstractmethod
    async def work(self, *args, **kwargs):
        """
        Handler of current branch

        :return: None
        """
        pass
