

from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

bdb = BigchainDB(
    'https://test.bigchaindb.com',
    headers={'app_id': '64acf62a',
             'app_key': '3b1e2c3b228caf4b9f9a036f1478b4dd'})
i=0
while(i<50):
	alice = generate_keypair()
	tx = bdb.transactions.prepare(operation='CREATE', signers=alice.public_key,asset={'data': {'message': 'keyur'}})
	signed_tx = bdb.transactions.fulfill(tx,private_keys=alice.private_key)
	bdb.transactions.send(signed_tx)
	print(signed_tx['id'])
	print(bdb.transactions.status(signed_tx['id']))
	print(i)
	i=i+1
