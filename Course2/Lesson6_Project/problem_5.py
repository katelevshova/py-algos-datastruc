"""
TASK5:
Blockchain

A Blockchain is a sequential chain of records, similar to a linked list.
Each block contains some information and how it is connected related to the other blocks in the chain.
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.
For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created,
and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.

"""
"""
NOTE:
A blockchain is essentially a linked list that contains ordered data, 
with a few constraints such as:

    Blocks can’t be modified once added; in other words, it is append only.
    There are specific rules for appending data to it.
    Its architecture is distributed.
"""
# USED sources: https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/

import hashlib
import time


class Block:

    def __init__(self, _index, _timestamp, _data, _previous_hash, _nonce=0):
        self.index = _index
        self.timestamp = _timestamp
        self.data = _data
        self.previous_hash = _previous_hash  # to ensure immutability of the entire blockchain
        self.hash = self.calc_hash()
        print("Block hash=" + self.hash)
        self.nonce = _nonce  # value that starts with a certain number of zero bits when hashed

    def calc_hash(self):
        #sha = hashlib.sha256()
        #hash_str = "We are going to encode this string of data!".encode('utf-8')
        hash_str = "We are going to encode this string of data!"
        # sha.update(hash_str)
        # return sha.hexdigest()
        return hashlib.sha256(hash_str.encode('utf-8')).hexdigest()


class Blockchain:
    difficulty = 2  # The number of leading zero bits

    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []  # store the data of each transaction
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Is used to initialize the blockchain.
        Creates an initial block with an index of 0 and a previous hash of 0.
        """
        genesis_block = Block(0, time.time(), "Some information", "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    '''
    The average work required to create a block increases exponentially with the number 
    of leading zero bits, and therefore, by increasing the difficulty with each new block,
    we can sufficiently prevent users from modifying previous blocks, 
    since it is practically impossible to redo the following blocks and catch up to others.
    '''

    def proof_of_work(self, block: Block):
        print("->proof_of_work: block.nonce= " + str(block.nonce))
        computed_hash = block.calc_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):  # '00' if difficulty=2
            block.nonce += 1
            print("in while: block.nonce= " + str(block.nonce))
            computed_hash = block.calc_hash()
        return computed_hash

    def add_block(self, block: Block, proof):
        prev_hash = self.get_last_block().hash
        if prev_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        return block_hash.startswith('0' * Blockchain.difficulty) and block_hash == block.calc_hash()

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        if not self.unconfirmed_transactions:
            return False

        last_block = self.get_last_block()
        print("->mine: last_block.index={}".format(last_block.index))

        new_block = Block(last_block.index + 1, self.unconfirmed_transactions, time.time(), last_block.hash)
        print("new_block.index={}".format(new_block.index))

        proof = self.proof_of_work(new_block)
        print("proof=" + str(proof))

        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index


def test_create_genesis_block():
    print("->test_create_genesis_block: start")
    blockchain = Blockchain()
    assert len(blockchain.chain) == 1
    assert blockchain.get_last_block().index == 0
    assert blockchain.get_last_block().data == "Some information"
    assert blockchain.get_last_block().previous_hash == "0"
    # assert blockchain.is_valid_proof(blockchain.get_last_block(), blockchain.get_last_block().hash)
    print("->test_create_genesis_block: end")


def test_mine():
    print("->test_mine: start")
    blockchain = Blockchain()
    blockchain.add_new_transaction("1_This is new transaction data")
    blockchain.add_new_transaction("2_This is new transaction data")
    # blockchain.mine()

    print("->test_mine: end")


def test():
    test_create_genesis_block()
    test_mine()


test()
