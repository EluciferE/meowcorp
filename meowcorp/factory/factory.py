from telegram.branches import branches
from telegram.callbacks import callbacks

from meowcorp.handlers import args_validation


class Factory:
    def __init__(self, db):
        self.db = db

    async def process_branch(self, user, message):
        for branch in branches:
            if branch.status.match(user=user):
                worker = branch(user, self.db, message)
                args = args_validation.prepare_args(worker, self.db, user=user)
                await worker.work(*args)
                return

    async def process_callback(self, user, call):
        for callback in callbacks:
            if callback.status.match(call=call):
                worker = callback(user, self.db, call)
                args = args_validation.prepare_args(worker, self.db, call=call)
                await worker.work(*args)
                return
