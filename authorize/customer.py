from authorize import Configuration


class Customer(object):

    @staticmethod
    def create(params={}):
        return Configuration.api.customer.create(params)

    @staticmethod
    def from_transaction(transaction_id, params={}):
        return Configuration.api.customer.from_transaction(transaction_id, params)

    @staticmethod
    def details(customer_id=None, merchant_id=None):
        if customer_id is None and merchant_id is None:
            raise TypeError(
                'You must specify either the '
                '`customer_id` or `merchant_id`'
            )

        return Configuration.api.customer.details(customer_id, merchant_id)

    @staticmethod
    def update(customer_id, params={}):
        return Configuration.api.customer.update(customer_id, params)

    @staticmethod
    def delete(customer_id):
        return Configuration.api.customer.delete(customer_id)

    @staticmethod
    def list():
        return Configuration.api.customer.list()
