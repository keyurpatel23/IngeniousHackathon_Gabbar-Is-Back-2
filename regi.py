from tkinter import *
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

fields = 'First Name', 'Last Name', 'Email', 'Mobile no','Password','Confirm Password'

#def fetch(entries):
#   for entry in entries:
#      field = entry[0]
#      text  = entry[1].get()
#      print('%s: "%s"' % (field, text)) 
def con(entries):
	bdb = BigchainDB('https://test.bigchaindb.com',headers={'app_id': '64acf62a','app_key': '3b1e2c3b228caf4b9f9a036f1478b4dd'})
	i=0
	while(i<1):
		alice = generate_keypair()
		print(type(entries))
		x="keyur"
		tx = bdb.transactions.prepare(operation='CREATE', signers=alice.public_key,asset={'data': {'message': x}})
		signed_tx = bdb.transactions.fulfill(tx,private_keys=alice.private_key)
		bdb.transactions.send(signed_tx)
		print(signed_tx['id'])
		print(bdb.transactions.status(signed_tx['id']))
		print(i)
		i=i+1

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   print('dsdsaafdafdafdff',ents)
   root.bind('<Return>', (lambda event, e=ents: con(e)))   
   b1 = Button(root, text='Show',
          command=(lambda e=ents: con(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
