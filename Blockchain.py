# This class is responsible for managing the chain
# Create a genesis block!

import hashlib
import json # JavaScript Object Notation
# JSON most common data format used in web APIs
# Faster data transmission than XML

from time import time
from uuid import uuid4
from textwrap import dedent

from flask import Flask, jsonify, request

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : time(),
            'transaction' : self.current_transactions,
            'proof' : proof,
            'previous_hash' : previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount=0):
        self.current_transactions.append({
            'Sender' : sender,
            'Recipient' : recipient,
            'Amount' : amount
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Will create a SHA-256 hash of a Block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Returns previous block in the chain
        self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof
    
    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'
    
app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()

@app.route("/", methods=['GET'])
def home():
    return "hello world!"

@app.route("/kill", methods=['GET', 'POST'])
def killSwitch():
    global exiting
    return

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = blockchain.last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    blockchain.new_transaction(sender='0', recipient=node_identifier, amount=1)
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message' : 'New Block Created',
        'index' : block['index'],
        'transactions' : block['transactions'],
        'proof' : block['proof'],
        'previous_hash' : block['previous_hash']
    }

    return jsonify(response), 200

# Method for creating transactions
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all (k in values for k in required):
        return 'Missing values', 400

    # Creating new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message' : f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain' : blockchain.chain,
        'length' : len(blockchain.chain)
    }
    return jsonify(response), 200 # Converts Python data structures into a JSON response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5600)