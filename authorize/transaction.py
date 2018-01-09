from authorize import Configuration


class Transaction(object):

    @staticmethod
    def sale(params={}):
        return Configuration.api.transaction.sale(params)

    @staticmethod
    def auth(params={}):
        return Configuration.api.transaction.auth(params)

    @staticmethod
    def settle(transaction_id, amount=None):
        return Configuration.api.transaction.settle(transaction_id, amount)

    @staticmethod
    def credit(params={}):
        return Configuration.api.transaction.credit(params)

    @staticmethod
    def auth_continue(params={}):
        return Configuration.api.transaction.auth_continue(params)

    @staticmethod
    def sale_continue(params={}):
        return Configuration.api.transaction.sale_continue(params)

    @staticmethod
    def refund(params={}):
        return Configuration.api.transaction.refund(params)

    @staticmethod
    def void(transaction_id):
        return Configuration.api.transaction.void(transaction_id)

    @staticmethod
    def details(transaction_id):
        return Configuration.api.transaction.details(transaction_id)

    @staticmethod
    def list(batch_id=None):
        return Configuration.api.transaction.list(batch_id)

    @staticmethod
    def list_by_customer(customer_id, **kwargs):
        return Configuration.api.transaction.list_by_customer(customer_id, **kwargs)
