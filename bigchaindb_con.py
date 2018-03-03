

from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

bdb = BigchainDB(
    'https://test.bigchaindb.com',
    headers={'app_id': '64acf62a',
             'app_key': '3b1e2c3b228caf4b9f9a036f1478b4dd'})
trials = 0
while (trials < 150):
	
	try:

		alice = generate_keypair()
		prepared_creation_tx = bdb.transactions.prepare(operation='CREATE',signers=alice.public_key,asset={'data': {'message': 'hello 			testing creating'}})
		fulfilled_creation_tx = bdb.transactions.fulfill(prepared_creation_tx,private_keys=alice.private_key)
		sent_creation_tx = bdb.transactions.send(fulfilled_creation_tx)

		txid = fulfilled_creation_tx['id']
		print(txid)

		print(trials)
		
		if (bdb.transactions.status(txid).get('status') == 'valid'):
			print(txid)
			print(sent_creation_tx == fulfilled_creation_tx)
			break
			
	except e:
		print(e)
		print('not valid')
		
	trials=trials+1





print(bdb.transactions.status(fulfilled_creation_tx['id']))
